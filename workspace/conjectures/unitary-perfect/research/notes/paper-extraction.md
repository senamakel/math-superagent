# arXiv:2605.20475 — Bounded-box reductions in the Subbarao–Warren problem (Maciejewski, May 2026)

Real digest of `[[maciejewski-bounded-box-subbarao-warren.full]]`. Stub replaced.
Rigorous results (R): Theorems 2, 7, 8–19, 21, Lemma 20, Propositions 4, 5, 28.
Conditional (C-A): Theorem 27, Theorem 30, Conjectures 6, 23, 24, 26, 29.

## 3-Higgs primes and H_even

`p` is **3-Higgs** (OEIS A057447) iff `p−1` divides the cube of the product of
smaller 3-Higgs primes; equivalently every prime factor `q` of `p−1` is 3-Higgs
and `v_q(p−1) ≤ 3`. The smallest omitted prime is `17` (`17−1=2^4`, v2=4>3), so
`𝒫₃` is downward-closed (Ford applies). Every prime divisor of a UPN is 3-Higgs.

```
H      = { m ≥ 1 : every prime factor of 2^m + 1 is 3-Higgs }
H_even = H ∩ 2Z
```
Conjecture 6 (the remaining branch, equivalent to the Subbarao–Warren
finiteness question): **H_even is finite.**

## Impostor kernels and the three-filter certificate

The full balance `(2^a+1)∏(p_i^{e_i}+1) = 2^{a+1}∏p_i^{e_i}`. Enumerating the
bounded box `ℬ = {p≤2000, e≤6, p^e≤10^9, |SCC|≤6}` yields, besides the two known
kernels `3²` (in 90) and `5⁴` (fifth UPN), five impostor kernels: `3²5³`,
`3⁴41`, `5²13²`, `5⁴157²313`, `5⁴29·157²313`. Theorem 2: for every impostor
kernel and every `a` in its seed congruence class with `1≤a≤10000`, one of three
filters closes it (Z Zsigmondy/Higgs exponent; N seed-divisor non-3-Higgs
witness, robust to partial factorization; O 2-adic budget overshoot by Lemma 1,
monotone in the seed). Split at max a=10000: 495 / 1614 / 10 / 0. Corollary 3:
inside ℬ the only source-SCC kernels available (a≤10000) are `3²` and `5⁴`.

## Rigorous structure of H_even

- **Prop 4 (structural):** `m=2k ∈ H_even`, `k` odd ⇒ (1) every prime of `k`
  is 3-Higgs; (2) `v_q(k) ≤ 3` (k "Higgs-cubefree"); (3) `2d ∈ H_even` for every
  odd divisor `d | k`. Proof: Zsigmondy gives a primitive divisor `r` of
  `2^{2k}+1` with `ord_r(2)=4k`, `r≡1 mod 4k`, `4k | r−1`.
- **Prop 5:** `H_even ⊆ {m ≡ 2 mod 4}` (Lucas refinement; any `q | F_k` has
  `v2(q−1)=k+2≥4` for k≥2, non-3-Higgs).
- **Thm 7 (prime-case reduction):** `H_even` finite **iff** the prime branch
  `{2p : p odd prime, 2p∈H_even}` is finite; `|H_even| ≤ 4^N`. All open
  primitive cases have `m=2p`; five composite candidates inherited via Prop 4.
- **Thm 8:** `H_even ∩ [2,1200] = {2,6,10,18,26,30,46,62,82,122}`.
- **Thms 9–19:** each interval is contained in a small explicit candidate set
  (2426,2602; 5; 5; 10; 27; 27; 48; 32; 35; 33; 38), all else rigorously
  excluded. No verified element in `(122, 50000]`.
- **Lemma 20:** six `m=2p` closed via a non-3-Higgs witness in `p*−1` for a
  large APR-CL-verified prime `p* | 2^m+1`; one more by Prop 4(3). Combined
  frontier: `|H_even∩[2,40000]| ≤ 201`, `|H_even∩[2,50000]| ≤ 272` (rigorous).
- **Thm 21 + Cor 22:** `#{m≤X : m∈H} ≪ X^{1−η}` (power-saving, via
  `Π₃(X) ≪ X/(log X)^{17/16}`, Rankin trick on `𝒮₃^{(≤3)}`), and `Σ_{m∈H} 1/m < ∞`.

## The scale obstruction and the analytic gap

