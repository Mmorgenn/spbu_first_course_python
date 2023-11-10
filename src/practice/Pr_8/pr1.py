from dataclasses import dataclass
from typing import Generic, Callable, Any, NamedTuple, TypeVar

DEFAULT_HASH_TABLE_SIZE = 8
LOAD_FACTOR_THRESHOLD = 2 / 3
Value = TypeVar("Value")
Key = TypeVar("Key")

Entry = NamedTuple("Entry", [("key", Any), ("value", Any)])


@dataclass
class Bucket(Generic[Key, Value]):
    entries: list[Entry]


@dataclass
class HashTable(Generic[Key, Value]):
    buckets: list[Bucket | None]
    hash_function: Callable[[Any], int]
    size: int = 0
    total_buckets: int = 0

    def get_index(self, key):
        return self.hash_function(key) % self.total_buckets


def create_hash_table(hash_fn: Callable) -> HashTable:
    return HashTable(
        hash_function=hash_fn,
        buckets=[None] * DEFAULT_HASH_TABLE_SIZE,
        total_buckets=DEFAULT_HASH_TABLE_SIZE,
    )


def delete_hash_table(hash_table: HashTable):
    for i in range(hash_table.total_buckets):
        del hash_table.buckets[i]
    del hash_table


def _check_load_factor(hash_table: HashTable):
    load_factor = hash_table.size / hash_table.total_buckets
    if load_factor > LOAD_FACTOR_THRESHOLD:
        _resize(hash_table)


def _resize(hash_table: HashTable):
    new_size = hash_table.total_buckets * 2
    new_buckets = [None] * new_size
    item_list = get_items(hash_table)
    hash_table.buckets = new_buckets
    hash_table.total_buckets = new_size
    hash_table.size = 0
    for entry in item_list:
        put(hash_table, entry.key, entry.value)


def _get_node_from_bucket(bucket: list[Entry], key: Key) -> Entry | None:
    for entry in bucket:
        if entry.key == key:
            return entry
    return None


def put(hash_table: HashTable, key: Any, value: Any):
    _check_load_factor(hash_table)
    index = hash_table.get_index(key)
    if hash_table.buckets[index] is None:
        hash_table.buckets[index] = Bucket([Entry(key, value)])
        hash_table.size += 1
    else:
        old_entry = _get_node_from_bucket(hash_table.buckets[index].entries, key)
        if old_entry is None:
            hash_table.buckets[index] = Bucket([Entry(key, value)])
            hash_table.size += 1
        else:
            hash_table.buckets[index].entries.remove(old_entry)
            hash_table.buckets[index].entries.append(Entry(key, value))


def remove(hash_table: HashTable, key: Key) -> Value:
    if not has_key(hash_table, key):
        raise KeyError(f"No such key")
    index = hash_table.get_index(key)
    need_entry = _get_node_from_bucket(hash_table.buckets[index].entries, key)
    hash_table.buckets[index] = None
    hash_table.size -= 1
    return need_entry.value


def has_key(hash_table: HashTable, key: Any) -> bool:
    index = hash_table.get_index(key)
    if key > hash_table.total_buckets:
        return False
    return hash_table.buckets[index] is not None


def get_value(hash_table: HashTable, key: Key) -> Value:
    if not has_key(hash_table, key):
        raise KeyError(f"No such key")
    index = hash_table.hash_function(key)
    return hash_table.buckets[index].entries[0].value


def get_items(hash_table: HashTable) -> list:
    result_list, curr_index = [], 0
    while len(result_list) != hash_table.size:
        if hash_table.buckets[curr_index] is not None:
            result_list.append(hash_table.buckets[curr_index].entries[0])
        curr_index += 1
    return result_list
