"""PE1006 pattern hunt: produce the integer sequences the run cares about.

Sequences written to code/out/:

  psi_residues.txt  : k, Psi(k) mod M  for k = 1..KMAX        (M = 101001001;
                       this is the quantity the problem asks for at k = 10^18)
  psi_exact.txt     : k, Psi(k) exact for k = 1..KEXACT       (big-int)
  lmin.txt          : k, Lmin(k) = minimal prefix length of the infinite
                       Fibonacci word containing all k+1 distinct length-k
                       factors
  counts.txt        : verification that every length-k factor harvest has
                       exactly k+1 distinct factors, and that a longer prefix
                       (3.5k+20) adds no new factors on a probe set of k.

Representation: the word prefix is a big int, bit (k-1-j) of a length-k factor
being digit j of the string, so the decimal value of factor f is
sum_{t in bits(f)} 10^t  (t counted from the rightmost digit).  This is exact
integer arithmetic; mod-M values use precomputed powers of 10.
"""

M = 101001001


def fib_prefix(L):
    """Return a prefix of the infinite Fibonacci word of length >= L."""
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def value_exact(f):
    """Decimal value of binary string whose integer form is f."""
    v = 0
    pw = 1
    while f:
        if f & 1:
            v += pw
        pw *= 10
        f >>= 1
    return v


def main():
    KMAX = 400
    KEXACT = 25
    L = 3 * KMAX + 5
    W = fib_prefix(L)
    WI = int(W, 2)
    assert len(W) >= L
    Ltot = len(W)

    pow10mod = [1] * (Ltot + 1)
    for t in range(1, Ltot + 1):
        pow10mod[t] = pow10mod[t - 1] * 10 % M

    def factor_int(i, k):
        # substring W[i:i+k] as an integer (leftmost char = MSB of length-k)
        return (WI >> (Ltot - k - i)) & ((1 << k) - 1)

    def value_mod(f):
        s = 0
        while f:
            t = (f & -f).bit_length() - 1
            s += pow10mod[t]
            f &= f - 1
        return s % M

    res, lmin, exact, counts = [], [], [], []
    probe_oks = []
    for k in range(1, KMAX + 1):
        n = Ltot - k + 1
        seen = set()
        for i in range(n):
            seen.add(factor_int(i, k))
            if len(seen) == k + 1:
                if lmin is not None and len(lmin) < k:
                    pass
        # full harvest
        seen = {factor_int(i, k) for i in range(n)}
        counts.append((k, len(seen)))
        if len(seen) != k + 1:
            print(f"!!! count mismatch k={k}: {len(seen)} != {k+1}")
        # minimal prefix length (fresh scan)
        s = set()
        lmin_k = None
        for i in range(n):
            s.add(factor_int(i, k))
            if len(s) == k + 1:
                lmin_k = i + k
                break
        lmin.append((k, lmin_k))
        # residue
        ssum = 0
        for f in seen:
            ssum = (ssum + value_mod(f) * value_mod(f)) % M
        res.append((k, ssum))
        if k <= KEXACT:
            exact.append((k, sum(value_exact(f) ** 2 for f in seen)))
        # stability probe: longer prefix must add nothing
        if k <= 60 or k % 25 == 0:
            Lp = 7 * k // 2 + 20
            if Lp <= Ltot:
                seen2 = {factor_int(i, k) for i in range(Lp - k + 1)}
                probe_oks.append((k, seen2 == seen))
                if seen2 != seen:
                    print(f"!!! stability fail k={k}: prefix {Lp} != prefix {Ltot}")

    with open('code/out/psi_residues.txt', 'w') as fh:
        for k, r in res:
            fh.write(f"{k} {r}\n")
    with open('code/out/psi_exact.txt', 'w') as fh:
        for k, v in exact:
            fh.write(f"{k} {v}\n")
    with open('code/out/lmin.txt', 'w') as fh:
        for k, v in lmin:
            fh.write(f"{k} {v}\n")
    with open('code/out/counts.txt', 'w') as fh:
        for k, c in counts:
            fh.write(f"{k} {c} {'OK' if c == k + 1 else 'MISMATCH'}\n")

    print(f"KMAX={KMAX} Ltot={Ltot}")
    print(f"count mismatches: {sum(1 for k, c in counts if c != k + 1)}")
    print(f"stability probes run: {len(probe_oks)}, "
          f"failures: {sum(1 for k, ok in probe_oks if not ok)}")
    print("first 15 residues:", [r for _, r in res[:15]])
    print("last 5 residues:", [r for _, r in res[-5:]])
    print("first 15 lmin:", [v for _, v in lmin[:15]])
    print("exact Psi(1..10):", [v for _, v in exact[:10]])


if __name__ == '__main__':
    main()