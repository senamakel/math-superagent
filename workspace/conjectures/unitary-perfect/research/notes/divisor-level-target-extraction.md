# Divisor-level target extraction — Maciejewski, "Bounded-box reductions in the Subbarao–Warren problem for unitary perfect numbers"

Source: [[maciejewski-bounded-box-subbarao-warren.full]] (arXiv:2605.20475v1,
19 May 2026, converted from HTML). Section and object references use the
paper's own numbering; quotes are verbatim from the converted text with the
conversion's doubled tokens (MathML artifacts, e.g. "p p") silently removed.
This note extracts the six families of statements requested and cross-checks
`research/approaches/biquadratic-character-divisors.md` and
`research/threads/divisor-level-phi4p.md` against the paper. The general digest
lives in `research/notes/paper-extraction.md`; the claim blocks below are new
rows for the ledger.

## 1. Definitions: 3-Higgs prime, H, H_even (§1.1, §5, §5.1)

§1.1: "A prime `p` is **3-Higgs** (OEIS A057447 [8]; see also Burris–Yeats
[16]) if `p − 1` divides the cube of the product of smaller 3-Higgs primes.
Every prime divisor of a UPN is 3-Higgs."

The exponent cap is part of the definition (Lemma 20 remark, a = 4527 example):
"`20127043 − 1 = 2 · 3⁴ · 13 · 19 · 503`. All prime factors
{2, 3, 13, 19, 503} are themselves 3-Higgs, but `v₃(20127042) = 4 > 3`
violates the exponent bound in the 3-Higgs definition. So 20127043 is not
3-Higgs." So: `p ∈ 𝒫₃ ⟺` every prime factor `q` of `p−1` is 3-Higgs **and**
`v_q(p−1) ≤ 3`. Recursive-closure form (§5.1): "`p ∈ 𝒫₃ ⇔ q | (p−1) ⇒ q ∈ 𝒫₃`".
Smallest omitted prime (§5.1): "the smallest omitted prime is `p₀ = 17` (as
`17 − 1 = 2⁴` violates the `v₂ ≤ 3` exponent bound)".

§5, verbatim: "Let `H := { m ≥ 1 : every prime factor of 2^m + 1 is 3-Higgs }`
and `H_even := H ∩ 2ℤ`."

§5.1 defines the confining semigroup: `𝒮₃^{(≤3)} := { n ≥ 1 : every prime
factor of n lies in 𝒫₃, and each such prime has exponent at most 3 }`.

## 2. The counting bounds and the verified set

**The two bounds are not numbered theorems.** The `40000` bound appears in the
abstract and in "Status of results"; the `50000` bound in the abstract and as a
derived statement at the end of §5 (after Theorems 8–19 and Lemma 20).

Abstract: "we prove `|H_even ∩ [2, 40000]| ≤ 201` and
`|H_even ∩ [2, 50000]| ≤ 272`, with explicit undecided frontier lists."

"Status of results": "Theorems 2, 7, 8–17 (rigorous bounds
`|H_even ∩ [2,N]| ≤ ·` with 191 undecided through N = 40000), Theorem 21
(power-saving thinness …), … and the combined rigorous bound
`|H_even ∩ [2, 40000]| ≤ 201`."

§5, after Theorem 19: "Combining Theorems 8–19, the factor-cache verification
alone yields `|H_even ∩ [2, 50000]| ≤ 279`, with the 10 verified elements
through m = 122, no verified element in `(122, 50000]`, and at most 269
undecided candidates beyond (of which 198 lie in `(1200, 40000]`, 33 in
`(40000, 45000]`, and 38 in `(45000, 50000]` before the seven deep-Pratt
closures). … The combined bound is therefore `|H_even ∩ [2, 50000]| ≤ 272`
(rigorous, no probable-prime caveat), with 262 undecided candidates remaining."

**Arithmetic check (this pass):** 198 undecided in `(1200,40000]` minus the
seven Lemma-20 closures (2446, 10294, 10958, 17398, 19066, 20282, 30882 — all
in that range) = 191; 191 + 10 verified = **201**. 269 − 7 = 262; 262 + 10 =
**272**. Both bounds recompute exactly.

