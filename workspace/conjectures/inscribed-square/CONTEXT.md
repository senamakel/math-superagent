# Context — what this run knows (surveyed 2026-08-18)

## The problem and its status

Toeplitz's Square Peg conjecture (1911): every Jordan curve γ : S¹ → R² (continuous injective; no smoothness) inscribes a square. **Open in full generality.** No source in this library claims a proof; the only full-proof-style claim anywhere is Yoshiki Ueoka's Zenodo preprint series (2025–26, unvalidated, 0 citations — its C¹→C⁰ degree step is exactly the step the literature calls unsolved). Do not treat as established (`research/sources/asano-ike-2024-status.md`; claim `arxiv-sweep-2025-2026-no-full-proof`).

The CDM "full conjecture proof" that problem.md suspected does **not exist**: CDM (arXiv:1402.6174, published split as Illinois J. Math. 66(2) 2022) proves only that a C¹-dense family of smooth circles has an odd number of inscribed squares. Conjecture open; that question is closed (claim `cdm2022-no-full-conjecture-proof`).

## Established, cited (asserted-by-source unless marked)

- **Stromquist 1989**: every locally monotone Jordan curve inscribes a square (Mathematika 36, 187–197; via Matschke 2014 survey Thm 2). Local monotonicity = every point has a neighbourhood on which some linear functional is strictly monotone. Claim `cited-stromquist-1989`, `matschke2014-stromquist-locally-monotone`.
- **Matschke 2009 Thm 2.8/Cor 2.9**: no square ⟹ mod-2 intersection i(S, P₄(ω)) = 1 for *every* generator ω of π₁((S¹)²\Δ) ≅ Z; if some generator's membrane avoids the special-trapezoid locus S then i = 0, contradiction ⟹ square. Cor 2.10: no special trapezoid of size ε (0<ε<1), or generically an even number, ⟹ square. Claim `matschke2009-mod2-intersection`, `matschke2009-special-trapezoid-criterion`.
- **Matschke 2009 Thm 1.4**: explicit C⁰-open-dense neighbourhood of locally monotone curves, every curve in it inscribes a square. Claim `matschke2009-open-dense-class`.
- **Matschke 2009 Thm 1.3**: nontrivial loop in annulus {1 ≤ ‖x‖ ≤ 1+√2} inscribes a square of side ≥ √2 — the published prototype of a quantitative nondegeneracy bound (claim `matschke2009-annulus-quantitative`).
- **Asano–Ike 2024** (arXiv:2412.21057 **v3, 5 Jan 2026 — preprint only, NOT peer-reviewed, v2 fixed an error in §5**): Theorem 1.1 — if a Jordan curve admits a continuous Legendrian lift (C⁰ limit of smooth curves whose lifted primitives converge uniformly on compacta), it inscribes a θ-rectangle for all θ, hence a square. Cor 5.9: every **rectifiable** curve admits the lift. Cor 5.12: every locally monotone curve does (via its own Prop 5.11, not via rectifiability). Claims `asano-ike-2024-thm1-1`, `-cor5-9-rectifiable-square`, `-cor5-12-locmon-rectangle`, `-continuous-legendrian-lift-defn`; status file records preprint/OpenAlex 0-citation evidence. **Rectifiable is the strongest positive class in the library.**
- **Tao 2017 / Rifford 2021 / Greene–Lobb 2024**: two Lipschitz graphs (constant < 1 / = 1 with side ≥ C·max(g−f) / < 1+√2) inscribe a square.
- **Pettersson–Tverberg–Östergård 2014**: the literature's computational bound — Conjecture C (grid curve inscribes lattice square of side ≥ i(J)/√2) verified for grid size n ≤ 13; Conjecture C implies Toeplitz. Claims `pto2014-verification-bound-n13`, `pto2014-conjecture-c-implies-T`. Note: survey says n≤12, paper says n≤13.
- **Greene–Lobb 2021 (Annals)**: smooth curves inscribe every rectangle aspect ratio (symplectic; does **not** transfer to continuous). Vaughan (survey Thm 7): every continuous Jordan curve inscribes a rectangle.
- **Chambers 2025**: C⁰-near-C² curves inscribe a positive-side square (claim `chambers2025-stability-near-C2`).

## The single frontier (thesis `legendrian-lift-frontier`, standing)

Every rectifiable curve has a continuous Legendrian lift; the question **does every Jordan curve admit one?** is open, and if yes, Asano–Ike Thm 1.1 settles the whole conjecture. A minimal counterexample, if one exists, must be non-rectifiable (infinite length), outside Matschke's open-dense class, with every approximating square shrinking to a point (**shrinkout**, Tao 2017 — the only known escape). The three published nondegeneracy devices: Matschke annulus bound, Rifford quantitative bound, Asano–Ike lift condition. CDM 2021 (FTCWC): no explicit shrinkout example is known and no general lower-bound argument exists.

## Formalized in Lean (kernel verdicts in code/out/lean/*.json)

