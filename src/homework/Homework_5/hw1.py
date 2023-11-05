def get_unicode(symbol_ord):
    unicode = hex(symbol_ord)[2:]
    return ((unicode.upper()).rjust(4, "0")).ljust(5)


def get_encoded_representation(symbol_ord):
    encode = bin(symbol_ord)[2:]
    if symbol_ord <= 65535:
        encode = encode.rjust(16, "0")
        return "{} {}".format(encode[:8], encode[8:16])
    encode = encode.rjust(32, "0")
    return "{} {} {} {}".format(encode[:8], encode[8:16], encode[16:24], encode[24:32])


def encode_symbol(symbol):
    symbol_ord = ord(symbol)
    unicode, representation = get_unicode(symbol_ord), get_encoded_representation(
        symbol_ord
    )
    return "{}\tU+{}\t {}".format(symbol, unicode, representation)


def encode_string(string):
    encoded = [
        "UTF-16 encoding:",
    ]
    for symbol in string:
        encoded.append(encode_symbol(symbol))
    return encoded


def main():
    string_input = input("Введите текст для кодирования: ")
    if string_input != "":
        print(*encode_string(string_input), sep="\n")
        return
    print("Строка пуста!")


if __name__ == "__main__":
    while True:
        main()
