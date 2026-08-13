#!/usr/bin/env python3
"""Exact integer iterated absolute-difference generators for Gilbreath rows,
reproducing the worked examples in problem.md.

Exports:
  primes_up_to(n)
  rows_generator(primes, depth)
  block_profile(row)
  diff_block(row)          -> row after one diff pass
  ramp_family(block, x, T) -> generic even rows: [1,b..., x, x+2, ...] all
                              even, first beyond-block entry = x.
Used by the block-lemma verification and by the real-rows check.
"""
from math import isqrt


def primes_up_to(n):
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = b"\x00" * (((n - i*i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def rows_generator(primes, depth):
    cur = [int(p) for p in primes]
    yield cur
    for _ in range(depth):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        yield cur


def diff_block(row):
    return [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]


def block_profile(row):
    length = 0
    for x in row[1:]:
        if x in (0, 2):
            length += 1
        else:
            break
    return length


EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
    3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
}


def _work():
    depth = 5
    primes = primes_up_to(60)
    gen = rows_generator(primes, depth)
    got = [next(gen) for _ in range(depth + 1)]
    all_match = all(got[k][:12] == EXPECTED[k] for k in range(1, depth + 1))
    for k in range(1, depth + 1):
        print(f"A_{k} = {got[k][:12]}  match={got[k][:12] == EXPECTED[k]}")
    print("ALL five worked rows match:", all_match)
    return all_match


if __name__ == "__main__":
    _work()
