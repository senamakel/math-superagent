# Claim — Christoffel words characterised by strong factor-symmetry (Lanciault–Reutenauer)

Source: Yan Lanciault, Christophe Reutenauer, "A Symmetry Property of
Christoffel Words", EPTCS 403 (2024) 123–127, doi:10.4204/eptcs.403.26,
arXiv:2406.16408. Held in the library at
`research/sources/lanciault-reutenauer-symmetry-property-christoffel-eptcs.full.md`
(CC BY 4.0 full text; URL recorded in-file).

```claim
id: christoffel-strong-factor-symmetry
statement: For a word w over {a,b} with Parikh image (p,q) and delta_w(i,j) the
number of distinct factors of w with Parikh image (i,j), w is strongly
factor-symmetric if delta_w(i,j) = delta_w(p-i, q-j) for all i,j. Then: (Thm 3.1)
every Christoffel word is strongly factor-symmetric; (Thm 3.2) a primitive
Sturmian word whose support of delta_w is symmetric (in particular strongly
factor-symmetric) is a Christoffel word; (Thm 3.3) for w = u^k with u primitive
and k >= 2, w is strongly factor-symmetric iff u is a Christoffel word; (Thm 4.3)
such w is factor-symmetric iff u is a conjugate of a Christoffel word. The paper
also recalls: a Sturmian word is a Christoffel word iff it is Lyndon iff it is
unbordered.
hypotheses: w a finite word over a binary alphabet; Christoffel word in the
standard sense (lower/upper, primitive); Sturmian = balanced aperiodic.
holds-here: yes — the Christoffel/conjugacy characterisation applies to the
finite standard/Christoffel words whose rotations are the length-k factors of
the Fibonacci word (the run's factor structure).
status: sourced
follows-from: independent recent primary (EPTCS GASCom 2024); corroborates the
Christoffel-Lyndon-unbordered characterisation the library holds via
Borel-Reutenauer 2006.
bearing: Modern open-access companion on the Christoffel-class axis that the
run's refuted approach pe1006-christoffel-conjugacy-rotation-sum explored. The
Parikh-image symmetry is a structural property of the factor set, not a
decimal-value statement: Psi(k) sums squares of decimal values of length-k
factors, and no decimal-weight or moment statement appears in this paper. It is
background corroboration for the conjugacy/rotation structure of F_k, not an
engine for G4.
anchor: research/sources/lanciault-reutenauer-symmetry-property-christoffel-eptcs.full.md
(Thms 3.1-3.3, 4.1-4.3; lines 34-88)
```

## Corroboration

- Held Borel–Reutenauer 2006 "On Christoffel classes"
  (`research/sources/borel-reutenauer-christoffel-classes-2006.full.md`) is the
  Christoffel-class reference; this paper is a modern (2024) companion.
- The held Fici–Mantaci–Restivo–Romana–Rosone–Sciortino BWT survey gives the
  Christoffel = Lyndon conjugate of a standard word characterisation.

## Boundary

Strong factor-symmetry counts distinct factors by their Parikh image (number of
0s and 1s). It is NOT a statement about decimal values val(x) and does not give
a formula for Ψ(k). Use it only to corroborate the rotation/Christoffel
structure of the factor set.
