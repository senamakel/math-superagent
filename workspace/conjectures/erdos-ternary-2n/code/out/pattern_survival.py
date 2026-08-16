"""Survival-depth sequence f(n) = least base-3 digit position (LSB-first,
0-indexed) where 2^n first shows a digit 2.

n in A_k  (survives the sieve to level k)  <=>  low k ternary digits of 2^n
avoid 2  <=>  f(n) >= k.  So f(n) is the survival depth of n in the residue
sieve: 0,2,8 are digit-free, f = +infinity.

Oracle: direct big-int digit scan (independent of the modular machinery).
"""

def f_of_n(n):
    """Least i >= 0 with the i-th base-3 digit of 2^n equal to 2, LSB-first.
    Returns None if 2^n is digit-{0,1}-free (i.e. n in {0,2,8}, conjecturally)."""
    m = 2 ** n
    i = 0
    while m > 0:
        if m % 3 == 2:
            return i
        m //= 3
        i += 1
    return None  # digit-free


def main():
    N = 400
    seq = []
    surv_depth = {}   # f(n) -> count, f=None treated separately
    free = []
    for n in range(0, N):
        f = f_of_n(n)
        if f is None:
            free.append(n)
        else:
            seq.append((n, f))
            surv_depth[f] = surv_depth.get(f, 0) + 1
    # print f(n) in order n=0..N-1, with '.' for digit-free
    vals = []
    for n in range(N):
        f = f_of_n(n)
        vals.append('inf' if f is None else f)
    print(f"=== f(n) for n=0..{N-1} ('.' not used; 'inf'=digit-free) ===")
    print([v for v in vals])
    print()
    print(f"digit-free n (f=inf) in [0,{N-1}]: {free}")
    print(f"count of digit-free: {len(free)}")
    print()
    print("=== distribution of f over digit-containing n in[0,%d] ===" % (N-1))
    for k in sorted(surv_depth):
        print(f"f={k}: {surv_depth[k]}")
    print()
    # The raw integer sequence f(n) for the tools (skip the three digit-free).
    raw = []
    for n in range(N):
        f = f_of_n(n)
        if f is not None:
            raw.append(f)
    print("=== f(n) raw integer sequence, n ascending, digit-free omitted ===")
    print(raw)


if __name__ == "__main__":
    main()
