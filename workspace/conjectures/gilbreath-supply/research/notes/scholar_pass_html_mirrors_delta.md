# Scholar pass: delta against the newly arrived library material

Author: scholar. Date: this pass. Scope: the reference library was comprehensively
digested by six prior scholar passes (CLAIMS.md holds ~90 claims, every summary
carries blocks, every backward skeleton and thread is written). This pass
re-checked the whole library against the run's current goal, tasks, and beliefs,
found the one genuinely new piece (the two HTML-mirror sources whose digests
were still unfinished template stubs), replaced those stubs with real summaries,
and verified nothing else is new.

## What the "new material" actually was

The two files `research/summaries/meshulam_uncertainty_finite_abelian_html.md`
and `research/summaries/tao_uncertainty_cyclic_prime_html.md` still carried the
librarian's *template* text ("Digest only — read this first … Replace this
digest"). They are the HTML mirrors of two papers whose PDF versions were already
fully digested with claim blocks (`meshulam-finite-abelian-divisor-bound`,
`tao-additive-uncertainty-prime-cyclic`):

- **Meshulam HTML mirror** = same Theorem 1.2 (divisor-sharpened `|supp f̂| ≥
  (n/(d₁d₂))(d₁+d₂−k)`), plus the **full proofs** (Prop 1.3 subgroup/factor
  reduction, Prop 1.4 submultiplicativity, Thm 4.1 non-abelian `|supp f|·μ(f) ≥
  |G|`) that the PDF digest only stated.
- **Tao HTML mirror** = same Theorem 1.1 (`|supp f|+|supp f̂| ≥ p+1`, absolutely
  sharp) plus the **Chebotarëv Lemma 1.3 proof** (minor-nonzero Fourier matrix,
  engine of the theorem) and the Cauchy–Davenport corollary.

Both mirrors were replaced with real summaries (wikilinked to their full texts)
that record the proof-level detail and confirm the two mirrors agree with the PDF
digests — **no new theorem, no change to any claim**. Since the digests carry no
new claim blocks of their own (the theorems were already claimed from the PDF
twins), no `answers:` line is added to the open request.

## Bearing: does any of this move the goal?

No. The library's position is unchanged and the requests stay open:

1. **`walsh-spectral-subset-b904` remains genuinely open.** The Meshulam/Tao
   digests (both mirrors) fix the sharpest Walsh-side support bounds on
   `(Z/2)^n` and their equality cases (subgroup indicators = exactly the
   structured low-weight inputs the five closed doors forbid), but neither is a
   lower bound on the co-domain image weight `wt(Φ_n h)`; both are directional.
2. **The finite-prefix transfer remains the single largest missing tool.**
   Pivato–Yassawi Thm 7.1 (Lucas mixing ⟺ randomization at density-one times)
   is a measure-level ergodic equivalence; the finite deterministic
   `wt(Φ_n h) ≥ c·n` bound is not in any source. Both halves absent: (a) the
   prime-gap-parity measure being Lucas/harmonically mixing, (b) the
   quantitative weak-*-→weight transfer.
3. **The averaged/density-1 form remains the live line** (GOAL priority 1):
   G-mean-linear + G-var-vanishing, with s2_N → 0 (or finiteness of the
   exceptional set) as the sharpest open statement; all measured, none proved.

## Sources that do not help (confirmed, so nobody re-reads them)

- The **two HTML mirrors' templates** are now replaced; the PDF twins remain the
  canonical digests. Both duplicates confirmed identical in content.
- `odlyzko_gilbreath` — bibliography index page, leads only.
- `granville_martin_prime_number_races` — duplicate mirror of the canonical
  `_prime_races` paper; both kept intentionally.
- Five `citations_w*` files — citation graphs, explicitly not evidence.
- Four OEIS files — marked "does not help SUPPLY" (quadratic-irrational digits,
  ternary fractal); none touches the fold.
- `rowland_nonzero_binomial_modp` — counts nonzero binomials on a row
  (background for the submask count `2^{s₂(d)}`); gives no weight bound on the
  fold.
- `chase_random_gilbreath` — random-sequence analogue of Gilbreath's leading
  term; `holds-here: no` (primes are deterministic; conclusion is about the
  first column, not ν₂'s suffix) — plausibility context only.
- `encyclopedia_gilbreath` — dictionary-level statement of Gilbreath (out of
  scope per GOAL.md).

## Contradictions re-verified (all resolved on disk, none live)

- **ABGS vs LOS emphasis** (not factual): ABGS leave even pair-class equality
  open; LOS conjecture switch dominance at every x. Both can hold; neither is a
  theorem. LOS must not be cited as proof of the switch-density input.
- **Rampersad–Wiebe overstatement corrected**: `rw-not-the-submask-xor-fold`
  supersedes the earlier "RW is the fold itself" gloss; RW gives no weight bound
  on Φ.
- **R-finite-verified contradiction**: "ν₂/n ≥ 0.42 on [50,4000]" is false (10
  counterexamples ≤ 274); correct statement ν₂/n ≥ 0.42 for all n ≥ 500. The
  CLAIMS.md "contradictions" rows for both were naming artefacts (stale ids),
  self-resolved by the verification passes.
- **nu2_terms superseded**: ν₂(53)=19/ν₂(64)=28 are wrong; three exact routes
  give 18/27. Not re-imported.
- **Kernel correction stands**: Φ_n rank n−2, nullity 2, ker = span(even-alt,
  odd-alt); problem.md fact 3 superseded (Bacher's square-symmetric determinants
  are independent of the rectangular fold's rank).

## What this pass adds to durable knowledge

The proof-level detail of Meshulam Prop 1.3/1.4 + Thm 4.1 and Tao Lemma 1.3
(Chebotarëv) are now on disk in the summaries (verified against the full texts);
the claim blocks were already present from the PDF digests, so no claim-id
change. The decisive finding is negative-but-cheap: **the newly arrived material
contains no new theorem, changes no claim, and leaves both the finite-prefix
transfer and the Walsh-weight request open.** The next loop should not re-read
these mirrors; it should attack the in-house computation (density-1/s2_N and the
submask-window correlation of the prime h), per the search freeze (directive 7).