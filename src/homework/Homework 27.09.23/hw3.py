from os.path import *


def start():
    while True:
        file_input = input("Введите файл для чтения (txt): ")
        file_output = input("Введите файл для чтения (txt): ")
        if all(
            [
                isfile(file_output),
                isfile(file_input),
                file_input[-3:] == "txt",
                file_output[-3:] == "txt",
                file_input != file_output,
            ]
        ):
            file_scrolling(file_input, file_output)
        else:
            print("Файлы не были найдены! Попрбуйте еще раз")


def file_scrolling(file_name_input, file_name_output):
    with open(file_name_input, "r") as file_input, open(
        file_name_output, "w"
    ) as file_output:
        m = int(file_input.readline())
        dna_line = file_input.readline()
        n = int(file_input.readline())
        for i in range(n):
            command, arg1, arg2 = "".join(
                [i for i in str(file_input.readline()) if i not in "]\n"]
            ).split("[")
            if command == "DELETE":
                dna_line = delete_fragment(dna_line, arg1, arg2, file_output)
            elif command == "INSERT":
                dna_line = insert_fragment(dna_line, arg1, arg2, file_output)
            elif command == "REPLACE":
                dna_line = replace_fragment(dna_line, arg1, arg2, file_output)
            else:
                file_output.write(dna_line)


def delete_fragment(line, start, end, file):
    line = line.replace(start, " ", 1).split()
    line[1] = line[1].replace(end, " ", 1).split()[1]
    new_line = line[0] + line[1]
    file.write(new_line + "\n")
    return new_line


def insert_fragment(line, start, fragment, file):
    new_line = line.replace(start, start + fragment, 1)
    file.write(new_line + "\n")
    return new_line


def replace_fragment(line, template, fragment, file):
    new_line = line.replace(template, fragment, 1)
    file.write(new_line + "\n")
    return new_line


if __name__ == "__main__":
    start()
