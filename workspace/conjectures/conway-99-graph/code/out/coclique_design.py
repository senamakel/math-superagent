#!/usr/bin/env python3
"""Coclique-design line for the open problem srg(99,14,1,2).

Three tasks, exact integer / sympy rational arithmetic only. No search.

TASK A — Prove algebraically the tight-Hoffman-bound structure at (99,14,1,2):
  eigenvalues k=14, r=3, s=-4, coclique bound alpha = v*(-s)/(k-s) = 22.
  If a 22-coclique C existed, equality in the ratio bound forces
  f = 1_C - (alpha/v)*1 into the s=-4 eigenspace (Af = s f). For an outside
  vertex x the EIGENVALUE EQUATION then forces d_C(x) = number of neighbours
  of x inside C = alpha*(k-s)/v = 4. That is a provable identity, not a
  search. Then every pair in C has exactly mu=2 common neighbours (C is a
  coclique so all its pairs are non-adjacent; srg gives mu=2 common
  neighbours, both outside C), so the outside neighbourhoods cut down to C
  give the blocks of a 2-(22,4,2) design (b=77, r=14, lambda=2). Verify the
  parameter identities exactly.

TASK B — Controls: does the same equality-force hold at rook(3) and bvls?
  rook(3): alpha=3, k=4, v=9, s=-2  -> forced d_C = 3*6/9 = 2.
  bvls   : alpha=45, k=22, v=243, s=-5 -> forced d_C = 45*27/243 = 5,
           giving a 2-(45,5,2) design (b=198, r=22).
  Verify by exact adjacency that rook(3) really has a 3-coclique and that
  every outside vertex has exactly 2 neighbours inside it (matching the forced
  value). For bvls report the forced formula/design (actual alpha not
  established <= 45; report a greedy lower bound).

TASK C — Does a 2-(22,4,2) design exist / is it arithmetically excluded?
  b=77, r=14, lambda=2, v=22, k=4. All standard necessary arithmetic passes
  (Fisher b>=v, integers); the symmetric Bruck-Ryser-Chowla condition does
  NOT apply because b=77 != v=22. The determinant/Gram condition
  det(N^T N) = (r-lambda)^{v-1} * (b k) = 12^21 * 308 is automatically a sum
  of v squares by Cauchy-Binet (trivially satisfiable by Lagrange), so no
  arithmetic exclusion. Report the verdict.
"""
import itertools
from sympy import Rational, binomial, sqrt, symbols, simplify, Integer
from sympy.ntheory.factor_ import factorint

from lib.srg import rook, bvls_graph, is_srg

# ---------------------------------------------------------------------------
# Task A: symbolic derivation at (99,14,1,2)
# ---------------------------------------------------------------------------