**Theorem 8 (the verified-set theorem):** "`H_even ∩ [2, 1200] = {2, 6, 10,
18, 26, 30, 46, 62, 82, 122}`." Proof sketch quoted: "Of the 300 odd k in
[1,600], exactly 246 are Higgs-cubefree; the other 54 are structurally excluded
… 10 values of m have every prime factor of 2^m + 1 3-Higgs; these are exactly
the elements listed in the theorem statement. 236 values of m each contain at
least one verified non-3-Higgs prime factor … 0 values remain undecided."
Consequence: "Theorem 8 extends the verified gap considerably: H_even has no
element in the wide range `(122, 1200]`, strongly supporting Conjecture 6."

## 3. The divisor-level problem for Φ_{4p}(2) — the named analytic target

**The paper's own naming** (abstract): "The remaining task is a divisor-level
problem for the cyclotomic values `Φ_{4p}(2)`." And: "Thus the paper does not
prove finiteness; it gives a bounded-box elimination, a verified finite
frontier, and a precise analytic target for closing the remaining branch."

The gap statement (§5.1, end): "The remaining gap between this unconditional
result and Conjecture 6 is the last analytic step: showing that for
sufficiently large `k ∈ 𝒮₃^{(≤3)}`, no prime `r | 2^{2k} + 1` with
`ord_r(2) = 4k` has `(r−1)/(4k) ∈ 𝒮₃^{(≤3)}`."

The primitive-divisor admissibility condition a solution must break (§5.3):
"For each `m = 2k ∈ H_even`, a primitive prime divisor `r` of `2^{2k}+1` must
satisfy `r ≡ 1 (mod 4k)`, `ord_r(2) = 4k`, `(r−1)/(4k) ∈ 𝒮₃^{(≤3)}`."

The scale obstruction (§5.3): "The gap between what Ford-type thinness controls
and what would yield finiteness is exponential, of size `2^{2p}/p`", because
"the primitive divisors of `Φ_{4p}(2)` must supply primitive log-mass `≫ p`"
while Ford thinness gives only the reciprocal-mass bound `Σ 1/r ≪ 1/p`.
Also: "Density arguments by themselves cannot close Conjecture 6."

Why GRH/Chebotarev is the wrong scale (§5.3): "for fixed p … the set
`{r : ord_r(2) = 4p}` is finite—it is exactly the prime support of the single
integer `Φ_{4p}(2)` … A finiteness proof must control the divisors of
`Φ_{4p}(2)` individually (a divisor-transference statement), not via a density
estimate on `1 mod 4p`." Conjectures 23, 24, 29 are the three candidate
divisor-level theorems; the paper's own summary of them (§5.3): "Theorem 27
(semigroup-growth route) is logically valid but its hypothesis is too strong to
be the realistic endpoint. Conjecture 29 (divisor mod-16 equidistribution) is
much closer to the real obstruction and matches the empirical evidence
directly. Conjecture 24 (divisor log-mass bound) sits between the two and is
the cleanest formulation tied to the cyclotomic identity."

### 3a. What a solution would give / would not give

**Would give.** Finiteness of `H_even` (Conjecture 6). Conjecture 29's quoted
consequence: "Conjecture 29 would close Conjecture 6: any prime
`r ≡ 1 (mod 16)` has `v₂(r−1) ≥ 4 > 3`, hence `r ∉ 𝒫₃`." Combined with the
prime-case reduction (Theorem 7: `|H_even| ≤ 4^{|H_even^prime|}`, finite
prime branch ⟺ finite H_even) and the in-box impostor elimination, §5.4 says:
"A proof of Conjecture 6 (equivalently Conjecture 23), combined with the
cascade overshoot (filter O) for the necessarily finite set of
seed-non-Higgs-filter survivors, would close the impostor branch of the unitary
perfect number conjecture within ℬ." Final assessment (from §6): "What is
proved is a clean reduction of the impostor branch (within the bounded box ℬ at
max a = 10000) to a single specific analytic question (Conjecture 6,
equivalently Conjecture 23)".

**Would not give.** (i) The full Subbarao–Warren conjecture: "The full
Subbarao–Warren conjecture is not proved here." All bounded-box results are
confined to `ℬ := {p ≤ 2000, e ≤ 6, p^e ≤ 10^9, |SCC| ≤ 6, cycle length ≤ 6}`
(§1.2) and `1 ≤ a ≤ 10000` (Theorem 2). §6(2): "Enlarge the enumeration box ℬ
… Verify either that no new impostor kernels appear, or that any new ones are
closed by the same three filters." (ii) Control of `ω(Φ_{4p}(2))`: the
`ω → ∞` conjunct inside Conjecture 29 is itself open — "(H2) … is best regarded
as a conjectural target that the manuscript's analytic discussion isolates
rather than a near-result." (iii) Closure of the computational frontier: the
open candidates stay NFS-blocked — "Closing m = 2426 therefore requires finding
a non-3-Higgs prime in the residual composite `L_{1213}/(5·P)` (355 digits) or
in `M_{1213}` (366 digits)". (iv) Anything about `H_odd`: Corollary 32 notes
the fifth impostor kernel `3⁴41` has odd seed parity and "reduces to the
analogous odd-parity set H_odd, for which an analogous finiteness conjecture
applies". (v) The quantitative log-mass gap that Conjecture 24 targets, or
effective error terms.

## 4. Conjecture 6 and Conjecture 29, verbatim; Theorem 30's (H1)/(H2)

**Conjecture 6** (§5, in full): "H_even is finite." Equivalence used
throughout: "A proof of Conjecture 6 (equivalently Conjecture 23)…" and, via
Theorem 7, "prove that only finitely many odd primes p have all prime factors
of `2^{2p} + 1` in `𝒫₃`".

**Conjecture 29** (§5.3, in full): "**Conjecture 29 (Divisor mod-16
equidistribution).** There exists `c > 0` such that for all sufficiently large
odd primes `p ∈ 𝒫₃`, `#{ r ∣ Φ_{4p}(2): r ≡ 1 (mod 16) } ≥ c · ω(Φ_{4p}(2))`,
where `ω(Φ_{4p}(2)) → ∞` as `p → ∞`." Note the load-bearing one-way
implication (Prop 5, C29, Thm 30 all use it): `r ≡ 1 (mod 16) ⟹ v₂(r−1) ≥ 4 >
3 ⟹ r ∉ 𝒫₃`. The converse is **false** (see §7, M2). Also: "Conjecture 29 is
… a *divisor-level equidistribution* statement about the prime divisors of a
single fixed integer `Φ_{4p}(2)`. It is **not** a consequence of any standard
Chebotarev theorem, including effective Chebotarev under GRH
(Lagarias–Odlyzko)."

