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

img = cv2.imread("sample.jpg",0)

_,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

pixels = binary.flatten()

encoded=[]

count=1

for i in range(1,len(pixels)):
    if pixels[i]==pixels[i-1]:
        count+=1
    else:
        encoded.append((pixels[i-1],count))
        count=1

encoded.append((pixels[-1],count))

original_size=len(pixels)
compressed_size=len(encoded)*2

print("Original Pixels :",original_size)
print("Encoded Length :",len(encoded))
print("Approx Compressed Size :",compressed_size)

print("\nFirst 30 Encoded Values\n")
print(encoded[:30])

cv2.imshow("Original",img)
cv2.imshow("Binary Image",binary)

cv2.waitKey(0)
cv2.destroyAllWindows()