import cv2
import os
import numpy as np

# === CONFIG ===
INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/clean"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def deskew(image):
    """Deskew the image using OpenCV moments."""
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def preprocess_image(input_path, output_path):
    # Load
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # 1. Denoise
    denoised = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)

    # 2. Threshold (binarize)
    _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. Deskew
    deskewed = deskew(binary)

    # Save
    cv2.imwrite(output_path, deskewed)
    print(f"[+] Cleaned → {output_path}")

def process_all():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".png"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename)
            preprocess_image(input_path, output_path)

if __name__ == "__main__":
    print("🔹 Preprocessing all images...")
    process_all()
    print("\n✅ Preprocessing complete! Cleaned images in data/clean/")
    