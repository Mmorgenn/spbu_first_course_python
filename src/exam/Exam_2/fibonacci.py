def is_correct_input(user_input: str) -> bool:
    if not user_input.isdigit():
        return False
    return int(user_input) <= 90


def get_fibonacci_num(num: int) -> int:
    first_num = 0
    second_num = 1
    for i in range(num):
        first_num, second_num = second_num, first_num + second_num
    return first_num


def main():
    user_input = input("Введите цеолое положительное число меньшее 91: ")
    if is_correct_input(user_input):
        print(f"Число Фибоначчи под номером {user_input}: {get_fibonacci_num(int(user_input))}")
    else:
        print("Вы не корректно ввели число! Ваше число должно быть целым, положительным, меньше 91")


if __name__ == "__main__":
    main()