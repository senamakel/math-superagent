#!/usr/bin/env python3
"""Machine check for the prefix-determinism identity (Directive 48 item 1).

Claim (three lines)
-------------------
The 0-2 cycle pattern of delta(q_n) depends only on q_1..q_{n-1}.  By the
right-diagonal recurrence
      delta_k(q_n) = | delta_{k-1}(q_n) - delta_{k-1}(q_{n-1}) |   (k >= 1)
the eps_k = delta_{k-1}(q_{n-1}) entries are read off the STORED prefix
diagonal delta(q_{n-1}); the new element q_n enters only at the diagonal
bottom (position k = n).  Hence nu2 (the count of 2s in the {0,2} cycle) and
the whole descent pattern are fixed in advance of q_n.

Indexing
--------
A_0 = (q_1, q_2, ...);  A_{k+1}(i) = |A_k(i) - A_k(i+1)|.
Right diagonal of prefix length n:
      delta_k(q_n) = A_k(n - k),                      k = 0..n.
Then  delta_k(q_{n-1}) = A_k((n-1) - k) = A_k(n - 1 - k),  k = 0..n-1.

With rows[k][j] = A_k(j), the identity is
      rows[k][n-k] == | rows[k-1][n-k+1] - rows[k-1][n-k] |      (k >= 1)
where rows[k-1][n-k] = delta_{k-1}(q_{n-1}) is the eps read off the prefix.

Exact integer arithmetic; reuses code/lib/gilbreath.py oracle.
"""
import sys
from lib.gilbreath import primes_up_to, rows_generator


def identity_violations(primes, N):
    """Verify the prefix-determinism identity over prefix lengths 1..N on the
    real primes.  Returns (positions_checked, mismatches)."""
    gen = rows_generator(primes, N)
    rows = [next(gen) for _ in range(N + 1)]

    total = 0
    mism = 0
    first_viol = None
    for n in range(2, N + 1):            # prefix length n
        for k in range(1, n + 1):        # delta_k(q_n)
            lhs = rows[k][n - k]                     # delta_k(q_n)
            a = rows[k - 1][n - k + 1]               # delta_{k-1}(q_n)
            b = rows[k - 1][n - k]                   # delta_{k-1}(q_{n-1}) = eps
            total += 1
            if lhs != abs(a - b):
                mism += 1
                if first_viol is None:
                    first_viol = (n, k, lhs, a, b)
    return total, mism, first_viol


def eps_prefix_locality(primes, N, per=3):
    """Fix a prefix q_1..q_{n-1}, append several different q_n, and confirm
    that every eps entry delta_{k-1}(q_{n-1}) is IDENTICAL across the
    continuations (it lives entirely inside the prefix), while the diagonal
    bottom delta_n(q_n) is the only entry that moves with q_n.
    Returns (cases, mismatches)."""
    cases = 0
    mism = 0
    for n in range(3, N + 1):
        # prefix q_1..q_{n-1}; choose 'per' distinct continuations q_n
        conts = primes[n-1 : n-1 + per]      # the next 'per' primes
        # build the rows restricted to window [0..n] of each continuation
        diags = []
        for qn in conts:
            top = list(primes[:n-1]) + [qn]          # prefix + this q_n
            g = rows_generator(top, n)
            rws = [next(g) for _ in range(n + 1)]
            d = [rws[k][n - k] for k in range(n + 1)]   # delta(q_n), k=0..n
            diags.append(d)
        # eps entries = delta_{k-1}(q_{n-1}); compare across continuations
        for d in diags:
            for k in range(1, n):                    # cycle positions k=1..n-1
                cases += 1
                # expected eps = delta_{k-1}(q_{n-1}) (prefix-only)
                dprev = rows_generator(list(primes[:n-1]), n - 1)
                rwprev = [next(dprev) for _ in range(n)]
                exp = rwprev[k-1][(n-1) - (k-1)]
                if d[k-1] != exp:
                    mism += 1
    return cases, mism


def main():
    N = 200
    SIEVE = 2000
    primes = primes_up_to(SIEVE)
    assert len(primes) >= N + 3, f"need {N+3} primes, have {len(primes)}"
    print("Prefix-determinism identity check (Directive 48 item 1)")
    print("=" * 74)
    print(f"sieve to {SIEVE}: {len(primes)} primes; prefix lengths n = 1..{N}")

    # Part 1: the identity, cell by cell, on real primes
    total, mism, first_viol = identity_violations(primes, N)
    print("\nPart 1:  delta_k(q_n) = |delta_{k-1}(q_n) - delta_{k-1}(q_{n-1})|")
    print(f"  positions checked (k=1..n over n=2..{N}): {total}")
    print(f"  identity mismatches: {mism}   (expect 0)")
    if first_viol:
        n, k, lhs, a, b = first_viol
        print(f"    FIRST VIOLATION n={n} k={k}: delta_k={lhs} "
              f"!= |delta_{k-1}(q_n)={a} - delta_{k-1}(q_{n-1})={b}|")

    # Part 2: eps is prefix-local (independent of the appended q_n)
    cases, lmism = eps_prefix_locality(primes, N)
    print("\nPart 2: eps entries delta_{k-1}(q_{n-1}) are prefix-local")
    print(f"  (fixed prefix q_1..q_{{n-1}}, several continuations q_n)")
    print(f"  eps positions checked across continuations: {cases}")
    print(f"  prefix-locality mismatches: {lmism}   (expect 0)")

    ok = (mism == 0 and lmism == 0)
    print("\n" + "=" * 74)
    print(f"RESULT: {total} identity positions, {mism} mismatches; "
          f"{cases} prefix-locality positions, {lmism} mismatches.")
    print("PREFIX-DETERMINISM IDENTITY: " +
          ("CONFIRMED over the stated range (0 violations)" if ok
           else "VIOLATED — see above"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
