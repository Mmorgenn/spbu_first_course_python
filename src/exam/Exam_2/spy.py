from functools import wraps
from time import time, ctime


def spy(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not hasattr(inner, "calls"):
            inner.calls = []
        call = {"time": ctime(time()), "args": args, "kwargs": kwargs}
        inner.calls.append(call)
        return func(*args, **kwargs)

    return inner


def get_usage_statistic(function):
    if not getattr(function, "calls", False):
        raise ValueError(
            f"Функция {function.__name__} не была вызвана после применения декоратора @spy"
        )

    for call in function.calls:
        call_time = call["time"]
        call_args = ", ".join(map(str, call["args"]))
        call_kwargs = ", ".join(
            f"{key}={value}" for key, value in call["kwargs"].items()
        )
        parameters = ", ".join(filter(None, [call_args, call_kwargs]))
        yield (call_time, parameters)


def get_list_of_statistic(function) -> list:
    list_of_statistic = []
    for time, parameters in get_usage_statistic(function):
        list_of_statistic.append(
            f"function {function.__name__} was called at {time} "
            f"with parameters: {parameters}"
        )
    return list_of_statistic
