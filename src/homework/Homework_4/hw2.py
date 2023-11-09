def num_check(num):
    try:
        num_float = float(num)
    except ValueError:
        raise ValueError("It must be float number")
    if "inf" in num:
        raise ValueError("It should not be inf")
    return num_float


def get_binary_integer(num):
    if num == 0:
        return ["0"]
    bin_num = []
    while num > 0:
        bin_num = [str(num % 2)] + bin_num
        num //= 2
    return bin_num


def get_binary_fraction(num, precision):
    num = num / 10 ** len(str(num))
    bin_num = []
    if num == 0:
        return ["0"]
    for i in range(precision):
        num *= 2
        bin_num.append(str(num // 1)[0])
        if num % 1 == 0:
            return bin_num
        num = num % 1
    return bin_num


def normalization(int_part, float_part):
    p = 0
    while len(int_part) != 0:
        element = int_part.pop(-1)
        float_part = [element] + float_part
        p += 1
    result = "0." + ("").join(float_part)
    return [result, p]


def fp_conversation(num_list, range, precision):
    shift = ("").join(get_binary_integer(int(num_list[2] - 1) + 2 ** (range - 1) - 1))
    if len(shift) > range:
        raise OverflowError("The number i too large for this format")
    mantissa = num_list[1][3:] if len(num_list[1]) > 3 else num_list[1][2]
    if len(mantissa) > precision:
        mantissa = mantissa[:precision]
    else:
        mantissa += "0" * (precision - len(mantissa))
    sign = int(num_list[0] == "-")
    return [sign, shift, mantissa]


def main(num, range, precision):
    sign = "-" if str(num)[0] == "-" else "+"
    int_part, float_part = (str(num)).removeprefix("-").split(".")
    int_bin, float_bin = get_binary_integer(int(int_part)), get_binary_fraction(
        int(float_part), precision
    )
    bin_num_normalization = [sign] + normalization(int_bin, float_bin)
    print("{}{}*2^{}".format(*bin_num_normalization))
    try:
        fp_converted = fp_conversation(bin_num_normalization, range, precision)
    except OverflowError:
        print("Это число слишком большое/маленькое для этого формата хранения числа")
        return
    print("Результат: {} {} {}".format(*fp_converted))


def start():
    num_input = input("Ввещите вещественное число: ")
    try:
        num = num_check(num_input)
    except ValueError as e:
        print(f"Ошибка! Причина: {e}")
        return
    fp_input = input("Выберите: (1)FP64, (2)FP32, (3)FP16: ")
    if fp_input == "1":
        main(num, 11, 52)
    elif fp_input == "2":
        main(num, 8, 23)
    elif fp_input == "3":
        main(num, 5, 10)
    else:
        print("Ошибка! От вас требовалось написать число от 1 до 3")


if __name__ == "__main__":
    while True:
        start()
