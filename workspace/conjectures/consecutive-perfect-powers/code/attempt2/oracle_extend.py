#!/usr/bin/env python3
"""oracle_extend.py — Task A: extend the exact-integer oracle to N = 10^9 and
N = 10^10.

Reuses lib/valuation.perfect_powers_upto + lib/valuation.solutions (exact
integer arithmetic only; no floats anywhere).  Must return exactly
{(3, 2, 2, 3)} for both bounds.  Reports the N reached and wall runtime.

Run:  timeout 540 python3 code/attempt2/oracle_extend.py 2>&1 |
      tee code/out/oracle_1e10.captured.txt; echo EXIT_CODE=$?
"""
import time

from lib.valuation import perfect_powers_upto, solutions


def main():
    print("=" * 72)
    print("TASK A: oracle solutions(N) at N = 10^9 and N = 10^10")
    print("exact integer arithmetic only (no floats)")
    print("=" * 72)
    expected = {(3, 2, 2, 3)}
    all_ok = True
    for N in (10 ** 9, 10 ** 10):
        t0 = time.time()
        result = solutions(N)
        dt = time.time() - t0
        ok = set(result) == expected
        all_ok &= ok
        print(f"N={N:<12} result={result}  "
              f"{'OK' if ok else 'MISMATCH'}  {dt:.3f}s")
    # a cheap independent cross-check: the number of perfect powers <= 1e10
    t0 = time.time()
    pp = perfect_powers_upto(10 ** 10)
    dt = time.time() - t0
    print(f"independent count: perfect-power values <= 10^10 = {len(pp)} "
          f"({dt:.3f}s)")
    print("=" * 72)
    if all_ok:
        print("ORACLE: exactly {(3,2,2,3)} at N=10^9 and N=10^10. PASS")
    else:
        print("ORACLE: MISMATCH")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
