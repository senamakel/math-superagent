# Claims: exceptional set, circle method, and the ternary theorem

Established by the sources in `research/sources/`. Each claim cites the source
that establishes it, with hypotheses and falsifier.

```claim
id: structural-closure-analogue-refuted
statement: The inference "if n_0 is the least Goldbach counterexample then the
  exceptional set E(X) has positive lower density (E(X) >> X)" is not
  supported by any known structure: minimality alone gives no closure
  operation, translation-by-modulus and multiplication-by-prime do not
  preserve the exact additive primality predicate, and the singular-series
  main term is only a local (major-arc) feature that says nothing about
  minor-arc cancellation. This is a refutation of the proposed analogy,
  not of the conditional skeleton (an upper bound E(X)=O(X^(2/3)) plus a
  proven lower bound E(X)>>X would indeed force E(X)=0).
hypotheses: none — this is an attack on a proposed structural lemma, not a
  theorem about primes; the conditional skeleton itself is untouched.
holds-here: yes — the backward decomposition's G-structural-closure gap rests
  on exactly this unsupported inference.
status: refuted-as-analogy (checked)
evidence: hand checks (least-failure closure fails for the prime, square and
  semiprime predicates); exact Goldbach oracle in code/refute/closure_oracle.py
  (no exception <= 198, independently SymPy-verified); TPTP finite-model attack
  in code/refute/goldbach_closure.p returned undecided at reached sizes. Full
  note: research/approaches/structural-closure-analogue.md.
falsifies: a concrete proved map T with n in E => T(n) in E for a
  positive-density family of n; or a published theorem establishing
  positive-density closure of the exceptional set from a single element.
```

```claim
id: exceptional-set-definition
statement: E(X) := #{n ≤ X : n even, n ≠ p1 + p2 for any primes p1, p2}. The binary Goldbach conjecture is equivalent to E(X) = 2 for all X ≥ 4 (only 2 and 4 are the even n > 0 not sums of two primes under the conjecture).
hypotheses: none — definition.
holds-here: yes — this is the standard exceptional set for the binary problem.
status: definition (sourced)
evidence: Hongze Li, "The exceptional set of Goldbach numbers (II)", Acta Arith. 92 (2000) 71–88, DOI 10.4064/aa-92-1-71-88 (summary in search results; on-disk copy is the abstract page).
falsifies: a different standard definition in the primary literature.
```

```claim
id: montgomery-vaughan-1975
statement: (Montgomery–Vaughan 1975) There exists a positive δ > 0 such that E(X) ≪ X^{1−δ} for all large X. This improved Vaughan's 1972 E(X) ≪ X·exp(−c√log X) and was the first power-saving bound. Per Pintz's paraphrase the δ is "unspecified but explicitly calculable" — the existence is effective but no numerical value is computed. This is the foundational exceptional-set bound for the binary problem.
hypotheses: X sufficiently large; δ > 0 explicitly calculable in principle but not computed in the paper.
holds-here: yes — the foundational exceptional-set bound for the binary problem.
status: proved (by source)
evidence: H.L. Montgomery, R.C. Vaughan, "The exceptional set in Goldbach's problem", Acta Arith. 27 (1975) 353–370, DOI 10.4064/aa-27-1-353-370, as paraphrased by Pintz (arXiv:1804.09084, on disk) and Bhowmik–Halupczok. Full-text gap remains (request full-text-montgomery-6b42).
falsifies: a later source showing the bound is not of the stated form or not effective.
```

