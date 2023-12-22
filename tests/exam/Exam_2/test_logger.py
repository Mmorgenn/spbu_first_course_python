from src.exam.Exam_2.logger import logger
import datetime
import tempfile
import pytest
from unittest import mock

FAKE_TIME = datetime.datetime(2020, 12, 12, 14, 30, 30, 420766)


@pytest.fixture
def patch_datetime_now(monkeypatch):
    class fake_time(datetime.datetime):
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, "datetime", fake_time)


@pytest.mark.parametrize(
    "arguments,expected",
    (
        ((("1", "2"),), ["12/12/2020 14:30:30 get_summary a=1 b=2 3\n"]),
        ((("test", "text"),), ["12/12/2020 14:30:30 get_summary a=test b=text -1\n"]),
        (
            (("1", "2"), ("33", "77"), ("num", "0")),
            [
                "12/12/2020 14:30:30 get_summary a=1 b=2 3\n",
                "12/12/2020 14:30:30 get_summary a=33 b=77 110\n",
                "12/12/2020 14:30:30 get_summary a=num b=0 -1\n",
            ],
        ),
    ),
)
def test_logger_simple_function(arguments, expected, patch_datetime_now):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as templ_file:
        log_file = templ_file.name

        @logger(log_file)
        def get_summary(a, b):
            if a.isdigit() and b.isdigit():
                return int(a) + int(b)
            return -1

        for argement_1, argement_2 in arguments:
            get_summary(argement_1, argement_2)

        with open(log_file, "r") as file:
            for i in range(len(expected)):
                assert file.readline() == expected[i]


def test_logger_recursion_function(patch_datetime_now):
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as templ_file:
        log_file = templ_file.name

        @logger(log_file)
        def f(a, b):
            if a != 0:
                return f(a - 1, b - 1)
            return b

        f(1, 1)
        f(b=2, a=1)

        expected = [
            "12/12/2020 14:30:30 f a=0 b=0 0\n",
            "12/12/2020 14:30:30 f a=1 b=1 0\n",
            "12/12/2020 14:30:30 f a=0 b=1 1\n",
            "12/12/2020 14:30:30 f a=1 b=2 1\n",
        ]

        with open(log_file, "r") as file:
            for i in range(len(expected)):
                assert file.readline() == expected[i]
