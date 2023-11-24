import pytest
from io import StringIO
from src.exam.Exam_2.fibonacci import get_fibonacci_num, is_correct_input, main


@pytest.mark.parametrize(
    "number,expected",
    ((12, 144), (0, 0), (1, 1), (2, 1), (75, 2111485077978050))
)
def test_fibonacci(number, expected):
    function = get_fibonacci_num(number)
    assert function == expected


@pytest.mark.parametrize(
    "number,expected",
    (("12", True), ("gh", False), ("1.0", False), ("-12", False), ("912", False))
)
def test_fibonacci(number, expected):
    function = is_correct_input(number)
    assert function == expected


@pytest.mark.parametrize(
    "user_input,expected",
    (
        ("12", "Число Фибоначчи под номером 12: 144\n"),
        ("0", "Число Фибоначчи под номером 0: 0\n"),
        ("90", "Число Фибоначчи под номером 90: 2880067194370816120\n"),
        ("test", "Вы не корректно ввели число! Ваше число должно быть целым, положительным, меньше 91\n"),
        ("1.2", "Вы не корректно ввели число! Ваше число должно быть целым, положительным, меньше 91\n"),
        ("-77", "Вы не корректно ввели число! Ваше число должно быть целым, положительным, меньше 91\n"),
    ),
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert fake_output.getvalue() == expected


