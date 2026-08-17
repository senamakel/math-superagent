# Durable findings awaiting Cognee promotion (memory server down — workspace stand-in)

The `remember_memory` server's health check failed 18 times across the last two scholar
cycles; per the workspace tool-permission fallback, these verified, source-backed findings are
written here so a later pass with a healthy server can `remember_memory` each verbatim. Every
statement is verified against a held primary full text on disk under `research/sources/`.

## D1 — Tóth–Valtr chain, corrected labels (verified vs toth-valtr-full.md, suk-arxiv1604.08657.full.md)

- 1998 bound: **ES(n) ≤ C(2n-5,n-2) + 2** (Theorem 5). 2005 combined Chung–Graham +
  projective transform: **ES(n) ≤ C(2n-5,n-2) + 1 for n ≥ 5** (Theorem 1).
- C(2n-5,n-2) = C(2n-5,n-3) by binomial symmetry, so n-2 / n-3 phrasings of the same bound are
  identical (resolves the earlier "flag resolved" entries).
- Mojarrad–Vlachos bound **≈ 7/16·C(2n-4,n-2)**: C(2n-8,n-3)/C(2n-4,n-2) → 1/16, and
  C(2n-5,n-2)/C(2n-4,n-2) = 1/2, so 1/2 − 1/16 = 7/16.
- Suk 2017: **ES(n) ≤ 2^{n + 6n^{2/3} log n} for n ≥ n0** (line 43 of held primary).
- All asymptotic-type; none bears on the exact constant 2^{n-2}+1.

## D2 — Dumitru arXiv:2512.24061 (verified vs paper body)

578,336 vars (5456 triple-orientation + 572,880 4-set selectors, 14 per 4-set); 16,670,808
clauses (9,493,440 reduced 5-point CC + 2,905,320 4-set consistency + 4,272,048
no-convex-7-set). Proposition 1 (4-set criterion) = this run's es35-four-criterion. UNSAT only
for convex-layer-anchored subfamilies; heavy-tailed runtimes; ES(7)=33 OPEN. Soundness:
relaxed (clause-omitting) UNSAT is a valid certificate.

## D3 — PointSAT arXiv:2607.02958 (verified vs full text)

h(6,7)=24 (adjacent hole/gon result). 32-point no-7-gon: 2191 core-hrs, 200,000 abstract
order-types, ZERO realizable — evidence only; abstract space not exhausted; few flippable
orientations (0.9% vs ≥1.2%) and mean 121.6 violations (vs ≤38). Consistent with SMQH 4-fold
and Dumitru. Realizability needs a separate solver (Localizer), not added clauses (smallest
unrealizable abstracts have 9 points; forbidding needs O(n⁹) clauses).

## D4 — Koshelev–Koshka arXiv:2604.20120 (verified vs HTML full text)

h(6,≥2)=17, h(6,1)=18 (pins ES(6)=17 boundary); explicit 17-point integer set = oracle
checkpoint. Linear subreduction: fix abscissae (x_i=i or exponential), feed whole formula to
SMT/Z3, orientation determinants become linear-integer — the run's concrete realizability
route for ES(5)/ES(6) reproduction. Authors' caveat: fixing x can in principle lose
realizations; empirical. Signotope 4-tuple one-sign-change axiom = 8 clauses per 4-set.
Preprint, asserted-by-source.

## D5 — Baek–Balko SoCG 2025 (verified vs held full PDF)

- `baek-balko-split`: ESsplit(k)=2^{k-2}+1 PROVED in-source — Lemma 10 upper bound (down-set
  injectivity) complete, Lemma 11 abstract lower bound (delta-colorings) complete; Lemmas 9/12
  "proof omitted" in SoCG.
- `baek-balko-decomposable`: Theorem 8 **asserted-by-source** — SoCG line 343-352 says verbatim
  "The proof of Theorem 8 is omitted", deferred to JCTA 2026 (DOI 10.1016/j.jcta.2026.106195,
  paywalled; no arXiv preprint). Do not present as proved.
- `baek-balko-weak7-fails`: Cweak(7)>33, abstract weak-k-gon analogue false at k=7 (SAT).
- `baek-balko-signotope-analogue-open`: every signotope on 2^{k-2}+1 vertices has a weak k-gon
  OPEN, equivalent to a Goodman–Pollack conjecture; the right SAT-arm target.
- `baek-balko-blowup-new-constructions`: x-blow-up of explicit M-set (Thm 19) has exactly
  2^{k-2} points, no k in convex position — new extremal family generalizing ES/Valtr.
- CONTEXT.md Established's "proved (SoCG 2025)" line for decomposable is STALE; the ledger is
  correct (asserted).

## D6 — Baek ETV arXiv:2206.04260 (verified vs full text)

- P(n,4,n) PROVED (Theorem 1.6 → 2.7 via Theorem 5.10 + Lemma 5.2, proofs present at lines
  603-630, 748-900); first new ETV case since 1935. Held text proves it; status upgrade to
  proved from a prior cycle is correct.
- `etv-alpha-statistic-injective` (Theorem 3.6, lines 377-395) and `baek-interweaved-laced-cups`
  (Lemma 5.2, Thm 5.10) PROVED over abstract configurations, hence a fortiori over realizable.
- `etv-equivalent-to-es` stays asserted (cited to Erdős–Tuza–Valtr 1996, not proved in held text).
- Open generalization: Conjecture 5 (size (n-1 choose 2)+k forces k interweaved laced (n−1)-cups)
  proved only for k=1,2,n.
- POLYNOMIAL CAVEAT: N(n,4,n)=(n−1 choose 2)+1 ≈ n²/2 is far below 2^{n−2}; does NOT touch ES(7)
  at N=33.

## D7 — Horton 1983 (primary held; machine check pending)

S_k = {(i,d(i))}, d(i)=Σ a_j c^{j-1}, c=2^k+1, 2^k points, NO empty convex 7-gon; hence g(n)
does not exist for n≥7 (g(5)=10 Harborth, g(6) open). Empty-side analogue of the ES 1961
construction; strictly distinct from the convex-position ES(n) conjecture; kept out of
Established. `code/out/horton_verify.py` written but NOT yet executed — `horton-*` claims are
proved from the source argument, not machine-checked, until the run runs it.

## To store (one call each) when the memory server recovers

```
remember_memory { text: "D1 ...", source: "scholar readback digestion cycle" }
remember_memory { text: "D2 ...", source: "scholar readback digestion cycle" }
... D3, D4, D5, D6, D7 ...
```
