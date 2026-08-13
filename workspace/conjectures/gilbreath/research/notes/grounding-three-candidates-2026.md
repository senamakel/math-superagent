# Grounding report — three candidate approaches (2026 grounding cycle)

Question asked of the literature, per candidate: what is the reformulation
actually called; the precise theorem it relies on and whether its hypotheses
hold here; whether anyone has applied it to Gilbreath; what it would buy.
All three are registered in `research/approaches/`; all three are now
**refuted**, each on evidence (hand-checkable computations plus held claims),
not on absence. Two of the three refutations use the run's own established
record; the literature search confirmed the named theory is real but does not
reach the nonlinear absolute-difference operator.

## Candidate 1: `gantmacher-krein-oscillatory-matrix-sign-regularity`

- **What it is called**: the Gantmacher–Krein oscillation theorem /
  variation-diminishing property of totally positive (sign-regular) matrices.
  Precise modern form: *A has the variation-diminishing property
  S⁺(Ax) ≤ S⁻(x) for all x ≠ 0 iff A is strictly sign-regular* (Choudhury–
  Yadav, Proc. AMS, arXiv:2307.11822 / doi 10.1090/proc/17026). Classical
  antecedents: Fekete–Pólya 1912, Schoenberg 1930, Motzkin, Gantmacher–Krein
  1950; Karlin 1965 (eigenvector oscillation of STP matrices,
  doi 10.1007/BF02806392); modern TP/TN control theory (Schwarz 1970 TPDS,
  Margaliot et al. 2019).
- **Hypotheses hold here? NO — three independent failures.**
  (1) The load-bearing matrix M_{k,j} = (−1)^{k−j} binom(k,j) is NOT
  sign-regular of order 2: the 2×2 minor on rows {1,2}, cols {0,1} is
  (+1), while rows {1,2}, cols {0,2} is (−1). (Hand check; script
  `code/out/check_three_candidates.py` written but not executed this cycle.)
  So the VD theorem's hypothesis fails at the first nontrivial order.
  (2) The claimed bound S⁻(Δ_k) ≤ S⁻(A_0) is false at k=2 on the primes:
  A_0 strictly increasing gives S⁻(A_0)=0, but the signed second difference
  D_2 = (1,0,2,−2,2,−2,2,2) has 4 sign changes after deleting zeros.
  (3) The mechanism needs A_k(i) = |Δ_k(i)|, which is **already refuted** at
  (k=3,i=2) inside the leading {0,2} block and at position 1 from k=4 on —
  claim `fwd-diff-identity-refuted`, evidence checked. This is the same
  mechanism as the already-refuted `sign-coherence-forward-differences`
  approach: oscillation theory is a new name for the same dead linearization.
- **Applied to Gilbreath before?** No. The actual Gilbreath literature
  (Odlyzko 1993, CHT 2026) uses the mod-4 linearization and the
  {0,d}-block obstruction language, never VD theory. The run's earlier
  `runcount-lemma-refuted` bearing already recorded that the
  Schoenberg/Pólya-frequency/total-positivity machinery is LINEAR sign-variation
  theory and does not transfer to the nonlinear |a−b| map.
- **What it would buy**: nothing — the linearization cannot start (identity
  false inside the block) and the matrix is not sign-regular.

## Candidate 2: `zero-sum-flow-conservation-mincut`

- **What it is called**: max-flow/min-cut (Ford–Fulkerson 1957,
  doi 10.4153/cjm-1957-024-0), Menger, Hall, Dilworth — classical network
  flow theory.
- **Hypotheses hold here? The network formulation is a restatement, not a
  theorem.** The recharge identity b_k = b_1 + Σ(j_i+1) − (k−1) is already
  PROVED (claim `step-law-and-recharge-identity`, evidence checked, zero
  failures to depth 800). On the forward chain S→row1→…→rowk the min-cut
  value is exactly b_k: there is no branch structure for a cut to exploit.
  "No cut of capacity < consumption" ⟺ "b_k ≥ 1 ∀k" is the conjecture
  itself in flow language. The required lemma (pumps inject at least some
  minimum mass on average) is exactly the open regeneration-rate question;
  the run's own data says a mean-rate bound is the wrong target
  (`bigjump-cap-characterization-1000`: 12 genuine giants carry 86.1% of the
  surplus; `conditional-rate-experiment-family-independent`: λ̂=0.585 measured,
  not bounded below for all k). The class-level version is false by Eppstein
  2011 (`anti-gilbreath-construction`): his 2-then-odds sequences run the
  "flow" dry infinitely often.
- **Applied to Gilbreath before?** No source in the flow literature touches
  iterated absolute differences of primes (searches confirmed; the Gilbreath
  literature itself has no network formulation).
