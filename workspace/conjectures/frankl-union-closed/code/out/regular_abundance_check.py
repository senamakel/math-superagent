"""Exhaustive check of the regular-family structure:
For every union-closed family F on [n] (n=1..5) whose present elements all
have equal abundance count c (r present elements):
  (a) c in {1,...,2^{r-1}}  (trivial upper bound = #subsets of [r] containing one element)
  (b) achievability: every value 1..2^{r-1} occurs (checked by collecting the set)
  (c) abundance: c >= m/2, i.e. m <= 2c  (every present element abundant)
n=1..4: direct exhaustive enumeration through lib.uc (65536 subfamilies at n=4).
n=5: all 2,771,102 nonempty UC families via the validated projection/up-set
cascade (profile_count_cascade, same as regular_profiles.captured.txt).
"""
from lib.uc import decide_union_closed, abundance
import importlib.util

spec = importlib.util.spec_from_file_location(
    "profile_count_cascade", "code/out/profile_count_cascade.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)

GUARD = {1: 3, 2: 13, 3: 121, 4: 4959, 5: 2771102}


def check_family(F, n):
    """Return (r, c, m, regular?) with r=#present, c=uniform count, m=|F|."""
    ab = abundance(F, n)
    present = [a for a in ab if a > 0]
    if not present:
        return None
    if len(set(present)) == 1:
        return (len(present), present[0], len(F))
    return None


def direct_levels():
    res = {1: 3, 2: 13, 3: 121, 4: 4959}
    for n in range(1, 5):
        for mask in range(1, 1 << (1 << n)):
            F = frozenset(s for s in range(1 << n) if (mask >> s) & 1)
            if decide_union_closed(F):
                yield n, F


def cascade_levels():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: {f for f in level if f != frozenset({0})}}
    for k in range(1, 5):
        level = pc.extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}
    return levels


def run(n, families, expected):
    total = 0
    by_r = {}
    violations_c = []   # c not in 1..2^{r-1}
    violations_ab = []  # m > 2c
    for F in families:
        total += 1
        reg = check_family(F, n)
        if reg is None:
            continue
        r, c, m = reg
        assert 1 <= c <= 2 ** (r - 1), ("c out of range", n, r, c, m, sorted(F))
        if m > 2 * c:
            violations_ab.append((r, c, m, sorted(F)))
        by_r.setdefault(r, set()).add(c)
    assert total == expected, (n, total, expected)
    print(f"n={n}: UC families={total}")
    reg_total = 0
    ok = True
    for r in sorted(by_r):
        degs = sorted(by_r[r])
        claim = degs == list(range(1, 2 ** (r - 1) + 1))
        ok = ok and claim
        reg_total += len(degs)
        print(f"  r={r}: achievable degrees={degs}  "
              f"all of 1..2^{r-1}: {claim}")
    print(f"  REG(n)={reg_total} == 2^n-1={2**n - 1}: {reg_total == 2**n - 1}")
    print(f"  (a)+(b) full: {ok}")
    print(f"  (c) m<=2c violations (every element abundant): {len(violations_ab)}")
    for v in violations_ab[:5]:
        print("     VIOLATION:", v)
    return ok, len(violations_ab)


if __name__ == "__main__":
    print("Regular-family structure check (a),(b),(c), n=1..5, exhaustive, exact.")
    print("oracle: lib.uc (n<=4 direct) + profile_count_cascade (n=5), both "
          "validated vs A121921.")
    print("range : ALL UC families on n=1..5; no floats; assertions on guards.")
    # n=1..4 direct
    for n in range(1, 5):
        fams = (F for nn, F in direct_levels() if nn == n)
        run(n, fams, GUARD[n])
    # n=5 cascade
    levels = cascade_levels()
    run(5, levels[5], GUARD[5])
    print("ALL DONE")