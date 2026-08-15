# Pattern-finder report: ν₂ — the open supply quantity of Route B

## What this quantity is

`ν₂(q_n)` = number of 2s (`c_s = 2`) in the maximal `{0,2}` suffix of the
prime right diagonal through `q_n` (= cell `A_k[n-k]`). This is the **entire
remaining open content** of the primary route (GOAL.md/Gaps): Granville
Lemma 5.4 → Theorem 5.5 reduces Gilbreath's conjecture to
`ν₂(q_n) > n^β, β > 0.525`, and no source proves it. The demand side is
closed (`lemma54-re-derived-proof`); only the **supply** bound is open.

Data source: `code/out/nu2_dense.txt` — 30,000 exact integer terms, sieve
`1e6`, computed by `code/pattern_finder/nu2_dense_transfer.py` (O(N²) exact
abs-diff diagonal; O(N) memory). All figures below are exact over these
30,000 supplied terms; none proved beyond them.

## Findings

### 1. The atomic bits are two-point, as the board already concluded

The `{0,2}`-tail evolves by XOR (Pascal mod 2), and by the mod-4
linearization an entry's exact value mod 4 is a Rule-90 combination of the
*halved gaps*. Each halved-gap parity bit is
`[p_{n+1} ≢ p_n (mod 4)]` = the consecutive-prime mod-4 class switch. This is
a **two-point** statistic (needs both `p_n` and `p_{n+1}` mod 4), so PNT-in-AP
does not alone give the supply; Hardy–Littlewood / Lemke-Oliver-level
control is the honest target. Fis conslistent with `check_nu2_one_vs_two_point`.

### 2. Transfer bound `ν₂ ≥ c·w` — clean and tightens with scale (the key number)

Let `w(n)` = Hamming weight of the mod-4 gap bits over the ancestor window
`j ∈ [2, n-1]` (one cell reaches column 2, so the window is the fixed
interval regardless of where the tail starts). Then, **exact over n = 2..30000**:

| tail | smallest c with ν₂ ≥ c·w on every n ≥ tail | last violating n |
| --- | --- | --- |
| 2 | 0 (n=3,4 fail) | — |
| 17 | **0.5** | 16 |
| 1000 | **0.75** | 1005 (alone) |
| 4000 | **0.80** | none |

So on the sampled scale `ν₂ ≥ 0.75 · w` holds once n ≥ 1005, and `ν₂ ≥ 0.5·w`
for all n ≥ 17. Since `w` is a coin-like random walk (its bits are two-point
prime-gap mod-4 switches with empirical density ≈ 0.6 per the run), `w ≈ c′n`
and this is the cleanest *transfer* lower bound available. **Conjecture** (not
proved): `ν₂(q_n) ≥ (1/2)·w(n)` for all `n ≥ 17`, and `ν₂ ≥ (3/4)·w(n)` for all
sufficiently large n.

### 3. Fluctuation concentration — the linear bound survives by a huge margin

`dev(n) = 2·ν₂(n) − n` is "Gaussian-like" around 0:
- max |dev| = 639 at n = 27625; never below `−5·sqrt(n)`.
- max |dev|/sqrt(n) = 3.845 (n=27625); max |dev|/sqrt(n·log n) = 1.34.
- longest deficit run (dev < 0) = 15 (n = 3410..3424); dev is negative on
  55.3% of n (it oscillates — confirms the Rubinstein–Sarnak bias-oscillation
  caution: nothing one-sided can be asserted unconditionally).

The implied supply exponent `β = log(ν₂)/log(n)` ranges **[0.888, 0.934]**
over n ≥ 1000 — comfortably above the required 0.525. The honest claim is
`ν₂ = n/2 + O(n^{1/2+ε})`, from which `n/2 − O(n^{0.525}) > n^{0.525}`
follows for large n (the deviation margin at the worst n=27625 is 13174 vs.
a threshold of 215).

### 4. min `ν₂/n^0.525` over n ≥ 4000 = 24.95 (at n=4020)

So even pointwise against the theorem's actual threshold, the margin is a
factor ≥ 25 on the whole sampled range. Not a proof, but the target is
comfortable.

### 5. No closed form to extract by lookup — both ν₂ sequences are OEIS-miss

- raw ν₂ prefix `0,0,0,0,2,2,2,2,2,2,6,3,5,3,5,3,11,6,6,14,10,9,8,12,11,13,11,11,12,18,11,10,...`: **no OEIS entry**.
- sample-100 terms `46,106,148,216,239,285,337,397,408,489,...`: **no OEIS entry**.

`find_linear_recurrence` (order ≤ 8) and `analyze_sequence` find no
constant-coefficient recurrence, no low-degree polynomial. The fluctuation
`2ν₂−n` is irregular at every order the tools test. This records a dead end:
**nobody should re-search ν₂ in OEIS** — it is uncatalogued and no closed form
is available by lookup. The regularity is not in a low-order arithmetic law of
ν₂ but in the **transfer to w** and the linear fluctuation bound.

## What is a conjecture vs. a check

- Erosion / block-protection / step law: **proved** elsewhere (not this file).
- All transfer bounds and fluctuation margins above: **verified-numerically,
  exact over the 30,000 supplied terms** — conjectures for the full sequence.
- Specifically: `ν₂ ≥ 0.5·w(n) ∀ n≥17`, `ν₂ ≥ 0.75·w(n)` asymptotically,
  `ν₂ = n/2 + O(n^{1/2+ε})` are conjectures; each is stated with its
  false-ying first term unknown (data ran to 30000, none).

## Recommendation

Route B needs the supply bound. The cleanest, most likely-to-yield-derivation
regularity is the **transfer bound `ν₂ ≥ 0.75·w`** (§2): it turns the problem
into controlling the consecutive-prime mod-4 switch density `w(n)`, which is a
two-point (Hardy–Littlewood / Lemke-Oliver) density — a named, attackable
target — rather than the raw ν₂, which demonstrably has no low-order arithmetic
structure (§5). The fluctuation concentration (§3), at the stated
`O(n^{1/2+ε})` level, is the stronger claim that directly meets the theorem's
`β>0.525` threshold and is what a "regeneration-rate" proof actually needs.
