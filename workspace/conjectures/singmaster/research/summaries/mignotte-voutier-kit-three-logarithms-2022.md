# Mignotte–Voutier (with appendix by M. Laurent), "A kit for linear forms in three logarithms" (Math. Comp., accepted; arXiv:2205.08899)

Source: https://arxiv.org/abs/2205.08899 (landing page; full PDF at https://arxiv.org/pdf/2205.08899)
Full text on disk: `research/sources/mignotte-voutier-kit-three-logarithms-2022.full.md`
(Note: what is on disk is the arXiv landing page with abstract and metadata, not the
full body text — the paper's detailed lemmas/constants are in the PDF, which this
container did not convert. The claim below is the abstract-level statement.)

## What this source is

A 2022/2023 method paper (Mignotte, Voutier; appendix by Laurent) providing an
interpolation-determinant "kit" for **linear forms in three logarithms of
algebraic numbers**, producing explicit bounds significantly better than the
general Matveev-style results. Public code accompanies it. Accepted by
Mathematics of Computation.

## Relevance to this run

The adopted `baker-linear-forms-two-logarithms` approach and the
`matveev-explicit-*` computations need explicit lower bounds for linear forms in
logarithms with **computable constants**. This is the state-of-the-art toolkit
for exactly that: it improves on Matveev in the three-logarithm case (with
worked numerical reductions, e.g. bounds from ~10^12 reduced to ~10^6). For the
run's per-pair effective-deliverable, this is a stronger constant supplier than
Matveev alone — relevant whenever a collision reduces to Λ = b1 log a1 +
b2 log a2 + b3 log a3 (three logarithms), which is the natural shape after the
falling-factorial reduction (log n1, log n2, log(k1!/k2!)).

## Claim block

```
id: mignotte-voutier-three-log-kit
statement: There is an explicit, implementable technique (interpolation determinants,
  Laurent zero lemmas) giving lower bounds for nonzero linear forms in three complex
  logarithms of algebraic numbers, with numerical constants better than the general
  Matveev bounds; worked examples reduce bounds on the variables from ~10^12 to ~10^6.
hypotheses: linear form in 3 logarithms of algebraic numbers; nonzero; algebraic
  numbers may be variable (the kit's strength) or fixed (then Matveev + LLL is advised).
holds-here: yes, conditionally — the run's equal-binomial reduction gives two-logarithm
  forms (log n1, log n2) per the adopted approach; the three-logarithm case arises for
  some reductions (log n1, log n2, log(k1!/k2!)). The kit is a constant-improver, not a
  new framework for Singmaster.
status: asserted-by-source (abstract; peer-reviewed venue accepted; full constants in PDF)
source: https://arxiv.org/abs/2205.08899
```

## Why it was fetched

Deep-research survey of 2022–2026 literature found NO new results on the MRSTT
boundary, no new effective constants for C(x,k1)=C(y,k2), no new witnesses
beyond 3003/Fibonacci. The Mignotte–Voutier kit is the one genuinely useful new
method piece for the run's effective-bound route. It is now indexed with its
claim; if a specific computation needs its constants, the PDF body should be
fetched separately.