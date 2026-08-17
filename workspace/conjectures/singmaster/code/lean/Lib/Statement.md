# Statement.lean — Lean statement of Singmaster's conjecture

File: `code/lean/Lib/Statement.lean`

## Verdict (lean_check)

```
compiled: true
outcome: failed
sorry warnings:
  Statement.lean:38:8: warning: declaration uses `sorry`
#print axioms:
  'singmaster_conjecture' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
checked:
  theorem singmaster_conjecture : ∃ B : ℕ, ∀ a : ℕ, 1 < a → N a ≤ B
```

The theorem **elaborates** (compiles). The only non-standard axiom is
`sorryAx`, from the intentionally-placed `:= by sorry` — this is the
deliverable: a statement whose type carries every hypothesis, not a proof.
The other axioms (`propext`, `Classical.choice`, `Quot.sound`) are Mathlib's
standard kernel axioms. There is no `native_decide` and no cited `axiom`.

`outcome: failed` is expected and correct: `lean_check` refuses to mark a
file with a remaining `sorry` as `formalised`. That is precisely the intended
state for a conjecture statement.

## What the statement means

```lean
def occurrences (a : ℕ) : Set (ℕ × ℕ) :=
  { p | p.2 ≤ p.1 ∧ Nat.choose p.1 p.2 = a }

noncomputable def N (a : ℕ) : ℕ := (occurrences a).ncard

theorem singmaster_conjecture : ∃ B : ℕ, ∀ a : ℕ, 1 < a → N a ≤ B := by sorry
```

- `Nat.choose n k` is Mathlib's binomial coefficient (the `n`-th row,
  `k`-th column).
- `occurrences a` is the set of all pairs `(n,k)` with `0 ≤ k ≤ n` (enforced
  by `k ≤ n`, since `n, k : ℕ` are nonneg automatically) and `C(n,k) = a`.
  **Every** such pair is included: both mirrors `(n,k)` and `(n,n-k)`, and the
  trivial pair `C(a,1)=C(a,a-1)`, as distinct pairs. So
  `N(3003) = 8` under this convention.
- `Set.ncard` is Mathlib's natural-valued cardinality of a set, returning `0`
  for infinite sets. For `a > 1` the occurrence set is in fact finite
  (the `k ≤ log₂ a`/choose bounds; the k=2/3 results), so `N a` is genuine —
  but I do **not** assert finiteness here, only the conjecture that wraps it
  into a uniform bound.
- `∃ B : ℕ, ∀ a : ℕ, 1 < a → N a ≤ B` is exactly: there is an absolute
  constant `B` such that every `a > 1` appears at most `B` times. This is
  Singmaster's conjecture verbatim.

## Convention — stated on the bound

`N(a)` counts BOTH mirrors AND the trivial pair `C(a,1)=C(a,a-1)`. Under this
convention `N(3003)=8`; under the "one half-triangle rep" convention it would
be 4. The theorem's bound `B` is therefore in the both-mirrors-plus-trivial
scale, and any `B` is automatically ≥ 8 (since `N(3003)=8`). The `B ≥ 6`
constraint from the infinite Fibonacci family is likewise in this scale.

## Where it could differ from the problem as written

1. **Bound uses ≥ on the wrong hypothesis order — no.** The `1 < a` hypothesis
   matches the problem ("for every a > 1"). `a = 0` and `a = 1` (which appear
   infinitely many times) are excluded, exactly as the problem states.
2. **`N(a)` for infinite sets returns 0 by `ncard`'s definition.** If one
   wanted to be fully literal about "bounded above by B", one might worry the
   count value is technically 0 when the set is infinite — but that case cannot
   occur for `a > 1`, and in any case the conjecture-for-all-a is bounded
   *above* (a set with `ncard = 0` satisfies `0 ≤ B` trivially), so the
   statement is not weakened by it.
3. **The genus / Faltings / Siegel material is NOT formalised.** The problem's
   suggested attack (genus of `C(x,k1)=C(y,k2)` as a function of the pair,
   threshold where genus crosses 1, Baker/linear-forms height bounds) is a
   *route*, not part of the conjecture's statement. Mathlib has no Faltings or
   curve genus machinery under `Mathlib.AlgebraicGeometry`, and the effective
   height bound for a single pair would be its own large formalisation. The
   deliverable here — the conjecture itself, with every hypothesis — is
   complete; the curve/effectivity analysis is outside the statement's scope
   and is covered by the run's computational and prose work.
4. **`N` is noncomputable** (`Set.ncard`, `Classical`). This is fine for a
   statement; it does not affect the theorem's meaning.
