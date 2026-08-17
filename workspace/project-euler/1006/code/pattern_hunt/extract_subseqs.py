"""PE1006: extract structurally meaningful subsequences from already-computed
data and probe them for regularity.

Reads code/out/psi_residues.txt (Psi(k) mod 101001001, k=1..400) and
code/out/psi_exact.txt (Psi(k) exact, k=1..25).

Subsequences probed:
  A(k) = Psi(k) mod M at k = F_m - 1   (directive 1: factors are rotations
         of the truncated standard word)
  B(k) = Psi(k) mod M at k = F_m
  C(k) = Psi(k) mod M at k = F_m + 1
  plus the counts of factors starting with '1' (leading nonzero) among the
  k+1 factors -- recomputed from the word.
"""

import re

M = 101001001


def read_pairs(path):
    out = []
    with open(path) as fh:
        for line in fh:
            a, b = line.split()
            out.append((int(a), int(b)))
    return out


def fibs_upto(N):
    f = [2, 3]
    while f[-1] < N:
        f.append(f[-1] + f[-2])
    return f


def leading_ones_counts(kmax, word):
    """Among the k+1 distinct length-k factors, count those starting with '1'."""
    res = {}
    n = len(word)
    for k in range(1, kmax + 1):
        facs = set()
        for i in range(n - k + 1):
            facs.add(word[i:i + k])
        res[k] = sum(1 for w in facs if w[0] == '1')
    return res


def main():
    res = read_pairs('code/out/psi_residues.txt')
    exact = read_pairs('code/out/psi_exact.txt')
    byk = dict(res)
    byk_exact = dict(exact)

    fibs = fibs_upto(400)
    print("F_m list (<=400):", fibs)

    for label, off in [("F_m - 1", -1), ("F_m", 0), ("F_m + 1", +1)]:
        sub = [(k, byk[k]) for k in (f + off for f in fibs) if k in byk]
        print(f"\nPsi mod M at k = {label}:  (k, residue)")
        print("  ", sub)

    # exact values at F_m - 1 where available
    subex = [(k, byk_exact[k]) for k in (f - 1 for f in fibs) if k in byk_exact]
    print("\nPsi exact at k = F_m - 1 (k<=25):")
    for k, v in subex:
        print(f"  k={k:3d}  Psi={v}")

    # leading-one counts: need the word; Q: do we still have one built? build again.
    a, b = '0', '01'
    while len(b) < 900:
        a, b = b, b + a
    W = b
    loc = leading_ones_counts(60, W)
    print("\nfactors starting with '1' among the k+1 distinct length-k factors,")
    print("k=1..60, as (count, k+1-count):")
    print("  ", [(k, loc[k]) for k in range(1, 61)])


if __name__ == '__main__':
    main()