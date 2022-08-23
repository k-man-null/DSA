from stack import Stack
"""
We can also reverse strings in python using the syntax string[::-1]
However, for the purposes of learning, a stack will be used,
leveraging the LIFO system of a stack datastructure
"""


def reverse_string(string):
    my_stack = Stack()
    reversed = ""
    for letter in string:
        my_stack.push(letter)

    while not my_stack.is_empty():
        reversed += my_stack.pop()

    return reversed



