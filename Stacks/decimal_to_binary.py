from stack import Stack


def decimal_to_binary(number):
    myStack = Stack()
    current_number = number

    while current_number != 0:
        rem = int(current_number % 2)

        myStack.push(rem)
        current_number = current_number // 2

    binary_string = ""
    while not myStack.is_empty():
        binary_string += str(myStack.pop())

    return binary_string







