"""Tests for temperature_converter module (SCRUM-9)."""

import pytest

from temperature_converter import celsius_to_fahrenheit


class TestPositive:
    def test_boiling_point(self) -> None:
        assert celsius_to_fahrenheit(100) == pytest.approx(212.0)

    def test_body_temperature(self) -> None:
        assert celsius_to_fahrenheit(37) == pytest.approx(98.6)

    def test_decimal(self) -> None:
        assert celsius_to_fahrenheit(25.5) == pytest.approx(77.9)


class TestNegative:
    def test_negative_integer(self) -> None:
        assert celsius_to_fahrenheit(-10) == pytest.approx(14.0)

    def test_minus_forty_is_equal_on_both_scales(self) -> None:
        assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)

    def test_negative_decimal(self) -> None:
        assert celsius_to_fahrenheit(-17.5) == pytest.approx(0.5)


class TestZero:
    def test_zero_is_freezing_point(self) -> None:
        assert celsius_to_fahrenheit(0) == 32

    def test_float_zero_returns_float(self) -> None:
        result = celsius_to_fahrenheit(0.0)
        assert result == 32.0
        assert isinstance(result, float)


@pytest.mark.parametrize(
    ("celsius", "fahrenheit"),
    [
        (100, 212.0),
        (37, 98.6),
        (25.5, 77.9),
        (0, 32.0),
        (-10, 14.0),
        (-40, -40.0),
        (-17.5, 0.5),
    ],
)
def test_conversion_table(celsius: float, fahrenheit: float) -> None:
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)
