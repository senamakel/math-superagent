"""PE1006 pattern hunt, cycle 3c: pair-correlation Toeplitz defect, full scan.

C(i,j) = #{ length-k factors w : w_i = w_j = '1' } (1-indexed positions).
Toeplitz defect d(i,j) = C(i,j) - C(i-1,j-1) for 2<=i,j<=k.

Claims to verify EXACTLY for k = 1..400:
  (a) every nonzero defect has |d| = 1   (never |d| >= 2)
  (b) which k have a fully-Toeplitz matrix (all defects zero):
      expected exactly k = F_n - 1 (Fibonacci minus one) plus the small k.
  (c) how many nonzero defect cells there are, as a function of k
      (record it as a sequence for later analysis).
"""
M = 101001001


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def fibs_up_to(N):
    f = [1, 1, 2]
    while f[-1] <= N:
        f.append(f[-1] + f[-2])
    return f


def main():
    kmax = 400
    W = fib_prefix(4 * kmax + 10)
    L = len(W)
    F = {}
    for k in range(1, kmax + 1):
        F[k] = {W[i:i + k] for i in range(L - k + 1)}

    fibset = set(fibs_up_to(kmax))
    max_abs_d = 0
    zero_defect_ks = []
    ndef_seq = []   # number of nonzero defect cells per k
    violation_at_least_2 = []
    for k in range(1, kmax + 1):
        Fk = F[k]
        C = {}
        for w in Fk:
            ones = [t for t in range(k) if w[t] == '1']
            for a in ones:
                for b in ones:
                    key = (a + 1, b + 1)
                    C[key] = C.get(key, 0) + 1
        nz = 0
        bad = 0
        for i in range(2, k + 1):
            for j in range(2, k + 1):
                d = C.get((i, j), 0) - C.get((i - 1, j - 1), 0)
                if d:
                    nz += 1
                    max_abs_d = max(max_abs_d, abs(d))
                    if abs(d) >= 2:
                        bad += 1
        if bad:
            violation_at_least_2.append(k)
        if nz == 0:
            zero_defect_ks.append(k)
        ndef_seq.append(nz)

    print(f"k = 1..{kmax}")
    print(f"max |Toeplitz defect| over all k, all cells = {max_abs_d}")
    print(f"k with any |d| >= 2: {violation_at_least_2 or 'NONE'}")
    print(f"k with fully-Toeplitz matrix (zero defects): {zero_defect_ks}")
    # compare with F_n - 1
    pred = sorted({f - 1 for f in fibset if f - 1 <= kmax})
    print(f"predicted (F_n - 1): {pred}")
    print(f"zero-defect k == F_n - 1 set? {zero_defect_ks == pred}")
    # ndef sequence first 60
    print("ndef (nonzero defect cells) k=1..60:")
    print(" " + ",".join(map(str, ndef_seq[:60])))
    # ratio  ndef / (k-1)^2
    print("k where ndef == (k-1)^2 (fully defective off-diagonal-irrelevant):")
    full = [k for k in range(1, kmax + 1) if ndef_seq[k - 1] == (k - 1) ** 2]
    print(" ", full[:30])
    with open('code/out/topelitz_defects.txt', 'w') as fh:
        for k in range(1, kmax + 1):
            fh.write(f"{k} {ndef_seq[k-1]}\n")
    print("wrote code/out/topelitz_defects.txt")


if __name__ == '__main__':
    main()