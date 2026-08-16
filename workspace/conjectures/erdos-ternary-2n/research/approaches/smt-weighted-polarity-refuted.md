# Refutation of weighted-Polarity candidate invariants (G-invariant skeleton)

```approach
id: smt-weighted-polarity
idea: Test candidate symbolic invariants (weighted digit sums with sign
  polarity) for the Erdős ternary conjecture against the SMT encoding
  over digit-{0,1} variables, as the first concrete G-invariant candidates.
mechanism: Z3/cvc5 QF_LIA over digit vars a_0..a_{L-1} in {0,1}, 2^n = Σ a_i 3^i,
  n pinned by a disjunction over [0,63]; check Polarity(n) = Σ(-1)^i a_i
  satisfies a candidate congruence that S survives and the orbit tail violates.
status: refuted
precedent: the weighted/signed-digit-search literature for ×2×3 (Zhang; no
  positive hit exists in the library on a signed statistic separating S from
  the orbit tail)
first-step: done -- both concrete candidates (C1: Polarity ≡ 0 mod 3, C2:
  Polarity ≡ 0 mod 2) refuted at witness n=0 (Polarity(0)=1), SAT model
  validated by independent arithmetic.
killed-by: both polarities evaluated mod 2 and mod 3 fail at n=0 (Polarity=1),
  so no fixed polaroid weight with these moduli can be the invariant; and,
  more structurally, within any finite digit bound the orbit tail is EMPTY of
  digit-free powers, so "UNSAT for n>8 within bound L" is vacuous and not a
  theorem (the oracle finds only {0,2,8} digit-free in [0,63]).
```

Approach: test candidate symbolic invariants for the Erdős ternary
conjecture following `research/backward/erdos-via-symbolic-invariant.md`
(gap G-invariant) with Z3/cvc5, digit-length bound L=40.

## Result: both concrete weighted candidates REFUTED at witness n=0

Encoding (QF_LIA, L=40 → n fits 2^n < 3^40, i.e. n ≤ 63):
digit vars `a_0..a_{L-1} ∈ {0,1}` (digit-free), `2^n = Σ a_i 3^i`, n an
integer variable resolved by a disjunction pinning the actual digits of
2^n0 for each n0 ∈ [0,63].

- **C1: Polarity(n) = Σ (-1)^i a_i ≡ 0 (mod 3)** → REFUTED. n=0 has
  digits [1], Polarity = 1, and 1 ≢ 0 (mod 3).
- **C2: Polarity(n) ≡ 0 (mod 2)** → REFUTED. n=0 has Polarity = 1 (odd).

Both solvers (z3 4.8.12, cvc5 1.0.3) return SAT and the model
`n=0, digits=[1,0,...]`, Polarity=1; validated by independent direct
arithmetic (`validate_invariant_models.py`). These are machine-refuted
candidates, recorded as dead ends.

## Gate PASSED (encoding not over-constrained)

The falsification oracle (GOAL.md): with n unrestricted, the encoding
returns SAT and finds each witness:
- n=0 → 1_3 = [1]
- n=2 → 11_3 = [1,1]
- n=8 → 100111_3 = [1,1,1,0,0,1]

Both z3 and cvc5 confirm. `validate_invariant_models.py` reconstructs 256
from the n=8 digits.

## The central structural finding: bounded "n>8 digit-free" UNSAT is vacuous

Exact oracle `digit_free` over [0,63] (the whole digit bound):
the only digit-free 2^n are **{0,2,8}** (the conjecture itself, for the
fitting range). Therefore "digit-free n > 8" within L=40 is UNSAT
*independently of any invariant* — the bounded UNSAT is vacuous and is
**NOT a theorem**. Any SMT route that reports "unsat for n>8 within bound
L" as evidence for a candidate is reporting the conjecture's own (fitting)
truth, not a separating property of the invariant.

Consistent-but-uninformative candidates within L:
- **c1(n) even for n ≥ 1** — true (proved, G-cong(i)); holds on n=2,8
  (n=0 gives c1=1). Not a new obstruction.
- **carry total under ×2** — equals 0 (zero carries) on all of {0,2,8},
  so it does not separate the witnesses from anything.

## Why this beats/limits the standard SMT reading

The naive reading — "UNSAT on n>8 proves the invariant separates the
orbit tail from S" — is invalid for this problem, because within any
finite digit bound the orbit tail is *empty* of digit-free powers. The
only non-vacuous SMT content is witness-level refutation of candidate
invariants (done: C1, C2) and, per the skeleton, a *transducer-dynamics*
invariant (property (a)) that can be checked as a first-order carry
statement — that piece is out of scope of this static-digit encoding and
is where a real theorem could still live.

## Status / evidence class
- C1, C2 refuted: **proved by model + validated** (solver SAT, model
  substituted back, independent arithmetic agrees). Evidence: machine
  model.
- Bounded n>8 UNSAT: **vacuous**, verified by exact oracle — not evidence
  for any invariant, must not be promoted to a theorem.
- Files: `code/out/z3_invariant.py` (.captured.txt), `code/out/cvc5_invariant.smt2`,
  `code/out/witness_invariants.py`, `code/out/validate_invariant_models.py`.
