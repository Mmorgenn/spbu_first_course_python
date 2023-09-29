from os.path import *
import sys


def start():
    if len(sys.argv) == 5:
        command = sys.argv[1]
        if command == "wc":
            wc(sys.argv[2], sys.argv[3])
        elif command == "head":
            head(sys.argv[2], sys.argv[3], sys.argv[4])
        elif command == "tail":
            tail(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Такой команды нет")


def wc(arg, file_name):
    if arg == "-c":
        print(wc_c(file_name))
    elif arg == "-l":
        print(wc_l(file_name))
    elif arg == "-w":
        print(wc_w(file_name))
    elif arg == "-m":
        print(wc_m(file_name))
    else:
        print("Не найдено подходящей команды \n")


def wc_c(file_name):
    return getsize(file_name)


def wc_l(file_name):
    with open(file_name, "r") as file:
        count_lines = sum([1 for line in file])
        return count_lines


def wc_w(file_name):
    with open(file_name, "r") as file:
        count = sum([len(line.split()) for line in file])
        return count


def wc_m(file_name):
    with open(file_name, "r") as file:
        count = 0
        for line in file:
            if line[-1] == "\n":
                count += 1
            count += len(line)
    return count


def head(arg, int_arg, file_name):
    if arg == "-n":
        head_n(int_arg, file_name)
    elif arg == "-c":
        head_c(int_arg, file_name)
    else:
        print("Не найдено подходящей команды")


def head_n(int_arg, file_name):
    with open(file_name, "r") as file:
        for i in range(int(int_arg)):
            line = file.readline()
            if not line:
                break
            print(line.strip())


def head_c(int_arg, file_name):
    text = ""
    with open(file_name, "r") as file:
        text = file.read(int(int_arg))
        line_count = text.count("\n")
        if line_count > 0:
            print(text[: -(text.count("\n"))])
        else:
            print(text)


def tail(arg, int_arg, file_name):
    if arg == "-n":
        tail_n(int_arg, file_name)
    elif arg == "-c":
        tail_c(int_arg, file_name)
    else:
        print("Не найдено подходящей команды")


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
        line_1 = 0
        for line in file.readlines()[::-1]:
            line_len = len(line.replace("\n", "=n").encode("utf-8"))
            if size + line_len >= int(int_arg) and int(int_arg) - size - line_1 != 0:
                text = (
                    line.encode("utf-8")[-(int(int_arg) - size - line_1) :].decode(
                        "utf-8"
                    )
                    + text
                )
                break
            elif size + line_len >= int(int_arg):
                text = "\n" + text
                break
            else:
                text = line + text
                size += len(line.replace("\n", "=n").encode("utf-8"))
                line_1 = 1
    print(text)


if __name__ == "__main__":
    start()
