"""Count exponent signatures (e1>=e2>=...>=er>=1) whose minimal prime
assignment prod_i p_i^e_i <= 10^18, where p_i is the i-th prime.

This is a partition-count over the shape (a bounded integer-partition
problem constrained by the product of smallest primes), i.e. a structural
parameter of the signature-first method, NOT an enumeration of the answer
space up to 10^18. It tests the feasibility claim in
research/approaches/exponent-signature-first.md.
"""
from sympy import primerange

LIMIT = 10**18
# enough primes: r cannot exceed log_2(LIMIT) ~ 60, so 30 primes suffice
PRIMES = list(primerange(2, 200))  # 46 primes


def count_signatures(limit):
    count = 0
    siglist = []

    def dfs(idx, max_exp, n, sig):
        nonlocal count
        p = PRIMES[idx]
        pk = p
        e = 1
        extended = False
        while e <= max_exp and n * pk <= limit:
            extended = True
            sig.append(e)
            dfs(idx + 1, e, n * pk, sig)
            sig.pop()
            e += 1
            pk *= p
        if not extended:
            # leaf: a completed exponent signature
            count += 1
            siglist.append(tuple(sig))

    dfs(0, 64, 1, [])
    return count, siglist


def main():
    for L in (10**6, 10**10, 10**14, 10**18):
        c, _ = count_signatures(L)
        print(f"LIMIT {L}: {c} feasible exponent signatures")

    c, sl = count_signatures(10**18)
    # distribution by number of distinct primes
    from collections import Counter
    dist = Counter(len(s) for s in sl)
    print("signature count by number of distinct primes r (at 1e18):")
    for r in sorted(dist):
        print(f"  r={r}: {dist[r]}")


if __name__ == "__main__":
    main()
