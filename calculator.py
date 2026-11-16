"""Simple arithmetic calculator for SCRUM-1."""

from __future__ import annotations

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return ``a`` minus ``b``."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return ``a`` divided by ``b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def power(a: Number, b: Number) -> Number:
    """Return ``a`` raised to the power ``b``."""
    return a**b


def modulo(a: Number, b: Number) -> Number:
    """Return the remainder of ``a`` divided by ``b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("modulo by zero")
    return a % b


def floor_divide(a: Number, b: Number) -> Number:
    """Return ``a`` floor-divided by ``b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("floor division by zero")
    return a // b


def absolute(a: Number) -> Number:
    """Return the non-negative magnitude of ``a``."""
    return abs(a)
