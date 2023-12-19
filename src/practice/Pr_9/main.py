from src.practice.Pr_9.fsm import *
import string


OUTPUT_STRING_ANY = "[✅] - The string is suitable for this language:"
OUTPUT_STRING_NONE = "[⛔] - The string is not suitable for any languages!"


def create_first_fs_machine():
    return create_fs_machine(
        "first_fs_machine",
        {
            0: {"a": 1, "b": 0},
            1: {"a": 1, "b": 2},
            2: {"a": 1, "b": 3},
            3: {"a": 1, "b": 0},
        },
        0,
        [3],
    )


def create_second_fs_machine():
    return create_fs_machine(
        "second_fs_machine",
        {
            0: {string.digits: 1},
            1: {".": 2, "E": 4, string.digits: 1},
            2: {string.digits: 3},
            3: {"E": 4, string.digits: 3},
            4: {"+-": 5, string.digits: 6},
            5: {string.digits: 6},
            6: {string.digits: 6},
        },
        0,
        [1, 3, 6],
    )


def validate_for_multiple_languages(word: str, fs_machines: list[FSMachine]):
    result = []
    for fs_machine in fs_machines:
        if validate_string(fs_machine, word):
            result.append(f"{OUTPUT_STRING_ANY} {fs_machine.name}")
    if not result:
        result.append(OUTPUT_STRING_NONE)
    return result


def main():
    user_string = input("Input a string to check for it on FSMachine: ")
    fs_machines = [create_first_fs_machine(), create_second_fs_machine()]
    result_for_output = validate_for_multiple_languages(user_string, fs_machines)
    print(*result_for_output, sep="\n")


if __name__ == "__main__":
    main()
