import argparse
import os
import cv2
from src.loader import ImageLoader
from src.preprocessor import Preprocessor
from src.detector import ZoneDetector
from src.ocr import TextExtractor

def main():
    parser = argparse.ArgumentParser(description="ZoneBot - Construction Plan Analyzer")
    parser.add_argument("file_path", type=str, help="Path to the construction plan image or PDF.")
    parser.add_argument("--output", type=str, default="output.png", help="Path to save the processed image.")
    args = parser.parse_args()

    # 1. Load Image
    try:
        print(f"Loading plan from: {args.file_path}")
        image = ImageLoader.load_image(args.file_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # 2. Preprocess
    print("Preprocessing image...")
    gray = Preprocessor.to_grayscale(image)
    binary = Preprocessor.binarize(gray)
    # Optional: Denoise if needed
    # denoised = Preprocessor.denoise(binary) 

    # 3. Detect Zones
    print("Detecting zones...")
    detector = ZoneDetector(min_area=5000) # Adjust min_area as needed
    zones = detector.detect_zones(binary)
    polygons = detector.approximate_polygons(zones)
    
    print(f"Found {len(polygons)} potential zones.")

    # 4. Extract Text (OCR)
    print("Extracting text...")
    ocr = TextExtractor()
    extracted_text = ocr.extract_text(gray)
    
    # 5. Draw Results
    result_image = detector.draw_zones(image, polygons, color=(0, 255, 0), thickness=3)
    
    # Save output
    cv2.imwrite(args.output, result_image)
    print(f"Processed image saved to: {args.output}")
    
    # Print extracted text summary
    if extracted_text:
        print("\n--- Extracted Text Preview ---")
        print(extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text)
        print("------------------------------")

if __name__ == "__main__":
    main()
