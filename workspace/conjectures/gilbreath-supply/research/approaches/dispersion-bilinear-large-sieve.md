# Attack the dyadic-gap character correlation itself with analytic number theory — dispersion method and the large sieve

```approach
idea: >
  The three adopted routes (dyadic-gap character correlation, Krawtchouk second
  moment, Lucas mixing) all leave the SAME arithmetic input as an abstract,
  unpriced correlation statement: S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} is a sum of
  products of the quadratic character χ_4(q_j) = (−1/q_j) = (−1)^{(q_j−1)/2}
  along the primes at dyadic index shifts. Nobody has attacked THAT sum with the
  machinery that exists for exactly this shape of bilinear character sum. Do it:
  square S, average over n, and bound the resulting 4-fold correlation of χ_4
  along the prime sequence with Linnik's dispersion method and the large sieve.
  The target is Σ_{n≤N} S(n)² = O(N^{2−δ}) for some δ > 0, which by Chebyshev
  gives S(n)/n → 0 in L², hence ν₂(n)/n → 1/2 on a density-1 set (GOAL priority 1).

mechanism: >
  By the run telescope already on disk, (−1)^{T(n,d)} = ∏_{R ∈ runs(↓d)}
  χ_4(q_{a_R}) χ_4(q_{b_R}) where every run R has the same length 2^{ν₂(d+1)},
  so b_R − a_R = 2^{ν₂(d+1)} and there are 2^{popcount(d)−ν₂(d+1)} runs. Hence
  S(n) is a sum over dyadic-shift patterns of products of a single multiplicative
  character evaluated at consecutive-prime-index shifts. Squaring:
  Σ_{n≤N} S(n)² = Σ_{n} Σ_{d,d'≤n} ∏_R ∏_{R'} χ_4(...)χ_4(...). The d=d' term
  is the trivial diagonal (n−2). The off-diagonal terms are correlations of χ_4
  along the PRIME INDEX at controlled separations — a bilinear form in the
  prime-indexed character sequence. This is precisely the shape Linnik's
  dispersion method was built for (a bilinear form in the von Mangoldt / prime
  sequence: swap the role of the two variables, then apply the large sieve to
  the resulting value-shifted correlation of χ_4). The classical boundary input
  is PNT in AP mod 4 (Σ_{p≤x} χ_4(p) = o(π(x)) unconditionally by Siegel–Walfisz),
  which is the ONE-point statistic; the dispersion method is the standard device
  for promoting one-point control of a character along primes to two/four-point
  correlation control. This route names a toolbox, not a heuristic: dispersion
  (Linnik), large sieve (Bombieri–Davenport), and the Siegel–Walfisz / PNT-in-AP
  estimate for the conductor-4 character. All are classical, citable, and none
  has been applied to THIS sum in this workspace.

status: refuted

precedent: >
  The toolbox is real and is classically applied to VALUE-shifted character
  sums — but every settled instance evaluates χ at a shifted INTEGER argument,
  which is exactly the hypothesis that fails here. Sources:
  - Karatsuba-school shifted-prime estimates: "Sums of Values of Nonprincipal
    Characters over a Sequence of Shifted Primes", Proc. Steklov Inst. Math.
    (2018), DOI 10.1134/S0081543817080156 — Σ_{n≤x} Λ(n)χ(n−l) = O(x exp(−0.6√log D))
    for (l,D)=1, cube-free conductor: a VALUE shift n−l.
  - "Shifted character sums with multiplicative coefficients, II", J. Number
    Theory (2018), DOI/URL https://www.sciencedirect.com/science/article/pii/S0022314X17301178 —
    Σ_{n≤N} f(n)χ(n+a) and Σ f(n)χ(n+a_1)…χ(n+a_t) ≪ N loglog q/log q for q prime,
    (a,q)=1: again integer shifts a of the argument.
  - Fouvry–Radziwill, dispersion for narrow type-II sums, Chebyshevskii Sb. (2019),
    DOI 10.22405/2226-8383-2018-19-3-148-163 — a Siegel–Walfisz sequence α*β has
    exponent of distribution 1/2+δ in a weak sense; still a value-domain bilinear
    form α_mβ_n with mn ≡ a (mod q).
  - Large sieve: Bombieri's inequality (value-domain residue classes), e.g.
    https://www.cambridge.org/core/journals/mathematika/article/abs/large-sieve/4DC1EC8072D840195F1EF81F5828BB0F
  - Inside-workspace parity barrier: abgs-p1-wide-open, abgs-pair-frequency-equality-open,
    lau-nonconstant-pattern-open, los-switch-preferred-mod4 (all asserted/heuristic).

killed-by: >
  The value-shift step of the large sieve / dispersion method does not apply.
  Every result in the shifted-character literature bounds χ at a shifted INTEGER
  argument (n−l, n+a, n+a_i) with the shift in the value index; the object here
  correlates χ_4(q_j)·χ_4(q_b) at two PRIME VALUES indexed by a prime-INDEX
  separation b−a = 2^{ν₂(d+1)}. q_{j+2^g} is not q_j plus a constant, so there is
  no integer shift for dispersion to feed on — the bilinear form lives in the
  prime index, not the value. Concretely, the g=0 (separation 2^0 = 1, index-adjacent)
  terms of S(n)² are products containing χ_4(q_j)χ_4(q_{j+1}), i.e. exactly the
  mod-4 pair-switch object, and its positivity/vanish is the named open problem
  ABGS §9 ("cannot be treated using L-functions") and Lau's
  lau-nonconstant-pattern-open (even ONE non-constant 2-term pattern is unproved
  to occur infinitely often). So the second moment Σ S(n)² contains, and must
  control, the very correlation whose sign is open; a O(N^{2−δ}) bound is not
  reachable without resolving positive mod-4 switch density. The route therefore
  does not escape the parity barrier — it re-encounters it at the coarsest dyadic
  scale — and offers no input weaker than switch density.

first-step: >
  (parked) tool_builder: the mechanical derivation in the original first-step
  (assert Σ_{n≤N}S(n)² against the oracle, stratify by ν₂(d+1),ν₂(d'+1),|d−d'|)
  is still worth running as a MEASUREMENT — it will confirm that the dominant
  off-diagonal mass sits at small |d−d'| where the switch-pair correlation lives —
  but it cannot supply the missing arithmetic: the per-stratum magnitudes are
  empirical, and the theorem that would need them is unavailable precisely
  because the g=0 stratum is the open parity barrier. Run it only as a diagnostic
  that records, not as the engine of a proof.
```

