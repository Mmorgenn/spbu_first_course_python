from os.path import *
from string import *
from csv import *


def start():
    while True:
        file_input = str(input("Введите файл для чтения (txt): "))
        file_output = str(input("Введите файл для записи (csv): "))
        if (
            isfile(file_output)
            and isfile(file_input)
            and file_input[-3:] == "txt"
            and file_output[-3:] == "csv"
        ):
            dict_words, set_words = find_dict(file_input)
            write(file_output, dict_words, set_words)
        else:
            print("Файлы не были найдены! Попрбуйте еще раз")


def find_dict(file_input):
    words_count = {}
    words_set = set()
    with open(file_input, encoding="utf-8", mode="r") as file:
        for line in file:
            for word in (
                line.translate(str.maketrans("", "", punctuation)).lower().split()
            ):
                if word == "-":
                    continue
                elif word not in words_set:
                    words_count[word] = 1
                    words_set.add(word)
                else:
                    words_count[word] += 1
    return words_count, words_set


def write(file_output, dict_words, set_words):
    with open(file_output, encoding="utf-8-sig", mode="w", newline="") as file:
        header = ["Word", "Count"]
        file_writer = DictWriter(file, fieldnames=header)
        file_writer.writeheader()
        for word in set_words:
            file_writer.writerow({"Word": word, "Count": dict_words[word]})


if __name__ == "__main__":
    punctuation = punctuation.replace("-", "") + "\n«»…"
    start()
