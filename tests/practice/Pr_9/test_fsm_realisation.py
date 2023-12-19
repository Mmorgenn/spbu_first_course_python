import pytest
from io import StringIO
from src.practice.Pr_9.fsm import create_fs_machine, validate_string
from src.practice.Pr_9.main import main, OUTPUT_STRING_ANY, OUTPUT_STRING_NONE


@pytest.fixture
def create_first_dummy_fsm():
    return create_fs_machine(
        "first_dummy",
        {
            0: {"1": 1},
            1: {"2": 2},
            2: {"3": 3},
            3: {"4": 4},
            4: {"5": 5},
            5: {"1": 1},
        },
        0,
        [3, 5],
    )


@pytest.fixture
def create_second_dummy_fsm():
    return create_fs_machine(
        "second_dummy",
        {0: {"b": 2, "o": 1}, 1: {"b": 1, "o": 0}, 2: {"b": 2, "o": 2}},
        0,
        [2],
    )


@pytest.mark.parametrize(
    "string,expected",
    (
        ("123", True),
        ("12345", True),
        ("112345", False),
        ("23", False),
        ("1234512345", True),
        ("12345123", True),
        ("12312345", False),
        ("test", False),
        ("012345", False),
        ("12345\n", False),
    ),
)
def test_first_dummy_fsm(string, expected, create_first_dummy_fsm):
    function = validate_string(create_first_dummy_fsm, string)
    assert function == expected


@pytest.mark.parametrize(
    "string,expected",
    (
        ("b", True),
        ("bbbbbb", True),
        ("boo", True),
        ("bobobobo", True),
        ("ooobbobobob", True),
        ("o", False),
        ("obb", False),
        ("obo", False),
        ("ooooooobb", False),
        ("123456", False),
        ("boofoo", False),
        ("oooooooo", False),
    ),
)
def test_second_dummy_fsm(string, expected, create_second_dummy_fsm):
    function = validate_string(create_second_dummy_fsm, string)
    assert function == expected


@pytest.mark.parametrize(
    "string,expected",
    (
        ("abb", f"{OUTPUT_STRING_ANY} first_fs_machine\n"),
        ("a", OUTPUT_STRING_NONE + "\n"),
        ("bb", OUTPUT_STRING_NONE + "\n"),
        ("ababababb", f"{OUTPUT_STRING_ANY} first_fs_machine\n"),
        ("bbabb", f"{OUTPUT_STRING_ANY} first_fs_machine\n"),
        ("abbabbabb", f"{OUTPUT_STRING_ANY} first_fs_machine\n"),
        ("SAMPLE_TEXT", OUTPUT_STRING_NONE + "\n"),
        ("123456", f"{OUTPUT_STRING_ANY} second_fs_machine\n"),
        ("0.7788", f"{OUTPUT_STRING_ANY} second_fs_machine\n"),
        ("12.45E+13", f"{OUTPUT_STRING_ANY} second_fs_machine\n"),
        ("34E98", f"{OUTPUT_STRING_ANY} second_fs_machine\n"),
        ("1E-78", f"{OUTPUT_STRING_ANY} second_fs_machine\n"),
        ("56.78E7", f"{OUTPUT_STRING_ANY} second_fs_machine\n"),
        ("1-E78", OUTPUT_STRING_NONE + "\n"),
        ("12.E-12.0", OUTPUT_STRING_NONE + "\n"),
        ("7-8", OUTPUT_STRING_NONE + "\n"),
        ("E-42", OUTPUT_STRING_NONE + "\n"),
    ),
)
def test_first_fsm(string, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: string)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    test_output = fake_output.getvalue()
    assert test_output == expected
