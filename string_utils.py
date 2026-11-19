"""String utilities (SCRUM-8)."""

from __future__ import annotations


def reverse_string(text: str) -> str:
    """Return ``text`` with its characters in reverse order.

    Reversal is per Unicode code point, so whitespace is preserved in its
    mirrored position and an empty string returns an empty string.
    """
    if not isinstance(text, str):
        raise TypeError("reverse_string requires a str")
    return text[::-1]
