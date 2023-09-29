def prime(a):
    mas_prime = []
    for i1 in range(1, a + 1):
        for i2 in range(2, int(i1**0.5) + 1):
            if i1 != i2 and i1 % i2 == 0:
                break
        else:
            mas_prime.append(i1)
    return mas_prime


def find():
    while True:
        try:
            num = int(input("Введите число: "))
            prime_str = ", ".join(map(str, prime(num)))
            print(f"Все простые числа: {prime_str} \n")
        except Exception:
            print("Ошибка! Поробуй еще! \n")


if __name__ == "__main__":
    find()
