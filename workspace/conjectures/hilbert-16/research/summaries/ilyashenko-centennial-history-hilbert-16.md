# Ilyashenko 2002, "Centennial history of Hilbert's 16th problem" (Bull. AMS 39(3):301–354)

Source: `research/sources/ilyashenko-centennial-history-hilbert-16.full.md` [[ilyashenko-centennial-history-hilbert-16.full]] — AMS PDF (verified content). A concatenated mirror copy is [[ilyashenko-centennial-history-h16.full]].

## What the source establishes (canonical survey, verified statements)

- **Theorem 2.1 (Finiteness Theorem)**: a polynomial vector field in the plane has only finitely many limit cycles; same for analytic fields on the 2-sphere. Proved by Écalle (1992) and Ilyashenko (1991). This is the individual-field finiteness (Dulac's problem), not the uniform H(n).
- **Dulac's error** (Section 3): Dulac inferred triviality of the return map of a polycycle from triviality of its asymptotic expansion — the exact C^∞-vs-analytic failure. Ilyashenko's 1984/85 result: limit cycles cannot accumulate on a polycycle with only hyperbolic saddle vertices (Theorem 3.5); the correspondence map of a hyperbolic saddle is **almost regular** (Lemma 3.4), a quasi-analytic class.
- **Theorem 2.2 [V, Kh84]**: the upper bound V(n) in the infinitesimal Hilbert 16th problem exists (non-constructive; Varchenko–Khovanskii).
- **Theorems 2.3–2.4 [IYa95, Kaloshin]**: E(k) exists for families with elementary singular points; E(k) ≤ 2^{25k²}. The Hilbert–Arnold problem is positively solved for elementary-singularity families.
- **Exactness Theorem 7.1 [I69a,b, Pu]**: for an ultra-Morse H of degree n+1 ≥ 3, if I(t) ≡ 0 over ovals then ω is exact. This yields **Corollary 7.1**: for ultra-Morse H with N = (n²+n)/2 − 1 ovals and any δ > 0, there is a perturbation dH + εω with N limit cycles near those ovals.
- **Theorem 7.7 [GI\*]**: for H critically balanced (sum of two critically bounded one-variable polynomials), deg ω ≤ n, the number of zeros of the Abelian integral over an oval family is ≤ **e^{2500n⁴}** (explicit, but restricted to critically balanced H — not general ultra-Morse). General V(n) bound: tower of four exponentials (Theorem 7.6).
- **Petrovskii–Landis** attempted solution refuted by Novikov–Ilyashenko (Section 3); the DRR 121-program and the H(3) "unrealistic" remark at §5.2.

## What it implies here

Sourced anchors for: `h16-dulac-finiteness-theorem`, `h16-kaloshin-uniform-bound`, `h16-abelian-integral-bounds` (V(n) exists; e^{2500n⁴} for critically balanced; tower-of-4 for the general case). The Exactness Theorem/Corollary 7.1 is the clean quantitative statement behind "M(n) ≥ (n²+n)/2 − 1"-type lower bounds — the dimension-count argument in Liang–Torregrosa's weak-foci work and the (n²+n)/2 − 1 tangential lower bound. The Dulac-error description (Section 3) is the canonical statement of problem.md's smooth test.

Evidence class: sourced-held — read from the held full text. Hypotheses: as stated per theorem (polynomial fields; ultra-Morse/critically balanced H). Falsifier: a polynomial field with infinitely many limit cycles (would refute Theorem 2.1); a counterexample to the e^{2500n⁴} bound within its hypotheses.