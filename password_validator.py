"""Password length validation (SCRUM-7)."""

from __future__ import annotations

MIN_PASSWORD_LENGTH = 8


def is_valid_password_length(password: str) -> bool:
    """Return ``True`` when ``password`` has at least ``MIN_PASSWORD_LENGTH`` characters.

    Length is counted per Unicode code point and every character (including
    whitespace) counts, so an empty string is always invalid.
    """
    if not isinstance(password, str):
        raise TypeError("is_valid_password_length requires a str")
    return len(password) >= MIN_PASSWORD_LENGTH
