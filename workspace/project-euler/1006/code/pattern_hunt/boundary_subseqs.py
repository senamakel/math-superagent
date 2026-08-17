"""PE1006: extract Fibonacci-boundary subsequences from computed data.

Structural fact already established by this run (directive-1 route): at
k = F_m - 1 the k+1 factors are exactly the rotations of the truncated
standard word, so Psi(F_m - 1) has a special autocorrelation form.  This
script pulls out the boundary-indexed subsequences from the recorded tables
so the sequence tools can probe them:

  E(m) = Psi(F_m - 1) exact             (from code/out/psi_exact.txt)
  Rm1(m) = Psi(F_m - 1) mod M           (from code/out/psi_residues.txt)
  R0(m)  = Psi(F_m)     mod M
  Rp1(m) = Psi(F_m + 1) mod M

F_1 = 1, F_2 = 2, ... so F_m - 1 for m >= 2 gives k = 1, 2, 4, 7, 12, ...
"""
M = 101001001


def read_pairs(path):
    d = {}
    for line in open(path):
        a, b = line.split()
        d[int(a)] = int(b)
    return d


def fibs_upto(N):
    f = [1, 2]
    while f[-1] <= N:
        f.append(f[-1] + f[-2])
    return f


def main():
    exact = read_pairs('code/out/psi_exact.txt')
    res = read_pairs('code/out/psi_residues.txt')
    fibs = fibs_upto(400)
    print("Fibonacci numbers (F_1=1,F_2=2, up to 400):", fibs)

    print("\nExact Psi at k = F_m - 1 (m such that F_m - 1 <= 25):")
    e = []
    for f in fibs:
        k = f - 1
        if k in exact:
            e.append((f, exact[k]))
    for f, v in e:
        print(f"  m: F_m={f:<3d} k={f-1:<3d} Psi = {v}")
    print("as sequence:",
          ", ".join(str(v) for _, v in e))

    print("\nResidues mod M at k = F_m - 1, F_m, F_m + 1 (k <= 400):")
    for label, off in [("F_m - 1", -1), ("F_m", 0), ("F_m + 1", +1)]:
        seq = [(f + off, res[f + off]) for f in fibs if (f + off) in res]
        print(f"  {label}: {[v for _, v in seq]}")
        print(f"    k-values: {[k for k, _ in seq]}")

    # first differences of the boundary residue sequences, for completeness
    for label, off in [("F_m - 1", -1), ("F_m", 0), ("F_m + 1", +1)]:
        seq = [res[f + off] for f in fibs if (f + off) in res]
        diffs = [(seq[i + 1] - seq[i]) % M for i in range(len(seq) - 1)]
        print(f"  first differences (mod M) of {label}: {diffs}")


if __name__ == '__main__':
    main()