```claim
id: grimmelt-teravainen-2025-two-chen-primes
statement: (Grimmelt–Teräväinen 2025, arXiv:2508.16400, Theorem 1.1) There is a constant δ > 0 such that all but O(N^{1−δ}) natural numbers m ≤ N with m ≡ 4 (mod 6) are sums of two Chen primes (primes p with p + 2 having at most two prime factors). Both δ and the implied constant are effective and could in principle be computed.
hypotheses: m ≤ N, m ≡ 4 (mod 6); summands are Chen primes; N large.
holds-here: yes — a power-saving exceptional-set result for a restricted class; a genuine restricted-class partial result for the binary problem.
status: asserted-by-source (arXiv preprint 2025, not yet refereed)
evidence: arXiv:2508.16400, Theorem 1.1 (research/sources/grimmelt-teravainen-exceptional-set-goldbach-two-chen-primes-arxiv-2508.16400.full.md). Improves Tolev (5,7), Meng (3,8), Matomäki (2,7).
falsifies: an independent check of the proof showing a gap; a referee rejection.
```

```claim
id: exceptional-set-chronology
statement: Published power-saving exponents for E(X) < X^{1−δ}: Montgomery–Vaughan 1975 (first power-saving, δ > 0 "explicitly calculable but not computed" per Pintz's paraphrase; not a computed effective value); Chen–Pan 1980 (Sci. Sinica 23, 416–430) Δ > 0.01; Chen 1983 (Sci. Sinica 26, 714–731, the (II) paper); Chen–Liu 1989 δ=0.05 (per Pintz arXiv:1804.09084; note the (III) paper "The exceptional set of Goldbach numbers (III)" is Chen–Liu, Chinese Quart. J. Math. 4 (1989) 1–15 — OpenAlex's "J Chen 1980 (III)" row mislabels it); H.Z. Li 1999 δ=0.079 (E(X)<X^{0.921}, per Pintz) — the "0.086" cited by Kumchev–Tolev and Zhao is Li 2000's exponent 1−0.914, i.e. two different Li papers, not a discrepancy; H.Z. Li 2000 E(X)<X^{0.914}; W.C. Lu 2010 E(X)<X^{0.879} (δ=0.121, the best published); Pintz 2018 E(X)<X^{0.72} (δ=0.28, arXiv preprint — still unrefereed; the 2023 Acta Arith. publication is Part I, not Part II); Zhao 2025 E(X)=O(X^{7/10}) (δ=0.3, arXiv preprint, sharpest claimed, unverified by a second route).
hypotheses: X sufficiently large; all constants ineffective.
holds-here: yes — the current record line for the exceptional set; the "best published" is Lu 2010, the "best claimed" is Zhao 2025 (0.7).
status: proved (by source) for the published bounds; preprint for Pintz 0.72 and Zhao 0.7.
evidence: Pintz, "A new explicit formula in the additive theory of primes with applications II. The exceptional set in Goldbach's problem", arXiv:1804.09084 (research/sources/pintz-explicit-formula-additive-theory-primes-II-exceptional-set-goldbach-arxiv-1804.09084.full.md); Bhowmik–Halupczok survey (research/sources/bhowmik-halupczok-asymptotics-goldbach-representations-arxiv-2010.01308.full.md); Zhao arXiv:2511.05631 (research/sources/zhao-exceptional-set-goldbach-linnik-constant-arxiv-2511.05631v2-pdf.full.md). Note: Zhao's corollary P(q)=O(q^5) is not new — Xylouris proved Linnik constant L=5 (PhD thesis 2011; L=5.2 in the published 2011 paper).
falsifies: a published bound sharper than Lu's 0.879 (e.g. Pintz 0.72 appearing in a refereed journal, or Zhao's 0.7 verified), which would supersede the "best published" attribution.
```

```claim
id: zhao-2025-exceptional-0.7
statement: (Zhao 2025, arXiv:2511.05631) E(X) = O(X^{7/10}) = O(X^{0.7}), with an ineffective implicit constant; the method also gives P(q) = O(q^5) for the least prime P(q) in an arithmetic progression mod q. Note: the P(q) = O(q^5) corollary is NOT new — the unconditional Linnik constant is already L = 5 (Xylouris, PhD thesis 2011; L = 5.2 in the published 2011 paper); Zhao's paper says "L = 5.2 … still best up to date", which is stale.
hypotheses: X large; implicit constant ineffective.
holds-here: yes — a recent arXiv preprint, the sharpest claimed exceptional-set exponent if correct. Unverified against a second route; not refereed.
status: asserted-by-source (preprint, not yet verified by a second route or referee)
evidence: Genheng Zhao, "The exceptional set of Goldbach problem and Linnik's constant", arXiv:2511.05631v2 (research/sources/zhao-exceptional-set-goldbach-linnik-constant-arxiv-2511.05631v2-pdf.full.md). Linnik L = 5: Xylouris thesis via Zaman thesis hdl.handle.net/1807/79531, Leung arXiv:2402.07941.
falsifies: an independent check of the proof showing a gap; a counterexample in the claimed range; a referee rejection identifying a flaw.
```

