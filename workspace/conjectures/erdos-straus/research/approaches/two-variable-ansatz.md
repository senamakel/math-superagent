```approach
idea: Bradford (x,d) two-variable reduction as polynomial-ansatz search space
mechanism: Bradford's reduction states that for prime p, a Type I/II solution exists iff there is x ∈ [⌈p/4⌉,⌈p/2⌉] and a divisor d of x² with d ≡ −px (mod 4x−p) (Type I) or d ≡ −x (mod 4x−p) (Type II). Rather than searching for triples (x,y,z), search for pairs (x(k), d(k)) of polynomials in k such that the congruence holds identically for n(k) = 840k+r. The condition d(k) | x(k)² and the congruence constraint together form a system of polynomial equations. The advantage over triple-ansatz search is dimension reduction: two unknowns instead of three, with the divisibility and congruence replacing the full identity equation. The Schinzel obstruction still applies if the resulting x,y,z end up polynomial, but the (x,d) representation may reveal families where the obstruction is circumvented — for instance, d(k) need not be polynomial even if x(k) is.
status: proposed
precedent: none yet
first-step: Formulate the Bradford congruence as a polynomial identity in k: d(k)·Q(k) = x(k)² for some quotient Q(k), with d(k) ≡ −n(k)·x(k) (mod 4x(k)−n(k)), and search low-degree x(k), d(k) via sympy.
killed-by:
```