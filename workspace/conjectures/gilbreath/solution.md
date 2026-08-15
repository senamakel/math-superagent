# Solution — the standing conditional theorem (Route B)

## The honest deliverable

Gilbreath's conjecture (1878/1958) remains **open**. Nothing in this run proves
it. What the run has established, kernel-checked in Lean and re-verified here
from scratch by independent programs, is a **conditional theorem** with a
precisely identified, named-open hypothesis. The deliverable is that theorem,
the map of five dead escapes and the one shared reason they all die, and the
knowledge that closing the hypothesis is an open problem in analytic number
theory — not a gap in this argument.

The conjecture reduces to one statement (problem.md): the second entry of every
row lies in `{0,2}`, because 2 is the only even prime and `|1−e|=1` iff
`e∈{0,2}`.

## What is proved

### 1. The reduction (proved, Lean-formalised, sorry-free)

`A_{k+1}(0)=1 ⟺ A_k(1)∈{0,2}`. The `(odd, even, even, …)` shape is preserved by
the absolute-difference operator, so the whole conjecture is the `{0,2}`
second-entry statement. Formalised in Lean 4 (`code/lean/gilbreath_reduction.lean`,
IFF, sorry-free; `#print axioms` = propext/Classical.choice/Quot.sound only).

### 2. Consumption is settled; regeneration is the open problem

A leading `{0,2}` block of length `n` protects exactly **n+1** rows — protection
constant 1, not n/2 (the n/2 figure was refuted this run; `odlyzko-block-lemma-exact`,
re-derived as the step law). Exact accounting:

```
step law:   b_{k+1} ≥ b_k  iff (x,y)=(2,4),  else b_{k+1}=b_k−1
recharge:   b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1)
```

A (2,4)-event is the only growth mechanism. The open problem is whether events
arrive fast enough that the recharge sum never falls k−1 behind —
**regeneration, not erosion**. Erosion is settled; regeneration is not.

### 3. Descent / absorption lemma (proved as a general theorem, Lean-formalised sorry-free)

Let `c_1..c_L∈{0,2}`, `v≥0` even, `x_0=v`, `x_s=|x_{s−1}−c_s|`, `ν₂=#{c_s=2}`.
Then:

1. `x_L∈{0,2} ⟺ v ≤ 2ν₂+2`
2. `v > 2ν₂+2 ⟹ x_L = v−2ν₂ ≥ 4` (never enters `{0,2}`)
3. `{0,2}` is absorbing

Proof: case split. **Branch A (absorption):** if ever `x_t≤2` then `x_t∈{0,2}`
and `{0,2}` absorbs. This is the δ=0 case Granville's published proof discards
as an "exception" — here it is the mechanism, occurring in 100% of real columns,
and it is proved, not waved away. **Branch B (descent):** if all `x_s≥4`, no
bounce occurs, `c=2` maps `x↦x−2`, so `x_L=v−2ν₂`, and the contradiction/runway
follows. This repairs the written-proof defect of the original (the old algebra
`δ=v−2ν₂` fails on bounce trajectories like `v=0,ε=(2,2,2)`).

Kernel-checked sorry-free at `code/lean/descent_lemma.lean`; exhaustively
machine-checked (12.58M halved + 11.53M unhalved `(pattern,v)` pairs, 0
violations). Link A (`v ≤ g*_n`) and the even-domain composition also
kernel-checked. This is the first kernel-checked result of the run.

### 4. Independent from-scratch backbone verification (this attempt)

A fully self-contained program (own sieve to 200000, own triangle builder, no
lib import) — `code/out/deliverable_backbone_check.py`, captured as
`deliverable_backbone_check.captured.txt` (EXIT_CODE=0):

- **Worked rows reproduced exactly**: `A_1=(1,2,2,4,2,4,2,4,6,2)`,
  `A_2=(1,0,2,2,2,2,2,2,4)`, `A_3=(1,2,0,0,0,0,0,2)` — MATCH each.
