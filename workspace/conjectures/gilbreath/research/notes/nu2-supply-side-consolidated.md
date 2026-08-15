# Route B supply side — what the library establishes about ν₂ ≥ c·n

The single remaining open content of the run's primary theoretical route
(Route B, Granville Theorem 5.5) is the **supply-side linear lower bound**

```
ν₂(q_{n−1}) ≥ c·n    for some c > 0   (measured c ≈ 0.5)
```

where ν₂(q_n) counts the 2s in the maximal {0,2} suffix of the right diagonal
through q_n. With Lemma 5.4 proved on the even domain
(`lemma54-re-derived-proof`), this bound alone would complete the ν₂ reduction
to Gilbreath's conjecture (`li2023-not-bottleneck`: any c > 0 suffices because
c·n > n^β for every β < 1, and the demand α ∈ {0.52, 0.525} is then immaterial).

This note consolidates what the six library sources that bear on ν₂ actually
establish — proving versus conjecturing — so the open statement is quoted with
the right evidence class and no source is over-cited.

## The atomic bit is TWO-POINT, and ν₂ = n/2 is the leading term

The natural transfer (this run's own bridge, measured): the {0,2} suffix cells
of the right diagonal have row-1 ancestors whose union is the fixed interval
[2, n−1]; the halved gap bit `h[j] = (gap_{j+1}//2) mod 2` is 1 iff
`gap_{j+1} ≡ 2 (mod 4)`; `w(n)` = its Hamming weight over j = 2..n−1; and
`w/n ≈ 0.60`, `nu2/w ∈ [0.689, 0.867]` (smallest 0.689), so `nu2 ≥ w/2`
holds on every sample and `nu2 ≥ c·n` for any `c < 1/2` is the honest demand
(`code/out/nu2_vs_gap_parity.captured.txt`, confirmed to N=30000 by
`nu2_dense_transfer.captured.txt` with nu2/w in [0.827, 0.864]).

The reason `ν₂ = n/2 + O(bias)` is the natural leading term is exactly
**Lemke Oliver & Soundararajan 2016** (`los-2016-consecutive-pair-mod4-bias`):
the atomic bit `bit_n = [p_{n+1} ≢ p_n (mod 4)] = [gap_n ≡ 2 (mod 4)]` is a
**two-point** consecutive-prime residue switch. At q=4 the four residue pairs
are each `li(x)/4 (1 ± (1/2log x)·log(2π log x/q))`, **minus for the repeating
(a,a) pairs, plus for the distinct (a,−a) pairs** — so two of the four
equiprobable pairs switch, giving n/2 to first order, and the bias pushes the
switch count *above* n/2 at finite x. **This is the sourced statement that
makes ν₂ = n/2 the leading term.** (Status: conjectural at the bias level —
Hardy–Littlewood; the main term n/2 rests on PNT-in-AP.)

## The honest deliverable is a FLUCTUATION bound, not a one-sided bias

**Rubinstein–Sarnak 1994** (`rubinstein-sarnak-fluctuation-not-bias`): under
GRH+GSH the mod-4 race has explicit Fourier transform; δ(P_{4;3,1}) = 0.9959
(bias toward primes ≡3 mod 4) — **but the sign oscillates** (Littlewood; first
1-leads point at 26861), so there is **no one-sided unconditional bias**.

**Lemke Oliver & Soundararajan 2017** (`rubinstein-sarnak-fluctuation-not-bias`):
Theorems 1.1–1.3 — the *secondary* (fluctuation) term in consecutive-prime
mod-q pattern biases has a **continuous, symmetric-about-0 limiting
distribution** as q→∞ (Φ_C(−x)+Φ_C(x)=1), tied to Dedekind-sum Fourier
transforms. Symmetric about 0 = the fluctuation is centred and oscillatory.

**Consequence:** an unconditional `ν₂ ≥ n^{0.525+δ}` claim is false in form —
the source-level honest statement is a *fluctuation bound* at
GRH/LI + Hardy–Littlewood/Dedekind-sum level. The open lower bound is real and
unproved; no held source establishes it.

## What does NOT supply the bound (and why)

- **Shiu 2000** (`shiu-2000-strings-of-congruent-primes`): unconditionally,
  arbitrarily long strings of consecutive primes in the SAME residue class mod
  q — i.e. infinitely many *non-switches* (equal residues). The strongest
  unconditional result in the mod-4 landscape, and it goes the **opposite**
  way from the supply bound (it exhibits the runs of 0s, not the density of
  switches). No quantitative switch lower bound.
- **Maynard 2015** (`maynard-2015-existence-not-frequency`): small-gap
  machinery gives *existence* of prime close-proximity configurations, never a
  *frequency* lower bound on mod-4 switches.
- **Lau 2024**: which consecutive-residue *patterns* occur infinitely often —
  ≥ mφ(q) patterns attained — but **existence**, not frequency; no constant on
  how often a given one occurs.
- **Granville & Lumley 2021** (`granville-lumley-short-intervals-heuristics`):
  **demand-side** short-interval heuristic (extremal counts M(x,y), m(x,y) of
  primes in length-y intervals over (x,2x]). Explicitly conjectural, and it
  says **nothing about the mod-4 distribution of consecutive primes** — so it
  neither closes nor bounds ν₂. Use it only as the documented short-interval /
  Cramér-model landscape companion; do not cite it for ν₂.
- **BCZ 2023** (`bcz-2023-left-edge-stabilization`): the structural F₂
  theorems (T²=id involution, Υ⁶=id, ray 0/1 proportions) are proved *for
  binary rows*; the **prime triangle's balanced 0/2 rays are Conjecture 2
  (unproved)**, numerically supported by Table 1 (|#0−#2| ≤ 431 of 78,496 per
  ray, primes < 10⁶). So BCZ *corroborates* ν₂ ~ n/2 but does not prove it.

## Cramér-model side (heuristic context, not the supply bound)

**Banks–Ford–Tao 2023** (`bft2023-cramer-model-canonical`): Cramér model
largest gap ~ log²x, Granville ~ ξ log²x, random-sieve model S. Fixes the
canonical probabilistic-prime-gap model underlying Chase 2024 / CHT 2026 / Tao;
records the two documented ways the plain Cramér model fails for real primes
(k-tuple residue bias, Maier short intervals). Heuristic support only for GC.

## Bearing — what this leaves open

The **supply bound ν₂ ≥ c·n is not supplied by any held theorem.** The leading
term n/2 is the (conditional) LOS two-point framework; the honest unconditional
statement is an oscillating fluctuation. To *prove* the bound one would need a
frequency lower bound on consecutive-prime mod-4 switches — which the sieve
machinery (Maynard, Lau) gives as existence only, Shiu's result goes the wrong
way, and the bias-distribution theory (RS, LOS-2017) gives the fluctuation law
not the bound. **This is the one sanctioned search target** (REQUESTS.md row 1)
and remains genuinely open. The measured margin is enormous (ν₂/n ∈ [0.42,
0.52] vs the needed n^0.525, factor 26 at n=3999), so the bound is the right
shape — it is simply unproved.

## Two-route verification status

ν₂/w and w/n are verified by two distinct captured programs
(`nu2_vs_gap_parity.captured.txt`, `nu2_dense_transfer.captured.txt`) which
compute the right-diagonal ν₂ and the halved-gap-bit Hamming weight w
independently and agree. `code/scholar/verify_supply_transfer_independent.py`
offers a third route but is not yet run (scholar has no exec tool in this run).

```claim
id: g-supply-transfer-measured
statement: For the prime right diagonal through q_n, let w(n) = #{2 <= j <= n-1 : gap_{j+1} == 2 (mod 4)} (the Hamming weight of the halved gap bits h[j]=(gap_{j+1}//2) mod 2, the row-1 ancestors of the {0,2}-tail cells whose union is the fixed interval [2,n-1]). Measured: w/n ~ 0.60; nu2/w in [0.689, 0.867] at sampled n in {50..3999} (min 0.689, so nu2 >= w/2 on every sample), and nu2/w in [0.827, 0.864] densely to N=30000. Hence nu2 >= c*n with c<1/2 is the honest Route B supply demand, and the transfer nu2 >= w/c for small c tracks the mod-4 gap-switch density.
hypotheses: primes below 5e4 (sampled to n=3999) and below 1e6 (dense to N=30000); {0,2} suffix of the right diagonal = maximal {0,2} suffix of delta_2..delta_{n-2}; exact integer arithmetic.
holds-here: yes
status: checked (two independent captured programs agree)
bearing: quantifies the G-supply (nu2 >= c*n) deficit of Route B: the bound is far from tight (factor 26 over n^0.525 at n=3999) and reduces to a frequency statement on consecutive-prime mod-4 switches; the leading term n/2 is the LOS-2016 two-point framework (conjectural bias), the unconditional honest statement is an oscillating fluctuation (RS-1994, LOS-2017). No held source proves the bound.
anchor: code/out/nu2_vs_gap_parity.captured.txt, code/out/nu2_dense_transfer.captured.txt, research/notes/nu2-supply-side-consolidated.md
```
