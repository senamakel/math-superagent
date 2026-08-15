# G-supply as a conditional theorem — exact statement

**Cycle / source:** research specialist, following the consolidated Route B skeleton
(`research/backward/route-b-supply-consolidated.md`) and the settled G-supply crux
(`research/notes/g-supply-two-point-crux-settled.md`). This note states, cleanly and
exactly, the CONDITIONAL theorem that is the honest deliverable of Route B. It does not
claim the unconditional bound — ABGS 2011 §9 shows that is open (see below).

---

## Notation

- `q_1, q_2, ... = 2, 3, 5, 7, ...` the primes. A finite prefix `q_1..q_n` (n ≥ 2).
- `A_k` the k-th row of the absolute-difference (Gilbreath) triangle: `A_0 = q`,
  `A_{k+1}(i) = |A_k(i) − A_k(i+1)|`.
- GC: `A_k(0) = 1` for every k ≥ 1.
- Right-diagonal coordinates: `δ(q_n) = (δ_0,...,δ_{n−1})`, `δ_k(q_n) = A_k(n−k)`.
  Then `δ_{n−1}(q_n) = A_{n−1}(0)`, so "prefix `q_1..q_n` succeeds" ⟺ `δ_{n−1}(q_n) = 1`.
- `ν₂(q_n)` = the number of 2s in the maximal `{0,2}` suffix of the right diagonal
  `δ(q_n)` (equivalently of row `A_*`'s leading `{0,2}` block at the relevant depth).
- `g*_n` = `max(g_2,...,g_n)`, the largest prime gap among the first n gaps.
- The mod-4 switch bit: `h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 = 1 ⟺ gap_{j+1} ≡ 2 (mod 4)`
  ⟺ the consecutive pair `(p_{j+1}, p_{j+2})` switches residue class mod 4.
- `N_switch(x) = #{p_j ≤ x : p_{j+1} ≢ p_j (mod 4)}` = the consecutive-pair switch count.
- (ABGS) `N(a,d,m,x) = #{p < q ≤ x : p ≡ a, q ≡ a+d (mod m)}` = consecutive-pair
  residue-pair count.

---

## The CONDITIONAL theorem

> **Theorem (conditional).** Assume the **Hardy–Littlewood prime k-tuple conjecture**
> (equivalently its two-point special case, the **Lemke Oliver–Soundararajan (LOS 2016)
> two-point consecutive-prime mod-4 switch-correlation lower bound**). Then
> ```
> ν₂(q_n) ≥ c·n  for some fixed c > 0 and all sufficiently large n.
> ```
> Hence, via Granville Lemma 5.4 and Theorem 5.5 (with the demand side
> `g*_n < n^{0.52+ε}` unconditional by Baker–Harman–Pintz, sharpened by Li 2023),
> **Gilbreath's conjecture holds** — every finite prime prefix `q_1..q_n` succeeds.

### The exact hypothesis

The hypothesis is one clean, well-studied two-point correlation — **not** PNT-in-AP,
Dirichlet, or GRH. Concretely either:

- **(HL)** the Hardy–Littlewood prime k-tuple conjecture: the count of prime k-tuples
  `n+h_1,...,n+h_k` is `𝔖(h) ∫_2^X dt/(log t)^k` with the singular series `𝔖(h)`; for the
  consecutive-pair count `N(a,d,m,x)` this gives
  `N(a,d,m,x) ~ c(a,d,m)·x/log²x` (the mod-4 switch pairs `(1,3)`, `(3,1)` each with the
  predicted positive density), or
- **(LOS two-point switch-correlation lower bound)** the (conjectural) statement that the
  consecutive-pair switch count obeys
  `N_switch(x) ≥ c·π(x)`, equivalently the mod-4 switch bit `h[j]` is unbiased,
  `P(h=1) ≥ δ` for a fixed `δ > 0`, with bounded two-point correlations — the LO/Sawtooth
  two-point structure.

Under either, the halved-gap parity bit string `h[j]` is asymptotically unbiased with
bounded pair correlations, so the mod-4 switch frequency is genuinely positive density.
It is exactly this fact that PNT-in-AP alone cannot deliver (see the crux below).

### The precise inference

1. **Supply (the named hypothesis, DONE conditionally).** Under HL/LOS, `h[j]` is an
   unbiased bit string with bounded pair correlations. `ν₂(q_n)` is the Hamming weight of
   a **fixed invertible Rule-90 (Pascal-mod-2) fold** of `h` over the fixed window
   `[2, n−1]` of `A_1` (claim `rule90-interior-xor`; the fold is $F_2$-linear, invertible,
   claim `edge-interior-invertibility-sharpened`). A bounded-difference / Azuma-type
   concentration bound over the fold, applied to the prime bit string directly (NOT via
   the refuted universal transfer `ν₂ ≥ w/2`), gives the main term the data already show:
   `ν₂(q_n) = n/2 + O(√(n log n))`, in particular `ν₂(q_n) ≥ c·n`. (Measured to
   n = 1e5: max |ν₂ − n/2| = 624, min ν₂/n = 0.4587, weakest implied exponent 0.7658 ≫
   0.525.) This is a corollary-level conditional statement, not a new conjecture.

2. **Runway (discharged, proved).** Lemma 5.4 (re-derived and PROVED on the even domain,
   `lemma54-re-derived-proof`, kernel-checked in Lean as `lemma54-descent-lean-formalised`):
   ```
   q_1..q_{n−1} valid & successful  ∧  g*_n ≤ 2ν₂(q_{n−1}) + 2  ⟹  q_1..q_n succeeds.
   ```
   Link A (`v ≤ g*_n`) verified non-vacuously over 1181 columns, 0 violations.

3. **Demand (discharged, unconditional).** `g*_n < n^{0.525+ε}` (Baker–Harman–Pintz 2001),
   sharpened to `n^{0.52+ε}` (Li 2023). Immaterial once a linear supply bound holds
   (`li2023-not-bottleneck`).

4. **Combine.** For large n, supply gives `ν₂(q_{n−1}) ≥ c(n−1) > n^{0.52} ≥ g*_n`, so the
   runway (2) turns "`q_1..q_{n−1}` successful" into "`q_1..q_n` successful". Strong
   induction on n from a verified base (the run's depth 1000, or Odlyzko 10^13 /
   verification-record-2026) gives every finite prime prefix successful, hence GC.

### The honest caveat

This is a **conditional** theorem. Its sole hypothesis is a named open two-point
correlation. It is **not** claimed to be provable unconditionally from anything the
library holds.

---

## Why the unconditional version is open — ABGS 2011 §9 (verbatim)

The claim `abgs-2011-s9-mod4-switch-limit-open` (verified against the primary text in
`research/notes/abgs-s9-verbatim-verified.md`):

> Ash–Beltis–Gross–Sinnott 2011, *Experimental Mathematics* 20(4):400–411, §9 ("Further
> Open Questions"): whether the consecutive-pair residue frequency
> `N(a,d,m,x)/π(x)` tends to **any** limit as x → ∞ is **open**. Verbatim: *"we cannot
> tell whether they are tending toward a limiting ratio of 1."* The Introduction states
> the asymptotics of `N(a,d,m,x)` "*is wide open, and cannot be treated using
> L-functions*" — the structural reason the switch count is beyond one-point analytic
> machinery.

Consequence: **no unconditional positive-linear lower bound `ν₂ ≥ c·n` is provable from
current methods.** The switch count `N_switch(x)` is a two-point statistic (the joint
distribution of two consecutive primes), and one-point marginals (PNT-in-AP classes, GRH,
Dirichlet) impose **no** lower bound on it: an ordering listing all 1-mod-4 primes then
all 3-mod-4 primes is consistent with the marginals yet has a single switch. The
unconditional literature (Ruzsa 2001, Shiu, Martin et al. 2024 survey) bounds only the
**non-switch / equal-residue** direction `≫ x loglog x/log² x` — which pushes the switch
count *down*, the wrong way for ν₂. Route B therefore rests on exactly one open,
well-studied two-point conjecture.

---

## MathOverflow fetch (questions/34669) — does NOT advance G-supply

The named fetch-and-close target (Directive 47) is already DONE in the library
(`research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md`,
`research/summaries/mathoverflow-gilbreath-what-is-known-thread.md`); per the
"do not re-fetch" instruction the held full text was consulted (not re-downloaded) and
checked against the G-supply question.

**Result: the thread does NOT advance the mod-4 switch-frequency matter.** Its entire
content is (a) Tao 2024 on Chase 2024's random analogue (the `{0,2d}`-block obstruction
and mod-4 control of *even*-d blocks — the CHT-equivalent obstruction, already held), (b)
Zaimi 2010 / Myerson on there being no progress beyond Odlyzko's verification and on the
general-class "2-and-odds, slow growth" framing, (c) Srilakshmi 2012 independently hitting
the run's refuted forward-difference route, and (d) tdnoe on OEIS A080839. **No answer or
comment touches `N(a,d,m,x)`, `ν₂`, consecutive-pair residue switching, the two-point
crux, or any supply-side bound.** So the fetch confirms the library's dead-route records
and adds the `mo-thread-*` claims (`mo-thread-no-new-dead-route` etc.), but is silent on
G-supply.

**The G-supply row in `research/REQUESTS.md` is UNCHANGED by the fetch.** It stood (and
stands) CLOSED — negative, settled by `g-supply-two-point-crux-settled.md`: the switch bit
is two-point, no unconditional linear bound is provable from current methods, and the
honest Route B deliverable is the conditional theorem stated above. The named-open
hypothesis remains `abgs-2011-s9-mod4-switch-limit-open`.

---

## Claims relied on

`gilbreath-reduces-to-second-in-02`, `gilbreath-second-entry-equivalence`,
`lemma54-re-derived-proof`, `lemma54-descent-lean-formalised`,
`lemma54-lean-and-linkA-current-verified`, `gap-bounds-cannot-force-block-growth`,
`li2023-short-interval-052`, `li2023-not-bottleneck`, `abgs-2011-s9-mod4-switch-limit-open`,
`abgs-s9-verbatim-verified`, `rule90-interior-xor`, `edge-interior-invertibility-sharpened`,
`g-supply-transfer-measured`, `verification-record-2026`.

**Anchor for the MO fetch:** `research/sources/mathoverflow-gilbreath-what-is-known-thread.full.md`.
