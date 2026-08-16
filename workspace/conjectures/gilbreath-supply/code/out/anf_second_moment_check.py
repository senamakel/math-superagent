"""Check the exact Phi-alone second-moment identity behind the adopted repoint.

Claim (deduction): with S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)} and eps_d = (-1)^{T(n,d)},
for iid Bernoulli(p) input h we have

    E[S(n)^2] = (n-2) + sum_{d != d'} (1-2p)^{|M_d XOR M_{d'}|}

where M_d = row d of Phi_n = the translated digital down-set {n-1-d+o : o subseteq d},
so |M_d| = 2^{popcount(d)}. We verify (a) the row-weight formula |M_d| = 2^{popcount(d)}
and (b) the second-moment formula against a direct Monte-Carlo / exhaustive-in-small-n
computation.

This is a CHECK of the identity, not a proof of anything about the primes.
"""
from collections import Counter


def popcount(x):
    return bin(x).count("1")


def submask_row(n, d):
    """Row d of Phi_n: positions j with (j - (n-1-d)) a submask of d."""
    row = set()
    for j in range(n):
        o = j - (n - 1 - d)
        if 0 <= o <= d and (o & ~d) == 0:
            row.add(j)
    return row


def xor_weight(n, d1, d2):
    r1 = submask_row(n, d1)
    r2 = submask_row(n, d2)
    return len(r1 ^ r2)


def second_moment_formula(n, p):
    """E[S(n)^2] = (n-2) + sum_{d != d'} (1-2p)^{|M_d XOR M_{d'}|}."""
    total = n - 2
    q = 1 - 2 * p
    for d1 in range(2, n):
        for d2 in range(2, n):
            if d1 != d2:
                total += q ** xor_weight(n, d1, d2)
    return total


def second_moment_direct(n, p):
    """Direct: enumerate over the full Phi_n kernel? No - over all 2^n inputs for small n,
    compute S(n) = sum_d (-1)^{T(n,d)} exactly and average S^2 over iid Bernoulli(p) h."""
    rows = [submask_row(n, d) for d in range(2, n)]
    total = 0.0
    prob_cache = {}
    for mask in range(1 << n):
        prob = 1.0
        for j in range(n):
            bit = (mask >> j) & 1
            prob *= p if bit else (1 - p)
        # S(n) = sum_d eps_d, eps_d = (-1)^{T(n,d)}
        S = 0
        for row in rows:
            t = sum(1 for j in row if (mask >> j) & 1) & 1
            S += -1 if t else 1
        total += prob * S * S
    return total


if __name__ == "__main__":
    # (a) row weight = 2^popcount(d)
    print("(a) |M_d| = 2^popcount(d):")
    ok = True
    for n in (8, 12):
        for d in range(2, n):
            w = len(submask_row(n, d))
            expect = 2 ** popcount(d)
            if w != expect:
                ok = False
                print(f"  MISMATCH n={n} d={d}: {w} vs {expect}")
    print("  all match" if ok else "  FAILED")

    # (b) second-moment formula vs direct, small n
    print("(b) E[S(n)^2] formula vs direct enumeration:")
    for n in (4, 5, 6):
        for p in (0.5, 0.585, 0.3):
            f = second_moment_formula(n, p)
            d = second_moment_direct(n, p)
            print(f"  n={n} p={p}: formula={f:.6f} direct={d:.6f}  "
                  f"{'OK' if abs(f-d) < 1e-9 else 'MISMATCH'}")

    # (c) growth of E[S^2]/n for p=0.585 up to n where feasible
    print("(c) E[S(n)^2]/n (should be O(1) for p bounded away from 0,1):")
    for n in (8, 16, 32, 64):
        f = second_moment_formula(n, 0.585)
        print(f"  n={n}: E[S^2]={f:.2f}  E[S^2]/n={f/n:.3f}")
