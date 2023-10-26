from dataclasses import dataclass


@dataclass
class Queue:
    size: 0
    head: None
    tail: None


@dataclass
class Node:
    value: None
    next: None


def create():
    return Queue(0, None, None)


def size(queue):
    return queue.size


def empty(queue):
    return queue.size == 0


def top(queue):
    if empty(queue):
        raise AttributeError("Queue is empty")
    return queue.head.value


def push(queue, value):
    if empty(queue):
        queue.head = Node(value, None)
        queue.tail = queue.head
    else:
        new_element = Node(value, None)
        queue.tail.next = new_element
        queue.tail = queue.tail.next
    queue.size += 1
    return queue


def pop(queue):
    if empty(queue):
        raise AttributeError("Queue is empty")
    if size(queue) > 1:
        pop_value = queue.head.value
        queue.head = queue.head.next
    else:
        pop_value = queue.head.value
        queue.head = None
    queue.size -= 1
    return pop_value
