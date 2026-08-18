# ROOT — What the literature actually establishes

*Last updated: phase 1 of this run. Every statement below is sourced to a file in `research/sources/` or `research/summaries/`; nothing here is recalled. The conjecture is open; no source in this library claims a full proof.*

## The statement

**Toeplitz's Square Peg Problem (1911).** Every Jordan curve γ : S¹ → R² (continuous injective, equivalently a topological embedding) contains four points that are the vertices of a square. No smoothness, convexity, rectifiability, or symmetry is assumed. (Source: Matschke 2014 survey, Conjecture 1 — [[research/summaries/matschke2014-survey-square-peg.md]]).

**Status: OPEN in full generality.** All known positive results prove the conjecture for restricted classes, and every one of them uses the same mechanism: *smooth curves inscribe generically an odd number of squares*, measurable topologically. None extends to arbitrary continuous curves. (Matschke 2014 survey.)

## The verification bound and the oracle

The literature's **computational verification bound** is Pettersson–Tverberg–Östergård 2014 (Discrete Comput. Geom. 51, 722–728): **Conjecture C holds for every grid Jordan curve J ∈ 𝒥′ with o(J) ≤ 13** (grid size n ≤ 13), verified by exhaustive depth-first search with pruning over chordless cycles of the (n+1)×(n+1) grid graph. Conjecture C: a grid curve inscribes a lattice square of side ≥ i(J)/√2, where i(J) is the largest axis-aligned open square in the bounded component. **Theorem 1 of that paper: Conjecture C implies Toeplitz' conjecture** — the limit argument is shrinkout-free because the side length is bounded below by i(J)/√2 > 0. (Note: Matschke's survey says n ≤ 12; the paper itself says n ≤ 13.) ([[research/summaries/pettersson-tverberg-ostergard-2014-toeplitz-note.md]])

Machine-checkable anchors beyond the discrete bound:
- **CDM 2022, Prop. 26:** a non-circular ellipse x²/a² + y²/b² = 1 (a²≠b²) has a transverse configuration-space intersection representing **exactly one** inscribed square. ([[research/summaries/cantarella-denne-mccleary-2022-square-peg-theorem.md]])
- **CDM 2022, Lemma 27:** parallel chords of an ellipse have midpoints on a diameter — the geometric fact behind Prop. 26.
- **Matschke 2009, Thm 1.3:** a continuous curve in the annulus {1 ≤ ||x|| ≤ 1+√2}, nontrivial in π₁, inscribes a square of side ≥ √2 — a *continuous-curve* existence result with an explicit nondegeneracy bound.
- **Rifford 2021, Thm 1.1:** two 1-Lipschitz graphs inscribe a square of side ≥ C·max(g−f), a universal constant C.

## The three restricted classes (with exact hypotheses)

1. **Locally monotone curves (Stromquist 1989, Theorem 2 in Matschke 2014 survey).** γ is locally monotone if every point x ∈ S¹ has a neighborhood U and a linear functional ℓ : R² → R such that ℓ∘γ|_U is strictly monotone. Contains all convex curves, all polygons, and (with restrictions) all piecewise-C¹ curves. Primary source (Stromquist, Mathematika 36, 1989, 187–197) is paywalled; its statement is carried by the survey and by Matschke 2009, and its square conclusion is subsumed by Asano–Ike (Corollary 1.3: every locally monotone curve inscribes a θ-rectangle for all θ, hence a square).
2. **Rectifiable curves (Asano–Ike 2024, Corollary 5.9).** Every rectifiable (finite-length) Jordan curve inscribes a θ-rectangle for every θ ∈ (0,π), in particular a square. **The strongest positive class in the library.** Proved by microlocal sheaf theory (Tamarkin category); the general hypothesis (Theorem 1.1) is the existence of a *continuous Legendrian lift*, which every rectifiable curve satisfies. ([[research/summaries/asano-ike-2024-rectifiable-rectangular-peg.md]]) **Nesting caution:** locally monotone and rectifiable are two *separate* classes, both contained in the Legendrian-lift class (AI Cor 5.9, Cor 5.12, Prop 5.11); no source establishes either nesting, and locally monotone ⊄ rectifiable is plausible (point-dependent linear functionals allow unbounded winding — monotone-in-x graphs with unbounded y-oscillation are locally monotone but not rectifiable). Rectifiable does contain two-graphs (graphs of Lipschitz functions).
3. **Two Lipschitz graphs (Tao 2017 Thm 1.2 → Rifford 2021 Thm 1.1 → Greene–Lobb 2024).** γ = graph(f) ∪ graph(g), f,g : [t₀,t₁]→R agreeing at endpoints, f<g inside. Tao: Lipschitz < 1 ⇒ square. Rifford: Lipschitz = 1 ⇒ square with side ≥ C·max(g−f) (universal C). Greene–Lobb: Lipschitz < 1+√2 ⇒ square; Lipschitz = 1 ⇒ rectangles of every aspect ratio. The 1+√2 threshold is geometric (the 45° meeting angle). ([[research/summaries/greene-lobb-2024-square-pegs-between-graphs.md]])
4. **Matschke's open-dense class (Matschke 2009, Thm 1.4 / Cor 2.10).** An explicit open-dense neighborhood of locally monotone curves in the C⁰ topology; curves inscribing no special trapezoid of size ε (or generically an even number) inscribe a square. Strictly contains Stromquist's class.

**Adjacent, NOT square results (do not conflate):**
- **Vaughan (in Matschke 2014 survey, Thm 7):** every continuous Jordan curve inscribes a **rectangle**. The rectangle problem is solved for continuous curves; the square problem is not.
- **Greene–Lobb 2021 (Annals):** every **smooth** Jordan curve inscribes rectangles of every aspect ratio (symplectic proof via non-existence of Lagrangian Klein bottles in C²). Does **not** transfer to continuous curves. ([[research/summaries/greene-lobb-2021-rectangular-peg.md]])
- **Greene–Lobb 2024 Floer homology:** a rectifiable Jordan curve enclosing more than half the area of a circle of equal diameter inscribes a square (subsumed by Asano–Ike for rectifiable curves).

## Status of the Cantarella–Denne–McCleary claim (checked, not assumed)

problem.md flagged a "Cantarella–Denne–McCleary (2020 preprint) claims a proof of the full conjecture for every continuous Jordan curve." **This claim does not exist in the literature.** The paper (arXiv:1402.6174, 2014; published in split form, Illinois J. Math. 66(2) 2022, DOI 10.1215/00192082-10120454) proves: *there is a C¹-dense family of smooth embedded circles in the plane where each simple closed curve has an odd number of inscribed squares*, plus higher-dimensional analogues. That is a genericity/odd-count theorem for smooth curves — strictly weaker than the full conjecture, and not a proof for general continuous curves. The authors' own note says the preprint was split into three papers; the published IJM paper is the version of record. **The conjecture remains open; the CDM claim as problem.md framed it is closed.** ([[research/summaries/cantarella-denne-mccleary-2022-square-peg-theorem.md]])

## The structure of a minimal counterexample

The literature (Matschke 2014 survey; Tao 2017; Matschke 2009; Asano–Ike 2024) pins the obstruction precisely. A counterexample to the general conjecture, if one exists, must be a Jordan curve γ such that:

1. **It is not rectifiable** — every rectifiable Jordan curve inscribes a square (Asano–Ike 2024, Cor 5.9). So γ must have infinite length: nowhere-rectifiable, fractal-like, with unbounded variation. It also cannot admit a continuous Legendrian lift (the sharp hypothesis of Asano–Ike Thm 1.1). This is a concrete, named frontier: *does every Jordan curve admit a continuous Legendrian lift?* If yes, the conjecture is true; if no, the non-rectifiable non-liftable curves are the only possible counterexamples.
2. **It is not in Matschke's open-dense class and not a two-graphs curve** — otherwise the corresponding theorems give a square.
3. **Its configuration-space parity argument must break.** All positive proofs count inscribed squares mod 2 via the Mobius-band boundary winding number; the count is odd for every curve on which the boundary map is computable. A counterexample must be a curve on which the boundary winding number of the map F is **not well-defined** (failure point 1 of problem.md), OR on which the parity argument finds only **degenerate** intersections (failure point 2), OR on which every inscribed square found by approximation **shrinks to a point** (shrinkout — failure point 3, named by Tao 2017).
4. **Its inscribed squares, if any, must be absent or degenerate at every scale.** Any approximating sequence of rectifiable curves (each with a genuine square, by Asano–Ike) must have side lengths → 0; the limit is a point, not a square. This is the *only* known way a continuous curve escapes the rectifiable theorem: square side length must be forced to 0 along every approximation. Asano–Ike's Legendrian-lift condition is exactly what rules this out for rectifiable curves — the lift pins a positive scale.
5. **Minimality.** Among counterexamples (if any exist), take one with minimal "wildness" — e.g., a limit of rectifiable curves that is itself non-rectifiable, where the squares from each approximant shrink away. The annulus theorems (Matschke Thm 1.3) show the *homotopy class alone* cannot force shrinkout: a nontrivial loop in an annulus must have a square of side ≥ √2. So a minimal counterexample must live in a region where the geometry does not pin a positive scale — in particular it must be thin at every scale (its curve must pass arbitrarily close to itself in ways that forbid large squares).

**Consequence for the run's partial result:** the tractable target is not the general case. It is either (a) a named subclass strictly larger than rectifiable — e.g., non-rectifiable curves that still admit a continuous Legendrian lift — with the corresponding step of the Asano–Ike argument redone, or (b) an exact impossibility statement: a named class of curves on which a specific step of the argument (continuous Legendrian lift / boundary winding number / parity) provably fails, with the obstruction identified. Both are open; the literature's own open threads point at (b) via the Legendrian-lift question and shrinkout.

## What this run's own extension should beat

The obstruction is **shrinkout**, stated exactly: approximating a wild Jordan curve by rectifiable curves yields genuine inscribed squares whose side lengths may converge to 0. Any honest extension of the rectifiable theorem to a larger class must prove a **lower bound on inscribed-square side length** for its class (as Matschke's annulus theorems and Rifford's quantitative bound do), or must show the curve admits a **continuous Legendrian lift** (as Asano–Ike's hypothesis requires). Tao's integral method, Matschke's special-trapezoid criterion, and Asano–Ike's sheaf-theoretic lift condition are the three published devices that achieve nondegeneracy without rectifiability.

## Library inventory (sources on disk)

- `research/sources/matschke2014-survey-square-peg.full.md` — Matschke 2014 Notices survey (canonical entry point)
- `research/sources/cantarella-denne-mccleary-2022-square-peg-theorem.full.md` — CDM 2022 IJM / arXiv:1402.6174
- `research/sources/tao2017-integration-toeplitz-square-peg.full.md` — Tao 2017 Forum Math. Sigma
- `research/sources/greene-lobb-2021-rectangular-peg.full.md` — Greene–Lobb 2021 Annals
- `research/sources/matschke2009-square-peg-relatives.full.md` — Matschke 2009 arXiv:1001.0186
- `research/sources/pettersson-tverberg-ostergard-2014-toeplitz-note.full.md` — Pettersson–Tverberg–Östergård 2014 Discrete Comput. Geom. (verification bound)
- `research/sources/rifford2021-quantitative-tao.full.md` — Rifford 2021 arXiv:2106.01914
- `research/sources/greene-lobb-2024-square-pegs-between-graphs.full.md` — Greene–Lobb 2024 arXiv:2407.07798
- `research/sources/greene-lobb-2024-floer-homology-square-pegs.full.md` — Greene–Lobb 2024 arXiv:2404.05179
- `research/sources/asano-ike-2024-rectifiable-rectangular-peg.full.md` — Asano–Ike 2024 arXiv:2412.21057

Summaries with claim blocks: `research/summaries/` (same names, plus schwartz2022 — the Schwartz BAMS survey's article text failed to capture; its content is covered by Greene–Lobb 2021 and the search passages). Stromquist 1989 primary text and the Schwartz BAMS survey full text are the two named acquisition gaps.
