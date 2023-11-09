import pytest
from io import StringIO
from src.homework.Homework_5.hw2 import (
    encode_dna,
    check_encoded_line,
    decode_dna,
    check_decoded_line,
    start_encode,
    start_decode,
    main,
)


@pytest.mark.parametrize(
    "dna_line,expected",
    (
        ("a", "a1"),
        ("abcabcabc", "a1b1c1a1b1c1a1b1c1"),
        ("tttttesttttt", "t5e1s1t5"),
        ("aaabbbcccabcacaab", "a3b3c3a1b1c1a1c1a2b1"),
    ),
)
def test_encode_dna(dna_line, expected):
    function = encode_dna(dna_line)
    assert function == expected


@pytest.mark.parametrize(
    "dna_line,expected",
    (
        ("TESTDNA", False),
        ("abccccabbbcB", False),
        ("аабббсссфббс", False),
        ("abbbca cc aaa", False),
        (".,/-=+", False),
        ("a1b6c8", False),
        ("aaaaabbbbcddfs", True),
        ("a", True),
    ),
)
def test_check_encode_line(dna_line, expected):
    function = check_encoded_line(dna_line)
    assert function == expected


@pytest.mark.parametrize(
    "dna_line,expected",
    (
        ("a1", "a"),
        ("a1b1c1", "abc"),
        ("a1a1", "aa"),
        ("a3b5c7", "aaabbbbbccccccc"),
        ("a1b1c1a1n1g1h2t3", "abcanghhttt"),
    ),
)
def test_decode_dna(dna_line, expected):
    function = decode_dna(dna_line)
    assert function == expected


@pytest.mark.parametrize(
    "dna_line",
    ("a3bc6c9a1", "b37b1-4", "aa1b6v3", "12n6b8", "b12n"),
)
def test_check_decode_line(dna_line):
    with pytest.raises(ValueError):
        check_decoded_line(dna_line)


@pytest.mark.parametrize(
    "user_input,output",
    (
        ("", "Строка пустая!\n"),
        ("aaaaabaaaaccc", "Результат:\ta5b1a4c3\n"),
        (
            "absddfёёё",
            "Произошла ошибка! Причина: В линии ДНК должны быть использованы"
            " только строчные буквы латинского алфавита\n",
        ),
    ),
)
def test_start_encode(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    start_encode()
    test_output = fake_output.getvalue()
    assert test_output == output


@pytest.mark.parametrize(
    "user_input,output",
    (
        ("", "Строка пустая!\n"),
        ("a3b6a1c12", "Результат:\taaabbbbbbacccccccccccc\n"),
        (
            "A1B6B8N0V5",
            "Ошибка! Причина: Строка должно состоять из цифр и строчных латинских букв\n",
        ),
        ("12f7b45m13", "Ошибка! Причина: Строка не может начинаться с цифры\n"),
        ("a123b70m", "Ошибка! Причина: Строка должна оканчиваться цифрой\n"),
        (
            "vv45z1r34y6v3n1",
            "Ошибка! Причина: Строка должна состоять из пар строчная латинская буква + число\n",
        ),
    ),
)
def test_start_decode(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    start_decode()
    test_output = fake_output.getvalue()
    assert test_output == output
