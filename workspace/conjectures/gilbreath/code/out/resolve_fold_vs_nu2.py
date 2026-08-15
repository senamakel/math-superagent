"""RESOLVE the prefix-vs-suffix fold contradiction (Directive).

Question: does true nu2 (maximal {0,2}-suffix count of the right diagonal)
equal the SUFFIX fold (geometric window fold ending at column n-1), and not
the PREFIX fold (whole-word subset-zeta / powers-of-two count)?

Set-up (faithful to the run's ground truth, C1 convention, Thue-Morse):
  q = [2,3]; q.append(q[-1]+(2 if t(j) else 4)) for j=0..,  t(j)=wt(j) mod 2.
  halved-gap column bit h[c] = ((q[c+1]-q[c])//2)%2 = t(c-1).
  delta(q_n) via lib.rightdiag.incremental_diagonals; nu2 via cycle_and_nu2
  (body diag[:-1], maximal {0,2} suffix floored at index 2).  Ground truth:
  nu2(100)=27, nu2(4000)=45.

Two candidate folds of the word over columns 2..n-1 (m = n-2 bits):

  (A) SUFFIX fold (windows ending at column n-1) = lib.rule90fold.fold_weight_h:
      fold_cell(k) = XOR_{i=0..k-1, C(k-1,i) odd} h[n-k+i],  k=2..n-2.
      This is the RIGHT-DIAGONAL geometric fold: cell at depth k reads the
      ancestor window [n-k, n-1] of row 1.  Called the "suffix fold" because
      every window ends at the last column n-1 (grows back from the end).

  (B) PREFIX fold = whole-word subset-zeta of the length-m word:
      z[d] = XOR_{j submask d} h[j], d=0..m-1.  For Thue-Morse h this is the
      powers-of-two indicator (zeta(d)=1 <=> d a power of 2), so its weight
      = #{powers of 2 <= m}.  A genuinely different object.

Conclusion sought: (A) == true nu2, (B) != true nu2.

Exact integers only.  No floats.
"""
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
from lib.rule90fold import fold_weight_h


def thue_morse(j):
    return bin(j).count('1') & 1


def build_q(D):
    q = [2, 3]
    for j in range(D + 2):
        q.append(q[-1] + (2 if thue_morse(j) else 4))
    return q


def suffix_fold_weight(q, n):
    """Geometric suffix fold via lib.rule90fold.fold_weight_h.  h[c] = actual
    halved-gap column bit c, c=2..n-1, i.e. h[j0] with j0=c-2."""
    m = n - 2
    h = [((q[c + 1] - q[c]) // 2) & 1 for c in range(2, n)]  # h[0..m-1]=cols 2..n-1
    return fold_weight_h(h, m)


def prefix_fold_weight(n):
    """Whole-word subset-zeta of the TM word h[j]=t(j): weight = # powers of 2
    <= m (exact for TM: zeta(d)=1 <=> d is a power of two, verified)."""
    m = n - 2
    cnt = 0
    for d in range(1, m + 1):
        if (d & (d - 1)) == 0:      # d is a power of two
            cnt += 1
    return cnt


def main():
    D = 4000
    q = build_q(D)
    ds = list(incremental_diagonals(q))
    print("Prefix-vs-suffix fold resolution, Thue-Morse (C1, exact ints)")
    print("=" * 60)
    for n in (100, 4000):
        diag = ds[n]
        tau, nu2 = cycle_and_nu2(diag)
        sf = suffix_fold_weight(q, n)
        pf = prefix_fold_weight(n)
        print(f"n={n}:")
        print(f"   TRUE nu2 (canonical cycle_and_nu2) = {nu2}   (tau={tau})")
        print(f"   (A) SUFFIX fold (lib.fold_weight_h, windows ending col n-1)"
              f" = {sf}   suffix==true nu2? {sf == nu2}")
        print(f"   (B) PREFIX fold (whole-word subset-zeta, "
              f"# pw2<=m) = {pf}   prefix==true nu2? {pf == nu2}")
        print()
    # discriminating assertion
    ok = True
    for n in (100, 4000):
        diag = ds[n]
        nu2 = cycle_and_nu2(diag)[1]
        if not (suffix_fold_weight(q, n) == nu2 and prefix_fold_weight(n) != nu2):
            ok = False
    print("DISCRIMINATING ASSERTION "
          "(suffix==true nu2 AND prefix!=true nu2 at n=100,4000):",
          "PASSES" if ok else "FAILS")
    return ok


if __name__ == '__main__':
    main()
