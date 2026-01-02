import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.ndimage as ndimage
import os

# ----------------------------
# 1. Load Image
# ----------------------------
image_path = r"C:\Users\Thiru LM\Downloads\STUDIES\IMAGE PROCESSING\apple\tomato.jpg"

if not os.path.exists(image_path):
    print("Error: The file path provided does not exist. Please check the path.")
else:
    # Load original color image (RGB)
    img_color = Image.open(image_path).convert("RGB")
    img_color_np = np.array(img_color)

    # Load grayscale version for Otsu calculation
    img_gray = Image.open(image_path).convert("L")
    img_gray_np = np.array(img_gray)

    # ----------------------------
    # 2. Otsu Thresholding (Manual)
    # ----------------------------
    hist, bins = np.histogram(img_gray_np.flatten(), 256, [0, 256])
    total_pixels = img_gray_np.size
    sum_total = np.dot(np.arange(256), hist)

    sum_bg, weight_bg, max_variance, threshold = 0, 0, 0, 0

    for i in range(256):
        weight_bg += hist[i]
        if weight_bg == 0: continue
        weight_fg = total_pixels - weight_bg
        if weight_fg == 0: break

        sum_bg += i * hist[i]
        mean_bg = sum_bg / weight_bg
        mean_fg = (sum_total - sum_bg) / weight_fg
        
        variance = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2
        if variance > max_variance:
            max_variance = variance
            threshold = i

    # ----------------------------
    # 3. Mask Refinement (Fixing Color and Background)
    # ----------------------------
    # Use an offset to include dark green veins
    adjusted_threshold = max(0, threshold - 35) 
    
    # Create mask (Leaf is > threshold)
    mask = img_gray_np > adjusted_threshold 

    # Morphological cleaning: Remove background noise and fill holes in leaf
    mask = ndimage.binary_opening(mask, structure=np.ones((5,5)))
    mask = ndimage.binary_fill_holes(mask)

    # Convert to 0-255 binary image
    binary_mask_img = (mask.astype(np.uint8)) * 255

    # ----------------------------
    # 4. Apply Mask to Color Image
    # ----------------------------
    mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2)

    # Isolated Leaf (Color)
    leaf_color = np.where(mask_3d, img_color_np, 0)

    # Background Only (Color)
    background_color = np.where(~mask_3d, img_color_np, 0)

    # ----------------------------
    # 5. Display Results (4 Pictures)
    # ----------------------------
    plt.figure(figsize=(15, 10))

    # Plot 1: Original
    plt.subplot(2, 2, 1)
    plt.title("1. Original Color Image")
    plt.imshow(img_color_np)
    plt.axis("off")

    # Plot 2: Binary Mask
    plt.subplot(2, 2, 2)
    plt.title("2. Binary Mask (Leaf=White)")
    plt.imshow(binary_mask_img, cmap="gray")
    plt.axis("off")

    # Plot 3: Object Only
    plt.subplot(2, 2, 3)
    plt.title("3. Object Only (Color Leaf)")
    plt.imshow(leaf_color)
    plt.axis("off")

    # Plot 4: Background Only
    plt.subplot(2, 2, 4)
    plt.title("4. Background Only (Color)")
    plt.imshow(background_color)
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    print(f"Otsu Threshold: {threshold}, Adjusted: {adjusted_threshold}")
    