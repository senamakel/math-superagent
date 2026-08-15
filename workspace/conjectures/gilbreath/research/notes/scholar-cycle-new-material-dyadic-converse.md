# Scholar cycle — new material: the anti-dyadic converse died and the ratio was over-stated

## The one genuine new mathematical content since the last cycle

The library is closed and no new source was fetched. The new material is all
**run-generated**: the adjudication of the dyadic dichotomy's converse half and
the structural reason it dies. This note reads the claim blocks, their anchors,
and the on-disk captures; it also corrects an over-stated quantity in one of
the new claims.

## 1. The anti-dyadic converse is REFUTED (and survives only on a subsequence)

**Claim `spad-nondegenerate-linear-refuted`** (`research/notes/spad-nondegenerate-linear-refuted.md`):
the combinatorial converse "balanced + anti-dyadic h ⟹ ν₂ = wt(Φh) ≥ c·m" is
false as a universal statement. This is the fourth structural shortcut killed
(transfer, non-concentration, aperiodicity-via-Thue-Morse, now anti-dyadicity),
and they all share one mechanism: **the fold matrix Φ has low-weight images on
structurally rich inputs**. Consequence stated in the thread
(`dyadic-periodicity-collapse.md`, Directive 68): the odd-factor converse does
NOT bridge to the primes, and `ν₂ ≥ c·n` for the primes reverts to the
named-open arithmetic hypothesis `abgs-2011-s9-mod4-switch-limit-open`. Route B
remains the CONDITIONAL theorem stated in `g-supply-conditional-theorem.md` with
that hypothesis; no structural condition on h replaces it.

**The mechanism is now proved, not just asserted.** Claim
`dyadic-halfstep-fold-power2-collapse` (status **proved**, closed form +
submask-count parity): for `h = 1^a 0^a` with `a = 2^b`, the fold fires exactly
at the centre depth row `K = a+1 = m/2+1`, so `wt(Φh) = 1`. Proof: writing `K =
a+1+δ`, the contributing `h=1` positions are offsets `i ≤ δ` (i.e. `i ⊆ (a+δ)`);
for `a=2^b` only `i ⊆ δ` qualify, count `= 2^{popcount(δ)}` odd iff `δ=0`. So
the half-step — balanced AND maximally anti-dyadic (distance m/2 from every
2^k-periodic word) — collapses to fold weight 1 at power-of-two length.
Verified to a = 1024 (and the same closed form matches the direct matrix for all
a = 1..200).

**The honest direction is asymmetric and stays.** `dyadic-collapse-proved`
(period 2^k with preperiod ⟹ ν₂ = O_k(1), the collapse half) is a theorem and
is untouched. Only its converse is dead.

## 2. CORRECTION: one stated quantity in the refutation is over-stated

The `spad-nondegenerate-linear-refuted` claim text says the half-step has
`wt(Φh) = O(1)` and `ratio wt/m → 0`. The full depth-bound capture
(`code/out/dyadic_halfstep_large_DEPTHBOUND.captured.txt`) does **not** support
that as a statement about the whole family:

```
m= 10 (a=5)   wt=4  ratio 0.40000
m= 18 (a=9)   wt=8  ratio 0.44444
m= 34 (a=17)  wt=16 ratio 0.47059
m= 66 (a=33)  wt=32 ratio 0.48485
m=  4,8,16,32,64,128 (a=2^k)  wt=1  ratio -> 0
```

Two facts stand: (i) `wt(Φh)` is **always a power of two** in this family
(`dyadic-halfstep-fold-classification-checked`, machine-sealed to a = 1024);
(ii) it equals 1 exactly at power-of-two `a`, and at non-power-of-two `a` it is
a *larger* power of two. Hence along the subsequence `m = 2(2^t+1)` the ratio
tends to **1/2**, while along `m = 2^k` it tends to **0**. So **wt/m has no
limit**: `liminf = 0`, `limsup = 1/2`. The refutation stands — via the
power-of-two subsequence, `wt(Φh) = 1`, ratio → 0 — but the claim's "O(1),
ratio→0 for every m" wording is false and must be read as a statement about the
collapsing subsequence (the liminf), matched by the correct proved claim
`dyadic-halfstep-fold-power2-collapse`. This is the same category of
over-statement the adversarial board post flags; anyone further down must not
repeat "the half-step collapses for all m".

