import pytest
from src.homework.Homework_6.avl_tree import (
    TreeMap,
    TreeNode,
    create_tree_map,
    put,
    join,
    split,
    get_all_keys,
    remove_keys,
)


def create_dummy_tree(tree_elements):
    dummy_tree = create_tree_map()
    for key, value in tree_elements:
        put(dummy_tree, key, value)
    return dummy_tree


@pytest.mark.parametrize(
    "tree_elements,key,expected",
    (
        ((), 12, (TreeMap(root=None), TreeMap(root=None))),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            12,
            (
                TreeMap(
                    root=TreeNode(
                        key=7,
                        value=7,
                        left=TreeNode(
                            key=3,
                            value=3,
                            left=TreeNode(
                                key=1,
                                value=1,
                                left=TreeNode(
                                    key=0,
                                    value=0,
                                    left=None,
                                    right=None,
                                    height=0,
                                    size=1,
                                ),
                                right=TreeNode(
                                    key=2,
                                    value=2,
                                    left=None,
                                    right=None,
                                    height=0,
                                    size=1,
                                ),
                                height=1,
                                size=3,
                            ),
                            right=TreeNode(
                                key=5,
                                value=5,
                                left=TreeNode(
                                    key=4,
                                    value=4,
                                    left=None,
                                    right=None,
                                    height=0,
                                    size=1,
                                ),
                                right=TreeNode(
                                    key=6,
                                    value=6,
                                    left=None,
                                    right=None,
                                    height=0,
                                    size=1,
                                ),
                                height=1,
                                size=3,
                            ),
                            height=2,
                            size=7,
                        ),
                        right=TreeNode(
                            key=9,
                            value=9,
                            left=TreeNode(
                                key=8, value=8, left=None, right=None, height=0, size=1
                            ),
                            right=None,
                            height=1,
                            size=2,
                        ),
                        height=3,
                        size=10,
                    )
                ),
                TreeMap(root=None),
            ),
        ),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            0,
            (
                TreeMap(root=None),
                TreeMap(
                    root=TreeNode(
                        key=7,
                        value=7,
                        left=TreeNode(
                            key=5,
                            value=5,
                            left=TreeNode(
                                key=4,
                                value=4,
                                left=TreeNode(
                                    key=1,
                                    value=1,
                                    left=TreeNode(
                                        key=0,
                                        value=0,
                                        left=None,
                                        right=None,
                                        height=0,
                                        size=1,
                                    ),
                                    right=TreeNode(
                                        key=3,
                                        value=3,
                                        left=TreeNode(
                                            key=2,
                                            value=2,
                                            left=None,
                                            right=None,
                                            height=0,
                                            size=1,
                                        ),
                                        right=None,
                                        height=1,
                                        size=2,
                                    ),
                                    height=2,
                                    size=4,
                                ),
                                right=None,
                                height=3,
                                size=5,
                            ),
                            right=TreeNode(
                                key=6, value=6, left=None, right=None, height=0, size=1
                            ),
                            height=4,
                            size=7,
                        ),
                        right=TreeNode(
                            key=8,
                            value=8,
                            left=None,
                            right=TreeNode(
                                key=9, value=9, left=None, right=None, height=0, size=1
                            ),
                            height=1,
                            size=2,
                        ),
                        height=5,
                        size=10,
                    )
                ),
            ),
        ),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            5,
            (
                TreeMap(
                    root=TreeNode(
                        key=1,
                        value=1,
                        left=TreeNode(
                            key=0, value=0, left=None, right=None, height=0, size=1
                        ),
                        right=TreeNode(
                            key=3,
                            value=3,
                            left=TreeNode(
                                key=2, value=2, left=None, right=None, height=0, size=1
                            ),
                            right=TreeNode(
                                key=4, value=4, left=None, right=None, height=0, size=1
                            ),
                            height=1,
                            size=3,
                        ),
                        height=2,
                        size=5,
                    )
                ),
                TreeMap(
                    root=TreeNode(
                        key=8,
                        value=8,
                        left=TreeNode(
                            key=6,
                            value=6,
                            left=TreeNode(
                                key=5, value=5, left=None, right=None, height=0, size=1
                            ),
                            right=TreeNode(
                                key=7, value=7, left=None, right=None, height=0, size=1
                            ),
                            height=1,
                            size=3,
                        ),
                        right=TreeNode(
                            key=9, value=9, left=None, right=None, height=0, size=1
                        ),
                        height=2,
                        size=5,
                    )
                ),
            ),
        ),
    ),
)
def test_split_tree(tree_elements, key, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = split(dummy_tree, key)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,another_elements,expected",
    (
        ((), (), TreeMap(root=None)),
        (
            ((0, 0), (1, 1), (2, 2)),
            (),
            TreeMap(
                root=TreeNode(
                    key=1,
                    value=1,
                    left=TreeNode(
                        key=0, value=0, left=None, right=None, height=0, size=1
                    ),
                    right=TreeNode(
                        key=2, value=2, left=None, right=None, height=0, size=1
                    ),
                    height=1,
                    size=3,
                )
            ),
        ),
        (
            ((0, 0), (1, 1), (2, 2)),
            ((6, 6), (7, 7), (8, 8)),
            TreeMap(
                root=TreeNode(
                    key=6,
                    value=6,
                    left=TreeNode(
                        key=1,
                        value=1,
                        left=TreeNode(
                            key=0, value=0, left=None, right=None, height=0, size=1
                        ),
                        right=TreeNode(
                            key=2, value=2, left=None, right=None, height=0, size=1
                        ),
                        height=1,
                        size=3,
                    ),
                    right=TreeNode(
                        key=7,
                        value=7,
                        left=None,
                        right=TreeNode(
                            key=8, value=8, left=None, right=None, height=0, size=1
                        ),
                        height=1,
                        size=2,
                    ),
                    height=2,
                    size=6,
                )
            ),
        ),
        (
            ((10, 10), (11, 11), (12, 12)),
            ((2, 2), (3, 3)),
            TreeMap(
                root=TreeNode(
                    key=11,
                    value=11,
                    left=TreeNode(
                        key=3,
                        value=3,
                        left=TreeNode(
                            key=2, value=2, left=None, right=None, height=0, size=1
                        ),
                        right=TreeNode(
                            key=10, value=10, left=None, right=None, height=0, size=1
                        ),
                        height=1,
                        size=3,
                    ),
                    right=TreeNode(
                        key=12, value=12, left=None, right=None, height=0, size=1
                    ),
                    height=2,
                    size=5,
                )
            ),
        ),
        (
            ((101, 101),),
            ((13, 13), (14, 14), (15, 15), (16, 16)),
            TreeMap(
                root=TreeNode(
                    key=14,
                    value=14,
                    left=TreeNode(
                        key=13, value=13, left=None, right=None, height=0, size=1
                    ),
                    right=TreeNode(
                        key=16,
                        value=16,
                        left=TreeNode(
                            key=15, value=15, left=None, right=None, height=0, size=1
                        ),
                        right=TreeNode(
                            key=101, value=101, left=None, right=None, height=0, size=1
                        ),
                        height=1,
                        size=3,
                    ),
                    height=2,
                    size=5,
                )
            ),
        ),
    ),
)
def test_join_tree(tree_elements, another_elements, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    another_dummy_tree = create_dummy_tree(another_elements)
    function = join(dummy_tree, another_dummy_tree)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,left,right,expected",
    (
        ((), 0, 0, []),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            0,
            0,
            [],
        ),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            0,
            1,
            [0],
        ),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            5,
            8,
            [5, 6, 7],
        ),
        (((13, 13), (14, 14), (15, 15), (16, 16)), 16, 1000, [16]),
        (
            ((16, 16), (9, 9), (-123, -123), (0, 0), (1, 1)),
            -200,
            200,
            [-123, 0, 1, 9, 16],
        ),
    ),
)
def test_get_all_keys(tree_elements, left, right, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    function = get_all_keys(dummy_tree, left, right)
    assert function == expected


@pytest.mark.parametrize(
    "tree_elements,left,right,expected",
    (
        ((), 0, 15, TreeMap(root=None)),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            12,
            14,
            TreeMap(
                root=TreeNode(
                    key=7,
                    value=7,
                    left=TreeNode(
                        key=3,
                        value=3,
                        left=TreeNode(
                            key=1,
                            value=1,
                            left=TreeNode(
                                key=0, value=0, left=None, right=None, height=0, size=1
                            ),
                            right=TreeNode(
                                key=2, value=2, left=None, right=None, height=0, size=1
                            ),
                            height=1,
                            size=3,
                        ),
                        right=TreeNode(
                            key=5,
                            value=5,
                            left=TreeNode(
                                key=4, value=4, left=None, right=None, height=0, size=1
                            ),
                            right=TreeNode(
                                key=6, value=6, left=None, right=None, height=0, size=1
                            ),
                            height=1,
                            size=3,
                        ),
                        height=2,
                        size=7,
                    ),
                    right=TreeNode(
                        key=9,
                        value=9,
                        left=TreeNode(
                            key=8, value=8, left=None, right=None, height=0, size=1
                        ),
                        right=None,
                        height=1,
                        size=2,
                    ),
                    height=3,
                    size=10,
                )
            ),
        ),
        (
            (
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
            ),
            6,
            9,
            TreeMap(
                root=TreeNode(
                    key=3,
                    value=3,
                    left=TreeNode(
                        key=1,
                        value=1,
                        left=TreeNode(
                            key=0, value=0, left=None, right=None, height=0, size=1
                        ),
                        right=TreeNode(
                            key=2, value=2, left=None, right=None, height=0, size=1
                        ),
                        height=1,
                        size=3,
                    ),
                    right=TreeNode(
                        key=5,
                        value=5,
                        left=TreeNode(
                            key=4, value=4, left=None, right=None, height=0, size=1
                        ),
                        right=TreeNode(
                            key=9, value=9, left=None, right=None, height=0, size=1
                        ),
                        height=1,
                        size=3,
                    ),
                    height=2,
                    size=7,
                )
            ),
        ),
        (
            ((9, 9), (12, 12), (101, 101), (-12, -12), (76, 76)),
            -20,
            200,
            TreeMap(root=None),
        ),
    ),
)
def test_remove_keys(tree_elements, left, right, expected):
    dummy_tree = create_dummy_tree(tree_elements)
    remove_keys(dummy_tree, left, right)
    assert dummy_tree == expected


