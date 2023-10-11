from os.path import isfile
from sys import argv


def check_files(file_input, file_output):
    if isfile(file_input) and not isfile(file_output):
        return True
    if not isfile(file_input):
        print(f"Файл {file_input} ненайден")
    if isfile(file_output):
        print(f"Файл {file_output} уже существует!")
    return False


def sort_nums(a, b, file_input):
    with open(file_input, mode="r") as file:
        line = (file.readline()).split()
        list_a, list_ab, list_b = [], [], []
        for i in line:
            num = int(i)
            if num < a:
                list_a.append(i)
            elif num > b:
                list_b.append(i)
            else:
                list_ab.append(i)
        return [list_a, list_ab, list_b]


def write_nums(lists_nums, file_output):
    with open(file_output, mode="w", newline="") as file:
        file.writelines([" ".join(list) + "\n" for list in lists_nums])


def start():
    if len(argv) == 5:
        if check_files(argv[3], argv[4]):
            list_nums = sort_nums(int(argv[1]), int(argv[2]), argv[3])
            write_nums(list_nums, argv[4])
    else:
        print("Ошибка в синстаксисе комманды")


if __name__ == "__main__":
    start()
