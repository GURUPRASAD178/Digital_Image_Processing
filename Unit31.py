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
img = cv2.resize(img,(250,250))

def gaussian(img):
    noise=np.random.normal(0,25,img.shape)
    return np.clip(img+noise,0,255).astype(np.uint8)

def rayleigh(img):
    noise=np.random.rayleigh(20,img.shape)
    return np.clip(img+noise,0,255).astype(np.uint8)

def gamma_noise(img):
    noise=np.random.gamma(2,10,img.shape)
    return np.clip(img+noise,0,255).astype(np.uint8)

def exponential(img):
    noise=np.random.exponential(20,img.shape)
    return np.clip(img+noise,0,255).astype(np.uint8)

def uniform(img):
    noise=np.random.uniform(-30,30,img.shape)
    return np.clip(img+noise,0,255).astype(np.uint8)

def salt_pepper(img):
    out=img.copy()
    p=0.03
    rnd=np.random.rand(*img.shape)
    out[rnd<p]=0
    out[rnd>1-p]=255
    return out

imgs=[
img,
gaussian(img),
rayleigh(img),
gamma_noise(img),
exponential(img),
uniform(img),
salt_pepper(img)
]

titles=[
"Original",
"Gaussian",
"Rayleigh",
"Gamma",
"Exponential",
"Uniform",
"SaltPepper"
]

result=[]

for t,i in zip(titles,imgs):
    i=cv2.cvtColor(i,cv2.COLOR_GRAY2BGR)
    cv2.putText(i,t,(10,25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.55,(0,0,255),2)
    result.append(i)

top=cv2.hconcat(result[:4])
bottom=cv2.hconcat(result[4:])

blank=np.zeros_like(result[0])
bottom=cv2.hconcat([result[4],result[5],result[6],blank])

output=create_image_grid(result,cols=4,space=20,bg_color=[255,255,255]) 

cv2.imshow("All Noises",output)
cv2.waitKey(0)
cv2.destroyAllWindows()