**Theorem 30 (Conditional finiteness)**, hypotheses verbatim:
- (H1) "There exists an effective constant `C > 0` such that for every odd
  prime p with `ω(Φ_{4p}(2)) ≥ C log p`, at least one prime divisor
  `r | Φ_{4p}(2)` satisfies `r ≡ 1 (mod 16)`."
- (H2) "There exists an effective threshold `p₀` such that for every prime
  `p ≥ p₀` we have `ω(Φ_{4p}(2)) ≥ C log p`, where C is the constant from
  (H1)."
- Conclusion: "Then H_even is finite. Explicitly, `H_even ⊆ {2, 6, 10, 18,
  26, 30, 46, 62, 82, 122} ∪ { m = 2p : p prime, p < p₀, m ∈ Open }`."

The paper's status notes: "(H1) is *not* a known consequence of any standard
effective Chebotarev theorem … (H2) … the natural target of Stewart's program
on radicals of Lehmer sequences", and "The unconditional version of Theorem 30
remains open and is the natural next research goal."

**Conjectures 23 and 24** (the other two named divisor-level targets), verbatim:

- C23: "For all sufficiently large `k ∈ 𝒮₃^{(≤3)}`, no prime `r` satisfies
  both `ord_r(2) = 4k` and `(r−1)/(4k) ∈ 𝒮₃^{(≤3)}`." Consequence: "Conjecture
  23 would close Conjecture 6 immediately, since the primitive divisor produced
  by Bilu–Hanrot–Voutier for k ≥ 4 would have to violate at least one of the
  two clauses, hence fail the 3-Higgs test."
- C24: "There exists an absolute `δ > 0` such that for all sufficiently large
  odd primes `p ∈ 𝒫₃`, `Σ_{r prime, r ≤ 2^{2p}+1, r ≡ 1 (mod 4p),
  (r−1)/(4p) ∈ 𝒮₃^{(≤3)}} log r ≤ (2 log 2 − δ) p`." Consequence: "Conjecture
  24 would close Conjecture 6: in any scenario `2p ∈ H_even`, every primitive
  divisor of `Φ_{4p}(2)` contributes to the admissible-prime sum, so the LHS
  must be at least the primitive log-mass `2p log 2 − O(log p)`, contradicting
  the upper bound for p large."

## 5. The five impostor kernels and the three filters (§2, §3, §4)

Kernels (verbatim table, §2) — "so named because they pass the cheap filters
but are not associated with any known UPN":

| Kernel | Forced exponents | Seed congruence |
| --- | --- | --- |
| `3²5³` | {3: 2, 5: 3} | `a ≡ 10 (mod 20)` |
| `3⁴41` | {3: 4, 41: 1} | `a ≡ 9 (mod 18)` |
| `5²13²` | {5: 2, 13: 2} | `a ≡ 6 (mod 12)` |
| `5⁴157²313` | {5: 4, 157: 2, 313: 1} | `a ≡ 130 (mod 260)` |
| `5⁴29·157²313` | {5: 4, 29: 1, 157: 2, 313: 1} | `a ≡ 26 (mod 52)` |

§2: "The conjecture restricted to ℬ is therefore equivalent to: no `a` in any
of the five impostor seed congruence classes admits a UPN."

§3: "We exhibit a rigorous obstruction for each candidate via one of three
filters."
- **Filter Z — Zsigmondy/Higgs exponent (§3.1):** "By Zsigmondy's theorem,
  every primitive prime divisor r of `p^e + 1` (with e > 1) satisfies
  `r ≡ 1 (mod 2e)`. For r to be 3-Higgs, every prime factor of 2e must be
  3-Higgs and occur in 2e with exponent at most 3. Applied to the seed exponent
  a itself, certain values of a are immediately incompatible."
- **Filter N — seed-divisor non-3-Higgs witness (§3.2):** "If `m | a` and
  `a/m` is odd, then `2^m + 1 | 2^a + 1`. If `2^m + 1` contains a non-3-Higgs
  prime factor, then any UPN with `2^a || n` would inherit a non-3-Higgs prime
  divisor, a contradiction." (Robust to partial factorisations: the a = 4527
  example is killed via the single known prime 20127043 | 2^1509 + 1.)
- **Filter O — 2-adic budget overshoot (§3.3):** "Initialize targets to
  `K ∪ (factor(2^m + 1) for cached m | a, a/m odd)`. Iterate: for each
  `p^e ∈ targets`, factor `p^e + 1` and accumulate the resulting odd needs; if
  any prime's incoming valuation exceeds its current target, raise the target.
  At each step, compute `v₂ := Σ_{p^e ∈ targets} v₂(p^e + 1)`." Its
  justification is **Lemma 1**: "The lower-bound closure is monotone in the
  seed. If `v₂ > a + 1` at any step using a subset S of `factor(2^a + 1)`, the
  same overshoot survives when more primes from `factor(2^a + 1)` are added.
  Hence no UPN with `2^a || n` and odd-component structure refining K exists."

The three filters together constitute **Theorem 2**: "For every impostor kernel
K listed in Section 2 and every a in K's seed congruence class with
`1 ≤ a ≤ 10000`, at least one of the three filters Z, N, O certifies that no
even unitary perfect number n exists with `2^a || n` and odd-component
structure refining K." Split (2119 candidates, max a = 10000): `Z | N | O |
Unresolved = 495 | 1614 | 10 | 0`. **Corollary 3:** "Within ℬ, the only
source-SCC kernels available to an even UPN with `2^a || n`, `1 ≤ a ≤ 10000`,
are the two known kernels `3²` and `5⁴`." (Prop 31 / Cor 32 tie the surviving
filter-N seeds exactly to `H_even`: survivors of N in an even-parity impostor
class = `{a ∈ K's seed class ∩ H_even : every proper m | a with a/m odd is in
H_even}`; e.g. for `3²5³`, `H_even ∩ {a ≡ 10 mod 20} = {10, 30}` in range,
both killed by filter O.)

## 6. Divisor-level results: which primes dividing Φ_{4p}(2) / 2^m+1 are 3-Higgs or forced non-Higgs

- **Prop 4 (structural lemma) mechanism** (§5): for `m = 2k ∈ H_even`, "the
  number `2^{2k} + 1` has a primitive prime divisor r for every k ≥ 1 odd …
  The order of 2 modulo r is exactly 4k, so `r ≡ 1 (mod 4k)` and
  `r − 1 = 4k·s`"; since r is 3-Higgs, "every prime q | r−1 is 3-Higgs and
  `v_q(r−1) ≤ 3`" — this forces k's prime factors to be 3-Higgs with
  `v_q(k) ≤ 3` (Higgs-cubefree) and forces every `2d` (d | k odd) into H_even.
- **Prop 5 (Fermat-prime obstruction)** (§5): every prime divisor q of the
  Fermat number `F_k = 2^{2^k} + 1` has `ord_q(2) = 2^{k+1}`, and "The
  refinement due to Lucas strengthens this for k ≥ 2 to
  `q ≡ 1 (mod 2^{k+2})`, hence `v₂(q−1) ≥ k + 2 ≥ 4 > 3 (k ≥ 2)`. The 3-Higgs
  definition forbids any prime factor of p−1 to occur with exponent exceeding
  3, so q is not 3-Higgs." Therefore "for any m with `v₂(m) = j ≥ 2` … q | 2^m
  + 1 and q is not 3-Higgs, so m ∉ H": **`H_even ⊆ {m ≡ 2 (mod 4)}`**. This is
  the paper's only unconditional "divisors of 2^m+1 are forced non-Higgs"
  mechanism.
- **Lemma 20 (deep-Pratt closures)** — six large divisors of `2^m+1` forced
  non-Higgs through their own `p*−1`: m → p* digits → witness → reason = 2446 →
  368 → 4513 (`v₂(4512) = 5`); 10294 → 1549 → 2657 (`v₂(2656) = 5`); 10958 →
  1649 → 593 (`v₂(592) = 4`); 17398 → 2612 → 139313 (`v₂(139312) = 4`); 19066 →
  2870 → 343081 (Pratt chain 343081 ≻ 953 ≻ 17); 20282 → 3053 (direct
  `v₂(p*−1) = 5071`). All p* APR-CL-verified (PARI `isprime(n,2)`); plus
  30882 via Prop 4(3) from 10294. These are forced non-Higgs divisors of
  `2^m + 1` (hence `m ∉ H_even`).
- **No shallow non-Higgs divisor exists for the open candidates** (the 2-adic
  sweep): "For each of the 162 original open candidates m = 2p with
  `p ∈ [1213, 17467]`, we enumerated every prime `r ≡ 1 (mod 16p)` with
  `r ≤ 10^11` and tested whether any divides L_p or M_p. No such r was found …
  For m = 2426 specifically the search was extended to `r ≤ 6 × 10^11`
  (2,389,527 primes tested), again with no divisor." Same for the
  non-Higgs-descendant sweep: "for each q ∈ {17, 97, 103, 113, 193, 257, 449,
  577, 641, 673, 769} … we also searched for primes `r ≡ 1 (mod 4pq)` with
  `r ≤ 10^11` dividing L_p or M_p across the first 80 open candidates. No
  witness was found. … The first non-3-Higgs prime in the factorization of
  `2^{2p}+1`, for each open p, must be of size beyond 10^11."
- **Positive 3-Higgs example** (§5.2, m = 2426, p = 1213): the known prime
  `P = 25893760589 | L_{1213}` has a full Pratt descent with "every exponent in
  every intermediate q−1 is at most 3. So P is *fully* 3-Higgs-compatible; no
  shallow recursive obstruction exists." This is what makes the open candidates
  genuinely open: ordinary Pratt descent cannot close them.
- **Empirical v₂ distribution** (§5.3, 53 open candidates in m ≤ 20000): "82
  distinct non-trivial prime factors … `v₂(q−1) = 2:` 53 primes;
  `v₂(q−1) = 3:` 29 primes; `v₂(q−1) ≥ 4:` 0 primes." Quote: "Open candidates
  are therefore precisely those for which the Chebotarev 'coin flip' on
  r mod 16 has not yet thrown a heads (r ≡ 1 mod 16) on the primes uncovered
  by FactorDB."

There is **no theorem** in the paper asserting that a prime divisor of
`Φ_{4p}(2)` is 3-Higgs, or forcing one to be non-Higgs, except Prop 5's
Fermat-number branch and Lemma 20's six APR-CL closures. Everything at the
`Φ_{4p}(2)` level is Conjectures 23/24/29 or the empirical sweeps above.

## 7. Cross-check: `research/approaches/biquadratic-character-divisors.md` vs the paper

Three mismatches. The first two change what the approach would prove; the third
misattributes a route to the paper.

**M1 — Conjecture 29 is conflated with mere existence.** Approach file:
"Conjecture 29 ('some divisor of Φ_{4p}(2) is ≡ 1 mod 16') is therefore
exactly: the quartic symbol `(2/r)_4` equals 1 for at least one primitive
divisor r." The paper's C29 requires proportionality: `#{r ≡ 1 (mod 16)} ≥
c·ω(Φ_{4p}(2))` with `c > 0` for all sufficiently large `p ∈ 𝒫₃` (ω → ∞ being
a conjunct). Existence of one `r ≡ 1 (mod 16)` is the (H1)-type hypothesis of
**Theorem 30**, not Conjecture 29; it is strictly weaker than C29. Consequence:
proving existence for one congruence class of p (the file's stated theorem
sought) would neither prove C29 nor close C6/Conjecture 6 — primes in the other
classes mod 8 would remain untouched. The file's phrase "proving Conjecture 29
for that infinite class" overstates the deliverable.

**M2 — the iff "r ≡ 1 (mod 16) ⟺ r is NOT 3-Higgs" is false in the converse
direction.** Approach file: "v2(r−1) ≤ 3 is exactly the 2-adic part of the
3-Higgs condition, so 'r ≡ 1 mod 16' ⟺ 'r is NOT 3-Higgs'." Only the forward
implication holds (`r ≡ 1 (mod 16) ⟹ v₂(r−1) ≥ 4 > 3 ⟹ r ∉ 𝒫₃`), and that is
all Prop 5, C29 and Thm 30 use. The converse is refuted inside the paper
itself: Lemma 20 row 5's witness 343081 | 2^19066 + 1 has `v₂(343080) = 3` yet
is non-3-Higgs (Pratt chain 343081 ≻ 953 ≻ 17), and in general odd q | r−1 must
also be 3-Higgs with exponent ≤ 3. (The file's generator equivalence itself —
`(2/r)₄ = 1` (2 a fourth power mod r) ⟺ `4 | (r−1)/4p` ⟺ `16p | r−1` for
primitive r, ord_r(2) = 4p — is mathematically correct: writing 2 = g^j,
`j = t·j'` with j' odd and `gcd(j', 4p) = 1`, so `4 | j ⟺ 4 | t`. Only the
chain to "3-Higgs" is wrong; it should stop at the one-way implication.)

