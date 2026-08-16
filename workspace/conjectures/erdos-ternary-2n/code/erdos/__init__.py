"""Erdos ternary-digits oracle.

Package `code.erdos` (a plain folder on PYTHONPATH; import as
`from erdos.oracle import digit_free, sieve_count, finite_check`).

Implements the exact, float-free oracle functions for the Erdos conjecture
(1979): the only powers of 2 whose base-3 expansion avoids the digit 2 are
2^0=1, 2^2=4, 2^8=256.
"""

from .oracle import (
    digit_free,
    sieve_count,
    finite_check,
    direct_count,
    lift_count,
    to_base3,
)

__all__ = [
    "digit_free",
    "sieve_count",
    "finite_check",
    "direct_count",
    "lift_count",
    "to_base3",
]
