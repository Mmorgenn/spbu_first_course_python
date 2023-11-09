import pytest
from io import StringIO
from src.homework.Homework_5.hw1 import (
    get_unicode,
    get_encoded_representation,
    encode_symbol,
    encode_string,
    main,
)


@pytest.mark.parametrize(
    "symbol_ord,expected", ((72, "0048 "), (1082, "043A "), (71892, "118D4"))
)
def test_get_unicode(symbol_ord, expected):
    function = get_unicode(symbol_ord)
    assert function == expected


@pytest.mark.parametrize(
    "symbol_ord,expected",
    (
        (52, "00000000 00110100"),
        (1034, "00000100 00001010"),
        (84012, "11011000 00010010 11011100 00101100"),
    ),
)
def test_get_encoded_representation(symbol_ord, expected):
    function = get_encoded_representation(symbol_ord)
    assert function == expected


@pytest.mark.parametrize(
    "symbol,expected",
    (
        ("9", "9	U+0039 	 00000000 00111001"),
        (",", ",	U+002C 	 00000000 00101100"),
        ("𩁔", "𩁔	U+29054	 11011000 01100100 11011100 01010100"),
        ("م", "م	U+0645 	 00000110 01000101"),
        ("♌", "♌	U+264C 	 00100110 01001100"),
        ("☺", "☺	U+263A 	 00100110 00111010"),
    ),
)
def test_encode_symbol(symbol, expected):
    function = encode_symbol(symbol)
    assert function == expected


@pytest.mark.parametrize(
    "string,expected",
    (
        ("1", ["UTF-16 encoding:", "1	U+0031 	 00000000 00110001"]),
        (
            "Hello World!",
            [
                "UTF-16 encoding:",
                "H	U+0048 	 00000000 01001000",
                "e	U+0065 	 00000000 01100101",
                "l	U+006C 	 00000000 01101100",
                "l	U+006C 	 00000000 01101100",
                "o	U+006F 	 00000000 01101111",
                " 	U+0020 	 00000000 00100000",
                "W	U+0057 	 00000000 01010111",
                "o	U+006F 	 00000000 01101111",
                "r	U+0072 	 00000000 01110010",
                "l	U+006C 	 00000000 01101100",
                "d	U+0064 	 00000000 01100100",
                "!	U+0021 	 00000000 00100001",
            ],
        ),
        (
            "Символ: 𩁔",
            [
                "UTF-16 encoding:",
                "С	U+0421 	 00000100 00100001",
                "и	U+0438 	 00000100 00111000",
                "м	U+043C 	 00000100 00111100",
                "в	U+0432 	 00000100 00110010",
                "о	U+043E 	 00000100 00111110",
                "л	U+043B 	 00000100 00111011",
                ":	U+003A 	 00000000 00111010",
                " 	U+0020 	 00000000 00100000",
                "𩁔	U+29054	 11011000 01100100 11011100 01010100",
            ],
        ),
    ),
)
def test_encode_string(string, expected):
    function = encode_string(string)
    assert function == expected


@pytest.mark.parametrize(
    "user_input,output",
    (
        ("", "Строка пуста!\n"),
        (
            "      ",
            "UTF-16 encoding:\n"
            " 	U+0020 	 00000000 00100000\n"
            " 	U+0020 	 00000000 00100000\n"
            " 	U+0020 	 00000000 00100000\n"
            " 	U+0020 	 00000000 00100000\n"
            " 	U+0020 	 00000000 00100000\n"
            " 	U+0020 	 00000000 00100000\n",
        ),
        (
            "文本进行测试。",
            "UTF-16 encoding:\n"
            "文	U+6587 	 01100101 10000111\n"
            "本	U+672C 	 01100111 00101100\n"
            "进	U+8FDB 	 10001111 11011011\n"
            "行	U+884C 	 10001000 01001100\n"
            "测	U+6D4B 	 01101101 01001011\n"
            "试	U+8BD5 	 10001011 11010101\n"
            "。	U+3002 	 00110000 00000010\n",
        ),
    ),
)
def test_main(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    test_output = fake_output.getvalue()
    assert test_output == output
