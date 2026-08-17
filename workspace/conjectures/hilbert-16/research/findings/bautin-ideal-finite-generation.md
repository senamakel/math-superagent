# Bautin focal-value ideal: finite-generation test through degree 14

Computed this run (exact sympy, lex Groebner over QQ; every verdict
cross-checked by the independent `G.contains` path; positive controls all
pass — see code/out/membership.captured.txt).

## The numeric facts (all exact)

Monomial counts of the focal obstructions L_d (d-homogeneous in the 5 params
A,C,D,E,F), from mono_counts → d=14, and membership re-run:

    d :    4    6    8    10   12   14
    mon:   4    30   97   236  485  890     (hdeg d-2)
    dim:  15    70  210  495  1001 1820     (monomials in degree d-2 of 5 vars)

Ideal-membership verdicts (exact lex Groebner over QQ):

    L8  in <L4,L6>      -> False   (third generator independent/needed)
    L6  in <L4>         -> False   (first two independent)
    L10 in <L4,L6,L8>   -> True
    L12 in <L4,L6,L8>   -> True
    L14 in <L4,L6,L8>   -> True

So the "Bautin trick" — the first three focal values generate the higher
degrees — holds through d = 14. (This is the ideal-membership statement that
Bautin's finite-generation theorem M(2)=3 relies on; the literature boundary
is degree 6; this run extends the verified membership to degree 14.)

## Cofactor-certificate sizes (new, from code/bautin/cofactor_counts.py)

Explicit identities L_d = q1*L4 + q2*L6 + q3*L8 verified by direct expansion,
q_i rational polynomials. Total monomials across (q1,q2,q3):

    d = 10 : q1,q2,q3 = (38,?),(... glb ...) ... total 146
    d = 12 : total 342
    d = 14 : total 682

## Structural assessment

The membership verdicts are a clean, exact structural fact: three focal values
generate all higher-degree focal values of the quadratic focus (through 14).
The monomial-count sequence (4,30,97,236,485,890) shows no clean closed form
(prior pass: OEIS no match, several candidate regularities refuted — see
research/findings/sequence-workspace-audit.md). The cofactor-size sequence
(146,342,682) has only 3 terms — too few to say anything exact; needs more.

## Falsifier

The generation claim L_d ∈ <L4,L6,L8> is attacked at d = 16 (next even
degree). If L16 ∈ <L4,L6,L8> fails, the 3-generator ideal claim is FALSE and
the pattern dies; the first term that would falsify the "all higher L_d are
generated" conjecture is d = 16.
