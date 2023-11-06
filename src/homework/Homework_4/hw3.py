from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: any
    next: Node | None


@dataclass
class Queue:
    size: int
    head: Node | None
    tail: Node | None


def create():
    return Queue(0, None, None)


def get_size(queue):
    return queue.size


def is_empty(queue):
    return queue.size == 0


def view_top(queue):
    if is_empty(queue):
        raise AttributeError("Queue is empty")
    return queue.head.value


def push(queue, value):
    if is_empty(queue):
        queue.head = Node(value, None)
        queue.tail = queue.head
    else:
        new_element = Node(value, None)
        queue.tail.next = new_element
        queue.tail = queue.tail.next
    queue.size += 1
    return queue


def pop(queue):
    if is_empty(queue):
        raise AttributeError("Queue is empty")
    if get_size(queue) > 1:
        pop_value = queue.head.value
        queue.head = queue.head.next
    else:
        pop_value = queue.head.value
        queue.head = None
    queue.size -= 1
    return pop_value
