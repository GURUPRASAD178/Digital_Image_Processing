import cv2
import numpy as np

# Read image
img = cv2.imread("sample.jpg", 0)

# Resize image
img = cv2.resize(img, (256, 256))

# Convert image to byte sequence
data = img.flatten().tolist()

# Initialize dictionary
dictionary = {tuple([i]): i for i in range(256)}
dict_size = 256

w = ()
compressed = []

# LZW Compression
for k in data:
    wk = w + (k,)
    if wk in dictionary:
        w = wk
    else:
        compressed.append(dictionary[w])
        dictionary[wk] = dict_size
        dict_size += 1
        w = (k,)

if w:
    compressed.append(dictionary[w])

# Display Results
print("Original Pixels :", len(data))
print("Compressed Codes :", len(compressed))
print("Dictionary Size :", dict_size)

compression_ratio = len(data) / len(compressed)

print("Compression Ratio : {:.2f}".format(compression_ratio))

# Display Image
cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()