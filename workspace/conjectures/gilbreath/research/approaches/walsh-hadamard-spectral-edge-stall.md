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
status: refuted
killed-by: |
  The Walsh-Hadamard diagonalisation of Rule 90 is correct and the
  combinatorial question about max zero-run in the edge sequence is a real
  one — but the approach is quantitatively insufficient and the program
  it launches cannot close.

  1. **The quantitative gap is fatal even if the lemma holds.** The
     approach's own arithmetic shows this: even with the best-case bound
     "stall ≤ b_k", the inter-event gap is at most G/2 + b_k + 1, which
     GROWS with b_k. In the recharge identity
     b_k = b_1 + Σ(j_i+1) − (k−1), each event contributes j_i+1 ≥ 1, and
     with at most one event every ∼b_k rows we get at most k/b_k events
     contributing mass ≥ 1 each — total recharge ≤ b_1 + k/b_k, against
     consumption k. Since b_k grows super-exponentially relative to k
     (b_161 ≈ 1.27×10^6 vs k=161), k/b_k ≪ k, and the inequality fails by
     an enormous margin. The approach's own text recognises this: "the
     bound needs to be much stronger."

  2. **The sub-linear O(log n) sharpening is the unproved non-degeneracy
     hypothesis.** The "O(log n)" claim would require the WH spectrum to
     avoid concentration at any single frequency — which is exactly the
     CHT "no long shallow {0,d}-block" obstruction, restated in spectral
     language. The CHT inverse theorem says this is as hard as the
     conjecture itself; no source proves it for primes, and Eppstein's
     construction shows the general 2-then-odds class permits the
     degenerate (all-zero) block that maximises the stall. So the
     spectral-sharpening step is the conjecture, not a route to it.

  3. **The framework is not wrong, it is just a dead end as a
     self-contained attack.** The WH formulation is a useful lens on the
     stall problem and could serve as a sub-lemma inside a broader
     approach (like the adopted subadditive-growth framework). But as a
     standalone proof strategy it aims at a bound the recharge identity
     shows is too weak by several orders of magnitude. The correct
     quantitative target is to bound the *mass* of jumps relative to
     inter-event gaps, not the gap length alone — which is exactly what
     the adopted approach does.
precedent: |
  BCZ 2023 (Bhat–Cobeli–Zaharescu) study PG triangles via GF(2)[[X]]
  rational generating functions — the WH/Rule-90 diagonalisation is their
  mod-2 framework. They do not address the stall problem or give spectral
  bounds on the edge sequence. The combinatorial question (max zero-run in
  Rule-90 edge sequence) appears not to have been studied in the CA or
  coding-theory literature under this framing, but the quantitative
  insufficiency does not depend on its answer.
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