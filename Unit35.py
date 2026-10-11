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

motion=np.zeros((15,15))
motion[7,:]=1
motion/=15

motion_blur=cv2.filter2D(img,-1,motion)

gaussian=cv2.GaussianBlur(img,(15,15),0)

noise=np.random.normal(0,20,img.shape)

degraded=np.clip(gaussian+noise,0,255).astype(np.uint8)

estimate=cv2.fastNlMeansDenoisingColored(degraded)

imgs=[
img,
motion_blur,
gaussian,
degraded,
estimate
]

titles=[
"Original",
"Motion",
"Gaussian",
"Degraded",
"Estimated"
]

result=[]

for t,i in zip(titles,imgs):
    temp=i.copy()
    cv2.putText(temp,t,(10,25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,(0,0,255),2)
    result.append(temp)

output=create_image_grid(result,cols=2,space=20,bg_color=[255,255,255])

cv2.imshow("Degradation & Estimation",output)
cv2.waitKey(0)
cv2.destroyAllWindows()