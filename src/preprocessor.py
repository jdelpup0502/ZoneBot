import cv2
import numpy as np

class Preprocessor:
    """Basic image preprocessing for construction plans."""

    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """Converts an image to grayscale."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def binarize(image: np.ndarray, threshold: int = 127) -> np.ndarray:
        """Applies binary thresholding."""
        _, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        return thresh

    @staticmethod
    def denoise(image: np.ndarray) -> np.ndarray:
        """Removes noise using Gaussian Blur."""
        return cv2.GaussianBlur(image, (5, 5), 0)

    @staticmethod
    def detect_edges(image: np.ndarray, low_threshold: int = 50, high_threshold: int = 150) -> np.ndarray:
        """Detects edges using Canny edge detector."""
        return cv2.Canny(image, low_threshold, high_threshold)
