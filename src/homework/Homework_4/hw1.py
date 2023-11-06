def parsing_numbers(num_1, num_2):
    try:
        return [int(i) for i in (num_1, num_2)]
    except ValueError:
        raise ValueError("Each element must be int")


def invert_binary(bin_num):
    return ["1" if i == "0" else "0" for i in bin_num]


def change_sign(bin_num):
    return get_binary_sum(
        invert_binary(bin_num), ["0" for i in range(len(bin_num) - 1)] + ["1"]
    )


def get_binary_sum(num_1, num_2):
    new_num = []
    extra_num = 0
    for i in range(len(num_1) - 1, -1, -1):
        sum = int(num_1[i]) + int(num_2[i])
        new_num = [str((sum + extra_num) % 2)] + new_num
        extra_num = int(sum + extra_num >= 2)
    return new_num


def get_binary(int_num):
    sign = str(int(int_num < 0))
    number, bin_num = abs(int_num), []
    while number > 0:
        bin_num = [str(number % 2)] + bin_num
        number //= 2
    extra_bytes = (len(bin_num) + 1) % 8 + 2
    if sign == "0":
        return ["0" for i in range(extra_bytes)] + bin_num
    else:
        return ["1" for i in range(extra_bytes)] + change_sign(bin_num)


def equalized_bin(first_bin, second_bin):
    first_len, second_len = len(first_bin), len(second_bin)
    if first_len > second_len:
        sign = second_bin[0]
        second_bin = [sign for i in range(first_len - second_len)] + second_bin
    elif len(first_bin) < len(second_bin):
        sign = first_bin[0]
        first_bin = [sign for i in range(second_len - first_len)] + first_bin
    return first_bin, second_bin


def get_int(bin_num):
    sign = bin_num[0]
    if sign == "1":
        bin_num = change_sign(bin_num)
    int_num, counter = 0, len(bin_num) - 1
    for num in bin_num:
        int_num += 2**counter * int(num)
        counter -= 1
    if sign == "1":
        return -int_num
    return int_num


def main():
    first_num = input("Введите первое число: ")
    second_num = input("Введите второе число: ")
    try:
        first_num, second_num = parsing_numbers(first_num, second_num)
    except ValueError:
        print("Ошибка! Не каждый введенный элемент является целым числом")
        return
    first_bin, second_bin = get_binary(first_num), get_binary(second_num)
    first_bin, second_bin = equalized_bin(first_bin, second_bin)
    output_1, output_2 = [("").join(num) for num in (first_bin, second_bin)]
    print(f"{output_1} => Число: {first_num}\n{output_2} => Число: {second_num}")
    bin_sum = get_binary_sum(first_bin, second_bin)
    sum_output = ("").join(bin_sum)
    print(f"Сумма:\n{sum_output} => Число: {get_int(bin_sum)}")
    bin_sub = get_binary_sum(first_bin, change_sign(second_bin))
    sub_output = ("").join(bin_sub)
    print(f"Вычетание:\n{sub_output} => Число: {get_int(bin_sub)}")


if __name__ == "__main__":
    while True:
        main()
