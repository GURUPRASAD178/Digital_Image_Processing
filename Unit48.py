import cv2
import numpy as np

# Read grayscale image
img = cv2.imread("sample.jpg", 0)

rows, cols = img.shape

prediction = np.zeros((rows, cols), dtype=np.uint8)
error = np.zeros((rows, cols), dtype=np.int16)

# Prediction and Error Calculation
for i in range(rows):
    for j in range(cols):

        if j == 0:
            pred = 0
        else:
            pred = int(img[i, j-1])   # Convert to int

        prediction[i, j] = np.uint8(pred)

        error[i, j] = int(img[i, j]) - pred

# Reconstruction
reconstructed = np.zeros((rows, cols), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):

        if j == 0:
            pred = 0
        else:
            pred = int(reconstructed[i, j-1])   # Convert to int

        reconstructed[i, j] = np.uint8(
            np.clip(pred + int(error[i, j]), 0, 255)
        )

cv2.imshow("Original", img)
cv2.imshow("Lossless Prediction", prediction)
cv2.imshow("LosslessReconstructed", reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()