# Scholar: the uniform-h fold second moment E[S²] = n−2 is a theorem for all n, not a small-n verification

The note `research/notes/pattern_finder_second_moment_at_uniform.md` states the
iid-uniform benchmark `E[S²] = n−2` and marks it "verified by full enumeration
n=3..7". That is true but understated: the statement is provable for **every** n
in one line from facts already in the ledger. This note files that proof and
upgrades the benchmark's evidence class.

## Setup (all from the ledger)

- Rows of the fold: `M_d = {n−1−d+o : o ⊆ d}`, `d ∈ [2, n−1]`, `|M_d| = 2^popcount(d)`
  — all rows have even size ≥ 2 (capture `fold_second_moment_capture.txt`, verified n=8..128).
- Distance distribution: `A_0 = n−2` (diagonal), `A_1 = 0`; distinct rows have
  even symmetric-difference size ≥ 2. (Computed exactly, n=16..4096, same capture.)
- XOR moment (verified exact in the capture): for iid Bernoulli(p) bits,
  `E[ε_d ε_{d'}] = (1−2p)^{|M_d △ M_{d'}|}`.

## The theorem

**Claim.** For h uniform on F₂ⁿ (p = 1/2), `E[S(n)²] = n−2` exactly, for all n.

**Proof.** `S(n) = Σ_{d=2}^{n−1} ε_d`, so
`E[S²] = Σ_{d,d'} E[ε_d ε_{d'}] = Σ_{d,d'} 0^{|M_d △ M_{d'}|}`,
where `0^0 := 1` and `0^k = 0` for k ≥ 1. The diagonal terms (d = d′) have
`|M_d △ M_{d'}| = 0` and contribute 1 each — there are `n−2` of them. Every
off-diagonal pair has `|M_d △ M_{d'}| ≥ 2` (rows even-sized, distinct ⇒ distance
even and ≥ 2, i.e. A₁ = 0), so every off-diagonal term is `0^{≥2} = 0`. Hence
`E[S²] = n−2`. ∎

As a corollary `E[S] = 0` at p = 1/2 (each `|M_d| ≥ 2` gives `E[ε_d] = 0^{|M_d|} = 0`),
so `Var(S) = n−2` and `Var(ν₂/n) = (n−2)/(4n²) = 1/(4n)·(1−2/n)` — the ideal
Chebyshev rate, matching the proved rank fact `wt(Φ_n h) ~ Binomial(n−2, 1/2)`
(fold-rank-is-n-2-nullity-2-alternating) for uniform h.

## Why this matters

The primes' measured second moment `E[S(n)²]/(n−2) = 1.03@1000 → 1.002@30000`
(claim `primes-fold-second-moment-at-uniform`) is compared against this exact
benchmark. The benchmark being a theorem (not a small-n fit) is what makes the
measurement's message precise: **the primes sit at the uniform second-moment
level**, and the single open arithmetic step is proving `E[S(n)²] = O(n)` for
the real prime h (GOAL priority 2, strictly weaker than positive mod-4 switch
density). Combined with the settled geometry side (condition (C): `F_n(1−2p)=O(n)`,
`A_2 = O(n^{0.48})`), that bound yields density-1 SUPPLY by Markov/Chebyshev
(result tier 3).

## Claim block

```claim
id: uniform-second-moment-n-minus-2-exact
statement: >
  For h uniform on F₂ⁿ (iid Bernoulli(1/2)) and the floored submask fold
  S(n)=Σ_{d=2}^{n−1}(−1)^{T(n,d)}, E[S(n)²] = n−2 exactly for every n≥3, and
  E[S(n)] = 0; hence Var(S(n)) = n−2 and Var(ν₂/n) = (n−2)/(4n²).
hypotheses: h uniform on F₂ⁿ; rows M_d even-sized (|M_d|=2^popcount(d)≥2) and
  pairwise distinct with even distance ≥ 2 (A₁=0); XOR moment (1−2p)^{|M_d △ M_{d'}|}.
holds-here: yes — all hypotheses are verified facts of the fold row set
  (capture fold_second_moment_capture.txt; rank note fold-rank-is-n-2-nullity-2-alternating).
status: proved (one-line argument above; the n=3..7 full-enumeration check in
  pattern_finder_second_moment_at_uniform.md is consistent as a spot check)
bearing: upgrades the uniform benchmark E[S²]=n−2 from "verified n=3..7" to
  "theorem for all n"; it is the exact level the prime h's measured second
  moment (≈1.00–1.03 × (n−2)) is compared against, and it pins the ideal
  Chebyshev rate 1/(4n) for the density-1 route.
anchor: research/notes/scholar_uniform_second_moment_theorem.md
follows-from: fair-model-exact-binomial (wt(Φ_n h) exactly Binomial(n−2,1/2) for uniform h, via S = n−2−2ν₂), fold-rank-is-n-2-nullity-2-alternating (row facts)
answers: (none — the open request is E[S(n)²]=O(n) for the PRIME h, which this does not touch)
```

## Independent check (rule 11)

Two independent routes confirm the value:

1. The direct proof above (diagonal terms only, at p = 1/2).
2. The Krawtchouk diagonalization at z = 0: `E[S²] = F_n(0)` and
   `F_n(0) = 2^{−n} Σ_ω Ĉ_n(ω)²`; by Parseval on the cube,
   `Σ_ω Ĉ_n(ω)² = Σ_{d,d'} Σ_ω (−1)^{⟨ω, 1_{M_d} △ 1_{M_{d'}}⟩} = 2^n · #{(d,d') : M_d = M_{d'}} = 2^n (n−2)`
   (rows pairwise distinct), so `F_n(0) = n−2`. The n=3..7 full-enumeration
   values in `pattern_finder_second_moment_at_uniform.md` agree wherever
   computed.
