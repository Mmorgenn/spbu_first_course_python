from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

Value = TypeVar("Value")
Key = TypeVar("Key")


@dataclass
class TreeNode(Generic[Value]):
    key: Key
    value: Value
    left: Optional["TreeNode[Value]"] = None
    right: Optional["TreeNode[Value]"] = None
    height: int = 0


@dataclass
class TreeMap(Generic[Value]):
    root: Optional["TreeNode[Value]"] = None
    size: int = 0


def _get_height(node: TreeNode[Value]) -> int:
    if node is None:
        return -1
    else:
        return node.height


def _get_balance_factor(node: TreeNode[Value]) -> int:
    if node is None:
        return 0
    return _get_height(node.left) - _get_height(node.right)


def _update_height(node: TreeNode[Value]):
    node.height = max(_get_height(node.left), _get_height(node.right)) + 1


def _update_balance(node: TreeNode[Value]) -> TreeNode[Value]:
    _update_height(node)
    balance_factor = _get_balance_factor(node)

    if balance_factor == 2:
        if _get_balance_factor(node.left) < 0:
            return _double_left_rotate(node)
        return _single_left_rotate(node)

    elif balance_factor == -2:
        if _get_balance_factor(node.right) > 0:
            return _double_right_rotate(node)
        return _single_right_rotate(node)

    return node


def _is_empty(tree_map: TreeMap[Value]) -> bool:
    return tree_map.size == 0


def create_tree_map() -> TreeMap[Value]:
    return TreeMap()


def delete_tree_map(tree_map: TreeMap[Value]):
    def _delete_tree_map(node: TreeNode[Value]):
        if node.left is not None:
            _delete_tree_map(node.left)
        if node.right is not None:
            _delete_tree_map(node.right)
        node.left = None
        node.right = None

    if not _is_empty(tree_map):
        _delete_tree_map(tree_map.root)
    tree_map.root = None
    tree_map.size = 0


def put(tree_map: TreeMap[Value], key: Key, value: Value):
    if not has_key(tree_map, key):
        tree_map.size += 1

    def _put(node: TreeNode[Value], key: Key, value: Value):
        if node is None:
            return TreeNode(key=key, value=value)
        if key == node.key:
            node.value = value
            return node
        if key < node.key:
            node.left = _put(node.left, key, value)
        else:
            node.right = _put(node.right, key, value)
        return _update_balance(node)

    tree_map.root = _put(tree_map.root, key, value)


def remove(tree_map: TreeMap[Value], key: Key) -> Value:
    if not has_key(tree_map, key):
        raise ValueError("No such key!")

    def _remove(node: TreeNode[Value], key: Key):
        if node.left is None and node.right is None:
            return None, node.value

        if key == node.key:
            value_result = node.value
            if node.left is None:
                return node.right, value_result
            elif node.right is None:
                return node.left, value_result

            min_right_node = _find_min_node(node.right)
            new_right_node = _remove(node.right, min_right_node.key)[0]
            new_node = TreeNode(
                min_right_node.key, min_right_node.value, node.left, new_right_node
            )
            return _update_balance(new_node), value_result
        if key < node.key:
            node.left, value_result = _remove(node.left, key)
        else:
            node.right, value_result = _remove(node.right, key)
        return _update_balance(node), value_result

    tree_map.root, result = _remove(tree_map.root, key)
    tree_map.size -= 1
    return result


def has_key(tree_map: TreeMap[Value], key: Key) -> bool:
    if _is_empty(tree_map):
        return False

    def _hash_key(node: TreeNode[Value], key: Key):
        if node is None:
            return False
        if node.key == key:
            return True
        if node.key > key:
            return _hash_key(node.left, key)
        return _hash_key(node.right, key)

    return _hash_key(tree_map.root, key)


def get_value(tree_map: TreeMap[Value], key: Key) -> Value:
    if not has_key(tree_map, key):
        raise ValueError("No such key!")

    def _get_value(node: TreeNode[Value], key: Key):
        if node.key == key:
            return node.value
        if node.key > key:
            return_value = _get_value(node.left, key)
        else:
            return_value = _get_value(node.right, key)
        return return_value

    return _get_value(tree_map.root, key)


