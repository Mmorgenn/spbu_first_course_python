from os.path import isfile


def start():
    while True:
        file_input = input("Введите файл для чтения (txt): ")
        file_output = input("Введите файл для чтения (txt): ")
        if all(
            [
                isfile(file_input),
                not isfile(file_output),
                file_input.endswith("txt"),
                file_output.endswith("txt"),
                file_input != file_output,
            ]
        ):
            dna_lines = file_scrolling(file_input)
            file_writer(dna_lines, file_output)
        elif isfile(file_output) and file_output.endswith("txt"):
            print(f"Файл {file_output} уже существует!")
        else:
            print("Ошибка! Попрбуйте еще раз")


def file_scrolling(file_name_input):
    with open(file_name_input, "r") as file_input:
        m = int(file_input.readline())
        dna_line = file_input.readline()
        n = int(file_input.readline())
        dna_lines = list()
        for i in range(n):
            command, arg1, arg2 = str(file_input.readline()).rstrip().split()
            if command == "DELETE":
                dna_line = delete_fragment(dna_line, arg1, arg2)
            elif command == "INSERT":
                dna_line = insert_fragment(dna_line, arg1, arg2)
            elif command == "REPLACE":
                dna_line = replace_fragment(dna_line, arg1, arg2)
            dna_lines.append(dna_line)
        return dna_lines


def file_writer(dna_lines, file_name_output):
    with open(file_name_output, "w") as file_output:
        file_output.writelines(line for line in dna_lines)


def delete_fragment(line, start, end):
    start_id = line.find(start)
    end_line = line[start_id:]
    end_id = end_line.find(end) + len(end)
    return line[:start_id] + end_line[end_id:]


def insert_fragment(line, start, fragment):
    new_line = line.replace(start, start + fragment, 1)
    return new_line


def replace_fragment(line, template, fragment):
    new_line = line.replace(template, fragment, 1)
    return new_line


if __name__ == "__main__":
    start()
