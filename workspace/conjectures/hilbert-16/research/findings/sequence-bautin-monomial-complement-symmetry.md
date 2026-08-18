# Bautin monomial-count complement: the quadratic formula and its symmetry refutation

## Direct computation (exact, from executed runs on disk)

Monomial counts of the Bautin focal-value obstructions L_d for the 5-parameter
chart family Q1=A u^2+C u v+D v^2, Q2=E u v+F v^2, rotation R(p)=-v p_u+u p_v,
V2=(u^2+v^2)/2, gauge c_{k,0}=0, over (A,C,D,E,F):

    d :   4    6    8   10   12   14   16
    a :   4   30   97  236  485  890  1505
  (4..890 from code/out/mono_counts.captured.txt; 1505 from code/out/.d16.tmp.txt)

With dim(h) = C(h+4,4) for h = d-2 (number of degree-h monomials in 5 vars),
the complement c(h) = dim(h) - 2*a_d:

    h :   2    4    6    8   10   12   14
    c :   7   10   16   23   31   40   50

## The conjecture (verify_quadratic_complement.py)

c(h) = (h^2 + 14 h + 8)/8 for even h >= 4  (so a_d = (dim(h) - (h^2+14h+8)/8)/2,
with a_4 = 4 exceptional). Holds exactly on d = 6,8,10,12,14,16 (h = 4..14);
FAILS at h=2 (formula gives c=5, actual 7) — the d=4 exceptional term.

Re-verified here: `python code/bautin/verify_quadratic_complement.py` → all
computed terms match on d>=6, residuals [2,0,0,0,0,0,0].

FALSIFIER = a_18, predicted 2392 (h=16). NOT previously computed (the d18
recurrence run in code/out/.d18.tmp.txt stalled at degree 17). Delegated to
tool_builder via spawn_agent (run id recorded by pattern_finder).

## Symmetry refutation (probe, exact, this pattern pass)

A natural "explanation" of a_d = (dim(h) - c(h))/2 is a monomial pairing:
L_d odd under a signed-permutation involution sigma on (A,C,D,E,F), forcing
support = all monomials minus the sigma-fixed ones, i.e. c(h) = |Fix_sigma(h)|
for one sigma for all h.  This is DEAD:

- All 26 permutation involutions on 5 letters enumerated; the attainable
  |Fix(h=4)| values are {6, 22, 70}, and c(4)=10 is not among them.
- All 312 signed-permutation involutions enumerated; signs do not affect
  monomial fixedness, so the same {6,22,70} at h=4. c(4)=10 NOT attainable.
- Best partial match over all 7 h was 1/7 (a transposition of D,E).

So NO signed permutation pairing yields the observed complement; a_d is not
"half the monomials minus one symmetry-paired set". Any derivation of the
quadratic formula would need a different mechanism (it is not a simple
symmetry-support identity).

## Exact status

A quadratic closed form on 6 of 7 computed terms, no surviving symmetry
explanation, falsifier term uncomputed at the time of writing. The pending
d18 computation settles a_18 =? 2392.
