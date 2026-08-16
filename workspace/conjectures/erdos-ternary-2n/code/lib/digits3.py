"""Base-3 digit helpers for the Erdos ternary work.

The most fundamental object is the base-3 expansion of a power of two.
This module gives the digit string least-significant-first so the digit
*position* is just the list index, which is what the 2-adic residue-class
constraint family keys on (position a and residue a mod 2^(r-2)).
"""


def base3_digits_lsb(m):
    """Return the base-3 digits of m, least significant first.

    m >= 0.  m == 0 -> [0].  For a power of two we never recompute the whole
    integer where the range is big; callers that only need digits mod 3^K
    should use base3_digits_lsb_mod instead.
    """
    if m == 0:
        return [0]
    digs = []
    while m > 0:
        digs.append(m % 3)
        m //= 3
    return digs


def base3_digits_lsb_mod(m, k):
    """The low k base-3 digits of m, least significant first, using only m mod 3^k.

    Exact integer arithmetic (modular), never larger than 3^k.  This is the
    oracle-lean form: for huge 2^n it avoids materialising the whole power.
    """
    v = m % (3 ** k)
    out = []
    for _ in range(k):
        out.append(v % 3)
        v //= 3
    return out


def digit_positions(digits_lsb, wanted=(1,)):
    """Positions (list indices) whose digit is in `wanted`. digits_lsb = LSB-first."""
    return [a for a, d in enumerate(digits_lsb) if d in wanted]


def digit_free_lsb(digits_lsb):
    """True iff no digit equals 2."""
    return all(d != 2 for d in digits_lsb)
