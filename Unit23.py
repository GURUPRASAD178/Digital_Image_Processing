import cv2
import numpy as np
import matplotlib.pyplot as plt


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
img=cv2.resize(img,(300,300))

equal=cv2.equalizeHist(img)

reference=cv2.GaussianBlur(img,(31,31),0)
matched=cv2.equalizeHist(reference)

display=create_image_grid([cv2.cvtColor(img,cv2.COLOR_GRAY2BGR),
                           cv2.cvtColor(equal,cv2.COLOR_GRAY2BGR),      
                            cv2.cvtColor(matched,cv2.COLOR_GRAY2BGR)],cols=3,space=20,bg_color=[255,255,255])

cv2.putText(display,"Original",(40,45),0,0.8,(0,0,255),2)
cv2.putText(display,"Equalized",(340,45),0,0.8,(0,0,255),2)
cv2.putText(display,"Matched",(680,45),0,0.8,(0,0,255),2)

cv2.imshow("Histogram Processing",display)

plt.figure(figsize=(10,4))

plt.subplot(131)
plt.hist(img.ravel(),256,[0,256])
plt.title("Original")

plt.subplot(132)
plt.hist(equal.ravel(),256,[0,256])
plt.title("Equalized")

plt.subplot(133)
plt.hist(matched.ravel(),256,[0,256])
plt.title("Matched")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()