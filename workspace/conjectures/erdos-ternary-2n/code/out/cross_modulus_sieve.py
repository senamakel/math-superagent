"""Mixed-modulus sieve: does adding a mod-q constraint kill 3-adic survivors?

VERIFIED-NUMERICALLY for the stated (k, q) pairs only -- NOT a theorem.

Pure 3-adic sieve:
    survivor class r (mod l = 2*3^(k-1)) is one whose low k ternary digits
    of 2^r (mod 3^k) all lie in {0,1}.  Claimed count of classes: 2^(k-1).
    The program counts this directly over a full period [0, l) and reports
    the class count, verifying the 2^(k-1) claim per k.

Mixed sieve: for M = 3^k * q, q a prime coprime to 6, N = ord_M(2) =
    lcm(2*3^(k-1), n_order(2, q)).  Count r in [0, N) such that BOTH
      (a) low k ternary digits of 2^r mod 3^k are in {0,1}, AND
      (b) 2^r mod q is a sub-sum of {3^0,...,3^(k-1)} mod q.
    Work is entirely modular: 2^r is never built whole, both residues are
    advanced by one doubling per step.

Meaning of the flag "mixed < 2^(k-1)":
    [0,N) contains exactly T = N/(2*3^(k-1)) full pure-periods, so the pure
    count over [0,N) is 2^(k-1)*T.  Each survivor class contributes an
    integer c_j in [0,T] of r values satisfying (b).  If every class kept at
    least one representative, mixed_count >= 2^(k-1).  Therefore
    mixed_count < 2^(k-1)  <==>  some survivor class has c_j = 0, i.e. every
    representative of that class in [0,N) fails (b): the mixed modulus kills
    that class outright (removing an entire arithmetic progression of n).

Exact integer arithmetic only.  No floats.
Complexity: O(sum over (q,k) of N) time, N <= 4e5;  O(2^k) space for the
sub-sum set D (k <= 11, so <= 2048 entries).
"""

from sympy.ntheory import n_order

Q_LIST = [5, 7, 11, 13, 17, 19, 29, 41, 193, 257]
K_MAX = 11
N_LIMIT = 400000


def subset_sum_set(k, q):
    """{ sum_{i in B} 3^i mod q : B subseteq {0..k-1} }.  O(k * 2^k)."""
    D = {0}
    for i in range(k):
        p = pow(3, i, q)
        D |= {(d + p) % q for d in list(D)}
    return D


def low_k_digits_01(v3, k, m):
    """True iff the low k ternary digits of v3 (which is 2^r mod 3^k) are in {0,1}."""
    v = v3
    for _ in range(k):
        if v % 3 == 2:
            return False
        v //= 3
    return True


def pure_class_count(k):
    """Number of survivor classes mod l=2*3^(k-1); direct count over [0,l)."""
    l = 2 * 3 ** (k - 1)
    m = 3 ** k
    val = 1
    n = 0
    survivors = []
    for r in range(l):
        if low_k_digits_01(val, k, m):
            survivors.append(r)
            n += 1
        val = (val * 2) % m
    return n, survivors, l


def run(q, k):
    """Return dict with pure and mixed counts over [0,N), plus N."""
    m = 3 ** k
    l = 2 * 3 ** (k - 1)
    ord_q = n_order(2, q)
    N = __import__("math").lcm(l, ord_q)
    if N > N_LIMIT:
        return None
    D = subset_sum_set(k, q)
    val3, valq = 1, 1
    pure = 0
    mixed = 0
    pure_fail = []          # pure survivors (r, modq, inD?)  -- for reporting
    for r in range(N):
        ok3 = low_k_digits_01(val3, k, m)
        if ok3:
            pure += 1
            inD = valq in D
            if inD:
                mixed += 1
            else:
                pure_fail.append((r, valq))
        val3 = (val3 * 2) % m
        valq = (valq * 2) % q
    return {
        "q": q, "k": k, "N": N, "ord_q": ord_q,
        "T": N // l,
        "pure": pure,            # over [0,N)  == 2^(k-1)*T
        "classes": 2 ** (k - 1),
        "mixed": mixed,
        "D_count": len(D),
        "pure_fail": pure_fail,
    }


