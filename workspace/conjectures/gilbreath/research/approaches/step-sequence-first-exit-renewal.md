```approach
idea: >
  Close the recharge renewal process into a DETERMINISTIC Markov renewal whose
  kernel is a first-exit statistic of the halved row's step sequence. The jump
  size j_k and the landing intruder y_{k+1} at a (2,4)-event are BOTH read off
  the same halved row h_k: j_k is the position of the first halved step of
  size >= 2, and y_{k+1} is TWICE that step's size. This is the missing link
  between the run's two adopted regeneration approaches — edge-readout-descent-fuel
  gives WHEN an event fires; this gives WHAT HAPPENS when it fires — turning
  the black-box renewal (subadditive-growth-ergodic-block-length) into a closed
  transition on a single derived object.
mechanism: >
  Conventions: A_{k+1}(i) = |A_k(i) − A_k(i+1)|; entries A_k(i), i >= 1, are
  even (parity induction); halve them: h_k(i) = A_k(i)/2 for i >= 1. Then
  h_{k+1}(i) = |h_k(i) − h_k(i+1)| for i >= 1 (halving commutes with |·| on
  evens). The leading {0,2} block of row k+1 is positions i where
  h_{k+1}(i) ∈ {0,1}, i.e. EXACTLY where the step s_i := |h_k(i) − h_k(i+1)|
  is <= 1 (this is the run's proved 1-Lipschitz characterization). So

      b_{k+1} = max{ b : s_i <= 1 for all i <= b }  (leading small-step run of h_k).

  NEW EXACT LANDING LAW (the synthesis — to be machine-verified, then proved).
  At a (2,4)-event at row k (edge A_k(b_k) = 2 => h_k(b_k) = 1, intruder
  A_k(b_k+1) = 4 => h_k(b_k+1) = 2, so s_{b_k} = |1−2| = 1 <= 1, the run
  extends through the event):

      j_k  = b_{k+1} − b_k                       (number of extra small steps)
      y_{k+1} = 2 · s_{b_{k+1}+1}  = 2·|h_k(b_{k+1}+1) − h_k(b_{k+1}+2)|.

  In words: the jump is the length of the maximal run of halved steps of size
  <= 1 starting at the old boundary; the landing intruder is twice the size of
  the FIRST halved step of size >= 2, which terminates that run. Both are the
  SAME first-passage event of the step sequence s = |∂h_k|. Hence the recharge
  identity b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1) becomes a renewal-reward sum whose
  increments are an explicit first-exit functional of the halved-row orbit
  h_{k+1} = |∂h_k|, and the conjecture is: that deterministic renewal's reward
  never falls (k−1) behind.

  Why this is the third option the three refutations pointed at but did not name:
  - Freiman-refutation said "set doubling cannot reach sequence partial sums; the
    right object is renewal-reward r·J > 1." Correct — and this gives J (the
    per-event mass) an exact formula, not a black-box average.
  - Tucker-refutation said "the GLOBAL sign word is disconnected from A_k(1),
    and index theorems return global counts not a boundary value." Correct — the
    quantity that governs A_k(1) is the LOCAL step size at the boundary, which
    is exactly s, not a global sign word.
  - B-series-refutation said "the map is non-smooth, and the nonlinearity is
    localized at the boundary (Rule 90 inside, kink at the boundary)." Correct —
    the single nonlinear event is the first step >= 2; inside the block all
    steps are {−1,0,1}, the linear/Rule-90 regime.

  Aim past the goal: this does not bound the event rate; it REPLACES the event
  rate with a closed deterministic transition on (h_k, b_k, y_k). A general-class
  theorem becomes: "for a 2-then-odds start whose halved-row orbit has the
  property that the first-exit times of |∂h_k| to a >=2-step satisfy reward >=
  consumption, the block survives." The primes enter only through the orbit of H.

  Scholze check (new setting reproduces a result already in CLAIMS.md): it
  refines, not contradicts, step-law-theorem-proved (b grows <=> (2,4)) and the
  drain law (y_{k+1} = y_k − 2[x_k=2] on erosion): the step law's (2,4) trigger
  is the s_{b_k} <= 1 boundary condition, and the drain law is the erosion case
  s_{b_k+...} >= 2 read at a boundary that is NOT an event. It also refines
  bigjump-cap-characterization-1000 (the heavy tail of j is the heavy tail of
  the first >=2-step position of |∂h_k|) and giant-parity (parity of the event
  row is a parity constraint on the orbit of H, still unexplained).
status: adopted
first-step: >
  tool_builder: write `code/renewal/verify_landing_kernel.py`. Input:
  `code/out/blocks_depth1000.json` (exact integers; oracle regeneration rows).
  For every live row k with a genuine (2,4)-event — edge A_k[b_k] = 2, intruder
  A_k[b_k+1] = 4, and landing uncapped (b_{k+1} < W − k − 1, so the recorded
  jump is the complete jump) — compute h_k(i) = A_k(i)/2 for i >= 1,
  s_i = |h_k(i) − h_k(i+1)|, predicted b_{k+1} = leading run of s_i <= 1,
  predicted j_k = b_{k+1} − b_k, predicted y_{k+1} = 2·s_{b_{k+1}+1}. Compare
  against the actual b_{k+1}, j_k, y_{k+1} in the data; also confirm each
  erosion row has s_{b_k+...} >= 2 at its boundary (so it is not an event).
  Report violation counts and per-event margins; expect 0. Say CONFIRMED/REFUTED
  over the stated depth/width — never theorem/proved. A single violation refutes
  the landing law. Output `code/out/landing_kernel.{captured.txt,json}`.
precedent: >
  Proved ingredients (this run): step-law-theorem-proved (b grows <=> (2,4);
  drain law; recharge identity), the 1-Lipschitz block characterization
  (b_{k+1} = leading run of |h_k(i)−h_k(i+1)| <= 1), rule90-interior-xor
  (inside the block, halved steps are the linear/Rule-90 regime), and
  edge-interior-invertibility-sharpened (edge readout e = M h, M unitriangular
  Pascal-mod-2). Refuted ancestors whose positive content is absorbed here:
  doubling-constant-jump-set (recharge is SEQUENCE-additive, not set-additive),
  tucker-sign-index-topology (the governing quantity is the LOCAL boundary step,
  not a global sign word), discrete-bseries-composition (non-smooth map;
  nonlinearity localized at the >=2-step). Computed support: bigjump-cap-
  characterization-1000 (landing intruders {4,6,12,14} = 2 × first >=2-step,
  consistent), giant-jump 1-Lipschitz mechanism (Established, CONTEXT.md).
```

