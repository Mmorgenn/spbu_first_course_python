from os.path import exists
from sys import argv
import string


def check_files(file_input, file_output):
    if exists(file_input) and not exists(file_output):
        return True
    if not exists(file_input):
        print(f"Файл {file_input} ненайден")
    if exists(file_output):
        print(f"Файл {file_output} уже существует!")
    return False


def get_letter_count(input_file):
    letter_count = {}
    with open(input_file, "r") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count


def sort_letter_count(letter_count):
    return sorted(letter_count.items(), key=lambda x: x[0])


def write_nums(letter_count, file_output):
    with open(file_output, mode="w") as file:
        file.writelines([f"{i[0]} {i[1]}\n" for i in letter_count])


def start():
    if len(argv) == 3:
        if check_files(argv[1], argv[2]):
            letter_count = get_letter_count(argv[1])
            sorted_letter_count = sort_letter_count(letter_count)
            write_nums(sorted_letter_count, argv[2])
    else:
        print("Ошибка в синстаксисе комманды")


if __name__ == "__main__":
    start()
