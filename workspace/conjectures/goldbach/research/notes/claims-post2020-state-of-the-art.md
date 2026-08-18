# Claims: post-2020 state of the art (Chen constant, distribution level, parity survey)

New sources landed this cycle, closing three thin spots in the library:
(1) the Chen-count constant had stalled at 0.867 in the claims ledger, but the
record has moved three times since (0.899 Wu 2008, 1.733 Runbo Li 2024 preprint,
1.9728 Runbo Li 2024/2025 v4); (2) the first Goldbach bound using a level of
distribution beyond the square-root barrier (Lichtman 2023); (3) the full text
of Friedlander–Iwaniec, "Exceptional zeros, sieve parity, Goldbach" (the parity
survey was abstract-only on disk before).

Each claim cites the source in `research/sources/` that establishes it, with
hypotheses and falsifier.

```claim
id: chen-count-constant-1.9728
statement: (Runbo Li, "On Chen's theorem, Goldbach's conjecture and almost prime twins II", Math. Reports 28(78) (2026) 39–61, DOI 10.59277/mrar.2026.28.78.1.2.39 — published; arXiv:2405.05727v4) For every sufficiently large even integer N, the number D_{1,2}(N) of primes p such that N − p has at most two prime factors satisfies D_{1,2}(N) ≥ 1.9728·C(N)·N/(log N)^2, where C(N) = ∏_{p>2}(1 − 1/(p−1)^2)·∏_{p|N, p>2}(p−1)/(p−2). This is within 1.36% of the conjectured asymptotic constant 2 for D_{1,1}(N) (the Goldbach representation count). Record chain per the paper: Chen 0.67 → 0.689 (Halberstam–Richert) → 0.7544, 0.81 (Chen) → 0.8285 (Cai–Lu) → 0.836, 0.867, 0.899 (Wu/Cai/Wu) → 1.733 (a different 2024 preprint [13] of the same author) → 1.9728 (this paper). Note: arXiv:2405.05727 v1 itself proves 1.253, not 1.733; the "1.733" the paper cites is the separate preprint [13].
hypotheses: N sufficiently large even; the constant 1.9728 is a lower-bound coefficient in the Chen-type weighted sieve.
holds-here: yes — this is the current record lower-bound constant for Chen's theorem (p + P2), superseding claim chen-count-constant-0.867 (the 0.867 claim is retired).
status: proved (by source, published in Math. Reports 2026)
evidence: Runbo Li, "On Chen's theorem, Goldbach's conjecture and almost prime twins II", Math. Reports 28(78) (2026) 39–61, DOI 10.59277/mrar.2026.28.78.1.2.39; arXiv:2405.05727v4, Theorem 1.1, full text at research/sources/runbo-li-chen-theorem-goldbach-almost-prime-twins-II-arxiv-2405.05727.html.full.md. Publication confirmed by this audit's live search.
falsifies: an independent check of the proof showing a gap in the weighted-sieve or distribution-level inputs; a referee rejection identifying a flaw.
```

```claim
id: runbo-li-twin-1.2759
statement: (Runbo Li 2024, arXiv:2405.05727v4, Theorem 1.3) For sufficiently large x, the count π_{1,2}(x) of primes p ≤ x with p + 2 having at most two prime factors satisfies π_{1,2}(x) ≥ 1.2759·C_2·x/(log x)^2, where C_2 = 2∏_{p>2}(1 − 1/(p−1)^2) is the twin-prime constant. This uses Pascadi's new distribution level.
hypotheses: x sufficiently large; C_2 as defined.
holds-here: yes — a companion Chen-type result for the twin-prime problem, using the same sieve machinery as the Goldbach constant.
status: asserted-by-source (arXiv preprint v4)
evidence: same source as chen-count-constant-1.9728, Theorem 1.3.
falsifies: an independent check of the proof showing a gap.
```

```claim
id: pintz-I-explicit-formula-major-arcs
statement: (Pintz 2018, arXiv:1804.05561, Theorem 1) There is a new explicit formula for the contribution of the major arcs in the Goldbach problem (and Generalized Twin Prime Problem), valid with the major-arc level P_0 ≤ X^{4/9−ε}. For all m ≤ X, R_1(m) (the weighted Goldbach major-arc contribution) equals a double sum over exceptional zeros (ϱ_i, χ_i) ∈ ℰ of A(ϱ_i)A(ϱ_j)𝔖(χ_i,χ_j,m)·Γ(ϱ_i)Γ(ϱ_j)/Γ(ϱ_i+ϱ_j)·m^{ϱ_i+ϱ_j−1}, plus error O_ε(𝔖(m)Xe^{−c_εH}) + O_ε(X^{1−ε_0}); with a restricted summation (|γ_i| ≤ U, [r_1,r_2] ≤ P, U(χ_1,χ_2,m) ≤ U) an additional error O(𝔖(m)X log U/√U) appears. If there is no Siegel zero one may take H, U large constants. Consequently, for all but O(X^{3/5+ε}) values of m ∈ [X/2,X], R_1(m) ≫_ε m^{1−ε} and R_1'(m) ≫_ε m^{1−ε}.
hypotheses: P_0 ≤ X^{4/9−ε}; P chosen in [P_0 X^{−ε}, P_0]; ℰ = set of exceptional (zero, character) pairs; 𝔖(m) the singular series; H, U parameters; at most one simple Siegel zero (Lemma 4.13).
holds-here: yes — this is the technical core of Pintz's Part II (E(X) < X^0.72), and the explicit-formula foundation for the exceptional-set density route (goal full-goldbach-via-exceptional-set, Lemma A needs E(X) ≪ X^{2/3}).
status: proved (by source, arXiv preprint 2018)
evidence: J. Pintz, "A new explicit formula in the additive theory of primes with applications I...", arXiv:1804.05561v1, Theorem 1; full text at research/sources/pintz-explicit-formula-additive-theory-primes-I-goldbach-arxiv-1804.05561.html.full.md.
falsifies: an independent check of the major-arc dissection or Siegel-zero handling showing a gap; a referee rejection.
```

