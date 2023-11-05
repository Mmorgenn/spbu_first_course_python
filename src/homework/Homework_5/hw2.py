from re import search
from string import ascii_lowercase


def encode_dna(dna_line):
    new_dna_line = dna_line
    for i in range(len(dna_line) - 1):
        e_1, e_2 = dna_line[i], dna_line[i + 1]
        if e_1 != e_2:
            new_dna_line = new_dna_line.replace(e_1 + e_2, f"{e_1} {e_2}", 1)
    return ("").join(i[0] + str(len(i)) for i in new_dna_line.split())


def check_encoded_line(dna_line):
    return dna_line.isascii() and dna_line.islower() and dna_line.isalpha()


def decode_dna(dna_line):
    pattern = search("\D\d+", dna_line)
    if pattern is None:
        return dna_line
    pattern = pattern.group()
    if not pattern[0] in ascii_lowercase:
        raise ValueError("Extraneous characters detected!")
    new_dna_line = dna_line.replace(pattern, pattern[0] * int(pattern[1:]), 1)
    return decode_dna(new_dna_line)


def check_decoded_line(dna_line):
    first_element_check = dna_line[0].isdigit()
    return (
        search("\D{2}", dna_line) is None
        and not first_element_check
        and dna_line[-1] not in ascii_lowercase
    )


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
    if check_decoded_line(input_dna_line):
        try:
            print("Результат:\t{}".format(decode_dna(input_dna_line)))
        except ValueError:
            print(
                "Произошла ошибка! Причина: В линии ДНК используютуся лишние элементы!\n"
                "В закодированной строке могут быть только цифры и строчные буквы латинского алфавита"
            )
    else:
        print(
            "Произошла ошибка! Причина: Нарушена структура закодированной линии ДНК\n"
            "Строка должна состоять из пар: Строчная латинская буква + Число"
        )


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
