# Christol–Cobham inverse theorem, corrected: the rigidity dichotomy of the F2 fold

```approach
idea: |
  Prove the STRUCTURE THEOREM for low-weight preimages of the Pascal/Rule-90
  F2 fold Φ_n — the open, unclaimed inverse question — but with the target
  class corrected away from periodicity/automaticity, which the run's own
  ledger has already bracketed false. The correct statement is the RIGIDITY
  DICHOTOMY: every h ∈ {0,1}^ℕ satisfies either

      ν₂(n) = o(n)   (h dyadically rigid)      or     ν₂(n) ≥ c·n   (h non-rigid)

  for a universal c > 0, where rigidity is detected by the 2-adic spectrum of
  the odometer operator σ = I + S (S = the 2-adic shift, σ^{2^k} = I + S^{2^k}
  by Frobenius), which is nilpotent exactly on the dyadic component. Christol's
  theorem (algebraic ⇔ q-automatic) and Cobham's theorem (p/q-automatic
  rigidity) enter ONLY as the tool for the 2-AUTOMATIC SUBCLASS of the rigid
  side — a clean, provable lemma — not as the characterization.
mechanism: |
  ν₂(q_n) = wt(Φ_n h) = #{d ≤ n : ζ(h)[d] = 1}, where ζ is the F₂
  subset-zeta transform ζ(h)[d] = ⊕_{j⊆d} h[j] (rule90-interior-xor, proved).
  ζ is an INVOLUTION (Möbius over F₂ has μ ≡ 1, so the inverse of the subset
  zeta equals the subset zeta itself). Hence the rigid class is exactly

      { h : ζ(h) has density 0 } = ζ( { f : f has density 0 } )

  — a tautology via the involution, and a class in bijection with ALL
  density-0 sets. Two established witnesses pin down where automaticity sits
  relative to this class:

  (1) Thue–Morse h (2-automatic, APERIODIC): ζ(h) = indicator of powers of 2,
      density 0, so ν₂ = O(log n). Rigid. Hence "low weight ⟹ near 2^k-periodic"
      is FALSE — the naive inverse theorem in the original proposal.
  (2) Period-3 h (2-automatic: the 2-kernel of a period-p word has ≤ p states):
      ζ(h) has density ≈ 0.647, so ν₂ ≈ 0.647 n. Non-rigid. Hence
      "2-automatic ⟹ rigid" is FALSE — the automaticity "correction".

  So the rigid class is NOT a subset of the 2-automatic class and the
  2-automatic class is NOT a subset of the rigid class. Automaticity is the
  wrong invariant; the correct one is the σ = I+S spectral decomposition:
  σ is nilpotent on the dyadic (2^k-periodic) part and invertible on odd
  cyclic parts. The conjecture that matters — and that is genuinely open and
  unclaimed — is that the dichotomy above holds, with

      rigid  ⟺  h carries mass only on the σ-nilpotent (dyadic) part.

  Christol/Cobham enter as the clean lemma for the 2-automatic subclass:
  a 2-automatic h has a finite 2-kernel, so its σ-action is finite-state, and
  Cobham rigidity then yields that an automatic h is rigid iff its σ-action is
  nilpotent. This is provable today; it does not characterize the whole rigid
  class, and it does not by itself close G-supply (the prime switch bit is NOT
  2-automatic — Hartmanis–Shank; binary-carry-transducer-automatic-sequence
  refuted on exactly this).
status: adopted
side: regeneration (supply side) — general-class structure theorem; the prime
  leg stays the named-open two-point mod-4 hypothesis
precedent: |
  - Christol's theorem (algebraic formal power series over F_q ⇔ q-automatic
    coefficient sequence), Christol 1979; Christol–Kamae–Mendès France–Rauzy
    1980; Allouche–Shallit Thm 12.2.5; quantitative Adamczewski–Bostan–Caruso
    2023 (arXiv:2306.02640).
  - Cobham's theorem: p- and q-automatic with log p / log q ∉ Q ⟹ ultimately
    periodic — the finite-state rigidity tool for the automatic subclass.
  - The specific inverse theorem "sublinear fold weight ⟹ structured input" is
    ABSENT from the literature (deep search of linear-CA preimage rigidity,
    Rule-90 measure rigidity, Pascal matroid, low-weight codeword rigidity:
    Takei 2017; Mariot–Leporati 2016; Fukś 2003; Barbé 2000 — none states it).
    The QUESTION is open and unclaimed; this run owns the correct formulation.
  - Run's own bracketing witnesses (decisive corrections the original proposal
    missed): thue-morse-sublinear-supply-witness (proved: aperiodic 2-automatic
    rigid, ν₂ = O(log n)); dyadic-oddfactor-infimum-bounded (measured: period-3
    gives ν₂ ≈ 0.647 n, non-rigid); dyadic-collapse-proved (2^k-periodic ⟹
    finite support ⟹ rigid); transfer-matrix-kernel-allones (ker Φ_n =
    span(all-ones)); rule90-interior-xor (fold = subset-zeta).
  - Decisive caveat on the payoff (research, correct): the anti-dyadic
    hypothesis on the prime switch bit is a TWO-POINT consecutive-pair mod-4
    statistic; Siegel–Walfisz (one-point) does not imply it. So the prime leg
    is the ABGS-open kind of quantity, not Siegel–Walfisz-reachable.
named-mathematics: |
  F₂ subset-zeta / Möbius transform (an involution), Lucas' theorem /
  Rule 90 / Pascal mod 2, 2-adic odometer spectral decomposition (σ = I+S,
  Frobenius), Christol's theorem, Cobham's theorem, the 2-kernel
  (Allouche–Shallit).
speculative: |
  The DICHOTOMY (no intermediate sublinear non-rigid h) and the spectral
  characterization "rigid ⟺ σ-nilpotent" are CONJECTURED — exactly the open
  converse `DPC-kernel-classification` of the dyadic-periodicity-collapse
  thread, here given (a) its correct invariant and (b) Christol/Cobham as the
  automatic-subclass tool. Proved so far: collapse half (dyadic-collapse-proved),
  involution, Thue–Morse witness. Do NOT claim this closes G-supply.
falsifier: |
  (a) An h with ν₂(n)/n → 0 (rigid) that carries positive mass on an
      odd-factor (non-nilpotent) σ-component — breaks the spectral
      characterization. (b) An h with ν₂(n)/n decaying to 0 along a
      subsequence but ≥ c > 0 along another (no dichotomy — intermediate
      sublinear). (c) The odd-factor density gate (below) returning a
      DECAYING infimum: the dichotomy is true but USELESS for supply (only
      linear ν₂ ≥ c·n feeds Granville's Lemma 5.4). Period-3 (2-automatic,
      non-rigid) and Thue–Morse (2-automatic, rigid) are NOT falsifiers — they
      are the witnesses that force the invariant to be σ-spectrum, not
      automaticity.
first-step: |
  tool_builder, TODAY (O(n) per family, one row live, n ≤ 20000, cheap;
  report every number, never "theorem"):
  (1) Run the drafted gate `code/out/dyadic_oddfactor_density.py` (write it if
      absent): for odd-factor periods P = 3,5,7,9 compute ν₂(n)/n for n to
      20000 and report inf_n ν₂(n)/n and the argmin. A positive infimum anchors
      the odd-factor converse; a decaying infimum kills the supply usefulness.
  (2) Classify the corner families by 2-KERNEL SIZE (finite ⟺ 2-automatic,
      Christol): dyadic-periodic 2^k, Thue–Morse, period 3/5/7/9,
      Rudin–Shapiro, pseudo-random h, and the real prime mod-4 switch bit
      (sieve ~1e6). Tabulate (2-kernel size, inf ν₂/n) per family and check
      the corrected dichotomy: the rigid set (inf → 0) should be detected by
      σ-nilpotence, NOT by finite 2-kernel. Report CONFIRMED/REFUTED against
      the dichotomy, with the exact infimum.
  (3) [theorem_prover, parallel] attempt the automatic-subclass lemma: a
      2-automatic h is rigid iff its σ-action is nilpotent (finite 2-kernel +
      Cobham). This is the provable residue that survives both bracketing
      witnesses.
```

