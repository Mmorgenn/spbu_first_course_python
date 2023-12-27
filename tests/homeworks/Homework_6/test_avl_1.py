import pytest
from src.homework.Homework_6.avl_tree import (
    is_empty,
    create_tree_map,
    get_size,
    get_balance_factor,
    put,
    remove,
    has_key,
    get_value,
    get_maximum_key,
    get_minimum_key,
    get_upper_bound,
    get_lower_bound,
)


def create_dummy_tree(tree_elements):
    dummy_tree = create_tree_map()
    for key, value in tree_elements:
        put(dummy_tree, key, value)
    return dummy_tree


def check_tree_balance(tree_map) -> bool:
    if is_empty(tree_map):
        return True

    def _check_balance(node):
        if not node:
            return True
        if abs(get_balance_factor(node)) > 1:
            return False
        if not _check_balance(node.left) or not _check_balance(node.right):
            return False
        return True

    return _check_balance(tree_map.root)


@pytest.mark.parametrize(
    "tree_elements,expected_size",
    (
        ((), 0),
        (((1, 12), (13, 4), (15, 7), (15, 8), (1, 3)), 3),
        (
            (
                (1, "a"),
                (10, "b"),
                (13, 0),
                (14, True),
                (0, 0),
                (9, 9),
                (127, 128),
                (37, "00:43 :)"),
            ),
            8,
        ),
        (((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)), 9),
        (
            (
                (12, [0]),
                (11, 6),
                (10, "27.12.2023"),
                (12, ""),
                (3, 3),
                (100, None),
                (8, 18),
            ),
            6,
        ),
    ),
)
def test_put(tree_elements, expected_size):
    dummy_tree = create_dummy_tree(tree_elements)
    assert get_size(dummy_tree.root) == expected_size and check_tree_balance(dummy_tree)


@pytest.mark.parametrize("keys_count", (1, 10, 25, 50, 100, 1000))
def test_tree_balance(keys_count):
    dummy_tree = create_tree_map()
    for i in range(keys_count):
        put(dummy_tree, i, i)
        assert check_tree_balance(dummy_tree)


@pytest.mark.parametrize(
    "tree_elements,key,expected_size,expected_value",
    (
        (
            (
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (8, 9),
                (9, 10),
                (10, 11),
            ),
            3,
            9,
            4,
        ),
        (
            (
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (8, 9),
                (9, 10),
                (10, 11),
            ),
            10,
            9,
            11,
        ),
        (
            (
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (8, 9),
                (9, 10),
                (10, 11),
            ),
            2,
            9,
            3,
        ),
        (
            (
                (1, "a"),
                (10, "b"),
                (13, 0),
                (14, True),
                (0, 0),
                (9, 9),
                (127, 128),
                (37, "00:43 :)"),
            ),
            37,
            7,
            "00:43 :)",
        ),
        (
            ((12, [0]), (11, 6), (10, "27.12.2023"), (3, 3), (100, None), (8, 18)),
            100,
            5,
            None,
        ),
    ),
)
def test_remove(tree_elements, key, expected_size, expected_value):
    dummy_tree = create_dummy_tree(tree_elements)
    value = remove(dummy_tree, key)
    assert (
        value == expected_value
        and get_size(dummy_tree.root) == expected_size
        and check_tree_balance(dummy_tree)
    )


