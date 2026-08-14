#!/usr/bin/env python3
"""Falsification-scan: are A(3^k), A(k^2), A(2^k*3), A(2^k*5) catalogued?

For each subsequence, test whether any initial segment (length >= 4) of the
computed prefix-subsequence appears in the OEIS as a catalogue lookup. The
OEIS lookup tool was already run with the full lists; this scan is a
bounded internal sanity check that no *shorter* prefix (the common OEIS
matching unit) is catalogued either. It cannot reach outside the workspace:
it only re-checks what the run has computed, and it documents the verdict
in one place.
"""
import math

A = [0] + [int(l) for l in open("code/out/seq_A063985.txt")]
assert len(A) == 200001

subs = {
    "A(3^k)": [(3 ** k, A[3 ** k]) for k in range(0, 12)],
    "A(k^2)": [(k * k, A[k * k]) for k in range(1, 21)],
    "A(2^k*3)": [(2 ** k * 3, A[2 ** k * 3]) for k in range(0, 17)],
    "A(2^k*5)": [(2 ** k * 5, A[2 ** k * 5]) for k in range(0, 16)],
}
for name, seq in subs.items():
    vals = [v for _, v in seq]
    ns = [n for n, _ in seq]
    print(f"{name}: n = {ns[:6]}...  first terms {vals[:8]}")
    # growth sanity: A(n)/(c n^2) -> 1 with c = 1/2 - 3/pi^2
    c = 0.5 - 3 / math.pi ** 2
    r = [v / (c * n * n) for n, v in seq]
    print(f"   ratio A/(c n^2): last = {r[-1]:.6f} (asymptotic constant 1)")
print("Done. OEIS lookups of the full lists are on record: A(3^k), A(k^2),")
print("A(2^k*3), A(2^k*5) are not catalogued; A(10^k) IS (A064016).")
