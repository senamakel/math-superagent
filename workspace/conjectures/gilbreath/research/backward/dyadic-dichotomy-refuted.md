# Supply bound via the dyadic dichotomy — REFUTED (the converse is dead)

This file does **not** restate Route B and does **not** propose a fourth supply
decomposition. It corrects the ledger: the skeleton
`dyadic-periodicity-collapse.md` was still marked `live` with three "open" gaps,
but two of those three are already settled — one **proved** and one **refuted**
— and the refutation kills the skeleton's inference outright. The point of this
file is to stop a forward attempt from spending a turn on a lemma the run's own
claims already falsify.

## What the dyadic skeleton claimed, and what is actually true

The dyadic skeleton (`dyadic-periodicity-collapse.md`) inferred the supply bound
`ν₂(q_n) ≥ c·n` from four steps: linearization, **dyadic collapse**, **the
converse (kernel classification)**, and prime anti-dyadicity. The inference runs
"collapse + its converse + prime-anti-dyadic ⟹ supply". The converse is the
load-bearing step, and it is false.

**Collapse (proved).** `h` eventually `2^k`-periodic ⟹ `ν₂(q_n) = O_k(1)`. This
is `dyadic-collapse-proved` (sharp: `ν₂ ≤ N0 + 2^k`, attained by the word
`0…01`). It survives and is a genuine artifact. It explains both recorded
counterexamples (consecutive odds, alternating 2/4).

**Converse (refuted).** The claimed converse — *sublinear `wt(Φ_n h)` forces `h`
within `o(n)` of a `2^k`-periodic string* — is false, on two independent
witnesses:

1. **Half-step strings** `h = 1^{m/2} 0^{m/2}` (Directive 68): balanced and
   dyadically aperiodic, yet `wt(Φ h) = 1` exactly, so `wt/m → 0`
   (0.125@8, 0.0625@16, 0.0833@24, 0.0313@32;
   `dyadic_halfstep_large.captured.txt`). This is the cleaner witness: it is
   exact, not a measurement.

2. **Thue–Morse** `h[j] = wt(j) mod 2`: **aperiodic**, in fact at Hamming
   distance exactly `n/2` from every `2^k`-periodic string (for fixed `k`: over
   `j ∈ [0, 2^k)` the pair `(h[j], h[j+2^k])` contains one 0 and one 1, while a
   `2^k`-periodic string repeats one value, so exactly half the positions
   disagree — linear, not `o(n)`). Its driven triangle has **sublinear** `ν₂`:
   measured `ν₂/n` collapsing `0.270 → 0.011`, max `ν₂ ≈ 219` over `n ≤ 4000`
   (`dyadic-separating-invariant-three-strings`). The exact `ν₂ = O(log n)`
   claim inside `thue-morse-sublinear-supply-witness` (status proved) is broken
   at its subset-zeta identification (`thue-morse-subset-zeta-confirmed-identification-refuted`
   — the fold bit marks cell parity, not `{0,2}` membership), so the sublinearity
   survives as an independent measurement, not a proof.

Either way the converse is not available to a proof of supply: it is refuted
numerically and decisively (witness 1 is exact), and the only *proof* of its
Thue–Morse witness offered so far is broken. Aperiodicity / anti-dyadicity of
`h` does **not** force linear supply. The dyadic dichotomy is one-sided: collapse
is proved, the converse is dead.

## Consequence

The unconditional prime-free dyadic route contributes **no further reduction** to
the supply bound. Proving `DPC-prime-antidyadic` (the primes are not `2^k`-periodic)
would still not give `ν₂ ≥ c·n`, because the converse it was bought to contradict
is false.

What survives toward the goal:

- the collapse direction `dyadic-collapse-proved` (a real proved artifact, no
  supply bound);
- the **conditional** route `nu2-supply-concentration-split.md`, whose
  combinatorial half `CT-concentration` is attackable today independently of the
  named-open suffix length, and whose number-theoretic half `CT-suffix-length`
  is the honest named-open content (`abgs-2011-s9-mod4-switch-limit-open`);
- the bounded-intruder measurement `REG-intruder-sharp-bound` on the
  regeneration side.