```claim
id: hardy-littlewood-singular-series
statement: (Hardy–Littlewood 1923, Conjecture A) The number of representations R(n) of even n as a sum of two primes satisfies R(n) ~ 2C_twin · n/(log n)(log(n−2)) · ∏_{p odd, p|n} (p−1)/(p−2), where C_twin = ∏_{p odd} p(p−2)/(p−1)² = 0.6601618158... is the twin-prime constant. This is conjectural (prime k-tuple conjecture), not proved.
hypotheses: n even, n → ∞; the conjecture is the Hardy–Littlewood k-tuple / singular-series conjecture.
holds-here: yes — this is the precise predicted asymptotic (weighted and unweighted forms) for the binary problem.
status: conjectured (by source)
evidence: Hardy–Littlewood, "Some problems of 'Partitio numerorum'; III", Acta Math. 44 (1923) 1–70, full text on disk at research/sources/hardy-littlewood-partitio-numerorum-iii-1923-tsinghua-pdf.full.md; also stated on Oliveira e Silva's project page (research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md) and MathWorld.
falsifies: a proved counterexample to the asymptotic.
```

```claim
id: ternary-helfgott
statement: (Helfgott 2013/2015) The ternary Goldbach conjecture is true: every odd integer n > 5 is a sum of three primes. Proved unconditionally: for n ≥ 10^27 by the analytic proof, and for the remaining n ≤ 8.875×10^30 by computation (Helfgott–Platt).
hypotheses: n odd, n > 5.
holds-here: yes — but it is the ternary variant; it does NOT resolve the binary conjecture (it would follow from binary, not the reverse).
status: proved (by source)
evidence: H.A. Helfgott, "The ternary Goldbach conjecture is true", arXiv:1312.7748 (research/sources/helfgott-ternary-goldbach-conjecture-is-true-arxiv-1312.7748.full.md); Helfgott–Platt, "Numerical verification of the ternary Goldbach conjecture up to 8.875×10^30", arXiv:1305.3062 (research/sources/helfgott-platt-numerical-verification-ternary-goldbach-8.875e30-arxiv-1305.3062.full.md).
falsifies: an odd n > 5 not a sum of three primes.
```

```claim
id: tao-five-primes
statement: (Tao 2012) Every odd number N > 1 is a sum of at most five primes; this lowers Schnirelman's constant from 7 to 6 (as a corollary, every n > 1 is a sum of at most 6 primes).
hypotheses: N odd, N > 1.
holds-here: yes — a quantitative approximation result for the odd case, not the binary target.
status: proved (by source)
evidence: Terence Tao, "Every odd number greater than 1 is the sum of at most five primes", arXiv:1201.6656 (research/sources/tao-every-odd-integer-sum-of-at-most-five-primes-arxiv-1201.6656.full.md).
falsifies: an odd N > 1 needing six or more primes.
```

```claim
id: linnik-goldbach-k6-grh
statement: (Johnston–Trudgian 2026) Under GRH, every sufficiently large even integer is a sum of two primes and K = 6 powers of 2 (Linnik–Goldbach problem); unconditionally K = 13 (Heath-Brown–Schlage-Puchta), K = 8 (Pintz–Ruzsa). Under Elliott–Halberstam, K = 4.
hypotheses: GRH for the K=6 result; EH for K=4; unconditional for K=8/13.
holds-here: yes — a conditional partial result with a well-defined K.
status: proved (by source), conditional on GRH/EH
evidence: Daniel R. Johnston, Tim Trudgian, "An update on the Linnik–Goldbach and Romanov problems", arXiv:2605.17825 (research/sources/johnston-trudgian-update-linnik-goldbach-romanov-problems-arxiv-2605.17825.full.md).
falsifies: an even N in the claimed range failing the K=6 representation, assuming the hypothesis.
```

