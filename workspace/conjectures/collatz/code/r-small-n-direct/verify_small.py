"""code/r-small-n-direct/verify_small.py -- exact memoized verification that
every 1 <= n <= 2^20 reaches 1 under the Collatz map.

Bears on: code/lean/Lib/collatz_conjecture.lean, Cited.collatz_conjecture
(forall n > 0, exists k, C^k(n) = 1). This program is finite, exact evidence
for the instances n <= 2^20 of that statement; it is not a proof for all n.

Method (deliberately naive): direct simulation one step at a time with a
visited set and a step cap -- the same oracle semantics as code/brute.py --
plus a dict memoising the verdict for every value whose orbit has been
decided, so orbits are never recomputed. When a walk hits a memoised value
its verdict propagates back along the whole current path. The single source
for the map C and for the naive oracle is code/brute.py (imported as
`brute`), so the two methods cannot drift apart on the definition of a step.

Verdicts, identical in meaning to code/brute.py:
  True  -- the orbit reached 1 (conjecture holds for this n).
  False -- the orbit revisited a value x != 1; the map is deterministic, so
           this is a genuine non-trivial cycle, i.e. a counterexample.
  None  -- the step cap ran out with no repeat and no 1 reached; divergence
           to infinity is undecidable in finite time, so None means unknown.

Complexity: time O(B * cap) worst case, where B = number of n checked and
cap = STEP_CAP (memoisation makes the real cost far smaller: every walk
stops at the first already-decided value, and all values below n are decided
before n is processed); space O(distinct values visited + cap). Exact integer
arithmetic only, no floats in any verdict.

The run prints, in order:
  1. a cross-check of the memoised method against brute.orbit_reaches_one on
     n = 1..CROSSCHECK_MAX (1000);
  2. the sweep n = 1..BOUND with a FAIL line on any non-True verdict;
  3. the count of n checked, the wall time of the sweep, and the verdict
     line "ALL n <= 2^20 REACH 1" when every n checked reached 1.
"""

import time
from typing import Dict, Optional

from brute import collatz_step, orbit_reaches_one

BOUND = 2**20          # check every 1 <= n <= 2^20 -- do not raise this here
STEP_CAP = 10**6       # safety cap; matches brute.py's default
CROSSCHECK_MAX = 1000  # cross-check range against the naive oracle

# memo[n] = verdict for the orbit of n: True / False / None.
memo: Dict[int, Optional[bool]] = {1: True}


def memoized_reaches_one(n: int, cap: int = STEP_CAP) -> Optional[bool]:
    """Decide whether the orbit of n reaches 1, memoising every value walked.

    Walks the orbit of n, appending each value to `path`, until it either
    hits a value already in `memo` (whose verdict propagates to the whole
    path), revisits a value inside the path (a deterministic cycle not
    containing 1: verdict False), or exceeds the cap (verdict None).
    Time O(path length), space O(path length) beyond the shared memo.
    """
    path: list[int] = []
    in_path: set[int] = set()
    x = n
    while True:
        if x in memo:
            verdict = memo[x]
            for v in path:
                memo[v] = verdict
            return verdict
        if x in in_path:
            # x != 1 here (1 is in memo), and the map is deterministic, so
            # the orbit cycles and never reaches 1: a counterexample.
            for v in path:
                memo[v] = False
            return False
        in_path.add(x)
        path.append(x)
        if len(path) > cap:
            # Inconclusive: cap exhausted without a decision.
            for v in path:
                memo[v] = None
            return None
        x = collatz_step(x)


def main() -> None:
    # 1. Cross-check the memoised method against the naive oracle.
    mismatches = 0
    for n in range(1, CROSSCHECK_MAX + 1):
        fast = memoized_reaches_one(n)
        naive = orbit_reaches_one(n)
        if fast != naive:
            mismatches += 1
            print(f"CROSSCHECK MISMATCH n={n}: memoized={fast} naive={naive}")
    print(f"cross-check vs code/brute.py orbit_reaches_one on n=1..{CROSSCHECK_MAX}: "
          f"{'AGREE' if mismatches == 0 else str(mismatches) + ' MISMATCHES'}")

    # 2. The verification sweep, n ascending; everything below n is already
    #    decided, so each walk stops at the first previously-decided value.
    t0 = time.perf_counter()
    count = 0
    all_reach = True
    for n in range(1, BOUND + 1):
        if n not in memo:
            v = memoized_reaches_one(n)
            if v is not True:
                all_reach = False
                print(f"FAIL: n={n} verdict={v}")
                break
        count += 1
    sweep_wall = time.perf_counter() - t0

    # 3. Report.
    print(f"count of n checked: {count}")
    print(f"sweep wall time: {sweep_wall:.3f} s")
    print("VERDICT:", "ALL n <= 2^20 REACH 1"
          if all_reach and count == BOUND
          else "NOT ALL n <= 2^20 REACH 1")


if __name__ == "__main__":
    main()