@pytest.mark.parametrize(
    "tree_elements,left,right",
    (
        ((), 12, 3),
        (((12, 12), (3, 3), (40, 40), (-31, -31)), 90, 0),
        ((("a", 0), ("acb", 12), ("cbd", 144)), "bd", "ac"),
        (
            ((("ab", 1), 10), (("bd", 2), 13), (("nnn", 3), 16)),
            ("test", 13),
            ("test", 1),
        ),
    ),
)
def test_error_get_all_keys(tree_elements, left, right):
    dummy_tree = create_dummy_tree(tree_elements)
    with pytest.raises(ValueError):
        get_all_keys(dummy_tree, left, right)


@pytest.mark.parametrize(
    "tree_elements,left,right",
    (
        ((), 36, 35),
        (((12, 12), (3, 3), (40, 40), (-31, -31)), 101, -101),
        ((("a", 0), ("acb", 12), ("cbd", 144)), "bdc", "bd"),
        (
            ((("ab", 1), 10), (("bd", 2), 13), (("nnn", 3), 16)),
            ("test", 13),
            ("test", 12),
        ),
    ),
)
def test_error_get_all_keys(tree_elements, left, right):
    dummy_tree = create_dummy_tree(tree_elements)
    with pytest.raises(ValueError):
        remove_keys(dummy_tree, left, right)
