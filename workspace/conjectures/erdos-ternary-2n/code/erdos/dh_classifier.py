"""Determinacy classifier for the Dimitrov--Howe / Bertok--Hajdu cross-modulus method.

Importable as ``erdos.dh_classifier`` (module ``code/erdos/dh_classifier.py``).
All arithmetic is exact integer arithmetic (``sympy.ntheory.n_order`` and
plain modular exponentiation); nothing here is floating point.

Background (Dimitrov--Howe 2021, arXiv:2105.06440v4, "Powers of 3 with few
nonzero bits and a conjecture of Erdos"; Rocky Mountain J. Math.):

  Write M = 2^u * 3^v * M'  with M' coprime to 6 (u = v_2(M), v = v_3(M)).
  Notation 2.3 defines
      O2 (M) = order of 2 in (Z/3^v M' Z)^x
      O2'(M) = order of 2 in (Z/M' Z)^x
      O3 (M) = order of 3 in (Z/2^u M' Z)^x
      O3'(M) = order of 3 in (Z/M' Z)^x

  Determinate power (Def 2.2 and the tail-of-diagram argument): p^i is a
  DETERMINATE power of p mod M iff M is divisible by p^(i+1), i.e. iff
  i < v_p(M). The multiplication-by-p diagram has v_p(M) tail elements and
  O_p(M) loop elements, hence v_p(M)+O_p(M) distinct powers of p mod M.

  Lemma 3.1: let x > 2, y > 0, c be integers with 3^y == c + 2^x (mod M).
  If O3'(M) is NOT divisible by 2^(x-1) AND O2'(M) is NOT divisible by 3^y,
  then there exist x' >= 0, y' >= 0 with
      (a) 3^y' == c + 2^x' (mod M),
      (b) 2^x' an indeterminate power of 2 mod M, and
      (c) 3^y' an indeterminate power of 3 mod M.
  i.e. an "extraneous" solution exists: one involving an indeterminate power
  of 2 AND an indeterminate power of 3.

  Degenerate instance M = 3^k: M' = 1, so O2' = O3' = 1 (the units group of
  Z/Z is trivial). Both divisibility failures then always hold, so Lemma 3.1
  forces an extraneous solution for every datum; the pure-3-adic sieve
  |A_k| = 2^(k-1) (see erdos.oracle.sieve_count) can therefore never close.

The two worked n = 3 examples of the paper (falsification gate):

  M1 = 5440 = 2^6 * 5 * 17:  3^1 == 2^0+2^0+2^0, 3^2 == 2^0+2^2+2^2,
  3^4 == 2^0+2^4+2^6 mod M1;  14 distinct powers of 2, 16 of 3; 2^6 is on
  the 8-cycle loop (indeterminate: 6 >= v2 = 6) while 2^0, 2^2, 2^4 are
  determinate.

  M2 = 2^7 * 5 * 17 * 257: the same three congruences hold (2^0, 2^4, 2^6
  are then all determinate, 0,4,6 < v2 = 7), the lifts 2^0+2^4+2^14 and
  2^0+2^4+2^22 are NOT powers of 3 mod M2, and no solution uses an
  indeterminate power of 2: no extraneous solution.
"""

from sympy.ntheory import n_order


def v_p(n, p):
    """The p-adic valuation of n (largest e with p**e | n); n >= 1."""
    if n <= 0:
        raise ValueError("v_p requires n >= 1")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def decompose(M):
    """Return (u, v, M') with M = 2^u * 3^v * M', M' coprime to 6."""
    u = v_p(M, 2)
    v = v_p(M, 3)
    return u, v, M // (2 ** u * 3 ** v)


def _order_mod(a, m):
    """Multiplicative order of a mod m; 1 for the trivial ring m == 1."""
    return n_order(a, m) if m > 1 else 1


