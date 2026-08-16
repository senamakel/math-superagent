# Derivative ladder / Δ-commutation: SUPPLY is invariant under F₂-differentiation

```approach
idea: Exploit the canonical fold-cell form T(n,d) = ((1+σ)^d h)[n−1−d] over F₂
(claim `linearisation-fold-weight`). The F₂ difference operator Δ = 1+σ COMMUTES
with the fold up to a diagonal shift in (n,d): for every k ≥ 0,
T_{Δ^k h}(n,d) = T(n+k, d+k) — exact, elementary, no spectral or measure theory.
Consequently the fold weight satisfies an exact one-cell ladder
ν₂(n+1) = wt(Φ_n Δh) + (h[n−2] ⊕ h[n]),
and by iteration, for any fixed k,
ν₂(n+k) = wt(Φ_n Δ^k h) + #{ d ∈ [2, k+1] : T(n+k, d) = 1 }.
So SUPPLY is INVARIANT under replacing the input h by its k-th F₂-derivative
Δ^k h (up to k bounded local cells). The switch indicator h satisfies
Δh[j] = [q_j ≢ q_{j+2} mod 4]: the ladder rewrites SUPPLY as a statement about the
fold-weight of the mod-4 two-point correlation at prime-index distance 2, not the
adjacent switch itself.
mechanism: (1+σ)^a (1+σ)^b = (1+σ)^{a+b} over F₂ (Frobenius), so a derivative
applied to the input is absorbed as a shift of the depth index: no conjecture,
the transfer is an identity. This is a change of representation (input string →
its F₂-differences) with a transfer that is exact, unlike the spectral-gap/energy
transfers of the three grounded candidates which have no mechanism coupling them
to wt(Φ_n h) for a fixed input. It prices GOAL priority 2 precisely: the weakest
input that suffices must be invariant under h → Δ^k h, and for k=1 the object is
the distance-2 two-point correlation [q_j ≢ q_{j+2} mod 4], the same parity-barrier
family as switch density (index-domain quadratic-character 2-point correlation).
status: grounded (identities machine-verified; arithmetic input = the distance-2 parity barrier, open — see claim derivative-ladder-identities-survive, anchor code/out/refuter_derivative_ladder_check.md)
precedent: (identity is derived, not sourced; the constituents are sourced)
- Canonical fold-cell form and linearisation: claim `linearisation-fold-weight`
  (ν₂(n) = wt(Φ_n h), T(n,d) = ⊕_{o⊆d} h[n−1−d+o]) — problem.md fact 1, imported
  as proved.
- Lucas submask fact (C(d,o) ≡ 1 mod 2 ⟺ o⊆d): problem.md fact 2, and
  `downset-row-intersection-meet-formula`; makes (1+σ)^d h[n−1−d] = ⊕_{o⊆d} h[n−1−d+o].
- Frobenius (1+σ)^{2^m} = 1+σ^{2^m} over F₂: the standard Frobenius endomorphism,
  already named in the refuted `dyadic-renormalization-selfsimilar` record as a real
  identity (its failure there was the lack of a fixed point, not this identity).
- h is the mod-4 switch indicator, switch density 0.5968 measured: claim
  `density-model-rising-mean-is-generic` (ones(h[0..3999]) = 2387).
- Adjacent-switch / two-point correlation is the parity barrier: claims
  `abgs-p1-wide-open`, `matomaki-radziwill-index-autocorrelation` (refuted), and the
  problem.md reduction note (Ash–Beltis–Gross–Sinnott 2011 §9).

first-step: (tool_builder) Machine-verify the ladder against the brute submask-XOR
oracle. (a) T_{Δ^k h}(n,d) = T(n+k,d+k) for k ∈ {1,2,4}, n ≤ 200, d ∈ [2,n−1];
(b) ν₂(n+1) = wt(Φ_n Δh) + (h[n−2]⊕h[n]) against the canonical ν₂ (guards
ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975); (c) Δh[j] = [q_j ≢ q_{j+2} mod 4] against the
literal residue string; (d) negative control — show the anti-Pascal relation
T(n+1,d)=T(n,d)⊕T(n+1,d+1) makes S(n+1)−S(n) NON-telescoping (no local boundary),
i.e. the boundary term printed is a full re-accumulation, not O(log n). Then hand
the priced question to research: is there an arithmetic input on Δ^k h strictly
weaker than positive mod-4 switch density?
falsifier: If the ladder identities fail against the oracle, the route is dead
(before that, no arithmetic is spent). If they pass but research confirms the
distance-2 two-point correlation [q_j ≢ q_{j+2} mod 4] has no unconditional positive
density — the same index-domain parity barrier as switch density — then the route's
honest product is the exact invariance/equivalence theorem (GOAL priority-5 flavour),
not a solution; state that and close, do not drift.
```

