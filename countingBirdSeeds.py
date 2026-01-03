from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

# Load image
image_path = r"C:\Users\User\Documents\FIK SEM 3 2025-2026\Digital Image\Final Project\bird seed.jpeg"
img = Image.open(image_path)

# Grayscale
gray = img.convert("L")
gray_np = np.array(gray)

# Thresholding (manual)
binary = gray_np > 128
binary = np.invert(binary)

# Morphological operations
binary = ndimage.binary_erosion(binary, iterations=1)
binary = ndimage.binary_dilation(binary, iterations=2)

# Connected component labeling
labels, count = ndimage.label(binary)

print("Number of rice grains detected:", count)

# Display
plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(gray_np, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(binary, cmap="gray")
plt.title("After Morphology")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(labels, cmap="nipy_spectral")
plt.title(f"Detected Bird Seeds = {count}")
plt.axis("off")

plt.tight_layout()
plt.show()
