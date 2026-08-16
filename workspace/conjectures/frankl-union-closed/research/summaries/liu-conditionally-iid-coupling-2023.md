# Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling

Jingbo Liu. arXiv:2306.08824 (Jun 2023). Preprint (CISS 2024 conference);
not (as of the run's record) a journal paper.
Full text (read, at least the abstract + structure):
`research/sources/liu-conditionally-iid-coupling-2023.html.full.md`

<!-- source: https://arxiv.org/html/2306.08824v1 ; also https://arxiv.org/pdf/2306.08824 -->

## What it establishes (sourced; numerical claims marked)

Liu improves the entropy bound **strictly** above the Sawin/Yu value
(0.38234) by using a richer coupling class: the two binary sequences are
**i.i.d. conditioned on an auxiliary random variable** (conditionally IID
coupling), strictly containing Sawin's convex-combination class. Provides a new
class of bounds in finite-dimensional optimization form.

Under numerically-verified structural hypotheses on a **9-dimensional
optimization** (the optimizer is conjectured/observed to take a specific
structured form), the bound improves to **≈ 0.38271**.

The state-of-the-art layout, per this paper:
- iid-Gilmer coupling: cap (3−√5)/2 ≈ 0.38197 (AHS/Chase–Lovett/Sawin/Pebody);
- Sawin's mixture (iid + max-entropy): ≈ 0.38234 (Yu, Cambie);
- Liu's conditionally-IID: strictly > that, ≈ 0.38271 under numerically
  verified hypotheses.

## Why it matters for this run

Liu shows the entropy method is **not** capped at the (3−√5)/2 barrier nor at
Sawin's 0.38234 — a richer coupling class escapes both. This directly bears on
the "is there a proved barrier for the entropy method" question: no proved
barrier stopping at 0.38234 exists; the frontier goes to ≥ 0.38271 (conditional
on Liu's numeric hypotheses). The 9-d optimization structure is the next thing
the attack-coupling work would implement — this run now has its source.

```claim
id: liu-conditionally-iid
statement: Using conditionally-IID couplings (the two sequences are i.i.d.
  conditioned on an auxiliary variable), the entropy bound is strictly greater
  than Sawin's 0.38234; a 9-dimensional optimization gives ≈ 0.38271 under
  numerically verified structural hypotheses.
hypotheses: F union-closed; the optimizer structure is numerically verified,
  not proved in full.
holds-here: true
status: asserted
bearing: the strongest known entropy bound (0.38271) but conditional on numeric
  hypotheses and unpublished as a journal paper; do not cite as the published
  record.
anchor: Liu arXiv:2306.08824; full text in sources.
```

```claim
id: liu-no-barrier-at-record
statement: There is no proved barrier stopping the entropy method at
  (3−√5)/2 or at 0.38234: strictly stronger couplings (conditionally-IID) give
  a bigger constant, so a "method-capped" theorem would have to restrict the
  coupling class explicitly.
hypotheses: none.
holds-here: true
status: asserted
bearing: refines the "proved barrier" target: it must be stated for a precisely
  delimited class of entropy/coupling arguments.
anchor: Liu arXiv:2306.08824; full text in sources.
```
