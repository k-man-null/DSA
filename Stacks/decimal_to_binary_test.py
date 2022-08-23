from decimal_to_binary import decimal_to_binary
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(242), "11110010")
        self.assertEqual(decimal_to_binary(600), "1001011000")


if __name__ == '__main__':
    unittest.main()

