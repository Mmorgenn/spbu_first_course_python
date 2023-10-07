from collections import namedtuple
from dataclasses import dataclass

StackElement = namedtuple("StackElement", ["next", "value"])


@dataclass
class Stack:
    size: int
    head: StackElement


def empty(stack: Stack):
    return stack.size == 0


def size(stack: Stack):
    return stack.size


def top(stack: Stack):
    if not empty(stack):
        return stack.head.value
    else:
        return None


def push(stack: Stack, value):
    stack.head = StackElement(stack.head, value)
    stack.size += 1
    return stack


def pop(stack: Stack):
    if not empty(stack):
        stack.head = stack.head.next
        stack.size -= 1
        return True
    return False


def stack_new():
    return Stack(0, None)


def stack_output(stack):
    print(f"\nempty: {empty(stack)}\nsize: {size(stack)}\ntop: {top(stack)}\n")


def start():
    stack = stack_new()
    push(stack, "123")
    stack_output(stack)
    push(stack, "567")
    stack_output(stack)
    print(pop(stack))
    print(pop(stack))
    stack_output(stack)
    print(pop(stack))


if __name__ == "__main__":
    start()
