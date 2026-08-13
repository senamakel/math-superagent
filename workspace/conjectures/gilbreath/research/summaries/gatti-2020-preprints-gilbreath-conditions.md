# Gatti 2020 — Gilbreath's sequences and proof of conditions for Gilbreath's conjecture

<!-- source: https://web.archive.org/web/20201202160317/https://www.preprints.org/manuscript/202003.0145/v1/download (PDF capture of https://www.preprints.org/manuscript/202003.0145/v1) | full text: sources/gatti-2020-preprints-gilbreath-conditions.full.md -->

Riccardo Gatti, Preprints.org 202003.0145.v1 (8 Mar 2020), "NOT PEER-REVIEWED". Later expanded/recast as the MDPI Mathematics 11(18):4006 (2023) "Gilbreath Equation, Gilbreath Polynomials…" paper (whose PDF is 403-blocked; the run holds only its RePEc/abstract record). This is the same valid-extension machinery the run already held from Alkan et al. 2023 and Muney 2026 — now sourced independently in primary form.

## What it establishes (sound parts)

- **Gilbreath's equation (Thm 2, Cor 1).** Appending `k` to `S ∈ G_n` preserves the property iff the nested-absolute "Gilbreath equation" holds; the solutions are `k = ±s^{n-1}_1 ± s^{n-2}_2 ± … ± s^1_{n-1} + s_n ± 1` (Eq. 2), a signed sum down the **whole right anti-diagonal** plus `s_n ± 1`. Hence `max K_S = Σ_i s^{n-i}_i + s_n + 1`, `min K_S = 2s_n − max K_S` (Eq. 3, the reflection symmetry). This is the same **global, order-sensitive criterion** as the run's held Alkan/Muney results — independent confirmation that valid extension is a whole-prefix condition, not a bounded window. Bearing: reinforces the refutation of the backward-extension-automaton approach (research/approaches/backward-extension-automaton.md).
- **Parity alternation (Lemmas 1–3).** In a Gilbreath sequence, `s_1` even ⟹ `s_2..s_n` all odd; `s_1` odd ⟹ all later even. This is the general-class half of the run's parity-wave/shape fact for the primes, proved by induction on the extension equation. Consistent with, and an independent statement of, the run's proved `(odd, even, even, …)` row-shape preservation.
- **Upper/lower bound sequences (Defs 2–6).** Every Gilbreath-sequence element lies between iterated `min/max K` bounds; the bound sequences grow exponentially (fit example: `U'_S ≈ 14.42 e^{0.75n}`, R²≈0.92 for S={2,3,5,7,11,13}); no closed form for the (n+1)-th bound given the first n — Gatti openly states none was found.

## Located flaw — Theorem 4's proof does not prove the prime case

Theorem 4 asserts the bound (15): `min K_{p1..p_{n-1}} ≤ p_n ≤ max K_{p1..p_{n-1}}` for every prime. The **right inequality is not established**:

- The induction step begins "If `p_n ≤ max K`, then subtracting `2p_{n-1}` from both sides…", i.e. it **assumes the conclusion**, then derives `min K ≤ α` for an arbitrary `α > 0` (using Bertrand `p_n < 2p_{n-1}`) — a trivially true statement — and then asserts "hence `p_n ≤ max K`". The needed inequality is `p_n ≤ p_{n-1} + 1 + Σ` (anti-diagonal entries); Bertrand only gives `2p_{n-1} − p_n > 0`, and Gatti substitutes the generic "min K ≤ positive" for the specific bound required. Nothing connects them.
- The left inequality does work (via Corollary 2, `k = s_n` is always a valid extension, so `min K ≤ p_{n-1} ≤ p_n`).
- So Theorem 4 is **unproved by this argument**; the claim itself is, in effect, a bounded-gap/valid-extension statement about the primes (equivalent in spirit to the conjecture, not a corollary of it).

## Located flaw — Lemma 4 (interval completeness) is false and refuted by Muney 2026

- Lemma 4 + Theorem 3 assert `K_S` = the whole parity class in `]min K, max K[`. Muney 2026 (held: research/sources/muney-2026-holes-valid-extension-html.full.md) **refutes this in general**: the valid-extension set can have interior holes, first at length 5 for `(2,3,5,9,15)`.
- **Even on the run's own example the open-interval statement is false at both endpoints.** For `S = {2,3,5}`, `min K = 1` and `max K = 9`, and both 1 and 9 ARE valid extensions (apex = 1), yet 1, 9 ∉ `]1,9[`. So Gatti's Theorem 3 equivalence `k ∈ ]min K, max K[ ∧ parity ⟺ S′ ∈ G_{n+1}` fails here at both endpoints — consistent with Muney's "endpoint validity and reflection symmetry" theorem (endpoints are always valid), which directly contradicts the open-interval form.
- The Corollary-1 count `dim K_S = 2^{n−1}` also fails on a held example: for `S = {2,3,5} ∈ G_3`, the equation `|1 − |2 − |5−k||| = 1` has solutions `K = {1,3,5,7,9}` — five solutions, not `2^{3−1} = 4` (the eight signed combinations of Eq. 2 collapse to five distinct values because nested absolute values impose consistency). Verify: `code/research_mod_check/verify_gatti_kset.py` (queued for the coder; anti-diagonal fixed to rows b=1..n−1 so the formula matches Eq. 2).
- Gatti's regularity claim (exponential trend of the bounds) is explicitly "observed", not proved.

## Status

