# Beatty-floor pair-correlation (position-domain telescoping)

```approach
idea: Replace the "enumerate the k+1 factors" viewpoint with a position-domain sum.
  The Fibonacci word is the lower mechanical word of slope α = 1/φ² = (3−√5)/2, so its
  letter at position p is the Beatty increment F[p] = ⌊(p+1)α⌋ − ⌊pα⌋ (up to an intercept
  shift, which is irrelevant since the factor set depends only on slope). Each factor is
  F[p..p+k−1] for p in the first-occurrence set L(k) (|L(k)| = k+1). Squaring the value
  and expanding gives

      Ψ(k) = Σ_{i,j=0..k−1} 10^{2k−2−i−j} · C(i,j;k),
      C(i,j;k) = Σ_{p∈L(k)} F[p+i]·F[p+j].

  Each C(i,j;k) is a Beatty-difference count: the number of pairs of 1-positions at
  circular distance |i−j| lying in a window. Because F is a difference of floors,
  F[p]F[p+d] = (⌊(p+1)α⌋−⌊pα⌋)(⌊(p+d+1)α⌋−⌊(p+d)α⌋), and summing this over p telescopes by
  discrete summation by parts into O(1) boundary terms of the form ⌊(k+1)α+c⌋, ⌊kα+c⌋,
  and a few Σ⌊nα⌋/Σ⌊nα⌋² sums. Those floor sums are evaluated in O(log k) by continued
  fractions / Zeckendorf. L(k) itself is given by the three-gap theorem as a consecutive
  block plus a Fibonacci-structured tail, so the sum over L(k) splits into the main window
  [0..k−1] plus O(log k) tail terms.
mechanism: The blocker recorded in THREADS is "no indexed enumeration of factors relating
  grade k to grade k−1 in poly(log k)". This line bypasses enumeration entirely: the double
  sum is carried out in the position domain, where the bits are a Beatty sequence and a
  product of two floor-increments telescopes. The modular arithmetic then only needs
  geometric sums of powers of 10 (period ord_10(M) = 50500500) and closed-form floor sums,
  neither of which grows with k.
status: proposed
first-step: For k = 1..40, read the pair-correlation table A(i,j) out of
  code/out/structure.json, and verify the telescoped Beatty formula for C(i,j;k) against it
  (do d = 0, 1, 2, 3 first by hand); then rebuild Ψ(k) = Σ 10^{2k−2−i−j} C(i,j;k) and check
  it reproduces the oracle Ψ(3)=20302 and Ψ(10)≡10699667 (mod 101001001).
```
