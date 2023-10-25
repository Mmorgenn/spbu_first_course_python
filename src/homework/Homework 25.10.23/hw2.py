def num_check(num):
    if num.removeprefix("-").replace(".", "").isdigit():
        return float(num)
    raise SyntaxError("This element must be float")


def binary_integer_get(num):
    if num == 0:
        return "0"
    bin_num = ""
    while num > 0:
        bin_num = str(num % 2) + bin_num
        num //= 2
    return bin_num


def binary_fraction_get(num, precision):
    bin_num = ""
    if num == 0:
        return "0"
    for i in range(precision):
        num *= 2
        bin_num = bin_num + str(num // 1)[0]
        if num % 1 == 0:
            return bin_num
        num = num % 1
    return bin_num


def binary_conversion(num, precision):
    sign = int(num[0] == "-")
    num_integer, num_fraction = num.removeprefix("-").split(".")
    bin_integer = binary_integer_get(int(num_integer))
    bin_fraction = binary_fraction_get(float("0." + num_fraction), precision)
    return str(sign) + bin_integer + "." + bin_fraction


def normalization(num):
    if num[0] == "0":
        sign = "+"
        num = num.removeprefix("0")
    else:
        sign = "-"
        num = num.removeprefix("1")
    need_point = num.find(".")
    if num[0] == "0":
        need_one = num.find("1")
        p = need_point - need_one
        mantissa = "1." + num[need_one + 1 :] + "0"
        return [sign, mantissa, p]
    else:
        p = need_point - 1
        num = num.replace(".", "")
        mantissa = "1." + num[1:]
        return [sign, mantissa, p]


def fp_conversation(num_list, range, precision):
    shift = binary_integer_get(int(num_list[2]) + 2 ** (range - 1) - 1)
    if len(shift) > range:
        raise OverflowError("The number i too large for this format")
    mantissa = num_list[1][2:]
    if len(mantissa) > precision:
        mantissa = mantissa[:precision]
    else:
        mantissa += "0" * (precision - len(mantissa))
    sign = int(num_list[0] == "-")
    return [sign, shift, mantissa]


def main(num, range, precision):
    bin_num = binary_conversion(str(num), precision)
    bin_num_normalization = normalization(bin_num)
    print("{}{}*2^{}".format(*bin_num_normalization))
    try:
        fp_converted = fp_conversation(bin_num_normalization, range, precision)
    except OverflowError:
        print("Это число слишком большое/маленькое для этого формата хранения числа")
        return False
    print("Результат: {} {} {}".format(*fp_converted))
    return True


def start():
    num_input = input("Ввещите вещественное число: ")
    try:
        num = num_check(num_input)
    except SyntaxError:
        print(
            "Введенная строка не соответствует стандартному виду вещественных чисел (Пример: 2.0)"
        )
        return False
    fp_input = input("Выберите: (1)FP64, (2)FP32, (3)FP16: ")
    if fp_input == "1":
        main(num, 11, 52)
    elif fp_input == "2":
        main(num, 8, 23)
    elif fp_input == "3":
        main(num, 5, 10)
    else:
        print("Ошибка! От вас требовалось написать число от 1 до 3")
        return False
    return True


if __name__ == "__main__":
    while True:
        start()
