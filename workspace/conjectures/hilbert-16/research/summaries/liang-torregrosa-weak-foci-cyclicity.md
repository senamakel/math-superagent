# Liang–Torregrosa — Weak foci of high order and cyclicity

Full text: [[liang-torregrosa-weak-foci-cyclicity.full]]. Qual. Theory Dyn. Syst. © (2023/24); note the stored file is a Springer **preview page** — abstract references only, not the full paper. Claims below are abstract-level.

## What the source establishes (abstract level, held)

Study of M(n) — the number of limit cycles bifurcating from a singularity of
center-focus type — via cyclicity of weak foci, for concrete n:

- For even n, the system of Qiu–Yang (JDE 246, 2009) attaining **weak-focus
  order n²+n−2** is studied for n = 4, 6, …, 18.
- A system with a weak focus of order **(n−1)²** for n ≤ 100 is provided.
- Christopher's approach (Differ. Equ. Symb. Comput., 2006) — originally for
  studying cyclicity of centers — is shown to apply also to weak foci, and by
  concrete examples the cyclicity is obtained in a simple computational way.
- Computation on a Xeon (CPU E5-450, 3.0 GHz, 384 GB RAM) — the machine note
  matters for the run's Bautin-ideal feasibility wall.

## What it implies here

- Corroborates the literature boundary: M(2)=3 (Bautin) is not re-derived here;
  the paper is about higher-degree lower bounds on small-amplitude cyclicity.
- The Bautin/Lyapunov machinery (ideal of Lyapunov quantities) is the run's
  R-local-focus-bautin rung; this source hints at the computational scaling
  (n² order quantities for degree n, Xeon-scale). The feasibility wall statement
  is the run's phase-4 deliverable.

```claim
id: h16-liang-torregrosa-weak-foci
statement: Weak-focus order (hence lower bounds for M(n)) can be as large as
  n^2+n-2 for even n (Qiu-Yang class, n=4..18) and (n-1)^2 for n <= 100;
  Christopher's center-cyclicity method extends to weak foci, giving cyclicity by
  computation.
hypotheses: degree-n systems; focus/center singularity; n as stated.
holds-here: unchecked -- abstract-level preview, not full text.
status: asserted
bearing: confirms the small-amplitude (M(n)) lower-bound landscape and the
  computational route to cyclicity; the exact numbers are abstract-level only.
anchor: research/sources/liang-torregrosa-weak-foci-cyclicity.full.md
```

## Does not help

The full text is paywalled; the exact system coefficient matrices and the
cyclicity numbers are not in the held preview. Do not cite precise values beyond
the abstract.