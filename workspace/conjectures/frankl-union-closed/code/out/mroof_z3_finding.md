# M♮-certificate under-certification finding

**Result (verified-computational, n≤3; Z3 4.8.12 + cvc5 1.0.3 agree):**
The support-restricted M♮-concave weight certificate UNDER-CERTIFIES abundance
on the Boolean lattice. There is a union-closed family F={5,7} over [3]
(masks {x,z},{x,y,z}) in which element x has **density 1** (truly abundant),
yet NO weight w with (i) support F, (ii) w≥0, Σw=1, (iii) Σ_{x∈A}w(A)≥1/2,
(iv) M♮-concave exists.

**Proof (manual, matches both solvers' `unsat`):** w[5]=a, w[7]=b, a+b=1.
- X={x,z}, Y={y}, u=x: B1 and B2 both give w[5]+w[2] ≤ 0+0 ⇒ a≤0; with a≥0, a=0.
- X={x,y,z}, Y=∅, u=x: B1 gives w[7]+w[0] ≤ w[{y,z}]+w[{x}] = 0+0 ⇒ b=0.
- a=b=0 contradicts a+b=1. ∎

**Why the task's case (a) premise was wrong (the root cause):** the
whole-lattice constant w≡1/|F| IS M♮-concave (B1 is 2c≤2c everywhere), but
constraint (i) restricts w to be zero outside F, and the support-restricted
constant is NOT M♮-concave: at n=2, F={00,11}, the restricted constant 1/2 on
{00,11}, 0 elsewhere fails the triple (X={x,y}, Y=∅, u=x): B1 is 1/2+1/2 ≤ 0+0
(false), V=Y\X=∅ so B2 is unavailable. The constant-weight fact therefore does
NOT imply every abundant element is feasible.

**Consequences.**
1. The M♮-certificate class is a genuine restriction, not a vacuous one: it
   can fail to certify elements that are abundant in the strongest sense
   (density 1).
2. UC is preserved (the families here are UC and abundant at x), so this is
   **not** a counterexample to Frankl's conjecture; it is a negative result
   for the M♮-certificate approach as "every UC family has an
   M♮-certifiable abundant element". The memory note
   "the naive M♮-certificate is vacuous (uniform w certifies everything)" is
   now **refuted** for the support-restricted class: the class is small enough
   to under-certify.
3. The class also over-certifies (element y of family {0,1,3} is certifiable
   but density 1/3) and blocks non-abundant elements (z of {0,3,4}): it is
   neither a subset nor a superset of the truly-abundant set in general.

**Bearing.:** verified computationally for n≤3 by two independent solvers;
general statement for larger n is open (the obstruction is structural — pairs
where every branch leaves the support — and does not look size-specific, but
has not been proved for all n).

## Where this leads

- The over/under-certification *classification* over ALL n=3 UC families is
  now cheap (Z3 per family is milliseconds) and is the natural next step:
  it decides whether under-certification is rare or dominant, and whether any
  UC family has an abundant element that M♮ cannot certify *while every
  non-abundant one is blocked* — the soundness configuration the approach needs.
- The n=2 observation generalises: a two-level family {L, U} (L⊂U) shrinks
  under M♮; whether the obstruction is exactly "families with a 2-element
  chain whose every M♮-branch leaves F" is worth formalising.

## Files
- `code/out/mroof_z3.py` — the checker (exact, z3 Real/QF_LRA).
- `code/out/mroof_z3.captured.txt` — full validation capture (headers, all
  True/False per case, solver cross-check table).