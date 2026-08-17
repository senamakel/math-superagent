# Scholar direct-verification pass — the load-bearing n3 source against its primary text

Status: verification completed. No new source acquired — the library is CLOSED
(ROOT.md, directive 18–19). This pass's job was to re-read the primary full
text of the one source the run's sharpest live lever leans on, and confirm the
digested note is faithful. It is.

## What was verified directly (this pass, against the Russian primary)

Source: A. A. Makhnev, "О сильно регулярных графах с λ=1" (On strongly
regular graphs with λ=1), Mat. Zametki 44(5) 667–672 (1988). Full text held at
`research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`
(mathnet.ru paperid=4220, open access).

Read word for word this pass. Confirmed:

1. **Condition (*), verbatim**: "любая пара треугольников из Γ, соединенных
   по крайней мере двумя ребрами, соединена точно тремя ребрами" — any pair
   of triangles joined by at least two edges is joined by exactly three edges.
   This is exactly Reimbayev's `n_3 = 0`. The note's identification is faithful.

2. **Theorem 1, verbatim**: a strongly regular graph with λ=1 satisfying (*)
   is either μ ≤ 3 or the unique (27,10,1,5). Faithful.

3. **Theorem 2, verbatim**: no srg(99,14,1,2) or srg(115,18,1,3) satisfying
   (*). Makhnev's own words: this is "a partial answer to Seidel's question on
   the existence of an srg(99,14,1,2)". Faithful.

4. **The 99 mechanism, verbatim**: the proof builds Λ₀ = {A} ∪ Λ₁ ∪ Λ₂ where
   Λ₁ are the 12 triangles (36 points, Lemma 6) meeting the closure Γ(A), and
   Λ₂ the 20 outer triangles (60 points, Lemma 7), on 33 triangle-vertices;
   Lemmas 8–9 show Λ₀ is an srg(33,12,1,6) satisfying (*); it contradicts
   Theorem 1 (μ=6>3, not (27,10,1,5)). Lemma 6 gives |Γ(A)| = 36+3 = 39, NOT
   9 — confirming the note's warning that the "9-point closure" phrasing is a
   misreading.

5. **The run's independent strengthening is distinct from the sourced lemma
   chain**: Makhnev rejects srg(33,12,1,6) via his Theorem 1 (μ=6>3 branch).
   The run additionally observes srg(33,12,1,6) is parameter-infeasible by
   eigenvalue-multiplicity integrality directly: √Δ = 7 does not divide
   `2k + (v−1)(λ−μ) = 2·12 + 32·(1−6) = 24 − 160 = −136`. That integrality
   step is a checked computation (`code/out/check_srg33_12_1_6.captured.txt`),
   SEPARATE from the sourced lemma chain — it belongs to the (λ=1, μ=6)
   family which integrality rejects, a different family from (99,14,1,2).
   Both reject Λ₀; they are independent and agree. Claim
   `makhnev99-shorter-proof-integrality` records this correctly.

## Result

Claim `makhnev1988-condstar-theorems` is a faithful reading of the primary
text. The contrapositive the whole n3 pivot rests on —

> **any putative srg(99,14,1,2) has n_3 ≥ 1** (a constraint, not a
> nonexistence proof; the n_3≥1 interior case remains open)

— is sourced from the primary text and its mechanism confirmed. Both control
graphs rook(3) and bvls_graph() satisfy (*) with n_3=0 (checked,
`code/out/makhnev-1988-condition-captured.txt`), so the theorem does not rule
them out (μ≤3 branch) and they cannot refute an n_3≥1 argument. This is the
correct, current state.

## No contradiction found

The digested note, the thread `n3-forced`, and the primary text all agree.
Nothing in this pass contradicts recalled memory or an earlier claim. The
"contradiction between sources" the run once worried about (Bagchi/BN1988
μ=2 dichotomy vs BvLS existence) was already resolved (`c6-resolved-no-bite`),
and the two sources at issue there agree once the second branch k < (λ+1)(λ+2)
is restored.

## Sources that add nothing new this pass

- `brouwer-haemers-srg-chapter.md` — paywalled landing page; only the standard
  definition.
- `makhnev-2013-local-subgraphs-srg-99.md` — paywalled, body absent.
- `vanlint-brouwer-srg-partial-geometries-1984` — garbled OCR, do not cite.
- `zehavi-oliveira-not-conway-99.md` — solves a *variant*, not the problem.
- `keramatipour-sat-conway99.md` — no reportable boundary; confirms
  enumeration is the wrong method.
- `bagchi-mu2-correct.md` — wrong paper (pre-Lie); correct Bagchi content in
  `research/notes/bagchi-mu2-dichotomy-resolution.md`.
- `index.full.md`, `cesarz-woldar-automorph-conway99.md`, `makhnev-1988-lambda1.md`
  — duplicate landing pages of real content held elsewhere.

These are maintained from prior passes and re-confirmed.

## Cognee note

`remember_memory` failed again this pass (memory server down — the same outage
directive 20 warned about; 6 failures this run). The verified finding above is
therefore recorded here on disk, which is the authoritative record. When the
memory server recovers, the verified Makhnev statement should be re-stored with
source URL and hypotheses (it is already carried as claim
`makhnev1988-condstar-theorems` in `derived/CLAIMS.md`).
