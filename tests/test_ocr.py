import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import sys

# Mock pytesseract before importing src.ocr if it's not installed
if 'pytesseract' not in sys.modules:
    sys.modules['pytesseract'] = MagicMock()

from src.ocr import TextExtractor

class TestTextExtractor(unittest.TestCase):
    
    def setUp(self):
        self.extractor = TextExtractor()
        self.dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)

    def test_extract_text(self):
        # We need to patch the pytesseract module within src.ocr
        with patch('src.ocr.pytesseract') as mock_pytesseract:
            mock_pytesseract.image_to_string.return_value = "Living Room\n10'6\" x 12'0\""
            
            # Re-initialize to ensure it picks up the mock if needed (though class level patch is better)
            # Actually, we just need to ensure self.extractor uses the mocked pytesseract
            # Since we patched src.ocr.pytesseract, the instance method should use it.
            
            text = self.extractor.extract_text(self.dummy_image)
            
            self.assertIn("Living Room", text)
            self.assertIn("10'6\"", text)
            mock_pytesseract.image_to_string.assert_called_once()

    def test_extract_dimensions(self):
        with patch('src.ocr.pytesseract') as mock_pytesseract:
            mock_pytesseract.image_to_string.return_value = "Living Room\n10'6\" x 12'0\"\nBedroom\n"
            
            dimensions = self.extractor.extract_dimensions(self.dummy_image)
            
            self.assertEqual(len(dimensions), 1)
            self.assertIn("10'6\" x 12'0\"", dimensions)