## Why this is the adopted synthesis (and not one of the three candidates)

All three candidates died correctly, but each death named the *right* object while refuting the *wrong* mechanism. The three refutations converge on one statement neither I nor research wrote down:

1. **Freiman (refuted: set structure ≠ sequence partial sums).** The surviving sentence is "the correct reformulation is renewal-reward r·J > 1." That leaves J unexplained — a black-box average over events. My synthesis gives J an exact formula: at each event, J = j+1 = (position of the first ≥2-step of |∂h_k|) + 1.

2. **Tucker (refuted: the *global* signed-difference sign word is disconnected from A_k(1), and index theorems return global counts).** The surviving sentence is that the governing object is *local*. The local step size s_i = |h_k(i) − h_k(i+1)| at the boundary is exactly what determines A_{k+1}(i) — no global topology needed.

3. **B-series (refuted: non-smooth, nonlinearity localized, exponential tree growth).** The surviving sentence is that the nonlinearity lives at a *single threshold* (the kink / the switch), while the interior is the linear Rule-90 regime. The "first step ≥ 2" is precisely that single threshold.

Composing the three survivals gives the landing law: **the (2,4)-event transition (b_k, y_k) ↦ (b_k + j_k, 2·s) is a deterministic first-exit functional of the halved row's step sequence**, with j_k the exit *position* and 2·s the exit *magnitude*. This is the exact kernel that closes the renewal.

**Scholze's gate** is satisfied explicitly: the new setting reproduces the proved step law and drain law (erosion is the boundary step ≥ 2 case; the event is the boundary step = 1 followed by a small-step run), and it refines — not contradicts — the measured heavy-tail claim (the jump heavy tail = the heavy tail of the first ≥2-step position).

## Hand-check on problem.md rows (before delegating the machine check)

Row 1 halved: h₁ = (1,1,2,1,2,1,2,3,1,…); steps s = (0,1,1,1,1,1,1,2,…), first ≥2 at i=8, so b₂ = 7 ✓ (matches the recorded profile 2,7,13,…) and landing intruder y₂ = 2·s₈ = 4 ✓ (A₂(8)=4).

Row 2 is a genuine (2,4)-event (edge A₂(7)=2, intruder A₂(8)=4, both read off problem.md's A₂ row). With b₃ = 13 taken from the run's recorded b-profile (CONTEXT.md: rows 1..40 = 2,7,13,…), the jump is j₂ = b₃−b₂ = 13−7 = 6 (arithmetic on recorded data, not re-derived). The prediction y₃ = 2·s₁₄ requires A₂(9..15), which problem.md's snippet truncates, so it is a PREDICTION to be checked by the tool, not a hand-verified value.

This is hand arithmetic on two rows, not a proof; the first-step hands the full machine verification to tool_builder.
