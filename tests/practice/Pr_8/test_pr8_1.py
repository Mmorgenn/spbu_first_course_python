import pytest
from src.practice.Pr_8.pr1 import (
    HashTable,
    Bucket,
    Entry,
    create_hash_table,
    put,
    remove,
    has_key,
    get_value,
    get_items,
)


def test_create_hash_table():
    function = create_hash_table(hash)
    assert function == HashTable(
        hash_function=hash, buckets=[None] * 8, total_buckets=8
    )


HASH_TABLE_1 = HashTable(
    buckets=[None] * 8, hash_function=hash, size=0, total_buckets=8
)
HASH_TABLE_2 = HashTable(
    buckets=[
        None,
        Bucket(entries=[Entry(key=1, value="12")]),
        Bucket(entries=[Entry(key=2, value="2")]),
        Bucket(entries=[Entry(key=3, value="12")]),
        Bucket(entries=[Entry(key=4, value="12")]),
        Bucket(entries=[Entry(key=5, value="12")]),
        Bucket(entries=[Entry(key=6, value="12")]),
        None,
    ],
    hash_function=hash,
    size=6,
    total_buckets=8,
)
HASH_TABLE_3 = HashTable(
    buckets=[
        None,
        Bucket(entries=[Entry(key=1, value="12")]),
        Bucket(entries=[Entry(key=2, value="2")]),
        Bucket(entries=[Entry(key=3, value="12")]),
        Bucket(entries=[Entry(key=4, value="12")]),
        Bucket(entries=[Entry(key=5, value="21")]),
        Bucket(entries=[Entry(key=6, value="12")]),
        Bucket(entries=[Entry(key=7, value=True)]),
        Bucket(entries=[Entry(key=8, value=["12", 1])]),
        None,
        Bucket(entries=[Entry(key=10, value=())]),
        None,
        None,
        None,
        None,
        None,
    ],
    hash_function=hash,
    size=9,
    total_buckets=16,
)
HASH_TABLE_4 = HashTable(
    buckets=[
        None,
        Bucket(entries=[Entry(key=1, value="12")]),
        Bucket(entries=[Entry(key=2, value="2")]),
        Bucket(entries=[Entry(key=3, value="12")]),
        Bucket(entries=[Entry(key=4, value="12")]),
        Bucket(entries=[Entry(key=5, value="12")]),
        Bucket(entries=[Entry(key=6, value="12")]),
        None,
    ],
    hash_function=hash,
    size=6,
    total_buckets=8,
)


@pytest.mark.parametrize(
    "table,key,expected",
    (
        (HASH_TABLE_1, 1, False),
        (HASH_TABLE_2, 1, True),
        (HASH_TABLE_3, 0, False),
        (HASH_TABLE_3, 8, True),
    ),
)
def test_has_key(table, key, expected):
    function = has_key(table, key)
    assert function == expected


@pytest.mark.parametrize(
    "table,key,expected",
    ((HASH_TABLE_2, 1, "12"), (HASH_TABLE_2, 5, "12"), (HASH_TABLE_3, 8, ["12", 1])),
)
def test_get_value(table, key, expected):
    function = get_value(table, key)
    assert function == expected


@pytest.mark.parametrize(
    "table,expected",
    (
        (HASH_TABLE_1, []),
        (
            HASH_TABLE_2,
            [
                Entry(key=1, value="12"),
                Entry(key=2, value="2"),
                Entry(key=3, value="12"),
                Entry(key=4, value="12"),
                Entry(key=5, value="12"),
                Entry(key=6, value="12"),
            ],
        ),
        (
            HASH_TABLE_3,
            [
                Entry(key=1, value="12"),
                Entry(key=2, value="2"),
                Entry(key=3, value="12"),
                Entry(key=4, value="12"),
                Entry(key=5, value="21"),
                Entry(key=6, value="12"),
                Entry(key=7, value=True),
                Entry(key=8, value=["12", 1]),
                Entry(key=10, value=()),
            ],
        ),
    ),
)
def test_get_items(table, expected):
    function = get_items(table)
    assert function == expected