def task_a():
    print("=" * 72)
    print("TASK A - tight-Hoffman-bound structure at srg(99,14,1,2), symbolic")
    v, k, lam, mu, r, s, alpha = (99, 14, 1, 2, 3, -4, Rational(22, 1))

    # 1. Hoffman ratio bound value
    bound = Rational(v * (-s), k - s)
    print(f"1) Hoffman coclique bound  alpha <= v*(-s)/(k-s)"
          f" = {v}*{(-s)}/{k - s} = {bound}  (integer {int(bound)})")

    # 2. Equality force -> f in the s=-4 eigenspace
    print("\n2) If a coclique C with |C| = alpha = 22 existed, equality in the "
          "ratio bound\n   forces f = 1_C - (alpha/v)*1 into the s=-4 eigenspace, "
          "i.e. A f = s f.")
    # For x inside C:  f_x = 1 - alpha/v
    # For x outside C: f_x = -alpha/v
    fx_out = -Rational(alpha, v)
    print(f"   f_x for x outside C = -alpha/v = -{alpha}/{v} = {fx_out}")
    print(f"   expected (A f)_x = s*f_x = ({s})*({fx_out}) = {s*fx_out}")

    # 3. LHS for x outside C: neighbours in C give f=+1, other k-d_C neighbours
    #    give -alpha/v.  (A f)_x = d_C + (k - d_C)*(-alpha/v)
    #                              = d_C - (alpha/v)*k   (alpha/v * d_C cancels)
    dC = symbols('d_C')
    # (A f)_x = d_C*(1-alpha/v) + (k-d_C)*(-alpha/v)
    #         = d_C - d_C*alpha/v - k*alpha/v + d_C*alpha/v
    #         = d_C - (alpha/v)*k   (the d_C*alpha/v terms cancel)
    lhs = dC * (1 - Rational(alpha, v)) + (k - dC) * (-Rational(alpha, v))
    lhs = simplify(lhs)
    print(f"\n3) For x outside C, (A f)_x = d_C*(1-alpha/v) + (k-d_C)*(-alpha/v)"
          f" = {lhs}   [the d_C*alpha/v terms cancel, leaving d_C - alpha*k/v]")
    print(f"   with numbers: d_C*(1-{Rational(alpha,v)}) + ({k}-d_C)*(-{Rational(alpha,v)})"
          f" = d_C - {Rational(alpha*k,v)}"
          f" = (9*d_C - 28)/9  [since alpha*k/v = {alpha}*{k}/{v} = {Rational(alpha*k,v)}]")

    # 4. set LHS == expected
    sol = Rational(alpha * (k - s), v)  # closed form
    print(f"\n4) Eigenvalue equation (A f)_x = s*f_x at x outside:")
    print(f"   d_C - {Rational(alpha*k,v)} = {s*fx_out}")
    eq_lhs = Rational(9)  # 9 d_C - 28 = 8
    print(f"   => 9*d_C - 28 = {9*s*fx_out}  =>  9*d_C = 36  =>  d_C = 4 (exact)")
    print(f"   CLOSED FORM  d_C = alpha*(k-s)/v = {alpha}*({k}-({s}))/{v}"
          f" = {alpha*(k-s)}/{v} = {sol}")
    assert sol == 4, "d_C closed form should be exactly 4"

    # 5. design claim
    print("\n5) Every pair in C has exactly mu = 2 common neighbours")
    print("   (C is a coclique, so every two of its vertices are non-adjacent;")
    print("   srg mu=2 gives exactly 2 common neighbours for each non-adjacent pair,")
    print("   and those common neighbours lie OUTSIDE C since no vertex of C is")
    print("   adjacent to any other vertex of C).")
    print("   => the neighbourhoods (N(x) intersect C) for x outside C are the")
    print("      blocks of a design with:")
    v_d, k_d, la_d = 22, 4, 2
    b_d = v - alpha          # one block per outside vertex
    r_d = la_d * (v_d - 1) // (k_d - 1)
    print(f"      points v' = alpha = {v_d}, block size k' = d_C = {k_d},"
          f" lambda' = mu = {la_d}")
    print(f"      blocks b = v - alpha = {v} - {alpha} = {b_d},"
          f"  replication r = lambda'*(v'-1)/(k'-1) = {la_d}*{v_d-1}/{k_d-1} = {r_d}")
    print("   i.e. a 2-(22,4,2) design.")
    c1 = b_d * binomial(k_d, 2)
    c2 = la_d * binomial(v_d, 2)
    c3 = b_d * k_d
    c4 = v_d * r_d
    c5 = r_d
    c6 = la_d * (v_d - 1) // (k_d - 1)
    print(f"\n6) Parameter identities (exact):")
    print(f"   b*C(k,2) = {b_d}*{binomial(k_d,2)} = {c1}")
    print(f"   lambda*C(v,2) = {la_d}*{binomial(v_d,2)} = {c2}")
    print(f"   match: {c1 == c2}")
    print(f"   b*k = {b_d}*{k_d} = {c3};  v*r = {v_d}*{r_d} = {c4};  match: {c3 == c4}")
    print(f"   r = lambda*(v-1)/(k-1) = {la_d}*{v_d-1}/{k_d-1} = {c5};  r = {r_d}: {c5 == c6}")
    assert c1 == c2 and c3 == c4 and c5 == c6


# ---------------------------------------------------------------------------
# Task B: controls
# ---------------------------------------------------------------------------

def max_coclique_rook():
    """Exhaustive (tiny, 2^9) max coclique of rook(3). Returns (size, [cocliques])."""
    A = rook(3)
    best = -1
    bests = []
    for mask in range(1 << 9):
        S = [i for i in range(9) if (mask >> i) & 1]
        ok = True
        for a, b in itertools.combinations(S, 2):
            if A[a, b]:
                ok = False
                break
        if ok and len(S) > best:
            best = len(S)
            bests = [S]
        elif ok and len(S) == best:
            bests.append(S)
    return best, bests


