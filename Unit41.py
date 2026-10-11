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

# Point Detection
point_kernel = np.array([[-1,-1,-1],
                         [-1, 8,-1],
                         [-1,-1,-1]])

point = cv2.filter2D(gray,-1,point_kernel)

# Line Detection
line_kernel = np.array([[-1,-1,-1],
                        [ 2, 2, 2],
                        [-1,-1,-1]])

line = cv2.filter2D(gray,-1,line_kernel)

# Edge Detection
edge = cv2.Canny(gray,100,200)

# ==========================
# EDGE DETECTION OPERATORS
# ==========================

# Roberts Operator
kernel_rx = np.array([[1, 0],
                      [0,-1]], dtype=np.float32)

kernel_ry = np.array([[0, 1],
                      [-1,0]], dtype=np.float32)

roberts_x = cv2.filter2D(gray, cv2.CV_32F, kernel_rx)
roberts_y = cv2.filter2D(gray, cv2.CV_32F, kernel_ry)

roberts = cv2.convertScaleAbs(
    cv2.addWeighted(
        cv2.convertScaleAbs(roberts_x),
        0.5,
        cv2.convertScaleAbs(roberts_y),
        0.5,
        0
    )
)

# -----------------------------
# PREWITT
# -----------------------------

prewitt_x_kernel = np.array([
    [-1,0,1],
    [-1,0,1],
    [-1,0,1]
], dtype=np.float32)

prewitt_y_kernel = np.array([
    [-1,-1,-1],
    [ 0, 0, 0],
    [ 1, 1, 1]
], dtype=np.float32)

prewitt_x = cv2.filter2D(gray,-1,prewitt_x_kernel)
prewitt_y = cv2.filter2D(gray,-1,prewitt_y_kernel)

# -----------------------------
# SOBEL
# -----------------------------

sobel_x = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

sobel_y = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

# 45 Degree Kernel

kernel45 = np.array([
[-2,-1,0],
[-1,0,1],
[0,1,2]
],dtype=np.float32)

sobel45 = cv2.filter2D(gray,-1,kernel45)

# 135 Degree Kernel

kernel135 = np.array([
[0,1,2],
[-1,0,1],
[-2,-1,0]
],dtype=np.float32)

sobel135 = cv2.filter2D(gray,-1,kernel135)

# -----------------------------
# LAPLACIAN
# -----------------------------

laplacian = cv2.Laplacian(gray,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# -----------------------------
# CANNY
# -----------------------------

canny = cv2.Canny(gray,100,200)

imgs = [

img,

cv2.cvtColor(point,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(line,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(roberts,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(prewitt_x,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(prewitt_y,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(sobel_x,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(sobel_y,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(sobel45,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(sobel135,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(laplacian,cv2.COLOR_GRAY2BGR),

cv2.cvtColor(canny,cv2.COLOR_GRAY2BGR)

]

titles = [

"Original",

"Point",

"Line",

"Roberts",

"Prewitt X",

"Prewitt Y",

"Sobel 0",

"Sobel 90",

"Sobel 45",

"Sobel 135",

"Laplacian",

"Canny"

]

result=[]

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
    cols=6,
    space=20,
    bg_color=[255,255,255]
)

cv2.imshow("Point Line Edge Detection",output)
cv2.waitKey(0)
cv2.destroyAllWindows()