For `m=2p`, a primitive divisor `r | Φ_{4p}(2)` needs `ord_r(2)=4p`,
`r≡1 mod 4p`, `(r−1)/(4p) ∈ 𝒮₃^{(≤3)}`. The log-mass identity
`log(2^{2p}+1) = log 5 + log Φ_{4p}(2) ~ 2p log 2` (non-primitive part `O(log p)`
by Hong) forces primitive divisors to carry log-mass `≫ p`, while Ford-type
thinness gives only reciprocal-mass `Σ 1/r ≪ 1/p`. **The gap is exponential,
`2^{2p}/p`**: thinness is on the wrong scale, `Π₃(2^{2k})` is still exponential
in `k`. Hence density/rarity is not finiteness.

**Why GRH/Chebotarev is the wrong scale:** Chebotarev/Hooley/Artin control
*varying* primes in a range by Frobenius; but `{r : ord_r(2)=4p}` is exactly the
prime divisor set of the single integer `Φ_{4p}(2)` — a finite set, not a range.
Nothing short of a *divisor-level* (transference) statement about the divisors
of `Φ_{4p}(2)` suffices; the paper states none such exists.

## Conjectures and conditional theorems (§5.3)

- **C23 (hybrid semigroup-friable shifted-prime):** for all large
  `k∈𝒮₃^{(≤3)}`, no prime `r` has both `ord_r(2)=4k` and `(r−1)/4k∈𝒮₃^{(≤3)}`.
  Would close C6 directly (Bilu–Hanrot–Voutier primitive divisor for k≥4).
- **C24 (semigroup log-mass):** admissible `r≤2^{2p}+1` satisfy
  `Σ log r ≤ (2 log 2 − δ)p`; would close C6 via the log-mass identity.
- **C29 (divisor mod-16 equidistribution):** `#{r | Φ_{4p}(2) : r≡1 mod 16} ≥ c·ω(Φ_{4p}(2))`; any such `r` has `v2(r−1)≥4`, non-3-Higgs. Matches empirical v2 data (53:29:0). C29 + C24 are the most plausible analytic targets.
- **C26 (sublog semigroup growth) `A(x)=o(log x)` + C25 ⇒ Thm 27 (finiteness).** **C26 is implausible**: Prop 28 shows `A_p(x)=o(log x)` forces `#{p∈P:p≤x}=O(log log x)`, contradicting `Π₃ ≍ x^{0.62}` unless `𝒫₃` itself is finite.
- **Thm 30 (conditional finiteness):** under (H1) effective Chebotarev-for-divisors: every `p` with `ω(Φ_{4p}(2)) ≥ C log p` has a divisor `≡1 mod 16`; and (H2) `ω(Φ_{4p}(2)) ≥ C log p` for `p≥p₀` — then `H_even` is finite with explicit candidate set. (H1),(H2) are conjectural; H2 is the target of Stewart's program (no `ω ≫ log n` bound in the literature). (H1) is **not** a consequence of GRH / effective Chebotarev.
- **Prop 31 / Cor 32:** surviving filter-N seeds in an even-parity impostor class are exactly `class ∩ H_even` with all proper divisors in `H_even`; if C6 holds, only finitely many seeds need filter O. For `3²5³`, `H_even ∩ {a≡10 mod 20} = {10,30}` in range, both killed by O.

**Bottom line:** the paper does not prove finiteness. It gives a verified finite
frontier, the prime-case reduction, a clean impossibility certificate for the
impostor kernels, and isolates the exact missing theorem: divisor-level control
of the prime divisors of `Φ_{4p}(2)` (C23/C24/C29), where thinness, GRH, and
Chebotarev are all the wrong scale.

```claim
id: hb-prop4-structural
statement: If m=2k∈H_even with k odd, then every prime factor of k is 3-Higgs,
  v_q(k)≤3 for every prime q|k (k is Higgs-cubefree), and 2d∈H_even for every
  odd divisor d|k.
hypotheses: Zsigmondy's theorem on {2^n+1} gives a primitive divisor r of
  2^{2k}+1 with ord_r(2)=4k and 4k | r-1; r 3-Higgs ⇒ v_q(r-1)≤3
holds-here: yes
status: catalogued
bearing: confines H_even to the doubled image of the cubefree 3-Higgs
  semigroup; this is the engine that lets finite factor-cache verification
  bound H_even over long ranges and transfers to the prime case
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1c3
```

```claim
id: heven-prime-case-reduction
statement: H_even is finite iff H_even^prime = {2p : p odd prime, 2p∈H_even}
  is finite, and |H_even| ≤ 4^|H_even^prime|.
hypotheses: Prop 4 structural lemma (Higgs-cubefree + divisor closure)
holds-here: yes
status: catalogued
bearing: the exact bottleneck — the UPN branch closes iff the 2p prime branch
  closes; every open primitive candidate has the form m=2p, the rest inherited
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1
```

