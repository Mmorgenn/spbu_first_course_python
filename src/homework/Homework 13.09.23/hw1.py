def calculating(x):
    step_1 = x*x
    step_2 = (step_1 + 1)*(step_1 + x) + 1
    return step_2


def start():
    while True:
        x = str(input("Вычисление x^4 + x^3 + x^2 + x + 1 \n Введите значение x: "))
        if x.isdigit():
            print(f"\n Вычисляю: {x}^4 + {x}^3 + {x}^2 + {x} + 1 = {calculating(int(x))} \n")


if __name__ == "__main__":
    start()