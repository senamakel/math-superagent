#!/usr/bin/env python3
"""Prove the c2-alternating-sum identity (upgrade check -> proved).

STATEMENT (exact invariant of the iterated absolute-difference operator, for
ANY nonneg-integer starting sequence, not just the primes):

For any row A_k = (A_k(0), ..., A_k(W)) with W = len(A_k)-1, and
A_{k+1}(i) = |A_k(i) - A_k(i+1)| for i=0..W-1, with the alternating sum
sigma(v) = sum_i (-1)^i v_i:

    sigma(A_{k+1}) = A_k(0) - (-1)^W A_k(W) - 2 * sum_{i=0}^{W-1} (-1)^i min(A_k(i), A_k(i+1))

PROOF (two lines, general over all nonneg integers):
  |a-b| = a+b-2min(a,b), so
  sigma(A_{k+1})
    = sum_{i=0}^{W-1} (-1)^i A_k(i)            [part A]
    + sum_{i=0}^{W-1} (-1)^i A_k(i+1)          [part B]
    - 2 sum_{i=0}^{W-1} (-1)^i min(A_k(i),A_k(i+1))
  Part B = sum_{j=1}^{W} (-1)^{j-1} A_k(j) = -sum_{j=1}^{W} (-1)^j A_k(j).
  Part A has terms i=0..W-1; part B has terms j=1..W. The interior terms
  i=j=1..W-1 carry opposite signs and cancel exactly, leaving
  A_k(0)   (from part A, i=0)
  + (-1)^W A_k(W) * -1 = -(-1)^W A_k(W)   (from part B, j=W, note the minus)
  i.e. A_k(0) - (-1)^W A_k(W). QED.

This program (1) exploits the ORACLE rows_generator to re-verify the identity
on the real prime rows (claim c2 alternates), (2) re-verifies it on MANY
arbitrary random nonneg starting rows (showing it is general, not prime-
specific), and (3) checks the algebraic split numerically: |a-b| vs a+b-2min
on every pair. All exact integer arithmetic.
"""
import random
from lib.gilbreath import primes_up_to, rows_generator


def alternating_sum(v):
    return sum((-1)**i * val for i, val in enumerate(v))


def identity_rhs(row):
    """Right-hand side: A_k(0) - (-1)^W A_k(W) - 2 sum (-1)^i min(pair)."""
    W = len(row) - 1
    total = row[0] - (-1)**W * row[W]
    for i in range(W):
        total -= 2 * ((-1)**i) * min(row[i], row[i + 1])
    return total


def verify_rows(rows, label):
    """rows: list of consecutive rows A_0..A_D. Check identity on each pair."""
    viol = 0
    checked = 0
    for k in range(len(rows) - 1):
        A_k = rows[k]
        A_k1 = rows[k + 1]
        # self-consistency: A_{k+1} must literally be the diff of A_k
        assert A_k1 == [abs(A_k[i] - A_k[i + 1]) for i in range(len(A_k) - 1)], \
            f"{label}: A_{k+1} not the diff of A_{k}"
        if alternating_sum(A_k1) != identity_rhs(A_k):
            viol += 1
            print(f"  VIOLATION {label} row k={k}: sigma(A_{k+1})={alternating_sum(A_k1)} rhs={identity_rhs(A_k)}")
        checked += 1
    return checked, viol


def check_abs_split(pairs):
    """Verify |a-b| = a+b-2min(a,b) exactly on the given pairs."""
    for a, b in pairs:
        if abs(a - b) != a + b - 2 * min(a, b):
            return False
    return True


def main():
    print("=" * 70)
    print("PROOF of the c2 alternating-sum identity (general, nonneg integers)")
    print("=" * 70)

    # (1) Real prime rows.
    primes = primes_up_to(200000)
    depth = 158
    rows = list(rows_generator(primes, depth))
    print(f"\n(1) Real prime rows: sieve 200000 ({len(primes)} primes), depth {depth}.")
    c, v = verify_rows(rows, "primes")
    print(f"    {c} consecutive row pairs checked, {v} violations.")
    print("    -> reproduces claim c2-alternating-sum-identity (0 violations).")

    # (2) Arbitrary nonneg starting rows: the identity generalizes to any
    #     nonneg-integer sequence (the proof never used primality).
    rng = random.Random(12345)
    tot_c, tot_v = 0, 0
    for trial in range(300):
        L = rng.randint(2, 10)
        start = [rng.randint(0, 30) for _ in range(L)]
        # only take as many rows as the width supports (each diff shrinks by 1)
        sub = []
        cur = start
        while len(cur) >= 2:
            sub.append(cur)
            cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        c2, v2 = verify_rows(sub, f"random#{trial}")
        tot_c += c2
        tot_v += v2
    print(f"\n(2) 300 arbitrary nonneg starting rows (length 2..10, entries 0..30):")
    print(f"    {tot_c} consecutive row pairs checked, {tot_v} violations.")
    print("    -> the identity is a general invariant of the operator, not prime-specific.")

    # (3) Algebraic split |a-b| = a+b-2min on every pair met.
    pairs = [(rng.randint(0, 10**9), rng.randint(0, 10**9)) for _ in range(200000)]
    ok = check_abs_split(pairs)
    pairs_small = [(a, b) for a in range(8) for b in range(8)]
    ok_small = check_abs_split(pairs_small)
    print(f"\n(3) |a-b| == a+b-2*min(a,b) on all 8x8 small pairs: {ok_small};")
    print(f"    on 200000 random pairs in [0,1e9]: {ok}.")

    total_viol = v + tot_v
    print("\n" + "=" * 70)
    if total_viol == 0:
        print("RESULT: identity CONFIRMED with 0 violations — and PROVED")
        print("by the exact two-line telescoping argument above (general over")
        print("all nonneg-integer sequences, uses only |a-b|=a+b-2min(a,b)).")
    else:
        print(f"RESULT: REFUTED — {total_viol} violations")
    print("=" * 70)


if __name__ == "__main__":
    main()
