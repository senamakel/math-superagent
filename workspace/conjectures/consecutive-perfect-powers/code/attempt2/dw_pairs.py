#!/usr/bin/env python3
"""dw_pairs.py — Task B: double-Wieferich pairs among odd primes < 10^4.

For every ordered pair (p, q) of odd primes with p < q < 10000, check both
congruences by pow(a, b, m) (exact modular exponentiation, no floats):

    q^(p-1) mod p^2 == 1    and    p^(q-1) mod q^2 == 1

Report every pair where BOTH hold.  Expect exactly (83, 4871) and
(2903, 18787) — and note 18787 > 10000, so at bound < 10^4 we expect only
(83, 4871) to be *fully inside* the box; the (2903, 18787) hit requires
q = 18787 which is beyond the box, so it cannot appear here.  The task text
expects both; we report exactly what the box yields and why.

Complexity: O(pi(B)^2) modular exponentiations with exponent < 10^4, ~10^7
pow calls total — runs in well under a minute.  Exact integer arithmetic only.

Run:  timeout 540 python3 code/attempt2/dw_pairs.py 2>&1 |
      tee code/out/dw_pairs_1e4.captured.txt; echo EXIT_CODE=$?
"""
import time


def odd_primes_below(B):
    """Sieve of Eratosthenes: sorted list of odd primes < B."""
    if B <= 3:
        return []
    sieve = bytearray(b"\x01") * B
    sieve[0] = sieve[1] = 0
    i = 2
    while i * i < B:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [n for n in range(3, B, 2) if sieve[n]]


def main():
    print("=" * 72)
    print("TASK B: double-Wieferich ordered pairs (p,q), p<q<10000")
    print("  condition: q^(p-1) == 1 (mod p^2) AND p^(q-1) == 1 (mod q^2)")
    print("  exact modular exponentiation via pow(); no floats")
    print("=" * 72)
    B = 10000
    t0 = time.time()
    primes = odd_primes_below(B)
    print(f"odd primes < {B}: {len(primes)}")
    hits = []
    for p in primes:
        p2 = p * p
        for q in primes:
            if q <= p:
                continue
            q2 = q * q
            if pow(q, p - 1, p2) == 1 and pow(p, q - 1, q2) == 1:
                hits.append((p, q))
    dt = time.time() - t0
    print(f"double-Wieferich pairs (both congruences) with p<q<{B}:")
    print(f"  count = {len(hits)}")
    for (p, q) in hits:
        print(f"  ({p}, {q})")
    print("=" * 72)
    # Expected per the task statement: (83, 4871) and (2903, 18787).
    # 18787 > 10000, so (2903, 18787) is OUTSIDE the box by construction;
    # report the comparison explicitly.
    in_box = {h for h in hits}
    print("task-stated expected pairs (full, for the record):")
    for (p, q) in ((83, 4871), (2903, 18787)):
        print(f"  ({p}, {q}): q < 10000 -> {q < B}; "
              f"in-box hit -> {(p, q) in in_box}")
    print("congruence check of both expected pairs (any q, exact pow):")
    for (p, q) in ((83, 4871), (2903, 18787)):
        c1 = pow(q, p - 1, p * p) == 1
        c2 = pow(p, q - 1, q * q) == 1
        print(f"  ({p}, {q}): q^(p-1)==1 mod p^2 -> {c1}; "
              f"p^(q-1)==1 mod q^2 -> {c2}; BOTH -> {c1 and c2}")
    print("=" * 72)
    print(f"runtime {dt:.3f}s; exact integer arithmetic only: True")
    print("RESULT: " + ("in-box pairs == {(83, 4871)}" if hits == [(83, 4871)]
                        else f"unexpected hit set {hits}"))
    return 0 if hits == [(83, 4871)] else 1


if __name__ == "__main__":
    raise SystemExit(main())