## The exact identities (derived by hand; machine verification is first-step)

Fix the F₂ conventions. `σ` is the left shift `(σx)[j] = x[j+1]`, `Δ = 1+σ` is the
F₂ difference. From claim `linearisation-fold-weight`, the fold cell at depth `d`,
position `n` is

```
T(n,d) = ((1+σ)^d h)[n−1−d] = ⊕_{o⊆d} h[n−1−d+o],
```

the second equality being Lucas. Then for every `k ≥ 0`:

```
T_{Δ^k h}(n,d) = ((1+σ)^d (1+σ)^k h)[n−1−d]
               = ((1+σ)^{d+k} h)[n−1−d]
               = T(n+k, d+k).                          (L1)
```

This is exact because `(1+σ)^a (1+σ)^b = (1+σ)^{a+b}` over F₂ (Frobenius), and the
index `n−1−d` is unchanged by the `(n+k, d+k)` substitution. **Hand-check (n=4,d=2):**
`T_{Δh}(4,2) = Δh[1]⊕Δh[3] = h[1]⊕h[2]⊕h[3]⊕h[4] = T(5,3)` (submasks of 2 are {0,2};
submasks of 3 are {0,1,2,3}). ✓

### Corollary 1 — the one-cell ladder

Summing (L1) with `k=1` over `d ∈ [2, n−1]`:

```
wt(Φ_n Δh) = #{ d ∈ [2,n−1] : T(n+1, d+1) = 1 }
           = #{ e ∈ [3,n] : T(n+1, e) = 1 },
ν₂(n+1)    = #{ e ∈ [2,n] : T(n+1, e) = 1 },
```

so

```
ν₂(n+1) = wt(Φ_n Δh) + [T(n+1,2)=1] = wt(Φ_n Δh) + (h[n−2] ⊕ h[n]),   (L2)
```

using `T(n+1,2) = ((1+σ)^2 h)[n−2] = (h ⊕ σ²h)[n−2] = h[n−2] ⊕ h[n]`.
**Hand-check (n=3):** `ν₂(4) = [T(4,2)] + [T(4,3)] = [h[1]⊕h[3]] + [h[0]⊕h[1]⊕h[2]⊕h[3]]`,
while `wt(Φ_3 Δh) = [h[0]⊕h[1]⊕h[2]⊕h[3]]`; difference is `[h[1]⊕h[3]] = [h[n−2]⊕h[n]]`. ✓

### Corollary 2 — the invariance

Iterating, for fixed `k`:

```
ν₂(n+k) = wt(Φ_n Δ^k h) + #{ d ∈ [2, k+1] : T(n+k, d) = 1 }.         (L3)
```

The correction is exactly `k` bounded cells (rows `d = 2..k+1` at level `n+k`), so
**SUPPLY(h) ⟺ SUPPLY(Δ^k h) for every fixed k** — the target is invariant under
F₂-differentiation of the input.

### Corollary 3 — the anti-Pascal recurrence (kills the Abel-boundary candidate)

Rearranging (L1) at `k=1` in terms of `h` (i.e. `T_{Δh}(n,d) = T(n+1,d+1)` with
`T_{Δh}(n,d) = T(n,d) ⊕ T(n+1,d)`):

```
T(n+1,d) = T(n,d) ⊕ T(n+1,d+1).                                     (L4)
```

This is *anti*-Pascal: it chains `d` **upward at the same level `n+1`**, so a depth-sum
`S(n) = Σ_d (−1)^{T(n,d)}` does not telescope into a boundary — `S(n+1) − S(n)` carries
the body over all `d`, not a local inhomogeneity. This is exactly why
`abel-boundary-recurrence` cannot land on an O(log n) boundary.

### Corollary 4 — the arithmetic content of Δh

`h[j] = [q_j ≢ q_{j+1} mod 4]` (the switch indicator). Then

```
Δh[j] = h[j] ⊕ h[j+1] = [q_j ≢ q_{j+2} mod 4],                     (L5)
```

