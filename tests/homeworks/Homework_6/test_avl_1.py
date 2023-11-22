import pytest
from src.homework.Homework_6.avl_tree import (
    TreeMap,
    TreeNode,
    create_tree_map,
    put,
    remove,
    has_key,
    get_value,
    get_maximum_key,
    get_minimum_key,
    get_higher_bound,
    get_lower_bound,
)


def create_dummy_tree(key_value_list):
    dummy_tree = create_tree_map()
    for key_value in key_value_list:
        put(dummy_tree, *key_value)
    return dummy_tree


@pytest.mark.parametrize(
    "tree_elements,element,expected",
    (
        (
            ((1, 2), (2, "text"), (3, [0]), (4, True), (5, 1.0), (6, -10), (7, "hey")),
            (7, 7),
            TreeMap(
                root=TreeNode(
                    key=4,
                    value=True,
                    left=TreeNode(
                        key=2,
                        value="text",
                        left=TreeNode(key=1, value=2, left=None, right=None, height=0),
                        right=TreeNode(
                            key=3, value=[0], left=None, right=None, height=0
                        ),
                        height=1,
                    ),
                    right=TreeNode(
                        key=6,
                        value=-10,
                        left=TreeNode(
                            key=5, value=1.0, left=None, right=None, height=0
                        ),
                        right=TreeNode(key=7, value=7, left=None, right=None, height=0),
                        height=1,
                    ),
                    height=2,
                )
            ),
        ),
        (
            ((1, 2), (2, "text"), (3, [0]), (4, True), (5, 1.0), (6, -10), (7, "hey")),
            (8, 8),
            TreeMap(
                root=TreeNode(
                    key=4,
                    value=True,
                    left=TreeNode(
                        key=2,
                        value="text",
                        left=TreeNode(key=1, value=2, left=None, right=None, height=0),
                        right=TreeNode(
                            key=3, value=[0], left=None, right=None, height=0
                        ),
                        height=1,
                    ),
                    right=TreeNode(
                        key=6,
                        value=-10,
                        left=TreeNode(
                            key=5, value=1.0, left=None, right=None, height=0
                        ),
                        right=TreeNode(
                            key=7,
                            value="hey",
                            left=None,
                            right=TreeNode(
                                key=8, value=8, left=None, right=None, height=0
                            ),
                            height=1,
                        ),
                        height=2,
                    ),
                    height=3,
                )
            ),
        ),
        (
            (
                (1, 2),
                (2, "text"),
                (3, [0]),
                (4, True),
                (5, 1.0),
                (6, -10),
                (7, "hey"),
                (8, 8),
            ),
            (100, ("test", 1)),
            TreeMap(
                root=TreeNode(
                    key=4,
                    value=True,
                    left=TreeNode(
                        key=2,
                        value="text",
                        left=TreeNode(key=1, value=2, left=None, right=None, height=0),
                        right=TreeNode(
                            key=3, value=[0], left=None, right=None, height=0
                        ),
                        height=1,
                    ),
                    right=TreeNode(
                        key=6,
                        value=-10,
                        left=TreeNode(
                            key=5, value=1.0, left=None, right=None, height=0
                        ),
                        right=TreeNode(
                            key=8,
                            value=8,
                            left=TreeNode(
                                key=7, value="hey", left=None, right=None, height=0
                            ),
                            right=TreeNode(
                                key=100,
                                value=("test", 1),
                                left=None,
                                right=None,
                                height=0,
                            ),
                            height=1,
                        ),
                        height=2,
                    ),
                    height=3,
                )
            ),
        ),
        (
            (
                (1, 2),
                (2, "text"),
                (3, [0]),
                (4, True),
                (5, 1.0),
                (6, -10),
                (7, "hey"),
                (8, 8),
                (100, ("test", 1)),
            ),
            (77, 77),
            TreeMap(
                root=TreeNode(
                    key=4,
                    value=True,
                    left=TreeNode(
                        key=2,
                        value="text",
                        left=TreeNode(key=1, value=2, left=None, right=None, height=0),
                        right=TreeNode(
                            key=3, value=[0], left=None, right=None, height=0
                        ),
                        height=1,
                    ),
                    right=TreeNode(
                        key=8,
                        value=8,
                        left=TreeNode(
                            key=6,
                            value=-10,
                            left=TreeNode(
                                key=5, value=1.0, left=None, right=None, height=0
                            ),
                            right=TreeNode(
                                key=7, value="hey", left=None, right=None, height=0
                            ),
                            height=1,
                        ),
                        right=TreeNode(
                            key=100,
                            value=("test", 1),
                            left=TreeNode(
                                key=77, value=77, left=None, right=None, height=0
                            ),
                            right=None,
                            height=1,
                        ),
                        height=2,
                    ),
                    height=3,
                )
            ),
        ),
    ),
)
def test_put(tree_elements, element, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    put(dummy_tree, *element)
    assert dummy_tree == expected


@pytest.mark.parametrize(
    "tree_elements,key,expected",
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
            6,
            (
                TreeMap(
                    root=TreeNode(
                        key=4,
                        value=5,
                        left=TreeNode(
                            key=2,
                            value=3,
                            left=TreeNode(
                                key=1, value=2, left=None, right=None, height=0
                            ),
                            right=TreeNode(
                                key=3, value=4, left=None, right=None, height=0
                            ),
                            height=1,
                        ),
                        right=TreeNode(
                            key=8,
                            value=9,
                            left=TreeNode(
                                key=7,
                                value=8,
                                left=TreeNode(
                                    key=5, value=6, left=None, right=None, height=0
                                ),
                                right=None,
                                height=1,
                            ),
                            right=TreeNode(
                                key=9,
                                value=10,
                                left=None,
                                right=TreeNode(
                                    key=10, value=11, left=None, right=None, height=0
                                ),
                                height=1,
                            ),
                            height=2,
                        ),
                        height=3,
                    )
                ),
                7,
            ),
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
            (
                TreeMap(
                    root=TreeNode(
                        key=4,
                        value=5,
                        left=TreeNode(
                            key=2,
                            value=3,
                            left=TreeNode(
                                key=1, value=2, left=None, right=None, height=0
                            ),
                            right=TreeNode(
                                key=3, value=4, left=None, right=None, height=0
                            ),
                            height=1,
                        ),
                        right=TreeNode(
                            key=8,
                            value=9,
                            left=TreeNode(
                                key=6,
                                value=7,
                                left=TreeNode(
                                    key=5, value=6, left=None, right=None, height=0
                                ),
                                right=TreeNode(
                                    key=7, value=8, left=None, right=None, height=0
                                ),
                                height=1,
                            ),
                            right=TreeNode(
                                key=9, value=10, left=None, right=None, height=0
                            ),
                            height=2,
                        ),
                        height=3,
                    )
                ),
                11,
            ),
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
            9,
            (
                TreeMap(
                    root=TreeNode(
                        key=4,
                        value=5,
                        left=TreeNode(
                            key=2,
                            value=3,
                            left=TreeNode(
                                key=1, value=2, left=None, right=None, height=0
                            ),
                            right=TreeNode(
                                key=3, value=4, left=None, right=None, height=0
                            ),
                            height=1,
                        ),
                        right=TreeNode(
                            key=8,
                            value=9,
                            left=TreeNode(
                                key=6,
                                value=7,
                                left=TreeNode(
                                    key=5, value=6, left=None, right=None, height=0
                                ),
                                right=TreeNode(
                                    key=7, value=8, left=None, right=None, height=0
                                ),
                                height=1,
                            ),
                            right=TreeNode(
                                key=10, value=11, left=None, right=None, height=0
                            ),
                            height=2,
                        ),
                        height=3,
                    )
                ),
                10,
            ),
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
            4,
            (
                TreeMap(
                    root=TreeNode(
                        key=5,
                        value=6,
                        left=TreeNode(
                            key=2,
                            value=3,
                            left=TreeNode(
                                key=1, value=2, left=None, right=None, height=0
                            ),
                            right=TreeNode(
                                key=3, value=4, left=None, right=None, height=0
                            ),
                            height=1,
                        ),
                        right=TreeNode(
                            key=8,
                            value=9,
                            left=TreeNode(
                                key=6,
                                value=7,
                                left=None,
                                right=TreeNode(
                                    key=7, value=8, left=None, right=None, height=0
                                ),
                                height=1,
                            ),
                            right=TreeNode(
                                key=9,
                                value=10,
                                left=None,
                                right=TreeNode(
                                    key=10, value=11, left=None, right=None, height=0
                                ),
                                height=1,
                            ),
                            height=2,
                        ),
                        height=3,
                    )
                ),
                5,
            ),
        ),
    ),
)
def test_remove(tree_elements, key, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    value = remove(dummy_tree, key)
    assert dummy_tree, value == expected


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
    function = get_higher_bound(dummy_tree, key)
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
        (((1, 1), (2, 2), (4, 4)), 3),
        ((("hello", 1), ("world", 2), ("!", 77)), "HELLO"),
    ),
)
def test_error_in_remove(tree_elements, key):
    dummy_tree = create_dummy_tree(tree_elements)
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
        get_higher_bound(dummy_tree, key)


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


@pytest.mark.parametrize("key", (-10, 4, "test"))
def test_error_in_empty_tree(key):
    dummy_tree = create_tree_map()
    with pytest.raises(ValueError):
        remove(dummy_tree, key)
    with pytest.raises(ValueError):
        get_value(dummy_tree, key)
    with pytest.raises(ValueError):
        get_maximum_key(dummy_tree)
    with pytest.raises(ValueError):
        get_minimum_key(dummy_tree)
