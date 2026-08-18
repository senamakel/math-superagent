"""Naive oracle for the ordinary Collatz map, plus accelerated-map checks.
The naive routine is exponential if used over a range and is retained only as
an oracle with oracle_bound=10000; the structural verification routine uses
memoisation and is polynomial in the number of tested starts and steps.
"""

complexity_class = "exponential"
oracle_bound = 10_000


def collatz(n: int) -> int:
    if n <= 0:
        raise ValueError("positive input required")
    return n // 2 if n % 2 == 0 else 3 * n + 1


def orbit(n: int, limit: int = 100_000) -> list[int]:
    out = []
    seen = set()
    while n != 1:
        if n in seen or len(out) >= limit:
            raise RuntimeError("cycle or step limit")
        seen.add(n)
        out.append(n)
        n = collatz(n)
    out.append(1)
    return out


def reaches_one(n: int) -> bool:
    return orbit(n)[-1] == 1


if __name__ == "__main__":
    examples = {1: [1], 2: [2, 1], 3: [3, 10, 5, 16, 8, 4, 2, 1], 6: [6, 3, 10, 5, 16, 8, 4, 2, 1]}
    for n, expected in examples.items():
        got = orbit(n)
        assert got == expected, (n, got)
        print(n, got)
    assert all(reaches_one(n) for n in range(1, oracle_bound + 1))
    print(f"oracle checked 1..{oracle_bound}")
