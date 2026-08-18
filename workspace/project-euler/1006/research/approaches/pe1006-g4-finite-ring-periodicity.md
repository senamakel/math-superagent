# G4 finite-ring periodicity investigation

```approach
slug: pe1006-g4-finite-ring-periodicity
idea: Factor M, use multiplicative orders of 10, and aggregate Psi via residue-class correlations of Sturmian factor columns.
status: refuted
killed-by: finite coefficient period does not bound the irrational-rotation/intercept boundary data; exact tests show the required correlation kernel remains k-dependent.
```

## Algebraic setup

For a length-k factor x, write its decimal value as
\[
 v(x)=\sum_{j=0}^{k-1}x_j10^{k-1-j}.
\]
For any modulus q coprime to 10, let L=ord_q(10). Then 10^{k-1-j} is L-periodic in j, so the value v(x) mod q is a linear combination of the L residue-class column sums. Consequently
\[
 \Psi(k)\equiv\sum_{x\in F_k}v(x)^2\pmod q
\]
expands into finitely many residue-class column correlations
\[
 C_{r,s}(k)=\sum_{x\in F_k}\sum_{i\equiv r(L),j\equiv s(L)}x_ix_j.
\]
This is an exact finite-ring representation, but it does not imply that the C_{r,s}(k) have a fixed-dimensional recurrence.

## Factorisation and orders

The exact modulus is
\[
 M=101001001=3\cdot7\cdot13\cdot37\cdot101.
\]
Thus CRT has five prime components (all exponent one). The relevant coefficient periods are ord_q(10):
\[
\operatorname{ord}_3(10)=1,\quad
\operatorname{ord}_7(10)=6,\quad
\operatorname{ord}_{13}(10)=6,\quad
\operatorname{ord}_{37}(10)=3,\quad
\operatorname{ord}_{101}(10)=4.
\]
The combined period is lcm(1,6,6,3,4)=12, equal to ord_M(10). (These values should be mechanically checked with the supplied factor/order script or SymPy; web search independently confirms the standard definition of multiplicative order, but the numerical table is computational evidence.)

## Why the proposed fixed state does not close

The Sturmian mechanical representation has k+1 intercept classes cut by the irrational orbit points {-ma}, with a=1/phi^2. Periodic decimal weights only identify column indices modulo 12. The correlation still asks how every orbit interval intersects its shifts by d, including endpoint/boundary terms. For general k, the pair correlation is not Toeplitz in the factor index: the identity depending only on lag is valid only at k=F_n-1. In general, the intersection count is a lattice-point count whose starting point depends on the factor/intercept index.

Therefore a putative state consisting only of the 12 residue columns (or the 5 CRT copies of those columns) loses the intercept phase. To be correct for all k, it must retain the ordered irrational-rotation cut data, whose number grows with k, or an equivalent Euclidean/Ostrowski summary. The latter is precisely the unresolved G4 joint-intercept problem; periodicity does not solve it.

This is a structural obstruction, not merely a failed implementation: the finite ring bounds the coefficient alphabet/period, but not the Sturmian partition complexity. A fixed-dimensional state would require a new theorem showing that all these phase-dependent lattice counts close under a finite list of recurrences; no such theorem is in the current library, and the existing general-k counterexamples rule out the naive Toeplitz collapse.

## Exact small-k tests and implementation advice

Keep the naive oracle only for small k (complexity exponential/factorial in the input bound; oracle bound k<=10). Compare it with the mechanical factor generator and with the periodic correlation expansion. Required checks:

* k=3: factors 001,010,100,101 and Psi(3)=20302 exactly.
* k=10: Psi(10) mod M = 10699667.
* For k=1..50, periodic expansion modulo each q and CRT must equal the direct mechanical sum.
* At k=1,2,4,7,12,20,33,... (k=F_n-1), test the cyclic/Toeplitz shortcut; do not apply it at generic k.
* Generic-k anchors already verified independently: Psi(10^4) mod M=34432237 and Psi(10^6) mod M=20938836. The earlier values 16242174 and 77578256 are invalid.
* Check the cheap residue invariant Psi(k) = 1+floor(k/phi^2) (mod 100), hence the target must be 52 mod 100.

Implementation: precompute powers p[r]=10^r mod each prime q for r<12; accumulate C[r][s] while streaming factors, then combine with the corresponding weights. For an actual large-k solver, do not store factors. Use the universal-Euclidean monoid for each needed floor-sum primitive, but add a joint intercept/phase component; CRT and period-12 coefficient compression can reduce constants only. The missing operation is an associative fixed-dimensional summary of all k+1 intercept classes. Until that is proved and independently checked at both 10^4 and 10^6, no value at 10^18 should be claimed.

## Sources

* Multiplicative-order definition and divisibility by Euler phi: https://mathworld.wolfram.com/MultiplicativeOrder.html
* Sturmian factor complexity and mechanical representation: library claims `governing-sturmian`, `mechanical-word-digit-rule`, and sources cited there.
* General-k failure of Toeplitz correlation: library claim `dir1-domain-autocorrelation` and approach record `pe1006-periodic-weight-crt-localisation.md`.
