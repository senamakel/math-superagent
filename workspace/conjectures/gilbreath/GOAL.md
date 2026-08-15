# What ends this run, and what counts as a result

## Commentary

**Deliverable claimed — with the supply side explicitly open.** Granville's Lemma 5.4 (arXiv:2607.04166) has been (a) **proved as a general theorem** at its combinatorial core — the descent/absorption lemma: with `x_0=v`, `x_s=|x_{s-1}-c_s|`, `c_s∈{0,2}`, `ν₂=#{c_s=2}`, one has `x_L∈{0,2} ⟺ v ≤ 2ν₂+2`, `v>2ν₂+2 ⟹ x_L=v-2ν₂≥4`, and `{0,2}` is absorbing — and (b) **validated non-vacuously in both the success AND failure directions** on synthetic 2-then-odd failing sequences. **Standing correction (Directives 43/44):** the *written* proof of the descent step is defective on bounce trajectories (`0→2→0`; the "after the ν₂ twos, δ = v − 2ν₂" algebra assumes δ never hits 0, which fails on 100% of real columns); the theorem survives by the case split, but the case-split proof must be written out and Lean-formalised before "proved" is earned at the proof level. **The whole of Route B now rests on a NAMED OPEN problem, not a gap in this run's argument (Directive 47).** The supply statement G-supply (ν₂(q_n) > n^β, β>0.525 — equivalently any positive-linear ν₂ ≥ c·n) reduces cleanly to the frequency of the mod-4 switch bit `[gap ≡ 2 mod 4]`. Ash–Beltis–Gross–Sinnott 2011 §9 (claim `abgs-2011-s9-mod4-switch-limit-open`) establishes that it is OPEN whether `N(a,d,m,x)/π(x)` tends to any limit, so NO unconditional linear lower bound on the mod-4 switch count exists in the literature. Route B therefore yields a **CONDITIONAL theorem** (Lemma 5.4 + Theorem 5.5) whose hypothesis is that two-point mod-4 correlation lower bound. A conditional theorem with a precisely identified open hypothesis is a genuine deliverable; pretending the hypothesis is nearly closed is not. This is NOT a proof of Gilbreath and NOT a closed run: the supply side is the entire remaining open content.

## The deliverable

A **proof, or a genuine partial result stated exactly**. The conjecture has
stood since 1878 and is believed true, so the working assumption is that you
will not prove it. Claiming it on an argument that has not survived attack is
the one outright failure available here.

A partial result that would count:

- a **proved invariant** of the absolute-difference operator forcing
  `A_k(1) ∈ {0, 2}`, under stated hypotheses;

**Closed this run (not a goal deliverable, but a closed dead end):** the raw
run-count potential r(T(x)) ≤ r(x) of the total-variation-oscillation
approach (`research/approaches/total-variation-oscillation-potential.md`) is
**machine-refuted** — exhaustively over 6,725,600 strings, and in each class
the triangle lives in (all-even, halved {0,1,2,3}, halved {0,1}) with the
minimal counterexample (0,0,1,1) → (0,1,0), the halved form of (0,0,2,2)
inside the leading {0,2} regime itself. The on-disk verifier
`code/out/check_runcount_lemma.py` was written but never executed; this run
executed it and the class-restricted companion. The approach's only surviving
direction is a corrected weighted/max-factored potential à la Chamberland's
Ducci proof (`ducci-max-factoring-potential-template`), untested.
- a proof of the conjecture for a **general class of sequences** — since the
  problem is probably not about primes, a theorem covering "2 followed by odd
  numbers with gaps bounded by `g`" would settle the prime case as a corollary
  and would be the strongest realistic outcome;
- Odlyzko's block lemma **re-derived here with its constant made explicit**,
  rather than cited — including exactly how many rows a `{0,2}` block of
  length `n` protects;
- a proved statement about the **regeneration rate** of `{0,2}` blocks, in
  either direction: that it suffices, or that it can fail;
