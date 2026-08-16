"""Scholar verification of the load-bearing control facts (NOT RUN — no execution
tool in the scholar run).

What this WOULD run, for a later tool_builder/coder to execute and record: the
canonical oracle lib.srg.is_srg on the two positive controls (rook(3)=srg(9,4,1,2),
bvls_graph()=srg(243,22,1,2)) and the two further lambda=1 family members (doily
srg(15,6,1,3), GQ(2,4) srg(27,10,1,5)); the negative controls (circulant(9,{1,2})
against (9,4,1,2), circulant(99,{1..7}) against (99,14,1,2)); and the
integrality-five-member feasibility arithmetic that corrects problem.md. Exact
integer arithmetic throughout. The identical checks are ALREADY captured in this
workspace at code/out/oracle-controls.captured.txt and
code/out/oracle_verification.captured.txt (from earlier tool_builder runs); run
this only if those captures are lost. Do not report its output as this run's.
"""
from lib.srg import (is_srg, rook, bvls_graph, doily, gq24_graph,
                     random_regular_14_99, circulant)
import numpy as np


def five_members():
    """Eigenvalue-multiplicity integrality for srg(v,k,1,2), exact.

    v = 1 + k + k(k-2)/2 ; spectrum r,s roots of x^2 + (mu-lam)x + (mu-k),
    lam=1 mu=2: x^2 + x + (2-k), so r+s=-1, rs=2-k, disc = 4k-7.
    Multiplicities: f = (k - (v-1)s)/(r-s), g = (v-1) - f over integers.
    Accept k iff both nonnegative integers.
    """
    out = []
    for k in range(1, 2000):
        v = 1 + k + k * (k - 2) // 2
        if v - 1 - k != k * (k - 2) // 2:
            continue
        disc4 = 4 * k - 7          # discriminant (r-s)^2
        if disc4 <= 0:
            continue
        root = int(round(disc4 ** 0.5))
        if root * root != disc4:
            continue
        r = (-1 + root) // 2       # (mu-lam)+... : -1 + root over 2
        s = (-1 - root) // 2
        if r + s != -1 or r * s != 2 - k:
            continue
        # g = (v-1) - f, f = (k-(v-1)s)/(r-s)
        num = k - (v - 1) * s
        den = r - s
        if num % den != 0:
            continue
        f = num // den
        g = (v - 1) - f
        if f >= 0 and g >= 0 and f + g == v - 1:
            out.append((v, k, r, s, f, g))
    return out


def main():
    print("=== positive controls (canonical oracle) ===")
    print("rook(3) srg(9,4,1,2):", is_srg(rook(3), 9, 4, 1, 2))
    print("doily  srg(15,6,1,3):", is_srg(doily(), 15, 6, 1, 3))
    print("GQ(2,4) srg(27,10,1,5):", is_srg(gq24_graph(), 27, 10, 1, 5))
    B = bvls_graph()
    print("bvls shape:", B.shape, "edges:", int(B.sum() // 2))
    print("bvls srg(243,22,1,2):", is_srg(B, 243, 22, 1, 2))

    print("\n=== negative controls (reject, exercising the count path) ===")
    print("C9(1,2) vs (9,4,1,2):", is_srg(circulant(9, [1, 2]), 9, 4, 1, 2))
    print("circulant(99,{1..7}) vs (99,14,1,2):",
          is_srg(circulant(99, list(range(1, 8))), 99, 14, 1, 2))

    print("\n=== feasibility: eigenvalue-multiplicity integrality ===")
    for row in five_members():
        v, k, r, s, f, g = row
        star = "  <-- the object of this problem" if (v, k) == (99, 14) else ""
        print(f"  srg({v},{k},1,2)  spectrum {r}^{f},{s}^{g}{star}")

    print("\n=== 99 and 243 are both in the family; 33 is not ===")
    v33 = 1 + 8 + 8 * 6 // 2
    print("srg(33,8,1,2): v=1+8+8*6/2 =", v33)
    # multiplicity numerator for k=8: 2k-(v-1) over sqrt(4k-7)=5
    print("  2k-(v-1) =", 16 - (33 - 1), "not divisible by sqrt(25)=5 -> non-integral")


if __name__ == "__main__":
    main()
