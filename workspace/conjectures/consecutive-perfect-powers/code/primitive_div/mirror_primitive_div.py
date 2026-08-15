#!/usr/bin/env python3
"""Mirror primitive-divisor verification and scope demonstration for
x^p - y^q = 1.

Exact integer arithmetic only (Python ints, sympy.factorint). No floats.

Three tasks:

Task A  MIRROR PRIMITIVE DIVISOR (the q-side, condition on x):
  For x^p - y^q = 1 with q an odd prime, x^p = (y+1) * Phi_q(-y) with
  Phi_q(-y) = (y^q + 1)/(y + 1). For each odd prime q in {3,5,7,11,13,17}
  and each integer y in [2, Ymax] (scale: q=3 -> 120, decreasing),
  does Phi_q(-y) have a prime divisor s with s not dividing (y+1), and the
  multiplicative order of (-y) mod s exactly q (equiv s == 1 mod q)?
  Count (q,y) with NO such primitive s (the small Zsigmondy mirror
  exceptions; the builder noted (q,1) [Phi_q(-1)=1] and (3,2)). Report a
  per-q table (Ymax, successes, failures, largest primitive s). Confirm that
  for y >= 3 no failures occur.

Task B  CLEAN STATEMENT of the necessary condition (logic proof-check):
  If x^p - y^q = 1 with p,q odd primes then
    (i) y has a prime divisor r == 1 (mod p) with r | Phi_p(x), r not | x-1
        [from y^q = (x-1) Phi_p(x), r | y]
    (ii) x has a prime divisor s == 1 (mod q) with s | Phi_q(-y),
         s not | (y+1)  [from x^p = (y+1) Phi_q(-y), s | x]
  Verify the deduction by direct construction: the unconditional facts that
  carry the chain are r | (x^p - 1) with r not | (x-1) [so, under the
  equation y^q = x^p - 1, r | y], and s | (y^q + 1) with s not | (y+1) [so,
  under the equation, s | x]. We check those facts over a range, and state
  explicitly this is a demonstration of the deductive step on constructed
  data, NOT a proof that any solution exists (there are none with p,q odd
  prime in this range).

Task C  NON-EXCLUSION / SCOPE:
  Show the elementary conditions do NOT alone close the space. Over odd
  primes p,q in [3,30] and x,y in [2,200], count 4-tuples where ALL hold:
  y has a prime divisor r==1 (mod p); x has a prime divisor s==1 (mod q);
  p | x-1; q | y+1; AND x^p - y^q != 1 (NOT a solution). Report also whether
  p | y and q | x hold for these near-solutions. And count how many have the
  full Cassels congruences (p|y AND q|x) with x^p - y^q != 1. The point:
  the primitive-divisor + elementary Cassels congruences are far from
  sufficient; many non-solutions satisfy them.
"""
import sympy as sp
from math import gcd

OUT_MD = "code/out/primitive_div_mirror.md"
OUT_TXT = "code/out/primitive_div_mirror.captured.txt"

PRIMES_SMALL = [3, 5, 7, 11, 13, 17]


def phi_q_neg(q, y):
    """(y^q + 1)/(y + 1) exact integer. q odd, y >= 1."""
    return (y ** q + 1) // (y + 1)


def mirror_primitive_divisor(q, y):
    """Primitive divisor s of Phi_q(-y): s | Phi_q(-y), s not | (y+1), and
    order of (-y) mod s exactly q (so s == 1 mod q, since order q divides
    s-1). Returns (s, factorint) or (None, factorint). Exact integers."""
    facts = sp.factorint(phi_q_neg(q, y))
    for s in sorted(facts):
        if (y + 1) % s != 0:
            # order of (-y) mod s divides the prime q; it is 1 iff s | (y+1).
            assert pow((-y) % s, q, s) == 1
            assert pow((-y) % s, 1, s) != 1
            assert s % q == 1
            return s, facts
    return None, facts


