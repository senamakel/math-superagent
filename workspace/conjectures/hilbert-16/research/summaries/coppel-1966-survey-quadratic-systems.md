# Coppel, "A survey of quadratic systems" (1966) — held

[[coppel-1966-survey-quadratic-systems]]

**Source URL:** https://rainbow.ldeo.columbia.edu/~alexeyk/Papers/Coppel1966.pdf (open copy on a Columbia/LDEO mirror; published as J. Differential Equations **2** (1966) 293–304, DOI 10.1016/0022-0396(66)90070-2). Full text held at `research/sources/coppel-1966-survey-quadratic-systems.full.md` (617 lines, OCR'd from PDF).

## What this source is
The canonical 1966 survey of planar **quadratic** systems (P, Q relatively prime, degree ≤ 2, not both linear). It is the historical baseline for the degree-2 case of H16.2 and the earliest systematic account of the quadratic centre problem, Bautin's M(2) = 3, and the (then open) status of the Petrovskii–Landis "at most three limit cycles" claim. Cited by 17 of this library's held sources (Ilyashenko 2002, Ilyashenko–Yakovenko, BNY, etc.), which is why it belongs in the canonical tier.

## What it establishes (statement by statement, all pre-1966)

1. **Quadratic centre problem — complete solution (Theorem in §2).** For the system
   ẋ = −y + ax² + (2b+α)xy + cy², ẏ = x + bx² + (2c+β)xy + dy²
   (a real normal form of quadratic systems with the origin as a singular point of focus/centre type), the origin is a centre **iff one of three explicit conditions holds**:
   - **I.** a + c = b + d = 0,
   - **II.** α(a+c) = β(b+d), and α³ − (3b+α)α²β + (3c+β)αβ² − dβ³ = 0,
   - **III.** α + 5(b+d) = β + 5(a+c) = ac + bd + 2(a² + d²) = 0.
   Necessity by the Poincaré–Lyapunov procedure (finitely many steps), sufficiency because in each case the equation integrates in elementary functions (e.g. in case III an integral of the form f²/g³ = const with f quadratic, g cubic). Attributed to the Kapteyn–Frommer–Bautin–Šaharnikov–Belyustina–Sibirskii line; Coppel says this final form "is not available in the western literature" and states it in full. **This is the classical Bautin centre-variety statement, in the 1966 western-survey form.**
   - Consequence recorded by Coppel: integrability determines how far the closed curves extend, that **a limit cycle and a centre cannot coexist**, and the possible phase portraits of a quadratic system with a centre.

2. **Bautin's M(2) = 3 (§3).** "It was proved by Bautin [1],[2] that for quadratic systems this maximum number is three" — the maximum number of limit cycles that can appear in a neighbourhood of a weak focus. Coppel also records that this was "the starting point for the remarkable work of Petrovskii and Landis", who attempted to show a quadratic system has at most three limit cycles **altogether**, and — importantly — Coppel's contemporaneous judgement: *"Professor Jürgen Moser tells me that in addition to the published errata [32] further mistakes have been found, which have still not been corrected. Judgment on the validity of Petrovskii and Landis' result must therefore be suspended."* **This is a primary contemporaneous source for the Petrovskii–Landis gap, predating and independent of the later literature.**

3. **Tung Chin-chu's configuration theorems (Theorems 1–4, §3), stated with proofs.** For a quadratic system:
   - **Lemma:** three critical points can never be collinear; on any straight line not composed of paths, at most two critical points/contacts; with two such points the crossing senses are as described.
   - **Thm 1:** the interior of a closed path is a convex region.
   - **Thm 2:** there is a unique critical point in the interior of each closed path.
   - **Thm 3:** two closed paths are oppositely oriented if their interiors are disjoint; hence no three closed paths can be situated as in Fig. 2.
   - **Thm 4:** two closed paths are similarly oriented if their interiors intersect.
   - Theorems 1–4 hold also for **separatrix cycles** (Jordan curves of paths and saddle-points).
   - Corollary (conditional on Petrovskii–Landis): the only possible limit-cycle configurations with ≤ 3 cycles are the five in Fig. 3; existence of systems realising (a)–(e) is attributed to Frommer, Bautin, Yeh, Tung. (Shi's four-cycle example is 1979–80, after this survey.)

4. **Critical-point structure (§§4–5):**
   - **Thm 5:** two critical points each of which is a focus or centre are oppositely oriented; hence **at most two foci/centres total** (Berlinskii; simpler proof by Kukles–Casanova, reproduced).
   - **Thm 6:** a critical point in the interior of a closed path must be a focus or a centre (Vorob'ev's result, with Coppel's polar-coordinate proof).
   - **Thm 7 (Berlinskii):** with four critical points, if the quadrilateral is convex then two opposite are saddles and the other two antisaddles; if not convex, either the three exterior vertices are saddles and the interior one an antisaddle, or vice versa. Full proof via normalising the four points to (0,0),(1,0),(0,1),(α,β).
   - **Bautin [3]: a system of the form ẋ = x(a₀+a₁x+a₂y), ẏ = y(b₀+b₁x+b₂y) (the Kolmogorov/Lotka–Volterra form) cannot have a limit cycle.** Proof via the Dulac function B(x,y) = x^{k−1}y^{l−1} and Green's theorem (this is one of the earliest Dulac-function nonexistence arguments; note it is exactly the instrument the workspace's oracle spec names for nonexistence certificates).
   - Also recorded: Berlinskii's classification of critical-point distributions; Latipov on points at infinity; Chin Yuan-shun on elliptic limit cycles; Čerkas on algebraic limit cycles of degree 3; Lyagina on homogeneous quadratic phase portraits.

## Implications for this problem (H16.2)
- **Directly relevant to the Bautin-ideal oracle and Lean Bautin.lean:** Coppel §2 gives the three explicit centre conditions — the classical Bautin centre variety in the 1966 western form. The workspace's exact Lyapunov-quantity computations (code/bautin) and the Lean statement of M(2)=3 rest on this same classical content; this source is now the held primary/canonical anchor for the centre-variety statement and for "a limit cycle and a centre cannot coexist".
- **Historical anchor for the M(2)=3 claim** (GOAL.md step 1: "reproduce Bautin's M(2)=3 — the literature boundary") and for the Petrovskii–Landis gap (problem.md's test-1 warning has a 1966 source saying the gap was already known to Moser before the published errata were even complete).
- **Dulac-function precedent:** the no-limit-cycle proof in §5 is exactly the shape of the workspace's nonexistence certificate (Dulac function + sign condition on div(B·X)); Coppel is a clean citation for that method's classical pedigree.
- **Configuration constraints:** Thms 1–4 are real constraints on the *second half* of H16.2 (possible configurations of limit cycles) for n = 2: convexity of the interior of each closed path, unique critical point inside, orientation constraints, ≤ 2 foci/centres. These are the kind of configuration statements the goal's item 5 ("realisability of configurations") can build on.

## Evidence class
`asserted-by-source` — this is a survey, and every theorem above is stated with proof in the held text, but this run has not independently verified the proofs; where the run builds on them (e.g. the centre conditions, the Dulac-function argument) the computation should re-derive the specific statement. The OCR is from a scan and has formula corruption (e.g. "2" for sums, mangled subscripts), so the three centre conditions are quoted here as read, and the exact coefficient indexing should be re-checked against Bautin 1952 (held) before a Lean statement cites them.

## Falsifier
A primary source showing Coppel mis-stated the centre conditions, or a computation showing the three conditions do not characterise the quadratic centre variety (the held Bautin 1952 and the workspace's own Lyapunov computations are the cross-check).
