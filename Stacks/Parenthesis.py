from stack import Stack


def is_parenthesis_balanced(parenStr):
    parendict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    stack1 = Stack()
    balanced = True
    index = 0

    while index < len(parenStr) and balanced:
        paren = parenStr[index]

        if paren in "([{":
            stack1.push(paren)
        else:
            if stack1.is_empty():
                balanced = False
                break

            else:
                top = stack1.pop()
                if not parendict[top] == paren:
                    balanced = False
                    break
        index += 1

    if stack1.is_empty() and balanced:
        return True
    else:
        return False
