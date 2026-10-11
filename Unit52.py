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

img = cv2.imread("sample.jpg")
img = cv2.resize(img,(300,300))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)/255.0

# DCT
dct = cv2.dct(gray)
dct_display = cv2.normalize(np.log(np.abs(dct)+1),
None,0,255,cv2.NORM_MINMAX)
dct_display = np.uint8(dct_display)
dct_display = cv2.cvtColor(dct_display,cv2.COLOR_GRAY2BGR)

# Predictive Coding
pred = cv2.absdiff(img[:,1:],img[:,:-1])
pred = cv2.copyMakeBorder(pred,0,0,1,0,cv2.BORDER_CONSTANT)

# JPEG Compression
cv2.imwrite("q100.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,100])
cv2.imwrite("q50.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imwrite("q20.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,20])

q100 = cv2.imread("q100.jpg")
q50 = cv2.imread("q50.jpg")
q20 = cv2.imread("q20.jpg")

def label(im,text):
    image = im.copy()
    cv2.putText(image,text,(10,25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,(0,0,255),2)
    return image

imgs = [
    label(img, "Original"),
    label(q100, "JPEG Quality 100"),
    label(q50, "JPEG Quality 50"),
    label(q20, "JPEG Quality 20")
]

output = create_image_grid(
    imgs,
    cols=2,
    space=20,
    bg_color=[255,255,255]
)

cv2.imshow("Compression Techniques",output)
cv2.waitKey(0)
cv2.destroyAllWindows()