import cv2
import numpy as np
from scipy.ndimage import minimum_filter, maximum_filter




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



img=cv2.imread("sample.jpg",0)
img=cv2.resize(img,(250,250))

arith=cv2.blur(img,(5,5))

geo=np.exp(cv2.blur(np.log(img.astype(np.float32)+1),(5,5)))
geo=np.uint8(geo)

harm=25/(cv2.blur(1/(img.astype(np.float32)+1),(5,5)))
harm=np.uint8(harm)

Q=1.5
num=cv2.blur(np.power(img.astype(np.float32),Q+1),(5,5))
den=cv2.blur(np.power(img.astype(np.float32),Q),(5,5))
contra=np.uint8(num/(den+1))

median=cv2.medianBlur(img,5)

minimum=minimum_filter(img,size=5)
maximum=maximum_filter(img,size=5)

mid=((minimum.astype(int)+maximum.astype(int))/2).astype(np.uint8)

imgs=[
img,arith,geo,harm,
contra,median,minimum,
maximum,mid
]

titles=[
"Original","Arithmetic","Geometric",
"Harmonic","Contra",
"Median","Min","Max","Mid"
]

rows=[]

for t,i in zip(titles,imgs):
    i=cv2.cvtColor(i,cv2.COLOR_GRAY2BGR)
    cv2.putText(i,t,(10,20),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.45,(0,0,255),2)
    rows.append(i)

top = cv2.hconcat(rows[:3])
middle = cv2.hconcat(rows[3:6])
bottom = cv2.hconcat(rows[6:])

output = create_image_grid([top, middle, bottom], cols=1, space=20, bg_color=[255,255,255])

cv2.imshow("Mean Filters",output)
cv2.waitKey(0)
cv2.destroyAllWindows()