**M3 — §6 attribution.** Approach file: "This is the 'algebraic factorization'
route the paper names as its own next step (§6)." The paper's §6 contains no
Z[i]-factorization or quartic-reciprocity step. Its item (3) on Conjecture 6
reads: "A serious attack would combine Bilu–Hanrot–Voutier primitive divisor
bounds [5] with shifted-prime smoothness statements. A conditional density-zero
result (e.g., under GRH) would already suffice for the application here." §6's
other items are: extend max a; enlarge the box ℬ; combine Hagis/Graham/Theorem
2 bounds; formal verification. Note the paper-internal tension this exposes:
§5.3 says "Density arguments by themselves cannot close Conjecture 6" and
"GRH/Artin density is the wrong scale", while §6(3) says a GRH-conditional
density-zero result "would already suffice for the application here" — "the
application here" is ambiguous (it cannot mean closing C6 unconditionally).
Flagged, not resolved.

## 8. Cross-check: `research/threads/divisor-level-phi4p.md` vs the paper

The thread is accurate. Confirmed verbatim: Conjecture 29's proportional
statement (with `c·ω` and the ω → ∞ conjunct); Conjecture 24's log-mass bound;
Conjecture 23; the exponential gap of size `2^{2p}/p`; the Aurifeuillean split
`2^{2p}+1 = L_p·M_p` (Eq. 2) and the quartics `2X⁴ ∓ 2X² + 1` /
`8X⁴ ∓ 4X² + 1`; open candidates {2426, 2602}; Hong's non-primitive `O(log(4p))`
bound; the 53:29:0 v₂ data; the r ≤ 10^11 sweep; the claim that "no standard
effective Chebotarev (even under GRH)" gives divisor-level control. Minor
imprecisions, none substantive: the thread's C24 rendering omits the "r prime"
and "p ∈ 𝒫₃" qualifiers; its opening question ("some prime divisor of
Φ_{4p}(2) is NOT 3-Higgs" for all large p ∈ 𝒫₃) is wider than C29 (the mod-16
route) and drops (H1)'s `ω ≥ C log p` hypothesis — this is consistent with the
paper's own "last analytic step" framing and with Theorem 7, so it is a fair
paraphrase of the true target, not a misreading. The thread's "53 open
candidates" figure inherits a paper-internal count discrepancy (next section).