```claim
id: parity-problem-barrier
statement: The parity problem in sieve theory: classical sieve methods (upper-bound sieves) cannot distinguish numbers with an even number of prime factors from those with an odd number; consequently no pure sieve argument can prove the binary Goldbach conjecture or the twin prime conjecture, and the P2→prime step in Chen's theorem is blocked by this structural limitation.
hypotheses: classical sieve framework (Selberg-type weighted sieves).
holds-here: yes — this is the documented obstruction for sieve approaches to the binary conjecture.
status: proved (by source) as a limitation of sieve methods; the "no sieve can prove it" folklore is qualified — some non-classical sieves (e.g. Maynard-type, asymptotic sieve) evade it.
evidence: Friedlander–Iwaniec, "Exceptional zeros, sieve parity, Goldbach", Essential Number Theory 1 (2022) 13–39 (research/sources/friedlander-iwaniec-exceptional-zeros-sieve-parity-goldbach-ent-2022.full.md, abstract page); also Maynard, "Counting primes", ICM 2022 (search result).
falsifies: a published proof of a prime-detecting statement (like twin primes or binary Goldbach) using only classical sieve bounds — none exists; the Maynard/GPT workaround shows the barrier applies to the classical framework, not to every conceivable sieve.
```

```claim
id: siegel-zero-goldbach-connection
statement: A weak form of the Hardy–Littlewood–Goldbach conjecture (a two-sided bound on the weighted representation sum G(n) near the singular-series value δS(n)n) would rule out exceptional (Siegel) zeros of Dirichlet L-functions in the region σ > 1 − c/log(q(|t|+2)). Conversely, bounds on exceptional zeros feed back into sieve-parity improvements.
hypotheses: Weak HL-Goldbach conjecture for all sufficiently large even n; δ > 0 fixed.
holds-here: yes — a conditional structural connection between the binary problem and L-function zeros.
status: proved (by source) as a conditional theorem
evidence: Friedlander–Iwaniec, "Exceptional zeros, sieve parity, Goldbach" (ENT 2022); Matomäki–Merikoski, "Siegel zeros, twin primes, Goldbach's conjecture, and primes in short intervals", arXiv:2112.11412 (research/sources/matomaki-merikoski-siegel-zeros-twin-primes-goldbach-short-intervals-arxiv-2112.11412.full.md).
falsifies: an exceptional zero existing alongside a proved weak HL-Goldbach bound.
```

```claim
id: granville-goldbach-rh-equivalence
statement: (Granville 2007) Certain averaged strong forms of Goldbach's conjecture are equivalent to the Generalized Riemann Hypothesis: e.g. RH is equivalent to an estimate for the summatory function of Λ over Goldbach-type convolutions (Theorem 1A–1D). Also, if every even n > 2 has more than γn/log²n representations as p+q, then every even integer is a sum of two primes from a sparse set P with |P∩[1,x]| ≤ η√x log x.
hypotheses: strong forms of Goldbach's conjecture (representation-count bounds); γ, η constants.
holds-here: yes — conditional equivalences and sparse-prime-set corollaries.
status: proved (by source), conditional on the stated strong Goldbach forms
evidence: Andrew Granville, "Refinements of Goldbach's conjecture, and the generalized Riemann hypothesis", Funct. Approx. Comment. Math. 37 (2007), full text at research/sources/granville-refinements-goldbach-conjecture-GRH-2007.full.md.
falsifies: a proved strong Goldbach form that does NOT imply the corresponding RH statement, or vice versa.
```
