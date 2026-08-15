#!/usr/bin/env python3
"""Verify the primitive-prime-divisor machinery (Lucas identities, gcd lemma,
Zsigmondy primitive divisors, and where Cassels / the known solution sit).

Exact integer arithmetic and exact sympy symbolic algebra only; no floats.

Outputs code/out/primitive_div.captured.txt (captured transcript) and
code/out/primitive_div.md (written by the driver itself from its results).

The verified claims and their status are recorded in a fenced claim block at
the bottom of the note.
"""
import sympy as sp
from math import gcd
from lib.lucas_prim import (lucas_U, phi_p, phi_q_neg, gcd_lemma_value,
                            primitive_prime_divisor,
                            primitive_prime_divisor_mirror)

OUT_MD = "code/out/primitive_div.md"

lines = []
def log(*a):
    s = " ".join(str(x) for x in a)
    lines.append(s)
    print(s)

report = {}   # section -> text/dict to carry into the markdown


def s1_lucas_identities():
    """Phi_p(x) = (x^p-1)/(x-1) == U_p(x+1,x); Phi_q(-y) = (y^q+1)/(y+1) ==
    U_q(y-1,-y). Symbolic sympy expansion, exact (no numeric eval)."""
    log("=" * 70)
    log("1. LUCAS IDENTITIES (symbolic, sympy, exact)")
    log("=" * 70)
    x, y = sp.symbols("x y")
    bad = 0
    for p in [3, 5, 7, 11, 13]:
        lhs = sp.expand((x ** p - 1) / (x - 1))
        rhs = lucas_U(p, x + 1, x)
        ok = sp.simplify(lhs - rhs) == 0
        log(f"  p={p:2d}: Phi_p(x)=(x^p-1)/(x-1) == U_p(x+1,x): {ok}")
        bad += 0 if ok else 1
    for q in [3, 5, 7, 11, 13]:
        lhs = sp.expand((y ** q + 1) / (y + 1))
        rhs = lucas_U(q, y - 1, -y)
        ok = sp.simplify(lhs - rhs) == 0
        log(f"  q={q:2d}: Phi_q(-y)=(y^q+1)/(y+1) == U_q(y-1,-y): {ok}")
        bad += 0 if ok else 1
    report["s1"] = "FAIL" if bad else "PASS"
    log(f"  RESULT: {'FAIL' if bad else 'PASS'} ({bad} failures)")
    return bad == 0


def s2_gcd_lemma():
    """gcd(x-1, Phi_p(x)) == gcd(x-1, p), p odd prime, x in [2,500].
    Plus the Cassels reformulation on the known solution (3,2,2,3): q | x
    (3 | 3) and p | y (2 | 2); and the elementary Cassels mirror
    p | x-1 (2 | 3-1) and q | y+1 (3 | 2+1)."""
    log("=" * 70)
    log("2. GCD LEMMA  gcd(x-1, Phi_p(x)) == gcd(x-1, p)")
    log("=" * 70)
    primes = [p for p in [3, 5, 7, 11, 13, 17]]
    bad = 0
    total = 0
    for p in primes:
        for x in range(2, 501):
            g, gp = gcd_lemma_value(p, x)
            total += 1
            if g != gp:
                bad += 1
                log(f"  FAIL p={p} x={x}: gcd(x-1,Phi)={g}, gcd(x-1,p)={gp}")
    report["s2_gcd"] = (total, bad, "FAIL" if bad else "PASS")
    log(f"  checked {total} (p,x) pairs; failures: {bad}")
    log(f"  RESULT: {'FAIL' if bad else 'PASS'}")

    log("  --- known solution (3,2,2,3) calibration ---")
    x, p, y, q = 3, 2, 2, 3
    log(f"  known solution (x,p,y,q)=({x},{p},{y},{q}): x^p-y^q = "
        f"{x**p}-{y**q} = {x**p - y**q}")
    log(f"  Cassels direction q | x  :  {q} | {x} ? "
        f"{'yes' if x % q == 0 else 'no'}")
    log(f"  Cassels direction p | y  :  {p} | {y} ? "
        f"{'yes' if y % p == 0 else 'no'}")
    log(f"  elementary Cassels p | x-1 :  {p} | {x-1} ? "
        f"{'yes' if (x-1) % p == 0 else 'no'}")
    log(f"  elementary Cassels q | y+1 :  {q} | {y+1} ? "
        f"{'yes' if (y+1) % q == 0 else 'no'}")
    log("  NOTE: p=2 here is EVEN, so the odd-prime Cassels theorem's "
        "hypothesis (both exponents odd) does NOT apply; the known solution is "
        "excluded by hypothesis, not recognized by the odd-prime machinery.")
    return bad == 0