because with only two residue classes, the two adjacent switches XOR to 1 iff the two
endpoints `q_j, q_{j+2}` differ. **Hand-check:** primes 3,5,7,11,13,17,19,23 have
residues 3,1,3,3,1,1,3,3; `h = 1,1,0,1,0,1,0,1`, `Δh = 0,1,1,1,1,1,1,·`, and
`[q_j ≢ q_{j+2}] = 0,1,1,1,1,1,1,·` — agreement. ✓ (Two-symbol fact: for a,b,c ∈ {1,3},
`[a≠b]⊕[b≠c] = [a≠c]` in all four cases.) For general `k = 2^m ≥ 2`, Frobenius gives
`Δ^{2^m} h[j] = h[j] ⊕ h[j+2^m] = [q_j≢q_{j+1}] ⊕ [q_{j+2^m}≢q_{j+2^m+1}]` — a
**four-point** object (parity of two adjacent switches at index separation `2^m`), not a
two-point one. So the clean two-point correlation appears exactly at `k=1`; the ladder's
content is that SUPPLY is invariant under all F₂-derivatives, so it cannot distinguish
adjacent-switch-SUPPLY from distance-2-switch-SUPPLY.

## Why this beats the three grounded candidates

1. **`substitution-incidence-perron`.** Already refuted on its own literal premise: the
   four substitution rules are FALSE for the actual fold spacetime (claim
   `substitution-incidence-rules-false`, hand-verified counterexamples; structurally,
   `(1+σ)^{2d}=(1+σ²)^d` reads even offsets while `(1+σ)^d` reads consecutive ones — the
   rules would need dyadic periodicity, closed door). Independently, even correct rules
   would describe the self-similar growth of the *unweighted* spacetime — a property of the
   fold **map**, independent of `h` — with no transfer theorem coupling a spectral gap to
   `wt(Φ_n h)` for a fixed input. The ladder, by contrast, is an identity about the image
   of the **fixed** input.
2. **`abel-boundary-recurrence`.** Its single load-bearing claim (the boundary is LOCAL)
   is refuted twice over: the literal neighbour relation `T(n,d)=T(n−1,d)⊕T(n−1,d−1)` is
   FALSE (claim `abel-boundary-recurrence-relation-false`, hand-verified counterexample
   h=(0,0,0,1), n=4,d=2); and the *correct* relation is anti-Pascal (L4), chaining `d`
   upward at the same level, so the depth-sum re-accumulates — no O(log n) boundary exists
   for the depth-sum to rest on. Derived, not conjectured.
3. **`f2-gram-disjointness-spectrum`.** `G = Φ_n Φ_n^T` is **independent of h** (a property
   of the row set), so its golden spectrum cannot bound `wt(Φ_n h)` for a fixed input;
   and weight ≠ energy over ℤ (`wt(Φh)` counts parity cells while `h^TΦ^TΦh = Σ_d (integer
   dot)²` — the all-ones string has `wt(Φh)=0` but energy ~n, closed door 1). The only
   h-coupling Gram is `Φ^TΦ` (Krawtchouk), already the adopted `fold-second-moment-krawtchouk`
   route. The golden spectrum is a relabeling of row self-similarity, not a weight bound.

## What is honestly new, and what is honestly stalled

**New and provable now:** (L1)–(L5) are exact, elementary F₂ identities. They give a
genuine invariance theorem — SUPPLY is invariant under `h → Δ^k h` — and they rewrite the
target as `wt(Φ_n Δh) ≥ c·n` with `Δh` the distance-2 two-point correlation of the
quadratic character. That is a real structural result (GOAL priority-5 flavour: an exact
equivalence between two formulations of the parity barrier), independent of any conjecture.

**Stalled at the parity barrier, and it must be said:** `Δh`'s density is the frequency of
`q_j ≢ q_{j+2} mod 4`, an *index-domain two-point correlation of the quadratic character* —
the same family that the claims `abgs-p1-wide-open` (L-functions cannot treat it) and
`matomaki-radziwill-index-autocorrelation` (value-domain methods do not reach index-domain
correlations) place behind the barrier. So the ladder does **not** by itself weaken the
input; it relocates SUPPLY onto the distance-2 correlation and proves the two are
equivalent up to O(1). The realistic deliverable is the invariance/equivalence theorem
plus the cleanest possible formulation of GOAL priority 2; if research confirms the
distance-2 correlation has no unconditional positive density, the route ends honestly at
that theorem and the problem is closed as "SUPPLY is equivalent to a second two-point
correlation in the parity-barrier family", not solved.

**Status of every claim here:** (L1)–(L5) are *derived by hand* (elementary F₂ bookkeeping
plus two hand-checked small cases), **not yet machine-verified** — that is first-step
(a)–(d). No number theory is spent before the oracle confirms them.