- `Lib/Statement.lean` — `Toeplitz.toeplitz_inscribed_square`: conjecture as a type (Circle = AddCircle 1, Plane = EuclideanSpace ℝ (Fin 2), CyclicallyOrdered via real lifts a<b<c<d<a+1, square = diagonal conditions). Compiles; outcome **failed only from the intended `sorry`**; axioms [propext, sorryAx, Classical.choice, Quot.sound].
- `Lib/Stromquist.lean` — `Cited.stromquist_square_peg` axiom (docstring cites Stromquist 1989 + Matschke 2014). Outcome **conditional**; axioms add only `Cited.stromquist_square_peg`. Ledger records asserted-by-source until a theorem is proved *from* it.
- `SanityCyclic.lean` — two lemmas (CyclicallyOrdered forces t₁≠t₂, t₁≠t₃). Outcome **verified**, no sorry.
- `matschke2009_mod2_intersection-aec7691d.lean` — abstract Mod2IntersectionData structure; parity theorem is an input field, so this checks the logical reduction, not the geometry.
- `matschke2009_special_trapezoid_criterion-4ca30655.lean` — Cited axiom, Cor 2.10/2.12 schema.
- `toeplitz_square_peg_G_named_class_membrane-77cb53e4.lean` — NamedMembraneData structure; theorem conditional on hypothesis `hC` (the geometric membrane-avoidance premise, unproved). **This is the file CONTEXT.md's own prior line refers to.**
- `toeplitz_square_peg_G_curve_outside_published_classes-a7681979.lean` — logical exhibit shape; exclusion predicates are explicit parameters because C is undefined.
- `aikl2025_coisotropic_c0_rigidity-fe871eba.lean` — AIKL 2025 coisotropic rigidity, conditional on Cited axiom; method-adjacent only, does not bear on the lift question.

**Lean environment gotchas (learned, do not re-learn; code/out/lean-formalisation.md):** no cross-file imports (each file self-contained, re-declares Circle/Plane); the circle module is Mathlib.Analysis.Complex.Circle; no Inner on ℝ×ℝ (use EuclideanSpace ℝ (Fin 2)); AddCircle has no LinearOrder so monotonicity is stated on real lifts; docstring directly before `namespace` is a parse error; `#print axioms` needs fully-qualified names.

## Exact computation (all exact rational arithmetic, never floating-point)

- `code/brute.py` (oracle, deliberate C(n,4) exponential): unit square → 1, 2×1 rectangle → 0, diamond → 1 — matches hand-checked distance sets. `code/square_peg/oracle.py`: O(m²) edge-pair formulation for boundary squares, exact Fractions.
- `code/square_peg/verify_symmetric.py` + `code/out/verify_symmetric.txt`: reproduced the 3 sanity cases; **line-symmetric hexagon [(0,0),(2,0),(3,1),(2,2),(0,2),(-1,1)] is a simple Jordan polygon and inscribes exactly one square ((0,0),(0,2),(2,2),(2,0))**; irregular pentagon → none. Instance of published Nielsen–Wright symmetry theorem, not new mathematics. Independent checker `independent_check.py` agrees.
- **Dead end:** `check_oracle.py`'s ellipse numbers are invalid — `rat_ellipse_polygon` uses angles 2·arctan(2k/n), not 2πk/n, so vertices do not approximate the ellipse. `research/approaches/ellipse-oracle-invalid.md`. The CDM Prop 26 anchor (non-circular ellipse ⟹ exactly one square) is **not** computationally verified. oracle_check.txt's ellipse/circle numbers must not be cited.
- Sequence-extraction passes (code/out/sequence_review_2026-08-18.md): no exploitable exact regularity in polygon-size lists; no further runs warranted.
- The refute attempt `code/refute/g_membrane_avoids_special_trapezoids.p` (first-order fragment: every Jordan curve has ε with no special trapezoid) returned **undecided / none reported** — encodes only 4-point distinctness + special predicate, no topology; inconclusive, not a result.

## Ruled out / dead ends

- **CDM full-conjecture proof: does not exist** (see above) — closed.
- **Ellipse oracle reproduction: invalid** — rational angle formula wrong; must not cite.
- **Locally monotone ⊂ rectifiable: unproven, likely false** (Feller–Golla note; point-dependent functionals allow unbounded winding). Treat as separate classes, both inside the Legendrian-lift class.
- **Asano–Ike–Kuo–Li 2025** (C⁰-rigidity of Legendrians/coisotropics): does not settle the lift question (claims `aikl2025-legendrian-lift-frontier-still-open`).
- **Hugelmeyer 2024** solves the *periodic* variant; Tao Conjecture 4.6 has Toeplitz ⟹ periodic, not conversely — does not settle Toeplitz.
- **Sequence regularity: none found** — no structural conjecture from the polygon-size lists.
- **The full-conjecture reduction** (Skeleton A in research/backward/toeplitz-square-peg.md) is sketched, not live: it reduces to the single gap "every Jordan curve has a generator ω with P₄(ω) ∩ S = ∅", which is the whole conjecture. The run is committed to Skeleton B instead.

## What the run is committed to (GOAL.md, backward/toeplitz-square-peg.md)

A partial result, not the conjecture: extend the parity argument to a named class C strictly larger than locally monotone. Three open gaps, in dependency order:
1. **G-named-class-membrane** (load-bearing): define C and prove membrane-avoidance on it. Candidate C: locally monotone except at a finite controlled set of points. First move planned: extend the exact special-trapezoid enumerator to a polygon with one non-locally-monotone vertex; check S(ε) emptiness and square nondegeneracy as the corner sharpens.
2. **G-nondegeneracy-bound-on-C**: side length bounded below on C (kills shrinkout).
3. **G-curve-outside-published-classes**: exhibit γ₀ ∈ C outside locally monotone / Matschke open-dense / two-Lipschitz-graphs, with exact verified square.

**The obvious next unresolved thing:** fix the class C concretely and settle G-named-class-membrane — the exact-arithmetic experiment on a polygon with one bad corner (does a small-ε special trapezoid appear; does the membrane stay disjoint; does the square stay nondegenerate) is the designed first attack, and its collapse point, if any, is the obstruction that bounds C. The alternative frontier, R4-legendrian-lift (is the lift class strictly larger than rectifiable?), is the other open direction and the thesis's standing bet. Both are named, unattacked, and nonempty. Attempts and reductions ledgers are empty — no candidate has been proposed, scored, or rejected yet.
