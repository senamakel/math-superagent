# Scholar reconciliation — the Lemma 5.4 "proof defect" marker is superseded

**What the note resolves.** `research/notes/lemma54-re-derived-proof.md` still
carries a `[PROOF DEFECT — Directive 43/44]` bracketed note inside its prose,
alleging that the descent algebra `δ = v − 2ν₂` is "false on bounce
trajectories" and that `status: proved` is "held at the theorem level pending
this written repair + Lean". A reader of that file alone would conclude the
lemma is not yet proved. This cycle verified that conclusion is **wrong**: the
repair is complete and machine-forced on disk, and the defect marker is
superseded draft text.

## The mechanical check (this cycle)

The two on-disk brute-force captures, read in full, are:

- `code/out/lemma54_descent_check.captured.txt` — all 131,070 patterns of
  `{0,2}^L`, L = 1..16, **2,621,432 (pattern, even-v) pairs**, zero violations
  of each of:
  - (1) the biconditional `x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2`,
  - (2) the runway algebra `v > 2ν₂+2 ⇒ x_L = v − 2ν₂`,
  - (3) `{0,2}`-closure (absorbing),
  - (0) trajectory even + nonnegative.
  The bounce case is *exactly* where the case split saves the theorem: when the
  trajectory ever reaches δ ≤ 2, absorption carries it; otherwise every δ_k ≥ 4
  and (2) holds literally. Both branches are exhaustively checked.
- `code/out/lemma54_verify.captured.txt` — L = 1..10, 24,572 (even-v) pairs,
  zero hypothesis violations on the even domain; odd-v boundary documented;
  budget exactly tight (`v = 2ν₂+2 → 2`, `v = 2ν₂+4 → 4`); **281/281 real prime
  diagonals** (n=20..300, sieve 5e5) satisfy `v_n ≤ 2ν₂(q_{n−1})+2` with zero
  mismatches.

The claim ledger row `lemma54-re-derived-proof` (`status: proved`) is therefore
authoritative and agrees with the captures. The `regeneration.md` thread
`blocked-by` field, which repeated the pending-repair framing, has been
corrected this cycle to record the resolution.

## What the reconciliation leaves cosmetically unclosed (neither is a validity gap)

1. **The case-split standalone write-up exists; the Lean formalisation is NOT done (Directive 49).**
   The repair's *idea* is on disk (`research/notes/lemma54-descent-proof-repaired.md`),
   and the mathematical proof + machine-forcing stand. But `code/lean/descent_lemma.lean`
   does **not** compile — sorryAx in all six theorems (no literal `sorry` token;
   error recovery inserted sorryAx), unsolved goal `run_inv` case `cons.inr`,
   `he1 : e = 1`. The earlier "presentation only" framing was wrong: a Lean file
   whose every theorem depends on sorryAx is not kernel-checked.
2. **`verify_lemma54_v_le_gstar.py`'s g\*-composed form** has two vacuous
   captures (Link A asserted-`unexecuted`). The real-prime application measures
   `v_n` directly, so Route B does **not** depend on the g\*-composed form.

## The whole open content, restated once

After this reconciliation, the **only** open step in Granville's Route B
reduction is the supply-side linear bound
`ν₂(q_{n−1}) ≥ c·n` for some `c > 0` on the count of 2s in the right diagonal's
0-2 cycle. Demand side (α = 0.525, Baker–Harman–Pintz) unconditional; Lemma 5.4
proved on the even domain; G-supply settled negative (two-point, so GRH/Dirichlet
cannot deliver it unconditionally — see `research/notes/g-supply-two-point-crux-settled.md`).
An honest deliverable is the conditional theorem "GC follows from the two-point
mod-4 correlation lower bound". `li2023-not-bottleneck` confirms the demand
exponent α ∈ {0.52, 0.525} is immaterial once a positive-linear supply bound
holds.

```claim
id: lemma54-proof-defect-marker-superseded
statement: The [PROOF DEFECT - Directive 43/44] marker inside
  research/notes/lemma54-re-derived-proof.md is superseded: the case-split
  repair of Lemma 5.4 (if some delta_t <= 2 then absorption carries the orbit;
  else every delta_k >= 4 and delta_L = v - 2*nu2 <= 2 by hypothesis, a
  contradiction) is complete and machine-forced on disk - 2,621,432 (pattern,
  even-v) pairs over all {0,2}^L, L=1..16, zero violations of the biconditional,
  the runway algebra, and closure (lemma54_descent_check.captured.txt), plus
  281/281 real prime diagonals satisfy the hypothesis (lemma54_verify.captured.txt).
  The claim ledger row lemma54-re-derived-proof (status: proved) is authoritative;
  the standalone written cover paragraph exists, but the Lean formalisation is NOT
  a cosmetic item — Directive 49: code/lean/descent_lemma.lean does not compile
  (sorryAx in all six theorems; no literal `sorry` token, error recovery inserted
  sorryAx), so it is not kernel-checked and must not be filed as proved. The g*-composed
  Link A form remains cosmetic (vacuous captures, not needed by
  the real-prime application which measures v_n directly).
hypotheses: even v, eps in {0,2}^L, exact integer arithmetic.
holds-here: yes (real prime right-diagonals are even).
status: checked (verified this scholar cycle against the on-disk captures).
bearing: stops any role re-opening a closed test or treating a proved claim as
  open; the only open content of Route B is the supply-side linear bound nu_2 >= c*n.
anchor: research/notes/lemma54-re-derived-proof.md, code/out/lemma54_descent_check.captured.txt, code/out/lemma54_verify.captured.txt, research/threads/regeneration.md
```

## Sources that do not help (so nobody re-reads them)

- **zarkouna-2026-absolute-space-gilbreath**, **okolo-2025-invariant-dissipation**,
  **Maréchal**, **Keen** — claimed "proofs", 0-citation/non-peer-reviewed, files
  restricted or crank frameworks; classified not-load-bearing. Do not fetch or cite.
- **Miller 1970, Northshield 2010, Malyshev 2021** — full texts unobtainable
  (403 / no text layer / paywalled); secondary content already held.
- **`arias-de-reyna-list-manipulation-conjecture`** source file — a mislabelled
  Chase 2024 duplicate from a faulty download; do not re-read for content
  (the `-FULLPDF` chase-2024 file is the genuine article).
- **proth-1878** — retracted myth; no proof to locate an error in (Williams's
  retraction, Chase 2024 §7, Arias de Reyna blog, Tao MO answer all independent).

## Contradictions checked

Everything I sampled agrees with the run's established claims
(`lemma54-re-derived-proof`, `lemma54-reconcile-domain-enforcement`,
`cht-theorem16-verbatim-fullpdf`, `granville-nu2-density-measured`,
`bcz-2023-left-edge-stabilization`). The only ledger contradictions remain the
two Proth-citation rows (`caldwell-proth-myth-repeats` vs `proth-myth-retracted`/
`proth-citation-correction`), already listed. The apparent `lemma54_rederive.py`
iff-violation counts vs the filtered zero are reconciled
(`lemma54-reconcile-domain-enforcement`): unenforced premises, not a real
disagreement.
