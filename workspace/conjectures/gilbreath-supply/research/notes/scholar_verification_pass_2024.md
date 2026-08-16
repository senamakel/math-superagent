# Scholar verification pass — load-bearing digests checked against full texts

A verification (not a new-theory) pass. Every source in `research/sources/`
was already digested into a claim block by an earlier scholar pass; this pass
picked the claims the whole run's direction rests on and re-checked each
digest against the full text, so a mis-digested load-bearing claim cannot pass
silently. Result: the three load-bearing digests are **accurate**. No new
source was downloaded (the run's open gaps are in-house computation, not
literature; FRONTIER is polluted with "supply chain management" noise — see
below).

## Verified verbatim

1. **Pivato–Yassawi 2006 Thm 7.1** (the weakest-input candidate, GOAL priority
   2). Full text `research/sources/pivato_yassawi_sofic_randomization.full.md`
   lines 1721–1730: "Lucas mixing" is defined exactly as the digest says (for
   every nontrivial character χ, a density-one H ⊂ N with
   `lim_{H∋h→∞} ⟨χ∘Φ^{h·⟨⟨χ⟩⟩}, µ⟩ = 0`), and
   "**Theorem 7.1.** (Φ = 1+σ asymptotically randomizes µ) ⇐⇒ (µ is Lucas
   mixing)". The `⟨⟨χ⟩⟩ = p^{⌈log_p|χ|⌉}` engine and the Lucas-theorem step
   `Φ^{⟨⟨χ⟩⟩} = 1+σ^{⟨⟨χ⟩⟩}` are confirmed. The digest's `holds-here`, sharpness
   reading ("strongest possible extension", line 1735), and the caveat that this
   is measure-level (weak-* at density-one *times*), not a finite fixed-string
   weight bound, are all correct.

2. **Hofer 2025 Lemma 1 + Cor 1** (that Φ's mod-2 Pascal algebra is governed by
   Thue–Morse signs — the reason any weight bound must be input-dependent).
   Full text lines 317–400: the identity
   `M1^T diag(((−1)^{s₂(i)})·) M1 = M2` and Corollary 1's determinant
   `det(M2^(n)) = ∏_{i<n}(−1)^{s₂(i)}` are confirmed verbatim, with the proof
   via Lucas' theorem as the digest states.

3. **ABGS 2011 §1/§9** (the parity barrier). The summary quotes §1 p.401
   verbatim: "Problem 1.1 is wide open, and cannot be treated using L-functions,
   unlike the case of Dirichlet's theorem." The corrected mod-4 measured split
   (switch 45041 / equal 33289, ratio 1.353) is recorded in the summary table.

## Ghost contradictions self-resolve

The `CLAIMS.md` "Contradictions" section flags two rows whose second member
("no claim of that id is on disk"):

- `r-finite-verified-contradicted` vs `R-finite-verified`: the latter id is a
  *rung name* in `research/weakened/`, never filed as a claim. The correction
  is durably recorded (claim `r-finite-verified-contradicted`) — the
  "contradiction" is a naming artefact, not a live dispute. Resolved: the
  10-dip/exceptional-set-[50,274] statement stands; the rung is relabelled.
- `rw-not-the-submask-xor-fold` vs `rw-described-as-the-fold-itself`: the
  latter overstatement lived only in an earlier abstract-based note, never a
  claim block. The correction (Rampersad–Wiebe analyses sums over k of products,
  NOT the submask-XOR zeta transform Φ; Thm 20 is a different sum family) is
  the durable claim. Resolved: no one may cite RW for a weight bound on Φ.

Both "contradictions" are stale ids, not genuine disagreements between claims
that both hold. No content to reconcile.

## FRONTIER pollution (do not read)

`research/FRONTIER.md` carries ~40 rows of "DEFINING SUPPLY CHAIN MANAGEMENT"
citations (blockchain, operations research, market research) that matched the
word "SUPPLY" in the wrong domain. These are noise and must not be downloaded.
The relevant frontier rows are the math subjects (consecutive-prime tuples,
prime races, Lucas 2-regular sums, affine-CA limit measures). The open request
`walsh-spectral-subset-b904` is a genuine gap not served by reading more rows.

## What still lacks a source (unchanged)

- Any theorem lower-bounding `wt(Φ_n h)` from an input strictly weaker than
  positive mod-4 switch density. The Walsh/subset-sum request is still open;
  the uncertainty principles (Tao additive, Meshulam product, Donoho–Stark)
  fix the Walsh-side support trade-offs and their extremals (subspace indicators
  = the five-closed-doors witnesses) but do not bound image weight, and their
  extremals are exactly the inputs the run may not rely on.
- The finite-prefix transfer from the ergodic randomization theorems
  (Pivato–Yassawi, Takei) to SUPPLY's single deterministic finite-string fold.
  This is the single largest missing technical tool; it appears in no source.

## Verify the verifying

These three digests were already `status: checked`/`asserted` in the ledger on
the strength of the source text before this pass. This pass re-confirmed them
against the full converted text directly (not via the summary), so the
load-bearing school of the run is now verified at two removes. The
`holds-here` and `bearing` annotations, and the caveats (measure-level not
fixed-string; symmetric-Pascal vs rectangular Φ_n transfer unchecked), are
accurate and should be kept.