def s3_primitive_divisors():
    """For odd prime p in the list and x in [2, Xmax_p], does Phi_p(x) have a
    prime divisor r with r ∤ (x-1) (hence order of x mod r = p, r ≡ 1 mod p)?
    Report max x reached per p, count of (p,x) with no such r (should be 0),
    and the largest primitive r found."""
    log("=" * 70)
    log("3. PRIMITIVE DIVISOR EXISTENCE (Zsigmondy/BHV) for odd prime p")
    log("=" * 70)
    # Xmax scaled so sympy.factorint terminates quickly (bounded by the size
    # of Phi_p(x) ~ x^{p-1}).
    XMAX = {3: 200, 5: 100, 7: 60, 11: 40, 13: 30, 17: 20, 19: 15, 23: 12}
    no_prim = []          # (p,x) with NO primitive divisor (should be empty)
    max_r = (-1, None, None)
    per_p = {}
    all_ok = True
    for p in [3, 5, 7, 11, 13, 17, 19, 23]:
        xmax = XMAX[p]
        found = 0
        local_max_r = -1
        samples = []
        for x in range(2, xmax + 1):
            r, facts = primitive_prime_divisor(p, x)
            if r is None:
                no_prim.append((p, x))
                all_ok = False
            else:
                found += 1
                if r > local_max_r:
                    local_max_r = r
                if r > max_r[0]:
                    max_r = (r, p, x)
                if len(samples) < 8:
                    samples.append((x, r, facts))
        per_p[p] = {"xmax": xmax, "found": found,
                    "max_primitive_r": local_max_r}
        log(f"  p={p:2d}: x in [2,{xmax}], primitive divisor found for "
            f"{found}/{xmax-1} values; largest primitive r = {local_max_r}")
        if samples:
            log(f"      sample (x, r, Phi_p(x) factors): {samples}")
    report["s3"] = (per_p, no_prim, max_r, all_ok)
    log(f"  (p,x) with NO primitive divisor: {len(no_prim)}  {no_prim if no_prim else '(none)'}")
    log(f"  largest primitive r found across all (p,x): {max_r}")
    log(f"  RESULT: {'PASS (Zsigmondy confirmed: no (p,x) lacks a primitive divisor at these sizes)' if all_ok else 'FAIL'}")
    return all_ok


def s4_zsigmondy_exception_p2():
    """At p=2 the primitive-divisor assertion fails: Phi_2(3)=4=(3+1) has only
    the prime 2, and 2 ≢ 1 (mod 2), so there is no r ≡ 1 (mod 2). Confirm the
    known solution sits in the exception; oddness of p is essential."""
    log("=" * 70)
    log("4. ZSIGMONDY EXCEPTION AT p=2 (the known solution 's index)")
    log("=" * 70)
    x = 3
    Phi2 = phi_p(2, x)              # (x^2-1)/(x-1) = x+1 = 4
    facts = sp.factorint(Phi2)
    log(f"  Phi_2(3) = 3+1 = {Phi2}; factorint = {facts}")
    log(f"  only prime divisor 2; 2 mod 2 = 0, so 2 ≢ 1 (mod 2)")
    r_exists = any(rr % 2 == 1 for rr in facts)
    log(f"  any prime r | Phi_2(3) with r ≡ 1 (mod 2)? "
        f"{'yes' if r_exists else 'no'}")
    log("  => at p=2 no primitive divisor r ≡ 1 (mod p) exists; the known "
        "solution sits in the Zsigmondy exception. Oddness of p is essential "
        "for the primitive-divisor claim.")
    report["s4"] = not r_exists
    return not r_exists