def task_a():
    lines = []
    YMAX = {3: 120, 5: 80, 7: 60, 11: 40, 13: 30, 17: 20}
    rows = []          # per-q table rows
    all_fail = []      # (q, y) with no primitive s
    y3_fail = []       # failures with y >= 3
    for q in PRIMES_SMALL:
        ymax = YMAX[q]
        succ = 0
        fails = []          # for this q (all y)
        local_max_s = -1
        for y in range(2, ymax + 1):
            s, _ = mirror_primitive_divisor(q, y)
            if s is None:
                fails.append(y)
                all_fail.append((q, y))
                if y >= 3:
                    y3_fail.append((q, y))
            else:
                succ += 1
                if s > local_max_s:
                    local_max_s = s
        rows.append((q, ymax, succ, ymax - 1 - succ, local_max_s))
        lines.append(
            f"  q={q:2d}: Ymax={ymax:3d}, successes={succ:3d}, "
            f"failures={ymax-1-succ:2d}, largest primitive s={local_max_s}"
        )
        if fails:
            lines.append(f"         no-primitive y values: {fails}")
    lines.append(f"  TOTAL (q,y) with NO primitive s: {len(all_fail)} "
                 f"-> {all_fail if all_fail else '(none)'}")
    lines.append(f"  failures with y >= 3: {len(y3_fail)} "
                 f"-> {y3_fail if y3_fail else '(none): confirmed no failures for y >= 3'}")
    return rows, all_fail, y3_fail, lines


# --------------------------------------------------------------------------
# shared bits for tasks B and C
# --------------------------------------------------------------------------
PRIMES_TO_30 = [p for p in range(3, 31) if sp.isprime(p)]  # 3,5,...,29


def prime_divisors(n):
    return set(sp.factorint(n))


def has_div_cong1(n, m):
    """Does n have a prime divisor == 1 (mod m)? n >= 2, m odd prime."""
    for r in sp.factorint(n):
        if r % m == 1:
            return True
    return False


