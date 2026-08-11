"""Task 2: probe record b's for |b*sqrt(d)-pi|_Z (distance to nearest integer).

For each d in {2,3,5,6,7,8,10,...}, scan b in [0,N] and record the b's that
achieve a NEW strict minimum of distance(b*sqrt(d), pi) to nearest integer.
Report first ~30 record b's and whether each is a semiconvergent denominator
of sqrt(d) (exact integer continued fraction).

A semiconvergent denominator of sqrt(d) is any m*q_k + q_{k-1} for
0<=m<=a_{k+1}, where q_k are convergent denominators and a_j the partial
quotients of sqrt(d)'s CF.

Uses exact integer arithmetic; only the final float distance is float.
"""
import sympy as sp
from sympy import continued_fraction_periodic, continued_fraction_convergents

pi = 3.14159265358979323846264338327950288419716939937510  # high precision


def cf_of_sqrt(d, max_terms=1000):
    """Return partial quotients (list of ints) of sqrt(d) CF."""
    try:
        res = continued_fraction_periodic(0, 1, d)
    except Exception:
        return None
    # res is [a0, [period...]]  e.g. [1, [2]]
    a0 = res[0]
    period = list(res[1])
    seq = [a0] + period[:max_terms]
    return seq


def semiconvergent_denoms(d, N):
    """Set of semiconvergent denominators of sqrt(d) up to N (exact ints)."""
    a = cf_of_sqrt(d)
    if a is None:
        return None
    # convergents denominators via recurrence
    q_2, q_1 = 0, 1  # q_{-2}=0, q_{-1}=1
    denoms = set()
    # need a_{k+1} for each step -> pad
    for k in range(len(a) - 1):
        ak = a[k]
        qk = ak * q_1 + q_2
        # semiconvergents between q_{k-1} and q_{k+1}: m*q_k + q_{k-1}, 0<=m<=a_{k+1}
        qkm1 = q_1          # q_{k-1}
        qkplus = a[k+1] * qk + qkm1  # q_{k+1}
        m = 0
        while True:
            s = m * qk + qkm1
            if s > N:
                break
            denoms.add(s)
            m += 1
            if s >= qkplus:  # reached the next convergent; enough
                break
        q_2, q_1 = q_1, qk
    return denoms


def record_bs(d, N):
    """Scan b in [0,N], return list of (b, err) achieving new strict minima."""
    sd = d ** 0.5
    best = float('inf')
    recs = []
    for b in range(0, N + 1):
        v = b * sd - pi
        r = round(v)
        err = abs(v - r)
        if err < best - 1e-18:
            best = err
            recs.append((b, err))
    return recs


def main():
    ds = [2, 3, 5, 6, 7, 8, 10, 11, 13]
    N = 2_000_000
    for d in ds:
        recs = record_bs(d, N)
        semis = semiconvergent_denoms(d, N)
        print(f"=== d={d}  (scan N={N}) ===")
        print(f"  CF of sqrt({d}): {cf_of_sqrt(d)[:16]}")
        print("  first 30 records:")
        for (b, err) in recs[:30]:
            is_semi = b in semis
            print(f"    b={b:10d}  err={err:.6e}  semiconvergent={is_semi}")
        in_semi = sum(1 for b, _ in recs if b in semis)
        print(f"  records in first 30 that are semiconvergents: {in_semi}/30")
        # also check ALL records are semiconvergents
        allok = all(b in semis for b, _ in recs)
        print(f"  ALL {len(recs)} records are semiconvergents: {allok}")
        print()


if __name__ == "__main__":
    main()
