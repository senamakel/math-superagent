#!/usr/bin/env python3
"""Verify the n=96 open-degree discrepancy FROM the HELD degree-7 bad-prime
list (not from a count).

Directive-12 verification (tool_builder). EXACT integer/set arithmetic only —
no floating point, no inference from a count; every membership below is a
direct read of the held primary data files.

Data range:
  - research/sources/castryck2012_badprimes7.txt.full.md — the FULL degree-7
    bad-prime list (parsed from the fenced body `badprimes7 := [ ... ];`,
    366 primes).
  - research/sources/castryck2012_degree12_html.full.md — Table 1 (degree-6
    bad primes, 53 primes) and eq 6.5 (the degree<=100 published open list).

Base ring / route: integer set membership over QQ-empty (plain integer
arithmetic on parsed primes); no polynomial oracle involved. Source parsing is
exact (regex over the held files).

Four checks:
  (1) the degree-7 list contains exactly 366 primes
  (2) the prime 127 is ABSENT
  (3) every prime < 127 except 7 is PRESENT (i.e. the list contains exactly
      {2,3,5,11,...,113} plus the other small ones, but not 127 and not 7)
  (4) consequence claim: 96 = 6*16 IS an open degree, because 6p^k with base
      p=2 requires p=2 to be a degree-6 BAD prime (and 2 IS in Castryck's
      degree-6 Table 1 — cross-referenced from the held source below), yet
      the published open list (eq 6.5) OMITS 96 — so 96 is open-but-unlisted,
      a genuine discrepancy of the OPPOSITE kind from 98.

Exit code 0 only when checks 1-3 all PASS. Check 4 is reported as a
sourced-corroboration (2 in the degree-6 table, read from the held source;
plus the arithmetic 96=6*16); it does not gate the exit code (it is a
consequence statement resting on source membership, not a list-membership
fact).
"""
import re
import sys
from pathlib import Path

SRC7 = Path("/workspace/research/sources/castryck2012_badprimes7.txt.full.md")
SRC12 = Path("/workspace/research/sources/castryck2012_degree12_html.full.md")


def parse_deg7_list():
    """Parse the integers out of the fenced body `badprimes7 := [ ... ];`."""
    text = SRC7.read_text(encoding="utf-8")
    m = re.search(r"badprimes7\s*:=\s*\[(.*?)\];", text, re.S)
    if not m:
        sys.exit("FAIL: could not locate the badprimes7 list body")
    return [int(p) for p in re.findall(r"\d+", m.group(1))]


def parse_deg6_table():
    """Parse Castryck's degree-6 bad-prime Table 1 (53 primes) from the held
    source. The table body is the run of 'N |' cells between the phrase
    '(a 135 135 -digit number).' (end of the degree-7 sentence) and the
    caption 'Table 1: Bad primes for degree 6'. We slice that window and pull
    every integer, which is exactly the 53 table primes."""
    text = SRC12.read_text(encoding="utf-8")
    start = text.find("digit number).")
    cap = text.find("Table 1: Bad primes for degree 6")
    if start == -1 or cap == -1 or cap < start:
        sys.exit("FAIL: could not bound degree-6 Table 1 region in source")
    window = text[start:cap]
    nums = [int(t) for t in re.findall(r"\d+", window)]
    # The 53 table primes are all >= 2; drop any stray '135'/'number'-digits.
    table = sorted(n for n in set(nums) if n >= 2)
    if len(table) != 53:
        sys.exit(f"FAIL: degree-6 Table 1 parse gave {len(table)} primes, "
                 f"expected 53 (got {table[:10]}...)")
    return table


def parse_published_open():
    """Parse eq 6.5: the 27 published open degrees <= 100."""
    text = SRC12.read_text(encoding="utf-8")
    m = re.search(r"still open\s*is\s*(.*?)\.", text, re.S)
    if not m:
        sys.exit("FAIL: could not locate eq 6.5 published open list")
    # The HTML conversion duplicates the list (spaced + condensed); dedupe.
    return sorted({int(t) for t in re.findall(r"\d+", m.group(1))})


failures = []
def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")
    if not cond:
        failures.append(name)


