import pytest
from calculator import Calculator

test_cases_add = [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
]

test_cases_subtract = [
    (2, 3, -1),
    (0, 0, 0),
    (-1, 1, -2),
    (1.5, 2.5, -1),
]

test_cases_multiply = [
    (2, 3, 6),
    (0, 0, 0),
    (-1, 1, -1),
    (1.5, 2.5, 3.75),
]

test_cases_divide = [
    (2, 3, 2 / 3),
    (0, 1, 0),
    (-1, 1, -1),
    (1.5, 2.5, 1.5 / 2.5),
]


@pytest.fixture
def calculator():
    return Calculator()


def test_invalid_input(calculator):
    with pytest.raises(TypeError):
        calculator.add("2", 3)


def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(5, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    test_cases_add,
)
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    test_cases_subtract,
)
def test_subtract(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    test_cases_multiply,
)
def test_multiply(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    test_cases_divide,
)
def test_divide(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected
