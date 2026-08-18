```claim
id: h16-2-statement-stated-in-lean
statement: H16.2 (uniform bound half) stated in Lean: for every degree n there exists N such that every planar polynomial vector field of degree at most n (P Q : MvPolynomial (Fin 2) ℝ with totalDegree ≤ n, map toMap) has a finite set of limit-cycle orbits with cardinality at most N. A limit cycle is a non-constant periodic integral curve isolated in the set of periodic orbits (IsLimitCycle, written by hand; Mathlib has no such notion).
evidence: asserted
status: asserted
formalisation: code/lean/Lib/Statement.lean
falsifier: A field of degree ≤ n with infinitely many limit cycles, or with more than N for the least such N.
```

Scope notes:

- `lean_check code/lean/Lib/Statement.lean` → `compiled: true`, `outcome:
  failed` with exactly one `sorry` warning at the deliberate `:= by sorry` in
  `h16_2`. `#print axioms` shows only `sorryAx` beyond the kernel's own three
  (`propext`, `Classical.choice`, `Quot.sound`). This is the intentional
  deliverable verdict: the *statement* is the deliverable, not a proof, so the
  claim is `asserted`, never `formalised`, until the sorry is filled.
- The statement is `∀ n : ℕ` rather than `∀ n ≥ 2`: strictly stronger, and
  consistent since H(0) = H(1) = 0.
- Only the **bound half** of H16.2 is stated. The second half — which
  configurations (mutual positions, nestings) of limit cycles occur — is not in
  Lean anywhere; stating it needs a notion of nesting/Jordan curve of periodic
  orbits that Mathlib does not package.
- The `Set.ncard`-of-an-infinite-set-is-0 vacuity hole is closed: the theorem
  states `(LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N`
  together.
- The isolation clause is the part most in danger of diverging from the
  intended notion: it says any non-constant periodic integral curve δ of the
  same field whose orbit lies in a neighbourhood of γ's orbit must have the
  same orbit as γ. Audit this before building anything on it.
