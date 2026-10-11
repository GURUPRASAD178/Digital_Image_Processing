import cv2
import numpy as np

img = cv2.imread("sample.jpg", 0)

rows, cols = img.shape

step = 10

error = np.zeros((rows, cols), dtype=np.int16)
reconstructed = np.zeros((rows, cols), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):

        if j == 0:
            pred = 0
        else:
            pred = int(reconstructed[i, j-1])   # Convert to int

        e = int(img[i, j]) - pred

        q = round(e / step)

        error[i, j] = q

        reconstructed[i, j] = np.uint8(
            np.clip(pred + q * step, 0, 255)
        )

cv2.imshow("Original", img)
cv2.imshow("Lossy Reconstruction", reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()