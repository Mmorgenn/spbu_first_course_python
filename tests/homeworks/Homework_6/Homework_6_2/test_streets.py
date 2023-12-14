import pytest
import tempfile
from src.homework.Homework_6.avl_tree import TreeMap, TreeNode, create_tree_map
from src.homework.Homework_6.Homework_6_2.streets import (
    is_correct_address,
    create,
    get,
    delete_block,
    delete_house,
    delete_street,
    get_list_addresses,
    rename,
    run_static_mode,
)


FILE_LOGS = "tests/homeworks/Homework_6/Homework_6_2/streets_logs.txt"
FILE_RESULTS = "tests/homeworks/Homework_6/Homework_6_2/streets_results.txt"


def create_dummy_directory(directory_elements):
    dummy_directory = create_tree_map()
    for address, index in directory_elements:
        create(dummy_directory, address, index)
    return dummy_directory


@pytest.mark.parametrize(
    "address,expected",
    (
        (["Юбилейный", "12", "6"], True),
        (["Петроградская", "8"], False),
        (["A", "B", "C"], False),
        (["Чечеренская", "12a", "2"], False),
        (["Ломакино", "13", "3", "1"], False),
        (["Бульварная"], False),
        (["Ивановская", "9.75", "14"], False),
    ),
)
def test_is_correct_address(address, expected):
    function = is_correct_address(address)
    assert function == expected


