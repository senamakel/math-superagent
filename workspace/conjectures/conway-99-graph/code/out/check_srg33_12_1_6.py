"""Exact-integer feasibility of srg(33,12,1,6) — Makhnev Thm 2's forced subobject.

Under Makhnev 1988 condition (*) [n3=0] at (99,14,1,2), a triangle's closure
Gamma(A) is an srg(9,4,1,2) on 9 vertices, and Makhnev's Lemmas 6-9 assemble
the closure + 20 outer triangles into a subobject Lambda_0 claimed to be an
srg(33,12,1,6). Makhnev Thm 1 then kills it: a lambda=1 SRG satisfying (*) has
mu<=3 OR is the unique (27,10,1,5); 33,12,1,6 has mu=6>3 and is not (27,10,1,5).

This program independently re-derives the *standard parameter feasibility* of
(33,12,1,6) in exact integer/Fraction arithmetic, and compares it against:
  - (27,10,1,5)  the unique non-mu<=3 exception of Makhnev Thm 1 (it EXISTS)
  - the family members (9,4,1,2),(99,14,1,2),(243,22,1,2) (all exist)
  - (33,8,1,2)   the known-inf feasible next family member (consistency check)

Mechanism tested (exact integer, no floats):
  1. eigenvalue integrality: delta=(lam-mu)^2+4(k-mu) must be a perfect square
     and r,s=(lam-mu+-sqrt(delta))/2 integers;
  2. multiplicity integrality: g = 1/2[(v-1)-(2k+(v-1)(lam-mu))/sqrt(delta)]
     must be an integer >= 0 (f=(v-1)-g likewise). All integer arithmetic.
  3. Krein conditions (exact rational comparison of the two Krein inequalities).

Nothing here asserts existence/nonexistence of srg(99,14,1,2); it computes the
feasibility of the *sub-parameter-set* (33,12,1,6) that Makhnev's mechanism
forces, and reports by which exact mechanism that set is (in)feasible.
"""
from fractions import Fraction
from sympy import integer_nthroot


