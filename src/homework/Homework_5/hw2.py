from string import ascii_lowercase, digits


def encode_dna(dna):
    chars = list(
        map(
            lambda i: dna[i] if i == 0 or dna[i] == dna[i - 1] else " " + dna[i],
            (i for i in range(len(dna))),
        )
    )
    chars_filtered = ("").join(chars).split()
    result = list(map(lambda x: x[0] + str(len(x)), chars_filtered))
    return ("").join(result)


def check_encoded_line(dna_line):
    return all(i in ascii_lowercase for i in set(dna_line))


def decode_dna(dna_line):
    chars = list(filter(lambda x: x.isalpha(), dna_line))
    count = dna_line.translate(str.maketrans(ascii_lowercase, " " * 26)).split()
    return ("").join(list(map(lambda x: x[0] * int(x[1]), list(zip(chars, count)))))


def check_decoded_line(dna_line):
    if dna_line[0].isdigit():
        raise ValueError("Строка не может начинаться с цифры")
    if dna_line[-1] in ascii_lowercase:
        raise ValueError("Строка должна оканчиваться цифрой")
    if any(
        (dna_line[i] in ascii_lowercase and dna_line[i + 1] in ascii_lowercase)
        for i in range(len(dna_line) - 1)
    ):
        raise ValueError(
            "Строка должна состоять из пар строчная латинская буква + число"
        )
    if any(i not in (ascii_lowercase + digits) for i in set(dna_line)):
        raise ValueError("Строка должно состоять из цифр и строчных латинских букв")


def start_encode():
    input_dna_line = input(
        "Введите линию ДНК для закодирования (Пример: aabbbbccccccc): "
    )
    if input_dna_line == "":
        print("Строка пустая!")
        return
    if check_encoded_line(input_dna_line):
        print("Результат:\t{}".format(encode_dna(input_dna_line)))
    else:
        print(
            "Произошла ошибка! Причина: В линии ДНК должны быть использованы"
            " только строчные буквы латинского алфавита"
        )


def start_decode():
    input_dna_line = input("Введите закодированную линию ДНК (Пример: a2b4c7): ")
    if input_dna_line == "":
        print("Строка пустая!")
        return
    try:
        check_decoded_line(input_dna_line)
    except ValueError as e:
        print(f"Ошибка! Причина: {e}")
        return
    print("Результат:\t{}".format(decode_dna(input_dna_line)))


def main():
    input_function = input(
        "Выберите функцию для ДНК:\n(1) - Закодировать\n(2) - Декодировать\n"
    )
    if input_function == "1":
        start_encode()
    elif input_function == "2":
        start_decode()
    else:
        print("Ошибка! Такой функции не существует")


if __name__ == "__main__":
    while True:
        main()
