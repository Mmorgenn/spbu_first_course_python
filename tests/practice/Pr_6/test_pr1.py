import pytest
from io import StringIO
from src.practice.Pr_6.pr1 import (
    start,
    parsing_numbers,
    get_solution,
    linear_equation_solve,
    quadratic_equation_solve,
)


@pytest.mark.parametrize(
    "nums,expected",
    (
        (["2e-3", "2", "3"], [0.002, 2.0, 3.0]),
        (["-1", "-2", "3."], [-1.0, -2.0, 3.0]),
        ([".5", "2.36", "-3"], [0.5, 2.36, -3.0]),
    ),
)
def test_parsing_numbers_three_correct_numbers(nums, expected):
    function = parsing_numbers(nums)
    assert function == expected


@pytest.mark.parametrize(
    "nums",
    (
        ([".1", "1", "12.0.0"]),
        (["2,0", "1.0", "10"]),
        (["inf", "2", "0.0"]),
        (["text", "for", "test"]),
        (["++2.0", "1.0", "12"]),
        ([]),
        (["1", "2.0"]),
        (["what", "1", "10", "12.0."]),
    ),
)
def test_parsing_numbers_incorrect_elements(nums):
    with pytest.raises(ValueError):
        parsing_numbers(nums)


@pytest.mark.parametrize(
    "num_1,num_2,num_3,expected",
    (
        (1.0, 17.0, -18.0, (1.0, -18.0)),
        (5.0, 7.0, 2.0, (-0.4, -1.0)),
        (1.0, 4.0, 4.0, (-2.0,)),
    ),
)
def test_get_solution_quadratic_equation(num_1, num_2, num_3, expected):
    function = get_solution(num_1, num_2, num_3)
    assert function == expected


@pytest.mark.parametrize(
    "num_1,num_2,num_3,expected",
    (
        (0.0, 1.0, 2.0, (-2.0,)),
        (0.0, -10.0, 5.0, (0.5,)),
        (0.0, 25.0, -10.0, (0.4,)),
    ),
)
def test_get_solution_linear_equation(num_1, num_2, num_3, expected):
    function = get_solution(num_1, num_2, num_3)
    assert function == expected


@pytest.mark.parametrize("num_1,num_2,num_3", ((0.0, 0.0, 0.0), (0.0, 0.0, 12.0)))
def test_get_solution_no_options(num_1, num_2, num_3):
    with pytest.raises(ValueError):
        get_solution(num_1, num_2, num_3)


@pytest.mark.parametrize(
    "k,b,expected", ((1.0, 2.0, (-2.0,)), (-10.0, 5.0, (0.5,)), (25.0, -10.0, (0.4,)))
)
def test_linear_equation_solve(k, b, expected):
    function = linear_equation_solve(k, b)
    assert function == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    (
        (1.0, 17.0, -18.0, (1.0, -18.0)),
        (5.0, 7.0, 2.0, (-0.4, -1.0)),
        (1.0, 4.0, 4.0, (-2.0,)),
    ),
)
def test_quadratic_equation_solve(a, b, c, expected):
    function = quadratic_equation_solve(a, b, c)
    assert function == expected


@pytest.mark.parametrize(
    "a,b,c", ((1.0, 2.0, 3.0), (10.0, 0.0, 23.0), (2.0, 1.0, 101.0))
)
def test_quadratic_discriminant_less_zero(a, b, c):
    with pytest.raises(ArithmeticError):
        quadratic_equation_solve(a, b, c)


@pytest.mark.parametrize(
    "user_input,output",
    (
        ("0 1 2", "Решениe: -2.0\n"),
        ("1 17 -18", "Решениe: 1.0, -18.0\n"),
        ("1 2 3", "Уравнение не имеет корней\n"),
        (
            "1",
            "Произошла ошибка! Причина: The numbers must be 3\n",
        ),
        (
            "i u t",
            "Произошла ошибка! Причина: Each element must be float\n",
        ),
        (
            "inf 2.0 3",
            "Произошла ошибка! Причина: Element must not be inf\n",
        ),
        (
            "0 0 0",
            "Введенные данные не подходят ни для квадратного уравнения, ни для линейного\n",
        ),
    ),
)
def test_start(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    start()
    test_output = fake_output.getvalue()
    assert test_output == output
