# Abel summation in the depth index: a boundary-only recurrence for S(n)

```approach
idea: Attack the excess S(n)=Σ_{d=2}^{n−1} (−1)^{T(n,d)} by discrete Abel
summation (summation by parts) over the DEPTH index d, using the exact first-order
recurrence of the fold cells coming from Pascal's rule C(d,i)=C(d−1,i)+C(d−1,i−1).
The sum over d telescopes, leaving an inhomogeneous (boundary) term that is a
*local* statistic of h at O(log n) positions — the one-point/two-point residue
statistics that PNT in AP mod 4 controls — while the bulk is a pure recurrence.
This is a change of *variable ordering* (sum in d, recur in n), not a claim about
polynomial degree (distinct from `newton-series-degree-dichotomy`) and not a
2×2 weight-block recursion (distinct from the refuted `pascal-cascade`).
mechanism: T(n,d)=⊕_{o⊆d} h[n−1−d+o] obeys, from Pascal's rule mod 2 applied to the
d index, an exact neighbour relation T(n,d)=T(n−1,d)⊕T(n−1,d−1) (up to the window
reversal), because the submask set of d splits by the lowest set bit. Summation by
parts: S(n)=Σ_d (−1)^{T(n,d)} is then a first-order linear difference equation in n,
S(n)=S(n−1) + (boundary terms at d=2 and d=n−1) + (telescoped body). The boundary
terms are sums of (−1)^{h[j]} over a single index or a pair — a *one-point* or
*adjacent-pair* statistic of the prime gap parity — and the body telescopes to
zero or to a shift. The load-bearing, checkable claim is that the inhomogeneity is
LOCAL: if true, SUPPLY reduces to bounding a short, explicit sum over the prime
residue string, which is in the territory of PNT in AP (one-point, provable) or
at worst the adjacent switch density (the known barrier), with the depth-average
doing the rest of the work.
status: proposed
first-step: Derive the exact neighbour relation T(n,d) in the folded (reversed)
indexing and machine-verify it against the brute submask-XOR oracle for all
(n,d), n ≤ 200, d ∈ [2,n−1]. Then Abel-sum S(n) in d to produce the explicit
boundary recurrence S(n)=F(S(n−1), boundary(n)), verify it against the oracle
(and against the known S(4000)=48, ν₂(4000)=1975), and print the boundary term's
explicit arithmetic content. Falsifier: if the boundary term is NOT local (if it
re-accumulates a full n-length sum), the route is dead before any number theory.
```

## Speculation, marked

The existence of the neighbour relation is established (Pascal's rule is an exact
integer identity). That the d-sum telescopes into a LOCAL boundary term — rather
than merely re-expressing S(n) — is speculation and is precisely what the
first-step checks mechanically. If the boundary term is the adjacent-switch sum
Σ_j (−1)^{[q_j≢q_{j+1} mod 4]}, that is the named parity barrier, but it enters
here with a *known sign* in the recurrence ν₂=((n−2)−S)/2, so an upper bound on S
is what is needed and the sign structure may still help.