## Research verdict (grounding check)

**The reformulation is named and the toolbox is real — but its settled theorems
are all for VALUE shifts, and the shift here is in the prime index, so the
engine's one load-bearing hypothesis fails.**

**What it is called.** The object is a *bilinear character sum over the prime
sequence at index shifts*; the machinery is *Linnik's dispersion method* combined
with the *large sieve* (Bombieri–Davenport). All classical, all citable, and each
surviving application above is real and precise.

**Why the hypotheses fail here.** The two settled references above (Steklov 2018,
JNT 2018) and the Fouvry–Radziwill dispersion estimate all bound χ at shifted
*integer* arguments `n−l`, `n+a`, or a value-domain bilinear form `α_mβ_n` with
`mn ≡ a (mod q)`. Dispersion's power is precisely the *value* shift: the one-point
control of χ (Siegel–Walfisz) is promoted to two-point control of χ value-shifted.
Here the correlation is `χ_4(q_j)χ_4(q_{j+2^g})`: the two primes are separated in
the *index*, and `q_{j+2^g} − q_j` is not a fixed integer. No dispersion/large-sieve
argument that evaluates χ at value shifts reaches a prime-index-separated
correlation, and none in the literature does.

**The decisive point: the g=0 stratum is the parity barrier itself.** At index
separation `2^0 = 1`, the product factors reduce to `χ_4(q_j)χ_4(q_{j+1})` — the
mod-4 switch indicator. Its positive density is exactly the ABGS §9 open problem
(`abgs-p1-wide-open`: the pair-frequency asymptotics "cannot be treated using
L-functions"; `lau-nonconstant-pattern-open`: even a single (1,3)/(3,1) pattern is
unproved to occur infinitely often). A `Σ_{n≤N}S(n)² = O(N^{2−δ})` bound must
control the four-fold correlations, which contain the two-fold pair-switch object
as a restriction; bounding them unconditionally resolves the switch side, which is
open. So the route's target is not one step past Siegel–Walfisz; it is one step
past the parity barrier.

**Does it reopen a closed door?** No door directly, but it is the switch-density
dead end wearing the dispersion costume: it imports the open positive-switch-density
input, merely at higher (4-fold) order. As a route to SUPPLY from an input weaker
than switch density: **refuted**.

## Sources
- Steklov 2018 shifted-primes character sums, DOI 10.1134/S0081543817080156.
- JNT 2018 "Shifted character sums with multiplicative coefficients, II",
  https://www.sciencedirect.com/science/article/pii/S0022314X17301178.
- Fouvry–Radziwill narrow type-II dispersion, DOI 10.22405/2226-8383-2018-19-3-148-163 (2019).
- Cambridge large sieve survey, https://www.cambridge.org/core/journals/mathematika/article/abs/large-sieve/4DC1EC8072D840195F1EF81F5828BB0F.
- Parity barrier claims: abgs-p1-wide-open, abgs-pair-frequency-equality-open,
  lau-nonconstant-pattern-open (research/summaries/ash_beltis_gross_sinnott_prime_residues.md,
  research/summaries/lau_residue_patterns.md).