- **Second entry ∈{0,2} for 60/60 rows** (k=1..60) — the reduction at the heart
  of the conjecture, confirmed on every sampled row.
- **Descent biconditional on real prime diagonals (n=2..200): 0 violations** of
  `x_L∈{0,2}⟺v≤2ν₂+2`, of the runway `v>2ν₂+2⟹x_L=v−2ν₂`, and of absorption.
- **Supply measured, not proved**: min `ν₂/n` over n∈[50,2000] = 0.3273 (at
  n=55) — a linear bound is plausible at this scale but remains open.

## The one open condition: G-supply

Everything reduces to a single density statement on the primes:

> **G-supply.** There exists `c>0` (equivalently `β>0.525` for the Granville
> form) with `ν₂(q_n) ≥ c·n` for all large `n`, where `ν₂(q_n)` is the number
> of 2s in the maximal `{0,2}` suffix of the right diagonal of column `n`.

- **Demand side discharged unconditionally**: `g*_n < n^{0.525+ε}` by
  Baker–Harman–Pintz (and shaved to 0.52 by Li 2023); this is not the
  bottleneck.
- **Supply side is a prime-gap-mod-4 statement**: the `{0,2}` tail cells'
  row-1 ancestor union is the fixed interval `[2,n−1]` of `A_1`, halved bits are
  1 iff `gap≡2 (mod 4)`, and `ν₂(q_n)=wt(Φ_n h)` where `Φ_n` is the Pascal-mod-2
  fold of the mod-4 switch bit `h`. So G-supply reduces to how often
  `p_{j+1}−p_j≡2 (mod 4)` — a **two-point** correlation. Measured
  `ν₂/n ∈ [0.42,0.52]` on samples, but **no unconditional linear lower bound
  exists in the literature** (Ash–Beltis–Gross–Sinnott 2011 §9: whether
  `N(a,d,m,x)/π(x)` tends to any limit is open; it cannot be treated with
  L-functions).

Therefore Route B yields a **conditional theorem**: *IF* the two-point
consecutive-prime mod-4 switch correlation satisfies the linear lower bound
`ν₂ ≥ c·n`, *THEN* Gilbreath's conjecture holds. The hypothesis is named, open,
and precisely stated. This is not a proof.

## The five dead escapes, and the one shared reason

Five routes to replacing the arithmetic have been closed (all `refuted` in the
ledger). They die for one shared reason: **`Φ_n` has low-weight images on
structurally rich inputs.** Balancing, anti-dyadicity, aperiodicity, and
non-concentration are all structural conditions on the switch bit `h`, and none
is what grows `wt(Φ_n h)`. The surviving witness `h=1^{m/2}0^{m/2}` is balanced
*and* maximally anti-dyadic, yet collapses to `wt=1` at power-of-two length
(`dyadic-halfstep-fold-power2-collapse`). So `ν₂ ≥ c·n` for the primes is
**irreducibly arithmetic**, not structural.

1. **Universal F₂ transfer** `ν₂ ≥ c·w` — refuted: consecutive odds
   (`h=all-ones`) has maximal `w` yet `ν₂=0` (`g-supply-transfer-universal-refuted`;
   kernel of `Φ_n` = span(all-ones)).
2. **Non-concentration** (no long constant runs) — refuted as a constraint:
   the consecutive-odds killer has no large gaps at all.
3. **Aperiodicity via Thue–Morse** — known, and known-insufficient: Thue–Morse
   is aperiodic with `ν₂=O(log n)` (`thue-morse-sublinear-supply-witness`), so
   aperiodicity cannot bridge to the primes. (Note: the right statistic is the
   **suffix** fold = `ν₂`; the prefix subset-zeta is a different, BCZ
   left-edge operator. Convention fixed as `suffix-fold-equals-nu2-prefix-does-not`.)
