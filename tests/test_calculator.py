import sys
from pathlib import Path
import pytest

# Adding path to Python
project_directory = Path(__file__).resolve().parent.parent
sys.path.append(str(project_directory))

from app.services.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-2, 2) == 0
    assert calculator.add(0, 0) == 0


def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(2, -2) == 4
    assert calculator.subtract(0, 0) == 0


def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 2) == -4
    assert calculator.multiply(0, 1) == 0


def test_divide(calculator):
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(-6, 2) == -3

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)


def test_square_root(calculator):
    assert calculator.square_root(9) == 3
    assert calculator.square_root(0) == 0

    with pytest.raises(ValueError, match="Cannot compute the square root of a negative number"):
        calculator.square_root(-1)


def test_generate_random_string(calculator, monkeypatch):
    def mock_get(url):
        class MockResponse:
            status_code = 200
            text = "randomstring\n"

            @staticmethod
            def strip():
                return "randomstring"

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    result = calculator.generate_random_string(12)
    assert len(result) == 12
    assert isinstance(result, str)
