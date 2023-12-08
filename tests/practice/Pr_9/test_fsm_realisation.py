import pytest
from io import StringIO
from src.practice.Pr_9.fsm import create_fs_machine, validate_string
from src.practice.Pr_9.main import main


OUTPUT_STRING_FIRST = "[✅] - The string is suitable for the first language!\n"
OUTPUT_STRING_NONE = "[⛔] - The string is not suitable for any languages!\n"


first_dummy_fsm = create_fs_machine(
    ["1", "2", "3", "4", "5"],
    {
        0: [("1", 1)],
        1: [("2", 2)],
        2: [("3", 3)],
        3: [("4", 4)],
        4: [("5", 5)],
        5: [("1", 1)],
    },
    0,
    [3, 5],
)


second_dummy_fsm = create_fs_machine(
    ["b", "o"],
    {0: [("b", 2), ("o", 1)], 1: [("b", 1), ("o", 0)], 2: [("b", 2), ("o", 2)]},
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
def test_first_dummy_fsm(string, expected):
    function = validate_string(first_dummy_fsm, string)
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
def test_second_dummy_fsm(string, expected):
    function = validate_string(second_dummy_fsm, string)
    assert function == expected


@pytest.mark.parametrize(
    "string,expected",
    (
        ("abb", OUTPUT_STRING_FIRST),
        ("a", OUTPUT_STRING_NONE),
        ("bb", OUTPUT_STRING_NONE),
        ("ababababb", OUTPUT_STRING_FIRST),
        ("bbabb", OUTPUT_STRING_FIRST),
        ("abbabbabb", OUTPUT_STRING_FIRST),
        ("SAMPLE_TEXT", OUTPUT_STRING_NONE),
    ),
)
def test_first_fsm(string, expected, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: string)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    test_output = fake_output.getvalue()
    assert test_output == expected
