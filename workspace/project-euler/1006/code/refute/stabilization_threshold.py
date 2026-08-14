"""Refute test: G-stabilization candidate threshold n0(k) = smallest n with |S_{n-1}| >= k.

For each k, the claim's first-step candidate says the length-k factor set of S_n
stabilizes for all n >= n0(k) (with n0(k)=smallest n satisfying |S_{n-1}| >= k),
equalling the factor set of the infinite Fibonacci word f and having size k+1.

We test the minimal requirement: does S_{n0(k)} already contain all k+1
distinct length-k factors of f (i.e. does its factor set have size k+1)?

If not, the candidate threshold is too small and the claim as stated (that this
n0 is a stabilization threshold) is FALSE.
"""


def S(n):
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def wl(n):
    a, b = 1, 2
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factor_set(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def candidate_n0(k):
    n = 1
    while wl(n - 1) < k:
        n += 1
    return n


def empirical_stable_n0(k, NMAX=40):
    """smallest n with |factor set of S_n| == k+1 (i.e. already full)."""
    for n in range(2, NMAX + 1):
        if len(factor_set(S(n), k)) == k + 1:
            return n
    return None


def main():
    print("k : cand_n0 : stable_n0 : S_{cand} full (size==k+1)?")
    bad = 0
    for k in range(1, 41):
        c = candidate_n0(k)
        e = empirical_stable_n0(k)
        have = len(factor_set(S(c), k))
        ok = (have == k + 1)
        if not ok:
            bad += 1
        print(f"{k:2d} : {c:2d} : {e:2d} : full={ok}  (S_{{n0}} has {have}/{k+1} factors)")
    print()
    print("candidate threshold too small (already fails to be full) for", bad, "of 40 k-values")


if __name__ == "__main__":
    main()
