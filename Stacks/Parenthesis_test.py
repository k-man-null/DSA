import Parenthesis
import unittest

class TestParenthesis(unittest.TestCase):
    def testParenthesis(self):

        self.assertTrue(Parenthesis.is_parenthesis_balanced("(((({}))))"))
        self.assertFalse(Parenthesis.is_parenthesis_balanced("[][]]]"))
        self.assertTrue(Parenthesis.is_parenthesis_balanced("[][]"))

if __name__ == '__main__':
    unittest.main()

