"""Direct char-0 attack on the G-reformulation-equivalence lemma.

The lemma states: for every n, CA_n,0 holds iff for every T in {1..n}^{n-1}
the sequence (G_{T,1},..,G_{T,n-1}) is a regular sequence in Q[x_1..x_{n-1}].

By the Macaulay rank lemma (Thm 3.1 of Schaub-Spivakovsky) this regularity
is equivalent over char 0 to J_T != 0 (gcd of all CxC minors of M_T).  So I
check directly: is J_T nonzero for EVERY T at n=3 and n=4?

If some T has J_T = 0 in char 0, then the regular-sequence reformulation is
false AS TRANSCRIBED (a transcription bug in the Phi_j convention or in the
index set), even though the true theorem by Ghosh may differ.  That is
exactly the kind of mis-encoding the run must catch.
"""
import sympy as sp
from lib.badprimes import lcm_jt_over_T, jt_of_T


def main():
    lines = []
    lines.append("check: char-0 reformulation regularity (J_T != 0 for all T), exact")
    for n in (3, 4):
        lcm_j, js = lcm_jt_over_T(n)
        zeros = [T for T, j in js.items() if j == 0]
        nonzero = all(j != 0 for j in js.values())
        lines.append("")
        lines.append(f"== n={n}: |T| = {len(js)} tuples, "
                     f"all J_T nonzero = {nonzero} ==")
        lines.append(f"   lcm of all J_T = {lcm_j} = {dict(sp.factorint(lcm_j))}")
        if zeros:
            lines.append(f"   ZERO J_T tuples: {zeros[:10]} ...")
        else:
            lines.append("   no J_T is zero (regular-sequence reformulation "
                         "survives in char 0 at this n)")
        lines.append(f"   distinct J_T values: "
                     f"{ {v: sum(1 for j in js.values() if j == v) for v in set(js.values())} }")

    text = "\n".join(lines) + "\n"
    print(text)
    with open("/workspace/code/out/refute_reformulation_direct.captured.txt", "w") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
