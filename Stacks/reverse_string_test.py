from reverse_string import reverse_string
import unittest

class TestReverseString(unittest.TestCase):

    def test_reversestring(self):

        self.assertEqual(reverse_string("!evitacudE ot emocleW"), "Welcome to Educative!")

if __name__ == '__main__':
    unittest.main()



