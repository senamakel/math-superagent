# boundary-finite-collisions-g-nonfibonacci-pairs-are-bounded

```skeleton
detail: The irreducible open core of the singmaster-uniform-bound reduction. Needs a computable K(eps) such that every non-Fibonacci boundary collision C(x,k1)=C(y,k2)=a with both reps in B(eps) has max(k1,k2) <= K. First move: column-growth inequality — a = C(x,k1) >= 2^{k1} gives k1 <= log2(a), and boundary condition k2 < exp((log x)^{2/3+eps}) with x ~ (k1! a)^{1/k1} forces an inequality linking k1,k2 that should make |k2-k1| small, reducing to a finite effective search. Genus g(k1,k2) = ((k1-1)(k2-1)+1-gcd)/2 grows in |k2-k1| but Faltings alone is ineffective; the bound must come from the boundary inequalities. K<=8 slice already solved (SdW/Avanesov/BMSST).
status: open
title: G-nonfibonacci-pairs-are-bounded — prove non-Fibonacci boundary collision pairs are confined to a finite computable set
```