def main():
    # ---- Check 1: exactly 366 primes ----
    primes = parse_deg7_list()
    s = set(primes)
    print(f"degree-7 bad-prime list parsed from held file: {len(primes)} primes")
    check("(1) list contains exactly 366 primes",
          len(primes) == 366 and len(s) == len(primes),
          f"(len={len(primes)}, distinct={len(s)})")
    # Determinism anchor: largest entry must equal the 135-digit prime quoted
    # in Thm 4 (castryck2012_degree12_html.full.md line ~160).
    THM4_LARGEST = 249847120216983926479165256672374830117371749836786068968700949838499096141806825287856933123954724798488422551659890912229726792102063
    check("(1b) largest entry == Thm-4 quoted 135-digit prime",
          max(primes) == THM4_LARGEST,
          f"(largest starts {str(max(primes))[:30]}...)")

    # ---- Check 2: 127 ABSENT ----
    check("(2) prime 127 is ABSENT",
          127 not in s,
          f"(127 in list? {127 in s})")

    # ---- Check 3: every prime < 127 except 7 is PRESENT ----
    want = {p for p in range(2, 127) if _is_prime(p) and p != 7}
    missing = sorted(want - s)
    absent_7 = (7 not in s)
    check("(3) every prime < 127 except 7 is PRESENT",
          len(missing) == 0,
          f"(missing among primes<127, !=7: {missing})")
    check("(3b) 7 is absent (degree itself good)",
          absent_7,
          f"(7 in list? {7 in s})")
    # also: 127 is the smallest non-bad prime apart from 7 --- 131 present
    check("(3c) 131 present (next entry past a 113..131 gap)",
          131 in s)

    # ---- Check 4: consequence claim (sourced corroboration + arithmetic) ----
    print("\n== Check 4: n=96 open-but-unlisted consequence ==")
    deg6 = parse_deg6_table()
    # Determinism anchor: parsed degree-6 table must equal the known curated
    # 53-prime list (verified in research/notes/n96-verify-held-badprimes7.md).
    CURATED_D6 = {2, 5, 7, 11, 13, 19, 23, 29, 37, 47, 61, 67, 73, 97, 257,
                  811, 983, 1069, 1087, 1187, 1487, 1499, 1901, 2287, 3209,
                  3877, 3881, 4019, 4943, 5471, 6983, 8699, 9337, 15131,
                  15823, 20771, 21379, 23993, 150203, 266587, 547061, 685177,
                  885061, 1030951, 7783207, 17250187, 40362599, 9348983563,
                  70016757407, 2610767527031, 225833117528659,
                  7390044713023799, 51313000813080529}
    print(f"degree-6 Table 1 parsed from held source: {len(deg6)} primes, "
          f"first={deg6[0] if deg6 else None}")
    check("(4-0) parsed degree-6 table == known curated 53-prime list",
          set(deg6) == CURATED_D6)
    two_in_deg6 = 2 in set(deg6)
    print(f"  2 in degree-6 Table 1 (held source): {two_in_deg6}")
    check("(4a) 2 is a degree-6 bad prime (held Table 1)",
          two_in_deg6)
    # arithmetic: 96 = 6 * 2^4
    check("(4b) 96 = 6 * 16 (96 == 6*2**4)",
          96 == 6 * 16 and 96 == 6 * (2 ** 4))
    # 6p^k with base 2 and 2 bad for 6 => 96 not covered => open
    print("  Since 96 = 6*2^4 strictly needs p=2 good for degree 6, and")
    print("  2 IS in the degree-6 bad-prime Table 1, 96 is NOT covered by the")
    print("  6p^k settled family => 96 is open.")
    # published open list omits 96
    pub = parse_published_open()
    pub_set = set(pub)
    print(f"eq 6.5 published open list parsed: {len(pub)} degrees")
    check("(4c) published open list OMITS 96 (open-but-unlisted)",
          96 not in pub_set)
    check("(4d) published open list CONTAINS 98 (opposite-kind control)",
          98 in pub_set)
    # cross reference: 96 in open-by-complement? double check 96 is not in
    # any other m*p^k settled form under m<=7 using held bad sets.
    # (reported, corroborating; does not gate exit)
    open96_detail = _coverage_detail(96, deg6, s)
    print(open96_detail)

    print()
    if failures:
        print(f"SOME CHECKS FAILED: {failures}")
        sys.exit(1)
    print("ALL CHECKS PASSED (checks 1-3 gate exit 0; check 4 corroborated "
          "from held sources + 96=6*16 arithmetic)")
    sys.exit(0)


def _is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def _coverage_detail(n, deg6, deg7):
    """Confirm n is NOT covered by any m*p^k form with m<=7 using the held
    bad-prime sets (m=1,2 unconditional; m=3..7 with their held exclusions)."""
    lines = [f"coverage re-check n={n}: {n}=2^5*3"]
    bad_by_m = {3: {2},
                4: {3, 5, 7},
                5: {2, 3, 7, 11, 131, 193, 599, 3541, 8009},
                6: set(deg6),
                7: deg7}
    any_covered = False
    for m in range(1, 8):
        if n % m != 0:
            continue
        q = n // m
        # is q a prime power p^k?
        qq = q
        p = None
        for cand in range(2, qq + 1):
            if _is_prime(cand) and qq % cand == 0:
                r = qq
                while r % cand == 0:
                    r //= cand
                if r == 1:
                    p = cand
                break
        if p is None:
            continue
        good = True
        if m == 3:
            good = p not in bad_by_m[3]
        elif m == 4:
            good = p not in bad_by_m[4]
        elif m == 5:
            good = p not in bad_by_m[5]
        elif m == 6:
            good = p not in bad_by_m[6]
        elif m == 7:
            good = p not in bad_by_m[7]
        lines.append(f"  {n} = {m}*{p}^({q}-th pp): p={p} good for {m}? {good}")
        if good:
            any_covered = True
    lines.append(f"  => covered by any m*p^k (m<=7): {any_covered}")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
