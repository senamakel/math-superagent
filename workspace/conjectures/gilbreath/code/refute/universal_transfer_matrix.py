#!/usr/bin/env python3
"""Attack S1-nu2-transfer-weight: does the F2 transfer map satisfy
wt(Phi_n h) >= wt(h)/2 for ALL h in {0,1}^{n-2}?

Setup (from G-supply-linearization / rule90-interior-xor):
  Right diagonal of q_n: cells (k, n-k), k=0..n-1.
  Tail cells (the {0,2} suffix region, in the code's convention d[2:-1]):
    k = 2..n-2.
  A halved tail cell (k, n-k) at depth k equals the XOR of a Pascal window
  of row-1 halved gap bits h over ancestor columns [n-k, n-1]:
     halved(k,n-k) = XOR_{j : binom(k-1, j-(n-k)) odd} h[j], j in [n-k, n-1].
  Phi_n : {0,1}^{n-2} -> tail-cell bits, entry row k col j = [C(k-1, j-(n-k)) mod 2].
  w = wt(h);  nu2 = wt(Phi_n h) = number of k in [2, n-2] with XOR nonzero.

We test the UNIVERSAL claim wt(Phi_n h) >= wt(h)/2 for all h, n=4..20.
A single counterexample refutes case (a); per the claim's own fork, S1
then must move to case (b) (prime-specific) and the two-gap split is not
a genuine reduction.
"""
from math import comb

def phi_row(k, n, j):
    """entry of Phi_n: row k (2..n-2), col j (2..n-1)."""
    # ancestor interval [n-k, n-1]; offset = j-(n-k), 0..k-1
    if j < n - k or j > n - 1:
        return 0
    return comb(k - 1, j - (n - k)) % 2

def nu2_of_h(h, n):
    """h is list indexed j=2..n-1 (length n-2). Returns wt(Phi_n h)."""
    cnt = 0
    for k in range(2, n - 1):            # tail rows 2..n-2
        x = 0
        for j in range(n - k, n):
            if phi_row(k, n, j):
                x ^= h[j - 2]
        cnt += x
    return cnt

def main():
    worst_ratio = 2.0          # track min nu2/w
    worst_h = None
    worst_n = None
    for n in range(4, 21):
        m = n - 2               # window size 2..(n-1), columns count n-2
        N = 1 << m
        for mask in range(N):
            h = [(mask >> (j - 2)) & 1 for j in range(2, n)]
            w = bin(mask).count('1')
            if w == 0:
                continue
            nu2 = nu2_of_h(h, n)
            ratio = nu2 / w
            if ratio < worst_ratio:
                worst_ratio = ratio
                worst_h = h[:]
                worst_n = n
            if nu2 * 2 < w:              # strict: nu2 < w/2
                print("COUNTEREXAMPLE n=%d  nu2=%d  w=%d  h=%s"
                      % (n, nu2, w, h))
                print("=> wt(Phi_n h)=%d < wt(h)/2=%d"
                      % (nu2, (w + 1) // 2))
                return
        print("n=%2d : all %d strings pass (nu2>=w/2)" % (n, N))
    print("No counterexample n=4..20. Min ratio %.4f at n=%d h=%s"
          % (worst_ratio, worst_n, worst_h))

if __name__ == "__main__":
    main()
