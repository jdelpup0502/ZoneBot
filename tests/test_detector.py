import cv2
import numpy as np
import unittest
from src.detector import ZoneDetector

class TestZoneDetector(unittest.TestCase):
    
    def create_test_image(self, shape=(500, 500), bg_color=0, fg_color=255, rect_coords=((100, 100), (400, 400))):
        """Creates a simple test image with a rectangle."""
        image = np.full(shape, bg_color, dtype=np.uint8)
        cv2.rectangle(image, rect_coords[0], rect_coords[1], fg_color, -1)
        return image

    def test_detect_zones(self):
        """Test detecting zones in a simple image."""
        detector = ZoneDetector(min_area=1000)
        
        # Create image with a 300x300 rectangle (area = 90000)
        image = self.create_test_image()
        
        zones = detector.detect_zones(image)
        
        self.assertEqual(len(zones), 1)
        
        # Check area
        area = cv2.contourArea(zones[0])
        self.assertEqual(area, 90000)

    def test_filter_small_zones(self):
        """Test filtering small zones."""
        detector = ZoneDetector(min_area=5000)
        
        # Create image with a small 50x50 rectangle (area = 2500)
        image = self.create_test_image(rect_coords=((10, 10), (60, 60)))
        
        zones = detector.detect_zones(image)
        
        self.assertEqual(len(zones), 0)

    def test_approximate_polygons(self):
        """Test polygon approximation."""
        detector = ZoneDetector()
        
        # Create image with a rectangle
        image = self.create_test_image()
        
        zones = detector.detect_zones(image)
        polygons = detector.approximate_polygons(zones)
        
        self.assertEqual(len(polygons), 1)
        # A rectangle should be approximated to 4 points
        self.assertEqual(len(polygons[0]), 4)

    def test_draw_zones(self):
        """Test drawing zones."""
        detector = ZoneDetector()
        image = self.create_test_image()
        zones = detector.detect_zones(image)
        
        # Create a dummy color image to draw on
        color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        result = detector.draw_zones(color_image, zones)
        
        self.assertEqual(result.shape, color_image.shape)
        self.assertFalse(np.array_equal(result, color_image)) # Should be different due to drawing

    def test_detect_multiple_zones(self):
        """Test detecting multiple distinct zones."""
        detector = ZoneDetector(min_area=1000)
        
        image = np.full((600, 600), 0, dtype=np.uint8)
        # First rectangle
        cv2.rectangle(image, (50, 50), (150, 150), 255, -1) # Area = 100x100 = 10000
        # Second rectangle
        cv2.rectangle(image, (200, 200), (350, 350), 255, -1) # Area = 150x150 = 22500
        # Third rectangle, too small
        cv2.rectangle(image, (400, 400), (420, 420), 255, -1) # Area = 20x20 = 400
        
        zones = detector.detect_zones(image)
        
        self.assertEqual(len(zones), 2) # Expecting 2 zones, as one is too small

        areas = sorted([cv2.contourArea(z) for z in zones])
        self.assertEqual(areas, [10000, 22500])
