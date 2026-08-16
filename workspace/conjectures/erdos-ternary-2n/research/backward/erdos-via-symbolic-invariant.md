# Erdős ternary conjecture — reduction to a symbolic invariant on the ×2 orbit

The goal decomposed into: (i) the elementary congruence structure any counterexample must
carry, (ii) the already-established sparse case (Dimitrov–Howe), and (iii) the one genuine
residual — a finite-state statistic along `{2^n}` that separates the digit-`{0,1}` set `S`
from the tail of the orbit. The inference below is the actual argument; the gaps are what is
still missing to make it a proof.

```skeleton
goal: Prove or obtain an exact partial result on the Erdős ternary conjecture (2^n has a base-3 digit 2 for all n>8), working as a dynamical/symbolic system.
implies: Counterexample 2^n digit-2-free forces |A|=c1(n) even (proved) and 2-adic vanishing sum_N_c 3^c ≡ 0 mod 2^r (family); Dimitrov-Howe rules out |A|<=25; the residual ≥26-ones case is the open middle-digit region.
killed-by: none yet — the skeleton is live in its sketched state.
rests-on: DIMITROV-HOWE-26-ONES (asserted-by-source, Rocky Mountain J. Math); LAGARIAS-NARKIEWICZ-BOUND (sourced, used only to locate the difficulty).
status: live
```

## Why the invariant cannot be a continuous function of the 3-adic point

The obvious reading of "an invariant preserved by `x -> 2x` on `Z_3`" is a function `F: Z_3 -> Z`
with `F(2x) = F(x)`. That reading is **refuted before it starts**: the orbit `{2^n}` of `1`
under `x2` is dense in `Z_3^x`, so a continuous (or merely uniformly continuous) `F` invariant
under `x2` is constant on the orbit closure, hence cannot distinguish `S`. G-invariant below is
therefore stated on the *sequence index* `n` / the finite digit strings, where "invariance under
the dynamics" means property (a): `Phi` evolves by a fixed finite transducer step along the
`x2` carry, not that it is a function of the 3-adic limit point. This is a deliberate narrowing,
and it is the honest reading of the directed route in `problem.md` (carry/transducer statistic).

```gap
id: G-cong
lemma: Every digit-2-free power 2^n with n >= 1, written 2^n = sum_{a in A} 3^a for A the set of
  1-positions, satisfies (i) |A| = 0 (mod 2), and (ii) sum_{a in A} 3^a = 0 (mod 2^k) for every
  integer k with 1 <= k <= n.
status: discharged
discharged-by: c1-even-parity (R1, claim recorded in code/out/regularity_findings.md; part (i)
  follows because c1(n)=|A| is even for all n>=1; part (ii) is 2^n ≡ 0 mod 2^k for k <= n,
  trivial). Holds for ALL n >= 1, not just digit-2-free ones.
thread: research/threads/erdos-2adic-structure.md (to be opened)
next: tool_builder/theorem_prover writes the one-line proof — 2^n = 0 mod 2 and mod 2^k for k <= n,
  and 3^a = 1 mod 2 so (i) follows from (ii) at k = 1 — then records it as a `checked` claim block
  and hand-verifies n = 0, 2, 8 (note n = 0 has A = {0}, |A| odd, consistent since n = 0 is not a
  counterexample). Cheap, and it is the constraint family the invariant encoding reuses.
```

```gap
id: G-invariant
lemma: There exists a statistic Phi defined on the orbit {2^n : n >= 0} (equivalently a function of
  n, computable by a finite transducer along the base-2 -> base-3 carry), and a set W of values, such
  that
    (a) Phi(n+1) is obtained from Phi(n) by one fixed finite-transducer step (the x2 carry rule),
        so Phi is an invariant of the x -> 2x dynamics rather than a lookup table on n;
    (b) Phi(0), Phi(2), Phi(8) all lie in W  (the three witnesses survive);
    (c) 2^n in S  ==>  Phi(n) in W,  where S = {3-adic integers with digits in {0,1}};
    (d) n > 8  ==>  Phi(n) not in W.
  Candidate Phi to test first: weighted ternary digit sums sum_i w_i a_i, and carry-count statistics
  on the x2 transducer; the constraint family (i),(ii) of G-cong is the first filter a candidate
  must pass.
status: open
discharged-by: none yet
thread: research/threads/erdos-symbolic-invariant.md (to be opened)
next: smt_solver encodes a parametric family of candidate invariants in Z3 over digit variables
  a_i in {0,1} together with the modular constraints 2^n = sum a_i 3^i (mod 3^k); the encoding must
  return SAT on n = 0, 2, 8 (falsification oracle, per GOAL.md) before any UNSAT on n > 8 is read as
  evidence; report the digit-length bound. In parallel, tool_builder implements the x2 base-3 carry
  transducer so that property (a) can be checked mechanically for each candidate — this transducer
  part is the only piece with a chance of being a theorem on its own, and theorem_prover should be
  handed it as a first-order statement.
```

## What closes this skeleton

`G-cong` is minutes of work and should be discharged immediately. `G-invariant` is the run's
actual deliverable (GOAL.md's "symbolic invariant ... preserved by `x -> 2x` and violated by
`S`"), so closing it *is* closing the conjecture; a refutation of a specific candidate Phi with
the model the solver returned is the fallback partial result and must be recorded as such, not
as progress toward a proof.
