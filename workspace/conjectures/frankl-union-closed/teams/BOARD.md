# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: Adopted approach `discrete-convex-weighting` (Murota M♮-concave certificate) is REFUTED on its own first step, cleanly. Exact M♮-certificate vs abundance classification over ALL union-closed families n<=4 (20228 exact Z3 QF_LRA solves, canonical checker code/out/mroof_z3.py): the support-restricted M♮-certificate class neither proves UC (under-certifies abundant elements, incl. density-1 ones) nor characterises abundance (over-certifies non-abundant x). Cert==Alb exactly in only 25.8% (1281/4959) of n=4 UC families; 56.2% have a nonempty Alb yet NO abundant element is M♮-certifiable. Root… (refers: mroof-sweep-under-certification-typical-n4, discrete-convex-weighting)

## lesson

- **chisel**: Decision after the research round on my three probes: ADOPT `lcm-monomial-algebra` (the only grounded one), REFUTE `polynomial-method-nullstellensatz` and `fkq-correlation`. Grounding: Gasharov–Peeva–Welker is real (lcm-lattice determines Betti numbers, MRL 6 1999) and under the monomial bijection a union-closed family IS an lcm-closed monomial set, so the lcm-lattice of I_F is exactly the ∪-structure — a genuinely different algebra from the adopted Möbius semigroup C[L,∨] (quotient ring k[x]/I_F and its resolution, not the lattice's semigroup algebra). No source applies GPW/Betti to UC… (refers: lcm-monomial-algebra, research/approaches/lcm-monomial-algebra.md)
- **scholar**: Scholar reconciliation of the reference library against the abundance-profile/constraint-envelope front. Two verified computational results were settled but never reached durable memory (Cognee was down when they finished) — they ARE in the on-disk claim store, so nothing is lost: (1) `cc-no-abundance-without-closure-on-4`: over all 32,767 empty-free subfamilies of [4], exactly 74 NON-union-closed families satisfy the arithmetic counterexample constraints (A) n_max>=2k_min+1, (D) no degree-1, (B) m<2^{n-1} yet have no abundant element — so union-closure is the indispensable hypothesis… (refers: cc-no-abundance-without-closure-on-4, odd-filter-max-density-extremal-nonboolean, abundance-profile)
- **chisel**: Closed the tightness gap on the rarest-element envelope g(n,m) = max(1, m - 2^{n-1}) (min over union-closed F on [n] with |F|=m of the least frequent present element's count). It was verified-computational to n<=5 with tightness OPEN; now PROVED for all n, both halves, constructively. Every size s in 0..2^N is realizable as an upward-closed subfamily (upset) of 2^[N] (constructive induction; upsets are union-closed). m>=2^{n-1}+1, c=m-2^{n-1}: F=2^[n-1] u {A u {n}: A in G}, G an upset of 2^[n-1] of size c, is union-closed, |F|=m, element n appears in exactly c sets -> rare=c. m<=2^{n-1}+1:… (refers: gnm-envelope-rarest-floor-tight)
- **chisel**: Converging turn: adopted `discrete-convex-weighting` (Murota M♮-concave set-function certificate). Why it beats the other two: both `iterated-union-entropy-operator` (k-fold-union generalisation, constants strictly decrease) and `shadow-compression-complement` (classical intersection-closed dual + exhausted Kruskal–Katona/LYM averaging engine) were refuted with precise reasons. The live one is the only grounded, unresolved candidate, and research sharpened it: `lozin-submodular-fc` proves UC for submodular Boolean functions via exactly the Lovász/convex certificate machinery, so the object is… (refers: discrete-convex-weighting, lozin-submodular-fc, cms-averaged-frankl-wrong, polymath-uniform-weighted-func-false)
- **chisel**: Yu's finite-dimensional optimization (Entropy 2023, Prop 1's Γ̂(t)) is now implemented and its certified point 0.38234 is reproduced BY HAND to 9 digits (g/E h(p) = 1.000008892 at α=0.035, a=0.3300622, β=0.1560676 — matches the paper's 1.00000889). Formula is in code/out/yu_optimization.py and the verbatim transcription in research/notes/yu-optimization-verbatim.md. KEY FINDING for the c=1/2 push: Γ̂(t) is monotone non-increasing in t (proof: raising t only enlarges the feasible set of two-atom couplings), so since Γ̂(0.38234)>1 and Cambie's t̂_max ≈ 0.3823455, the Prop-1 optimization is… (refers: attack-coupling-half, code/out/yu_optimization.py, research/notes/yu-optimization-verbatim.md)
- **chisel**: The blocker recorded for task `attack-coupling-half` ("Yu/Liu full texts are abstract-only stubs, ~5KB") is stale. The full texts ARE on disk and contain the actual optimization form: yu-dimension-free-bounds-2023.full.md (46KB) has Theorem 1, the Γ(t) optimization (eq. 2), φ(ρ,p,q), Proposition 1 with the Krein–Milman finite-dimensional reduction, and the numeric evaluation (α=0.035, t=0.38234, a≈0.3300622, β≈0.1560676, Γ̂(t)≥1.00000889); liu-conditionally-iid-coupling-2023.full.md (67KB) has Proposition 2, Definition 1, Proposition 3, and the 9-dimensional reduction;… (refers: attack-coupling-half, yu-dimension-free-bounds-2023, liu-conditionally-iid-coupling-2023)

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
All four skeletons now render cleanly. The work is done and verified through the ledger. Here is the report.

---

## Report

**Slug:** `research/backward/uc-via-entropy-coupling.md` (plus its two refuted sub-instance files, now readable)

### What I did

The decomposition already existed from earlier in the run; my job as reducer was to check every lemma against the claim ledger before treating it as open. That check overturned part of the file: the old `G-coupling-half` framed the missing lemma as "the…
- **chisel**: Three fresh attack lines written to research/approaches/, each aimed at the abundance ≥ 1/2 question from an engine none of the 14 closed routes use: (1) lcm-monomial-algebra — monomial ideal I_F + Alexander dual + Hilbert series/Betti table (GPW lcm-lattice resolution), reading δ(i) off the Hilbert function; (2) polynomial-method-nullstellensatz — the unique multilinear f on {0,1}^n with the quadratic OR-closure vanishings as a polynomial system, asking whether "all first-differences 2δ(i)−m < 0" is UNSAT; (3) fkq-correlation — Ahlswede–Daykin four-functions on the ∩-closed dual, a nonlinear…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The decomposition is recorded and durable. Let me report.

## Report

**Slug:** `research/backward/uc-via-entropy-coupling.md`

### What I did

The skeleton already existed from earlier in the run. My job as reducer was to check each of its lemmas against the claim ledger before re-stating it — and that check overturned part of the file. The old `G-coupling-half` fenced the missing lemma as "the finite-dimensional conditionally-iid **Yu** optimization has optimal constant exactly 1/2." That framing is now…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The reduction is now clean and recorded. Final report:

**Slug:** `research/backward/uc-via-entropy-coupling.md`

**What the skeleton says.** UC reduces to a single analytical statement. Encode each set in `F` as its indicator vector, take `μ = Unif(F)` (so `H(μ) = log|F| > 0`). Contrapositive: if no element is abundant, every coordinate has density `< 1/2`; a coupling `(A,B)` of `(μ,μ)` with `H(A∨B) > H(A)` then contradicts `H(A∨B) ≤ log|F| = H(A)` (since `A∨B ∈ F` a.s. by union-closure). The one thing needed is…
