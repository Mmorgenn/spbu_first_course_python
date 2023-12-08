from src.practice.Pr_9.fsm import *


def create_first_fs_machine():
    return create_fs_machine(
        ["a", "b"],
        {
            0: [("a", 1), ("b", 0)],
            1: [("a", 1), ("b", 2)],
            2: [("a", 1), ("b", 3)],
            3: [("a", 1), ("b", 0)],
        },
        0,
        [3],
    )


def main():
    user_string = input("Input a string to check for it on FSMachine: ")
    fsm_1 = create_first_fs_machine()
    if validate_string(fsm_1, user_string):
        print("[✅] - The string is suitable for the first language!")
    else:
        print("[⛔] - The string is not suitable for any languages!")


if __name__ == "__main__":
    main()
