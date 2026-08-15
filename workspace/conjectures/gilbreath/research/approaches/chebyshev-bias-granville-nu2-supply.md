# Chebyshev-bias / prime-gap-mod-4 fluctuation bound for Granville's ν₂ supply

```claim
id: rubinstein-sarnak-fluctuation-not-bias
statement: Rubinstein–Sarnak 1994 (Experimental Math 3(3):173–197): under GRH+GSH the mod-4 prime race π(x;4,3) vs π(x;4,1) has explicit Fourier transform exp(iΣc(q,a_j)ξ_j)·Π_{χ,γ}J0(...) with the exponential bias-shift factor the source of the Chebyshev bias; δ(P_{4;3,1}) = 0.9959 (bias toward primes ≡3 mod 4), but the sign oscillates (Littlewood; first 1-leads point 26861) so NO one-sided unconditional bias holds. LOS-2017 (arXiv:1709.06168) Theorems 1.1–1.3: the secondary fluctuation term in consecutive-prime (mod q) pattern biases has a continuous symmetric-about-0 limiting distribution as q→∞ (e.g. (1/q)#{k: C(k)≤(e^γ/2)x}=Φ_C(x)+o(1), Φ_C(−x)+Φ_C(x)=1), connected to Dedekind-sum Fourier transforms.
hypotheses: GRH and (for the explicit value / symmetry) GSH/LI for the zeros of Dirichlet L-functions; primes, not a general 2-then-odds class.
holds-here: yes (supplies the fluctuation lens, not a one-sided bias, for the two-point mod-4 switch statistic bit_n=[p_{n+1}≢p_n mod 4] feeding Granville's ν₂)
status: sourced (clean primary Rubinstein–Sarnak Project Euclid text + LOS-2017 arXiv full text both held and read)
bearing: Route B supply side. The honest deliverable is a FLUCTUATION bound at GRH/LI + Hardy–Littlewood/Dedekind-sum level, never an unconditional one-sided density. These sources confirm ν₂ is two-point (consecutive-pair mod-4 switch), NOT a one-point PNT-in-AP statistic; neither proves the open lower bound ν₂ ≥ n^{0.525+δ}.
anchor: research/sources/rubinstein-sarnak-1994-chebyshev-bias-full.full.md, research/sources/lemke-oliver-soundararajan-2017-prime-biases-sawtooth.full.md, research/summaries/maynard-2015-small-gaps-between-primes.md, research/summaries/lau-2024-residue-class-patterns-consecutive-primes.md
answers: what-named-machinery-supplies-nu2
```

