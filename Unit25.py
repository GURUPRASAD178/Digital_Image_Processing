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

lap=cv2.Laplacian(gray,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))

sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobelx=np.uint8(np.absolute(sobelx))

sobely=cv2.Sobel(gray,cv2.CV_64F,0,1)
sobely=np.uint8(np.absolute(sobely))

blur=cv2.GaussianBlur(gray,(9,9),5)

unsharp=cv2.addWeighted(gray,1.5,blur,-0.5,0)

imgs=[
cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR),
cv2.cvtColor(lap,cv2.COLOR_GRAY2BGR),
cv2.cvtColor(sobelx,cv2.COLOR_GRAY2BGR),
cv2.cvtColor(sobely,cv2.COLOR_GRAY2BGR),
cv2.cvtColor(unsharp,cv2.COLOR_GRAY2BGR)
]

titles=[
"Original",
"Laplacian",
"Sobel X",
"Sobel Y",
"Unsharp"
]

result=[]

for t,i in zip(titles,imgs):
    temp=i.copy()
    cv2.putText(temp,t,(10,25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,(0,0,255),2)
    result.append(temp)

output=create_image_grid(result,cols=2,space=20,bg_color=[255,255,255])

cv2.imshow("Sharpening & Spatial Enhancement",output)
cv2.waitKey(0)
cv2.destroyAllWindows()