```skeleton
goal: For the prime sequence, ν₂(q_n) ≥ c·n for an absolute c > 0 and all sufficiently large n
      (SC-supply-nu2-linear), equivalently — via the discharged runway — Gilbreath's conjecture.
implies: |
  (0) LINEARIZATION [discharged]  ν₂(q_n) = wt(Φ_n h), h the mod-4 switch bit
      (rule90-interior-xor, proved; ancestor-window interval verified).

  (1) COLLAPSE [discharged]  h eventually 2^k-periodic ⟹ ν₂(q_n) = O_k(1).
      Proved prime-free: dyadic-collapse-proved (ν₂ ≤ N0 + 2^k).

  (2) CONVERSE [refuted]  sublinear ν₂ ⟹ h within o(n) of a 2^k-periodic string.
      FALSE on two independent balanced, dyadically-aperiodic witnesses: (i) half-step strings
      h = 1^{m/2} 0^{m/2} give wt(Φh) = 1 exactly, wt/m → 0 (dyadic_halfstep_large.captured.txt,
      Directive 68); (ii) Thue–Morse h[j] = wt(j) mod 2 is aperiodic with measured ν₂/n collapsing
      0.270 → 0.011, max ν₂ ≈ 219 over n ≤ 4000 (dyadic-separating-invariant-three-strings). The
      O(log n) proof once attached to Thue–Morse (thue-morse-sublinear-supply-witness) is broken at
      its exact identification (thue-morse-subset-zeta-confirmed-identification-refuted), so the
      sublinearity survives as a measurement, not a proof.

  (3) PRIME ANTI-DYADICITY [open, but vacuous]  the prime h is not asymptotically 2^k-periodic.

  THE INFERENCE THAT DIED:  (2)+(3) ⟹ supply. Since (2) is false, the dyadic dichotomy does
  not reduce the supply bound: aperiodicity of h is NOT sufficient for ν₂ ≥ c·n.

  CONCLUSION: the dyadic axis contributes no further reduction to SC-supply-nu2-linear. The
  surviving reductions are the conditional route (nu2-supply-concentration-split: CT-concentration,
  attackable, + CT-suffix-length, named-open) and the regeneration route. Nothing here re-opens
  the discharge of the collapse direction or resurrects the refuted converse.
status: broken
killed-by: SPAD-anti-dyadic-linear / DPC-kernel-classification — the converse on which the dyadic
  inference rested is refuted by two independent balanced aperiodic witnesses with sublinear
  supply: half-step strings h=1^{m/2}0^{m/2} (wt(Φh)=1, dyadic_halfstep_large.captured.txt) and
  Thue-Morse (measured ν₂/n → 0, dyadic-separating-invariant-three-strings). Aperiodicity does not
  force ν₂ ≥ c·n, so the dichotomy yields no supply bound.
rests-on: rule90-interior-xor, dyadic-collapse-proved, thue-morse-sublinear-supply-witness,
  thue-morse-subset-zeta-confirmed-identification-refuted, dyadic-separating-invariant-three-strings,
  gilbreath-reduces-to-second-in-02, abgs-2011-s9-mod4-switch-limit-open
```

```gap
id: DPC-dyadic-collapse
lemma: If h is eventually periodic with period 2^k (k ≥ 0), then ν₂(q_n) = wt(Φ_n h) = O_k(1).
status: discharged
discharged-by: dyadic-collapse-proved (proved, prime-free; sharp bound ν₂ ≤ N0 + 2^k, attained by 0…01)
next: none — restating this as open re-opens a proved claim.
```

```gap
id: DPC-kernel-classification
lemma: (Converse of the collapse.) sublinear wt(Φ_n h) forces h within o(n) of a 2^k-periodic string.
status: refuted
discharged-by: (refuted, not discharged) half-step strings h=1^{m/2}0^{m/2} give wt(Φh)=1 exactly
  (dyadic_halfstep_large.captured.txt); Thue–Morse gives measured sublinear ν₂
  (dyadic-separating-invariant-three-strings). Both balanced and dyadically aperiodic.
next: none — any repair needs an extra hypothesis the collapse proof does not require, and without it
  the dichotomy yields no supply bound. Do not re-attack this lemma in this form.
```

```gap
id: DPC-prime-antidyadic
lemma: The prime mod-4 switch bit h is not asymptotically periodic with period a power of 2
  (quantitatively: for each k, h|[1,n] stays ≥ δ_k·n Hamming-far from every 2^k-periodic string).
status: open
next: |
  NOTE: this lemma no longer closes anything toward GC — the inference that used it is refuted at
  the converse. It is kept open only as a cheap, likely provable prime statement. First move
  (tool_builder): compute the Hamming distance of h|[1,n] to the nearest 2^k-periodic string for
  k = 0..6, n up to 1e6 (sieve ≤ 1.6e7, O(n) memory), report distance/n. Expectation: distance/n
  stays near 0.4–0.6 (h is ~60% ones). If some k gives distance/n → 0, it is empirically refuted.
  Deprioritise behind CT-concentration and CT-suffix-length, which are the lemmas that actually
  move the goal.
thread: research/threads/dyadic-periodicity-collapse.md
```