def orders(M):
    """Dict with O2, O2', O3, O3' and the decomposition (Notation 2.3)."""
    u, v, Mp = decompose(M)
    return {
        "O2": _order_mod(2, 3 ** v * Mp),
        "O2'": _order_mod(2, Mp),
        "O3": _order_mod(3, 2 ** u * Mp),
        "O3'": _order_mod(3, Mp),
        "u": u, "v": v, "M'": Mp,
    }


def power_sequence(p, M):
    """(vals, tail_len): vals[e] = p^e mod M for e = 0..(v_p(M)+O_p(M)-1).

    The first repeated value occurs at e = v_p(M) (the loop start), so
    vals is the whole tail-and-loop diagram: tail_len = v_p(M) elements on
    the tail and len(vals) - tail_len = O_p(M) elements on the loop.  The
    canonical exponent e is determinate iff e < tail_len.
    """
    seen = {}
    vals = []
    x = 1 % M
    e = 0
    while x not in seen:
        seen[x] = e
        vals.append(x)
        x = (x * p) % M
        e += 1
    return vals, seen[x]


def is_determinate(p, i, M):
    """Whether the power p^i (canonical exponent i) is determinate mod M.

    Equivalent to the paper's criterion v_p(M) >= i+1, i.e. i < v_p(M);
    checked against the actual diagram by the caller.
    """
    return i < v_p(M, p)


def n3_solutions(M):
    """Enumerate sums 2^a1+2^a2+2^a3 (a_i >= 0, not necessarily distinct;
    Convention 2.1: two sums are the same when their terms are congruent
    mod M; we take *canonical* exponents 0..per-1 so each power residue
    appears once, and report summands as sorted canonical exponents).

    Returns (pow2_vals, pow3_vals, solutions) where pow2_vals /
    pow3_vals are the power_sequence value lists and solutions is a list of
    (s, ys, triples): s a power-of-3 residue, ys the canonical exponents
    with 3^y == s, triples the sorted canonical-exponent 3-tuples summing
    to s.  Complexity O(per2^3) in the number of distinct powers of 2.
    """
    pow2_vals, _ = power_sequence(2, M)
    pow3_vals, _ = power_sequence(3, M)
    per2, per3 = len(pow2_vals), len(pow3_vals)
    p3_set = set(pow3_vals)
    by_sum = {}
    for a in range(per2):
        va = pow2_vals[a]
        for b in range(a, per2):
            vb = pow2_vals[b]
            sab = (va + vb) % M
            for ri in range(b, per2):
                s = (sab + pow2_vals[ri]) % M
                if s in p3_set:
                    by_sum.setdefault(s, set()).add((a, b, ri))
    sols = []
    for s in sorted(by_sum):
        ys = [y for y in range(per3) if pow3_vals[y] == s]
        sols.append((s, ys, sorted(by_sum[s])))
    return pow2_vals, pow3_vals, sols


def extraneous_residue_sets(M):
    """(loop2_vals, loop3_vals): residues of the INDETERMINATE powers.

    loop2_vals = {2^x' mod M : x' in [v_2(M), v_2(M)+O2(M))}, the loop of
    the powers-of-2 diagram; similarly for 3.  A solution 3^y' == c + 2^x'
    with both indeterminate exists iff (shifted loop2) meets loop3 for the
    given c, i.e. iff (c + a) mod M is in loop3 for some a in loop2.
    """
    o = orders(M)
    u, v = o["u"], o["v"]
    loop2 = {pow(2, xp, M) for xp in range(u, u + o["O2"])}
    loop3 = {pow(3, yp, M) for yp in range(v, v + o["O3"])}
    return loop2, loop3


def has_extraneous(M, c):
    """True iff some c' congruent to c mod M equals 3^y' - 2^x' with BOTH
    powers indeterminate, i.e. (c + loop2) meets loop3."""
    loop2, loop3 = extraneous_residue_sets(M)
    return any((c + a) % M in loop3 for a in loop2)


