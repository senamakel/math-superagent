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

```claim
id: bremner-conjecture-proved
statement: There is an absolute constant C > 1 such that if E is an elliptic
  curve over Q with rank r, then all arithmetic progressions on E (sequences of
  rational points whose x-coordinates form a non-trivial AP) have length <= C^(r+1).
hypotheses: E/Q elliptic curve of rank r; AP = P1..PM in E(Q) with x-coords in AP;
  holds over any number field, not just Q
holds-here: yes (E is Robertson's curve y^2 = x(x^2 - c^2), which is an elliptic
  curve over Q; the AP length counted is exactly the three doubled-point
  x-coordinates c-u, c, c+u)
status: proved (Garcia-Fritz-Pasten 2021 IMRN via Nevanlinna + uniform
  Mordell-Lang of Gao-Ge-Kuhne; restated as Theorem 1.8 in the 2026 note)
bearing: an MSS gives an AP of length 3 of x-coordinates of points in 2E(Q) on
  E_e; Theorem 1.8 bounds AP length by C^(r+1), so an MSS forces C^(r+1) >= 3.
  The constant C is ineffective (Rémond's quantitative Mordell-Lang), so the
  theorem does NOT rule out MSS; it reframes non-existence as bounding
  rank(E_e). Combined with a rank bound R over the family, it would make the
  search finite (uniformity line).
anchor: research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md
  (Theorem 1.8, pp. 3 & 10)
answers: uniform-mordell-rank-bounds-ap (the conditional bounded-rank =>
  bounded-AP direction that feeds the uniform-height-bound-elliptic-ap thread)
```

```claim
id: uniform-rank-ap-bounded
statement: If the ranks of elliptic curves over Q are uniformly bounded, then so
  are the lengths of arithmetic progressions on elliptic curves over Q.
hypotheses: uniform rank bound R for all E/Q; AP of length M >= 4 on E
holds-here: yes (as a conditional uniformity consequence; the rank-bound premise
  is a major open problem, so the theorem gives a conditional, not an actual,
  bound here)
status: proved (short proof via the height-uniform Mordell theorem of
  Dimitrov-Gao-Habegger 2020 and genus-2 curves with split Jacobian; Theorem 1.2)
bearing: the adopted uniform-height-bound-elliptic-ap approach: if ranks over the
  family E_e are bounded, AP length is bounded, turning the 3x3 MSS into a
  finite (height-bounded) search. Ineffective in practice because the rank bound
  R is unknown and c(2,1) from DGH is not computed.
anchor: research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md
  (Theorem 1.2 and its proof, Section 3)
```

## Does this source help?

**Yes, as the linchpin of the adopted uniformity line.** It proves Bremner's 1998
rank conjecture (the exact statement this run's `uniformity-bremner-ap-bound`
thread depends on) and supplies the uniform-AP-length consequence. It confirms,
does not contradict, the Robertson reduction: the theorem's AP-length bound applies
to the three doubled x-coordinates only as a lower-bound constraint (C^(r+1) >= 3),
never as a ruling-out. The gap (ineffective C, unknown family rank bound) is
exactly the gap this run has already flagged in CONTEXT.md and APPROACHES.md.

## Source

Garcia-Fritz, Natalia and Pasten, Hector. "A note on Bremner's conjecture and
uniformity." arXiv:2604.04850v2 [math.NT], 18 May 2026.
https://arxiv.org/abs/2604.04850