4. **Anti-dyadicity (half-step)** — refuted: `1^{a}0^{a}` with `a=2^b` is
   maximally far from every `2^k`-periodic string yet reaches fold weight 1
   (`spad-nondegenerate-linear-refuted`, `dyadic-halfstep-fold-power2-collapse`).
   And the prime switch bit is proved **not** eventually periodic
   (`spad-prime-anti-dyadic-proved`), but since the anti-dyadic converse is
   dead, aperiodicity is inert for supply.
5. **Dyadic periodicity collapse** — proved (`dyadic-collapse-proved`: period
   2^k ⟹ `ν₂=O_k(1)`), but it is the *collapse* half; the odd-factor converse
   (`ν₂≥c·n` on odd periods) is numerically confirmed on periodic words yet does
   not transfer to the aperiodic primes.

The dyadic skeleton is closed: `SPAD-linearization` discharged,
`SPAD-dyadic-collapse` discharged, `SPAD-anti-dyadic-linear` REFUTED,
`SPAD-prime-anti-dyadic` proved-but-inert. The route delivers nothing toward an
unconditional supply bound — that is the honest negative result.

## What the odd-period family genuinely gives (checked, conjectured)

Independently re-verified this attempt from scratch (no lib imports,
`code/out/deliverable_supply_check.py`, captured, EXIT_CODE=0): on the
2-then-odds sequence from an odd-period tail-1 word, `ν₂(n)` is **per-residue
affine** mod the (extended) period, min per-residue constant `c_r ≥ 2`, i.e.
positive **linear** supply on every odd-period tail-1 word:

- P=3: `ν₂(n) = 2·floor(n/3) + offset_r`, offsets `{-2,-2,+1}`, sum slope 2/3 —
  matches the infimum-bounded figure. **Correction:** the earlier literal closed
  form `2·floor((n−1)/3)` is wrong (fails all residues 1,2 mod 3; right form is
  `2·floor(n/3)+offset_r`).
- Mersenne P=7: affine constants `c_r=[2,2,6,4,4,2,4]`, `Σc_r=24=3^3−3` —
  matches the Mersenne recursion claim.

This is periodic-family only, so it does **not** close G-supply for the
aperiodic primes. And even the linear families weaken as the period grows:
Mersenne density `(3^k−3)/(2^k−1)^2 → (3/4)^k`, so supply density tends to 0 as
the period grows — the sharpest version of the run's recurring fragility.

## Status summary

- **Proved + Lean-formalised (sorry-free):** the reduction; the
  descent/absorption lemma (Branch A/B case split); the composition; the block
  lemma (constant 1); the step law + recharge identity; Rule 90 interior; edge
  invertibility; `spad-prime-anti-dyadic` (negative).
- **Verified from scratch this attempt (0 violations):** worked rows
  A_1..A_3 reproduced; 60/60 second entries in {0,2}; descent biconditional on
  real diagonals. Per-residue affine supply on odd-period words + Mersenne sum.
- **Open (named):** the unconditional linear supply bound `ν₂ ≥ c·n` (the
  two-point mod-4 switch correlation), `abgs-2011-s9-mod4-switch-limit-open`.

**Gilbreath's conjecture is NOT proved by this run.** It is reduced, with a
machine-checked core, to a single named-open arithmetic hypothesis.

## Files

- `code/out/deliverable_backbone_check.py` + `.captured.txt` (this attempt)
- `code/out/deliverable_supply_check.py` + `.captured.txt` + `.notes.md` (this attempt)
- `code/lean/descent_lemma.lean`, `link_a.lean`, `lemma54_even_domain.lean`,
  `gilbreath_reduction.lean` (Lean, sorry-free)
- `research/notes/lemma54-descent-proof-repaired.md`
- `research/notes/dyadic-oddfactor-affine-modulus-lifting.md`,
  `research/notes/mersenne-nu2-affine-selfsimilar-recursion.md`
