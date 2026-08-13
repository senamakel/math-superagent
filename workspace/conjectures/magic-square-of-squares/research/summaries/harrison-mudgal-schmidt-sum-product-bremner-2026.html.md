# Harrison, Mudgal & Schmidt, "Uniform sum-product phenomenon for algebraic groups and Bremner's conjecture", arXiv:2603.06483 (2026)

[[harrison-mudgal-schmidt-sum-product-bremner-2026]]
Full text: `research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.html.full.md`
URL: https://arxiv.org/abs/2603.06483
Authors: Joseph Harrison, Akshat Mudgal, Harry Schmidt (U. Warwick). 30 pp, v1 6 Mar 2026.

## What it establishes

**Theorem 1.1 — Bremner's conjecture with an *effectively computable* constant.**
There is an effectively computable constant C ≥ 1 (independent of the curve and
its coefficients a, b) such that: for E/Q in Weierstrass form y²=x³+ax+b of rank r,
with X = {x(P): P∈E(Q)}, Y = {y(P): P∈E(Q)}, and A any **arithmetic progression,
geometric progression, or a set of consecutive squares {u²,(u+d)²,…,(u+ld)²}**,
if A ⊆ X or A ⊆ Y then |A| ≤ C^(1+r).

So all three pattern classes in the *coordinates* of rational points of a
rank-r elliptic curve have their length bounded by C^(1+r), uniformly in the
curve, with C effective. The general form is Corollary 2.2, bounding proper
generalised arithmetic progressions P of rank k contained in 𝒞(Γ) for a
correspondence 𝒞 of degree d between G (≈ 𝔾_m or an elliptic curve) and a
1-dimensional group H: |P| ≤ D(d)^(1+r), independent of k.

**Method.** Combination of additive combinatorics (resolution of the weak
polynomial Freiman–Ruzsa conjecture over ℤ by Gowers–Green–Manners–Tao, 2025)
with Diophantine geometry (uniform Mordell–Lang, David–Philippon; S-unit bounds,
Evertse–Schlickewei–Schmidt). Theorems 2.1 and 4.2 give the corresponding
sum-product / expansion statements via a non-degeneracy ("coset") analysis.

## Why it matters for the magic-square-of-squares run

The run's adopted approach `uniform-height-bound-elliptic-ap` was blocked by one
thing: Garcia-Fritz–Pasten's constant in the AP-length bound C^(r+1) was
**ineffective** (came from Rémond / Uniform Mordell–Lang), so one could not in
principle compute C and check whether C^(r+1) < 3. Harrison–Mudgal–Schmidt
(Theorem 1.1) supplies a constant that is **effectively computable**.

The relevant ceiling remains: an MSS gives an AP of length ≥ 3, so a proof of
non-existence via this bound requires C^(1+r) < 3, i.e. rank r < log(3)/log(C) − 1.
Effectiveness means C is *in principle* computable and this inequality is *in
principle* decidable, but C is almost certainly enormous (built from
David–Philippon and PFR constants), so no small explicit value is available in
the paper. The approach is therefore advanced but not closed: the obstruction is
reduced from "ineffective" to "effective-but-astronomically-large, no explicit
bound given".

## Robertson-reduction connection (preliminary, be careful)

Theorem 1.1's third pattern class — x-coordinates equal to squares of a rational
AP, {u²,(u+d)²,(u+2d)²} ⊆ X — is structurally the face of the MSS condition. An
MSS centre-line gives A², e², B² all squares with A²+B²=2e², whose *square
roots* A,e,B satisfy A²+e²... (not an AP of the roots in general). The exact
map from the Robertson AP-of-x(2Q_i) to Theorem 1.1's classes is **not yet
established** and must be pinned before Theorem 1.1 is cited as applying to the
MSS. Do not over-claim: the effectiveness advance is solid, the precise
application to the four centre APs is open.

```claim
id: hms-2026-bremner-effective-constant
statement: There is an effectively computable C ≥ 1 such that for any E/Q of rank r,
  any arithmetic or geometric progression, or set of consecutive squares, contained in
  the x- or y-coordinates of E(Q), has length ≤ C^(1+r). (Theorem 1.1.)
hypotheses: E/Q Weierstrass form; pattern in X or Y coordinates
holds-here: yes (this makes the previously-ineffective GFP constant effective)
status: sourced (Harrison, Mudgal, Schmidt, arXiv:2603.06483, Theorem 1.1, read in full text)
bearing: reduces `uniform-height-bound-elliptic-ap`'s obstruction from an ineffective to an
  effective-but-uncomputed constant; exact mapping of the MSS four-centre-AP to the three
  pattern classes still open (not claimed here)
anchor: research/summaries/harrison-mudgal-schmidt-sum-product-bremner-2026.html.md
```
