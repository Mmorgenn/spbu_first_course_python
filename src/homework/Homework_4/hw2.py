from math import isinf, isnan


def num_check(num):
    try:
        num_float = float(num)
    except ValueError:
        raise ValueError("It must be float number")
    if isinf(num_float) or isnan(num_float):
        raise ValueError("It should not be Inf or Nan")
    return num_float


def get_binary_integer(num):
    if num == 0:
        return ["0"]
    bin_num = []
    while num > 0:
        bin_num = [str(num % 2)] + bin_num
        num //= 2
    return bin_num


def get_binary_fraction(num, mantissa_bits):
    num = int(num) / 10 ** len(num)
    bin_num = []
    if num == 0:
        return ["0"]
    for i in range(mantissa_bits):
        num *= 2
        bin_num.append(str(num // 1))
        num = num % 1
        if num == 0:
            return bin_num
    return bin_num


def get_normalised_form(int_part, fraction_part):
    bin_number = ("").join(int_part) + "." + ("").join(fraction_part)
    mantissa = (
        (bin_number.replace(".", "")).lstrip("0") if float(bin_number) != 0 else "0"
    )
    order = (
        bin_number.find(".")
        if bin_number[0] != "0"
        else -len(bin_number[2 : bin_number.find(mantissa[0])])
    )
    mantissa = mantissa.rstrip("0")
    return ["0." + mantissa, order]


def convert_to_fp(normalized_num, order_bits, mantissa_bits):
    sign, mantissa, order = normalized_num
    shifted_order = ("").join(
        get_binary_integer((order - 1) + 2 ** (order_bits - 1) - 1)
    )
    if len(shifted_order) > order_bits:
        raise OverflowError("This number too large for this format")

    mantissa = mantissa[3:] if len(mantissa) > 3 else mantissa[2]
    if len(mantissa) > mantissa_bits:
        mantissa = mantissa[:mantissa_bits]
    else:
        mantissa = mantissa.ljust(mantissa_bits, "0")

    sign = "0"
    if normalized_num[0] == "-":
        sign = "1"
    return [sign, shifted_order, mantissa]


def main(num, order_bits, mantissa_bits):
    sign = "-" if str(num)[0] == "-" else "+"
    int_part, float_part = (str(num)).removeprefix("-").split(".")
    int_bin = get_binary_integer(int(int_part))
    float_bin = get_binary_fraction(float_part, mantissa_bits)
    bin_num_normalization = [sign] + get_normalised_form(int_bin, float_bin)
    print("{}{}*2^{}".format(*bin_num_normalization))
    try:
        fp_converted = convert_to_fp(bin_num_normalization, order_bits, mantissa_bits)
    except OverflowError:
        print("Это число слишком большое/маленькое для этого формата хранения числа")
        return
    print("Результат: {} {} {}".format(*fp_converted))


def start():
    num_input = input("Введите вещественное число: ")
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
    start()
