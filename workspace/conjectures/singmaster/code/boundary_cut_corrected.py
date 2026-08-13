"""Boundary-cut tabulation, corrected. Diagnoses code/boundary_cut.py.

Two faults in the original:

 1. WRONG CUT.  It computes exp((log n)**(2/3) + 0.5).  The MRSTT boundary is
    k < exp((log n)^(2/3+eps)); with eps=1/2 that is exp((log n)**(7/6)).  The
    exponent applies to the whole bracket, not as an added constant.  At
    n=229969 the two differ by a factor of 411,000 (344.4 vs 1.416e8), which
    reclassifies essentially every representative.

 2. HANGS.  reps(a) is called on the Fibonacci family, whose a_j have ~1412
    digits at j=4 and vastly more beyond.  It then loops k up to log2(a) —
    about 229,000 iterations at j=6 — each doing a binary search over
    math.comb on numbers of that size.  Intractable.  But the family's (n,k)
    is known BY CONSTRUCTION, so no search is needed for it at all.
"""
import math

def cut_correct(n, eps=0.5):
    return math.exp(math.log(n) ** (2.0 / 3.0 + eps))

def cut_as_coded(n):
    return math.exp(math.log(n) ** (2.0 / 3.0) + 0.5)

def reps(a):
    """Every (n,k) with C(n,k)=a, 2<=k<=n/2. Only for small a."""
    out = []
    k = 2
    while math.comb(2 * k, k) <= a:
        lo, hi = 2 * k, a
        while lo <= hi:
            mid = (lo + hi) // 2
            c = math.comb(mid, k)
            if c == a:
                out.append((mid, k)); break
            if c < a: lo = mid + 1
            else: hi = mid - 1
        k += 1
    return out

VALS = [120, 210, 1540, 3003, 7140, 11628, 24310]
print("=" * 74)
print("Witness set: every nontrivial representative, against BOTH cuts")
print("=" * 74)
print(f"{'a':>7} {'n':>7} {'k':>4} {'cut(correct)':>14} {'verdict':>9} {'cut(as coded)':>14} {'verdict':>9}")
counts = {}
for a in VALS:
    for (n, k) in reps(a):
        cc, ca = cut_correct(n), cut_as_coded(n)
        vc = "boundary" if k < cc else "interior"
        va = "boundary" if k < ca else "interior"
        counts[a] = counts.get(a, 0) + (1 if vc == "boundary" else 0)
        print(f"{a:>7} {n:>7} {k:>4} {cc:>14.4g} {vc:>9} {ca:>14.4g} {va:>9}")

print()
print("boundary-representative count per a, under the CORRECT cut:")
for a in VALS:
    print(f"  a={a:<6} boundary reps = {counts.get(a,0)}")
print(f"  max over the witness set = {max(counts.values())}")
print("  (counting left-half reps only; both mirrors doubles it)")

print()
print("=" * 74)
print("Fibonacci family: (n,k) known by construction, no search")
print("=" * 74)
F = [0, 1]
for i in range(2, 20): F.append(F[-1] + F[-2])
print(f"{'j':>2} {'n':>8} {'k':>8} {'cut(correct)':>14} {'verdict':>9} {'cut(as coded)':>14} {'verdict':>9}")
for j in range(1, 7):
    n = F[2 * j + 2] * F[2 * j + 3] - 1
    k = F[2 * j] * F[2 * j + 3] - 1
    cc, ca = cut_correct(n), cut_as_coded(n)
    print(f"{j:>2} {n:>8} {k:>8} {cc:>14.4g} {'boundary' if k<cc else 'interior':>9} "
          f"{ca:>14.4g} {'boundary' if k<ca else 'interior':>9}")
print()
print("Read the table, not the expectation. Under the CORRECT cut every family")
print("member is BOUNDARY: k < cut in all six rows (87839 < 1.416e8 at j=6).")
print("Under the mis-coded cut j>=2 flips to INTERIOR. The two cuts therefore")
print("disagree on the whole family, and the mis-coded one hides it entirely")
print("from the boundary count that G-boundary-uniform-count is about.")
print()
print("This does NOT refute a uniform bound. Each family member is a different a,")
print("so an infinite family each contributing >=1 boundary representative is")
print("consistent with a constant C bounding the count PER a. What it does mean:")
print("the family is inside the object being counted, so any argument for C must")
print("cover it rather than set it aside as interior.")
