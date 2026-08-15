# ν₂ supply via odometer disjointness and entropy of the mod-4 switch-bit subshift

```approach
idea: Treat the mod-4 switch bit h as an orbit of the 2-adic odometer, and the ν₂ fold Φ as a Birkhoff average over that odometer action. If the orbit closure of the prime h is a subshift disjoint from the odometer (Furstenberg disjointness), the averages are generic and ν₂ ≈ w/2. Positive entropy of the subshift is the named mechanism forcing disjointness from the rigid odometer.
mechanism: |
  ν₂(q_n) = wt(Φ_n h) as a sum over the "Pascal/odometer orbit" of h. The
  proposal asserts: positive entropy of the orbit closure X_h forces
  disjointness from the rigid odometer, and disjointness forces the Birkhoff
  averages to the uncorrelated value, giving ν₂ ≥ c·w.
status: refuted
killed-by: (a) positive entropy does NOT force disjointness from the odometer; (b) the linear-algebra object that kills the uniform bound is not an odometer orbit either.
  (a) THE NAMED MECHANISM IS WRONG. The deep research confirms: positive
      entropy alone does NOT guarantee disjointness from the 2-adic odometer
      (which is zero-entropy, rigid, equicontinuous/rotation-type). The correct
      sufficient classes are: ZE^⊥ = K-automorphisms (disjoint from ALL
      zero-entropy systems, Furstenberg 1967 + Lemańczyk–Parreau–Thouvenot +
      Sinai), and Milly-mixing ⟂ Rigid (Furstenberg–Weiss). The odometer is
      RIGID, so a subshift is disjoint from it if (and essentially only if) the
      subshift is MILDY MIXING. Positive entropy ≠ mild mixing; and mild mixing
      is a strictly strong, deep property. So "IF X_h has positive entropy THEN
      ν₂ ≥ c·w" rests on a false implication; the correct hypothesis would be
      mild mixing (or the odometer not being a factor of X_h), which is a
      number-theoretically deep claim about the prime bit, NOT a clean
      bit-string property. Real references: Furstenberg, "Disjointness in
      ergodic theory" (Math. Systems Theory 1 (1967)); "Joining properties of
      automorphisms disjoint with all ergodic systems" (ETDS 2024,
      doi:10.1017/etds.2024.129): ZE^⊥ = K-automorphisms; rigid ⟂ mildly-mixing;
      Moreira, "Disjointness for measurably distal group actions" (ETDS 2022).
  (b) THE BIRKHOFF/ODYOMETER READING OF Φ_n IS ALSO OFF. ν₂ = wt(Φ_n h) is a
      deterministic finite matrix-fold of a FIXED window [2,n−1], not a
      Birkhoff average along an odometer orbit of h; and the "collapse" that
      makes the uniform bound fail is the SINGLE all-ones vector in ker Φ_n
      (`transfer-matrix-kernel-allones`), not a rigidity/odometer-factor
      property. Weakening to a conditional theorem does not help: the unproved
      hypothesis is a density/measure claim about consecutive-prime mod-4
      pairs, exactly the two-point correlation `abgs-2011-s9-mod4-switch-limit-open`
      shows is open — the ergodic repackaging adds no unconditional content.
      The one genuinely transferable lesson (shared by the subadditive-growth
      thread) is that the bit string's factor counts / complexity are cheap to
      measure, but they cannot be turned into a supply bound without a deep
      two-point prime hypothesis.
precedent: |
  Furstenberg disjointness (1967); ZE^⊥=K-automorphisms (Lemańczyk–Parreau–
  Thouvenot, Sinai); rigid ⟂ mildly mixing (Furstenberg–Weiss); Berk–Górska–
  de la Rue, "Joining properties of automorphisms disjoint with all ergodic
  systems" (ETDS 2024, doi:10.1017/etds.2024.129); Moreira (ETDS 2022);
  Sarnak-Möbius disjointness for bijective substitutions (zero-entropy, the
  opposite regime from what is needed). None applies odometer disjointness to
  Gilbreath's supply; consistent with `block-growth-literature-not-covered`.
first-step: (was) estimate factor counts/entropy of the prime h — cheap and real, but does
  NOT yield the supply bound even when it works, because the correct disjointness
  hypothesis is mild mixing, not positive entropy.
side: regeneration (supply side)
named-mathematics: subshifts, measure-theoretic entropy, the 2-adic odometer, Furstenberg disjointness, minimal self-joinings, Birkhoff ergodic theorem
speculative: (moot) that X_h carries an ergodic measure with the needed property.
falsifier: (mechanism-level fatal) a positive-entropy subshift NOT disjoint from the odometer — which exists (positive entropy does not imply mild mixing).
```
