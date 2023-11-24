import pytest
from src.exam.Exam_2.spy import *


@spy
def foo(num):
    print(num)


@spy
def get_summary(nums: list) -> int:
    return sum(nums)


@spy
def get_subtraction(subtraction: int, subtractor: int) -> int:
    return subtraction - subtractor


def printer(list_for_print: list):
    print(*list_for_print)


@pytest.mark.parametrize(
    "function,parameters",
    ((foo, 3), (get_summary, [1])),
)
def test_spy_decorator_single_use(function, parameters):
    time_now = ctime(time())
    function(parameters)
    assert get_list_of_statistic(function) == [
        f"function {function.__name__} was called at {time_now} with parameters: {parameters}"
    ]


@pytest.mark.parametrize(
    "function,parameter_1,parameter_2,parameter_3",
    ((foo, 30, "hello", 5), (get_summary, [1], [2, 3, 4], [12, 0, 0, 10])),
)
def test_spy_decorator_single_use(function, parameter_1, parameter_2, parameter_3):
    time_now = []
    parameters = (parameter_1, parameter_2, parameter_3)
    for parameter in parameters:
        time_now.append(ctime(time()))
        function(parameter)
    list_of_statistic = [
        f"function {function.__name__} was called at {time_now[i]} with parameters: {parameters[i]}"
        for i in range(3)
    ]
    assert get_list_of_statistic(function) == list_of_statistic


def test_error():
    with pytest.raises(ValueError):
        get_list_of_statistic(printer)
    with pytest.raises(ValueError):
        printer([1, 2, 3])
        get_list_of_statistic(printer)
    with pytest.raises(ValueError):
        get_list_of_statistic(get_subtraction)