def outside_degrees(A, C):
    v = A.shape[0]
    Cset = set(C)
    return [sum(1 for c in C if A[x, c]) for x in range(v) if x not in Cset]


def task_b():
    print("\n" + "=" * 72)
    print("TASK B - equality-force at the controls (refuted-on-arrival or 99-specific?)")

    # ---- rook(3) : alpha=3, k=4, v=9, s=-2
    v, k, s, alpha = 9, 4, -2, 3
    forced = Rational(alpha * (k - s), v)
    print(f"\nB1) rook(3) srg(9,4,1,2): alpha={alpha}, k={k}, v={v}, s={s}")
    print(f"    forced outside-degree into a max coclique = alpha*(k-s)/v"
          f" = {alpha}*{k-s}/{v} = {forced}")
    print(f"    [NB: this is the correct closed form; alpha*k/v = {Rational(alpha*k,v)}"
          f" is NOT the equality-force value]")
    A = rook(3)
    sz, cs = max_coclique_rook()
    print(f"    ACTUAL alpha(rook(3)) = {sz}  (exhaustive, {len(cs)} max cocliques)")
    good = all(set(od) == {int(forced)} for od in (outside_degrees(A, C) for C in cs))
    exact = sorted(set(tuple(sorted(outside_degrees(A, C))) for C in cs))
    print(f"    outside-degree multisets over all max cocliques: {exact}")
    print(f"    every outside vertex has degree-into-C = forced value {int(forced)}"
          f" over every 3-coclique: {good}")
    # each max coclique has v-alpha = 6 outside vertices, each with the forced degree
    match = set(exact) == {(int(forced),) * (v - alpha)}
    print(f"    forced value MATCHES actual (each of the {v-alpha} outside vertex"
          f" degrees equals {int(forced)}): {match}")
    # design at rook: 2-(3,2,2), b=6, r=4
    v_d, k_d, la_d, b_d = 3, 2, 2, v - alpha
    r_d = la_d * (v_d - 1) // (k_d - 1)
    print(f"    rook(3) design analogy: 2-({v_d},{k_d},{la_d}), b={b_d}, r={r_d}")
    print(f"      b*C(k,2)={b_d*binomial(k_d,2)}  lambda*C(v,2)={la_d*binomial(v_d,2)}"
          f" match:{b_d*binomial(k_d,2)==la_d*binomial(v_d,2)};  "
          f" b*k={b_d*k_d} v*r={v_d*r_d} match:{b_d*k_d==v_d*r_d}")

    # ---- bvls : alpha=45, k=22, v=243, s=-5
    v, k, s, alpha = 243, 22, -5, 45
    forced = Rational(alpha * (k - s), v)
    print(f"\nB2) bvls_graph() srg(243,22,1,2): alpha={alpha}, k={k}, v={v}, s={s}")
    print(f"    forced outside-degree into a 45-coclique = alpha*(k-s)/v"
          f" = {alpha}*{k-s}/{v} = {forced}  (= 5, integer)")
    v_d, k_d, la_d = 45, 5, 2
    b_d = v - alpha
    r_d = la_d * (v_d - 1) // (k_d - 1)
    print(f"    (if such a coclique existed) design: 2-({v_d},{k_d},{la_d}),"
          f" b={b_d}, r={r_d}")
    print(f"      b*C(k,2)={b_d*binomial(k_d,2)}  lambda*C(v,2)={la_d*binomial(v_d,2)}"
          f" match:{b_d*binomial(k_d,2)==la_d*binomial(v_d,2)};  "
          f" b*k={b_d*k_d} v*r={v_d*r_d} match:{b_d*k_d==v_d*r_d}")

    # greedy lower bound on alpha(bvls) — clearly labeled as a bound, not exact
    B = bvls_graph()
    n = B.shape[0]
    # greedy: repeatedly pick a vertex, delete it and its neighbours
    import random
    random.seed(1)
    adj = [set(int(j) for j in range(n) if B[i, j]) for i in range(n)]
    best = 0
    for _ in range(50):
        remaining = set(range(n))
        S = []
        while remaining:
            x = random.choice(tuple(remaining))
            S.append(x)
            remaining -= adj[x]
            remaining.discard(x)
        best = max(best, len(S))
    print(f"    greedy lower bound on alpha(bvls) >= {best} (bound only, not exact;"
          f" exact alpha <= 45 is open here). This does not assert a 45-coclique.")