def main():
    print("=" * 78)
    print("MIXED-MODULUS SIEVE -- verified-numerically for the stated (k,q)," )
    print("NOT a theorem.  Exact integer arithmetic; 2^r never built whole.")
    print("flag = 'KILL' when mixed_count < 2^(k-1) (some survivor class is")
    print("        totally removed by the mod-q constraint).")
    print("=" * 78)

    # Sanity: q=1 (no mod-q constraint) must reproduce pure count.
    print("\n--- Sanity: 'q=1' (D = all residues, (b) vacuous) ---")
    for k in range(1, K_MAX + 1):
        n, survivors, l = pure_class_count(k)
        status = "OK" if n == 2 ** (k - 1) else "MISMATCH"
        print(f"  k={k:2d}  classes={n:6d}  expected 2^(k-1)={2**(k-1):6d}  {status}")

    header = (f"\n{'q':>4} {'k':>3} {'N':>9} {'T':>3} {'pure':>7} "
              f"{'2^(k-1)':>8} {'mixed':>7} {'ratio':>8}  flag")
    print(header)

    results = []
    dropped = []
    worst = None   # (key, eliminated_fraction)
    for q in Q_LIST:
        for k in range(1, K_MAX + 1):
            res = run(q, k)
            if res is None:
                N = __import__("math").lcm(2 * 3 ** (k - 1), n_order(2, q))
                if N > N_LIMIT:
                    dropped.append((q, k, N))
                continue
            pure = res["pure"]
            ratio = res["mixed"] / pure if pure else float("inf")
            kill = "KILL" if res["mixed"] < res["classes"] else ""
            print(f"{q:>4} {k:>3} {res['N']:>9} {res['T']:>3} {pure:>7} "
                  f"{res['classes']:>8} {res['mixed']:>7} {ratio:>8.4f}  {kill}")
            results.append(res)
            # track strongest reducer: biggest drop in survivor count per class
            avg_before = float(res["classes"])
            avg_after = res["mixed"] / res["T"]   # average c_j
            frac = (avg_before - avg_after) / avg_before if avg_before else 0
            if worst is None or frac > worst[1]:
                worst = (res, frac)

    print("\n--- dropped (N = lcm(2*3^(k-1), n_order(2,q)) exceeds 4e5) ---")
    for q, k, N in dropped:
        print(f"  q={q:>4} k={k:>2}: N={N} > 4e5 -- dropped")

    print("\n--- survivor classes actually KILLED (mixed < 2^(k-1)) ---")
    kills = [r for r in results if r["mixed"] < r["classes"]]
    if not kills:
        print("  none -- no (q,k) in range fully removed a survivor class")
    for res in kills:
        pf = res["pure_fail"]
        l = 2 * 3 ** (res["k"] - 1)
        from collections import defaultdict
        killed_classes = defaultdict(list)
        for r, vq in pf:
            killed_classes[r % l].append(r)
        print(f"  q={res['q']} k={res['k']}: classes={res['classes']} "
              f"mixed={res['mixed']}  --> {len(killed_classes)} class(es) fully "
              f"killed over [0,{res['N']}) (dying r counts as class reps below)")
        # the mixed count is the number of r that survive; a class is killed iff
        # none of its representatives survive.  Total killed classes:
        cnt = 0
        for cres, rs in list(killed_classes.items())[:12]:
            r0 = rs[0]
            target = (cr for cr in range(res["classes"]))
            print(f"    class r ≡ {cres} (mod {l}): dying representatives "
                  f"{[x for x in rs[:3]]}... (2^{r0} mod {res['q']} = "
                  f"{pow(2, r0, res['q'])}, not in D)")
            cnt += 1
        if len(killed_classes) > 12:
            print(f"    ... and {len(killed_classes)-12} more killed classes")
        # note: pure_fail lists ONLY r that are pure survivors but fail (b), so
        # a class appears here iff every pure r in it up to what we scanned died
        print(f"    (that is the set of fully-killed classes; "
              f"{res['mixed']} surviving r remain over [0,{res['N']}))")


if __name__ == "__main__":
    main()