def lemma31_bruteforce(M_range, xrange=range(2, 7), yrange=range(1, 7)):
    """Verify Lemma 3.1 directly: for every M in M_range and every
    (x, y, c) with c == (3^y - 2^x) mod M (the c making the congruence
    hold), if O3'(M) is not divisible by 2^(x-1) and O2'(M) is not
    divisible by 3^y then an extraneous solution must exist.

    The lemma is stated for x > 2; the x <= 2 data are counted separately
    and never treated as violations.  Returns a dict of counts and any
    violations (hypothesis true, x > 2, no extraneous solution).
    """
    total = hyp_true = x2_hyp = 0
    violations = []
    for M in M_range:
        o = orders(M)
        for x in xrange:
            for y in yrange:
                c = (pow(3, y, M) - pow(2, x, M)) % M
                total += 1
                hyp = (o["O3'"] % (2 ** (x - 1)) != 0) and (
                    o["O2'"] % (3 ** y) != 0)
                if hyp:
                    hyp_true += 1
                    if x <= 2:
                        x2_hyp += 1
                    elif not has_extraneous(M, c):
                        violations.append((M, x, y, c))
    return {"total": total, "hypothesis_true": hyp_true,
            "x2_hyp": x2_hyp, "violations": violations}


def main():
    print("=" * 78)
    print("DH/Bertok-Hajdu cross-modulus determinacy classifier")
    print("exact integer arithmetic; orders via sympy n_order")
    print("=" * 78)

    MODULI = [(5440, "M1 = 2^6*5*17"),
              (2 ** 7 * 5 * 17 * 257, "M2 = 2^7*5*17*257"),
              (3 ** 4, "3^4"),
              (3 ** 6, "3^6")]

    # ---- Part 0: determinate-power claim vs the actual diagram ----
    print("\n[0] Determinate-power claim: p^i determinate iff v_p(M) >= i+1")
    print("    (verified against the tail-and-loop diagram: tail_len == v_p,")
    print("     loop_len == O_p, distinct powers == v_p + O_p)")
    for M, label in MODULI:
        o = orders(M)
        v2, t2 = power_sequence(2, M)
        v3, t3 = power_sequence(3, M)
        ok_diag = (t2 == o["u"] and len(v2) - t2 == o["O2"]
                   and t3 == o["v"] and len(v3) - t3 == o["O3"])
        ok_claim = all(is_determinate(p, i, M) == (v_p(M, p) >= i + 1)
                       for p in (2, 3) for i in range(len(v2) + 3))
        print(f"   M={M} ({label}): diagram tail/loop matches v_p/O_p: {ok_diag};"
              f"  determinacy criterion holds: {ok_claim}")

    # ---- Part 1: orders and power counts for the two worked moduli ----
    print("\n[1] Orders (Notation 2.3) for the two worked moduli:")
    for M, label in [(5440, "M1"), (2 ** 7 * 5 * 17 * 257, "M2")]:
        o = orders(M)
        v2, _ = power_sequence(2, M)
        v3, _ = power_sequence(3, M)
        print(f"   {label} = {M}:  u={o['u']} v={o['v']} M'={o['M'']}")
        print(f"      O2={o['O2']} O2'={o['O2'']} O3={o['O3']} O3'={o['O3'']}")
        print(f"      distinct powers of 2: {len(v2)}  (tail {o['u']} + loop {o['O2']})")
        print(f"      distinct powers of 3: {len(v3)}  (tail {o['v']} + loop {o['O3']})")

    # ---- Part 2: reproduce the worked n=3 examples (falsification gate) ----
    print("\n[2] Worked n=3 examples: 3^y == 2^a1+2^a2+2^a3 mod M")
    for M, label in [(5440, "M1"), (2 ** 7 * 5 * 17 * 257, "M2")]:
        o = orders(M)
        pow2_vals, pow3_vals, sols = n3_solutions(M)
        print(f"\n   {label} = {M}:  {len(pow2_vals)} distinct powers of 2,"
              f" {len(pow3_vals)} distinct powers of 3")
        expected = {1: [(0, 0, 0)], 2: [(0, 2, 2)], 4: [(0, 4, 6)]}
        for s, ys, triples in sols:
            det = []
            for t in triples:
                indet = [e for e in t if e >= o["u"]]
                det.append((t, indet))
            print(f"      3^y == {s} mod M (y in {ys})")
            for t, indet in det:
                d = "DETERMINATE" if not indet else \
                    f"indeterminate 2-exponents {indet}"
                print(f"         2^{t[0]} + 2^{t[1]} + 2^{t[2]}  ->  {d}")
        # M1: exactly the three solutions, and (0,4,6) with 2^6 indeterminate
        if label == "M1":
            got3 = {}
            for s, ys, triples in sols:
                for y in ys:
                    got3[y] = triples
            expected = {1: [(0, 0, 0)], 2: [(0, 2, 2)], 4: [(0, 4, 6)]}
            match = (set(got3) == set(expected)
                     and all(sorted(got3[y]) == expected[y] for y in expected))
            print(f"      ==> exactly the three solutions (4)(5)(6): {match}")
            print(f"          exponents 0,2,4 are determinate (< v2={o['u']}):"
                  f" {all(e < o['u'] for e in (0, 2, 4))}")
            print(f"          2^6 is indeterminate (6 >= v2={o['u']}):"
                  f" {6 >= o['u']}")
        if label == "M2":
            # direct check of the paper's lift claim
            check = []
            for e in (6, 6 + o["O2"], 6 + 2 * o["O2"]):
                val = (pow(2, 0, M) + pow(2, 4, M) + pow(2, e, M)) % M
                is_pow3 = val in set(pow3_vals)
                check.append((e, is_pow3))
            print("      lifts 2^0+2^4+2^e of the M1 solution (e = 6, 6+16,"
                  " 6+32):")
            for e, p3 in check:
                print(f"         e={e}: is_pow3 mod M2 = {p3}")
            all_det = all(all(e < o["u"] for e in t)
                          for _, _, triples in sols for t in triples)
            print(f"      all summands of all {label} solutions are determinate"
                  f" (exponents < v2={o['u']}): {all_det}")
            print(f"      3^4 == 2^0+2^4+2^6 mod M2 holds:"
                  f" {(1 + 16 + 64) % M == 3 ** 4 % M}")
            # no extraneous solution: c of the 3^4 solution has no
            # indeterminate 2-power + indeterminate 3-power representation
            extraneous = has_extraneous(M, (pow(3, 4, M) - pow(2, 6, M)) % M)
            print(f"      extraneous solution for the (x=6,y=4) datum:"
                  f" {extraneous}")

    # ---- Part 3: Lemma 3.1 brute-force verification ----
    print("\n[3] Lemma 3.1 direct brute-force verification")
    small_M = list(range(2, 1000))
    res = lemma31_bruteforce(small_M)
    print(f"   M in [2, {small_M[-1]}]  ({len(small_M)} moduli),"
          f" x=2..6, y=1..6, c = (3^y - 2^x) mod M")
    print(f"   cases tested: {res['total']}")
    print(f"   hypothesis true: {res['hypothesis_true']}"
          f"  (of which x<=2 outside lemma scope: {res['x2_hyp']})")
    print(f"   VIOLATIONS (x>2, hypothesis true, no extraneous solution):"
          f" {len(res['violations'])}")
    for v in res["violations"][:10]:
        print("      ", v)

    # ---- Part 4: degenerate M = 3^k ----
    print("\n[4] Degenerate instance M = 3^k  (M' = 1 => O2' = O3' = 1):")
    for k in range(1, 7):
        o = orders(3 ** k)
        print(f"   M = 3^{k}:  M'={o['M'']}, O2'={o['O2'']}, O3'={o['O3'']}")
    print("   Since M'=1, both 2^(x-1) | O3' and 3^y | O2' fail for every")
    print("   x>=2, y>=1, so Lemma 3.1 forces an extraneous solution for")
    print("   every datum: the pure-3-adic sieve |A_k|=2^(k-1) never closes.")

    print("\nDONE.")


if __name__ == "__main__":
    main()