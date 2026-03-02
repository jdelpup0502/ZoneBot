import cv2
try:
    import pytesseract
except ImportError:
    pytesseract = None

import numpy as np
import shutil

class TextExtractor:
    """Handles text extraction (OCR) from construction plans."""

    def __init__(self, tesseract_cmd: str = None):
        """
        Args:
            tesseract_cmd (str): Optional path to tesseract executable.
        """
        if pytesseract is None:
            print("Warning: pytesseract module not found. OCR functionality will be disabled.")
            return

        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        
        if not shutil.which('tesseract') and not tesseract_cmd:
            print("Warning: Tesseract OCR executable not found in PATH.")

    def extract_text(self, image: np.ndarray, config: str = '--psm 6') -> str:
        """
        Extracts text from an image.
        
        Args:
            image (np.ndarray): Image to process (preferably preprocessed).
            config (str): Tesseract configuration string.
            
        Returns:
            str: Extracted text.
        """
        if pytesseract is None:
            return "Error: pytesseract not installed."

        try:
            text = pytesseract.image_to_string(image, config=config)
            return text.strip()
        except pytesseract.TesseractNotFoundError:
            return "Error: Tesseract OCR not found. Please install tesseract-ocr."
        except Exception as e:
            return f"Error during OCR: {e}"

    def extract_dimensions(self, image: np.ndarray) -> list[str]:
        """
        Extracts dimension-like strings from an image.
        
        Args:
            image (np.ndarray): Image to process.
            
        Returns:
            list[str]: List of dimension strings (e.g., "10'6"", "3.5m").
        """
        # This is a placeholder for more advanced dimension extraction logic.
        # For now, it just returns all text and filters for numbers/dimensions.
        raw_text = self.extract_text(image)
        lines = raw_text.split('\n')
        dimensions = []
        for line in lines:
            # Simple heuristic: if line contains digits and typical dimension markers
            if any(char.isdigit() for char in line) and any(marker in line for marker in ["'", '"', 'm', 'ft']):
                dimensions.append(line.strip())
        return dimensions
