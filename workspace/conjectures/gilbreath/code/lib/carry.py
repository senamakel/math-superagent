#!/usr/bin/env python3
"""Two's-complement carry/borrow bridge for |a-b|.

The absolute difference |a-b| is computed by two finite transducers:
  * a 3-state left-to-right (MSB-first) COMPARATOR that decides the sign,
    states: EQ (so-far equal), GT (a greater), LT (b greater);
  * a 2-state right-to-left (LSB-first) BORROW-SUBTRACTOR that produces the
    magnitude bits, using the two's-complement identity
        a - b == a + ~b + 1   (mod 2^m),
    so a subtraction BORROW is exactly an ADDITION CARRY of adding the
    bit-complement of b (plus 1) to a.

The 2-state borrow state c is the carry-in of the addition a + ~b + 1; the
carry-out to the next (more significant) bit is the majority-like rule
    c' = 1 iff a + (1 - b) + c >= 2,   i.e. (a,b,c) in {(1,1,·),(1,0,1),(0,1,1)}.
The output (lowest) bit is out = (a + (1-b) + c) mod 2, and with the usual
top-bit sign convention this reproduces a - b as a signed m-bit number.

Everything here is exact integer / boolean arithmetic. The exhaustive check run
in carry/* proves the composed transducer equals |a-b| for all a,b < 2^14.
"""
from functools import lru_cache


# --------------------------------------------------------------------------
# 3-state comparator (MSB first). Returns the sign of (a - b):
#   1 -> a > b, 0 -> a == b, -1 -> a < b.
# --------------------------------------------------------------------------
def comparator_sign(abits, bbits):
    """Given two equal-length MSB-first bit lists, return sign of a-b in {-1,0,1}."""
    state = 0  # 0 = EQ, 1 = GT, -1 = LT
    for x, y in zip(abits, bbits):
        if state == 0:
            if x != y:
                state = 1 if x > y else -1
        # once decided, state is fixed for the remaining (more significant)
        # digit is more significant only if MSB first -- here abits is MSB first,
        # so the FIRST differing bit decides; after that we keep scanning.
    return state


# --------------------------------------------------------------------------
# 2-state borrow-subtractor (LSB first), two's complement.
# Returns (outbits, final_carry) where outbits is LSB-first magnitude (after
# sign convention applied outside) and final_carry is the top carry.
# --------------------------------------------------------------------------
def borrow_bits_lsb(abits, bbits, cin=1):
    """LSB-first bit lists of equal length m. Returns (bits, cout):
    bits[0] is the least significant result bit of (a - b) as a signed m-bit
    number computed via a + ~b + 1; cout is the final carry-out (ignored when
    the result fits in m bits, which it does iff |a-b| < 2^(m-1) and the sign
    convention is handled outside). The two's-complement identity a-b = a+~b+1
    requires carry-in 1 (the '+1' of the complement), hence cin defaults to 1."""
    m = len(abits)
    out = [0] * m
    c = cin
    for i in range(m):
        x = abits[i]
        y = 1 - bbits[i]     # ~b_i
        s = x + y + c
        out[i] = s & 1
        c = 1 if s >= 2 else 0
    return out, c


# --------------------------------------------------------------------------
# Composed transducer: |a-b| via sign + magnitude.
# The magnitude when a>=b is a-b; when a<b it is b-a. We compute it directly
# from the borrow chain of the appropriate subtraction, but the cleanest
# machine-checked route is: run borrow on (a, b) for the a-b magnitude and on
# (b, a) for the b-a magnitude, select by the comparator sign.
# Returns |a-b| as an integer (MSB-first reconstruction).
# --------------------------------------------------------------------------
@lru_cache(maxsize=None)
def absdiff_transducer(a, b, m):
    """Integer |a-b| computed purely through the comparator and borrow chain
    on m-bit fixed-width two's-complement representations."""
    am = [(a >> i) & 1 for i in range(m)]           # LSB first
    bm = [(b >> i) & 1 for i in range(m)]
    sign = comparator_sign(list(reversed(am)), list(reversed(bm)))
    if sign == 0:
        return 0
    if sign >= 1:
        bits, _ = borrow_bits_lsb(am, bm)
        val = sum(bits[i] << i for i in range(m))
        return val & ((1 << m) - 1)
    else:
        bits, _ = borrow_bits_lsb(bm, am)
        val = sum(bits[i] << i for i in range(m))
        return val & ((1 << m) - 1)


# --------------------------------------------------------------------------
# One-cell simulated borrow chain: emit, per position, the carry-out bit, for
# the subtraction a-b in m-bit two's complement. This is the object whose
# count over positions is compared with nu2 in the carry-decorrelation claim.
# --------------------------------------------------------------------------
def borrow_chain(a, b, m, cin=1):
    """Return the list of carry-out bits c' at positions 0..m-1 of the
    two's-complement subtraction a - b (as a + ~b + 1), LSB first."""
    am = [(a >> i) & 1 for i in range(m)]
    bm = [(b >> i) & 1 for i in range(m)]
    c = cin
    carries = []
    for i in range(m):
        x = am[i]
        y = 1 - bm[i]
        s = x + y + c
        c = 1 if s >= 2 else 0
        carries.append(c)
    return carries


# --------------------------------------------------------------------------
# Two-operand addition carry chain (Diaconis-Fulman object): c' is the carry
# out of a_i + b_i + c_i for i.i.d. bits. c' = majority(a,b,c).
# --------------------------------------------------------------------------
def add_carry_chain(abits, bbits, cin=0):
    """LSB-first bit lists. Return (outbits, carries) of a+b, where carries[i]
    is the carry-out after position i."""
    m = len(abits)
    out = [0] * m
    carries = []
    c = cin
    for i in range(m):
        s = abits[i] + bbits[i] + c
        out[i] = s & 1
        c = 1 if s >= 2 else 0
        carries.append(c)
    return out, carries
