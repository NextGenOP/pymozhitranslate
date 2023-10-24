import unittest
from pymozhitranslate import Translator

class TestTranslate(unittest.TestCase):
    
    def setUp(self):
        # Set up any necessary objects or data for your tests
        self.translator = Translator(engine="google")
    
    def test_translate(self):
        # Write a test for the translate method
        source = "auto"
        target = "en"
        text = "Halo, apa kabar ?"
        expected = "Hello, how are you ?"
        
        result = self.translator.translate(source, target, text)
        self.assertEqual(result, expected)
    
    # Write more test functions for other methods or scenarios
    
if __name__ == '__main__':
    unittest.main()