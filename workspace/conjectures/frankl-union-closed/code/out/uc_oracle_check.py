"""Check every oracle routine in code/lib/uc.py against the guards from problem.md.

Runs and prints PASS/FAIL for:
  (1) guard: full power set 2^[n] is union-closed, every element at density 1/2
  (2) family {empty, {1}} reports singleton {1} abundant
  (3) negative control: non-union-closed antichain {{1},{2},{3}} rejected,
      and it has no abundant element
  (4) exhaustive verification for n = 1..4: every union-closed family (other
      than {empty}) has an abundant element; reports the number of such
      families and confirms no counterexample
  (5) closure() reproduces known small cases by hand

Exact integer arithmetic only. This is the oracle-check every later experiment
implicitly relies on.
"""

from lib.uc import (
    decide_union_closed,
    abundance,
    abundant_elements,
    closure,
    verify_uc_exhaustive,
)


def report(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return ok


def check_guard_powerset():
    ok = True
    for n in (0, 1, 2, 3, 4):
        fam = set(range(1 << n))  # the full power set 2^[n]
        uc = decide_union_closed(fam)
        counts = abundance(fam, n)
        m = len(fam)
        half_ok = all(2 * c == m for c in counts)     # density exactly 1/2
        abund = abundant_elements(fam, n)
        reports_all = (len(abund) == n)               # every element is abundant
        strict_abundant = any(2 * c > m for c in counts)  # none strictly > 1/2
        good = uc and half_ok and reports_all and not strict_abundant
        ok &= report(
            f"guard 2^[{n}]",
            good,
            f"|F|={m}, uc={uc}, all half={half_ok}, "
            f"abundant={abund}, strict_abundant={strict_abundant}",
        )
    return ok


def check_singleton():
    # {empty, {1}}: element 0 is in exactly the set {1}, |F|=2, so count=1 >= 1.
    # Using 0-indexed masks: {empty}=0, {1}=bit0 => mask 1.
    fam = {0, 1}
    uc = decide_union_closed(fam)
    abund = abundant_elements(fam, 2)
    ok = uc and (0 in abund)
    report(
        "family {empty,{1}} reports {1} abundant",
        ok,
        f"uc={uc}, abundant={abund}",
    )
    return ok


def check_negative_control():
    # Antichain {{1},{2},{3}} as masks -> bit0={1}, bit1={2}, bit2={3}: {1,2,4}.
    # Every element in exactly 1 of 3 sets, need >= ceil(3/2)=2; none abundant.
    fam = {1, 2, 4}
    uc = decide_union_closed(fam)          # must reject (not union-closed)
    abund = abundant_elements(fam, 3)
    ok = (not uc) and (len(abund) == 0)
    report(
        "negative control {{1},{2},{3}} rejected (not union-closed, no abundant elt)",
        ok,
        f"uc={uc}, abundant={abund}",
    )
    return ok


def check_exhaustive():
    ok = True
    all_counts = {}
    for n in (1, 2, 3, 4):
        count, counterex = verify_uc_exhaustive(n)
        all_counts[n] = count
        good = counterex is None
        ok &= report(
            f"exhaustive n={n}",
            good,
            f"{count} union-closed families (excl. empty collection, incl. {{∅}}), "
            f"counterexample={counterex if counterex is not None else 'none'}",
        )
    print(f"  union-closed family counts: {all_counts}")
    return ok


def check_closure():
    ok = True
    # generators {{1},{1,2}} = masks {1, 3} -> closure {1,3}
    c1 = closure({1, 3})
    ok &= report("closure {{1},{1,2}} -> {{1},{1,2}}", c1 == {1, 3}, f"got sorted={sorted(c1)}")
    # generators {{1},{2}} = masks {1, 2} -> closure {1,2,3}
    c2 = closure({1, 2})
    ok &= report("closure {{1},{2}} -> {{1},{2},{1,2}}", c2 == {1, 2, 3}, f"got sorted={sorted(c2)}")
    return ok


def main():
    results = [
        check_guard_powerset(),
        check_singleton(),
        check_negative_control(),
        check_exhaustive(),
        check_closure(),
    ]
    print()
    if all(results):
        print("ALL ORACLE CHECKS PASSED")
    else:
        print("SOME ORACLE CHECKS FAILED")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