## 9. Discrepancies found inside the paper (this pass)

- **"53 open candidates" does not match the printed candidate sets.** §5.3 says
  "all 53 remaining candidates in Theorem 13" and "Across all 53 open
  candidates of Theorem 12–13, 82 distinct non-trivial prime factors …" —
  but the printed sets are Theorem 9: 2, Theorem 10: 5, Theorem 11: 5,
  Theorem 12: 10, Theorem 13: 27 (37 candidates in m ≤ 20000 at print; 49
  through m ≤ 25000 including Theorem 14's 27). 53 is not recoverable from the
  print; likely an earlier computation stage. The 201/272 bound arithmetic is
  unaffected (it uses the 198/269/262 undecided counts, which do recompute).
- **"162 original open candidates" (the 2-adic sweep) is likewise unexplained**
  by the printed totals (191 undecided through 40000; 269 through 50000;
  279 − 10 = 269). Same status: unverified, low impact.
- **§5.3 vs §6(3) tension on GRH/density** (quoted in §7, M3).
- **"Status of results" describes Theorem 27 as "uses Stewart-radical plus
  effective Chebotarev"** — the theorem's actual statement is "Conjectures 25
  and 26 together imply |H_even| < ∞", with no Stewart-radical or Chebotarev
  content. The status list's description does not match the theorem. (Corollary
  32's remark about the four even-parity impostors also omits 3⁴41, which has
  odd parity — consistent with the paper's own text, not a discrepancy.)

## 10. Claim blocks for the ledger

```claim
id: hb-defs-3higgs-heven
statement: A prime p is 3-Higgs iff p−1 divides the cube of the product of
  smaller 3-Higgs primes, equivalently every prime factor q of p−1 is 3-Higgs
  with v_q(p−1) ≤ 3; P_3 = 3-Higgs primes, smallest omitted prime 17;
  H = {m ≥ 1 : every prime factor of 2^m+1 is 3-Higgs}, H_even = H ∩ 2Z;
  S_3^{(≤3)} = cubefree semigroup on P_3. Every prime divisor of a UPN is
  3-Higgs.
hypotheses: none (definitions, §1.1, §5, §5.1)
holds-here: yes
status: catalogued
bearing: H_even is the single remaining branch after the in-box impostor
  elimination; the semigroup S_3^{(≤3)} is the object every divisor-level
  conjecture quantifies over
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
answers: what-is-the-heven-target
```

```claim
id: hb-c6-finiteness
statement: Conjecture 6 — H_even is finite. Open. Equivalent (Theorem 7) to
  finiteness of the prime branch H_even^prime = {2p : p odd prime, 2p∈H_even},
  with |H_even| ≤ 4^|H_even^prime|.
hypotheses: none (conjecture)
holds-here: open — the statement the run targets
status: asserted
bearing: closes the Subbarao–Warren reduction within box B at max a=10000
  when combined with Theorem 2/Cor 3 (see §3a for what it does and does not
  give)
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
```

```claim
id: hb-c23-hybrid-semigroup
statement: Conjecture 23 — for all sufficiently large k in S_3^{(≤3)}, no
  prime r satisfies both ord_r(2) = 4k and (r−1)/(4k) ∈ S_3^{(≤3)}. Would close
  Conjecture 6 via the BHV primitive divisor of 2^{2k}+1 (k ≥ 4).
hypotheses: Bilu–Hanrot–Voutier primitive-divisor existence; k ∈ S_3^{(≤3)}
  sufficiently large
holds-here: yes (conjectural target; hypotheses apply to the sequence 2^n+1)
status: asserted
bearing: the paper's "genuine analytic target" combining recursive semigroup
  friability with the exact-order condition; nothing in the literature has this
  shape
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
```

```claim
id: hb-c24-semigroup-logmass
statement: Conjecture 24 — there is an absolute δ > 0 such that for all
  sufficiently large odd primes p ∈ P_3, the sum of log r over primes
  r ≤ 2^{2p}+1 with r ≡ 1 (mod 4p) and (r−1)/(4p) ∈ S_3^{(≤3)} is at most
  (2 log 2 − δ) p. Would close Conjecture 6: the primitive divisors of
  Φ_{4p}(2) then cannot carry their required log-mass ~ 2p log 2 − O(log p).
hypotheses: p ∈ P_3 large; non-primitive part of 2^{2p}+1 is O(log(4p)) (Hong)
holds-here: yes (conjectural target)
status: asserted
bearing: the "cleanest formulation tied to the cyclotomic identity" — the
  divisor-level log-mass bound the thread names as its closing conjecture
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
```

```claim
id: hb-c29-divisor-mod16
statement: Conjecture 29 — there is c > 0 such that for all sufficiently large
  odd primes p ∈ P_3, #{r | Φ_{4p}(2) : r ≡ 1 (mod 16)} ≥ c·ω(Φ_{4p}(2)),
  where ω(Φ_{4p}(2)) → ∞ as p → ∞. Any such r has v2(r−1) ≥ 4 > 3 so is not
  3-Higgs; would close Conjecture 6. PROPORTIONAL statement — not mere
  existence of one r ≡ 1 (mod 16); the existence form is (H1) of Theorem 30.
hypotheses: ω-growth is a conjunct of the conjecture, itself open (≈ (H2));
  the implication r ≡ 1 (mod 16) ⇒ r ∉ P_3 is unconditional and one-way only
holds-here: open (conjecture)
status: asserted
bearing: the paper's closest-to-the-obstruction target; NOT a consequence of
  standard effective Chebotarev even under GRH (divisor set of one fixed
  integer, not a range of primes)
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
contradicts: none on disk; the run document `approaches/biquadratic-character-divisors.md` glosses C29 as existence — mismatch recorded in §7 of this note
```

```claim
id: hb-thm30-h1-not-chebotarev
statement: (H1) of Theorem 30 — "every odd prime p with ω(Φ_{4p}(2)) ≥ C log p
  has at least one prime divisor r | Φ_{4p}(2) with r ≡ 1 (mod 16)" — is not a
  consequence of any standard effective Chebotarev theorem, including under GRH
  (Lagarias–Odlyzko): those control varying primes in Frobenius classes, while
  the prime support of Φ_{4p}(2) is one fixed integer. The missing object is a
  divisor-transference theorem, which does not currently exist in the
  literature.
hypotheses: none — the paper's own claim about the literature
holds-here: yes
status: asserted
bearing: rules out the GRH/Chebotarev route before it is attempted; any
  approach claiming density suffices contradicts this paragraph (§5.3)
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
```

## Verified against the full text

Read end-to-end (2026-08 scholar pass). All numbered items in §1–§6 above are
present verbatim in the source; the two run documents were compared to the
text, with the three mismatches in §7 and the paper-internal discrepancies in
§9 recorded. The 201/272 arithmetic and the 279→272 reduction were recomputed
by hand from the paper's own counts (`198−7=191`, `191+10=201`; `269−7=262`,
`262+10=272`).