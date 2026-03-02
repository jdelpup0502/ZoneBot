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
