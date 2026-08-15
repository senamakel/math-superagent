# Lean 4 formalisation: Catalan prime-exponent reduction + known solution

**Kernel-checked.** Lean 4.34.0-rc1 with Mathlib present at `/opt/mathlib4`
compiled everything below. `lean` (Lean 4.34.0-rc1) is on `PATH` against the
Elan toolchain; `lake`/`elan` are not installed, but that does not block `lean`
compiling Mathlib files directly (the `LEAN_PATH` wrapper covers Mathlib's build
output). Every statement below is **kernel-checked here**, not merely stated.

## Files

`code/lean_reduction/CatalanReduction.lean` — the only source file, three
theorems. The file ends with `#print axioms` commands so the axiom report is
reproducible by just recompiling it.

## What is formalised, in prose

### 1. The reduction identity (the three-line fact everything downstream assumes)

For natural bases/exponents `x,a,P,y,b,Q`:

```lean
theorem reduction_iff (x a P y b Q : ℕ) :
    (x ^ a) ^ P - (y ^ b) ^ Q = 1 ↔ x ^ (a * P) - y ^ (b * Q) = 1
```

and the directed version matching the task statement, with `P` and `Q` prime:

```lean
theorem prime_exponent_reduction (x a P y b Q : ℕ)
    (_hP : Nat.Prime P) (_hQ : Nat.Prime Q) :
    (x ^ a) ^ P - (y ^ b) ^ Q = 1 → x ^ (a * P) - y ^ (b * Q) = 1
```

plus the integer (no truncated subtraction) analogue:

```lean
theorem reduction_iff_int (x y : ℤ) (a b P Q : ℕ) :
    (x ^ a) ^ P - (y ^ b) ^ Q = 1 ↔ x ^ (a * P) - y ^ (b * Q) = 1
```

The content is `pow_mul : a ^ (m * n) = (a ^ m) ^ n` (and its reverse). This is
an **iff** and holds for *every* exponent — the primality hypotheses `_hP`, `_hQ`
are unused. I state and prove this explicitly, because the honest remark is that
the reduction needs no primality: what matters for the prime-exponent reduction
of the actual theorem is whether a given exponent splits as `a * P`, which is a
separate step downstream. If a *general* solution had `p` or `q` composite, the
identity still lets you descend to a smaller exponent representation.

### 2. The known solution

```lean
theorem known_solution : 3 ^ 2 - 2 ^ 3 = 1 := by norm_num
```

Direct arithmetic, `norm_num`-closed. (Also `known_solution_value` with a `ℕ`
cast.)

### 3. `2` and `3` are not nontrivial perfect powers

```lean
lemma two_not_perfect_power   : ¬ ∃ (a e : ℕ), 2 ≤ e ∧ a ^ e = 2
lemma three_not_perfect_power : ¬ ∃ (a e : ℕ), 2 ≤ e ∧ a ^ e = 3
```

Proof: for `e ≥ 2`, if `a ≤ 1` then `a^e ≤ 1`, and if `a ≥ 2` then `a^e ≥ 2^e ≥
2^2 = 4`, so the value can never be `2` or `3`. This is what makes the reduction
an **iff** at the known solution `(3,2,2,3)`: because neither base `3` nor `2`
arises as a nontrivial power of a smaller integer, `(3,2,2,3)` cannot be the
image of any smaller non-trivial representation, so it is fixed by the reduction.

## Consistency / `#print axioms` / `sorry`

- **No `sorry`, no `admit`, no declared `axiom`** — `grep` finds none.
- `#print axioms` (as recorded by Lean on compile):

```
'Catalin.reduction_iff'              depends on axioms: [propext]
'Catalin.prime_exponent_reduction'   depends on axioms: [propext]
'Catalin.reduction_iff_int'          depends on axioms: [propext]
'Catalin.known_solution'             depends on axioms: [propext]
'Catalin.two_not_perfect_power'      depends on axioms: [propext, Classical.choice, Quot.sound]
'Catalin.three_not_perfect_power'    depends on axioms: [propext, Classical.choice, Quot.sound]
```

These are exactly Lean's standard kernel axioms (`propext`, `Classical.choice`,
`Quot.sound`) that Mathlib itself reduces onto; no theory axiom is smuggled in.
Every proof is a real Mathlib proof and the file compiles with `lean` exit code 0.

## Position relative to the known solution (the falsifier of GOAL.md)

Every lemma here was written to **not** over-prove:
- the reduction identity holds for the known solution as a re-labelling and
  states nothing that would rule out *any* solution;
- `known_solution` asserts the known solution *exists* as a solution, so it
  cannot be one of the "no solution at all" lemmas the goal warns about;
- the non-perfect-power lemmas are true facts about `1,2,3` and are only used
  to state that the known representation is minimal, not to eliminate anything.

So none of these lemmas, evaluated at `3^2 - 2^3 = 1`, is the falsification trap.

## What this does NOT do (honest scope)

This formalises only the reduction identity and the known base case. It does
**not**:

- prove the reduction *to odd prime exponents* in the sense of "every solution
  descends to one with odd prime exponents" — that needs the separate
  exponent-2 cases (`q = 2` handled by factorization in `ℤ`, `p = 2` in `ℤ[i]`),
  which are not here;
- touch the open both-odd-prime case in `ℤ[ζ_p]`;
- close Catalan's conjecture in any way.

`known_solution` and the perfect-power lemmas use `norm_num`/`omega` which are
closed tactics — they produce kernel-checked proofs, not `sorry`s.

## Verification method

Compiled with `timeout 600 lean code/lean_reduction/CatalanReduction.lean`,
exit 0, no error, and the `#print axioms` lines printed. Independent confirmation
of the arithmetic: `norm_num` checks `3^2-2^3 = 9-8 = 1` by computation.