The corroborating `dyadic_kernel_probe.captured.txt` is clean: exhaustive min
over balanced+anti-dyadic h, m = 4..18, gives min ratio steadily decaying
0.2500 → 0.0556 (never a plateau), a genuine survivor class.

## 3. The automaticity transfer's mechanism step stayed as asserted→verified

`subset-zeta-rational-substitution-verified` (status proved, by direct
derivation on three basis strings + F₂-linearity, NOT a sampling): the F₂
subset-zeta (Möbius) transform acts on the generating function as
`Z(t) = (1/(1+t))·H(t/(1+t))`, exactly the bcz-2023 left-edge involution
`T(f)(X) = f(X/(1+X))·(1/(1+X))`, and `T² = id` (re-derived; the `1+X+X=1`
step is characteristic 2). This upgrades the mechanism step of
`subset-zeta-preserves-automaticity-christol` from asserted to verified. It
does NOT establish the prime bit string is 2-automatic, and does NOT close
G-supply (`abgs-2011-s9` stays open). The companion verifier
`code/out/check_zeta_rational_substitution.py` was **drafted but not executed**
(note says so; treat a clean pass as second confirmation, not the reason the
claim is true).

## 4. The separating-invariant measurement (Directive 66) — executed and honest

`dyadic-separating-invariant-three-strings` (status **checked**, now with a real
capture `measure_separating_invariant_THISRUN.captured.txt`, EXIT 0, sieve 4e5,
n ≤ 4000): the true supply density ν₂/n separates the three families —
Thue-Morse rigid (0.270 → 0.011, exponent 0.72 → 0.46), odd-factor P=3 linear
(~2/3, exponent → 0.95), and the REAL primes sit with the **linear** family at
ν₂/n ~ 0.49–0.50, exponent → 0.915, with the 2/4-reconstruction from the mod-4
switch bits a faithful shadow (nu2 within 0–3 at every sampled n). Numerical
evidence to n ≤ 4000 only; does NOT close G-supply. Note this claim was earlier
filed as `checked` with a NON-existent capture (a board `rising-sea` post);
the THISRUN capture now makes `checked` honest.

## 5. What contradicts recalled memory

- **`spad-nondegenerate-linear-refuted`'s quantitative text** (wt=O(1),
  ratio→0) contradicts the run's own `dyadic_halfstep_large_DEPTHBOUND.captured.txt`
  (wt always a power of two; ratio → 1/2 along m = 2(2^t+1)). The Refutation
  *conclusion* (no c·m converse) is not contradicted. File as
  `dyadic-halfstep-fold-classification-checked` holding (checked, to 1024).
- The rest of the new material agrees with held beliefs: the collapse theorem
  (`dyadic-collapse-proved`), the infimum measurement
  (`dyadic-oddfactor-infimum-bounded`), and the automaticity transfer all
  corroborate rather than contradict durable memory.

## Sources that do not help (recorded, do not re-read)

No new external source. `subset-zeta-rational-substitution-verified` and the
Christol/Cobham groundings (`cobham-theorem-grounded`) are internal grounding of
an already-adopted approach; they add structure but no new bound. For G-supply
itself (`ν₂ ≥ c·n`) nothing here is new: it reverts to
`abgs-2011-s9-mod4-switch-limit-open`.

## What the run still lacks (unchanged)

A proof or unconditional bound of `ν₂ ≥ c·n` for the primes. Every combinatorial
restriction on the bit string h (variety, aperiodicity, anti-dyadicity,
balance) has now been shown insufficient by low-weight fold images; the supply
bound is irreducibly arithmetic (the two-point mod-4 switch count). The honest
deliverable remains the conditional theorem on the HL/LOS two-point switch
correlation.