@pytest.mark.parametrize(
    "tree_elements,key,expected",
    (
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 90, True),
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 13, False),
        (
            (
                ("a", 0),
                ("34", "7-8"),
                ("1", 3),
                ("aba", 90),
                ("abac", True),
                ("bac", [17]),
            ),
            "abac",
            True,
        ),
        (
            (
                ("a", 0),
                ("34", "7-8"),
                ("1", 3),
                ("aba", 90),
                ("abac", True),
                ("bac", [17]),
            ),
            "abal",
            False,
        ),
    ),
)
def test_has_key(tree_elements, key, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = has_key(dummy_tree, key)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,key,expected",
    (
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 90, 90),
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 17, [17]),
        (
            (
                ("a", 0),
                ("34", "7-8"),
                ("1", 3),
                ("aba", 90),
                ("abac", True),
                ("bac", [17]),
            ),
            "abac",
            True,
        ),
        (
            (
                ("a", 0),
                ("34", "7-8"),
                ("1", 3),
                ("aba", 90),
                ("abac", True),
                ("bac", [17]),
            ),
            "a",
            0,
        ),
    ),
)
def test_get_value(tree_elements, key, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = get_value(dummy_tree, key)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,expected",
    (
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 90),
        (
            (
                ("a", 0),
                ("34", "7-8"),
                ("1", 3),
                ("aba", 90),
                ("abac", True),
                ("bac", [17]),
            ),
            "bac",
        ),
        (((1000, 0),), 1000),
    ),
)
def test_get_maximum_key(tree_elements, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = get_maximum_key(dummy_tree)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,expected",
    (
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 1),
        (
            (
                ("a", 0),
                ("34", "7-8"),
                ("1", 3),
                ("aba", 90),
                ("abac", True),
                ("bac", [17]),
            ),
            "1",
        ),
        (((1000, 0),), 1000),
    ),
)
def test_get_minimum_key(tree_elements, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = get_minimum_key(dummy_tree)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,key,expected",
    (
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 17, 34),
        (((1, 0), (2, "7-8"), (4, 3), (8, 90), (16, True), (32, [17])), 15, 16),
        (((1000, 0),), 1, 1000),
    ),
)
def test_get_higher_bound(tree_elements, key, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = get_upper_bound(dummy_tree, key)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,key,expected",
    (
        (((12, 0), (34, "7-8"), (1, 3), (90, 90), (5, True), (17, [17])), 17, 17),
        (((1, 0), (2, "7-8"), (4, 3), (8, 90), (16, True), (32, [17])), 15, 16),
        (((1000, 0),), 1, 1000),
    ),
)
def test_get_lower_bound(tree_elements, key, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = get_lower_bound(dummy_tree, key)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,key",
    (
        ((), -10),
        (((1, 1), (2, 2), (3, 3)), 4),
        ((("TEST", 13), ("text", 24), ("abc", 0)), "test"),
    ),
)
def test_error_get_value(tree_elements, key):
    dummy_tree = create_dummy_tree(tree_elements)
    with pytest.raises(ValueError):
        get_value(dummy_tree, key)


@pytest.mark.parametrize(
    "tree_elements,key",
    (
        (((1, 1), (2, 2), (4, 4)), 3),
        ((("hello", 1), ("world", 2), ("!", 77)), "HELLO"),
    ),
)
def test_error_remove(tree_elements, key):
    dummy_tree = create_dummy_tree(tree_elements)
    with pytest.raises(ValueError):
        remove(dummy_tree, key)


@pytest.mark.parametrize("key", (-10, 4, "test"))
def test_error_remove_in_empty_tree(key):
    dummy_tree = create_tree_map()
    with pytest.raises(ValueError):
        remove(dummy_tree, key)


@pytest.mark.parametrize(
    "tree_elements,key",
    (
        (((1, 1), (2, 2), (4, 4)), 5),
        (((34, 34), (52, 52), (84, 84)), 84),
    ),
)
def test_error_get_higher_bound(tree_elements, key):
    dummy_tree = create_dummy_tree(tree_elements)
    with pytest.raises(ValueError):
        get_upper_bound(dummy_tree, key)


@pytest.mark.parametrize(
    "tree_elements,key",
    (
        (((1, 1), (2, 2), (4, 4)), 5),
        (((34, 34), (52, 52), (84, 84)), 85),
    ),
)
def test_error_get_lower_bound(tree_elements, key):
    dummy_tree = create_dummy_tree(tree_elements)
    with pytest.raises(ValueError):
        get_lower_bound(dummy_tree, key)


def test_error_get_maximum():
    dummy_tree = create_tree_map()
    with pytest.raises(ValueError):
        get_maximum_key(dummy_tree)


def test_error_get_minimum():
    dummy_tree = create_tree_map()
    with pytest.raises(ValueError):
        get_minimum_key(dummy_tree)
