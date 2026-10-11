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

img=cv2.imread("sample.jpg")
img=cv2.resize(img,(300,300))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary=cv2.threshold(
gray,0,255,
cv2.THRESH_BINARY+cv2.THRESH_OTSU)

num,labels=cv2.connectedComponents(binary)

color=np.zeros_like(img)

for i in range(1,num):
    color[labels==i]=np.random.randint(0,255,3)

contours,_=cv2.findContours(
binary,
cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)

representation=img.copy()

cv2.drawContours(
representation,
contours,-1,
(0,255,0),2)

imgs=[
img,
cv2.cvtColor(binary,cv2.COLOR_GRAY2BGR),
representation,
color
]

titles=[
"Original",
"Binary",
"Representation",
"Regions"
]

result = []

header_height = 40

for t, i in zip(titles, imgs):
    # White header
    header = np.full((header_height, i.shape[1], 3), 255, dtype=np.uint8)

    # Calculate text size to center it
    (tw, th), _ = cv2.getTextSize(
        t,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        2
    )

    x = (i.shape[1] - tw) // 2
    y = (header_height + th) // 2

    cv2.putText(
        header,
        t,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # Stack title and image vertically
    temp = np.vstack((header, i))
    result.append(temp)

output = create_image_grid(
    result,
    cols=2,
    space=20,
    bg_color=[255, 255, 255]
)

cv2.imshow("Region Segmentation",output)
cv2.waitKey(0)
cv2.destroyAllWindows()