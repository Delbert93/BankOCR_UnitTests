import unittest
import BankOCR as ocr

class MyTestCase(unittest.TestCase):

    input = """    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""

    def test_getBankNumber(self):
        expected = 123456789
        actual = ocr.getBankNumber(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
