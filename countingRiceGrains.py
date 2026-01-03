from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

# 1. Load image
image_path = r"C:\Users\User\Documents\FIK SEM 3 2025-2026\Digital Image\Final Project\rice grain.jpg"
img = Image.open(image_path)

# 2. Grayscale
gray = img.convert("L")
gray_np = np.array(gray)

# 3. Improved Thresholding
thresh = gray_np.mean() * 0.8 
binary = gray_np < thresh 

# 4. Better Morphological Operations
struct = np.ones((3, 3))

# Clean up small dots (noise)
binary = ndimage.binary_opening(binary, structure=struct, iterations=2)

# This 'shrinks' the rice grains to disconnect them, then regrows them
binary = ndimage.binary_erosion(binary, structure=struct, iterations=4)
binary = ndimage.binary_dilation(binary, structure=struct, iterations=3)

# 5. Connected component labeling
labels, count = ndimage.label(binary)

# --- Display Results ---
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Photo")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(binary, cmap="gray")
plt.title("Binary Mask (Rice separated)")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(labels, cmap="nipy_spectral")
plt.title(f"Rice Grains (Count: {count})")
plt.axis("off")

# Zoom in on the labels to see the separation better
plt.subplot(2, 2, 4)
plt.imshow(labels[200:600, 200:600], cmap="nipy_spectral")
plt.title("Close-up view")
plt.axis("off")

plt.tight_layout()
plt.show()

print(f"Number of rice grains detected: {count}")