@pytest.mark.parametrize(
    "directory_elements,expected",
    (
        (
            ((("Центральная", "12", "21"), 787856),),
            TreeMap(
                root=TreeNode(
                    key=("Центральная", 12, 21),
                    value=787856,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
        (
            (
                (("Юбилейная", "1", "2"), 121),
                (("Юбилейная", "12", "2"), 119),
                (("Юбилейная", "1", "20"), 118),
            ),
            TreeMap(
                root=TreeNode(
                    key=("Юбилейная", 1, 20),
                    value=118,
                    left=TreeNode(
                        key=("Юбилейная", 1, 2),
                        value=121,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    right=TreeNode(
                        key=("Юбилейная", 12, 2),
                        value=119,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    height=1,
                    size=3,
                )
            ),
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "1", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            TreeMap(
                root=TreeNode(
                    key=("Лесная", 7, 8),
                    value=12000,
                    left=TreeNode(
                        key=("Лесная", 1, 2),
                        value=12100,
                        left=None,
                        right=TreeNode(
                            key=("Лесная", 1, 20),
                            value=11800,
                            left=None,
                            right=None,
                            height=0,
                            size=1,
                        ),
                        height=1,
                        size=2,
                    ),
                    right=TreeNode(
                        key=("Садовая", 3, 90),
                        value=11900,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    height=2,
                    size=4,
                )
            ),
        ),
    ),
)
def test_create(directory_elements, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    assert dummy_directory == expected


@pytest.mark.parametrize(
    "directory_elements,address,expected",
    (
        (
            ((("Центральная", "12", "21"), 787856),),
            ["Центральная", "12", "21"],
            "787856",
        ),
        (((("Центральная", "12", "21"), 787856),), ["Центральная", "1", "1"], "None"),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "1", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            ["Весенняя", "12", "23"],
            "None",
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "1", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            ["Лесная", "1", "20"],
            "11800",
        ),
    ),
)
def test_get(directory_elements, address, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    function = get(dummy_directory, address)
    assert function == expected


@pytest.mark.parametrize(
    "directory_elements,address,expected",
    (
        ((), ["Ивановская", "13", "4"], TreeMap(root=None)),
        (
            ((("Центральная", "12", "21"), 787856),),
            ["Центральная", "12", "21"],
            TreeMap(root=None),
        ),
        (
            ((("Центральная", "12", "21"), 787856),),
            ["Центральная", "34", "1"],
            TreeMap(
                root=TreeNode(
                    key=("Центральная", 12, 21),
                    value=787856,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "1", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            ["Садовая", "3", "90"],
            TreeMap(
                root=TreeNode(
                    key=("Лесная", 1, 20),
                    value=11800,
                    left=TreeNode(
                        key=("Лесная", 1, 2),
                        value=12100,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    right=TreeNode(
                        key=("Лесная", 7, 8),
                        value=12000,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    height=1,
                    size=3,
                )
            ),
        ),
    ),
)
def test_delete_block(directory_elements, address, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    delete_block(dummy_directory, address)
    assert dummy_directory == expected


@pytest.mark.parametrize(
    "directory_elements,street,house,expected",
    (
        ((), "Ивановская", 13, TreeMap(root=None)),
        (
            ((("Центральная", "12", "21"), 787856),),
            "Центральная",
            12,
            TreeMap(root=None),
        ),
        (
            ((("Центральная", "12", "21"), 787856),),
            "Центральная",
            34,
            TreeMap(
                root=TreeNode(
                    key=("Центральная", 12, 21),
                    value=787856,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "7", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            "Лесная",
            7,
            TreeMap(
                root=TreeNode(
                    key=("Садовая", 3, 90),
                    value=11900,
                    left=TreeNode(
                        key=("Лесная", 1, 20),
                        value=11800,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    right=None,
                    height=1,
                    size=2,
                )
            ),
        ),
    ),
)
def test_delete_house(directory_elements, street, house, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    delete_house(dummy_directory, street, house)
    assert dummy_directory == expected


@pytest.mark.parametrize(
    "directory_elements,street,expected",
    (
        ((), "Ивановская", TreeMap(root=None)),
        (((("Центральная", "12", "21"), 787856),), "Центральная", TreeMap(root=None)),
        (
            ((("Центральная", "12", "21"), 787856),),
            "Бульварная",
            TreeMap(
                root=TreeNode(
                    key=("Центральная", 12, 21),
                    value=787856,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "7", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            "Лесная",
            TreeMap(
                root=TreeNode(
                    key=("Садовая", 3, 90),
                    value=11900,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
    ),
)
def test_delete_street(directory_elements, street, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    delete_street(dummy_directory, street)
    assert dummy_directory == expected


@pytest.mark.parametrize(
    "directory_elements,address_1,address_2,expected",
    (
        ((), ["Строительная", "12", "3"], ["Строительная", "12", "34"], "\n"),
        (
            ((("Центральная", "12", "21"), 787856),),
            ["Центральная", "11", "3"],
            ["Центральная", "12", "34"],
            "Центральная 12 21\n\n",
        ),
        (
            ((("Центральная", "12", "21"), 787856),),
            ["Строительная", "12", "3"],
            ["Строительная", "12", "34"],
            "\n",
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "7", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            ["Лесная", "1", "1"],
            ["Лесная", "90", "1"],
            "Лесная 1 20\nЛесная 7 2\nЛесная 7 8\n\n",
        ),
    ),
)
def test_get_list(directory_elements, address_1, address_2, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    function = get_list_addresses(dummy_directory, address_1, address_2)
    assert function == expected


@pytest.mark.parametrize(
    "directory_elements,old_street,new_street,expected",
    (
        ((), "Центральная", "Ивановская", TreeMap(root=None)),
        (
            ((("Центральная", "12", "21"), 787856),),
            "Мемная",
            "Центральная",
            TreeMap(
                root=TreeNode(
                    key=("Центральная", 12, 21),
                    value=787856,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
        (
            ((("Центральная", "12", "21"), 787856),),
            "Центральная",
            "Мемная",
            TreeMap(
                root=TreeNode(
                    key=("Мемная", 12, 21),
                    value=787856,
                    left=None,
                    right=None,
                    height=0,
                    size=1,
                )
            ),
        ),
        (
            (
                (("Лесная", "7", "8"), 12000),
                (("Лесная", "1", "2"), 12100),
                (("Садовая", "3", "90"), 11900),
                (("Лесная", "1", "20"), 11800),
            ),
            "Лесная",
            "Морская",
            TreeMap(
                root=TreeNode(
                    key=("Морская", 1, 20),
                    value=11800,
                    left=TreeNode(
                        key=("Морская", 1, 2),
                        value=12100,
                        left=None,
                        right=None,
                        height=0,
                        size=1,
                    ),
                    right=TreeNode(
                        key=("Садовая", 3, 90),
                        value=11900,
                        left=TreeNode(
                            key=("Морская", 7, 8),
                            value=12000,
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
                )
            ),
        ),
    ),
)
def test_rename(directory_elements, old_street, new_street, expected):
    dummy_directory = create_dummy_directory(directory_elements)
    rename(dummy_directory, old_street, new_street)
    assert dummy_directory == expected


def test_static_mode():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as templ_file:
        test_file = templ_file.name
        directory = create_tree_map()
        run_static_mode(directory, FILE_LOGS, test_file)
        with open(test_file, mode="r") as file, open(
            FILE_RESULTS, mode="r", encoding="utf-8"
        ) as expected:
            for i in range(1562):
                assert file.readline() == expected.readline()
