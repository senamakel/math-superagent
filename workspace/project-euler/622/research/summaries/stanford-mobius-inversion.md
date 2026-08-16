# Stanford — Möbius Inversion

Source: https://crypto.stanford.edu/pbc/notes/numbertheory/mobius.html · full text: [[stanford-mobius-inversion.full]]

## What it establishes

A clean, citable statement of the **Möbius inversion theorem** (the rung the
sequence-structure note uses without an anchor).

**Theorem.** For arithmetic functions F, f:
```
   F(n) = sum_{d|n} f(d)  for all n >= 1
        iff
   f(n) = sum_{d|n} mu(n/d) F(d)  for all n >= 1
```
Equivalently `f(n) = sum_{d|n} mu(d) F(n/d)` (change of variable). f is
multiplicative iff F is multiplicative.

**The Möbius function.** The unique solution to
`sum_{d|m} mu(d) = 1 if m=1 else 0`:
- mu(1) = 1
- mu(n) = 0 if p^2 | n for some prime p
- mu(n) = (-1)^r if n = p_1...p_r for distinct primes p_i

The proof (switching the double sum) is given in full.

## Consequences for this problem

This is the missing anchor for the **Möbius-inversion route** (C(k), S(k) in
`research/notes/pe622-sequence-structure.md`, and the proposed approach
`research/approaches/mobius-inversion-exponent-lattice.md`): given the
order-divisibility bijection (ord_m(2) | d  iff  m | 2^d - 1, Conrad Thm 2.1),
the "exact order k" count and sum are obtained by Möbius inversion over the
divisors of k, exactly in the form this theorem states. It is the Cited-axiom
source for the Lean rung that inverts over d | 60.

## Does not settle

- The numerical answer.
- The specific application (the bijection that makes F = (tau/sigma of
  2^d - 1)) — that comes from Conrad Thm 2.1, already in the library.
- The finite-divisor-lattice version (Rota's poset Möbius inversion), which is
  the generalisation Mathlib's `Nat.sum_mul_moebius` realises.

## Status

A standard textbook premise, cleanly stated with proof. Hypotheses: f, F
arithmetic functions over N; the inversion is identical in any abelian group.
No hypotheses beyond being over the positive integers ordered by divisibility.
