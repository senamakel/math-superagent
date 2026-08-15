# Two's-complement carry decorrelation for the ν₂ (G-supply) bound

```approach
idea: The descent coefficient ν₂ = #{c_s = 2} in Granville's right-diagonal budget is
  EXACTLY the borrow count of the two's-complement subtraction of consecutive halved
  gaps; because a − b = a + b̄ + 1 (mod 2^m), the borrows of |a−b| are the carries of a
  base-2 addition of the complemented smaller operand and the larger operand. Diaconis–
  Fulman's theory of base-2 addition carries then gives a Markov chain with explicitly
  computable stationary measure (Bernoulli(1/2): carry density 1/2), so the open supply
  bound ν₂ ≥ c·n reduces to a single decorrelation statement about the prime-gap bits
  h_j = [p_{j+1} ≢ p_j mod 4] — strictly weaker than full Hardy–Littlewood pair
  correlation, and matching the CHT "2-separated / non-concentration" hypothesis.
mechanism: |
  This is the synthesis of the three refuted candidates, taking the surviving core of
  each and discarding the hypothesis that research killed.

  1. (From binary-carry-transducer, the part that survives) |a−b| is computed by a
     finite transducer: a 3-state left-to-right comparator fixes the sign, and a 2-state
     right-to-left borrow-subtractor produces the magnitude. That part was never refuted;
     what died was the claim that the INPUT (the primes) is automatic, which kills
     Christol/Cobham. We do not re-claim automaticity.

  2. (From borrow-young, with the bridge research missed) Research refuted the
     Diaconis–Fulman attachment on the ground that their carries belong to ADDITION
     while the min(a,b) branch of |a−b| = a+b−2min(a,b) is a SUBTRACTION borrow. That
     dichotomy is false: subtraction borrows ARE addition carries via two's complement,
     a − b = a + b̄ + 1 (mod 2^m). The min-branch correction is therefore a bona fide
     Diaconis–Fulman carry process — the carry of adding the two's complement of the
     smaller operand to the larger. No Young-diagram hypothesis is needed.

  3. (The precise object) On the halved gap diagonal h_j = (p_{j+1}−p_j)/2, the descent
     coefficients c_s ∈ {0,2} of Granville Lemma 5.4's budget are the borrows of the
     subtraction chain; ν₂ = #{c_s = 2} is the total carry/borrow count. The run already
     established (board, this run) that ν₂ is an F2-linear invertible function of the
     bits h_j mod 2, i.e. of [gap ≡ 2 mod 4], with measured transfer ν₂ ≥ w/2 where
     w = #{gap ≡ 2 mod 4}. The carry interpretation turns that measured linear map into
     an EXPLICIT finite-state computation, and it is exactly the map whose density the
     Diaconis–Fulman theory controls.

  4. (The named theorem to import, not Christol/Cobham) Diaconis–Fulman: the carries of
     base-2 addition form a Markov chain; for two operands plus carry-in the carry-out
     bit is c' = majority(a,b,c), transition matrix [[3/4,1/4],[1/4,3/4]], stationary
     measure Bernoulli(1/2). Hand-checked: P(carry=1) = 3·(1/4) − 3·(1/8) + 1/8 = 1/2.
     This matches the measured ν₂/n ∈ [0.42,0.52] and ν₂/w ∈ [0.689,0.867]. The entire
     gap between the i.i.d. model and the primes is a DECORRELATION property of the bit
     stream h_j: the carry chain mixes inputs that are "not too concentrated", and a
     non-concentration condition (exactly CHT's 2-separated-set condition (ii), and
     Ross 2026's operative hypothesis) is what forces positive stationary carry density.
     So "ν₂ ≥ c·n" becomes "the prime-gap bits h_j are not concentrated in a 2-separated
     set" — a statement strictly weaker than the two-point HL correlation, with the
     carry chain as the mixing mechanism that converts non-concentration into density.

  Why it is not one of the refuted three:
  - NOT automatic-sequence: no claim that the input or the column is automatic; the
    transducer is used only as an exact computation, and the proof engine is
    Diaconis–Fulman carry DECORRELATION, not Christol/Cobham algebraicity.
  - NOT curvature flow: no geometric/flow claim; no Grayson transfer.
  - NOT borrow-young: no Young-diagram shape claim; the correct bridge (borrow = carry
    under complement) replaces the unsupported "subtraction-borrow shape" conjecture.
  - NOT p-adic-valuation-carry-dynamics (proposed, distinct): that tracks v_2 (the
    scalar valuation). This tracks the BORROW/CARRY bit of the sign+magnitude
    computation, a finite-state object with a named Markov-chain theory.
  - NOT mod4-pascal (refuted): no congruence lift; the borrow bit is the exact
    computation at full binary precision, and the content is a mixing statement, not a
    modulus invariant.
status: refuted
closure: >
  Directive 52 (steer): `anticlustering_hypothesis` is a negative result that closes
  the PROOF STRATEGY this approach rested on. `code/out/anticlustering_hypothesis.captured.txt`:
  under Markov models of the mod-4 switch bit, generic anti-clustering does NOT deliver
  a uniform positive-linear bound nu2 >= c*w — prime-like (0.55,0.60) worst-min nu2/w
  = 0.0714 (11/30 trials violate); Bernoulli control and clustered variants 12–13/30;
  stationary-density-0.59 family 11–17/30; prime's own empirical transitions (a=0.5565,
  b=0.6584) 8/20. This is exactly the falsifier this file pre-registered: "if the carry
  chain fed by the actual prime-gap bits does not mix ... the carry machinery adds no
  new lower bound over the already-measured transfer, and the approach collapses back to
  chebyshev-bias's 'conditional at Hardy–Littlewood level'." The falsifier fired. Scope
  of the negative: it refutes the mixing/anti-clustering PROOF STRATEGY, not G-supply for
  the primes (real prime gaps are not a Markov chain; 30 trials of a worst-min statistic
  is noisy). What it leaves: a positive-linear bound cannot come from mixing alone; the
  remaining candidates are arithmetic — Hardy–Littlewood two-point mod-4 correlations, or
  the Lemke Oliver–Soundararajan two-point bias with its oscillating second-order term.
  **Run's recorded bet: neither is unconditional; G-supply stays a named open hypothesis
  and the deliverable is the CONDITIONAL theorem with the HL/LOS two-point switch-
  correlation lower bound as the named hypothesis.** The exact two's-complement
  transducer bridge (`carry-bridge-exhaustive`, `carry-bridge-nu2-reproduction`) survives
  as a verified computation; what died is the hope that a mixing theorem turns it into a
  lower bound.
side: regeneration / supply (attacks the single open G-supply statement ν₂ > n^β by
  making the F2-linear descent map explicit and handing its density to a named
  carry-mixing theorem); erosion is settled and untouched.
precedent: |
  - Diaconis–Fulman (arXiv:0806.3583, arXiv:0902.0179; Borodin–Diaconis–Fulman Bull. AMS
    2010, doi:10.1090/S0273-0979-2010-01306-9): carries of base-b addition form a Markov
    chain with Eulerian stationary measure; base-2 two-operand case has stationary
    Bernoulli(1/2). Held in the library (this run).
  - The two's-complement identity a − b = a + b̄ + 1 (mod 2^m) is standard; borrows of
    subtraction = carries of the complemented addition. Verified by hand above
    (carry density 1/2, transition matrix [[3/4,1/4],[1/4,3/4]]).
  - The transducer for |a−b| (comparator × borrow-subtractor) survives from
    binary-carry-transducer (research did not refute this part).
  - Run's own established content the approach consumes: ν₂ is F2-linear invertible in
    the gap bits h_j = [gap ≡ 2 mod 4] (board, rising-sea post); ν₂ ≥ w/2 with c ≈ 1.45
    (measured, granville-nu2-density-measured); ν₂ is TWO-POINT (consecutive-pair mod-4
    switch), not one-point (check_nu2_one_vs_two_point); CHT condition (ii) is a
    2-separated-set non-concentration hypothesis; Ross 2026's operative general-class
    hypothesis is 2-separation.
  - Hard refutations respected: Hartmanis–Shank 1968 / Dubbe 2024 (primes non-automatic)
    → no Christol/Cobham; Chow–Glickenstein / Grayson (flows linear, 2D) → no curvature
    import; Eppstein 2011 (anti-gilbreath-construction) → no general-class bounded-gap
    theorem. This approach is prime-side and conditional, consistent with all three.
first-step: |
  (a) Implement the exact finite-state computation and verify it: a 2-state
  borrow-subtractor for the magnitude (carry of a + b̄ + 1) plus a 3-state comparator for
  the sign; machine-check that the composed transducer equals |a−b| for all pairs
  a,b < 2^14. This establishes the borrow = carry bridge computationally, not just by
  hand.
  (b) Reproduce the transfer: compute the halved gap bits h_j = (p_{j+1}−p_j)/2 mod 2
  and run the borrow/carry chain to obtain the descent coefficients c_s; verify the
  borrow count equals ν₂ (reproducing granville-nu2-density-measured ν₂/n ∈ [0.42,0.52]
  for n = 1..3999) and the transfer ν₂ ≥ w/2.
  (c) Quantify the decorrelation gap: for i.i.d. Bernoulli(1/2) input the carry density
  is exactly 1/2 (stationary Bernoulli(1/2)); compare with the measured ν₂/w ∈
  [0.689,0.867] to measure how far the prime-gap bits sit from i.i.d., and record the
  empirical carry-chain transition kernel fed by the actual bits. This isolates the
  single quantity a mixing/non-concentration proof must bound.
  Cost: O(depth × width), one row live, no sieve beyond the existing 2e7 record. The
  falsifier: if the composed transducer does not equal |a−b|, or the borrow count does
  not reproduce ν₂, the bridge is wrong and the approach is dead before any theory.
scholze-gate: The old setting (Granville's ν₂ budget + the run's F2-linear transfer
  ν₂ ≥ w/2, established in granville-nu2-density-measured and the board posts) works
  well: it already reproduces the measured ν₂/n ∈ [0.42,0.52]. The new carry setting
  reproduces it exactly — the borrow count of the two's-complement chain IS ν₂ by
  construction, and its i.i.d. stationary density Bernoulli(1/2) matches the measured
  ~0.5, so the setting covers the case the old one was already handling. This is not a
  restatement: the carry chain additionally supplies the mixing mechanism (Diaconis–
  Fulman) that the bare F2-linear transfer lacked.
side: regeneration / supply (attacks the single open G-supply statement ν₂ > n^β by
  making the F2-linear descent map explicit and handing its density to a named
  carry-mixing theorem); erosion is settled and untouched.
named-mathematics: Diaconis–Fulman carries, two's-complement subtraction, Mealy/Moore
  transducers, Markov-chain stationary measures, 2-separation / non-concentration (CHT,
  Ross 2026).
speculative: The honest status is conditional — the carry chain gives the MIXING
  mechanism, but the non-concentration of the prime-gap bits h_j is exactly the
  unproved hypothesis (it is CHT condition (ii) / the 2-separation hypothesis, itself
  as hard as the conjecture in general, though the primes are believed to satisfy it
  strongly). The value is: the open statement is now pinned to ONE decorrelation
  property of ONE named automaton, with an explicit stationary measure to beat.
falsifier: If the carry chain fed by the actual prime-gap bits does not mix (its
  empirical stationary density can be made arbitrarily small by a 2-separated input
  that the primes might satisfy), then the carry machinery adds no new lower bound over
  the already-measured transfer, and the approach collapses back to chebyshev-bias's
  "conditional at Hardy–Littlewood level". That collapse is a real result, not a
  failure: it would prove the decorrelation hypothesis is the wall.
