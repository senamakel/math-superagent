# Wu, "Non-invariance of the Brauer–Manin obstruction for surfaces" (arXiv:2103.01784)

[[wu-non-invariance-brauer-manin]]
Full text: `research/sources/arxiv-2103.01784.abstract.full.md` (arXiv:2103.01784v2;
this workspace holds the abstract page and the full-text variant
`research/sources/wu-non-invariance-brauer-manin.full.md`).

## What it establishes

Assuming **Stoll's conjecture** (Conjecture 3.0.1: for a curve C over a number
field K, C(K) is dense in the Brauer-informed adelic points `pr∞_K(C(A_K)^Br)`),
Wu constructs, for **any nontrivial extension L/K of number fields**, two kinds
of smooth projective geometrically connected surfaces over K (not necessarily
K3):

1. A surface with a K-rational point satisfying weak approximation with
   Brauer–Manin obstruction off ∞_K, whose base change to L fails weak
   approximation with BM obstruction off ∞_L;
2. A Hasse-principle counterexample explained by the BM obstruction over K, whose
   base change's HP failure is NOT explained by BM over L.

Explicit unconditional examples are given illustrating both phenomena
(constructions over Q with K-rational points; the base-change examples use
elliptic surfaces / diagonal quartic surfaces per the full text).

## Bearing on this run

**Guards the K3 base-extension question.** Bremner's extension-field MSS
(`extension-field-mss-exist`) sit over degree-4 fields `Q(√3,√133)` and degree-27
`Q(u)`; Wu shows BM-obstruction behaviour is *not* invariant under base change,
so an obstruction over Q could vanish over the extension (or appear there). This
does NOT give this run a positive tool, but it kills the naive inference
"no Q-obstruction ⇒ no obstruction anywhere" and the reverse. The explicit
surfaces are elliptic/diagonal-quartic, not the Category III K3 S of Bremner II
(which anyway already has a Q-point, `catIII-k3-has-q-point`), so the transfer of
Wu's construction to S is not immediate. `holds-here: no` as a direct theorem —
its hypotheses (Stoll's conjecture, general surfaces) are not verified for S, and
S(Q) is already nonempty.

```claim
id: wu-bm-noninvariance-under-base-change
statement: Assuming Stoll's conjecture, for any nontrivial extension L/K of
  number fields there exist smooth projective geometrically connected surfaces
  over K whose Brauer-Manin obstruction behaviour (weak approximation off the
  archimedean place; Hasse principle) changes under base change to L, in both
  directions, with explicit unconditional examples.
hypotheses: Stoll's conjecture Conj 3.0.1 for curves over K; L/K nontrivial
  extension; surfaces geometrically connected
holds-here: no (conditional on Stoll; surfaces are not the Category III K3 S,
  and S(Q) is already nonempty so BM cannot prove S(Q)=empty)
status: proved (conditional, = Theorem-level statements + explicit examples in
  the full text; the abstract alone is asserted)
bearing: cautions against base-change-invariance arguments with the
  Brauer-Manin obstruction across Bremner's extension-field MSS; supports the
  RUN's standing 'any proof must separate Q from Q(sqrt3,sqrt133)' guard
anchor: research/sources/arxiv-2103.01784.abstract.full.md,
  research/sources/wu-non-invariance-brauer-manin.full.md
```