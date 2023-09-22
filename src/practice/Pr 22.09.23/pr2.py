import random


def random_number():
    return "".join(str(i) for i in random.sample(range(0, 10), 4))


def check_num(num_orig, num_input):
    b_count, c_count = 0, 0
    for i in range(4):
        if num_orig[i] == num_input[i]:
            b_count += 1
        elif num_input[i] in num_orig and num_input[i]:
            c_count += 1
    return b_count, c_count


def game(num_orig):
    while True:
        num_input = str(input("Введите четырех значное число: "))
        if len(num_input) == 4 and all([(num_input[i]!= num_input[i+1]) for i in range(3)]):
            b_count, c_count = check_num(num_orig, num_input)
            print(f"Быков: {b_count}, Коров: {c_count}")
            if b_count == 4:
                print(f"Абсолютно верно! Это число - {num_orig}")
                break
        else:
            print("Ошибка! Введите четырехзначное число без повторяющихся цифр")


def start():
    while True:
        num_orig = random_number()
        print(num_orig)
        game(num_orig)


if __name__ == "__main__":
    start()