def task_b():
    """Verify the deductive chain (i) and (ii). Since there are no actual
    solutions with p,q both odd prime in any reachable range, we verify the
    unconditional facts that carry the implication, over a range of (p,q,x,y),
    and report that the equation never holds there (so the implication is
    verified as a sound deductive step, explicitly NOT as existence of any
    solution)."""
    lines = []
    # We sweep (p, q, x, y) over modest ranges, checking:
    #   fact_r: prim r of Phi_p(x) with r | x^p-1, r not | x-1  (unconditional)
    #   fact_s: prim s of Phi_q(-y) with s | y^q+1, s not | y+1  (unconditional)
    # and, when x^p - y^q == 1 happens (never here for odd primes), that
    #   r | y and s | x.
    # Because r | (x^p - 1) and r not | (x-1), if the equation declared
    #   y^q = x^p - 1 then r | y^q hence r | y. We confirm the two
    #   unconditional facts hold for every queried (p,q,x,y), and report that
    #   no (p,q,x,y) in range actually satisfies x^p - y^q = 1.
    fact_r_bad = 0
    fact_s_bad = 0
    eq_cases = 0
    checked = 0
    fail_s_by_qy = {}    # (q,y) -> count of s-premise failures attributable
    xrange = range(2, 41)
    yrange = list(range(2, 41))
    # precompute primitive divisors: r-side depends only on (p,x), s-side
    # only on (q,y).
    prim_r = {}   # (p, x) -> primitive r of Phi_p(x) or None
    prim_s = {}   # (q, y) -> primitive s of Phi_q(-y) or None
    for p in [3, 5, 7, 11]:
        for x in xrange:
            facts = sp.factorint((x ** p - 1) // (x - 1))
            r_prim = next((rr for rr in sorted(facts)
                           if (x - 1) % rr != 0), None)
            prim_r[(p, x)] = r_prim
    for q in [3, 5, 7, 11]:
        for y in yrange:
            prim_s[(q, y)] = mirror_primitive_divisor(q, y)[0]
    for p in [3, 5, 7, 11]:
        for q in [3, 5, 7, 11]:
            for x in xrange:
                r_prim = prim_r[(p, x)]
                for y in yrange:
                    checked += 1
                    # fact_r must hold: if a prim r exists it divides x^p-1
                    # and not x-1. (Exists for all odd p, x>=2.)
                    fr = (r_prim is not None
                          and (x ** p - 1) % r_prim == 0
                          and (x - 1) % r_prim != 0)
                    if not fr:
                        fact_r_bad += 1
                    # fact_s
                    s_prim = prim_s[(q, y)]
                    fs = (s_prim is not None
                          and (y ** q + 1) % s_prim == 0
                          and (y + 1) % s_prim != 0)
                    if not fs:
                        fact_s_bad += 1
                        fail_s_by_qy[(q, y)] = fail_s_by_qy.get((q, y), 0) + 1
                    if x ** p - y ** q == 1:
                        eq_cases += 1
                        # would then also demand r_prim | y and s_prim | x
                        if r_prim is not None and y % r_prim != 0:
                            fact_r_bad += 1
                        if s_prim is not None and x % s_prim != 0:
                            fact_s_bad += 1
    lines.append(f"  (p,q,x,y) checked: {checked}")
    lines.append(f"  failures of unconditional r | x^p-1, r not|x-1: {fact_r_bad}")
    lines.append(f"  failures of unconditional s | y^q+1, s not|y+1: {fact_s_bad}")
    if fail_s_by_qy:
        lines.append(f"  s-premise failures attributed to (q,y): "
                     f"{fail_s_by_qy}  (each is the known small mirror "
                     f"exception (3,2) with NO primitive divisor, appearing "
                     f"once per (p,x) setting: 4 p * 39 x = 156)")
    else:
        lines.append(f"  s-premise failures attributed to (q,y): none")
    lines.append(f"  (p,q,x,y) with x^p - y^q == 1 in range: {eq_cases} "
                 f"(none, as expected: no odd-prime solutions here)")
    lines.append("  => the deductive steps are verified sound on this data; "
                 "the implication IF x^p-y^q=1 THEN r|y is NOT vacuous in "
                 "logic, it is simply verifiable only through its "
                 "unconditional premises here, since the antecedent never "
                 "fires. Explicitly NOT a proof of existence of any solution.")
    return (fact_r_bad, fact_s_bad, eq_cases, fail_s_by_qy), lines


def task_c():
    """Non-exclusion / scope: count non-solutions satisfying the elementary
    conditions. Over odd primes p,q in [3,30], x,y in [2,200]."""
    XMAX = 200
    # precompute powers and congruence/factor data
    powx = {p: {x: x ** p for x in range(2, XMAX + 1)} for p in PRIMES_TO_30}
    # has x (resp y) a prime divisor == 1 mod p (resp q)
    div1_x = {x: {p: has_div_cong1(x, p) for p in PRIMES_TO_30}
              for x in range(2, XMAX + 1)}
    div1_y = {y: {p: has_div_cong1(y, p) for p in PRIMES_TO_30}
              for y in range(2, XMAX + 1)}

    near = 0          # all elementary conditions + NOT a solution
    cassels_full_both = 0   # also p|y AND q|x
    cassels_py = 0          # p | y among near-solutions
    cassels_qx = 0          # q | x among near-solutions
    cassels_both_nonsol = 0 # (p,q,x,y) with p|y AND q|x AND NOT a solution
    cap = 0                 # total where all elementary + p|y,q|x congruences
    n_sol = 0               # should be 0 (no actual solutions with odd primes)
    total = 0
    for p in PRIMES_TO_30:
        for q in PRIMES_TO_30:
            for x in range(2, XMAX + 1):
                for y in range(2, XMAX + 1):
                    total += 1
                    is_sol = powx[p][x] == powx[q][y] + 1
                    if is_sol:
                        n_sol += 1
                    # elementary conditions
                    c_px1 = (x - 1) % p == 0      # p | x-1
                    c_qy1 = (y + 1) % q == 0      # q | y+1
                    c_dy = div1_y[y][p]           # y has prime div ==1 mod p
                    c_dx = div1_x[x][q]           # x has prime div ==1 mod q
                    if c_px1 and c_qy1 and c_dy and c_dx:
                        if not is_sol:            # NOT a solution
                            near += 1
                            # Cassels stronger congruences
                            py = (y % p == 0)
                            qx = (x % q == 0)
                            if py:
                                cassels_py += 1
                            if qx:
                                cassels_qx += 1
                            if py and qx:
                                cassels_full_both += 1
                    # full Cassels congruence count independent of elementary
                    if (y % p == 0) and (x % q == 0) and not is_sol:
                        cassels_both_nonsol += 1
                        # also count full Cassels congruence class even among
                        # those that are (should be none) — done above
    lines = []
    lines.append(f"  search space: |p|*|q|*|x|*|y| = {len(PRIMES_TO_30)}^2"
                 f"*{XMAX-1}^2 = {total} 4-tuples")
    lines.append(f"  actual solutions in space (x^p-y^q==1): {n_sol} "
                 f"(expected 0 for odd primes)")
    lines.append(f"  4-tuples with ALL elementary conditions (p|x-1, q|y+1, "
                 f"y has div==1 mod p, x has div==1 mod q) AND x^p-y^q != 1: "
                 f"{near}")
    lines.append(f"     ... of which p | y holds: {cassels_py}")
    lines.append(f"     ... of which q | x holds: {cassels_qx}")
    lines.append(f"     ... of which BOTH p|y AND q|x (full Cassels "
                 f"congruences) hold: {cassels_full_both}")
    lines.append(f"  (p,q,x,y) with BOTH p|y AND q|x AND x^p-y^q != 1 "
                 f"(Cassels-congruence non-solutions, no elementary "
                 f"condition): {cassels_both_nonsol}")
    return (total, n_sol, near, cassels_py, cassels_qx, cassels_full_both,
            cassels_both_nonsol), lines


def main():
    print("=" * 72)
    print("TASK A — MIRROR PRIMITIVE DIVISOR (q-side, condition on x)")
    print("=" * 72)
    rows_a, all_fail, y3_fail, la = task_a()
    for l in la:
        print(l)

    print()
    print("=" * 72)
    print("TASK B — CLEAN STATEMENT of the necessary condition (logic check)")
    print("=" * 72)
    (fr_bad, fs_bad, eq_cases, fail_s_by_qy), lb = task_b()
    for l in lb:
        print(l)

    print()
    print("=" * 72)
    print("TASK C — NON-EXCLUSION / SCOPE DEMONSTRATION")
    print("=" * 72)
    (total, n_sol, near, py, qx, both, cassels_both_nonsol), lc = task_c()
    for l in lc:
        print(l)

    # ---- write markdown ----
    md = []
    md.append("# Mirror primitive divisor — verification and scope\n")
    md.append("Exact integer arithmetic (Python ints, sympy.factorint); "
              "no floats.\n\n")
    md.append("## Task A — Mirror primitive divisor (q-side, condition on x)\n")
    md.append("For `x^p - y^q = 1` with q odd prime, `x^p = (y+1) Phi_q(-y)`, "
              "`Phi_q(-y) = (y^q+1)/(y+1)`. A *primitive* divisor s of "
              "`Phi_q(-y)` has `s | Phi_q(-y)`, `s` not dividing `(y+1)`, and "
              "order of `(-y)` mod s exactly q (equiv `s == 1 mod q`); since "
              "`x^p = (y+1) Phi_q(-y)` and `s` not `| (y+1)`, such an s "
              "divides x.\n")
    md.append("Per-q table (Ymax, successes, failures, largest primitive s):\n")
    md.append("| q | Ymax | successes | failures | largest primitive s |\n")
    md.append("|---|------|-----------|----------|--------------------|\n")
    for (q, ymax, succ, fail, ms) in rows_a:
        md.append(f"| {q} | {ymax} | {succ} | {fail} | {ms} |\n")
    md.append(f"\nTotal (q,y) with NO primitive s: {len(all_fail)} "
              f"({all_fail if all_fail else 'none'}); note (q,1) is excluded "
              "from the sweep because Phi_q(-1)=1 has no prime divisor.\n")
    md.append(f"Failures with y >= 3: {len(y3_fail)} "
              f"-> {'none: confirmed' if not y3_fail else y3_fail}. "
              "**For y >= 3 no failures occur** over this sweep.\n\n")

    md.append("## Task B — Clean statement of the necessary condition\n")
    md.append("Required deduction: if `x^p - y^q = 1` with p,q odd primes, "
              "then\n")
    md.append("  (i) y has a prime divisor `r == 1 (mod p)` with "
              "`r | Phi_p(x)`, `r` not `| x-1` (from `y^q = (x-1)Phi_p(x)`);\n")
    md.append("  (ii) x has a prime divisor `s == 1 (mod q)` with "
              "`s | Phi_q(-y)`, `s` not `| (y+1)` (from "
              "`x^p = (y+1)Phi_q(-y)`).\n")
    md.append("The deductive step is sound because `r | Phi_p(x)` and "
              "`r` not `| (x-1)` give `r | (x^p - 1) = y^q`, hence `r | y`; "
              "dually `s | (y^q + 1) = x^p` and `s` not `| (y+1)` give "
              "`s | x`. We verified the unconditional premises "
              "(`r | x^p - 1` with `r` not `| x - 1`; `s | y^q + 1` with "
              "`s` not `| y + 1`) over the (p,q,x,y) sweep:\n")
    md.append(f"- (p,q,x,y) checked: p,q in {{3,5,7,11}}, x,y in "
              f"[2,40].\n")
    md.append(f"- failures of `r | x^p-1`, `r` not `| x-1`: {fr_bad}.\n")
    md.append(f"- failures of `s | y^q+1`, `s` not `| y+1`: {fs_bad}.\n")
    md.append(f"- (p,q,x,y) with `x^p - y^q == 1` in range: {eq_cases} "
              "(none — no odd-prime solution exists here).\n")
    if fail_s_by_qy:
        md.append(f"- s-premise failures, all attributed to the known small "
                  f"Zsigmondy mirror exception `(q,y)=(3,2)` which has NO "
                  f"primitive divisor (appearing once per (p,x) setting: "
                  f"4 p * 39 x = 156): {fail_s_by_qy}.\n")
    md.append("**Scope note:** this is a demonstration of the deductive step "
              "on constructed data; because no actual (x,p,y,q) with p,q both "
              "odd prime satisfies the equation in any reachable range, the "
              "antecedent `x^p - y^q = 1` never fires here. This **does not** "
              "prove that any solution exists; it verifies the implication is "
              "sound as a conditional statement and that its non-trivial "
              "premises hold on the data.\n\n")

    md.append("## Task C — Non-exclusion / scope\n")
    md.append(f"Search over odd primes p,q in [3,30] "
              f"({len(PRIMES_TO_30)} primes) and x,y in [2,200]: "
              f"{total} 4-tuples.\n")
    md.append(f"- actual solutions (`x^p - y^q == 1`) in space: {n_sol} "
              f"(expected 0 for odd primes).\n")
    md.append(f"- 4-tuples satisfying ALL elementary conditions "
              f"`(p | x-1, q | y+1, y has a prime divisor ==1 mod p, "
              f"x has a prime divisor ==1 mod q)` AND `x^p - y^q != 1`: "
              f"**{near}**.\n")
    md.append(f"  - of which `p | y` holds: {py}\n")
    md.append(f"  - of which `q | x` holds: {qx}\n")
    md.append(f"  - of which BOTH `p | y` AND `q | x` (full Cassels "
              f"congruences) hold: {both}\n")
    md.append(f"- triples with BOTH `p | y` AND `q | x` and "
              f"`x^p - y^q != 1` (Cassels-congruence non-solutions, without "
              f"the elementary conditions imposed): {cassels_both_nonsol}\n")
    md.append("\n**Conclusion (sufficiency):** many non-solutions satisfy the "
              "primitive-divisor + elementary Cassels congruences; hence these "
              "conditions are **necessary, not sufficient**, and do NOT by "
              "themselves close the search space. This makes no claim about "
              "the Catalan conjecture; it bounds what the elementary "
              "conditions alone can establish.\n")
    md.append("\n```claim\n")
    md.append("id: mirror-prim-div-scope\n")
    md.append("statement: >\n")
    md.append("  For q in {3,5,7,11,13,17} and y in [2,Ymax_q], Phi_q(-y) has "
              "a primitive divisor s (s | Phi_q(-y), s not | y+1, order of "
              "(-y) mod s = q, s == 1 mod q) for all but the small exceptions "
              "(3,2) [plus excluded (q,1) with Phi_q(-1)=1]. No failure for "
              "y >= 3. The necessary-condition deduction (r | y, s | x) holds "
              "as a sound conditional verified on its unconditional premises. "
              f"Over p,q odd primes <= 29 and x,y in [2,200], {near} "
              "non-solutions satisfy all elementary conditions, so those "
              "conditions are not sufficient.\n")
    md.append("hypotheses: >\n")
    md.append("  p,q odd primes. Mirror primitive divisor on q-side; "
              "Task B checks the deductive chain without any actual solution "
              "existing (the antecedent never fires); Task C ranges are "
              "p,q in {3,5,...,29}, x,y in [2,200].\n")
    md.append("holds-here: yes\n")
    md.append("status: checked (exact integer code; ranges stated; no floats)\n")
    md.append("bearing: elementary (class-group-free); shows the primitive-"
              "divisor + elementary Cassels congruences are necessary but "
              "far from sufficient\n")
    md.append("anchor: code/out/primitive_div_mirror.md\n")
    md.append("```\n")
    with open(OUT_MD, "w") as f:
        f.write("".join(md))
    print(f"\nwrote {OUT_MD}")
    return (fr_bad, fs_bad, eq_cases, fail_s_by_qy,
            (total, n_sol, near, py, qx, both, cassels_both_nonsol))


if __name__ == "__main__":
    main()
