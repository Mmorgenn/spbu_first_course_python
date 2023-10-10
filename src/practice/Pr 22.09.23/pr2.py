from random import shuffle


def random_number():
    random_f1 = [str(i) for i in range(1, 10)]
    random_f0 = ["0", *random_f1]
    shuffle(random_f1)
    shuffle(random_f0)
    first_num = random_f1[0]
    random_f0.remove(first_num)
    return [first_num, *random_f0[:3]]


def check_num(num_orig, num_input):
    b_count, c_count = 0, 0
    for i in range(4):
        if num_orig[i] == num_input[i]:
            b_count += 1
        elif num_input[i] in num_orig:
            c_count += 1
    return b_count, c_count


def game(num_orig):
    while True:
        num_input = str(input("Введите четырех значное число: "))
        if (
            len(num_input) == 4
            and num_input.isdigit()
            and all([num_input.count(num_input[i]) == 1 for i in range(4)])
        ):
            b_count, c_count = check_num(num_orig, num_input)
            print(f"Быков: {b_count}, Коров: {c_count}")
            if b_count == 4:
                final_num = "".join(num_orig)
                print(f"Абсолютно верно! Это число - {final_num}")
                break
        else:
            print("Ошибка! Введите четырехзначное число без повторяющихся цифр")


def start():
    while True:
        num_orig = random_number()
        game(num_orig)


if __name__ == "__main__":
    start()
