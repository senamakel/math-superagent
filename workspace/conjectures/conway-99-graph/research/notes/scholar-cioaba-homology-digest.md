# Scholar digest pass — Cioabă clique-complex sources and the H1 gate correction

## What this pass did

Closed the one genuinely unfinished piece of library digestion: the **two Cioabă
clique-complex sources**, which are the primary material behind directive-39's
FIRST gate (clique-complex homology), still carried placeholder digests.

## The two sources

1. **Cioabă & Mim, "On the homology groups of clique complexes of strongly
   regular graphs", arXiv:2606.27328** — full body is in the library
   (`research/sources/cioaba-mim-clique-homology-srg-html.full.md`). Replaced the
   placeholder digest at `research/summaries/cioaba-mim-clique-homology-srg.md`
   and pointed the `-html` note at it. Statements recorded: the
   characteristic-free vanishing criterion (Thm 2.10), the SRG 4/5-cycle
   reduction (Thm 2.11), the classification (Thm 8.4), the infinite-family
   dichotomy (Thm 8.5), the conference-graph threshold v ≥ 256 (Thm 6.7), the
   least-eigenvalue −2 classification (Thm 7.8), and the Latin-square H₂ formula
   (Thm 3.12).

2. **Cioabă, Guo, Ji & Mim, "Clique complexes of strongly regular graphs, their
   eigenvalues, and cohomology groups", LAA 730 (2026) 152–197, arXiv:2508.05871**
   — only the landing page is on disk (body missing); digested honestly as such
   from the abstract and the successor paper's restatement of its theorems, with
   an explicit caveat that the exact theorem numbering is second-hand.

## The finding: a recorded overstatement corrected

The gap note `research/backward/n3-positive-global.md` (gap `G-h1-nonzero-99`)
and round-33 phrasing claimed **"the classification already forces H₁ = 0 at
99"**. That is too strong. Cioabă–Mim Thm 8.4 lists the *allowed* positions of
H₁ ≠ 0, and a putative (99,14,1,2) has λ_min = −4 = −m, m = 4, so it falls in
the finite **exceptional family E₄** bucket — an **allowed nonzero-H₁ position**,
not one the theorem forces to have H₁ = 0. Only the parameters rule out the conference (v = 99 ≡ 3 mod 4 ⇒ (v−5)/4 ∉ ℤ, so 99 is not a conference order), complete bipartite (μ=2≠0), and lattice (λ=1 ⇒ L₂(3) = the 9-vertex rook control) buckets; E₄ is undecided.

So the refutation of the homology line rests on the **controls** — H₁ nonzero on
BOTH rook(3)=4 and bvls=1540 (the exact gate, code/out/pf_h1_closed_form.py,
round 33) — NOT on the classification forcing H₁(99)=0. The gate task
`gate-clique-complex-homology` is already `done` with exactly this (correct)
conclusion. I corrected the two offending lines in `n3-positive-global.md` and
re-stated the gate's `status` to closed with the honest mechanism.

## Claims filed (to derived/CLAIMS.md)

- `cioaba-mim-h1-classification` — the classification assigns (99,14,1,2) to the
  E₄ exception bucket; does NOT force H₁(99)=0; the homology line is refuted as a
  separator by the controls, not the classification.
- `cioaba-mim-lattice-lambda1-is-rook` — the λ=1 lattice member is exactly
  L₂(3) = the rook control; no lattice graph is (99,14,1,2).
- Companion-paper claim `cioaba-guo-ji-mim-spectral-clique` — the 4/5-cycle
  sufficient vanishing criterion; holds-here unchecked (unknown whether a
  putative 99-graph satisfies it); sufficient, so no 99/243 separator.

## Contradiction handling

- The `contradicts:` field on `cioaba-mim-h1-classification` names
  `n3-positive-global`'s "classification forces H1(99)=0" phrasing — the runtime
  parsed the short target ids as dangling claim refs (rendered as "no claim of
  that id is on disk" rows), which is the expected mechanical no-op; the
  substantive correction is in the corrected gap note body.

## Memory

`remember_memory` is still down (degraded server), so the durable finding lives
on disk: the two rewritten digests, the corrected gap note, the two claim blocks,
and this note. Nothing durable was lost; the fallback is the sanctioned one.

## What the run still lacks

Nothing from these two sources: the clique-complex homology line is closed
(refuted-on-arrival as a separator, by a computed control gate). The next open
tasks are the two gates named in TASKS.md (incidence-budget-ledger-controls,
pair-labeling-84), both computational and out of the scholar's tool scope.
