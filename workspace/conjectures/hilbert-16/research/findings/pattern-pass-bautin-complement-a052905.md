# Pattern pass: Bautin monomial-count complements are OEIS A052905 (exact)

Pattern-finder pass, 2026-08-18. Everything here is exact over the terms
supplied; nothing is extrapolated beyond them except where it is labelled a
conjecture with its falsifier term named.

## The sequences, and the tools' verdicts on them

5-parameter chart family (Q1 = A u^2 + C u v + D v^2, Q2 = E u v + F v^2,
rot(p) = -v p_u + u p_v, V2 = (u^2+v^2)/2, gauge c_{k,0} = 0, L_d the
even-degree radial obstruction):

    d :   4    6    8   10   12   14   16
    a :   4   30   97  236  485  890  1505      (monomial count of L_d)

6-parameter general quadratic focus (u' = -v + a1u^2+a2uv+a3v^2,
v' = u + b1u^2+b2uv+b3v^2, same rot/gauge):

    d :   4    6    8   10   12
    a6:   6   56  220  628 1481

Sanctioned tools, exact over supplied terms:

- `analyze_sequence` on a_d (7 terms) and a6_d (5 terms): differences never
  become constant; leading ratios decay slowly — NOT low-degree polynomials.
- `find_linear_recurrence` on a_d (max order 4), on a6_d (max order 3):
  NO constant-coefficient linear recurrence fits. (An earlier ad-hoc
  rational-coefficient order-3 fit on the 6-term a_d was already rejected as
  the documented false-positive trap.)
- OEIS lookups on a_d, a6_d, the denominators, and the v2/v3 valuations:
  all MISSES (recorded; nobody searches again).

## The identification that is exact and new

With dim(h) = C(h+4,4) (degree-h monomials in 5 variables), the complement

    c(h) = dim(h) - 2*a_{h+2}    for h = d-2 even:

    h :   2    4    6    8   10   12   14
    c :   7   10   16   23   31   40   50

The OEIS lookup of [10,16,23,31,40,50] (the h>=4 tail) matched
**A052905** = (j^2 + 7j + 2)/2 at j = h/2:

    c(h) = (h^2 + 14 h + 8)/8   for every even h in 4..14  (j = h/2).

Verified exactly by code/sequence_a052905_check.py: every computed term with
h >= 4 matches A052905(h/2) AND the closed form (h^2+14h+8)/8, in both
families. `analyze_sequence` on the tail [10,16,23,31,40,50] and on the
6-param tail [14,22,31,41,52] reports constant second difference 1 — exactly
quadratic, consistent with the A052905 closed form. `find_linear_recurrence`
reproduces A052905's order-3 recurrence a(n)=3a(n-1)-3a(n-2)+a(n-3) on the
5-param tail.

Exception, both families: h = 2 (d = 4) — c = 7 (5-param) / c = 9 (6-param),
where the formula gives 5 / 7. This is the documented d=4 exceptional term;
it is outside the A052905 tail by construction.

Cross-family (exact over all shared h): c6(h) - c5(h) = h for h = 4..10,
i.e. c6(h) = A052905(h/2) + h = (h^2 + 22 h + 8)/8. The 6-param tail is
exactly quadratic with the same constant second difference 1.

## What this means and what it does not

- The count sequences a_d / a6_d are dim(h)/2 minus a quadratic: a quadratic
  complement makes the sparsity pattern "almost exactly half the monomial
  space, minus a quadratically small symmetric deficit". This is a strong
  structural statement about L_d's support.
- It is a CONJECTURE for all h beyond the computed terms: no derivation is
  known. The symmetry-support pairing explanation (a_d = (dim - |Fix|)/2
  under a signed-permutation involution) was refuted exactly for both
  families (research/findings/sequence-bautin-monomial-complement-symmetry.md,
  research/findings/sequence-6param-bautin-audit.md).
- A052905 itself has no evident combinatorial meaning for Bautin obstructions;
  the identification is a cataloguing match, not a mechanism.

## Falsifiers (delegated to tool_builder; status at write time: running)

- 5-param: a_18 predicted 2392 (h=16, c=61). First falsifier.
- 6-param: a_14 predicted 3068 (h=12, c6=52). First falsifier.
- Denominator identity D5_d = D6_d, d=4..12 confirmed exact; D6_14 falsifier
  predicted 37456183296000.

## Denominator structure (exact over d=4..14, 5-param)

    D_d = 8, 192, 18432, 1105920, 22295347200, 37456183296000
    factorization: 2^3, 2^6·3, 2^11·3^2, 2^13·3^3·5, 2^19·3^5·5^2·7,
                   2^23·3^6·5^3·7^2
    valuations (v2, v3, v5, v7): (3,0,0,0), (6,1,0,0), (11,2,0,0),
                    (13,3,1,0), (19,5,2,1), (23,6,3,2)

v2 is irregular (3,6,11,13,19,23); v3 looks affine after a threshold
(0,1,2,3,5,6); v5 and v7 enter late. The rotation-operator-alone mechanism
for D_d was refuted exactly (pure 2-power lcm vs observed odd factors;
research/findings/sequence-6param-bautin-audit.md). No closed form for D_d
is conjectured here.

## Files

- code/sequence_a052905_check.py — the exact verification (run, exit 0).
- research/summaries/oeis_a052905.md — the OEIS entry (closed form).
- Delegated falsifier runs: agent-run-23 (5-param d=18), agent-run-24
  (6-param d=14).
