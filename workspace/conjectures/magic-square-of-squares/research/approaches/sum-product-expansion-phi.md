```approach
idea: Recast the additive-triple condition q1 + q2 = q3 with all q_i ∈ Φ = f(Q),
       f(x) = 4x(1−x²)/(1+x²)², as a question about the additive energy / sum-product
       structure of the value set of a degree-4 rational map, and bound it with the
       generalised sum-product / Elekes–Szabó / Polynomial Freiman–Ruzsa machinery
       (Gowers–Green–Manners–Tao; arXiv:2603.06483). A Φ-quadruple (q1, q2, q1+q2,
       q1−q2 all in Φ) lifts to a full MSS, so bounding additive relations in Φ to a
       finite, explicitly listed set settles the problem. This differs from the adopted
       uniform-height approach (whose bound C^(r+1) is ineffective — C unknown) by using
       the effective sum-product/PFR mechanism.

mechanism: Φ carries rich multiplicative structure — f is a group-coordinate map,
       f(x) = sin(4 arctan(x)) = the y-coordinate of [4]P on the unit circle — and the
       additive relation q1+q2=q3 is an additive coincidence inside a multiplicatively
       structured set. Elekes–Szabó-type results bound |f(A) ∩ (f(A)+f(A))| for A ⊂ Q of
       bounded height; the full-set question is controlled by the same expansion once a
       height is introduced. arXiv:2603.06483 resolves Bremner's conjecture on arithmetic
       progressions in coordinates of elliptic curves by exactly this combination (sum-
       product in algebraic groups + Diophantine geometry, using Gowers–Green–Manners–Tao
       PFR), and the Robertson reduction (MSS ⟺ three points of 2E(Q) on
       E: y² = x(x²−c²) with x-coordinates in AP) places the MSS inside that framework.
       The mechanism is orthogonal to the refuted Φ-Faltings line (which was geometric
       genus, and degenerated): this is additive-combinatorial expansion, not curve genus.

first-step: Download arXiv:2603.06483 and extract its main theorem verbatim (exact
       hypotheses and conclusion on additive relations / APs in coordinate sets of elliptic
       curves). Determine whether it yields an explicit finite list or explicit bound for
       x(2E(Q)) containing an AP of length ≥ 3 on E: y² = x(x²−c²), and whether the same
       argument transfers to the Φ-set formulation f(Q) ∩ (f(Q)+f(Q)).

status: refuted
killed-by: (1) HMS Theorem 1.1 (arXiv:2603.06483) bounds the LENGTH of an AP inside a
       single coordinate set {x(P):P in E(Q)} of an elliptic curve — the Robertson-curve
       formulation, i.e. the adopted uniform-height thread, NOT the Φ-value-set additive
       coincidence alpha+beta=gamma. No theorem in the library transfers to the Φ-set form.
       (2) Elekes-Szabo / PFR / sum-product are finite-population COUNTING statements
       (bound |Z(F) ∩ A×B×C| for large finite A,B,C); they cannot rule out a SINGLE
       coincidence q1+q2=q3 of two specific values. (3) The "effective PFR beats ineffective
       uniform-height-C" premise is false: HMS Theorem 1.1 already states an effectively
       computable C that is never exhibited and is built from David-Philippon uniform-ML
       constants one cannot size; the weak-PFR constants (140,110) feed the sum-product
       lemmas but NOT the §7 proof of the AP-length theorem. The candidate renames the
       adopted uniform-height thread, then asks for a Φ-transfer no source provides.
precedent:
       - https://arxiv.org/abs/2603.06483 (Harrison, Mudgal, Schmidt, "Uniform sum-product
         phenomenon for algebraic groups and Bremner's conjecture", 2026) — Theorem 1.1
         AP-length bound effective-in-principle but uncomputed; does NOT cover Φ value-set.
       - https://doi.org/10.19086/77361 (Bays, Dobrowolski, Zou, "Elekes-Szabo for groups",
         Discrete Analysis 2023:6) — ES expansion is population-counting.
       - claim hms-2026-bremner-effective-constant (this run, research/summaries/...html.md)
         — C effective-in-principle, no explicit value; PFR constant not in §7 proof.
       - this run's phi-no-triple-m400 (m,n <= 400 exhaustive, zero triples) — a finite
         check, not a transferable theorem.

speculation-vs-established: ESTABLISHED (this run, checked) — the Φ reduction
       (phi-universal-set): d ∈ S(e) ⟺ d/e² ∈ Φ, and a Φ-quadruple ⟺ full MSS;
       f(m,n) = sin(4 arctan(n/m)). ESTABLISHED (sourced) — Robertson/Bremner reduction.
       SPECULATION — that arXiv:2603.06483's sum-product bound is effective and tight
       enough to rule out length-3 APs of doubled x-coordinates; the first step is to read
       the actual theorem, and it fails if the bound is existential or larger than 3.
```
