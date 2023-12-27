from dataclasses import dataclass
from typing import Generic, Optional, TypeVar
from copy import deepcopy

Value = TypeVar("Value")
Key = TypeVar("Key")


@dataclass
class TreeNode(Generic[Value]):
    key: Key
    value: Value
    left: Optional["TreeNode[Value]"] = None
    right: Optional["TreeNode[Value]"] = None
    height: int = 1
    size: int = 1


@dataclass
class TreeMap(Generic[Value]):
    root: Optional["TreeNode[Value]"] = None


def get_height(node: TreeNode[Value]) -> int:
    if node is None:
        return 0
    else:
        return node.height


def get_size(node: TreeNode[Value]) -> int:
    if node is None:
        return 0
    else:
        return node.size


def get_balance_factor(node: TreeNode[Value]) -> int:
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def _update_height(
    node: TreeNode[Value], left: TreeNode[Value], right: TreeNode[Value]
):
    node.height = max(get_height(left), get_height(right)) + 1


def _update_size(node: TreeNode[Value], left: TreeNode[Value], right: TreeNode[Value]):
    node.size = get_size(left) + get_size(right) + 1


def _update_balance(node: TreeNode[Value]) -> TreeNode[Value]:
    _update_height(node, node.left, node.right)
    _update_size(node, node.left, node.right)
    balance_factor = get_balance_factor(node)

    if balance_factor == 2:
        if get_balance_factor(node.left) < 0:
            return _double_left_rotate(node)
        return _single_left_rotate(node)

    elif balance_factor == -2:
        if get_balance_factor(node.right) > 0:
            return _double_right_rotate(node)
        return _single_right_rotate(node)

    return node


def is_empty(tree_map: TreeMap[Value]) -> bool:
    return tree_map.root is None


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

    if not is_empty(tree_map):
        _delete_tree_map(tree_map.root)
    tree_map.root = None


def put(tree_map: TreeMap[Value], key: Key, value: Value):
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
    return result


def has_key(tree_map: TreeMap[Value], key: Key) -> bool:
    if is_empty(tree_map):
        return False
    return _get_node(tree_map.root, key) is not None


def get_value(tree_map: TreeMap[Value], key: Key) -> Value:
    node = _get_node(tree_map.root, key)
    if not node:
        raise ValueError("No such key!")
    return node[1]


def _get_node(node: TreeNode[Value], key: Key) -> list[Key, Value] | None:
    if node is None:
        return None
    if node.key == key:
        return [node.key, node.value]
    if node.key > key:
        return _get_node(node.left, key)
    return _get_node(node.right, key)


def get_maximum_key(tree_map: TreeMap[Value]) -> Key:
    if is_empty(tree_map):
        raise ValueError("No any keys!")

    def _get_maximum_key(node: TreeNode):
        current_node = node
        while current_node:
            if not current_node.right:
                return current_node.key
            current_node = current_node.right

    return _get_maximum_key(tree_map.root)


def get_minimum_key(tree_map: TreeMap[Value]) -> Key:
    if is_empty(tree_map):
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


def get_upper_bound(tree_map: TreeMap[Value], key: Key) -> Key:
    try:
        max_key = get_maximum_key(tree_map)
    except ValueError:
        raise ValueError("No any keys")
    if key >= max_key:
        raise ValueError(
            f"{key} is bigger than any keys or equal to the max key in TreeMap"
        )

    def _get_upper_bound(node: TreeNode[Value], key: Key, min_key):
        if node.key > key:
            min_key = min(min_key, node.key)
        if key < node.key and node.left is not None:
            return _get_upper_bound(node.left, key, min_key)
        elif key > node.key and node.right is not None:
            return _get_upper_bound(node.right, key, min_key)
        return min_key

    return _get_upper_bound(tree_map.root, key, max_key)


def traverse(tree_map: TreeMap[Value], order: str) -> list:
    if is_empty(tree_map):
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
    _update_height(node, node.left, node.right)
    _update_size(node, node.left, node.right)
    _update_height(new_node, node, new_node.right)
    _update_size(new_node, node, new_node.right)
    return new_node