```approach
idea: Supply the missing density input to the already-proved Granville Lemma 5.4 reduction by bounding, via analytic number theory (Dirichlet/PNT-in-AP, Chebyshev's bias, Bombieri–Vinogradov / GRH, Hardy–Littlewood correlations), the frequency of the prime-gap residue class that feeds the descent coefficient ν₂ = #{c_s = 2}, turning "ν₂ > n^β" from an open measurement into a conditional theorem.
mechanism: GOAL.md records the current state: Route B has Lemma 5.4 proved (this run), and "the whole of Route B now rests on the single open density statement G-supply (ν₂(q_n) > n^β, β > 0.525), which reduces cleanly to a prime-gap-mod-4 frequency bound." The missing object is therefore not a new reformulation of the operator but a named theorem that delivers that frequency bound. The key step is to pin down WHICH mod-4 statistic feeds ν₂ — a one-point statistic (primes in a residue class, handled by Dirichlet/PNT-in-AP) or a two-point correlation (consecutive primes p_n, p_{n+1} in prescribed residue classes mod 4, handled by the Hardy–Littlewood r-tuple / Bateman–Horn conjecture, or in short intervals by Gallagher's Poisson model, already in the library). If it is one-point, then ν₂(n) = n/2 − O(n^{θ}) follows from PNT-in-AP with θ = 1/2+ε (Bombieri–Vinogradov) or θ = 1/2 (GRH), and n/2 − O(n^{1/2+ε}) > n^{0.525} for large n gives GC as a corollary of Lemma 5.4 — a clean conditional partial result. If it is two-point, the honest statement is conditional on a correlation bound at Hardy–Littlewood level, still a real contribution because it isolates exactly which conjecture about prime gaps suffices. The Chebyshev-bias literature (Rubinstein–Sarnak 1994) is the right lens for the SECOND-order term: it tells us the sign of the bias and, crucially, that the bias oscillates (Littlewood-type), so no single-sided bias can be asserted unconditionally — the honest deliverable is a fluctuation bound, not a bias assertion.
status: adopted
disposition: (a) attached to G-supply — the bound it would give: ν₂ = n/2 + O(n^{1/2+ε}) from a two-point consecutive-prime mod-4 correlation (bit_n = [p_{n+1} ≢ p_n (mod 4)]), which yields ν₂ > n^β and hence GC via the re-derived Lemma 5.4; honest status is conditional at Hardy–Littlewood / Lemke Oliver–Soundararajan level, not unconditional (Directive 44 item 2).
precedent: >
  [Librarian 2026 addition:] A decisive negative confirmed — the supply bound
  ν₂ > n^β is NOT unconditional and NOT provable from PNT-in-AP or Shiu-level
  methods. The strongest unconditional result in the consecutive-prime mod-4
  landscape, Shiu 2000 "Strings of Congruent Primes" (J. LMS (2) 61, 359–373),
  proves the OPPOSITE direction the supply needs — infinitely many and
  arbitrarily long equal-residue (non-switch, gap ≡ 0 mod 4) runs — so it gives
  no quantitative or density lower bound on the switch count (gap ≡ 2 mod 4).
  The switch count is provable only at the Hardy–Littlewood / Lemke Oliver–
  Soundararajan conjecture level. Ruzsa "Consecutive primes modulo 4" (Indag.
  Math. 2003) is paywalled; its abstract-level π_11(x) bound is an infinitude
  bound, not positive density. Net: a conditional result ("IF the mod-4 switch
  count has positive density, THEN GC via Lemma 5.4") is the honest ceiling;
  the hypothesis cannot be upgraded to unconditional with held or found
  methods. See research/summaries/shiu-2000-strings-of-congruent-primes.md.
  The named analytic-number-theory machinery is real and this candidate's
  framing is CORRECT and checkable — resolved as TWO-POINT, not one-point.
  - https://doi.org/10.1080/10586458.1994.10504289 (Rubinstein–Sarnak,
    Chebyshev's Bias, Exp. Math. 3.3: under GRH + Grand Simplicity
    Hypothesis, the residue-class race has a well-defined logarithmic density
    — the correct lens for the second-order oscillation, and it oscillates —
    Littlewood-type — so no one-sided bias is unconditional.)
  - https://www.pnas.org/doi/10.1073/pnas.1605366113 (Lemke Oliver &
    Soundararajan, "Unexpected biases in the distribution of consecutive
    primes", PNAS 113, 2016 — the consecutive-prime residue-class-pair
    two-point correlations; the atomic bit that feeds ν₂ is precisely a
    consecutive-pair mod-4 switch, which is a two-point statistic under
    Hardy–Littlewood.)
  - https://doi.org/10.1007/s11511-010-0044-9 (Maynard, "Primes in tuples II",
    Acta Math. 204 — the two-point/small-gap correlation machinery; also the
    run's own claim gap-bounds-cannot-force-block-growth.)
  - https://arxiv.org/abs/2409.12819 (Lau 2024, residue-class patterns of
    consecutive primes, via a Maynard–Tao sieve — two-point consecutive-prime
    residue attainability.)
  - claims: granville-nu2-density-measured (ν₂/n ∈ [0.42,0.52] to n=3999,
    factor-26 margin over n^0.525), mod4-linearization,
    fwd-diff-identity-refuted (the linearization is parity-only and does not
    fix exact {0,2} values), block-growth-literature-not-covered.
  Two decisive findings from THIS run's derivation (code/out/check_nu2_one_vs_two_point.notes.md):
  (1) ν₂ is TWO-POINT, not one-point: the atomic bit is
  bit_n = [p_{n+1} ≢ p_n (mod 4)], i.e. the contiguous-pair residue switch,
  not a count of a single residue class. So PNT-in-AP / GRH-for-Dirichlet-L
  does NOT give ν₂ > n^β by itself; the supply needs the joint
  consecutive-prime residue distribution (Hardy–Littlewood /
  Lemke Oliver–Soundararajan level), or a spectral/fluctuation bound at the
  Rubinstein–Sarnak level. (2) The Chebyshev-bias caution is load-bearing: the
  second-order term oscillates (Littlewood-type), so the honest deliverable is
  a FLUCTUATION bound, never a one-sided bias claim.
buy: >
  The reduction is correct: GC reduces (via the proved Lemma 5.4 / Theorem 5.5
  and the run's own measurement ν₂ ~ n/2) to ν₂ > n^β for any β > 0.525, and
  the empirical margin (factor 26 at n=3999) is huge. The honest conditional
  theorem is: IF a two-point bound gives ν₂ = n/2 + O(n^{1/2+ε}) (or even the
  much weaker ν₂ > n^{0.525+something}), THEN GC holds — at the
  Hardy–Littlewood / Lemke Oliver–Soundararajan fluctuation level. This is a
  real partial result GOAL.md would count (a proved statement under a stated
  prime-gap hypothesis). The dichotomy the candidate posed is answered: two-point.
  Equal caution: this is about PRIME-SPECIFIC residue density entering a
  proved reduction — it cannot be the theorem for a general 2-then-odds class
  (Eppstein 2011 kills any bounded-gap class theorem), and it inherits
  Granville's own conditional status (his Conjecture 5.1 supplies the
  lower-bound form). The value is isolating EXACTLY which conjecture about
  consecutive-prime residues suffices — the single most informative fact the
  reduction can yield.
first-step: >
  Write the exact conditional bound as a checkable predicate and verify its
  two numerical ingredients against the oracle. (a) Recompute ν₂(q_n) for
  n = 1..3999 from the right diagonal of the prime-difference triangle
  (sieve the primes, form the halved gap diagonal, XOR/Rule-90 descent) and
  confirm ν₂/n ∈ [0.42, 0.52] with the factor-26 margin over n^0.525 at
  n = 3999, reproducing `granville-nu2-density-measured` independently.
  (b) State the target hypothesis precisely — there exists δ > 0 such that
  ν₂(q_n) ≥ n^{0.525+δ} for all large n — and check the needed direction:
  the measured constant 1/2 exceeds 0.525, so the demand is the WEAK lower
  bound ν₂ ≥ n^{0.525+δ}, not the full Gaussian ν₂ = n/2 + O(n^{1/2+ε}).
  Deliverable of this step: a machine-checked statement "IF ν₂(q_n) ≥
  n^{0.525+δ} for all large n (a two-point consecutive-prime mod-4 switch
  bound) THEN GC holds via Lemma 5.4", with the conditional theorem's
  hypothesis written as a single named prime-gap assumption (Hardy–Littlewood
  level) and the implication's logic traced step-by-step through the proved
  reduction. The proof of the IF itself is the next step; this step produces
  the exact statement, the verified margin, and the oracle-checked atomic bit
  identity bit_n = [p_{n+1} ≢ p_n (mod 4)].
side: regeneration (supplies the density the proved Lemma 5.4 consumes; erosion is already settled)
named-mathematics: Dirichlet's theorem / prime number theorem in arithmetic progressions, Chebyshev's bias, Rubinstein–Sarnak logarithmic densities, Bombieri–Vinogradov theorem, GRH zero-density / error terms, Hardy–Littlewood prime r-tuple conjecture, Gallagher's Poisson short-interval model.
speculative: Whether ν₂ is one-point or two-point in mod-4 determines whether this is a GRH-level or a Hardy–Littlewood-level conditional result; that distinction is exactly what the first step resolves, and it is the single most informative fact the run can extract from Granville's reduction.
falsifier: If ν₂ turns out to be a two-point correlation AND the required correlation bound is provably beyond BHP (as CHT's authors already found for their own obstruction, "looks difficult to establish rigorously"), then the route is a conditional-result at Hardy–Littlewood level, not a proof — still a deliverable, but the file must say so rather than presenting ν₂ > n^β as reachable from PNT-in-AP alone.
