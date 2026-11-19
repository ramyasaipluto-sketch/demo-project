"""Tests for password_validator module (SCRUM-7)."""

import pytest

import password_validator


class TestValidLength:
    @pytest.mark.parametrize(
        "password",
        [
            "abcdefgh",
            "12345678",
            "Passw0rd!",
            "a much longer passphrase",
            "x" * 128,
            "pässwörd",
        ],
    )
    def test_eight_or_more_returns_true(self, password: str) -> None:
        assert password_validator.is_valid_password_length(password) is True

    def test_exactly_min_length_boundary(self) -> None:
        password = "a" * password_validator.MIN_PASSWORD_LENGTH
        assert password_validator.is_valid_password_length(password) is True


class TestTooShort:
    @pytest.mark.parametrize(
        "password",
        ["a", "ab", "abc", "Pass1!", "1234567", " " * 7],
    )
    def test_fewer_than_eight_returns_false(self, password: str) -> None:
        assert password_validator.is_valid_password_length(password) is False

    def test_one_below_min_length_boundary(self) -> None:
        password = "a" * (password_validator.MIN_PASSWORD_LENGTH - 1)
        assert password_validator.is_valid_password_length(password) is False


class TestEmptyPassword:
    def test_empty_returns_false(self) -> None:
        assert password_validator.is_valid_password_length("") is False


class TestMinimumLengthConstant:
    def test_min_length_is_eight(self) -> None:
        assert password_validator.MIN_PASSWORD_LENGTH == 8


class TestInvalidInput:
    @pytest.mark.parametrize("value", [None, 12345678, ["a"] * 8, b"password"])
    def test_non_str_raises_type_error(self, value: object) -> None:
        with pytest.raises(TypeError):
            password_validator.is_valid_password_length(value)  # type: ignore[arg-type]
