# Individual finiteness: every fixed polynomial planar field has finitely many limit cycles

```claim
id: h16-dulac-finiteness-theorem
statement: Every fixed polynomial planar vector field (P,Q of arbitrary fixed degree) has finitely many limit cycles. This is the Dulac conjecture, proved independently by Ilyashenko (1991) and Écalle (1992). It is the INDIVIDUAL (pointwise) finiteness theorem: for each fixed field, the number of its limit cycles is finite; it gives NO bound uniform in the coefficients, which is exactly the H16.2 uniformity gap. The proof is contested in parts: Yeung (arXiv:2402.12506 and follow-ups) claims an ordering-of-asymptotics gap in Ilyashenko's semi-hyperbolic proof, without disproving the theorem; Gasull–Llibre 2024 note the proofs "are not fully accepted by the mathematical community" per Smale's surveys.
hypotheses: individual polynomial vector field of fixed degree; analyticity of the return map at regular points and quasi-analyticity/almost-regularity at the polycycle; limit cycles cannot accumulate on a polycycle of an analytic field (the non-accumulation theorem).
holds-here: yes (pointwise)
status: asserted-by-source (proof contested in parts, not disproved)
evidence: sourced-held — Ilyashenko's book "Finiteness theorems for limit cycles" (research/sources/primary-ilyashenko-finiteness-book.full.md): "This book is devoted to the following finiteness theorem: A polynomial vector field on the real plane has a finite number of limit cycles"; Kaloshin's IFT statement (research/sources/kaloshin-around-hilbert-arnold.html.full.md line 71); encyclopedia (research/sources/encyclopedia-hilbert16-wikipedia.full.md line 58); Gasull–Llibre survey (research/sources/gasull-abel-hilbert16-2024.full.md line 140); Yeung's contention (research/sources/yeung-ilyashenko-finiteness-gap.full.md). The quadratic special case is Bamon 1986, IHES 64:111-142, "Quadratic vector fields in the plane have a finite number of limit cycles" (research/sources/primary-bamon-quadratic-finiteness.pdf.full.md line 65, Theorem A) — held full text.
falsifier: A counterexample (a polynomial planar field with infinitely many limit cycles) would falsify the theorem; a source establishing that the Yeung critique invalidates a necessary step of both proofs (not just one) would downgrade it to open. The current record holds it as the established individual-finiteness theorem with the Yeung contention flagged, not as disproved.
sources: https://bookstore.ams.org/MMONO/94 (Ilyashenko 1991); https://doi.org/10.1007/BF02699193 (Bamon 1986); https://arxiv.org/abs/2402.12506 (Yeung 2024 contention)
anchors: research/sources/primary-ilyashenko-finiteness-book.full.md lines 159, 236; research/sources/primary-bamon-quadratic-finiteness.pdf.full.md line 65; research/sources/kaloshin-around-hilbert-arnold.html.full.md line 71; research/sources/yeung-ilyashenko-finiteness-gap.full.md
note: This is the pointwise-finiteness rung that the H16.2 uniformity question sits above. It is a Lean Cited-axiom anchor (code/lean/h16_dulac_finiteness-ed8142ab.lean) — conditional, not formalised. Do NOT cite it as a uniform bound; the whole DRR program exists because it is not one.
follows-from:
answers:
```

## Why this claim block exists

`h16-dulac-finiteness-theorem` is cited across approaches, summaries and the scholar
claim blocks (three `contradicts:` lines point at it), but no claim block with this
id was on disk. This block records the individual-finiteness theorem with its held
primary anchors, the Yeung contention, and the explicit uniformity caveat that makes
it the wrong tool for H16.2 by itself.
