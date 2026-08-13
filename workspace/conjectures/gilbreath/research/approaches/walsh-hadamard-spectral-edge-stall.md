```approach
idea: walsh-hadamard-spectral-edge-stall
mechanism: |
  The halved block h ∈ GF(2)^{b_k} evolves by the Rule 90 / Pascal-mod-2
  operator. The edge x(k+d) (the last entry of the block after d erosion rows,
  which determines whether the intruder drains or stalls) is:

      x(k+d)/2 = XOR_{j=0}^{d} [C(d,j) mod 2] · h_{b_k − d + j}

  This is the d-th term of the Rule-90 evolution of the string h, evaluated
  at the terminal position. The sequence (e_0, e_1, ..., e_{b_k−1}) where
  e_d = x(k+d)/2 is a linear function of h over GF(2).

  The Walsh-Hadamard (WH) transform diagonalizes the Rule 90 operator.
  For a binary string h of length n, the WH transform is

      Ĥ(w) = Σ_{i=0}^{n−1} (−1)^{popcount(w ∧ i)} · h_i   (mod 2)

  where w ∈ {0,1}^n is a frequency index. Rule 90 acts as pointwise
  multiplication: if h' = T(h) is one row of XOR evolution, then
  Ĥ'(w) = (1 + (−1)^{w_0}) · Ĥ(w) for the first position, etc. This means
  the WH spectrum evolves multiplicatively under Rule 90.

  The key spectral fact: the "all-ones" WH coefficient Ĥ(11...1) is exactly
  the XOR-sum of all entries of h. At depths d = 2^j − 1 (powers of 2 minus
  1), Rule 90 produces a row where every entry is the XOR of the full width-
  (2^j) window — this is the Sierpinski all-1s kernel. In the WH picture,
  this is a single-frequency selection.

  The edge stall problem — "how many consecutive rows can e_d = 0 while d
  increases?" — translates to a spectral condition: e_d = 0 for d = d_0,
  d_0+1, ..., d_0+m means that m+1 consecutive triangular XORs of h all
  vanish. These are m+1 linear equations over GF(2) on h. The WH transform
  converts this to constraints on the WH spectrum of h.

  The central claim: for any non-zero h ∈ GF(2)^n, the maximum number of
  consecutive zeros in the edge sequence (e_d) is at most n (the block length).
  Moreover, the unique worst case is h = (0,0,...,0) (all zeros), for which
  e_d = 0 for all d, and any non-zero h has strictly shorter maximum zero-run.

  If this combinatorial lemma holds, then the (0,4)-stall length is bounded
  by b_k. Combined with the drain law (y drops by 2 per x=2 step, bounded
  by the maximum gap G), the inter-event gap is at most G/2 + b_k + 1.
  Since b_k grows super-linearly with k (empirically), the average event rate
  is at least 1/(G/2 + b_k + 1), which vanishes as b_k → ∞ — but the
  REVERSE is what we need: events occur at least every ∼b_k rows, while
  each event recovers ∼b_k rows of block length. The balance is tight
  (recharge identity: Σ(j+1) must exceed k−1−b_1), and a bound
  "event gap ≤ b_k" with jump "j+1 ≥ 1" gives Σ(j+1) ≥ #events, which
  combined with "gap ≤ b_k" gives #events ≥ k/b_k. If b_k ∼ k, this is
  borderline; the real data shows b_k ≫ k (b_161 ≈ 1.27M vs k=161), so
  the bound needs to be much stronger, or the stall bound must be sub-linear
  in b_k.

  The WH framing provides the tool to sharpen the stall bound: instead of
  "max zero-run ≤ n", we may prove "max zero-run ≤ O(log n)" for non-degenerate
  h, using the fact that the WH spectrum of h arising from the halved prime
  gaps is far from degenerate (it is not concentrated at a single frequency
  that would give a long zero-run). This is the spectral analogue of the
  "no long constant-zero block" hypothesis.

  Why it beats existing approaches:
  - NOT rule90-regeneration (which looked at absolute depth timing and died
    on the null test). This is about the WORST-CASE edge-flip time.
  - NOT renewal-process (which treats the edge as an i.i.d. Bernoulli process
    and conjectures a union bound). This diagonalises the linear operator
    and gives exact spectral conditions for the stall.
  - NOT block-apex-parity-forcing (which tried to classify block patterns).
    This only needs one spectral property: that h is not in the kernel of
    too many consecutive edge operators.
  - The WH transform is the natural basis for Rule 90, used by BCZ 2023 at
    mod-2 level; this lifts it to the edge-stall question.

  Speculative: the worst-case stall bound is not b_k but something like the
  "linear complexity" (Berlekamp-Massey) of the halved block over GF(2).
  For the prime gaps, this may be provably large (close to b_k), which would
  give a substantially better than b_k stall bound.
status: proposed
first-step: |
  Exhaustively compute the maximum zero-run in the edge sequence e_d for all
  2^n binary strings h ∈ GF(2)^n with n ≤ 16. For each n, record the max
  zero-run length L(n), the string achieving it, and whether the all-zero
  string is the unique worst case. Then compute the WH spectrum of each
  worst-case string and look for a spectral characterization (e.g., all-zero
  run of length L corresponds to vanishing of the first L+1 coefficients
  in some frequency band). Then state the conjecture: "L(n) ≤ n for all n,
  and L(n) = n iff h is all-zero" vs what the data shows. Output to
  code/out/walsh_hadamard_stall_exhaust.{captured.txt,json}.

  Second: compute the WH spectrum of the actual halved blocks from the
  depth-1000 prime data (for each row k=1..161 in the live regime) and
  measure the spectral concentration (e.g., maximum WH coefficient magnitude,
  or the linear complexity / Berlekamp-Massey profile). Compare to the
  worst-case strings from the exhaustive search to see how far the prime blocks
  are from the stall-maximizing patterns.
```
