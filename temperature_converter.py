"""Temperature conversion utilities for SCRUM-9."""

from __future__ import annotations

Number = int | float


def celsius_to_fahrenheit(celsius: Number) -> float:
    """Return ``celsius`` converted to degrees Fahrenheit.

    Uses ``F = (C * 9/5) + 32``.
    """
    return celsius * 9 / 5 + 32
