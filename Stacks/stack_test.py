import unittest
from stack import Stack


class TestStackClass(unittest.TestCase):

    def test_push(self):
        stack1 = Stack()
        stack1.push("1")
        stack1.push("2")
        self.assertEqual(stack1.get_stack(), ["1", "2"])

    def test_pop(self):
        stack2 = Stack()
        stack2.push("9")
        stack2.push("8")
        stack2.push("7")
        stack2.pop()
        self.assertEqual(stack2.get_stack(), ["9", "8"])

    def test_peek(self):
        stack3 = Stack()
        stack3.push("1")
        stack3.push("2")
        stack3.push("3")
        self.assertEqual(stack3.peek(), "3")


    def test_is_empty(self):
        stack4 = Stack()

        self.assertEqual(stack4.is_empty(), True)

    def test_get_stack(self):

        stack5 = Stack()

        self.assertEqual(stack5.get_stack(), [])

if __name__ == '__main__':
    unittest.main()