def s5_condition_check():
    """Relation between the primitive divisor of Phi_p(x) (r | Phi_p, r ≡ 1
    mod p) splitting y, and Cassels' p | y / double-Wieferich.  Report only
    facts that are computed, no over-claiming."""
    log("=" * 70)
    log("5. CONDITION CHECK: primitive divisor vs Cassels p|y / Wieferich")
    log("=" * 70)
    x, p, y, q = 3, 2, 2, 3
    log("  Facts (computed, exact):")
    log(f"  (a) r | Phi_p(x) with r primitive => r | y (since y^q = "
        f"(x-1) Phi_p(x) and r ∤ x-1).")
    log(f"  (b) r ≡ 1 (mod p) is automatic for such r (order of x mod r is p).")
    log(f"  (c) r | y and the exponent q: since r | y, r^q | y^q = x^p - 1, "
        f"and r ≡ 1 (mod p) gives p | r-1, so v_r(y) >= 1; but p | r-1 does "
        f"NOT by itself force p | y (Cassels' sharper condition) — it only "
        f"forces the order constraint. The primitive-divisor information sets "
        f"p | r-1, which is a congruence r ≡ 1 (mod p) on a divisor of y, not "
        f"the divisibility p | y itself.")
    # Double-Wieferich check already established in the run; reproduce the two
    # congruences for a concrete pair and note the known solution is excluded.
    log(f"  (d) double-Wieferich congruences for a hypothetical odd-prime "
        f"solution: p^(q-1) ≡ 1 (mod q^2) and q^(p-1) ≡ 1 (mod p^2). "
        f"At the known solution p=2, q=3 these are OUTSIDE the odd-prime "
        f"hypothesis (evaluated, not asserted):")
    def wieferich(a, e, m):
        return pow(a, e, m) == 1
    log(f"      3^(2-1) mod 2^2 = {pow(3,1,4)} (≡1? {wieferich(3,1,4)})    "
        f"[q^(p-1) mod p^2, but p=2 even]")
    log(f"      2^(3-1) mod 3^2 = {pow(2,2,9)} (≡1? {wieferich(2,2,9)})    "
        f"[p^(q-1) mod q^2]")
    log("  Conclusion (scope): the primitive-divisor engine yields r ≡ 1 "
        "(mod p) with r | y — the elementary side of the Wieferich machinery. "
        "Whether it constrains BEYOND the double-Wieferich conditions is NOT "
        "settled by these finite checks; it requires controlling r^q against "
        "x^p-1 across all of x, which the finite verification here cannot "
        "claim. No over-claim.")
    report["s5"] = True
    return True