def srg_feasibility(v, k, lam, mu):
    """Full standard feasibility of srg(v,k,lam,mu) in exact arithmetic.

    Returns a dict with the eigenvalues, the multiplicity of k's second
    eigenvalue, and the verdict, the mechanism, and the failure detail.
    """
    res = {"v": v, "k": k, "lam": lam, "mu": mu}

    delta = (lam - mu) ** 2 + 4 * (k - mu)
    root, perfect = integer_nthroot(delta, 2)
    if not perfect:
        res["verdict"] = "INFEASIBLE"
        res["mechanism"] = "eigenvalue integrality: 4-delta not a perfect square"
        res["detail"] = f"delta={delta} not a perfect square"
        return res
    res["sqrt_delta"] = root
    num_r, num_s = (lam - mu) + root, (lam - mu) - root
    if num_r % 2 != 0 or num_s % 2 != 0:
        res["verdict"] = "INFEASIBLE"
        res["mechanism"] = "eigenvalue integrality: r,s not integers"
        res["detail"] = f"r,s=({Fraction(num_r,2)},{Fraction(num_s,2)}) not integers"
        return res
    r, s = num_r // 2, num_s // 2
    res["r"], res["s"] = r, s

    # multiplicity of the smaller eigenvalue s
    term = 2 * k + (v - 1) * (lam - mu)      # numerator over sqrt(delta)
    res["mult_num"] = term
    if term % root != 0:
        res["verdict"] = "INFEASIBLE"
        res["mechanism"] = "multiplicity integrality"
        res["detail"] = (f"g numerator 2k+(v-1)(lam-mu) = {term} not divisible "
                         f"by sqrt(delta) = {root}")
        return res
    gfrac = Fraction((v - 1) - term // root, 2)
    if gfrac.denominator != 1:
        res["verdict"] = "INFEASIBLE"
        res["mechanism"] = "multiplicity integrality"
        res["detail"] = f"multiplicity g = {gfrac} is not an integer"
        return res
    g, f = gfrac.numerator, (v - 1) - gfrac.numerator
    if g < 0 or f < 0:
        res["verdict"] = "INFEASIBLE"
        res["mechanism"] = "multiplicity negativity"
        res["detail"] = f"g={g}, f={f} -> negative multiplicity"
        return res
    res["g"], res["f"] = g, f

    # Krein conditions: (r+1)(k+r+2s) <= (k+r)(s+1)^2  and the s/r swap.
    def krein_ok(a, b):  # a,b = the two non-k eigenvalues, a the larger
        return (a + 1) * (k + a + 2 * b) <= (k + a) * (b + 1) ** 2
    krein1 = krein_ok(r, s)
    krein2 = krein_ok(s, r)
    res["krein"] = (krein1, krein2)
    if not (krein1 and krein2):
        res["verdict"] = "INFEASIBLE"
        res["mechanism"] = "Krein condition"
        res["detail"] = f"Krein fails: ({krein1},{krein2})"
        return res

    res["verdict"] = "FEASIBLE"
    res["mechanism"] = "passes all standard integrality/Krein checks"
    res["detail"] = (f"eigenvalues k={k}, r={r}, s={s}; multiplicities"
                     f" f={f}, g={g}")
    return res


def main():
    print("# Ran: python3 code/out/check_srg33_12_1_6.py")
    print("# Oracle: exact integer/Fraction feasibility of srg(v,k,lam,mu) (no floats).")
    print("# Purpose: independent re-derivation that Makhnev Thm 2's forced subobject")
    print("#   (33,12,1,6) is parameter-INFEASIBLE, and that it stands in contrast to")
    print("#   the feasible/existing comparison sets below. NO assertion about v=99.")
    print()
    cases = [
        (33, 12, 1, 6, "Makhnev Thm 2 forced subobject (mu=6)"),
        (27, 10, 1, 5, "Makhnev Thm 1's unique non-mu<=3 exception (EXISTS)"),
        (9, 4, 1, 2, "rook(3) — exists"),
        (99, 14, 1, 2, "the target family member — status OPEN"),
        (243, 22, 1, 2, "BvLS — exists"),
        (33, 8, 1, 2, "known-inf next family member (integrality, consistency)"),
    ]
    hdr = (f"{'v':>5} {'k':>3} {'lam':>4} {'mu':>3} | {'verdict':>10} | "
           f"{'eig r,s':>8} | mult f,g | mechanism / detail")
    print(hdr)
    print("-" * len(hdr))
    results = {}
    for v, k, lam, mu, label in cases:
        res = srg_feasibility(v, k, lam, mu)
        results[(v, k, lam, mu)] = res
        if "g" in res:
            eig = f"{res['r']},{res['s']}"
            mult = f"{res['f']},{res['g']}"
        elif "r" in res:
            eig = f"{res['r']},{res['s']}"
            mult = "non-integral"
        else:
            eig = "-"
            mult = "-"
        print(f"{v:>5} {k:>3} {lam:>4} {mu:>3} | {res['verdict']:>10} | "
              f"{eig:>8} | {mult:>8} | {res['detail']}")
    print()
    print("# VERDICT for (33,12,1,6):")
    r = results[(33, 12, 1, 6)]
    print(f"  srg(33,12,1,6) is {r['verdict']} by {r['mechanism']}.")
    print("  Mechanism: ", r["detail"])
    print("  This is the exact sub-parameter-set Makhnev Thm 2 forces under")
    print("  condition (*) at (99,14,1,2); Thm 1 then rejects it because mu=6>3")
    print("  and it is not (27,10,1,5). The contrast row (27,10,1,5) is FEASIBLE")
    print("  and EXISTS, which is why Thm 1's exception escapes the mechanism.")
    print()
    print("# Consistency: the known-inf feasible (33,8,1,2) must also report")
    print("#   INFEASIBLE by multiplicity integrality (same 2k-(v-1) divisibility")
    print("#   mechanism as (33,12,1,6)).")
    r33 = results[(33, 8, 1, 2)]
    print(f"  srg(33,8,1,2): {r33['verdict']} by {r33['mechanism']}: {r33['detail']}")


if __name__ == "__main__":
    main()
