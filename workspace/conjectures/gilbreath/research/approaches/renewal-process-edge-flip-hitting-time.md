```approach
idea: renewal-process-edge-flip-hitting-time
mechanism: |
  The drain law (`y_{k+1} = y_k − 2·[x_k = 2]`) and the step law
  (`b_{k+1} = b_k − 1` except at `(2,4)`) are exact and combinatorial. Between
  two `(2,4)`-events, the intruder y starts at some even value ≥ 4 and is
  drained by exactly 2 whenever the last block entry x(k) = `A_k[b_k]` is 2,
  and stays unchanged when x(k) = 0. The edge x(k) itself evolves as the
  terminal entry of the leading {0,2} block, whose interior is governed by
  XOR (Rule 90). So the inter-event dynamics are a **coupled process**:

  - The intruder y(k) is a counter (starts at some y₀, drains toward 4).
  - The edge x(k) is a binary process {0,2}-valued, driven by the XOR
    evolution of the halved block pattern.

  Regeneration fires the first time the pair hits (x=2, y=4). The question is:
  **what is the maximum number of rows from a post-regeneration state (where
  y_{k+1} is typically 4 or ≥ 6) to the NEXT (2,4)-event?**

  This is a **hitting-time problem** for a finite-state process. The edge x(k)
  at the boundary position is the XOR of a triangular window of the halved
  block's bit pattern; the window shrinks by one per row (because the block
  erodes by one per row). At the halved level, the block is a binary string
  of length `b_k`. At row `k+d` (d rows into erosion), the edge is at position
  `b_k − d`, and its value is the XOR of a depth-d triangle of the halved
  block bits. This is exactly the Rule 90 / Pascal-mod-2 evolution of the
  terminal bit.

  The key combinatorial fact: for a random halved block (uniform i.i.d. bits),
  the edge x(k+d) is a martingale (each step XORs a fresh bit with the
  previous XOR accumulator), so it is equally likely to be 0 or 1 at each step,
  independently of the past. This is the CHT "random walks on the boundary"
  picture. Under this model, the hitting time to x=1 (i.e. A=2) has geometric
  distribution with success probability 1/2 per row, so the expected time to
  the next x=2 is 2 rows.

  More precisely: when y=4 and x=0, the next row still has y=4 (drain law with
  x=0: y unchanged) and x' is another independent Rule 90 step — so the process
  `(x, y)= (0,4) → (x', 4)` repeats until x'=2, which takes geometric(1/2)
  rows. Once x=2 with y=4, regeneration fires. The maximum observed stall at
  y=4 is 6 rows (data: max consecutive non-regen y=4 rows = 6). Under the
  i.i.d. model, P(stall ≥ 6) = (1/2)^6 = 1/64 ≈ 1.6%, entirely consistent with
  the data.

  **The theorem to prove**: for ANY starting halved block pattern (not just
  i.i.d. random), the edge x(k+d) cannot stay 0 for more than `2·b_k` consecutive
  rows while the intruder is at 4. This is the combinatorial Route A of the
  regeneration thread — a worst-case bound on the (0,4)-stall length that depends
  only on the block length b_k, NOT on primality.

  Why this is new and not a variant of refuted approaches:
  - NOT rule90-absorbing-boundary (which claimed bounded ABSORPTION time for
    intruders — refuted by CHT Lemma 3.7(iii) and Eppstein). This proposal is
    about the HITTING TIME of the edge to flip to 2 AFTER the intruder has
    ALREADY drained to 4. The drain law is verified and the intruder is already
    at 4; the only remaining obstruction is the x=0 stall.
  - NOT block-apex-parity-forcing (which claimed block pattern class forces
    regeneration — refuted because CHT proves persistence regardless of pattern).
    This proposal makes NO claim about the block pattern forcing anything; it
    bounds the stall length under the Rule 90 dynamics of the EDGE evolution
    ALONE.
  - It is a direct attack on the regeneration thread's Route A with the exact
    combinatorial mechanism.

  The conjectured lemma: "In any {0,2} block evolving under the absolute-difference
  operator with an intruder y=4 at its right boundary, the edge value x(k) at the
  boundary position cannot remain 0 for more than L consecutive rows, where L
  depends only on the block's halved bit pattern." The sharpest form: L ≤ 2·b_k
  because any {0,2} string of length n under repeated XOR at the terminal position
  must produce a 1 within 2n steps (a known property of linear feedback shift
  registers, or at worst a provable Lemma by binary linear algebra).

  The renewal-process picture then gives: inter-event gap ≤ drain_time(y₀→4) +
  stall_time(x at y=4) + 1. The drain time is bounded by y₀/2 (each x=2 step
  drains 2), and y₀ is bounded by the maximum gap in the starting row. Under
  the hypothesis that the initial sequence has gaps bounded by G (prime gaps:
  known to be bounded by something small), y₀ ≤ G, and the total inter-event
  gap is at most G/2 + 2·b_k + 1. Since b_k grows, this gives a regeneration
  rate lower bound.

  **Speculative**: the worst-case stall bound L ≤ 2·b_k must be proved or
  refuted. If the halved block is the all-zero string, the edge stays 0
  forever — but the all-zero halved block means the block is constant-0, which
  means the original row had a constant-zero block. The data (depth 1000) shows
  no constant block beyond length 2 (only k=1 has constant (2,2)). The
  question is whether constant-zero halved blocks can arise from a 2-then-odds
  start — Eppstein's construction DOES produce long zero blocks, but those are
  original-row zeros (A_k(i)=0), not halved-block zeros. The halved block is
  A_k(i)/2 for i in the block; a halved zero means A_k(i)=0, which IS a
  constant-zero block in the original row. So: "no long constant-zero block"
  IS needed for the worst-case bound, and CHT Theorem 1.6 isolates long
  zero-blocks as one of exactly two obstructions. The primes are conjectured
  to avoid long zero-blocks, and this approach would prove that IF they do,
  THEN the regeneration rate suffices.

  This restates the CHT inverse theorem at the combinatorial level: the
  approach proves an explicit bound linking the zero-block length to the
  regeneration rate, making the CHT inverse theorem quantitative for the
  regeneration problem.
status: grounded (search, attempt-5) — literature provides the exact machinery; the blocking lemma is a genuinely open statement
precedent: |
  (grounded, attempt-5 search — lower-bound-search-6.md) The blocking lemma's
  own technical machinery IS in the literature, and the run had not brought it
  to bear:
  - **Northshield (2010), "Sums across Pascal's triangle modulo 2"**,
    http://hdl.handle.net/1951/69939 — studies mod-2 binomial sums
    Σ [C(i+j,i) mod 2] along Pascal lines via generating functions with
    functional equations of the form A(x) = P(x)·A(x^2) (divide-and-conquer,
    base-2 digit representations). The edge value e_d = XOR_{j=0}^d [C(d,j)
    mod 2]·h_{b_k−d+j} is EXACTLY such a mod-2 binomial sum; Northshield gives
    the recursion that determines the whole edge sequence (e_0, e_1, ...),
    which is the algebraic form of the (0,4)-stall zero-run question. This
    replaces the brute-force 2^n edge-run enumeration with an exact
    generating-function / digital-root analysis.
  - **Malyshev (2021), "Boolean analogues of Pascal's triangle with maximal
    possible number of ones"**, doi 10.1515/dma-2021-0029 — max # of 1s in a
    size-s Boolean Pascal triangle ≤ ⌈s(s+1)/3⌉, attained on Fibonacci-mod-2
    top row. Bounds how sparse edge=2 rows can be in a window, i.e. a raw
    lower bound on the edge-flip rate feeding the drain law.
  - **Blair Morgan (2026)**, doi 10.5281/zenodo.19143643 and 10.5281/zenodo.
    19144967 — independent rediscovery of the run's own reduction (GC ⟺
    second entry in {0,2}) and of the local-obstruction picture (a pure
    8→7→6→5→4 erosion corridor is impossible: it would force a zero-block in
    positions 4–7 contradicting Row 2's twos). Corroborates that the run's
    local boundary-obstruction shape is the accepted one. Preprints,
    h-index 0, not peer-reviewed.
  - Cyclic-Ducci sources (Lewis–Tefft 2024 arXiv:2401.17502; Breuer–
    Shparlinski 2019 Bull. Austral. Math. Soc.) confirmed NOT the model — the
    half-infinite regeneration has no right edge and is not covered by any
    cyclic vanishing/period theorem.
  No published source proves a half-infinite (2,4)-event rate lower bound:
  the blocking lemma itself is genuinely open, but its proof engine (mod-2
  Pascal sums) is a named literature technique.
  Evidence class: directional (search collision, downloaded sources not yet
  read in full — search halted per directive). Read Northshield/Malyshev in
  the source before building a proof on them.
first-step: |
  Encode the edge evolution as a linear process over GF(2). The halved block
  at row k is a binary string h ∈ {0,1}^{b_k}. After d rows of erosion, the
  edge (at position b_k − d of the halved block) is e_d = XOR_{j=0}^{d}
  [C(d,j) mod 2] · h_{b_k − d + j} (the Rule 90 convolution, proved in
  block_lemma.md). For a fixed h, the sequence e_0, e_1, ..., e_{b_k−1} is a
  sequence of XORs of expanding windows of h.
  (a) REPLACE the brute-force 2^n enumeration with the exact mod-2 structure:
  read Northshield 2010 and derive the A(x)=P(x)A(x^2) recursion for the edge
  sequence, then state the zero-run bound in terms of the digital (base-2)
  root structure of the window h. That is the normal, non-enumerative form of
  the blocking lemma's proof.
  (b) Small-instance verification (this is the permitted oracle use, NOT the
  method): for n = 1..12 compute the max zero-run of (e_d) over all 2^n
  strings h to confirm the conjecture "worst-case zero-run ≤ n" and that the
  all-zero string is the unique bad case — establishing the exact bound a
  proof must match before attempting it.
  (c) Then combine with the drain law: inter-event gap ≤ drain_time(y₀→4) +
  stall_time at y=4 + 1, giving the regeneration rate lower bound. The
  all-zero halved block (constant-zero original block) is the CHT zero-block
  obstruction; excluding it (primes' min b ≥ 2, no long zero-blocks) is the
  hypothesis the bound needs.
  If the bound holds for every non-zero string, the approach yields a
  provable regeneration rate lower bound for any sequence whose blocks are
  not constant-zero.
```