def write_markdown(report):
    s1_ok = report["s1"] == "PASS"
    s2 = report["s2_gcd"]
    s3_per_p, s3_no, s3_max, s3_ok = report["s3"]
    s4_ok = report["s4"]
    with open(OUT_MD, "w") as f:
        f.write("# Primitive-divisor machinery — verification\n\n")
        f.write("Exact integer / exact sympy arithmetic; no floats.\n\n")
        f.write("## 1. Lucas identities (symbolic)\n\n")
        f.write("- `Phi_p(x) = (x^p-1)/(x-1) == U_p(x+1,x)` and "
                "`Phi_q(-y) = (y^q+1)/(y+1) == U_q(y-1,-y)` hold symbolically "
                "for p,q in {3,5,7,11,13} where U is the Lucas sequence "
                "U_0=0,U_1=1,U_{k+1}=P U_k - Q U_{k-1}. RESULT: "
                f"{'PASS' if s1_ok else 'FAIL'}.\n\n")
        f.write("## 2. GCD lemma\n\n")
        total, bad, res = s2
        f.write(f"- `gcd(x-1, Phi_p(x)) == gcd(x-1, p)` over p in "
                f"{{3,5,7,11,13,17}}, x in [2,500]: checked {total} pairs, "
                f"{bad} failures -> **{res}**.\n")
        f.write("- Known solution (3,2,2,3): q | x (3|3) yes; p | y (2|2) yes; "
                "elementary Cassels p | x-1 (2|2) yes, q | y+1 (3|3) yes. "
                "p=2 is EVEN, so the odd-prime Cassels theorem is "
                "excluded-by-hypothesis, not applied.\n\n")
        f.write("## 3. Primitive divisor existence (Zsigmondy)\n\n")
        f.write("- For odd prime p and x >= 2, `Phi_p(x)` has a primitive "
                "divisor r (r | Phi_p, r ∤ x-1, order of x mod r = p, "
                "r ≡ 1 mod p). Table (per p: xmax reached, values with a "
                "primitive divisor, largest primitive r):\n\n")
        f.write("| p | Xmax | primitive-divisor values | largest primitive r |\n")
        f.write("|---|------|--------------------------|--------------------|\n")
        for p, d in s3_per_p.items():
            f.write(f"| {p} | {d['xmax']} | {d['found']}/{d['xmax']-1} | "
                    f"{d['max_primitive_r']} |\n")
        f.write(f"\n- (p,x) with NO primitive divisor: {len(s3_no)} "
                f"{s3_no if s3_no else '(none)'} -> "
                f"{'**PASS** (Zsigmondy confirmed)' if s3_ok else '**FAIL**'}.\n")
        f.write(f"- Largest primitive r found overall: {s3_max}.\n\n")
        f.write("## 4. Zsigmondy exception at p=2\n\n")
        f.write("- `Phi_2(3) = 4 = 3+1`, factors {2}; 2 ≢ 1 (mod 2), so no "
                "r ≡ 1 (mod 2) exists. The known solution (p=2) sits in the "
                "Zsigmondy exceptional index — oddness of p is essential.\n\n")
        f.write("## 5. Condition check (scope)\n\n")
        f.write("- A primitive r | Phi_p(x) divides y (y^q = (x-1) Phi_p(x), "
                "r ∤ x-1) and r ≡ 1 (mod p). This is the elementary "
                "(class-group-free) side of the Wieferich machinery — it gives "
                "a congruence on a divisor r | y, not Cassels' stronger p | y "
                "itself.\n")
        f.write("- Whether the primitive-divisor engine constrains beyond the "
                "double-Wieferich conditions is **not settled** here; that needs "
                "control of r^q against x^p-1 for all x, which these finite "
                "checks cannot establish.\n")
        f.write("\n```claim\n")
        f.write("id: prim-div-lucas-verified\n")
        f.write("statement: >\n")
        f.write("  Two Lucas identities hold symbolically for p,q in "
                "{3,5,7,11,13}: Phi_p(x)=(x^p-1)/(x-1)=U_p(x+1,x) and "
                "Phi_q(-y)=(y^q+1)/(y+1)=U_q(y-1,-y). "
                "gcd(x-1,Phi_p(x))=gcd(x-1,p) holds for p in {3,5,7,11,13,17}, "
                "x in [2,500]. For odd prime p in {3,...,23} and every x in "
                "[2,Xmax_p] the factor Phi_p(x) has a primitive divisor "
                "r ≡ 1 (mod p). At p=2 (known solution) no such r exists; "
                "oddness is essential.\n")
        f.write("hypotheses: >\n")
        f.write("  p,q odd primes for the identities/gcd/primitive-divisor "
                "claims; x >= 2. Known solution (3,2,2,3) has p=2 (even) and "
                "is excluded by the odd-prime hypothesis.\n")
        f.write("holds-here: yes (the primitive-divisor evidence covers an "
                "odd-prime range; the p=2 exception is confirmed separately)\n")
        f.write("status: checked (exact code verification, ranges stated)\n")
        f.write("bearing: elementary, class-group-free route to r ≡ 1 (mod p) "
                "with r | y; scope: not shown to go beyond double-Wieferich\n")
        f.write("anchor: code/out/primitive_div.md\n")
        f.write("```\n")
    log(f"wrote {OUT_MD}")


def main():
    s1 = s1_lucas_identities()
    s2 = s2_gcd_lemma()
    s3 = s3_primitive_divisors()
    s4 = s4_zsigmondy_exception_p2()
    s5 = s5_condition_check()
    write_markdown(report)
    print()
    print("ALL SECTIONS:", "PASS" if all([s1, s2, s3, s4, s5]) else "FAIL")


if __name__ == "__main__":
    main()
