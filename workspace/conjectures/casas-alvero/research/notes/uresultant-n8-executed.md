# Executed: n=8 Samuel-multiplicity via resultant homogeneity (2026)

(the memory server was unhealthy when this run tried to store this; written to
the workspace so the record survives — store to Cognee once it recovers)

Program: `code/uresultant/verify_n8_homogeneity.py`
Capture: `code/out/uresultant_n8_homogeneity.captured.txt` (ALL CHECKS PASSED, exit 0)
Oracle guard: `lib.casas_alvero.is_ca` / `is_pure_power` on `(x-1)^8` over QQ — PASS.
Base: exact integer resultants (sympy), traceless slice a_1=0, weights w(a_j)=j, 1 worker.

## Result

`ord_0(R_i) = n(n-i)` exactly at n=8 (ords [56,48,40,32,24,16,8]),
Samuel length `prod ords / prod(2..8) = 10569646080/40320 = 262144 = 8^6`,
extending the verified chain n=4..7 (16, 125, 1296, 16807) = n^(n-2)
(Cayley labelled trees), in a degree where CA holds.

## Method (why no expansion was needed)

Full expansion of `Res_x(f, H_i f)` at n=8 is measured infeasible (probe
`_probe_n8_cost.py` killed at 560 s before i=1 finished; exit 124; recorded
boundary, not retried; the wall lies between n=7 (35 s) and n=8 (>560 s)).
Instead: the resultant is weighted-homogeneous of weighted degree
`deg f * wdeg(H_i f) = n(n-i)` (Sylvester determinant monomial weights), so
one exact nonzero integer evaluation + the t^j-scaling identity
`Res(t^j c_j) = t^(n(n-i)) Res(c_j)` at t=3 certify non-identically-zero and
exact order — no expansion. Values at c=(2,3,5,7,11,13,17), n=8:
[1892782008062725, 2952542661064815563, 70757781031890048337,
34405281384297265625, 406731066266709977, 103856336582912, 285212672],
all nonzero; t-scaling exact for all (n,i), n=4..8.

## Boundaries / what it does not settle

- Singular vdim route stops at n=7 (3000 s wall; `uresultant_n7.captured.txt`);
  n=8 vdim a fortiori infeasible, so n=8 rests on the exact route alone.
- The length formula is a certificate where CA holds, not a proof of CA.
- Does not extend to n=9: homogeneity is a theorem for all n, so extending the
  number adds no information; the open route is a different witness (vdim), or
  the theorem route (b): research/notes/weighted-order-theorem.md.