```claim
id: chirre-hagen-short-interval-RH-123
statement: (Chirre–Hagen 2025, arXiv:2512.23534, Theorem 1) Assume the Riemann Hypothesis. Then for all x ≥ 2, there is a Goldbach number (an even integer expressible as a sum of two primes) in the interval (x, x + 123·log²x]. This improves Cully-Hugill–Dudek's constant 9696 to 123. Method: explicit formula for ψ(x) + Saffari–Vaughan averaging, working directly with zeros of ζ(s); the delicate step is passing from J_ψ(x,δ) to J_θ(x,δ) (primes in short intervals).
hypotheses: RH assumed; x ≥ 2; Goldbach number = even integer = p1+p2 (at least one representation).
holds-here: yes — a current conditional restricted-class result on the location of Goldbach numbers, directly relevant to the exceptional-set structure (where counterexamples provably cannot be, under RH).
status: asserted-by-source (arXiv preprint v1, Dec 2025; not yet refereed in a venue we hold)
evidence: A. Chirre, M. Valås Hagen, "On Goldbach numbers in short intervals", arXiv:2512.23534v1, Theorem 1; full text at research/sources/chirre-hagen-goldbach-numbers-short-intervals-RH-arxiv-2512.23534.html.full.md.
falsifies: an independent check of the explicit zero/ψ(x) estimates showing a gap; a referee rejection identifying a flaw.
```

```claim
id: lichtman-level-66-107
statement: (Lichtman 2023, arXiv:2309.08522) The primes have level of distribution 66/107 ≈ 0.617 using triply well-factorable weights, the highest in any setting, improving Maynard's 3/5 = 0.60; conditionally on Selberg's eigenvalue conjecture this extends to 5/8 = 0.625. This is the first level of distribution beyond the square-root barrier (x^{1/2}) used for the Goldbach problem.
hypotheses: Siegel–Walfisz condition; unconditionally 66/107, conditionally 5/8 on Selberg's eigenvalue conjecture.
holds-here: yes — the load-bearing equidistribution input for the record Goldbach upper bound and Chen-constant improvements.
status: proved (by source, arXiv preprint 2023; not yet refereed in a venue we hold)
evidence: J.D. Lichtman, "Primes in arithmetic progressions to large moduli, and Goldbach beyond the square-root barrier", arXiv:2309.08522, Theorem 1.7, full text at research/sources/lichtman-goldbach-beyond-square-root-barrier-arxiv-2309.08522.html.full.md.
falsifies: an independent check of the spectral large sieve estimates showing a gap; a referee rejection.
```

```claim
id: lichtman-goldbach-upper-3.3907
statement: (Lichtman 2023, arXiv:2309.08522, Theorem 1.2) For every sufficiently large even integer a, the number G(a) of Goldbach representations satisfies G(a) ≲ 3.3907·Π_a(a), where Π_a(a) is the Hardy–Littlewood singular-series main term. This is the greatest improvement on the Goldbach upper bound since Bombieri–Davenport 1966 (which had 4), refining Wu 2004 (3.9104); it is the first Goldbach bound using a level of distribution beyond the square-root barrier.
hypotheses: a sufficiently large even; G(a) the count of representations as a sum of two primes.
holds-here: yes — the record upper bound on Goldbach representations, a counterpart to the Chen lower bound.
status: proved (by source, arXiv preprint 2023)
evidence: same source as lichtman-level-66-107, Theorem 1.2, full text on disk.
falsifies: an independent check of the linear-sieve estimates showing a gap; a referee rejection.
```

```claim
id: parity-problem-survey-2022
statement: (Friedlander–Iwaniec 2022, "Exceptional zeros, sieve parity, Goldbach", Essential Number Theory 1(1), 13–39) The parity problem is a proven structural limitation of the linear sieve (upper/lower-bound functions F(s), f(s) of Jurkat–Richert cannot distinguish odd/even numbers of prime factors in general); recent work ties weak forms of the Goldbach conjecture to the nonexistence of exceptional (Siegel) zeros of Dirichlet L-functions, and this can be viewed in a generalized sieve framework.
hypotheses: none — survey, not a new theorem; states the parity barrier and the Goldbach–Siegel-zero connection.
holds-here: yes — the canonical statement of Obstruction A (parity problem) for this run, now full-text on disk.
status: asserted-by-source (peer-reviewed survey, Essential Number Theory 2022)
evidence: J. Friedlander, H. Iwaniec, "Exceptional zeros, sieve parity, Goldbach", Essential Number Theory 1 (2022) no. 1, 13–39, DOI 10.2140/ent.2022.1.13, full text at research/sources/friedlander-iwaniec-exceptional-zeros-sieve-parity-goldbach-ent-2022-fulltext.full.md.
falsifies: a construction showing a linear-sieve weight that does distinguish parity (contradicting the survey's framework).
```
