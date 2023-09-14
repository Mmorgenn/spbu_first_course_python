from os.path import *
import sys


def start():
    #try:
        command = sys.argv[1]
        if command == "wc":
            wc(sys.argv[2], sys.argv[3])
        elif command == "head":
            head(sys.argv[2], sys.argv[3], sys.argv[4])
        elif command == "tail":
            tail(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("Такой команды нет")
    #except Exception:
        #print("Ошибка в команде!")


def wc(arg, file_name):
    if arg == "-c":
        wc_c(file_name)
    elif arg == "-l":
        wc_l(file_name)
    elif arg == "-w":
        wc_w(file_name)
    elif arg == "-m":
        wc_m(file_name)
    else: print("Не найдено подходящей команды \n")


def wc_c(file_name):
    size = getsize(file_name)
    print(f"{size} Байт")


def wc_l(file_name):
    with open(file_name, "r") as file:
        count_lines = sum([1 for line in file])
        print(f"Строк: {count_lines}")


def wc_w(file_name):
    with open(file_name, "r") as file:
     count = sum([len(line.split()) for line in file])
    print(f"Количество слов: {count}")


def wc_m(file_name):
    with open(file_name, "r") as file:
        count = 0
        for line in file:
            if line[-1]=="\n": count += 1
            count += len(line)
    print(f"Количество символов: {count}")


def head(arg, int_arg, file_name):
    if arg == "-n": head_n(int_arg, file_name)
    elif arg == "-c": head_c(int_arg, file_name)
    else: print("Не найдено подходящей команды")


def head_n(int_arg, file_name):
    with open(file_name, "r") as file:
        for i in range(int(int_arg)):
            line = file.readline()
            if not line:
                break
            print(line.strip())


def head_c(int_arg, file_name):
    len_count = 0
    with open(file_name, "r") as file:
        len_count = len(file.readlines(int(int_arg)))
    with open(file_name, "r") as file:
        print(file.read(int(int_arg) - len_count + 1))


def tail(arg, int_arg, file_name):
    if arg == "-n": tail_n(int_arg, file_name)
    elif arg == "-c": tail_c(int_arg, file_name)
    else: print("Не найдено подходящей команды")


def tail_n(int_arg, file_name):
    text = ""
    current_line = 0
    with open(file_name, "r") as file:
        for line in file.readlines()[::-1]:
            current_line += 1
            text = line + text
            if current_line >= int(int_arg):
                break
        print(text)


def tail_c(int_arg, file_name):
    with open(file_name, "r") as file:
        size = 0
        text = ""
        for line in file.readlines()[::-1]:
            while size < int(int_arg):
                for symbol in line[::-1]:
                    if symbol == "\n":
                        size += 2
                        text = "\n" + text
                    else:
                        size += len(symbol.encode('utf-8'))
                        text = symbol + text
                    if size >= int(int_arg):
                        print(text)
                        break
                break


if __name__ == "__main__":
    start()