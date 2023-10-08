from os.path import isfile
from csv import DictWriter


def start():
    while True:
        file_input = str(input("Введите файл для чтения (txt): "))
        file_output = str(input("Введите файл для записи (csv): "))
        if (
            isfile(file_input)
            and not isfile(file_output)
            and file_input.endswith("txt")
            and file_output.endswith("csv")
        ):
            words_count = find_words_count(file_input)
            write(file_output, words_count)
        elif isfile(file_output) and file_output.endswith("csv"):
            print(f"Файл {file_output} уже существует!")
        else:
            print("Ошибка! Попрбуйте еще раз")


def find_words_count(file_input):
    words_count = {}
    with open(file_input, encoding="utf-8", mode="r") as file:
        for line in file:
            line = line.rstrip().lower().split()
            for word in line:
                words_count[word] = words_count.get(word, 0) + 1
    return words_count


def write(file_output, words_count):
    with open(file_output, encoding="utf-8-sig", mode="w", newline="") as file:
        header = ["Word", "Count"]
        file_writer = DictWriter(file, fieldnames=header)
        file_writer.writeheader()
        file_writer.writerows(
            {"Word": word, "Count": words_count[word]} for word in words_count
        )


if __name__ == "__main__":
    start()
