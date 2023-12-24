import random


Pixel = "█"


def is_correct_size(size: str):
    if not size.isdigit():
        return False
    if 2 <= int(size) <= 1000:
        return True
    return False


def select_symmetry() -> list[bool]:
    vertical = random.choice([True, False])
    if not vertical:
        return [False, True]
    horizontal = random.choice([True, False])
    return [vertical, horizontal]


def create_row(size: int) -> list[str]:
    return [random.choice([Pixel, " "]) for _ in range(size)]


def create_symmetry_row(size: int, multiplicity_size: int) -> list[str]:
    if multiplicity_size:
        return create_symmetry_row_odd(size)
    return create_symmetry_row_even(size)


def create_symmetry_row_odd(size: int) -> list[str]:
    part_size = size // 2 + 1
    row_part = create_row(part_size)
    row = row_part + row_part[: part_size - 1][::-1]
    return row


def create_symmetry_row_even(size: int) -> list[str]:
    row_part = create_row(size // 2)
    row = row_part + row_part[::-1]
    return row


def create_sprite_vertical(size: int) -> list[list[str]]:
    def _create_sprite(current_size):
        if current_size == 0:
            return []
        row = create_row(size)
        if current_size == 1:
            return [row]
        return [row, *_create_sprite(current_size - 2), row]

    return _create_sprite(size)


def create_sprite_horizontal(size: int) -> list[list[str]]:
    multiplicity_size = size % 2
    if multiplicity_size:
        return [create_symmetry_row_odd(size) for _ in range(size)]
    return [create_symmetry_row_even(size) for _ in range(size)]


def create_sprite_multiple_symmetries(size: int) -> list[list[str]]:
    multiplicity_size = size % 2

    def _create_sprite(current_size):
        if current_size == 0:
            return []
        row = create_symmetry_row(size, multiplicity_size)
        if current_size == 1:
            return [row]
        return [row, *_create_sprite(current_size - 2), row]

    return _create_sprite(size)


def create_sprite(size: int) -> list[list[str]]:
    symmetry = select_symmetry()
    match symmetry:
        case (True, False):
            return create_sprite_vertical(size)
        case (False, True):
            return create_sprite_horizontal(size)
        case (True, True):
            return create_sprite_multiple_symmetries(size)


def display_sprite(sprite: list[list[str]]):
    result_sprite = ["".join(row) for row in sprite]
    print(*result_sprite, sep="\n")


def main():
    user_size = input("Input size of sprites(2 <= size <= 1000): ")
    if is_correct_size(user_size):
        user_size = int(user_size)
    else:
        print("Incorrect size!")
        return
    activity = True
    while activity:
        sprite = create_sprite(user_size)
        display_sprite(sprite)
        stopping_activity = input("\n")
        if stopping_activity:
            activity = False


if __name__ == "__main__":
    h = ["█", " ", "█"]
    main()
