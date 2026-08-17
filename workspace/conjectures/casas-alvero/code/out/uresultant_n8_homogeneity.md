# uresultant_n8_homogeneity.captured.txt — what was executed and what it settles

Program: `code/uresultant/verify_n8_homogeneity.py`
Capture: `code/out/uresultant_n8_homogeneity.captured.txt` (ALL CHECKS PASSED, exit 0)
Oracle: `lib.casas_alvero.is_ca` / `is_pure_power` on `(x−1)^8` over QQ (char 0), both PASS.
Base ring of the arithmetic: exact rational/integer evaluations of Hasse resultants
`R_i = Res_x(f, H_i(f))` on the traceless slice `a_1 = 0`, weights `w(a_j) = j`.
Worker count: 1 (single-threaded sympy; the question does not parallelise across
derivatives without re-deriving shared data). Wall clock: ~10 s.

## What it settles

Task `uresultant-n6-multmap-closedform` route (a) — the executable half:
pushing the verified Samuel-multiplicity closed form
`|QQ[a_2..a_n]/I_n| = n^(n−2)` (Cayley labelled trees) from n=6 past n=7 to **n=8**.

- The n=7 capture (existing) had already passed the exact route and hit the
  Singular vdim wall at 3000 s: `code/out/uresultant_n7.captured.txt`.
- This run closes **n=8 on the exact route**: the ordinary derivative of the
  resultants would need full expansion of `Res_x(f, H_i f)` over 7 variables,
  measured infeasible (probe killed at 560 s before the first resultant
  finished). Instead, resultant weighted-HOMOGENEITY reduces each `R_i` to one
  exact nonzero integer evaluation plus the t^j-scaling identity at t=3.

## The result, stated exactly

For each `(n,i)`, n = 4..8, i = 1..n−1, with
`c = (a_2,a_3,a_4,a_5,a_6,a_7,a_8) = (2,3,5,7,11,13,17)`:

- `Res_x(f, H_i f)(c) ∈ Z` and is nonzero (printed exactly, huge integers);
- `Res_x(f, H_i f)(t^j c_j) = t^{n(n−i)} · Res_x(f, H_i f)(c)` exactly (t = 3, checked by exact integer division).

By Sylvester-determinant weighted homogeneity of the resultant
(`Res(P,Q)` weighted degree = deg P · (weighted degree of Q)), each monomial of
`R_i` has weighted degree exactly `n(n−i)`, so those two exact checks certify
`ord_0(R_i) = n(n−i)` with nonzero leading coefficient — no expansion needed.

Consequence (Samuel/Valabrega–Valla where `I = (R_1,…,R_{n−1})` is m₀-primary,
i.e. in degrees where CA holds):

| n | ords `n(n−i)` | prod ords / prod(2..n) | n^(n−2) |
|---|---|---|---|
| 4 | 12,8,4 | 384/24 = 16 | 4² = 16 |
| 5 | 20,15,10,5 | 15000/120 = 125 | 5³ = 125 |
| 6 | 30,24,18,12,6 | 933120/720 = 1296 | 6⁴ = 1296 |
| 7 | 42,35,28,21,14,7 | 84707280/5040 = 16807 | 7⁵ = 16807 |
| **8** | **56,48,40,32,24,16,8** | **10569646080/40320 = 262144** | **8⁶ = 262144** |

The n=8 row is new for the run, verified computationally and exactly.

## What it does NOT settle

- The **Singular vdim** route at n=8 (the other, fully independent witness) is
  NOT closed: n=7 already hit the 3000 s wall (`uresultant_n7.captured.txt`),
  so n=8 is a fortiori infeasible by that method. The n=8 ord/Samuel statement
  therefore rests on the exact route alone — which is independent of vdim.
- It does NOT assert CA at degree 8 (CA-8 is long verified; the length formula
  is a certificate where CA holds, not a proof of CA). The closed form is
  conditional on `I` being m₀-primary: a certificate in verified degrees, not an
  unconditional theorem.
- It does not extend to n=9: the invariance of the statement under the
  evaluation point is exactly what the homogeneity proof (theorem, not
  computation) supplies, so extending the number alone adds no information.

## Feasibility boundary recorded (this run)

`code/uresultant/_probe_n8_cost.py` (full expansion of the 7 resultants at
n=8) was killed by timeout after 560 s with no output — first resultant i=1
not finished. Recorded, not retried; this run closes the same n=8 question
without expansion. The full-expansion wall sits between n=7 (35 s
construction, `uresultant_n7.captured.txt`) and n=8 (>560 s).