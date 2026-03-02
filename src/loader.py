import cv2
import numpy as np
from pdf2image import convert_from_path
import os

class ImageLoader:
    """Handles loading of construction plans from various formats (images, PDF)."""

    @staticmethod
    def load_image(file_path: str) -> np.ndarray:
        """
        Loads an image from a file path.
        
        Args:
            file_path (str): Path to the image file.
            
        Returns:
            np.ndarray: Loaded image in BGR format.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not a valid image.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Check if it's a PDF
        if file_path.lower().endswith('.pdf'):
            return ImageLoader._load_pdf(file_path)

        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Failed to load image from {file_path}. Format might not be supported.")
        
        return image

    @staticmethod
    def _load_pdf(file_path: str) -> np.ndarray:
        """
        Converts the first page of a PDF to an OpenCV image.
        
        Args:
            file_path (str): Path to the PDF file.
            
        Returns:
            np.ndarray: Image of the first page.
        """
        try:
            pages = convert_from_path(file_path)
            if not pages:
                raise ValueError("PDF is empty.")
            
            # Convert first page to numpy array (RGB)
            pil_image = pages[0]
            open_cv_image = np.array(pil_image) 
            
            # Convert RGB to BGR
            open_cv_image = open_cv_image[:, :, ::-1].copy() 
            return open_cv_image
        except Exception as e:
            raise ValueError(f"Error converting PDF: {e}")
