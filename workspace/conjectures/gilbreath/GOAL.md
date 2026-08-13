# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**. The conjecture has
stood since 1878 and is believed true, so the working assumption is that you
will not prove it. Claiming it on an argument that has not survived attack is
the one outright failure available here.

A partial result that would count:

- a **proved invariant** of the absolute-difference operator forcing
  `A_k(1) ∈ {0, 2}`, under stated hypotheses;
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
