# Summary — Mauduit–Rivat, "Sur un problème de Gelfond : la somme des chiffres des nombres premiers"

Source: Christian Mauduit, Joël Rivat, "Sur un problème de Gelfond : la somme des chiffres des nombres premiers", *Annals of Mathematics* 171(3) (2010) 1591–1646. DOI 10.4007/annals.2010.171.1591.
Source URLs: HAL record https://hal.science/hal-02530074 (metadata/DOI); primary PDF http://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p04-p.pdf. Full text: `research/sources/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.full.md`.

## What this source establishes

This is the **primary** reference answering Gelfond's 1968 question about the digit sum of primes. `s_q(n)` denotes the base-q sum of digits of n, `Λ` the von-Mangoldt function.

**Théorème 1.** For q > 2 and α with (q−1)α ∉ ℤ, there is σ_q(α) > 0 such that
`Σ_{n≤x} Λ(n) e(α s_q(n)) = O_{q,α}(x^{1−σ_q(α)})` — a power-saving exponential-sum bound for the digital function along primes.

**Théorème 2.** For q > 2, the sequence (α s_q(p)) over primes p is equidistributed modulo 1 iff α ∈ ℝ∖ℚ.

**Théorème 3.** For q and m > 2 integers, there is σ_{q,m} > 0 such that for all a ∈ ℤ,
`card{p ≤ x : s_q(p) ≡ a (mod m)} = ((m, q−1)/m) π(x; a, (m,q−1)) + O_{q,m}(x^{1−σ_{q,m}})`.
The count of primes with digit sum in a given residue class has the equidistribution main term (proportional to the count of primes in the forcing congruence class a mod d, d = (m,q−1)) with a power-saving error. This **completely answers Gelfond's second problem**.

**Important scope note — the binary q=2 case.** Theorem 3 is stated for q > 2 and m > 2. The binary case (q = 2, the parity of the binary digit sum — equivalently the Thue–Morse function along primes) is the special case Green's notes prove with a self-contained Type I/II sum argument: `E_{n≤X} Λ(n)(−1)^{s(n)} = O(X^{−δ})`, i.e. exactly half the primes have odd binary digit sum. Both halves of the canonical tier are now local.

## Why it bears on SUPPLY (and its precise limit)

Same bearing as `research/summaries/green_three_topics_additive_prime_number_theory.md` (whose claim `mauduit-rivat-prime-digit-sum-equidistributed` records the binary case). This paper is the **primary, unconditional, power-saving** statement that the digit-sum statistic is equidistributed along the primes — the model for what a "weak arithmetic input the primes provably satisfy" looks like, directly relevant to GOAL priority 2 (weakest arithmetic input) and the Walsh-side of open request `walsh-spectral-subset-b904`.

**It does NOT close request `walsh-spectral-subset-b904`, and must not be filed as doing so** (same restriction as the Green-notes claim, reinforced here). The theorem is about the digit sum `s_q(p)` of the prime p. SUPPLY's fold Φ reads a *different* string: the gap-parity `h[j] = ((q_{j+1}−q_j)/2) mod 2`. No transfer from "digit sum of p is equidistributed" to "the gap-parity string h is generic under the submask-XOR fold Φ" is present in this source or anywhere in the library. It fixes the paradigm; the finite transfer remains the open core.

## Evidence class

Proved. Peer-reviewed primary reference (Annals of Mathematics). The power-saving exponential-sum bound and the equidistribution theorems are unconditional.

```claim
id: mauduit-rivat-gelfond-sum-of-digits-primes-equidistributed
statement: For q,m>2, #{p≤x : s_q(p)≡a (mod m)} = ((m,q−1)/m)·π(x; a, (m,q−1)) + O_{q,m}(x^{1−σ_{q,m}}); and for q>2 the sequence (α s_q(p)) over primes is equidistributed mod 1 iff α∉ℚ. The digit-sum statistic of primes is equidistributed with a power-saving error — answering Gelfond's second problem.
hypotheses: q ≥ 3, m ≥ 3 integers; s_q the base-q sum of digits; π(x;a,d) the count of primes ≤ x congruent to a mod d; σ constants > 0; α real.
holds-here: Yes as an unconditional theorem about the primes (the run may cite "the prime digit-sum is equidistributed"). It concerns s_q(p), the digit sum of the prime p — NOT the gap-parity string h[j]=((q_{j+1}−q_j)/2) mod 2 that the fold Φ reads. The binary q=2 case is in the Green-notes claim mauduit-rivat-prime-digit-sum-equidistributed.
status: proved (Mauduit–Rivat, Annals of Math 171(3) 2010)
bearing: Primary, unconditional, power-saving example of a weak arithmetic input the primes provably satisfy — the paradigm for GOAL priority 2's weakest-input question and the Walsh-side of request walsh-spectral-subset-b904. Does NOT close that request: the statistic (digit sum s_q(p)) differs from h (gap parity mod 2) and the transfer is absent. Records the model theorem, not the answer.
anchor: research/sources/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.full.md (Théorèmes 1–3, lines 284–305)
```

## What would falsify its bearing as a proof input

As with the Green-notes claim: treating this as a proof of `wt(Φ_n h) ≥ c·n` would fail, because the theorem is about s_q(p) (digit sum of the prime) while h encodes mod-4 gap structure. A valid use needs a demonstrated reduction of h's submask-window correlations to digit-sum correlations, or a separate argument that the fold only needs the digit-genericity Mauduit–Rivat supplies. Neither is established. As context it is correct and load-bearing for the paradigm; as a proof input it is inert until that transfer is given.
