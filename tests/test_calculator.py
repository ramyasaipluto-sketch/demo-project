"""Tests for calculator module (SCRUM-1)."""

import pytest

import calculator


class TestAdd:
    def test_positive(self) -> None:
        assert calculator.add(2, 3) == 5

    def test_negative(self) -> None:
        assert calculator.add(-2, -3) == -5

    def test_mixed_sign(self) -> None:
        assert calculator.add(-2, 5) == 3

    def test_decimals(self) -> None:
        assert calculator.add(1.5, 2.25) == pytest.approx(3.75)


class TestSubtract:
    def test_positive(self) -> None:
        assert calculator.subtract(10, 4) == 6

    def test_negative(self) -> None:
        assert calculator.subtract(-5, -2) == -3

    def test_decimals(self) -> None:
        assert calculator.subtract(5.5, 2.2) == pytest.approx(3.3)


class TestMultiply:
    def test_positive(self) -> None:
        assert calculator.multiply(3, 4) == 12

    def test_negative(self) -> None:
        assert calculator.multiply(-3, 4) == -12

    def test_zero(self) -> None:
        assert calculator.multiply(99, 0) == 0

    def test_decimals(self) -> None:
        assert calculator.multiply(0.5, 0.2) == pytest.approx(0.1)


class TestDivide:
    def test_integers(self) -> None:
        assert calculator.divide(10, 2) == 5.0

    def test_decimals(self) -> None:
        assert calculator.divide(7.5, 2.5) == pytest.approx(3.0)

    def test_negative(self) -> None:
        assert calculator.divide(-8, 2) == -4.0

    def test_division_by_zero_raises(self) -> None:
        with pytest.raises(ValueError, match="division by zero"):
            calculator.divide(1, 0)

    def test_division_by_zero_float(self) -> None:
        with pytest.raises(ValueError, match="division by zero"):
            calculator.divide(1.0, 0.0)
