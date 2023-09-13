def result(a, b):
    eq = 1
    if ((a < 0) + (b < 0)) == 1: eq = -1
    a = abs(a)
    b = abs(b)
    res = 0
    while a >= b:
        res += 1
        a -= b
    return res * eq


def dell():
    while True:
        try:
            num_a = int(input("Введите делимое: "))
            num_b = int(input("Введите делитель: "))
            print(f"Результат деления: {result(num_a, num_b)} \n")
        except Exception:
            print("Ошибка! Попробуй еще раз \n")


if __name__ == "__main__":
    dell()