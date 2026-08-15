# Fixed-modulus hunt for the Case-B residual class: no fixed M closes it

Program: `code/caseB/residual_modulus_hunt.py`
Output: `code/out/residual_modulus_hunt.captured.txt` (EXIT 0)

## Setting

Case B of Catalan, `x^p - y^2 = 1` (p odd prime), reduces (machine-certified,
`caseB.note.md`) to `x = c^2+1`, `y = c·m`, `m^2 = T(c,p) =
Σ_{k=0}^{p-1}(c^2+1)^k`. The mod-8 classification (`prove_T_mod8_classification`)
already proves `T(c,p)` is a non-square mod 8 for every class **except**
`c even & p ≡ 1 (mod 8)`. That single residual class is currently closed only
by the classical Ljunggren theorem (asserted, not re-proved here).

## Question and structural answer

Does there exist a **fixed modulus M** such that `T(c,p)` is never a square
mod M over the residual class (c even ≥ 2, p odd prime ≡ 1 mod 8)? If so the
class closes elementarily, without Ljunggren.

**No — for EVERY M the construction below produces a square residue.**

Take `c = 2M` (even, ≥ 2). Then `c² ≡ 0 (mod M)`, so `c²+1 ≡ 1 (mod M)` and
every term `(c²+1)^k ≡ 1 (mod M)`. Hence

    T(2M, p) ≡ Σ_{k=0}^{p-1} 1 = p   (mod M).

By Dirichlet's theorem (gcd(1, lcm(8,M)) = 1) there are infinitely many
primes `p ≡ 1 (mod lcm(8,M))`; any such p is an odd prime with
`p ≡ 1 (mod 8)` and `p ≡ 1 (mod M)`, giving

    T(2M, p) ≡ 1 ≡ 1²   (mod M),

a square mod M. So every M has a pair (c even, p odd prime ≡ 1 mod 8) with T
a square mod M. **No fixed modulus closes the residual class.** This is not a
computational limitation; the obstruction is structural (c² ≡ 0 collapses the
whole geometric sum to p).

## Verification (per candidate M)

33 candidate moduli: the explicit list {3,5,7,11,13,16,17,32,9,25,49,15,21,33},
all small primes 3..47, and their squares up to 47².

- **Method A (uniform construction):** for each M, c = 2M and p = least prime
  ≡ 1 mod lcm(8,M); T_mod computed by **direct summation** (never the
  (x^p−1)/(x−1) division, so gcd(c²,M) > 1 is harmless). Every row reports
  T ≡ 1 mod M, a square. Unconditional (Dirichlet guarantees the prime).
- **Method B (independent enumeration):** for each M, enumerate even residues
  c = 0..M−1 and primes p ≡ 1 mod 8 below 1000; record whether any
  T_mod(c,p) is a square residue. **Agrees with method A on all 33 moduli.**
  (Two independent routes to the same verdict.)

## Sanity oracle (Ljunggren-consistency)

True integer squares of T(c,p) for c even in [2,400], p prime ≡ 1 mod 8 in
[17,300]: **0 squares** (oracle_primes = 17,41,73,89,97,113,137,193,233,241,257,281),
exactly as Ljunggren's theorem requires. Direct exact isqrt; no floats.

## Falsifier / over-elimination

This is an **impossibility** result: the fixed-modulus approach cannot close
the class, so it does not claim to. It does not touch the known solution
`(3,2,2,3)` (outside Case B's hypothesis, y-exponent 3). The negative
orthogonal (no fixed M obstructs) is consistent with the oracle: the actual
squares are zero in the checked box, but the modular residues on every M are
all attainable by the Dirichlet construction.

## Claim

```claim
id: caseB-no-fixed-modulus-closes-residual
statement: Over the Case-B residual class (c even >= 2, p an odd prime,
  p == 1 mod 8), T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k is a square mod M for
  every modulus M: take c = 2M and an odd prime p == 1 mod lcm(8,M)
  (exists by Dirichlet); then c^2 == 0 mod M so each (c^2+1)^k == 1 mod M,
  T(2M,p) == p == 1 mod M, the square 1^2.  Hence no fixed modulus M makes
  T a non-square mod M on the whole residual class, and the class cannot be
  closed by any single fixed-modulus elementary argument.
hypotheses: c even >= 2, p odd prime, p == 1 mod 8, exact integer arithmetic;
  existence of primes == 1 mod lcm(8,M) is Dirichlet's theorem (an external
  sourced claim, gcd(1, lcm(8,M)) = 1).  Per-candidate verified for 33 moduli
  by direct summation (method A) and by independent enumeration (method B),
  which agree.
holds-here: yes -- the known solution (3,2,2,3) lies outside Case B's
  hypothesis (y-exponent 3); the statement is a negative bound on a
  hypothetical second solution and is consistent with the oracle (0 true
  squares in the box c even<=400, p in [17,300], p==1 mod 8).
status: checked (construction proved unconditionally given Dirichlet; agreed
  by two independent per-candidate computations over 33 moduli).
bearing: rules out the fixed-modulus elementary route for closing the last
  Case-B class; the residual class closes only via Ljunggren (or a
  modulus-dependent / non-congruence argument).
anchor: code/out/residual_modulus_hunt.captured.txt
```