```claim
id: heven-verified-members
statement: H_even ∩ [2,1200] = {2,6,10,18,26,30,46,62,82,122}; no verified
  element of H_even in (122,1200].
hypotheses: paper's factor cache, APR-CL transcripts; correct recursive
  3-Higgs verification for Theorem 8
holds-here: yes (not independently recomputed in this run)
status: asserted
bearing: the only confirmed H_even members; a run reproducing part of this
  table independently is the natural first check before trusting anything past it
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1b3
```

```claim
id: heven-thinness-not-finiteness
statement: #{m≤X : m∈H} ≪ X^{1-η} for an absolute η>0 and Σ_{m∈H} 1/m < ∞
  (same for H_even, H_odd); power-saving thinness, NOT finiteness.
hypotheses: Ford's theorem on downward-closed prime sets (omitted prime 17),
  then Rankin's trick over the cubefree semigroup S_3^{(≤3)}
holds-here: yes
status: proved (paper Thm 21 + Cor 22, R)
bearing: rarity is not finiteness; at the primitive-divisor height x=2^{2k}
  the bound is still exponential in k, so this theorem cannot close C6
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1c2
```

```claim
id: hb-lemma20-closures
statement: Six open candidates m=2p (2446, 10294, 10958, 17398, 19066, 20282)
  are excluded: a large APR-CL-verified prime p* | 2^m+1 has a non-3-Higgs
  witness q | p*-1 (v2 overflow or a Pratt-tree descent to 17), and 30882 via
  Prop 4(3) from 10294. This completes |H_even∩[2,50000]| ≤ 272.
hypotheses: p* primality by PARI/GP APR-CL (isprime(n,2)) trusted; trial
  division of q | p*-1; factor cache of 2^m+1
holds-here: yes (as sourced; transcript-dependent on APR-CL correctness)
status: asserted
bearing: the deep-closure mechanism that lowers the undecided frontier;
  shows the bottleneck is genuinely NFS-scale (cofactors of L_p/M_p),
  not shallow small-prime data
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1d2
```

```claim
id: hb-thm30-conditional
statement: If (H1) every odd prime p with ω(Φ_{4p}(2)) ≥ C log p has some
  prime divisor r≡1 mod 16, and (H2) ω(Φ_{4p}(2)) ≥ C log p for p≥p0, then
  H_even is finite, contained in the ten verified elements plus m=2p, p<p0
  in the open candidate set.
hypotheses: (H1) effective divisor-level mod-16 equidistribution of prime
  divisors of Φ_{4p}(2); (H2) ω-growth ≥ C log p. Both conjectural (H2 per
  Stewart's program, no ω ≫ log n bound known). (H1) NOT a GRH/Chebotarev
  consequence — those control varying primes, not divisors of one cyclotomic value.
holds-here: hypotheses unverified — this is a conditional theorem, not an
  unconditional result
status: asserted
bearing: names the precise near-miss route; the divisor-level mod-16
  equidistribution is the paper's recommended target, close to Conj 29
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1e1
```

```claim
id: hb-no-v2ge4-witness-1e11
statement: For all 162 original open candidates m=2p (p∈[1213,17467]), no
  prime r≡1 mod 16p with r ≤ 10^11 divides L_p or M_p; for m=2426 extended to
  6×10^11 (2,389,527 primes) with no divisor. So no v2≥4 non-3-Higgs witness
  exists below 10^11 across the open set; first non-3-Higgs prime of 2^{2p}+1
  must exceed 10^11 for every open p.
hypotheses: enumeration of r≡1 mod 16p up to 10^11, tested against the
  Aurifeuillean halves L_p,M_p; v2(r−1)≥4 forces r non-3-Higgs
holds-here: yes (computational sweep reported by the paper; bounded by 10^11)
status: catalogued
bearing: rules out a shallow 2-adic witness; says any such witness must be
  ≥10^11 (≥6×10^11 for 2426), which is why the open branch is NFS-scale —
  supports treating Conj 29/Thm 30 (H1) as the empirical-equidistribution target
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: whether-pass-loop-a1f1
```

## Gap status

- The five UPN witnesses and the run's own 2-adic budget identity are handled
  elsewhere (`research/notes/parity-and-2-adic-budget.md`, `heven-and-3-higgs-structure.md`);
  this note is the paper's structural digest and does not re-derive them.
- The paper settles the impostor branch only inside box ℬ at max a=10000; the
  UPN conjecture as a whole is untouched beyond that.
le is untouched beyond that.
 that.