- `gatti-2020-machinery-global` — the Eq.-2 anti-diagonal solution formula and parity alternation: **checked by hand arithmetic** (independently reproduces the run's Alkan/Muney-held global criterion).
- **Hand check of the K-set count (no program run by this role).** For `S={2,3,5}`, the Gilbreath equation is `|1 − |2 − |5−k||| = 1`. Solving: `|2−|5−k|| ∈ {0,2}` ⟺ `k ∈ {3,7}` or `k ∈ {1,5,9}`, so `K_S = {1,3,5,7,9}` — five solutions, not Gatti's `2^{n−1} = 4`. Eq. 2's eight signed combinations `±1 ±2 +5 ±1` also collapse to exactly `{1,3,5,7,9}`. Verification script available for the coder: `code/research_mod_check/verify_gatti_kset.py` (checks definition-by-left-edge, formula, dim prediction, and Lemma-4 interval completeness on this example).
- `gatti-2020-theorem4-invalid` — Theorem 4's proof fails at the right-inequality step: **located flaw, recorded as refuted** (the paper claims GC'’s core bound; the proof does not establish it).
- `gatti-2020-lemma4-refuted` — interval-completeness of K_S: **refuted in general** by Muney 2026 (length-5 hole); the CROSS-CHECK that the primes' prefixes avoid holes remains open (that is the conjecture, in this language).
- The 2023 MDPI "polynomial" claim (`gilbreath-polynomials-imply-gc`: GC follows from `p_n − 2^{n−1} ≤ P_{n-1}(1)`) is **still asserted-by-source, unverified**: the preprint on disk is a different (earlier) paper and does not contain the polynomial inequality; the MDPI PDF remains 403-unobtainable. Do not cite the preprint as evidence for the polynomial claim.
- Bibliographic note: Gatti cites Proth's C.R. paper as "C.R. 86 (1887) 329–331" — another instance of the wrong Proth citation (the library's `proth-citation-correction` holds the correct record: C.R. 85 (1877) 329–331 are Pépin's pages).
- The 2020 preprint does **not** contain the 2023-polynomial inequality `p_n − 2^{n−1} ≤ P_{n−1}(1)`; that claim remains asserted-by-source via the 403-blocked MDPI paper only.

```claim
id: gatti-2020-valid-extension-global-formula
statement: For S ∈ G_n, appending k preserves Gilbreath-ness iff the nested-absolute Gilbreath equation holds, with solutions k = ±s^{n−1}_1 ± s^{n−2}_2 ± … ± s^1_{n−1} + s_n ± 1 — a signed sum over the WHOLE right anti-diagonal; max K_S = Σ_i s^{n−i}_i + s_n + 1, min K_S = 2s_n − max K_S.
hypotheses: finite integer sequence S in G_n.
holds-here: yes — same global criterion the run holds from Alkan 2023 / Muney 2026, now sourced independently in primary form (Gatti 2020 Eq. 2–3).
status: checked (hand arithmetic; independent duplicate of the held global-valid-extension result)
bearing: reinforces the refutation of any bounded-window backward-extension automaton; valid extension is a whole-prefix condition.
anchor: research/sources/gatti-2020-preprints-gilbreath-conditions.full.md
```

```claim
id: gatti-2020-theorem4-proof-invalid
statement: Gatti's Theorem 4 (min K ≤ p_n ≤ max K for every prime, claimed to prove a core Gilbreath bound) has an invalid proof: the right-inequality step assumes p_n ≤ max K (subtracts 2p_{n−1} from both sides), then derives only "min K ≤ α for some α>0" via Bertrand — a trivially true statement that never establishes p_n ≤ max K. The left inequality min K ≤ p_n is sound (Corollary 2: k=s_n is always a valid extension).
hypotheses: Bertrand's postulate + the min/max K machinery.
holds-here: yes — the flawed step is in the prime-case proof, exactly the class whose GC status is open.
status: refuted (located flaw: conclusion assumed in the induction step)
bearing: Gatti 2020 does NOT prove GC nor any deterministic bounded-gap class result; nothing here overturns Eppstein's anti-Gilbreath refutation of the bounded-gap class.
anchor: research/sources/gatti-2020-preprints-gilbreath-conditions.full.md
```

```claim
id: gatti-2020-lemma4-interval-completeness-refuted
statement: Gatti Lemma 4 / Theorem 3 assert K_S fills the whole parity class in ]min K, max K[. This interval-completeness is FALSE in general: Muney 2026 exhibits the first hole at length 5 for (2,3,5,9,15), and even the count dim K_S = 2^{n−1} fails for S={2,3,5}: |K_S| = 5, not 4 (solutions {1,3,5,7,9}).
hypotheses: none beyond S ∈ G_n; checked on the S={2,3,5} example by hand: |1−|2−|5−k||| = 1 ⟺ k ∈ {1,3,5,7,9}.
holds-here: yes — the false lemma is the claimed mechanism of Gatti's bound-sequence theory.
status: refuted (by Muney 2026, held; and by direct example)
bearing: no interval-completeness of valid-extension sets can be assumed anywhere downstream; the run's approaches already treat valid extension as global and hole-prone.
anchor: research/summaries/gatti-2020-preprints-gilbreath-conditions.md
```

```claim
id: gatti-2020-parity-alternation-independent
statement: In any Gilbreath sequence, s_1 even ⟹ s_2..s_n all odd, s_1 odd ⟹ s_2..s_n all even (Gatti Lemmas 1–3, proved by induction on the extension equation) — an independent general-class statement of the parity alternation the run uses for the primes (shape (odd, even, even, …) preserved by the operator).
hypotheses: finite Gilbreath sequence.
holds-here: yes — general-class version of the run's parity-wave (a_1 = 2 even, all later primes odd).
status: checked (simple induction, consistent with the run's proved shape preservation)
bearing: the parity half of the reduction is general, not prime-specific; only the regeneration half is open.
anchor: research/sources/gatti-2020-preprints-gilbreath-conditions.full.md
```