def _single_left_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    new_node = node.left
    node.left = new_node.right
    new_node.right = node
    _update_height(node, node.left, node.right)
    _update_size(node, node.left, node.right)
    _update_height(new_node, new_node.left, node)
    _update_size(new_node, new_node.left, node)
    return new_node


def _double_right_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    node.right = _single_left_rotate(node.right)
    return _single_right_rotate(node)


def _double_left_rotate(node: TreeNode[Value]) -> TreeNode[Value]:
    node.left = _single_right_rotate(node.left)
    return _single_left_rotate(node)


# for Homework_6_2


def split(tree_map: TreeMap[Value], key: Key) -> tuple[TreeMap[Value], TreeMap[Value]]:
    tree_map = deepcopy(tree_map)
    if _is_empty(tree_map):
        another_map = create_tree_map()
        return tree_map, another_map

    def _split(node, small_root, big_root):
        if not node:
            return None, None
        if node.key == key:
            new_node = merge_node(TreeNode(node.key, node.value), node.right)
            return node.left, new_node
        if node.key < key:
            small_root, big_root = _split(node.right, small_root, big_root)
            new_node = merge_node(node.left, TreeNode(node.key, node.value))
            return merge_node(new_node, small_root), big_root
        if node.key > key:
            small_root, big_root = _split(node.left, small_root, big_root)
            new_node = merge_node(TreeNode(node.key, node.value), node.right)
            return small_root, merge_node(big_root, new_node)

    small_tree = create_tree_map()
    big_tree = create_tree_map()
    small_tree.root, big_tree.root = _split(tree_map.root, None, None)
    return small_tree, big_tree


def merge_node(node: TreeNode[Value], another_node: TreeNode[Value]) -> TreeNode[Value]:
    if not node or not another_node:
        return node if node else another_node
    if _get_height(node) <= _get_height(another_node):
        another_node.left = merge_node(node, another_node.left)
        return _update_balance(another_node)
    else:
        node.right = merge_node(node.right, another_node)
        return _update_balance(node)


def join(tree_map: TreeMap[Value], another: TreeMap[Value]) -> TreeMap[Value]:
    if _is_empty(tree_map):
        return another
    if _is_empty(another):
        return tree_map

    def _join_equal_keys_size(small_tree: TreeMap[Value], big_tree: TreeMap[Value]):
        for key, value in traverse(small_tree, "preorder"):
            put(big_tree, key, value)
        return big_tree

    if get_maximum_key(another) < get_minimum_key(tree_map):
        new_tree = create_tree_map()
        new_tree.root = merge_node(another.root, tree_map.root)
        return new_tree
    if get_maximum_key(tree_map) < get_minimum_key(another):
        new_tree = create_tree_map()
        new_tree.root = merge_node(tree_map.root, another.root)
        return new_tree
    if _get_size(tree_map.root) <= _get_size(another.root):
        return _join_equal_keys_size(tree_map, another)
    if _get_size(tree_map.root) > _get_size(another.root):
        return _join_equal_keys_size(another, tree_map)


def get_all(tree_map: TreeMap[Value], left: Key, right: Key) -> list[(Key, Value)]:
    if left > right:
        raise ValueError("Must be left_key <= right_key!")
    big_tree = split(tree_map, left)[1]
    tree_key_range = split(big_tree, right)[0]
    return traverse(tree_key_range, "inorder")


def get_all_keys(tree_map: TreeMap[Value], left: Key, right: Key) -> list[Key]:
    if left > right:
        raise ValueError("Must be left_key <= right_key!")
    return list(map(lambda pair: pair[0], get_all(tree_map, left, right)))


def remove_keys(tree_map: TreeMap[Value], left: Key, right: Key):
    if left > right:
        raise ValueError("Must be left_key <= right_key!")
    small_tree, big_tree = split(tree_map, left)
    big_tree = split(tree_map, right)[1]
    tree_map.root = join(small_tree, big_tree).root
