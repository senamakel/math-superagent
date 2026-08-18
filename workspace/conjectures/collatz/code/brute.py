"""code/brute.py -- naive oracle for the Collatz conjecture.

Bears on: code/lean/Lib/collatz_conjecture.lean (Cited.collatz_conjecture),
the statement that for every positive integer n the orbit of n under

    C(n) = n / 2   if n is even
           3n + 1  if n is odd

eventually reaches 1.

Deliberately naive, exact integer arithmetic only, no optimisation:
simulate one step at a time, remember every visited value in a set, and
stop at a hard step cap so a slow case cannot run away. This is the oracle
that later, faster methods are checked against -- it exists to pin down what
the statement means, not to reach any large bound.

The finite-time verdicts it can give:
  True   -- the orbit reached 1 (conjecture holds for this n).
  False  -- the orbit revisited a value x != 1; the map is deterministic,
            so from then on the orbit cycles and never reaches 1. This is a
            genuine non-trivial cycle: a counterexample to the conjecture.
  None   -- the step cap ran out with no repeat and no 1 reached. Divergence
            to infinity cannot be decided in finite time; None means unknown.
"""

from typing import Optional

__all__ = ["collatz_step", "orbit_reaches_one", "main"]

DEFAULT_CAP = 10**6  # safety cap; this run passes a much smaller one explicitly


def collatz_step(n: int) -> int:
    """One Collatz step: C(n) = n/2 if n even, else 3n+1. Exact arithmetic."""
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def orbit_reaches_one(n: int, cap: int = DEFAULT_CAP) -> Optional[bool]:
    """Decide, in at most `cap` steps, whether the orbit of n reaches 1.

    Returns True / False / None as documented in the module docstring.
    Time O(steps), space O(steps) for the visited set, steps <= cap.
    """
    seen = set()
    x = n
    steps = 0
    while steps < cap:
        if x == 1:
            return True
        if x in seen:
            # x != 1 and we have been here before: a cycle that never
            # reaches 1, i.e. a counterexample to the conjecture.
            return False
        seen.add(x)
        x = collatz_step(x)
        steps += 1
    return None  # inconclusive: cap exhausted


def main() -> None:
    """Reproduce the worked example from problem.md and check tiny orbits."""
    # Worked example: the cycle 1 -> 4 -> 2 -> 1.
    orbit = []
    x = 1
    for _ in range(4):
        orbit.append(x)
        x = collatz_step(x)
    print("worked example: orbit of 1 (4 terms) =", orbit)
    print("  collatz_step(1) =", collatz_step(1),
          " collatz_step(4) =", collatz_step(4),
          " collatz_step(2) =", collatz_step(2))
    ok_cycle = (orbit == [1, 4, 2, 1])
    print("  matched 1 -> 4 -> 2 -> 1:", ok_cycle)

    # Tiny orbits, all known to reach 1; the statement is about every
    # positive integer, so these are the smallest instances of it.
    for n in list(range(1, 11)) + [27]:
        v = orbit_reaches_one(n, cap=1000)
        print(f"  n = {n:3d}: reaches 1 = {v}")
        assert v is True, f"oracle failed on n={n}: got {v}"


if __name__ == "__main__":
    main()
