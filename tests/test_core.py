import unittest
import numpy as np
import cv2
import os
from src.loader import ImageLoader
from src.preprocessor import Preprocessor

class TestCoreLogic(unittest.TestCase):

    def setUp(self):
        # Create a dummy image for testing
        self.test_image_path = "test_image.png"
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.rectangle(self.image, (10, 10), (90, 90), (255, 255, 255), -1)
        cv2.imwrite(self.test_image_path, self.image)

    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

    def test_load_image(self):
        loaded_img = ImageLoader.load_image(self.test_image_path)
        self.assertIsNotNone(loaded_img)
        self.assertEqual(loaded_img.shape, (100, 100, 3))

    def test_grayscale(self):
        loaded_img = ImageLoader.load_image(self.test_image_path)
        gray = Preprocessor.to_grayscale(loaded_img)
        self.assertEqual(len(gray.shape), 2)

    def test_binarize(self):
        loaded_img = ImageLoader.load_image(self.test_image_path)
        gray = Preprocessor.to_grayscale(loaded_img)
        binary = Preprocessor.binarize(gray)
        # Check if values are only 0 or 255
        unique_values = np.unique(binary)
        self.assertTrue(np.all(np.isin(unique_values, [0, 255])))

if __name__ == '__main__':
    unittest.main()
