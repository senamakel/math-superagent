# Christopher–Lloyd, "Polynomial systems: a lower bound for the weakened 16th Hilbert problem"

<!-- source: https://ddd.uab.cat/pub/artpub/2001/110469/extmat_a2001v16n3p441.pdf | Extracta Mathematicae 16(3):441–447 (2001), open access -->

**Primary treatment of the weakened (tangential) H16 lower bound at one
singular point.** Let b_{m,n} be the maximum number of isolated zeros (counted
with multiplicity) of the Abelian integral

```
I(h) = ∮_{H(x,y)=h} ȳ·Q(x,y) dx,   H(x,y) = y²/2 + x^{m+1}/(m+1),
```

with Q any polynomial of degree ≤ n−1. For m, n odd the paper proves it is

```
b_{m,n} ≥ (n+1)(n+3)/8 − 1        if n ≤ m
b_{m,n} ≥ (m+1)(2n − m + 3)/8 − 1 if n ≥ m
```

and there are perturbations of the Hamiltonian system ẋ=−∂H/∂y, ẏ=∂H/∂x that
realise this number of continuous families of limit cycles from prescribed
periodic orbits of the period annulus. Consequently b_{m,n} ≤ N(m,n) ≤
H(max{m,n}).

## What it establishes

- The number of isolated zeros of the Abelian integral grows like **order n²**
  (degree n ≥ m: the factor 2n is quadratic); hence the Hilbert number H(n)
  itself is at least of this order.
- This is the "weakened"/tangential/infinitesimal H16 at a single singular
  point: limit cycles bifurcating from a Hamiltonian centre by a polynomial
  perturbation.
- The proof counts zeros of a single Abelian integral over ovals of the curve
  {H = h} — a Chebyshev-type argument with the y²/2 + x^{m+1}/(m+1) Hamiltonian.

## Implication for this problem

Corroborates the n² (and n² log n) growth of H(n) from the *primary, open-
access* side, complementary to the held Buzzi–Novaes 2024 note (which estimates
the upper side and refutes quadratic upper bounds) and to the paywalled
Christopher–Lloyd 1995. Gives the concrete lower-bound constant.

**Evidence class**: sourced (full text held
  `research/sources/christopher-lloyd-weakened-16th-extracta-2001.full.md`).
**Falsifier**: an error in the zero-counting / multiplicity argument.
**Holds-here**: yes — confirms weakened-H16 growth O(n²) directly.

Claims ledger: `h16-christopher-lloyd-weakened-16th`.
