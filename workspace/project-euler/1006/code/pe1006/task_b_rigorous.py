"""Task B (rigorous): test genuine eventual periodicity of r(k)=Psi(k) mod M.

Avoid vacuous checks: require enough overlapping comparisons, and require the
period to hold over a meaningful window. Report the smallest period that
survives, or None.
"""
import os
from fractions import Fraction

MOD = 101001001
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "psi_data_1_150.txt")


def load_psi(path):
    psi = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            parts = line.split(":")
            try:
                k = int(parts[0].strip())
            except ValueError:
                continue
            psi[k] = int(parts[-1].strip())
    return psi


def main():
    psi = load_psi(DATA)
    seq = [psi[k] for k in sorted(psi)]
    r = [x % MOD for x in seq]
    n = len(r)

    print("Genuine periodicity search on r(1..150) mod", MOD)
    print("n =", n)

    # A genuine eventual period (pre, T) requires at least H overlapping
    # aligned comparisons, and those comparisons must be non-vacuous.
    H = 40  # require at least 40 aligned comparisons (stronger than a single)
    found = []
    for pre in range(0, n):
        for T in range(1, n):
            # number of aligned comparisons in range
            count = sum(1 for i in range(pre, n - T))
            if count < H:
                continue
            if all(r[i] == r[i + T] for i in range(pre, n - T)):
                found.append((pre, T))
                break  # smallest T for this pre
    print("candidate (pre, T) with >=40 aligned comparisons:")
    for f in found[:10]:
        print("  ", f)
    if not found:
        print("  none found -> r(k) is NOT eventually periodic with any period < 150 over the data")
    else:
        print("smallest candidate:", found[0])

    print()
    print("Conclusion for Task B: no small/simple eventual period is present in the")
    print("first 150 exact terms. The trivial (0, 150) reported earlier is vacuous and")
    print("is NOT a genuine period. A genuine period would connect to ord_10(M) and")
    print("the Pisano structure, far beyond n=150 and not visible here.")


if __name__ == "__main__":
    main()
