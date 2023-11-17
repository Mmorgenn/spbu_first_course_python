def is_valid_input(input_nums):
    if len(input_nums) != 2:
        return False
    try:
        [int(num) for num in input_nums]
    except ValueError:
        return False
    return True


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
        extra_num = (sum + extra_num) // 2
    return new_num


def convert_to_binary(decimal_num):
    number = abs(decimal_num)
    bin_num = []
    while number > 0:
        bin_num = [str(number % 2)] + bin_num
        number //= 2
    extra_bytes = (len(bin_num) + 1) % 8 + 2
    if decimal_num >= 0:
        return ["0" for i in range(extra_bytes)] + bin_num
    return ["1" for i in range(extra_bytes)] + change_sign(bin_num)


def equate_lengths_binary(bin_list_1, bin_list_2):
    first_len = len(bin_list_1)
    second_len = len(bin_list_2)
    if first_len > second_len:
        return bin_list_1, enlarge_binary_list(bin_list_2, first_len - second_len)
    elif first_len < second_len:
        return enlarge_binary_list(bin_list_1, second_len - first_len), bin_list_2
    return bin_list_1, bin_list_2


def enlarge_binary_list(bin_list, len_difference):
    sign = bin_list[0]
    return [sign for i in range(len_difference)] + bin_list


def convert_to_decimal(bin_num):
    sign = bin_num[0]
    if sign == "1":
        bin_num = change_sign(bin_num)
    int_num = 0
    counter = len(bin_num) - 1
    for num in bin_num:
        int_num += 2**counter * int(num)
        counter -= 1
    if sign == "1":
        return -int_num
    return int_num


def main():
    input_nums = input("Введите два числа через пробел: ").split()
    if not is_valid_input(input_nums):
        print("Ошибка! В строке должно быть два числа записанные через пробел")
        return
    first_num, second_num = input_nums
    first_bin = convert_to_binary(int(first_num))
    second_bin = convert_to_binary(int(second_num))
    first_bin, second_bin = equate_lengths_binary(first_bin, second_bin)
    output_1 = ("").join(first_bin)
    output_2 = ("").join(second_bin)
    print(f"{output_1} => Число: {first_num}\n{output_2} => Число: {second_num}")
    bin_sum = get_binary_sum(first_bin, second_bin)
    sum_output = ("").join(bin_sum)
    print(f"Сумма:\n{sum_output} => Число: {convert_to_decimal(bin_sum)}")
    bin_sub = get_binary_sum(first_bin, change_sign(second_bin))
    sub_output = ("").join(bin_sub)
    print(f"Разность:\n{sub_output} => Число: {convert_to_decimal(bin_sub)}")


if __name__ == "__main__":
    main()
