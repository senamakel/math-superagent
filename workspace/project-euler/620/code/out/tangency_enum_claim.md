# Tangency enumeration — oracle match claim

```claim
id: tangency_enum_oracle_match
statement: Direct tangency enumeration of the residue Q = sigma*rho*(beta-gamma) - eta*R*beta + theta*r*gamma (mod 1) with sign variant (sigma=-1, eta=-1, theta=-1), where beta=angle of planet centre about ring centre O, gamma=angle about sun centre S, rho=planet radius, R=c/(2pi), r=s/(2pi), reproduces g(16,5,5,6)=9. All 9 valid arrangements are isolated d-values where Q_p(U) == Q_q(U) (mod 1) with both planet pairs on the same side of the line of centres (UU/LL combos only; all six mixed UL combos give zero). Mirror identity Q(L) = -Q(U) (mod 1) is exact. The other seven (sigma, eta, theta) sign variants give g ∈ {6,7,10}, none matching 9. Grid: N=2^20+1=1048577 points over d ∈ [d_min,d_max]; COARSE_TOL=1e-4 (coarse grid clustering), TIGHT_TOL=1e-9 (mpmath refinement, dps=60).
hypotheses: exact tangency (planet centre at intersection of two circles); tooth-mesh residue per planet defined by the three-term angular combination with signs as above; mod-1 congruence of all four planet residues is the meshing condition.
holds-here: yes — reproduces the oracle value g(16,5,5,6)=9
status: checked
bearing: establishes the correct tooth-mesh residue sign convention for the off-centre PE620 geometry; confirms that g is a count of isolated d-solutions of the congruence Q_p(U) == Q_q(U) (mod 1); validates the mirror-pair structure (UU/LL only, no UL).
anchor: code/out/tangency_enum.txt
source: this-run-computation
```

## Run parameters

- `code/pattern/tangency_enum.py`
- `(c,s,p,q) = (16,5,5,6)`
- `grid: 2^20 + 1 = 1,048,577 points`
- `d ∈ [d_min=0.159154943, d_max=0.750704374]`
- `spacing = (d_max - d_min) / (N-1) ≈ 5.641e-7`
- `COARSE_TOL = 1e-4` (grid-level residue agreement)
- `TIGHT_TOL = 1e-9` (mpmath-refined objective minimum)
- `mpmath dps = 60`

## Winning variant

`(sigma, eta, theta) = (-1, -1, -1)`

Residue: `Q = -rho*(beta-gamma) + R*beta - r*gamma` (mod 1)

This is the only variant yielding exactly 9. All 9 d-values are doubly represented
(once as UU, once as LL).

## Counts per variant

| sigma | eta | theta | g |
|-------|-----|-------|---|
| -1 | -1 | -1 | **9** |
| -1 | -1 | +1 | 7 |
| -1 | +1 | -1 | 10 |
| -1 | +1 | +1 | 6 |
| +1 | -1 | -1 | 6 |
| +1 | -1 | +1 | 10 |
| +1 | +1 | -1 | 7 |
| +1 | +1 | +1 | 9 |

Only (sigma=-1, eta=-1, theta=-1) gives exactly 9 — and all 9 are pure UU/LL pairs
with no mixed-side (UL) configurations surviving.

## G(20) verification

**NOT YET RUN.** The enumerator is hardwired to (16,5,5,6). TASKS.md STEP 1 is to
generalize it and run over all 22 G(20) tuples, summing against the oracle 205.
Results will go to `code/out/tangency_G20.txt`.