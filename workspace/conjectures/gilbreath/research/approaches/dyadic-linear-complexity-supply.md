```approach
idea: |
  The tail cells are the F₂ subset-zeta transform ζ(h)[d] = Σ_{j⊆d} h[j] (mod 2)
  of the mod-4 switch bit h, and ν₂(q_n) = #{d ≤ n : ζ(h)[d] = 1}. The F₂
  subset-zeta transform is an INVOLUTION (ζ∘ζ = id). Therefore ν₂ ≥ c·n ⟺ the
  zeta-dual ζ(h) has positive density — i.e. h is **dyadically non-rigid**. The
  supply bound is a statement about the 2-adic-spectral rigidity of h, NOT about
  periodicity, aperiodicity, or general linear complexity. Characterize the
  rigidity space {h : ζ(h) has density 0} and show the prime switch bit lies
  outside it.
mechanism: |
  Three facts, two held and one new, pin the structure; one held fact kills the
  naive reading.

  (1) [held, proved] rule90-interior-xor: the tail cell at depth d is
      ζ(h)[d] = Σ_{j⊆d} h[j] (mod 2) — the subset-zeta (Möbius) transform over
      F₂. So ν₂(q_n) = #{d : ζ(h)[d] = 1}.

  (2) [NEW, trivial but load-bearing] ζ is an INVOLUTION over F₂: Möbius
      inversion on the boolean lattice has μ(j,d) = (−1)^{|d|−|j|} ≡ 1 (mod 2),
      so the inverse of the subset-zeta transform equals the subset-zeta
      transform itself: ζ(ζ(h)) = h. (Consistent with, though not here shown
      identical to, bcz-2023-left-edge-stabilization's T² = id.)

  (3) [NEW, proved — research/notes/thue-morse-sublinear-supply-witness.md]
      The Thue–Morse string h[j] = wt(j) mod 2 has ζ(h)[d] = 1 ⟺ d is a power
      of two, so ν₂ = O(log n). By involution this is self-dual: the
      power-of-2 indicator 1_P and h = Thue–Morse are zeta-duals, since
      ζ(1_P)[d] = #{set bits of d} mod 2 = wt(d) mod 2 = h[d]. So the
      collapse class contains an APERIODIC, 2-automatic point — "aperiodic ⟹
      linear supply" is false.

  (4) [held, proved] dyadic-collapse-proved: h eventually periodic of minimal
      period 2^k ⟹ ζ(h) has finite support (≤ 2^k−1 points) ⟹ ν₂ = O_k(1).
      Finite support of ζ ⟺ dyadic periodicity (ζ(finite-support f) is
      eventually 2^k-periodic — this is the collapse theorem read through the
      involution).

  The CORRECT invariant, and the falsifier that forced it: the run's own
  `dyadic-oddfactor-infimum-bounded` shows period-3 h gives ν₂ ~ 0.647·n. A
  period-3 string is 2-automatic with bounded (indeed finite) linear complexity,
  yet its ζ has POSITIVE density. So "low linear complexity ⟹ collapse" is
  FALSE; general linear complexity does not separate the classes. What does: the
  2-adic spectral structure of the operator σ = I+S (S = 2-adic odometer shift).
  σ is nilpotent exactly on the dyadic (power-of-2-periodic) component
  (Frobenius: σ^{2^k} = 0 there), and has non-nilpotent eigenvalues on odd-
  length cyclic components. ν₂ ≥ c·n ⟺ h carries positive mass in σ's
  non-nilpotent part ⟺ h is **dyadically non-rigid**.

  Synthesis: supply ν₂ ≥ c·n ⟺ ζ(h) has positive density ⟺ h has positive
  2-adic non-rigidity. The two collapse witnesses (dyadic-periodic, Thue–Morse)
  are both dyadically rigid; the linear witnesses (odd-factor periods, random h,
  primes) are not. This gives a precise, prime-free reformulation of the supply
  step, with the obstruction class NAMED (dyadically rigid strings) rather than
  described as "periodic".
status: refuted
killed-by: |
  The load-bearing identity nu2 = #{d : zeta(h)[d] = 1} is the mod-4 parity
  count, not the exact {0,2} count: zeta(h)[d] fires on halved values odd
  (actual values 2, 6, 10, ...), not on cells exactly 2
  (thue-morse-sublinear-supply-witness; refutation of
  boolean-influence-parity-subset-density). The rigidity reformulation
  survives only as the parity half of the exact decomposition
  nu2 = F_diag - O; the magnitude half (overshoot O) is carried by the proved
  descent/excess machinery. Superseded by
  `overshoot-corrected-supply-weight` (adopted).
side: regeneration (supply side) — general-class / dynamical reformulation
named-mathematics: |
  Subset-zeta / Möbius transform over F₂ (an involution), Lucas' theorem,
  Rule 90 / Sierpinski / Pascal mod 2, 2-adic odometer spectral decomposition,
  2-automatic sequences (Christol), the BCZ left-edge F₂ involution.
speculative: |
  The positive direction — a clean characterization of the rigidity space
  {h : ζ(h) has density 0} and the inference "prime h ∉ rigidity space" — is
  CONJECTURED. Proved content: the collapse half (dyadic-collapse-proved), the
  involution (bcz), and the Thue–Morse witness (aperiodic + rigid ⟹ O(log n)).
  Do NOT claim this closes G-supply; it reframes the open step.
falsifier: |
  (a) An h that is dyadically non-rigid (e.g. positive mass on an odd-factor
      component) yet has ζ(h) of density 0 — would break the bridge in the
      collapse direction. (b) An h with ζ(h) of positive density whose
      ν₂ still fails ν₂ ≥ c·n for the needed c — would break the supply
      direction. The period-3 case (bounded LC, positive density) is NOT a
      falsifier; it is the clean witness that the invariant must be 2-adic
      rigidity, not linear complexity.
first-step: |
  (1) [tool_builder, today] Compute ζ(h) and its density ν₂(n)/n for the four
      corner families and confirm the dichotomy at the level of DENSITY OF ζ:
      collapse families (all-ones, alternating 2/4, period-4), Thue–Morse
      (density 0, proved), odd-factor periods P=3,5 (positive density,
      measured), Rudin–Shapiro (2-automatic; classify), pseudo-random h
      (density ~1/2), and the REAL prime switch bit (sieve ~1e6). Tabulate
      ν₂(n)/n. Cost O(n) per family, one row live, cheap. The conjecture being
      tested: density(ζ(h)) ∈ {0} ∪ {≥ c > 0}, i.e. no intermediate sublinear
      non-rigid point other than the dyadically rigid class.
  (2) [research, parallel] Pin the named theorem "the F₂ subset-zeta transform
      preserves 2-automaticity" (Christol / automatic-sequences literature):
      ζ is an F₂-linear substitution x ↦ x/(1+x) on the generating function, so
      it should preserve the class of 2-automatic (= algebraic over F₂[[x]])
      sequences. This is the load-bearing mechanism for turning "prime h is
      dyadically non-rigid" into a transferable statement.
```

## Corrected by `overshoot-corrected-supply-weight` (inventor converge, this round)

The load-bearing identity `nu2 = #{d <= n : zeta(h)[d] = 1}` is **refuted by
the run's own measurements**: `zeta(h)[d]` is the mod-4 parity bit, which fires
on halved values odd (actual values 2, 6, 10, ...), not on cells exactly 2
(`thue-morse-sublinear-supply-witness`; also the refutation of
`boolean-influence-parity-subset-density`). The fold bit therefore counts
`#{delta_k ≡ 2 (mod 4)}`, not `nu2`. The exact lift is
`nu2 = F_diag − O` with `O = #{k < tau : delta_k ≡ 2 (mod 4)}` (the cells
outside the maximal {0,2} suffix whose value is ≡ 2 mod 4), splitting into stray
2s and overshoot (≥ 6). This approach's "rigidity" reformulation survives as the
**parity half** of that decomposition; the magnitude half (the overshoot term O)
is carried by the proved descent/excess machinery, not by 2-adic rigidity. See
`research/approaches/overshoot-corrected-supply-weight.md` (adopted).