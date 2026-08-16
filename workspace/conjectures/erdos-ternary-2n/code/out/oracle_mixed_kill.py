"""Independent brute-force oracle for the mixed-modulus sieve KILL cases.

Materialises 2^r as a big integer (small r only) and checks both conditions
directly, confirming the "KILL" flags the sieve reported.  This is a bounded
verification of q=19 k=3,4 (the only cases where mixed < 2^(k-1)).
"""


def to_base_digits(m, base):
    if m == 0:
        return [0]
    out = []
    while m > 0:
        out.append(m % base)
        m //= base
    return out  # least significant first


def check(q, k):
    m = 3 ** k
    l = 2 * 3 ** (k - 1)
    from sympy.ntheory import n_order
    N = __import__("math").lcm(l, n_order(2, q))
    D = {0}
    for i in range(k):
        p = pow(3, i, q)
        D |= {(d + p) % q for d in list(D)}
    pure = []
    for r in range(N):
        val = 2 ** r                     # big int, but r small here
        digs = to_base_digits(val % m, 3)
        if all(d <= 1 for d in digs):
            if pow(2, r, q) in D:
                pure.append((r, True))
            else:
                pure.append((r, False))
    mixed = sum(1 for _, ok in pure if ok)
    classes = 2 ** (k - 1)
    # which classes (r mod l) are fully killed?
    from collections import defaultdict
    per_class = defaultdict(list)
    for r, ok in pure:
        per_class[r % l].append(ok)
    killed = [c for c, has in per_class.items() if not any(has)]
    print(f"q={q} k={k}: N={N}  pure={len(pure)}  classes={classes}  "
          f"mixed={mixed}  killed_classes={len(killed)}")
    for c in killed:
        r0 = min(r for r, ok in pure if r % l == c)
        print(f"    class r ≡ {c} (mod {l}) fully killed; e.g. r={r0}: "
              f"2^{r0}={2**r0}, low {k} ternary digits of 2^{r0} "
              f"(mod {m}) in {{0,1}}? yes; 2^{r0} mod {q}="
              f"{pow(2, r0, q)} in D? no")


if __name__ == "__main__":
    check(19, 3)
    check(19, 4)
