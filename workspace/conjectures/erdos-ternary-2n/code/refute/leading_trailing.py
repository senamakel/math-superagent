"""Refute the open rung R-leading-trailing.

Rung statement (with difficulties middle-digits, density-gap, independence off):
  For a stated L, for every integer n > 8, the base-3 expansion of 2^n contains
  a digit 2 among its first L leading digits OR its last L trailing digits.

A counterexample is an n > 8 whose 2^n has NO ternary digit 2 in either window:
all its 2s lie strictly in the middle (digits L..(len-L-1)).

Brute-force over small L and small n (this is the verifier of the hand
argument, which is that such n obviously exist for small L).
"""
from lib.digits3 import base3_digits_lsb


def tern_str(n):
    d = base3_digits_lsb(n)
    return "".join(str(x) for x in reversed(d))


def free_in_windows(n, L):
    """True iff 2**n has no digit-2 in first L or last L ternary digits."""
    digs = base3_digits_lsb(2 ** n)   # LSB first
    trailing = digs[:L]
    leading = digs[-L:]
    return (2 not in trailing) and (2 not in leading)


def main():
    print("2^10 =", tern_str(1024), "2^11 =", tern_str(2048),
          "2^12 =", tern_str(4096), "2^13 =", tern_str(8192))
    for L in range(1, 13):
        hits = [n for n in range(9, 5000) if free_in_windows(n, L)]
        # show lowest and highest known
        print(f"L={L}: exempt n (first 8) = {hits[:8]}   "
              f"total in [9,4999] = {len(hits)}")


if __name__ == "__main__":
    main()