def get_maximum_key(tree_map: TreeMap[Value]) -> Key:
    if _is_empty(tree_map):
        raise ValueError("No any keys!")

    def _get_maximum_key(node: TreeNode):
        if node.right is None:
            return node.key
        return _get_maximum_key(node.right)

    return _get_maximum_key(tree_map.root)


def get_minimum_key(tree_map: TreeMap[Value]) -> Key:
    if _is_empty(tree_map):
        raise ValueError("No any keys!")

    def _get_minimum_key(node: TreeNode[Value]):
        if node.left is None:
            return node.key
        return _get_minimum_key(node.left)

    return _get_minimum_key(tree_map.root)


def get_lower_bound(tree_map: TreeMap[Value], key: Key) -> Key:
    try:
        max_key = get_maximum_key(tree_map)
    except ValueError:
        raise ValueError("No any keys")
    if key > max_key:
        raise ValueError(f"{key} is bigger than any keys in TreeMap")

    def _get_lower_bound(node: TreeNode[Value], key: Key, min_key):
        if node.key >= key:
            min_key = min(min_key, node.key)
        if key < node.key and node.left is not None:
            return _get_lower_bound(node.left, key, min_key)
        elif key > node.key and node.right is not None:
            return _get_lower_bound(node.right, key, min_key)
        return min_key

    return _get_lower_bound(tree_map.root, key, max_key)


def get_higher_bound(tree_map: TreeMap[Value], key: Key) -> Key:
    try:
        max_key = get_maximum_key(tree_map)
    except ValueError:
        raise ValueError("No any keys")
    if key >= max_key:
        raise ValueError(
            f"{key} is bigger than any keys or equal to the max key in TreeMap"
        )

    def _get_lower_bound(node: TreeNode[Value], key: Key, min_key):
        if node.key > key:
            min_key = min(min_key, node.key)
        if key < node.key and node.left is not None:
            return _get_lower_bound(node.left, key, min_key)
        elif key > node.key and node.right is not None:
            return _get_lower_bound(node.right, key, min_key)
        return min_key

    return _get_lower_bound(tree_map.root, key, max_key)


def traverse(tree_map: TreeMap[Value], order: str) -> list:
    if _is_empty(tree_map):
        return []

    result = []

    def recursion(current_node: TreeNode[Value], order_func):
        node_list = order_func(current_node)
        for node in node_list:
            if node is not current_node:
                recursion(node, order_func)
            else:
                result.append((current_node.key, current_node.value))

    if order == "preorder":
        recursion(tree_map.root, _preorder_comparator)
    elif order == "inorder":
        recursion(tree_map.root, _inorder_comparator)
    elif order == "postorder":
        recursion(tree_map.root, _postorder_comparator)
    else:
        raise ValueError("No such order")
    return result


def _postorder_comparator(node: TreeNode[Value]):
    return filter(None, (node.left, node.right, node))


def _inorder_comparator(node: TreeNode[Value]):
    return filter(None, (node.left, node, node.right))


def _preorder_comparator(node: TreeNode[Value]):
    return filter(None, (node, node.left, node.right))


def _find_min_node(node: TreeNode[Value]) -> TreeNode[Value]:
    if node.left is None:
        return node
    else:
        return _find_min_node(node.left)


def _single_right_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    new_node = node.right
    node.right = new_node.left
    new_node.left = node
    _update_height(node)
    new_node.height = max(_get_height(new_node.right), _get_height(node)) + 1
    return new_node


def _single_left_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    new_node = node.left
    node.left = new_node.right
    new_node.right = node
    _update_height(node)
    new_node.height = max(_get_height(new_node.left), _get_height(node)) + 1
    return new_node


def _double_right_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    node.right = _single_left_rotate(node.right)
    return _single_right_rotate(node)


def _double_left_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    node.left = _single_right_rotate(node.left)
    return _single_left_rotate(node)


test = create_tree_map()
for key, value in ():
    put(test, key, value)
print(traverse(test, "preorder"))
