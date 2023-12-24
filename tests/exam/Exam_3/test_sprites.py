import src.exam.Exam_3.sprites
from src.exam.Exam_3.sprites import *
from io import StringIO
import pytest


FAKE_ROW_NO_SYMMETRY = ["█", " ", "█", "█", " "]
FAKE_ROW_FOR_SYMMETRY = ["█", " ", "█"]


@pytest.fixture
def patch_create_row(monkeypatch):
    def fake_row(size):
        return FAKE_ROW_NO_SYMMETRY

    monkeypatch.setattr(src.exam.Exam_3.sprites, "create_row", fake_row)


@pytest.fixture
def patch_create_symmetry_row(monkeypatch):
    def fake_row(size):
        return FAKE_ROW_FOR_SYMMETRY

    monkeypatch.setattr(src.exam.Exam_3.sprites, "create_row", fake_row)


@pytest.fixture
def patch_symmetry_vertical(monkeypatch):
    def fake_symmetry():
        return (True, False)

    monkeypatch.setattr(src.exam.Exam_3.sprites, "select_symmetry", fake_symmetry)


@pytest.fixture
def patch_symmetry_horizontal(monkeypatch):
    def fake_symmetry():
        return (False, True)

    monkeypatch.setattr(src.exam.Exam_3.sprites, "select_symmetry", fake_symmetry)


@pytest.fixture
def patch_symmetry_multiple(monkeypatch):
    def fake_symmetry():
        return (True, True)

    monkeypatch.setattr(src.exam.Exam_3.sprites, "select_symmetry", fake_symmetry)


@pytest.mark.parametrize(
    "size,expected",
    (
        ("2", True),
        ("4", True),
        ("1000", True),
        ("-12", False),
        ("1", False),
        ("1001", False),
        ("0.78", False),
        ("TEST", False),
    ),
)
def test_is_correct_size(size, expected):
    function = is_correct_size(size)
    assert function == expected


@pytest.mark.parametrize(
    "sprite,expected",
    (
        ([["█", "█"], ["█", "█"]], f"{Pixel}{Pixel}\n{Pixel}{Pixel}\n"),
        ([[" ", " "], [" ", " "]], f"  \n  \n"),
    ),
)
def test_display_sprite(sprite, expected, monkeypatch):
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    display_sprite(sprite)
    test_output = fake_output.getvalue()
    assert test_output == expected


def test_create_vertical(patch_create_row):
    sprite = create_sprite_vertical(5)
    assert sprite == [FAKE_ROW_NO_SYMMETRY for _ in range(5)]


def test_create_horizontal_even(patch_create_symmetry_row):
    sprite = create_sprite_horizontal(6)
    assert sprite == [FAKE_ROW_FOR_SYMMETRY + FAKE_ROW_FOR_SYMMETRY for _ in range(6)]


def test_create_horizontal_odd(patch_create_symmetry_row):
    sprite = create_sprite_horizontal(5)
    assert sprite == [["█", " ", "█", " ", "█"] for _ in range(5)]


def test_create_multiple_symmetry(patch_create_symmetry_row):
    sprite = create_sprite_horizontal(5)
    assert sprite == [["█", " ", "█", " ", "█"] for _ in range(5)]


def test_create_sprite_first_case(patch_create_row, patch_symmetry_vertical):
    sprite = create_sprite(5)
    assert sprite == [FAKE_ROW_NO_SYMMETRY for _ in range(5)]


def test_create_sprite_second_case(
    patch_create_symmetry_row, patch_symmetry_horizontal
):
    sprite = create_sprite(6)
    assert sprite == [FAKE_ROW_FOR_SYMMETRY + FAKE_ROW_FOR_SYMMETRY for _ in range(6)]


def test_create_sprite_third_case(patch_create_symmetry_row, patch_symmetry_multiple):
    sprite = create_sprite(5)
    assert sprite == [["█", " ", "█", " ", "█"] for _ in range(5)]
