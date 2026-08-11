#!/usr/bin/env python3
"""
verify_matrix.py -- independent verification of the PE175 final answer using a
2x2 matrix model over SBE runs.

This is deliberately INDEPENDENT of solution.py's Euclidean-peel loop.  It uses
only:

  * the verified recurrences  f(2m)=f(m)+f(m-1), f(2m+1)=f(m), f(2m-1)=f(m-1);
  * the 2x2 matrix representation over the state vector
        v = [f(m), f(m-1)]^T,   root m=1  ->  v = [f(1), f(0)] = [1,1]^T;
  * the unipotent closed forms
        M0^k = [[1,k],[0,1]]   (k appended '0' bits)
        M1^k = [[1,0],[k,1]]   (k appended '1' bits)
  * python ints / fractions.Fraction exclusively (exact arithmetic).

A whole SBE run of length k is processed in O(1) iterations; only big-int
arithmetic scales with k (constructing n).  No bit-by-bit loop, no search.

Worked check (n=241, SBE [4,3,1]):
  binary "11110001"; the leading '1' is the root, remaining runs are
  (3 ones, 3 zeros, 1 one) with bit pattern 1,0,1.
  v=[1,1]; 3 ones -> M1^3 [1,1] = [1,4] ; 3 zeros -> M0^3 [1,4] = [13,4] ;
  1 one     -> M1   [13,4] = [13,17] -> ratio 13/17.  (matches statement)
"""

from fractions import Fraction


# ---------------------------------------------------------------------------
# run application (closed form, exact ints)
# ---------------------------------------------------------------------------
def apply_run(v, bit, k):
    """Apply a run of k identical bits ('0' or '1') to state v=[f(m),f(m-1)].

    bit=='0': M0^k = [[1,k],[0,1]] -> v[0] += k*v[1]
    bit=='1': M1^k = [[1,0],[k,1]] -> v[1] += k*v[0]
    Returns new [a', b'] as a list of python ints.
    """
    a, b = v
    if bit == '0':
        return [a + k * b, b]
    elif bit == '1':
        return [a, k * a + b]
    else:
        raise ValueError(f"bit must be '0' or '1', got {bit!r}")


def ratio(v):
    """f(n)/f(n-1) from a state vector [f(n), f(n-1)]."""
    return Fraction(v[0], v[1])


# ---------------------------------------------------------------------------
# run-length encoding of a binary string (for the n reconstruction check)
# ---------------------------------------------------------------------------
def rle(bits):
    """Compact run-length encoding of a binary string, MSB first."""
    if not bits:
        return []
    runs = []
    cur = bits[0]
    length = 1
    for ch in bits[1:]:
        if ch == cur:
            length += 1
        else:
            runs.append(length)
            cur = ch
            length = 1
    runs.append(length)
    return runs


def main():
    all_ok = True

    # ---- (1) reproduce the worked example: n=241, SBE [4,3,1] ---------------
    print("=" * 60)
    print("[1] Worked example n=241, SBE [4,3,1]")
    print("    binary '11110001': root '1', remaining runs (3 ones,3 zeros,1 one), pattern 1,0,1")
    v = [1, 1]                      # root m=1: [f(1), f(0)]
    print(f"    v(root) = {v}")
    v = apply_run(v, '1', 3)        # 3 ones
    print(f"    after 3 ones  : v={v}")
    v = apply_run(v, '0', 3)        # 3 zeros
    print(f"    after 3 zeros : v={v}")
    v = apply_run(v, '1', 1)        # 1 one
    print(f"    after 1 one   : v={v}")
    r = ratio(v)
    print(f"    ratio f(241)/f(240) = {r}")
    ok = (r == Fraction(13, 17))
    print(f"    assert ratio == 13/17 : {ok}")
    assert v == [13, 17], v
    all_ok &= ok

    # ---- (2) final answer: SBE [1,13717420,8] --------------------------------
    print()
    print("=" * 60)
    print("[2] Final answer SBE [1,13717420,8]")
    print("    binary '1' + '0'*13717420 + '1'*8 ; root '1', then 13717420 zeros, 8 ones (pattern 0,1)")
    v = [1, 1]
    print(f"    v(root) = {v}")
    v = apply_run(v, '0', 13717420)  # 13717420 zeros
    print(f"    after 13717420 zeros : v={v}")
    v = apply_run(v, '1', 8)         # 8 ones
    print(f"    after 8 ones         : v={v}")
    r = ratio(v)
    print(f"    ratio f(n)/f(n-1) = {r}")
    ok1 = (r == Fraction(123456789, 987654321))
    ok2 = (r == Fraction(13717421, 109739369))
    print(f"    assert ratio == 123456789/987654321 : {ok1}")
    print(f"    assert ratio == 13717421/109739369 (reduced) : {ok2}")
    # sanity: divisibility by 9
    s1 = (13717421 * 9 == 123456789)
    s2 = (109739369 * 9 == 987654321)
    print(f"    sanity 13717421*9==123456789 : {s1}")
    print(f"    sanity 109739369*9==987654321 : {s2}")
    ok = ok1 and ok2 and s1 and s2
    all_ok &= ok

    # ---- (3) reconstruct n as a python int and verify its binary shape -------
    print()
    print("=" * 60)
    print("[3] Reconstruct n from SBE [1,13717420,8] arithmetically, no 13.7MB string materialized")
    # binary "1" + "0"*13717420 + "1"*8 :
    #   n = (1 << (13717420 + 8)) + (2^8 - 1)  = 2^13717428 + 255
    n = (1 << (13717420 + 8)) + (1 << 8) - 1
    nbits = len(bin(n)) - 2
    print(f"    n = 2^13717428 + 255")
    print(f"    bit length (len(bin(n))-2) = {nbits}")
    ok = (nbits == 13717429)
    print(f"    assert bit length == 13717429 : {ok}")
    all_ok &= ok

    # RLE over the full binary string (this does materialize it; ~13.7 MB string)
    bits = bin(n)[2:]
    print(f"    materialized binary string length = {len(bits)} (OK to do once)")
    runs = rle(bits)
    print(f"    run-length encoding = {runs}")
    ok = (runs == [1, 13717420, 8])
    print(f"    assert RLE == [1,13717420,8] : {ok}")
    all_ok &= ok

    # Verify binary shape by small string slices (avoid printing the whole thing)
    ok = bits[0] == '1'
    ok = ok and bits[1:1 + 4] == '0000'        # start of the zero run
    ok = ok and bits[100:100 + 4] == '0000'    # middle of the zero run
    ok = ok and bits[-8:] == '1' * 8           # final 8 ones
    ok = ok and bits[-9] == '0'                # last zero before the 1-run
    ok = ok and '1' not in bits[1:13717420 + 1]  # whole zero region has no 1
    print(f"    binary shape checks (prefix 1, long 0-run, 8 trailing ones) : {ok}")
    all_ok &= ok

    # ---- summary --------------------------------------------------------------
    print()
    print("=" * 60)
    print(f"ALL ASSERTIONS PASS: {all_ok}")
    print(f"VERIFIED FINAL RATIO = {r}  (== 123456789/987654321 == 13717421/109739369)")
    print(f"VERIFIED SBE = [1,13717420,8] with binary bit length {nbits}")
    if not all_ok:
        raise SystemExit("Some assertions failed. Exit 1.")
    print("Exit 0.")


if __name__ == "__main__":
    main()
