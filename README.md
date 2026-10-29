# 🖼️ Digital Image Processing Using Python & OpenCV

A comprehensive collection of **Digital Image Processing (DIP) techniques implemented using Python, OpenCV, and NumPy**, covering five units of image processing concepts.

This project demonstrates fundamental image operations, image enhancement, noise reduction, image segmentation, boundary and region descriptors, and image compression techniques. The processed results are displayed in organized OpenCV windows for easy visualization and comparison.

## 📌 Project Overview

Digital Image Processing involves manipulating digital images to improve their quality, extract useful information, identify objects, and reduce storage requirements.

This project implements various DIP algorithms through practical Python programs, with multiple processed outputs displayed together in a single window wherever appropriate.

### 🎯 Objectives

- Understand fundamental digital image processing operations.
- Implement image enhancement and transformation techniques.
- Analyze different types of image noise and filtering methods.
- Explore edge detection and image segmentation algorithms.
- Extract boundary and region descriptors for shape analysis.
- Understand image compression techniques and their trade-offs.
- Visualize the results of different algorithms using OpenCV.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| OpenCV (`cv2`) | Image processing and computer vision |
| NumPy | Numerical operations and matrix manipulation |
| Matplotlib | Optional plotting and histogram visualization |

## 📚 Topics Covered

### Unit 1: Fundamentals of Digital Image Processing

Basic image operations and pixel-level transformations.

- Grayscale image conversion
- Image sampling
- Image quantization
- Image addition
- Image subtraction
- Image multiplication
- Image division
- Bitwise AND operation
- Bitwise OR operation
- Bitwise XOR operation
- Bitwise NOT operation
- Bit-plane slicing

**Learning outcome:** Understand image representation, pixel values, sampling, quantization, and arithmetic and logical operations on images.

### Unit 2: Image Enhancement and Spatial Filtering

Image enhancement techniques improve image appearance and emphasize important features.

#### Intensity Transformations
- Image negative transformation
- Logarithmic transformation
- Power-law (gamma) transformation
- Piecewise-linear transformation

#### Histogram Processing
- Histogram calculation
- Histogram equalization
- Histogram matching (specification)
- Histogram visualization using graphs

#### Spatial Filtering
- Smoothing filters
- Sharpening filters
- Spatial enhancement methods

**Learning outcome:** Understand how intensity transformations, histogram processing, and spatial filters improve image contrast and visual quality.

### Unit 3: Noise Models, Filtering, and Restoration

This unit explores image degradation, noise generation, filtering, and restoration.

#### Types of Image Noise
- Gaussian noise
- Rayleigh noise
- Gamma noise
- Exponential noise
- Uniform noise
- Salt-and-pepper noise

#### Mean and Order-Statistic Filters
- Arithmetic mean filter
- Geometric mean filter
- Harmonic mean filter
- Contraharmonic mean filter
- Median filter
- Minimum filter
- Maximum filter
- Midpoint filter

#### Advanced Filtering and Restoration
- Adaptive filters
- Noise reduction using frequency-domain filtering
- Image degradation and estimation
- Inverse filtering

**Learning outcome:** Compare noise models, understand spatial and frequency-domain filtering, and explore techniques for restoring degraded images.

### Unit 4: Image Segmentation and Shape Analysis

Image segmentation separates an image into meaningful objects or regions.

#### 1. Point, Line, and Edge Detection
- Point detection
- Line detection
- Roberts edge detector
- Prewitt edge detector
- Sobel edge detector
- Directional edge detection at different angles
- Laplacian edge detection
- Canny edge detection

#### 2. Thresholding
- Global thresholding
- Local thresholding
- Adaptive thresholding
- Multiple thresholding
- Variable thresholding

#### 3. Edge Linking and Boundary Detection
- Edge linking using morphological operations
- Contour detection
- Boundary extraction

#### 4. Image Representation
- Boundary representation
- Region representation
- Binary and labeled-region representations

#### 5. Region-Based Segmentation
- Connected-component labeling
- Region growing
- Region splitting
- Split-and-merge segmentation

#### 6. Watershed Segmentation
- Morphological opening
- Distance transform
- Foreground and background marker extraction
- Marker-based watershed segmentation

#### 7. Boundary Descriptors
- Contour area
- Perimeter
- Aspect ratio
- Extent
- Convex hull
- Solidity
- Equivalent diameter
- Circularity
- Bounding rectangle
- Minimum enclosing circle
- Ellipse fitting
- Chain code
- Polygon approximation
- Skeletonization

#### 8. Region Descriptors
Region descriptors can be used to analyze the geometric and statistical properties of segmented objects.

Examples include:
- Area and centroid
- Image moments
- Orientation
- Major and minor axes
- Region bounding box
- Mean intensity
- Shape-related properties

**Learning outcome:** Detect edges, separate objects, represent shapes, and extract numerical features for image analysis.

### Unit 5: Image Compression

Image compression reduces the amount of data required to represent an image.

#### 1. Image Redundancy
- Coding redundancy
- Spatial redundancy
- Psychovisual redundancy

#### 2. Compression Algorithms
- Huffman coding
- Arithmetic coding
- LZW compression
- Run-length encoding (RLE)
- One-dimensional CCITT coding
- Two-dimensional CCITT coding

#### 3. Approximation and Transform Coding
- Image approximation
- Discrete Cosine Transform (DCT)
- Block transform coding
- Frequency coefficient analysis

#### 4. Predictive Coding
- Lossless predictive coding
- Lossy predictive coding
- Prediction error analysis

#### 5. JPEG Compression
- JPEG quality comparison
- High-quality compression
- Medium-quality compression
- Low-quality compression
- Visual comparison of compression artifacts

**Learning outcome:** Understand redundancy, lossless and lossy compression, transform coding, predictive coding, and the trade-off between image quality and file size.

> **Note:** Huffman, arithmetic, LZW, RLE, and CCITT are encoding techniques that require their own implementations or appropriate libraries. They are not all built-in OpenCV image-processing functions. JPEG compression can be demonstrated using OpenCV's image-writing functionality.

## 📂 Project Structure


```text
Digital-Image-Processing/
│
├── README.md
├── requirements.txt
├── sample.jpg
│
├── Unit1/
│   ├── basic_operations.py
│   └── bit_plane_slicing.py
│
├── Unit2/
│   ├── intensity_transformations.py
│   ├── histogram_processing.py
│   └── spatial_filters.py
│
├── Unit3/
│   ├── noise_models.py
│   ├── mean_filters.py
│   ├── adaptive_filters.py
│   └── image_restoration.py
│
├── Unit4/
│   ├── edge_detection.py
│   ├── thresholding.py
│   ├── boundary_detection.py
│   ├── region_segmentation.py
│   ├── watershed.py
│   ├── boundary_descriptors.py
│   ├── region_descriptors.py
│   ├── chain_code.py
│   ├── polygon_approximation.py
│   └── skeletonization.py
│
└── Unit5/
    ├── redundancy.py
    ├── huffman_coding.py
    ├── arithmetic_coding.py
    ├── lzw_compression.py
    ├── run_length_encoding.py
    ├── transform_coding.py
    ├── predictive_coding.py
    └── jpeg_compression.py
```

The structure above is a suggested organization. You do not need to create every listed file if the corresponding technique has not yet been implemented.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip package manager
- An IDE such as Visual Studio Code, PyCharm, or Jupyter Notebook

