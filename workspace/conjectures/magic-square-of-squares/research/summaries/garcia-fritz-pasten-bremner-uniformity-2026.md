# Garcia-Fritz–Pasten: A note on Bremner's conjecture and uniformity (2026)

Full text: `research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md`
(arXiv:2604.04850v2, 18 May 2026, 6 pages — now real PDF, not a wrapper).

## What it establishes

**Theorem 1.8 (Strong form of Bremner's conjecture, unconditional, proved).**
There is an absolute constant C > 1 such that if E is an elliptic curve over Q
with rank r, then **all arithmetic progressions on E have length ≤ C^(r+1)**.

This was proved by Garcia-Fritz–Pasten in their 2021 IMRN paper via Nevanlinna
theory + the uniform Mordell–Lang theorem of Gao–Ge–Kühne.  The 2026 note gives
an alternative short proof of the conditional uniformity consequence and extends
the method to finitely generated multiplicative groups.

**Theorem 1.2 (Conditional uniformity).** If the ranks of elliptic curves over Q
are uniformly bounded, then so are the lengths of arithmetic progressions on
elliptic curves over Q.

Proof uses the height-uniform Mordell theorem (Dimitrov–Gao–Habegger 2020) and
genus-2 curves with split Jacobian.  Key construction: from an AP of length M on
E, build a genus-2 hyperelliptic curve X whose Jacobian splits as E × E′;
DGH bounds #X(Q) by c^(1+rank J(Q)) ≤ c^(1+2R), giving a bound on M.

**Theorem 1.3 (Multiplicative groups).** If ranks are uniformly bounded, there
is κ > 1 such that for any finitely generated multiplicative subgroup Γ ⊂ Q^×
of rank ρ, #(x(E(Q)) ∩ Γ) ≤ κ·2^ρ.  (Corollary 1.4: same for geometric
progressions.)

**Conjecture 1.5** (height-uniform Mordell–Lang for E × G_m, not proved) would
give rank-dependent bounds for x-coordinates in multiplicative groups without
assuming uniform rank boundedness.

## Bearing on the 3×3 MSS

The Robertson reduction says an MSS exists iff there is e with an arithmetic
progression of x-coordinates on E_e: y² = x(x²−e⁴).  Theorem 1.8 bounds the
length of any such AP by C^(r+1).  If rank(E_e) can be bounded above for putative
MSS centres, this gives a contradiction for length ≥ 4 — or at least turns the
problem into bounding the rank of the Robertson curve.

**Gap**: C is not explicit (comes from Rémond's quantitative Mordell–Lang, not
computed in the paper). The bound is therefore ineffective for computation.

## Source

Garcia-Fritz, Natalia and Pasten, Hector. "A note on Bremner's conjecture and
uniformity." arXiv:2604.04850v2 [math.NT], 18 May 2026.
https://arxiv.org/abs/2604.04850