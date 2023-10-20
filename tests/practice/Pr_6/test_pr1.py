import pytest
from io import StringIO
from src.practice.Pr_6.pr1 import (
    start,
    check_numbers,
    choose_solution,
    linear_equation_solve,
    quadratic_equation_solve,
)


test_check_1 = [
    (["1", "2", "3"], [1.0, 2.0, 3.0]),
    (["-1", "-2", "3.0"], [-1.0, -2.0, 3.0]),
    (["1.5", "2.36", "-3"], [1.5, 2.36, -3.0]),
]
test_check_2 = [([]), (["1", "2.0"]), ["what", "1", "10", "12.0"]]
test_check_3 = [
    (["12.0.0", "1", "13"]),
    (["2.", "1.0", "10"]),
    (["text", "for", "test"]),
]
test_quadratic_1 = [
    (1.0, 17.0, -18.0, [-18.0, 1.0]),
    (5.0, 7.0, 2.0, [-1.0, -0.4]),
    (1.0, 4.0, 4.0, [-2.0]),
]
test_quadratic_2 = [(1.0, 2.0, 3.0), (10.0, 0.0, 23.0), (2.0, 1.0, 101.0)]
test_linear_1 = [
    (0.0, 1.0, 2.0, [-2.0]),
    (0.0, -10.0, 5.0, [0.5]),
    (0.0, 25.0, -10.0, [0.4]),
]
test_linear_2 = [(1.0, 2.0, [-2.0]), (-10.0, 5.0, [0.5]), (25.0, -10.0, [0.4])]
test_no_solution = [(0.0, 0.0, 0.0), (0.0, 0.0, 12.0)]
test_user_input = [
    ("0 1 2", "Решениe: -2.0\n"),
    ("1 17 -18", "Решениe: -18.0, 1.0\n"),
    ("1 2 3", "Уравнение не имеет корней\n"),
    ("1", "Чисел должно было быть ровно 3\n"),
    ("abra cada bra", "Не все эллементы которые вы ввели являются числами\n"),
    (
        "0 0 0",
        "Введенные данные не подходят ни для квадратного уравнения, ни для линейного\n",
    ),
]


@pytest.mark.parametrize("nums,expected", test_check_1)
def test_check_numbers_three_correct_numbers(nums, expected):
    function = check_numbers(nums)
    assert function == expected


@pytest.mark.parametrize("nums", test_check_2)
def test_check_numbers_incorrect_count_numbers(nums):
    with pytest.raises(TypeError):
        check_numbers(nums)


@pytest.mark.parametrize("nums", test_check_3)
def test_check_numbers_incorrect_elements(nums):
    with pytest.raises(SyntaxError):
        check_numbers(nums)


@pytest.mark.parametrize("num_1,num_2,num_3,expected", test_quadratic_1)
def test_chose_solution_quadratic_equation(num_1, num_2, num_3, expected):
    function = choose_solution(num_1, num_2, num_3)
    assert function == expected


@pytest.mark.parametrize("num_1,num_2,num_3,expected", test_linear_1)
def test_chose_solution_linear_equation(num_1, num_2, num_3, expected):
    function = choose_solution(num_1, num_2, num_3)
    assert function == expected


@pytest.mark.parametrize("num_1,num_2,num_3", test_no_solution)
def test_chose_solution_no_options(num_1, num_2, num_3):
    with pytest.raises(ValueError):
        choose_solution(num_1, num_2, num_3)


@pytest.mark.parametrize("k,b,expected", test_linear_2)
def test_linear_equation_solve(k, b, expected):
    function = linear_equation_solve(k, b)
    assert function == expected


@pytest.mark.parametrize("a,b,c,expected", test_quadratic_1)
def test_quadratic_equation_solve(a, b, c, expected):
    function = quadratic_equation_solve(a, b, c)
    assert function == expected


@pytest.mark.parametrize("a,b,c", test_quadratic_2)
def test_quadratic_discriminant_less_zero(a, b, c):
    with pytest.raises(ArithmeticError):
        quadratic_equation_solve(a, b, c)


@pytest.mark.parametrize("user_input,output", test_user_input)
def test_start(user_input, output, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    start()
    test_output = fake_output.getvalue()
    assert test_output == output
