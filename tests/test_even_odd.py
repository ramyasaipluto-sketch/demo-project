"""Tests for even_odd module (SCRUM-6)."""

import pytest

import even_odd


class TestIsEven:
    def test_positive_even(self) -> None:
        assert even_odd.is_even(4) is True

    def test_positive_odd(self) -> None:
        assert even_odd.is_even(7) is False

    def test_zero(self) -> None:
        assert even_odd.is_even(0) is True

    def test_negative_even(self) -> None:
        assert even_odd.is_even(-8) is True

    def test_negative_odd(self) -> None:
        assert even_odd.is_even(-3) is False


class TestIsOdd:
    def test_positive_odd(self) -> None:
        assert even_odd.is_odd(9) is True

    def test_positive_even(self) -> None:
        assert even_odd.is_odd(10) is False

    def test_zero(self) -> None:
        assert even_odd.is_odd(0) is False

    def test_negative_odd(self) -> None:
        assert even_odd.is_odd(-5) is True


class TestCheckParity:
    def test_even_label(self) -> None:
        assert even_odd.check_parity(12) == "even"

    def test_odd_label(self) -> None:
        assert even_odd.check_parity(11) == "odd"

    def test_negative_even(self) -> None:
        assert even_odd.check_parity(-2) == "even"


class TestInvalidInput:
    def test_float_rejected(self) -> None:
        with pytest.raises(TypeError, match="integer"):
            even_odd.is_even(3.0)

    def test_bool_rejected(self) -> None:
        with pytest.raises(TypeError, match="not bool"):
            even_odd.is_even(True)

    def test_string_rejected(self) -> None:
        with pytest.raises(TypeError, match="integer"):
            even_odd.check_parity("2")  # type: ignore[arg-type]