import cv2
import numpy as np
from typing import List, Tuple

class ZoneDetector:
    """Detects zones (rooms/areas) from processed construction plans."""

    def __init__(self, min_area: float = 1000.0):
        """
        Args:
            min_area (float): Minimum area (in pixels) for a contour to be considered a zone.
        """
        self.min_area = min_area

    def detect_zones(self, binary_image: np.ndarray) -> List[np.ndarray]:
        """
        Detects potential zones/rooms from a binary image.
        
        Args:
            binary_image (np.ndarray): Binary image (white zones on black background).
            
        Returns:
            List[np.ndarray]: List of contours representing detected zones.
        """
        # Find contours
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        filtered_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= self.min_area:
                filtered_contours.append(contour)
                
        return filtered_contours

    def approximate_polygons(self, contours: List[np.ndarray], epsilon_factor: float = 0.02) -> List[np.ndarray]:
        """
        Approximates contours to polygons (simplifies shapes).
        
        Args:
            contours (List[np.ndarray]): List of contours.
            epsilon_factor (float): Approximation accuracy parameter.
            
        Returns:
            List[np.ndarray]: List of approximated polygons.
        """
        polygons = []
        for contour in contours:
            epsilon = epsilon_factor * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            polygons.append(approx)
            
        return polygons

    def draw_zones(self, image: np.ndarray, zones: List[np.ndarray], color: Tuple[int, int, int] = (0, 255, 0), thickness: int = 2) -> np.ndarray:
        """
        Draws detected zones on the original image.
        
        Args:
            image (np.ndarray): Original image.
            zones (List[np.ndarray]): List of zone contours/polygons.
            color (Tuple[int, int, int]): BGR color for drawing.
            thickness (int): Line thickness.
            
        Returns:
            np.ndarray: Image with drawn zones.
        """
        result = image.copy()
        cv2.drawContours(result, zones, -1, color, thickness)
        return result
