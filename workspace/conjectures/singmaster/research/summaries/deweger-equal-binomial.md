# de Weger 1997 — Equal binomial coefficients: some elementary considerations

Source: B. M. M. de Weger, J. Number Theory 63 (1997) 373–386; primary PDF read.
[[deweger-equal-binomial]]

## Conjecture A (de Weger's main conjecture)

**(n,k)=(m,l) has no nontrivial solutions but those given above.**
"Those given above" = the six sporadic identities (120, 210, 1540, 7140, 11628,
24310), the triple 3003 (`C(78,2)=C(15,5)=C(14,6)`), and the infinite
Lind/Singmaster family `C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) =
C(F_{2i+2}F_{2i+3}−1, F_{2i}F_{2i+3}+1)` — together with the trivial relations.

**Consequence (stated in the paper)**: Conjecture A would imply `N(a) ≤ 8` for all
`a ≥ 2`, and `N(a) ≤ 6` for all `a ≠ 3003` (where `N=8`); the `N(a)=6` upper bound
is attained infinitely often. **This is precisely the route that would settle
Singmaster**, and confirms `3003` as the lone `N=8` value consistent with `B=8`.

## Theorem 1 — (k,l)=(3,4) completely solved

The **only** integer solutions to `C(n,3)=C(m,4)` are trivial:
`(n,m) ∈ {0,1,2}×{0,1,2,3}`, `(3,4),(3,−1),(7,7),(7,−4)`. So **no nontrivial
equality `C(n,3)=C(m,4)` exists**. Proof: `C(n,3)=C(m,4)` becomes, with `X=n−1`,
`Y=m(m−3)/2`, the Mordell curve `Y²+Y=X³−X`; Mordell's 1963 Theorem 2 lists all its
10 integral points. Note the paper stresses this connection was unnoticed for 30
years, and the proof is elementary (class group + unit group of a cubic field).

## Genus and the Faltings threshold (the key structural fact)

For fixed `(k,l)`, `C(n,k)=C(m,l)` with `k<l` is a plane curve. de Weger:
`(k,l)=(2,3)` and `(2,4)` are **elliptic curves** (Rank 2, rational points infinite
but fully understood); `(k,l)=(3,4)` has **genus 3** — so **Faltings applies** (only
finitely many rational points) — yet it is a **double cover of the elliptic curve
`Y²+Y=X³−X`**, which is why its integral points are still explicitly computable.
This is the concrete example that genus>1 alone does not make a bound effective:
the effective work comes from the elliptic (Mordell/Baker) descent, not from
Faltings.

## Theorem 3 — rational solutions with 2-power denominators

For `C(n,3)=C(m,4)`, the only rational solutions with denominators powers of 2 are
the integral ones (Theorem 1) plus `(n,m)=(5/4,1/2),(5/4,5/2)` (Conjecture B).
Counting 2-adic denominators: `X=X_1/2^{2k}, Y=Y_1/2^{3k}`, leading to `2V²=U³−2^{4k+2}U+2^{6k+1}`, factored in the cubic field `Q(θ)`, `θ³−4θ+2=0` (discriminant 148, trivial class group, units as stated). Proof is elementary; the `k>0` part exercises a Thue equation `Z³−4ZW²+2W³=1` restricted to `W` a power of 2.

## Bearing for this run

Primary source for both the **effective small-`(k,l)` list** and the **genus-3 /
elliptic-double-cover** structure that `research/approaches/genus-computation.md`
aims to reproduce (it is the `g(k1,k2)` deliverable's concrete anchor). It also
documents de Weger's Conjecture A, which is the cleanest known route to
`N(a)≤8`. The dedicated computer search (few hours, `C(n,k)≤10^30` or
`max[n,m]≤1000`) finds no new collisions — an early verification bound predating
BBW 2017.

```claim
id: deweger-genus3-curve
statement: de Weger 1997 (JNT 63): C(n,3)=C(m,4) has genus 3 (Faltings applies, only
  finitely many rational points) and is a double cover of the elliptic curve
  Y^2+Y=X^3-X (Mordell 1963); via Theorem 2 of Mordell its only integral solutions
  are trivial. Also (2,3),(2,4) are elliptic curves of rank 2 (Avane섭/Pinter
  Gelfond-Baker). Conjecture A (no nontrivial collisions beyond the known list +
  infinite family) would imply N(a)<=8 for all a>=2 and N(a)<=6 except a=3003.
hypotheses: fixed (k,l) pairs as listed.
holds-here: yes — the genus-3 elliptic-double-cover is the model for the genus
  deliverable; Conjecture A is the N<=8 route.
status: sourced (primary PDF read; Theorem 1/2/3 and Conjecture A quoted)
bearing: fixes the genus threshold example (g(k1,k2) for (3,4)=3 but still
  effectively solvable via elliptic descent); Conjecture A frames the target B<=8.
anchor: research/summaries/deweger-equal-binomial.md
```