- **What it would buy**: a clean vocabulary for the proved recharge identity
  (endowment + pump injections − consumption), but no new mathematics. The
  flow theorem is correct and inert: single-chain network ⇒ min-cut = b_k.

## Candidate 3: `fenchel-duality-minimax-sign-assignment`

- **What it is called**: Fenchel–Rockafellar duality / LP duality over a
  sign-history polytope; the relevant literature is the **absolute value
  equation (AVE)** body: Mangasarian 2007 (AVEs NP-hard; orthant/sign-pattern
  solution structure, citeseerx 10.1.1.416.1189), Hladík et al. 2024
  (arXiv:2404.06319: AVE solution sets are unions of ≤ 2ⁿ convex polyhedra,
  one per orthant), Hladík–Hartman 2023 (arXiv:2307.03510: absolute-value LP
  duality).
- **Hypotheses hold here? NO — two decisive failures.**
  (1) The representation A_k(1) = max over a static sign set of a linear
  functional is false: reachable sign histories depend on the gap values
  through the min branch. The identity A_k = |Δ_k| this needs fails at
  (k=3,i=2) (`fwd-diff-identity-refuted`).
  (2) The universal claim — the polytope's structure forces the dual minimum
  ≤ 2 for ANY even-gap input — is FALSE as a class statement: the Colonna
  delete-5 sequence (2,3,7,11,13,17,19,23,…), a 2-then-odds input with all
  gaps after the first even, has A_1(1) = 4 (claim
  `colonna-deletion-left-edge-failure`, held). Hand-check: gaps
  1,4,4,2,4,2,4,6,2,6,4 give A_1 = (1,4,4,2,4,2,4,6,2,6,4). The polytope
  theorem would have to exclude this input — and why the primes lie in the
  surviving subclass is precisely the conjecture.
  (3) The AVE literature gives the orthant geometry but no bound for nested
  absolute iterates on even-gap inputs, and AVE solvability is NP-hard —
  evidence against a cheap universal certificate.
- **Applied to Gilbreath before?** No. The AVE/absolute-value-LP literature
  studies Ax ± |x| = b (one level of absolute value), not k-fold nested
  absolute values; no source applies Fenchel duality to the iterated
  difference operator.
- **What it would buy**: genuine expressive power (nested absolute values as
  a minimax) and a real literature, but no theorem in it bounds nested
  iterates; the universal class claim is false; the needed subclass
  restriction is the conjecture. The orthant-decomposition picture survives
  only as vocabulary.

## Search record (what was tried, what was found)

- VD/TP theory: found the real theorems (Choudhury–Yadav 2024; Karlin 1965;
  Carnicer–Goodman–Peña 1995 generalization; TPDS/CVDDS control theory) —
  all for LINEAR sign-regular operators; none applies to |a−b|.
- Pascal matrix: found total nonnegativity of the *un*alternated Pascal
  matrix (bidiagonal factorization literature, Call–Velleman 1993,
  Koev/Higham survey 2024); the *alternated* Pascal matrix the candidate
  needs is not sign-regular (hand check).
- Gilbreath + flow: no source; the Gilbreath literature itself has no
  network formulation.
- Gilbreath + duality/AVE: found the AVE body (Mangasarian 2007, Hladík
  2024/2023, Rohn 2012); none touches nested absolute differences.
- Crank sweep: Okolo 2025 "Resolution of Gilbreath's Conjecture and the
  Principle of Invariant Dissipation" (Zenodo 10.5281/zenodo.16658833)
  surfaced — already classified not-load-bearing in the library
  (`library-state.md`); do not cite.
- One check could not be run: `code/out/check_three_candidates.py` was
  written but this cycle has no execution tool; the two decisive facts (2×2
  minors of both signs; D_2 sign changes = 4; A_1(1) = 4 for delete-5) are
  elementary hand computations and the third (A_k=|Δ_k| false) is the stored
  machine-checked claim `fwd-diff-identity-refuted`.

## Verdicts

All three candidates are **refuted on evidence**, and each refutation names
the exact obstruction:

- gantmacher-krein: matrix not sign-regular; S⁻(Δ_k) ≤ S⁻(A_0) false at k=2;
  the linearization identity is false inside the block (same mechanism as the
  already-refuted sign-coherence approach).
- zero-sum-flow: the min-cut certificate is a restatement of the already
  proved recharge identity; the missing lemma (jump-mass lower bound) is the
  conjecture; class-level false by Eppstein.
- fenchel-duality: the static-sign-set representation is false (min branch
  makes reachable histories input-dependent); the universal even-gap claim is
  false (Colonna delete-5, A_1(1)=4); the AVE literature gives geometry but
  no bound and NP-hardness cuts the other way.

Each file in `research/approaches/` now has `status: refuted`, a `killed-by`
line, `precedent` with source URLs and claim ids, and a fenced claim block.
`research/APPROACHES.md` re-derived accordingly.
