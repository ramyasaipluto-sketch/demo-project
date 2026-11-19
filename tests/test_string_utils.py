"""Tests for string_utils module (SCRUM-8)."""

import pytest

import string_utils


class TestReverseNormalStrings:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("hello", "olleh"),
            ("Python", "nohtyP"),
            ("a", "a"),
            ("ab", "ba"),
            ("racecar", "racecar"),
            ("abc123!?", "?!321cba"),
            ("héllo", "olléh"),
        ],
    )
    def test_reverses(self, text: str, expected: str) -> None:
        assert string_utils.reverse_string(text) == expected

    def test_double_reverse_is_identity(self) -> None:
        text = "The quick brown fox"
        assert string_utils.reverse_string(string_utils.reverse_string(text)) == text

    def test_returns_str_and_leaves_input_unchanged(self) -> None:
        text = "hello"
        result = string_utils.reverse_string(text)
        assert isinstance(result, str)
        assert text == "hello"


class TestReverseEmptyString:
    def test_empty_returns_empty(self) -> None:
        assert string_utils.reverse_string("") == ""


class TestReverseStringsWithSpaces:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("hello world", "dlrow olleh"),
            ("  leading", "gnidael  "),
            ("trailing  ", "  gniliart"),
            ("a  b   c", "c   b  a"),
            (" ", " "),
            ("   ", "   "),
        ],
    )
    def test_preserves_spaces(self, text: str, expected: str) -> None:
        assert string_utils.reverse_string(text) == expected


class TestReverseInvalidInput:
    @pytest.mark.parametrize("value", [None, 123, ["a", "b"], b"bytes"])
    def test_non_str_raises_type_error(self, value: object) -> None:
        with pytest.raises(TypeError):
            string_utils.reverse_string(value)  # type: ignore[arg-type]
