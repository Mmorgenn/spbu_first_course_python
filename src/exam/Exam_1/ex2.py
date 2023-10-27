from dataclasses import dataclass


@dataclass
class ListNode:
    value: any
    next_node: "ListNode" = None


@dataclass
class List:
    head: "ListNode" = None
    tail: "ListNode" = None


def create():
    return List(None, None)


def head(list):
    if list.head != None:
        return list.head.value
    return None


def tail(list):
    if list.tail != None:
        return list.tail.value
    return None


def insert(list, value, position):
    if value is not None:
        new_node = ListNode(value)
        if position == 0:
            new_node.next_node = list.head
            list.head = new_node
            if not list.tail:
                list.tail = new_node
            return True
        current = list.head
        current_position = 0
        while current:
            if current_position + 1 == position:
                new_node.next_node = current.next_node
                current.next_node = new_node
                if current == list.tail:
                    list.tail = new_node
                return True
            current = current.next_node
            current_position += 1
    return False


def locate(list, value):
    current = list.head
    position = 0
    while current:
        if current.value == value:
            return position
        current = current.next_node
        position += 1
    return None


def retrieve(list, position):
    current = list.head
    current_position = 0
    while current:
        if current_position == position:
            return current.value
        current = current.next_node
        current_position += 1
    return None


def delete(list, position):
    if position == 0:
        if list.head:
            list.head = list.head.next_node
            if not list.head:
                list.tail = None
            return True
    current = list.head
    current_position = 0
    while current:
        if current_position + 1 == position:
            if current.next_node:
                current.next_node = current.next_node.next_node
                if not current.next_node:
                    list.tail = current
                return True
        current = current.next_node
        current_position += 1
    return False
