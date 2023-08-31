# variant1
from collections import deque


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise ValueError("stack is empty")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise ValueError("stack is empty")


# variant 2
class Stack2:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise ValueError("stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise ValueError("stack is empty")


def reverse_string(a_string):
    stack = []
    string = ""
    for char in a_string:
        stack.append(char)
    for char in a_string:
        string += stack.pop()

    return string


def check_parentheses(a_string):
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    for char in a_string:
        if char in brackets:
            stack.append(char)

        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack
