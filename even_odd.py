"""Even or odd classification for integers (SCRUM-6)."""

from __future__ import annotations

ParityLabel = str


def _require_integer(value: int) -> int:
    """Return ``value`` if it is a true ``int`` (not ``bool`` or float)."""
    if isinstance(value, bool):
        raise TypeError("parity requires an integer, not bool")
    if not isinstance(value, int):
        raise TypeError("parity requires an integer")
    return value


def is_even(n: int) -> bool:
    """Return ``True`` when ``n`` is an even integer."""
    n = _require_integer(n)
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Return ``True`` when ``n`` is an odd integer."""
    return not is_even(n)


def check_parity(n: int) -> ParityLabel:
    """Return ``\"even\"`` or ``\"odd\"`` for integer ``n``."""
    return "even" if is_even(n) else "odd"