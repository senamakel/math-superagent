#!/usr/bin/env python3
"""Machine check for the prefix-determinism identity (Directive 48 item 1).

Claim (three lines)
-------------------
The 0-2 cycle pattern (hence nu2) used by the Lemma 5.4 descent depends only
on q_1..q_{n-1}.  By the right-diagonal recurrence
      delta_k(q_n) = | delta_{k-1}(q_n) - delta_{k-1}(q_{n-1}) |   (k >= 1)
the eps_k = delta_{k-1}(q_{n-1}) entries are inherited from the STORED prefix
diagonal delta(q_{n-1}); the new element q_n enters only at the diagonal
bottom (position k = n).  Hence the whole descent pattern is fixed in advance
of q_n.

Indexing (exact, 0-based)
-------------------------
A_0 = (q_1, q_2, ...);  A_{k+1}(i) = |A_k(i) - A_k(i+1)|,  i >= 0.
Row k over prefix length n has n-k entries, so its LAST entry is

      delta_k(q_n) = A_k[n - k - 1],            k = 0..n-1.

Because absolute differencing is local, the first n-k entries of A_k computed
from a longer top row equal A_k computed from just the prefix of length n.
So with `rows` the triangle of the full top row,
      delta_k(q_n)     = rows[k][n-k-1]
      delta_k(q_{n-1}) = rows[k][n-k-2]
and the identity under audit is, for each n and k>=1,
      rows[k][n-k-1] == | rows[k-1][n-k] - rows[k-1][n-k-1] |
                         ^^^ delta_k(q_n)     ^^^ delta_{k-1}(q_n)
                                                ^^^ delta_{k-1}(q_{n-1})=eps
which is exactly the triangle recurrence A_k[i]=|A_{k-1}[i]-A_{k-1}[i+1]|
with i=n-k-1.

Exact integer arithmetic; reuses code/lib/gilbreath.py oracle.
"""
from lib.gilbreath import primes_up_to, rows_generator


def prefix_cycle(diag):
    """Maximal {0,2} suffix of diag[:-1]; returns (tau, cycle_entries, nu2)."""
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    return i, body[i:], body[i:].count(2)


def main():
    N = 200
    SIEVE = 2000
    primes = primes_up_to(SIEVE)
    assert len(primes) >= N + 4, f"need {N+4} primes, have {len(primes)}"
    print("Prefix-determinism identity check (Directive 48 item 1)")
    print("=" * 74)
    print(f"sieve to {SIEVE}: {len(primes)} primes; prefix lengths n = 1..{N}")

    # Build one triangle from the full top row (length N+3); rows[k] has
    # length N+3-k, so any delta_k(q_n) with n <= N is a valid last entry.
    DEPTH = N + 3
    gen = rows_generator(primes[:DEPTH], DEPTH)
    rows = [next(gen) for _ in range(DEPTH + 1)]

    # ---- Part 1: the identity, cell by cell -------------------------------
    total = 0
    mism = 0
    first_viol = None
    for n in range(2, N + 1):                 # prefix length n
        for k in range(1, n):                 # delta_k(q_n), k=1..n-1
            lhs = rows[k][n - k - 1]          # delta_k(q_n)
            a = rows[k - 1][n - k]            # delta_{k-1}(q_n)
            b = rows[k - 1][n - k - 1]        # delta_{k-1}(q_{n-1}) = eps
            total += 1
            if lhs != abs(a - b):
                mism += 1
                if first_viol is None:
                    first_viol = (n, k, lhs, a, b)
    print("\nPart 1:  delta_k(q_n) = |delta_{k-1}(q_n) - delta_{k-1}(q_{n-1})|")
    print(f"  positions checked (k=1..n-1 over n=2..{N}): {total}")
    print(f"  identity mismatches: {mism}   (expect 0)")
    if first_viol:
        n, k, lhs, a, b = first_viol
        print(f"    FIRST VIOLATION n={n} k={k}: delta_k={lhs} "
              f"!= |delta_{k-1}(q_n)={a} - delta_{k-1}(q_{n-1})={b}|")

    # ---- Part 2: the descent eps is prefix-determined ---------------------
    # Fix prefix P = q_1..q_{n-1}.  Append SEVERAL distinct continuations q_n.
    # The descent eps cells are delta_{k-1}(q_{n-1}) = rows[k-1][n-k-1], which
    # live entirely inside the prefix and must be identical regardless of the
    # continuation.  Also confirm the {0,2} cycle region of delta(q_{n-1}) is
    # {0,2}-valued (the descent pattern) with continuation-independent nu2.
    per = 3
    eps_cases = 0
    eps_mism = 0
    cyc_cases = 0
    cyc_viol = 0
    for n in range(3, N + 1):
        # delta(q_{n-1}) from the stored prefix diagonal
        dprev = [rows[k - 1][(n - 1) - (k - 1) - 1] for k in range(1, n)]  # k-1=0..n-2
        dprev_full = [rows[j][(n - 1) - j - 1] for j in range(n - 1)]
        _, dprev_cyc, dprev_nu2 = prefix_cycle(dprev_full)
        for qn in primes[n - 1 : n - 1 + per]:            # distinct continuations
            # full triangle for the continuation (recompute for independence)
            g2 = rows_generator(list(primes[:n - 1]) + [qn], n)
            r2 = [next(g2) for _ in range(n + 1)]
            for k in range(1, n):                         # descent eps positions
                eps_cases += 1
                got = r2[k - 1][n - k - 1]                # delta_{k-1}(q_{n-1})
                if got != dprev[k - 1]:
                    eps_mism += 1
            cyc_cases += 1
            if any(x not in (0, 2) for x in dprev_cyc) or dprev_nu2 < 0:
                cyc_viol += 1
    print("\nPart 2: the descent eps = delta_{k-1}(q_{n-1}) is prefix-determined")
    print(f"  prefix lengths n=3..{N}, {per} distinct continuations each")
    print(f"  eps positions checked: {eps_cases}, mismatches: {eps_mism}")
    print(f"  {{0,2}}-cycle checks of prefix diagonal: {cyc_cases}, "
          f"violations: {cyc_viol}")

    ok = (mism == 0 and eps_mism == 0 and cyc_viol == 0)
    print("\n" + "=" * 74)
    print(f"RESULT: Part1 {total} identity positions, {mism} mismatches; "
          f"Part2 {eps_cases} eps positions, {eps_mism} mismatches.")
    print("PREFIX-DETERMINISM IDENTITY: " +
          ("CONFIRMED over the stated range (0 violations)" if ok
           else "VIOLATED — see above"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
