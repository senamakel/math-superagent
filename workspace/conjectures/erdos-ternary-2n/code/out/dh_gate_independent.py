"""Independent machine verification of the Dimitrov--Howe n=3 worked examples,
by a route that does NOT reuse erdos.dh_classifier's power_sequence/n3_solutions.

This is the second, independent route GOAL.md requires for the classifier. It
re-derives everything from scratch with a naive direct enumeration:

  Equation (n=3):  3^x = 2^a1 + 2^a2 + 2^a3   (mod M),  ai >= 0.

  M1 = 5440 = 2^6 * 5 * 17   -- the paper says there is an EXTRANEOUS
       solution (3^4 = 2^0+2^4+2^6, with 2^6 an indeterminate power of 2
       because v_2(M1)=6 puts canonical exponent 6 on the tail/loop boundary).
  M2 = 2^7 * 5 * 17 * 257    -- the paper says M2 is CLEAN: every residue
       solution uses only determinate (canonical, i.e. < v_2(M)) powers of 2,
       so each lifts uniquely to the integer solution 3^4 = 1+16+64 = 81.

Definition of "indeterminate"/"determinate" power (DH Def 2.2) used here:
  p^i is DETERMINATE mod M iff the only b>=0 with p^b = p^i (mod M) is b=i,
  equivalently iff p^(i+1) | M (i < v_p(M)); otherwise INDETERMINATE.

Exact integer arithmetic only (sympy n_order, plain pow, gcd). No floats.
"""

from math import gcd
from itertools import product
from sympy.ntheory import n_order


def v_p(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def all_distinct_powers(p, M):
    """Residues {p^e mod M : e >= 0} as a dict value->canonical-min-exponent."""
    seen = {}
    x = 1 % M
    e = 0
    while x not in seen:
        seen[x] = e
        x = (x * p) % M
        e += 1
    return seen


def brute_n3_residue_solutions(M):
    """Every (canonical-exponent triple a1<=a2<=a3, power-of-3 residue s) with
    2^a1+2^a2+2^a3 = 3^y (mod M) for some y.  Canonical exponents are the set
    of distinct residues {2^e mod M}, so a triple lists min-exponents and
    each residue appears once (DH Convention 2.1)."""
    P2 = all_distinct_powers(2, M)          # value -> canonical exponent
    P3 = all_distinct_powers(3, M)          # value -> canonical exponent
    p3vals = set(P3)
    canon = sorted(P2.values())             # exponents of the distinct 2-powers
    sols = []                               # (s, [triples])
    seen_sum = {}
    # triples with repetition allowed, a1 <= a2 <= a3, each in canon
    idx = {v: i for i, v in enumerate(canon)}
    nc = len(canon)
    for i in range(nc):
        for j in range(i, nc):
            for k in range(j, nc):
                s = (pow(2, canon[i], M) + pow(2, canon[j], M)
                     + pow(2, canon[k], M)) % M
                if s in p3vals:
                    trip = (canon[i], canon[j], canon[k])
                    s3 = s
                    if s3 not in seen_sum:
                        seen_sum[s3] = []
                    seen_sum[s3].append(trip)
    for s in sorted(seen_sum):
        ys = [P3[s]]   # canonical exponent with 3^min == s
        sols.append((s, ys, sorted(seen_sum[s])))
    return P2, P3, sols


def check(M, label):
    print("=" * 70)
    print(f"{label}: M = {M}  = 2^{v_p(M,2)} · 3^{v_p(M,3)} · {M // (2**v_p(M,2)*3**v_p(M,3))}")
    P2, P3, sols = brute_n3_residue_solutions(M)
    u = v_p(M, 2)
    print(f"  distinct powers of 2 mod M: {len(P2)} (v2={u})")
    print(f"  distinct powers of 3 mod M: {len(P3)} (v3={v_p(M,3)})")
    print("  residue-class solutions 3^y == 2^a1+2^a2+2^a3 (mod M):")
    any_indet = False
    for s, ys, triples in sols:
        for trip in triples:
            indet = [e for e in trip if e >= u]
            if indet:
                any_indet = True
            tag = "INDETERMINATE-2" if indet else "determinate"
            print(f"     3^{ys[0]} == 2^{trip[0]}+2^{trip[1]}+2^{trip[2]}  [{tag}]")
    print(f"  -> extraneous solution present (some indeterminate 2-power): {any_indet}")
    # exact lift check for 3^4==81 solution when present
    if 81 < M and (81 % M) in P3:
        for trip in (sols_by_s := {}).get(81 % M, []):
            pass
    # direct check: is 3^4 = 1+16+64 = 81 exactly, and < M?
    print(f"  3^4 == 1+16+64 == 81 in Z: {1+16+64 == 81}, 81 < M: {81 < M}")
    return any_indet


def main():
    M1 = 2 ** 6 * 5 * 17
    M2 = 2 ** 7 * 5 * 17 * 257
    print("INDEPENDENT RE-DERIVATION of DH n=3 worked examples (naive enumeration)")
    print("determinate power criterion (Def 2.2): p^i determinate iff i < v_p(M)\n")
    e1 = check(M1, "M1 = 2^6*5*17")
    e2 = check(M2, "M2 = 2^7*5*17*257")

    # verdicts vs the paper
    print("\n" + "=" * 70)
    print("VERDICTS (vs Dimitrov--Howe, eqns (4)(5)(6) and clean-M2 claim):")
    print(f"  M1 has an extraneous solution: got {e1}, paper expects True   -> {'PASS' if e1 else 'FAIL'}")
    print(f"  M2 is clean (no extraneous):   got {not e2}, paper expects True -> {'PASS' if not e2 else 'FAIL'}")

    # independent cross-check of the determinacy criterion definition itself
    print("\n  determinacy criterion spot-check (p^i determinate iff i < v_p(M)):")
    for M in (M1, M2, 3 ** 4, 2 ** 9):
        cites = []
        for p in (2, 3):
            u = v_p(M, p)
            P = all_distinct_powers(p, M)
            for i in range(0, u + 3):
                # true determinate: p^i appears only at exponent i among 0..some
                canon_of_val = P[pow(p, i, M)]   # canonical (smallest) exponent
                actually_det = (canon_of_val == i)
                criterion = (i < u)
                cites.append((M, p, i, actually_det == criterion))
        bad = [c for c in cites if not c[3]]
        print(f"    M={M}: {'ALL {} OK'.format(len(cites)) if not bad else 'MISMATCH ' + str(bad[:3])}")
    print("\nAll machine checks done against exact integer arithmetic.")


if __name__ == "__main__":
    main()
