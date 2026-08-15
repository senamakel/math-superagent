# Proof skeleton: the excess-height renormalization

This does not restate `regeneration-sufficiency.md` (whose single gap
`REG-intruder-drains` is the whole remaining content). It introduces the
adopted bridge from the converging cycle — *excess-height renormalization* —
which does two things the other skeletons do not:

1. it factors out two **provable and not yet filed** structural lemmas (the
   exact self-similarity identity, and the max principle), each a genuine
   "proved invariant of the absolute-difference operator" of the kind GOAL.md
   asks for; and
2. it states the single remaining open content in its sharpest coordinate —
   the number of edge-2 reads a Rule-90 block furnishes in its erosion life —
   where the degenerate sparse patterns are exactly the named-open mod-4
   switch-density obstruction, not a separate mystery.

Conventions: `H_k(j) = A_k(j+1)/2` for `j ≥ 0, k ≥ 1` (integer by the parity
wave), `t_k(j) = max(0, H_k(j) − 1)`, wall `w_k = b_k − 1`, intruder excess
`r_k = t_k(b_k) = A_k(b_k+1)/2 − 1 ≥ 1` (so the intruder is `y_k = 2(r_k+1)`).

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1.
implies: Step 3(i) EH-renorm-identity and Step 3(iii) EH-max-principle are now PROVED: Lean code/lean/excess_renorm.lean (sorry-free, axioms within propext/Classical.choice/Quot.sound, low_case has none) and universal finite-class verification code/excess_renorm_universal.py over {0..6}^9 (46,118,408 positions, 0 violations; complete because the identity is per-pair and the 49 ordered pairs exhaust the hypothesis space). Wall case corrected to t'(j)=t(j+1)-h(j). Claim excess-renorm-identity-proved. The SINGLE remaining open content is Step 5 EH-edge2-supply = the (2,4)-event-arrival = supply side, named-open abgs-2011-s9-mod4-switch-limit-open.
killed-by: (none — new decomposition; its single open gap is the same open content as the run's other live gaps, restated in excess coordinates, and is NOT disguised as provable)
rests-on: gilbreath-reduces-to-second-in-02, step-law-theorem-proved, edge-interior-invertibility-sharpened, rule90-interior-xor, closure-0d-double-edge
status: live
```

```gap
id: EH-renorm-identity
lemma: |
  Let H be a halved Gilbreath row (entries ≥ 0), t(j) = max(0, H(j) − 1),
  H'(j) = |H(j) − H(j+1)|, t'(j) = max(0, H'(j) − 1). Then:
  (a) if t(j) ≥ 1 and t(j+1) ≥ 1, then t'(j) = max(0, |t(j) − t(j+1)| − 1);
  (b) if t(j) = 0 and t(j+1) = r ≥ 1 (wall pair), then t'(j) = r − H(j)
      (i.e. r − 1 when the halved edge H(j) = 1, and r when H(j) = 0);
  (c) if t(j) = t(j+1) = 0, then t'(j) = 0.
  Consequence (excess drain law): with wall at w and r = t(w+1),
  r' = t'(w) = r − [H(w) = 1], i.e. the intruder excess decreases by 1 exactly
  when the halved edge is 1 (edge A = 2) and is constant when the halved edge
  is 0.
status: discharged
discharged-by: excess-renorm-identity-proved (research/notes/excess-renorm-identity-proved.md;
  Lean code/lean/excess_renorm.lean bulk_case/wall_case/low_case, sorry-free, axioms
  ⊆ {propext, Classical.choice, Quot.sound})
next: |
  Prove the three cases from |a−b| and the definition of t (three lines each:
  for (a) write H(j) = t(j)+1, H(j+1) = t(j+1)+1 so H'(j) = |t(j) − t(j+1)|;
  for (b) H(j) ∈ {0,1} and H(j+1) = r+1 so H'(j) = r+1−H(j); for (c)
  H'(j) ∈ {0,1}). Then formalise in Lean 4 over Nat.dist (already used by
  code/lean/descent_lemma.lean) with #print axioms free of sorryAx, and
  tool_builder: verify the identity against every consecutive row pair in
  code/out/witnesses.json (one row live, O(width)). Reproduce the seed
  hand-check h=(0,1,2,4) → t=(0,0,1,3) → h'=(1,1,2) → t'=(0,0,1).
```

```gap
id: EH-max-principle
lemma: |
  With M_k = max_j t_k(j) = max(0, (max_{j≥1} A_k(j))/2 − 1): M_{k+1} ≤ M_k,
  and for every j with t_k(j) ≥ 1 and t_k(j+1) ≥ 1 one has
  t_{k+1}(j) ≤ max(t_k(j), t_k(j+1)) − 1 < M_k. In particular the running
  maximum of the excess is non-increasing along rows, the bulk maximum decays
  by at least 1 per row, and every intruder excess satisfies
  r_k ≤ M_k ≤ M_1 = G₁ := max_{m≥2} ((p_{m+1} − p_m)/2 − 1) = g*/2 − 1.
  HONESTY: this bound is the demand-side / Link-A bound in excess coordinates
  (the same content as `gap-bounds-cannot-force-block-growth`'s "row maximum
  is non-increasing" and Granville's v ≤ g*), and it grows with the record
  gap, so it is NOT an absolute intruder bound and does NOT discharge the old
  G-intruder gap. The absolute bound `r₀ ≤ M` (empirically M = 6 at depth
  1000, i.e. y ≤ 14, and one wider-run instance r₀ = 26) is
  `REG-intruder-sharp-bound` in regeneration-intruder-drain.md and remains
  OPEN; this lemma is the proved half that would combine with it.
status: discharged
discharged-by: excess-renorm-identity-proved (research/notes/excess-renorm-identity-proved.md;
  Lean code/lean/excess_renorm.lean max_principle/bulk_strict/bulk_strict_ltM, sorry-free)
next: |
  Immediate from EH-renorm-identity cases (a)–(c) plus |a−b| ≤ max(a,b).
  theorem_prover/lean_prover: formalise as a corollary in the same Lean file
  as EH-renorm-identity (M_{k+1} ≤ M_k and the strict bulk decay), reporting
  #print axioms and zero sorry. tool_builder: verify M non-increasing and the
  bulk-decay inequality on the halved rows of code/out/witnesses.json
  (0 violations expected); also verify r_k ≤ G₁ on every intruder of the
  erosion-run records (code/out/erosion_run_draining.captured.txt) — the
  measured max r₀ = 6 (y₀ = 14, depth 1000) sits far below G₁, so the
  demand-side slack is large; record that this does NOT bound r₀ absolutely.
```

```gap
id: EH-edge2-supply
lemma: |
  For the prime Gilbreath triangle, every erosion run that starts from a
  nonzero block of length n = b_start with intruder excess r₀ = y₀/2 − 1 has
  at least r₀ − 1 edge-2 reads within its erosion life n — equivalently the
  Rule-90 edge sequence e_0..e_{n−1} (e_d = XOR_{j : C(d,j) odd} h[(n−1−d)+j],
  h the halved starting block) contains ≥ r₀ − 1 ones. By Steps 3–5 this is
  exactly: every erosion run reaches intruder y = 4 with b ≥ 1, i.e. the
  (2,4)-event arrival statement, which is Route B's supply bound
  ν₂(q_n) ≥ c·n in right-diagonal coordinates.
status: open
next: |
  STATUS HONESTY FIRST: this is the single remaining open content of the
  conjecture, not a gap in the run's own argument. The universal version is
  FALSE — the halved pattern [1,0,…,0] (and its mirror) has exactly one
  edge-2 read in n reads (edge-interior-invertibility-sharpened, the sharp
  n−1 zero-run), so any uniform lower bound > 1 fails. The prime-specific
  version is the named-open mod-4 switch-density problem
  (abgs-2011-s9-mod4-switch-limit-open): no unconditional linear lower bound
  on the switch bit exists in the literature. The attackable deliverable is
  therefore the CONDITIONAL theorem. First move (theorem_prover +
  lean_prover): formalise "Hardy–Littlewood / Lemke Oliver–Soundararajan
  two-point mod-4 correlation ⟹ for every prime erosion run e_0..e_{n−1} has
  ≥ r₀ − 1 ones", composing the discharged linearization
  (rule90-interior-xor, G-supply-linearization) with Lemma 5.4
  (lemma54-re-derived-proof); the correlation hypothesis is ASSUMED, not a
  gap. Second move (tool_builder, to fix the exact constant the conditional
  theorem must reproduce): from code/out/erosion_run_draining.captured.txt
  report, per run, (r₀, edge-2 count over life, n, count/(r₀−1)); the
  recorded max r₀ = 6 (y₀ = 14, depth 1000) means at most 5 edge-2 flips are
  needed, so the theorem only has to exclude the finitely-many degenerate
  sparse Rule-90 edge patterns.
thread: research/threads/regeneration.md
```
