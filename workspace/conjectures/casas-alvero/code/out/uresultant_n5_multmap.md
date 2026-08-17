# Lex-free u-resultant certificate: n=4 validated, n=5 past the lex wall

Task `uresultant-n5-multmap`, executed 2026. Capture: code/out/uresultant_n5_multmap.captured.txt.

## What was established (all exact, Singular 4.3.1 dp/std/reduce, rational arithmetic)

The CA traceless-slice ideal I = (R_1..R_{n-1}) ⊂ QQ[a2..a_n] (Hasse resultants, a1=0)
is 0-dimensional with multiplicity n^(n-2):
  n=4: 16 = 4^2;  n=5: 125 = 5^3;  n=6: 1296 = 6^4 (established earlier, extend_n6).

The lex eliminant (u-resultant) closes at n=4 (pure u^8, nilpotency index of u)
but does NOT close at n=5 in 180s — recorded boundary uresultant_n5_boundary.

A LEX-FREE certificate works past that wall. Since the quotient is 0-dim and
localised at 0:

  V(I) = {0}  (= CA on the traceless slice)
      <=>  every coordinate a_j is nilpotent in the quotient (Nullstellensatz)

Two exact, lex-free routes, both certifying V(I)={0}:

(A) MULTIPLICATION-MAP CHAR POLY at n=4 (validation): the standard monomial
    basis of QQ[a2,a3,a4]/I has size 16; multiplication by u=a2 gives a 16x16
    matrix whose characteristic polynomial is the pure power t^16 = 4^2.
    This agrees with the lex eliminant u^8 (nilpotency index) — the run's
    index-vs-length distinction: char poly degree = length 16, nilpotency
    index = 8.

(B) COORDINATE NILPOTENCY at n=5 (the extension past the lex wall): exact
    reduce(a_j^k, G)==0 gives minimal k with a_j^k in I:
        n=4: a2^7, a3^6, a4^1
        n=5: a2^19, a3^13, a4^10, a5^1
    Together with 0-dim vdim=125, this certifies rad(I) = m_0, so
    V(I)={0} = CA at degree 5.

## Measured boundaries

- 125x125 multiplication-map determinant is infeasible symbolically (a NEW
  latent boundary); coordinate nilpotency delivers the same single-point
  certificate without it.
- lex eliminant remains infeasible at n=5 in 180s (prior capture).

## Status
ALL CHECKS PASSED. Oracle-guarded by lib.casas_alvero is_ca/is_pure_power
on (x-1)^n for n=4,5 over QQ. Stores recorded here because the memory backend
was down at write time; store with remember_memory/note_scratch on recovery.
