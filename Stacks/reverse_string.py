from stack import Stack


def reverse_string(string):
    my_stack = Stack()
    reversed = ""
    for letter in string:
        my_stack.push(letter)

    while not my_stack.is_empty():
        reversed += my_stack.pop()

    return reversed