- a **located error in Proth's 1878 claimed proof**, recorded as refuted with
  the failing step named;
- a **Lean 4 formalisation** of the difference operator and the induction
  step, with `#print axioms` output reported and every remaining `sorry`
  listed.

A result stated without the bound it was established under is not a result. An
invariant verified to depth 10^5 is a fact about depth 10^5 unless it is
proved.

## The oracle here is a row generator and a falsifier, not a search

There is no value to recompute — the answer is a proof. So the oracle is:

1. **`rows(primes, depth)`** — exact integer generation of `A_0..A_depth`. No
   floats. It must reproduce the table in `problem.md` exactly:
   `A_1 = 1,2,2,4,2,4,2,4,6,2` and `A_2 = 1,0,2,2,2,2,2,2,4` and
   `A_3 = 1,2,0,0,0,0,0,2`. A generator that does not reproduce those is
   broken, and everything measured against it is worthless.

2. **`block_profile(row)`** — the length of the leading `{0,2}` block, which is
   the quantity Odlyzko's argument is about and the one every claim should be
   phrased in.

3. **The falsification oracle, which is the one that matters.**

> **Every claimed invariant or lemma must be run against the actual rows**, held
> in `code/out/witnesses.json`. A lemma implying `A_k(1) ∈ {0,2}` *always* must
> not also imply something the real rows contradict — and in particular any
> claim about the `{0,2}` structure must be checked against the rows where the
> block is short. A lemma that the generated rows refute is **false**. Full
> stop: record it refuted, not weakened.

Note the asymmetry: the conjecture asserts a positive (`A_k(0) = 1` always), so
the dangerous failure here is a **proof that proves too little but looks like
enough** — an argument that establishes the `{0,2}` regime persists for a
computable number of rows and quietly treats that as persistence forever.
Consumption is not regeneration. Every claim must say which it establishes.

Erosion is settled and regeneration is not, so the target has narrowed. A block
of length `n` protects exactly `n+1` rows — the constant is `1`, and the `n/2`
figure this run started with has been refuted (`odlyzko-block-lemma-exact`, and
the step law in `code/out/step_law_and_recharge_verified.md`). What remains is
the recharge side: `(2,4)`-events are the only mechanism that grows the block,
and the conjecture is exactly the claim that they keep arriving fast enough that
`Σ (j_i + 1)` never falls `k−1` behind. A partial result that bounds the event
rate from below, even under a stated hypothesis on prime gaps, would be a real
contribution; another verification of erosion would not.

## Compute policy — light, parallel, bounded

Verification depth is not the deliverable and is cheap to overspend on.

- **Generating rows is `O(depth × width)` and memory-bound.** A row of width
  `W` to depth `D` costs `O(W)` if you keep one row at a time — do that, and
  never hold the whole triangle.
- **The container has an 8 GiB cap and an OOM kill writes nothing to the
  console.** Say what a run will cost before running it. An OOM is a finding
  about the method, not a reason to ask for more memory.
- **Parallelise the search over hypotheses, not over depth** — depth is
  inherently sequential. `code/lib/parallel.py` with `code/lib/PARALLEL.md` is
  in this workspace; the box has 28 CPUs and no container CPU quota. Testing
  many candidate invariants, or many starting sequences in the general
  Gilbreath-like class, is exactly the shape `parallel_map` and `parallel_any`
  are for.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  Output that only reaches the model is destroyed when the attempt ends.

Use `lean_prover` early for the difference operator and the induction step —
the statement is small and elementary, which makes it unusually well suited to
formalisation, and a machine-checked induction step would be a real artifact.
Report `#print axioms` and every `sorry`; a Lean file asserting it is
kernel-checked with no artifact beside it is worth nothing.

## Ending

Stop and report when you have a partial result of the kind listed above, or
when you can state precisely what blocks the argument and why. Report the depth
reached, the block-length profile observed, which claims are proved versus
verified-numerically, and every remaining `sorry`.
