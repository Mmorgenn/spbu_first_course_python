import pytest
from src.homework.Homework_6.Homework_6_1.shopping import *


def create_dummy_storage(size_count_list):
    dummy_storage = create_tree_map()
    for size_count in size_count_list:
        put(dummy_storage, *size_count)
    return dummy_storage


@pytest.mark.parametrize(
    "storage_elements,size,count,expected",
    (
        (((30, 20), (31, 15), (33, 42), (34, 56)), 29, 10, 10),
        (((30, 20), (31, 15), (33, 42), (34, 56)), 30, 10, 30),
        (((30, 20), (31, 15), (33, 42), (34, 56)), 33, 18, 60),
    ),
)
def test_add(storage_elements, size, count, expected):
    dummy_storage = create_dummy_storage(storage_elements)
    add(dummy_storage, size, count)
    assert get_value(dummy_storage, size) == expected


@pytest.mark.parametrize(
    "storage_elements,size,expected",
    (
        (((12, 340), (27, 150), (43, 452), (56, 56)), 12, 340),
        (((30, 20), (31, 15), (33, 42), (34, 56)), 30, 20),
        (((3, 2), (4, 15), (10, 42), (34, 7)), 33, 0),
    ),
)
def test_get(storage_elements, size, expected):
    dummy_storage = create_dummy_storage(storage_elements)
    assert get(dummy_storage, size) == expected


@pytest.mark.parametrize(
    "storage_elements,size,expected",
    (
        (((12, 340), (27, 150), (43, 452), (56, 56)), 12, 339),
        (((30, 20), (31, 15), (33, 42), (34, 56)), 29, 19),
        (((3, 2), (4, 15), (10, 42), (34, 7)), 5, 41),
    ),
)
def test_select(storage_elements, size, expected):
    dummy_storage = create_dummy_storage(storage_elements)
    issued_size = int(select(dummy_storage, size))
    assert get_value(dummy_storage, issued_size) == expected


@pytest.mark.parametrize(
    "storage_elements,size",
    (
        (((12, 340), (27, 150), (43, 452), (56, 56)), 57),
        (((30, 20), (31, 15), (33, 42), (34, 56)), 37),
        (((3, 2), (4, 15), (10, 42), (34, 7)), 56),
    ),
)
def test_select_error(storage_elements, size):
    dummy_storage = create_dummy_storage(storage_elements)
    assert select(dummy_storage, size) == "SORRY"


@pytest.mark.parametrize(
    "storage_elements,size",
    (
        (((12, 340), (27, 150), (43, 452), (56, 1)), 55),
        (((30, 20), (31, 15), (33, 1), (34, 56)), 33),
        (((3, 2), (4, 15), (10, 1), (34, 7)), 10),
    ),
)
def test_select_if_count_one(storage_elements, size):
    dummy_storage = create_dummy_storage(storage_elements)
    issued_size = int(select(dummy_storage, size))
    assert has_key(dummy_storage, issued_size) is False
