import cv2
import numpy as np



# ==========================================
# REUSABLE HELPER FUNCTION FOR SPACING/GRIDS
# ==========================================
def create_image_grid(images, cols=4, space=10, bg_color=[255, 255, 255]):
    """
    Combines a list of same-sized images into a grid with background spacing.
    Works for any number of images, single rows, or multi-row grids.
    """
    if not images:
        return None
        
    h, w, c = images[0].shape
    
    # Calculate how many rows we need
    rows = int(np.ceil(len(images) / cols))
    
    # Calculate total dimensions of the final canvas including spacing
    total_w = (cols * w) + ((cols + 1) * space)
    total_h = (rows * h) + ((rows + 1) * space)
    
    # Create the empty background canvas
    canvas = np.full((total_h, total_w, c), bg_color, dtype=np.uint8)
    
    # Paste each image onto the canvas at the correct coordinate
    for idx, img in enumerate(images):
        r = idx // cols
        c_idx = idx % cols
        
        y_offset = space + r * (h + space)
        x_offset = space + c_idx * (w + space)
        
        canvas[y_offset:y_offset+h, x_offset:x_offset+w] = img
        
    return canvas

img = cv2.imread("sample.jpg", 0)
img = cv2.resize(img, (200, 200))

planes = []

for i in range(8):
    plane = ((img >> i) & 1) * 255
    plane = plane.astype(np.uint8)
    plane = cv2.cvtColor(plane, cv2.COLOR_GRAY2BGR)
    cv2.putText(plane,
                f"Bit {i}",
                (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2)
    planes.append(plane)

# --- 1. Define Spacer Dimensions & Color ---
space_width = 20   # Gap between columns
space_height = 20  # Gap between rows
spacer_color = [255, 255, 255]  # White spacer (use [0, 0, 0] for black)

# --- 2. Create the Spacers ---
# Vertical spacer goes between columns (same height as image: 200)
v_spacer = np.full((200, space_width, 3), spacer_color, dtype=np.uint8)

# --- 3. Concatenate Rows with Spacers ---
# Inject v_spacer between each image in the row
top = cv2.hconcat([planes[0], v_spacer, planes[1], v_spacer, planes[2], v_spacer, planes[3]])
bottom = cv2.hconcat([planes[4], v_spacer, planes[5], v_spacer, planes[6], v_spacer, planes[7]])

# --- 4. Create the Horizontal Spacer ---
# This goes between the top and bottom rows.
# Its width must match the exact total width of the 'top' row.
h_spacer = np.full((space_height, top.shape[1], 3), spacer_color, dtype=np.uint8)

# --- 5. Final Stack ---
output = create_image_grid([top, bottom], cols=1, space=space_height, bg_color=spacer_color)

cv2.imshow("Bit Plane Slicing", output)
cv2.waitKey(0)
cv2.destroyAllWindows()