@pytest.mark.parametrize(
    "table, key, expected",
    (
        (
            HASH_TABLE_1,
            1,
            HashTable(
                buckets=[
                    None,
                    None,
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    Bucket(entries=[Entry(key=5, value="12")]),
                    Bucket(entries=[Entry(key=6, value="12")]),
                    None,
                ],
                hash_function=hash,
                size=5,
                total_buckets=8,
            ),
        ),
        (
            HASH_TABLE_2,
            5,
            HashTable(
                buckets=[
                    None,
                    None,
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    None,
                    Bucket(entries=[Entry(key=6, value="12")]),
                    None,
                ],
                hash_function=hash,
                size=4,
                total_buckets=8,
            ),
        ),
        (
            HASH_TABLE_3,
            8,
            HashTable(
                buckets=[
                    None,
                    Bucket(entries=[Entry(key=1, value="12")]),
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    Bucket(entries=[Entry(key=5, value="21")]),
                    Bucket(entries=[Entry(key=6, value="12")]),
                    Bucket(entries=[Entry(key=7, value=True)]),
                    None,
                    None,
                    Bucket(entries=[Entry(key=10, value=())]),
                    None,
                    None,
                    None,
                    None,
                    None,
                ],
                hash_function=hash,
                size=8,
                total_buckets=16,
            ),
        ),
    ),
)
def test_remove(table, key, expected):
    new_table = table
    remove(new_table, key)
    assert new_table == expected


@pytest.mark.parametrize(
    "table, key, expected",
    (
        (
            HASH_TABLE_2,
            1,
            HashTable(
                buckets=[
                    None,
                    None,
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    Bucket(entries=[Entry(key=5, value="12")]),
                    Bucket(entries=[Entry(key=6, value="12")]),
                    None,
                ],
                hash_function=hash,
                size=5,
                total_buckets=8,
            ),
        ),
        (
            HASH_TABLE_2,
            5,
            HashTable(
                buckets=[
                    None,
                    None,
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    None,
                    Bucket(entries=[Entry(key=6, value="12")]),
                    None,
                ],
                hash_function=hash,
                size=4,
                total_buckets=8,
            ),
        ),
        (
            HASH_TABLE_3,
            8,
            HashTable(
                buckets=[
                    None,
                    Bucket(entries=[Entry(key=1, value="12")]),
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    Bucket(entries=[Entry(key=5, value="21")]),
                    Bucket(entries=[Entry(key=6, value="12")]),
                    Bucket(entries=[Entry(key=7, value=True)]),
                    None,
                    None,
                    Bucket(entries=[Entry(key=10, value=())]),
                    None,
                    None,
                    None,
                    None,
                    None,
                ],
                hash_function=hash,
                size=8,
                total_buckets=16,
            ),
        ),
    ),
)
def test_remove(table, key, expected):
    new_table = table
    remove(new_table, key)
    assert new_table == expected


@pytest.mark.parametrize(
    "table,key,value,expected",
    (
        (
            HASH_TABLE_1,
            2,
            "2",
            HashTable(
                buckets=[
                    None,
                    None,
                    Bucket(entries=[Entry(key=2, value="2")]),
                    None,
                    None,
                    None,
                    None,
                    None,
                ],
                hash_function=hash,
                size=1,
                total_buckets=8,
            ),
        ),
        (
            HASH_TABLE_1,
            2,
            "Yay",
            HashTable(
                buckets=[
                    None,
                    None,
                    Bucket(entries=[Entry(key=2, value="Yay")]),
                    None,
                    None,
                    None,
                    None,
                    None,
                ],
                hash_function=hash,
                size=1,
                total_buckets=8,
            ),
        ),
        (
            HASH_TABLE_4,
            7,
            "Hello",
            HashTable(
                buckets=[
                    None,
                    Bucket(entries=[Entry(key=1, value="12")]),
                    Bucket(entries=[Entry(key=2, value="2")]),
                    Bucket(entries=[Entry(key=3, value="12")]),
                    Bucket(entries=[Entry(key=4, value="12")]),
                    Bucket(entries=[Entry(key=5, value="12")]),
                    Bucket(entries=[Entry(key=6, value="12")]),
                    Bucket(entries=[Entry(key=7, value="Hello")]),
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                ],
                hash_function=hash,
                size=7,
                total_buckets=16,
            ),
        ),
    ),
)
def test_put(table, key, value, expected):
    new_table = table
    put(new_table, key, value)
    assert new_table == expected


@pytest.mark.parametrize("table,key", ((HASH_TABLE_1, 0), (HASH_TABLE_3, 17)))
def test_error_in_remove(table, key):
    with pytest.raises(KeyError):
        remove(table, key)


@pytest.mark.parametrize("table,key", ((HASH_TABLE_1, 0), (HASH_TABLE_4, 17)))
def test_error_in_get_value(table, key):
    with pytest.raises(KeyError):
        get_value(table, key)