## Why the original proposal had to be corrected before adoption

The proposal's load-bearing claim was "sublinear wt(Φ_n h) forces h to be
within o(n) of a 2^k-periodic word", proved via `(1+X)^{2^m} = 1+X^{2^m}`
and Christol/Cobham. That claim is FALSE on the run's own ledger, in both
directions:

- **Thue–Morse** (`thue-morse-sublinear-supply-witness`, status proved):
  `h[j] = wt(j) mod 2` is 2-automatic and aperiodic, yet `ζ(h)[d] = 1 ⟺ d`
  is a power of 2, so `ν₂ = O(log n)`. A rigid, aperiodic, 2-automatic
  point. The dyadic-collapse direction is the *only* periodicity fact that
  survives: `2^k`-periodic ⟹ finite support ⟹ rigid.
- **Period-3** (`dyadic-oddfactor-infimum-bounded`, status checked): a
  period-3 word is 2-automatic (2-kernel of size ≤ 3), but `ν₂ ≈ 0.647 n`.
  Automaticity does not force rigidity.

So neither "rigid ⟹ near-periodic" nor "rigid ⟹ 2-automatic" holds, and
"2-automatic ⟹ rigid" fails. Christol/Cobham classify the 2-automatic
sequences; the rigid class is `ζ({density-0})`, a strictly larger and
spectrally-defined object. The automaticity toolset is demoted to the
automatic-subclass lemma and the invariant corrected to `σ = I+S`.

## Why this is not on disk (and how it relates)

- **Not `f2-uncertainty-dyadic-spectral-mass`** (refuted): that used a
  Donoho–Stark uncertainty principle and died on `ker Φ_n = span(all-ones)`.
  This proves a structure theorem, no spectral inequality.
- **Not `nu2-code-minimum-distance`** (refuted): that asked about the image
  code (trivial, full space). This asks about PREIMAGES of the low-weight
  region — non-trivial because the fold is surjective but its low-weight
  preimages are structured.
- **Not `odometer-disjointness-subshift`** (refuted): that attacked the prime
  bit via ergodic disjointness. This attacks the FOLD via the σ = I+S spectrum
  and automaticity.
- **Subsumes and sharpens the already-adopted `dyadic-linear-complexity-supply`**:
  that entry named ζ (involution) and the 2-adic odometer spectral
  decomposition but left the dichotomy as "conjectured" and queued
  "ζ preserves 2-automaticity" as an open research step. This entry adds the
  *correct* observation that automaticity is provably not the invariant
  (Thue–Morse / period-3), the precise dichotomy theorem statement, and
  Christol/Cobham as the concrete tool for the automatic subclass.
- **Relation to the live thread `dyadic-periodicity-collapse`:** this is the
  corrected, named-tool attack on its open converse `DPC-kernel-classification`,
  with the first step being exactly the Directive 64 density gate the thread
  has queued three times unrun.
