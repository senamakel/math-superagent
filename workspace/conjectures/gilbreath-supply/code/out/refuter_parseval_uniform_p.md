# Refuter: "uniformly in p" in the Parseval second-moment claim is false

## What I attacked

The adopted (status: `grounded`) approach `research/approaches/meet-join-parseval-self-duality.md`
asserts, verbatim (mechanism step 5 / idea):

> the second moment under ANY product measure is E_p[S^2] = F_n(1−2p) = O(n),
> **uniformly in p**.

I attacked the **"uniformly in p ∈ (0,1)"** clause, on the suspicion that the
p → 0 edge kills it.

## The identity being claimed, and which part is right

For h iid Bernoulli(p), with ε_d = (−1)^{T(n,d)}, S(n) = Σ_{d=2}^{n−1} ε_d, the
XOR moment gives E[ε_d ε_{d'}] = (1−2p)^{|M_d △ M_{d'}|}, so

> E_p[S(n)²] = F_n(1−2p),  F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|}.

That identity and the Parseval form (F_n(z) = 2^{−n} Σ_ω (1−z)^{wt}(1+z)^{n−wt} S_ω²)
are **correct** — they reproduce the proved fair-model binomial law at z = 0
(`F_n(0) = n−2 = E[S²]` under uniform h). What is **wrong** is the uniformity
in p.

## The falsifier, by hand and by engine

As p → 0⁺, (1−2p) → 1, so every term (1−2p)^{dist} → 1 and

> F_n(1−2p) → (n−2)² = Θ(n²),

not O(n). The mechanism is the near-constant input h ≡ 0, which is in the fold's
kernel under the operative row range: every cell T(n,d) = 0, every ε_d = +1,
S(n) = n−2, E[S²] = (n−2)².

Concrete witness, n = 6 (rows d = 2,3,4,5), h = (0,0,0,0,0,0):
- d=2 (10): submasks {0,2} → T = h[3]⊕h[5] = 0
- d=3 (11): {0,1,2,3} → T = h[2]⊕h[3]⊕h[4]⊕h[5] = 0
- d=4 (100): {0,4} → T = h[1]⊕h[5] = 0
- d=5 (101): {0,1,4,5} → T = h[0]⊕h[1]⊕h[4]⊕h[5] = 0

All four ε_d = +1, S(6) = 4 = n−2, E[S²] = 16 = (n−2)². Verified by the engine:
`code/refute/second_moment_p0_witness.p` (XOR correctly encoded with
`~ (a <=> b)`), find_counterexample returned **proved**: the all-zero h forces
all ε_d = +1. (A first encoding that wrote XOR as `(a <=> b)` was my own bug;
the engine's model caught it, and the corrected file is the authoritative one.)

## The correct statement, and why this does NOT kill the route

The true statement is the **proved** one (`fold-distance-enumerator-On`): for
each **fixed** |z| < 1, F_n(z) = O(n), the constant depending on z. Hence
E_p[S²] = O(n) holds for p with |1−2p| ≤ z₀ < 1 — p bounded away from 0 and 1 —
and **not** uniformly over p ∈ (0,1). The constant blows up as z → 1 (p → 0).

The prime string sits at p ≈ 0.585, i.e. |1−2p| ≈ 0.17, an interior point where
the uniform-in-n bound does hold. So the route's actual working instance
(E[S²]=O(n) for the prime string) is **not** damaged by this correction. What
is false is only the over-strong "under ANY product measure / uniformly in p"
phrasing, which would wrongly predict no collapse under near-constant inputs.
Near-constant inputs do collapse (h ≡ 0 and all-ones are both in the kernel:
T(n,d)=0 for every d, S(n)=n−2, E[S²]=(n−2)²), consistent with the kernel fact
and with closed door 1. So the uniformity claim contradicts the kernel collapse
at both edges p=0 and p=1.

## The claim

```claim
id: parseval-second-moment-not-uniform-in-p
statement: The assertion in the grounded approach
  meet-join-parseval-self-duality that E_p[S(n)^2] = F_n(1-2p) = O(n)
  "uniformly in p in (0,1)" is FALSE. As p -> 0+, every term (1-2p)^{|M_d△M_{d'}|}
  -> 1, so F_n(1-2p) -> (n-2)^2 = Theta(n^2), not O(n). The mechanism is the
  near-constant (kernel) input: h == 0 (and h == all-ones) make every fold cell
  T(n,d) = 0, every eps_d = +1, S(n) = n-2, E[S^2] = (n-2)^2. The correct
  statement is the PROVED fold-distance-enumerator-On: for each FIXED |z|<1
  (i.e. p with |1-2p| <= z_0 < 1, bounded away from 0 and 1), F_n(z) = O(n) with
  constant depending on z.
hypotheses: h iid Bernoulli(p); fold cell T(n,d) = XOR_{o⊆d} h[n-1-d+o],
  d in [2,n-1]; eps_d = (-1)^{T(n,d)}; E_p[S^2] = F_n(1-2p); the XOR moment and
  Parseval identity are taken as correct (they reproduce the fair-model law at
  z=0).
holds-here: yes at the edges (p=0, p=1 give E[S^2]=(n-2)^2); the prime string at
  p ≈ 0.585 sits at an interior point where the uniform-in-n bound holds, so the
  route's real working instance is unaffected.
status: checked by hand (concrete n=6 witness) and confirmed by the engine
  (second_moment_p0_witness.p, corrected XOR encoding -> find_counterexample:
  proved).
bearing: an honest correction to an over-strong phrasing in the grounded
  approach; the "under ANY product measure / uniformly in p" claim would predict
  no fold collapse on near-constant inputs, contradicting the kernel collapse at
  p=0 and p=1 (closed door 1). The route's specific use (p ≈ 0.585 interior)
  survives.
anchor: code/refute/second_moment_p0_witness.p; this note.
```

## What I searched / what bounds the claim

- Hand check at n=6 (all four rows) plus the general argument (every term → 1 as
  p→0). The engine confirmed the n=6 all-zero witness is a model making every
  ε_d = +1 (find_counterexample: proved, after correcting my own XOR transcription
  bug). The n-dependence is exact integer arithmetic via the proven meet formula
  |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d∧d')+1}; no search or sampling.
- Honest limit: this refutes the *uniformity clause*, not the underlying
  Parseval/second-moment machinery, and not the route's use at p ≈ 0.585.