# ---------------------------------------------------------------------------
# Task C: 2-(22,4,2) existence / arithmetic exclusion
# ---------------------------------------------------------------------------

def task_c():
    print("\n" + "=" * 72)
    print("TASK C - does a 2-(22,4,2) design exist? arithmetic necessary conditions")
    v, k, lam, b, r = 22, 4, 2, 77, 14
    n = r - lam
    print(f"params: v={v}, k={k}, lambda={lam}, b={b}, r={r}")
    print(f"1) integers: b={b}, r={r} both positive integers: {b>0 and r>0}")
    print(f"2) Fisher's inequality b >= v : {b} >= {v} : {b >= v}")
    print(f"   twin identity b*k = v*r : {b}*{k}={b*k} vs {v}*{r}={v*r}: {b*k==v*r}")
    print(f"   pair count b*C(k,2)=lambda*C(v,2): {b*binomial(k,2)} vs "
          f"{lam*binomial(v,2)}: {b*binomial(k,2)==lam*binomial(v,2)}")
    print(f"   replication r=lambda*(v-1)/(k-1): {lam*(v-1)}/{k-1} = {lam*(v-1)//(k-1)}"
          f" == r: {lam*(v-1)//(k-1)==r}")

    print(f"\n3) Bruck-Ryser-Chowla (symmetric-design theorem): needs b == v.")
    print(f"   Here b={b} != v={v}={22}, so the design is NOT symmetric and BRC's")
    print(f"   symmetric form does NOT apply. (If it did, with v even, n=r-lambda={n}")
    print(f"   would need to be a square; {n} is a non-square {n==int(sqrt(n))**2},")
    print(f"   but that exclusion is inapplicable at an asymmetric 2-design.)")

    print(f"\n4) Incidence-matrix Gram/determinant necessary condition (always applies):")
    print(f"   N^T N = (r-lambda)I + lambda J  =>  det(N^T N) = (r-lambda)^(v-1) * (b*k)")
    print(f"     = {n}^{v-1} * {b*k}")
    det = n ** (v - 1) * (b * k)
    fac = factorint(det)
    print(f"     factorised = {' * '.join(f'{p}^{e}' for p, e in fac.items())}")
    print(f"     det = {det}")
    # squarefree part (product of primes with odd exponent)
    sf = 1
    for p, e in fac.items():
        if e % 2 == 1:
            sf *= int(p)
    print(f"     squarefree part = {sf}")
    print(f"   By Cauchy-Binet, det(N^T N) must be a sum of {v} squares of integers")
    print(f"   (sum of v x v minor squares). This is TRIVIALLY satisfiable: by")
    print(f"   Lagrange every positive integer is a sum of (at most) 4 squares, and")
    print(f"   any sum of 4 can be padded to {v} squares with zeros. So this")
    print(f"   condition imposes no obstruction here (squarefree part {sf} is")
    print(f"   trivially a sum of {v}>=4 squares).")

    print(f"\n5) VERDICT: 2-(22,4,2) is NOT arithmetically excluded.")
    print(f"   All standard necessary conditions (integers, Fisher, the three")
    print(f"   parameter identities, the Gram/determinant sum-of-squares condition)")
    print(f"   are satisfied. The symmetric-form BRC does not apply (b != v).")
    print(f"   Existence is a construction/existence question the arithmetic does")
    print(f"   not rule out; the 2-(22,4,2) parameters are feasible.")


def main():
    import time
    t0 = time.time()
    print("what ran: code/out/coclique_design.py")
    print("oracle function: from lib.srg import rook, bvls_graph, is_srg")
    print("search space: none for the derivations; only tiny/exhaustive rook(3)"
          " (9 vtx) and a greedy bvls lower bound")
    # sanity: confirm the controls really are the claimed srgs
    print("\n[sanity] is_srg(rook(3), 9,4,1,2):", is_srg(rook(3), 9, 4, 1, 2))
    print("[sanity] is_srg(bvls_graph(), 243,22,1,2):", is_srg(bvls_graph(), 243, 22, 1, 2))
    task_a()
    task_b()
    task_c()
    print("\n" + "=" * 72)
    print(f"wall clock: {time.time() - t0:.2f} s")
    print("ALL CHECKS DONE")


if __name__ == "__main__":
    main()
