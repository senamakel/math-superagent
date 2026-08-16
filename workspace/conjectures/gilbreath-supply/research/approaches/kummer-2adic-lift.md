# Lift the fold from F2 to the 2-adics: Kummer/Granville reads gap magnitudes

```approach
idea: >
  The linearisation ν₂(n) = wt(Φ_n h) already computes the count of 2s, but
  only as a weight of an F2-linear image: it reads the primes through the
  single coordinate h[j] = (gap_j/2) mod 2 and throws away every higher bit of
  the gap magnitude. Lift the triangle itself to the 2-adics. The cells of the
  {0,2} suffix are exactly the cells with 2-adic valuation ≥ 1; a "2" is
  v₂(cell) = 1 and a "0" is v₂(cell) ≥ 2. The absolute-difference operation
  satisfies the ultrametric law |a−b|₂ ≤ max(|a|₂, |b|₂), with strict inequality
  exactly when v₂(a) = v₂(b) (cancellation), so the valuation of every cell of
  the triangle is computed by a carry-type propagation from the initial gap
  valuations v₂(q_{j+1}−q_j). Kummer's theorem v₂(C(d,i)) = (number of carries
  in adding i and d−i in base 2), and Granville's Zaphod-Beeblebrox mod-p
  binomial structure already on disk (claims bacher-pascal-det-mod2,
  hofer-mod2-pascal-thue-morse-structure), make this propagation explicit as a
  binomial fold. This exposes the 0-vs-2 status of each individual cell —
  governed by the 2-adic valuations of the prime gaps — an arithmetic input
  about gap magnitudes that the switch-density reduction (pure mod 4) and the
  F2 fold (pure gap parity) both cannot see. The F2 fold is the mod-2 shadow of
  this valuation propagation; the lift is a different proof route to the same
  lower bound, via an invariant the closed doors never touch.

mechanism: >
  In the absolute-difference triangle a cell is in the {0,2} suffix exactly when
  v₂(cell) ≥ 1, and it is a "2" exactly when v₂(cell) = 1. The valuation v₂ of
  a cell is a well-defined function of the initial gap valuations
  v₂(q_{j+1}−q_j) via the ultrametric inequality: |a−b|₂ = max(|a|₂, |b|₂)
  unless v₂(a) = v₂(b), in which case it is strictly smaller (cancellation). So
  the whole {0,2}-suffix status propagates from the gap valuations by
  cancellation events, and Kummer/Granville make the binomial-fold form of that
  propagation explicit. The arithmetic hypothesis needed is then about the
  distribution of v₂ of prime gaps along binary-structured index patterns — an
  input strictly different from (and not implied by) mod-4 residue switch
  density, since a gap's residue mod 4 and its higher 2-adic valuation are
  independent coordinates (a gap can be ≡ 2 mod 4 with arbitrarily high v₂).
  This is the one genuinely new coordinate the valuation route can read: the
  closed doors and the switch-density reduction all live in F2/residue-mod-4,
  while this reads the prime gaps' 2-adic structure. The F2 fold is the mod-2
  shadow of this propagation, so this is a genuine lift, not a re-derivation.

status: refuted

killed-by: >
  The advertised "explicit valuation propagation from the initial gap
  valuations" is not realisable as stated, and it is what the whole mechanism
  rests on. In the absolute-difference triangle A_{k+1}(i) = |A_k(i) − A_k(i+1)|,
  the 2-adic valuation of a difference is NOT a function of the valuations of the
  two operands alone: under the ultrametric law |a−b|_2 ≤ max(|a|_2,|b|_2) the
  strict-inequality (cancellation) case v₂(a)=v₂(b) gives v₂(a−b) its value from
  the 2-adic RESIDUE of the ratio a/b, not from v₂(a), v₂(b). So valuation — the
  only coordinate the mechanism proposes to propagate — is insufficient: one
  needs the full 2-adic values of every prior cell, i.e. exactly the data the
  F2 fold discards and exactly the data that makes the triangle hard (Odlyzko
  1993: the iterated-difference object resists a determinant-free valuation
  recursion). The lift therefore re-derives the same count with no new
  tractable invariant, rather than reading prime-gap valuations through a
  Kummer-type fold in the clean form claimed.

precedent: >
  The components are all classical and real, but none buys the mechanism:
  Kummer's theorem v₂(C(d,i)) = (number of base-2 carries adding i and d−i) —
  citable in Meštrović's survey (on disk, mestrovic_lucas_theorem_survey) and
  Barat–Grabner (Distribution of binomial coefficients and digital functions,
  JLMS 64 (2001) DOI 10.1112/S0024610701002630, 2-adic via carries);
  Granville's Zaphod–Beeblebrox mod-4 / prime-power Pascal structure — AMM 1997
  "Correction to: Zaphod Beeblebrox's Brain and the Fifty-Ninth Row of Pascal's
  Triangle" DOI 10.1080/00029890.1997.11990728 (and the on-disk
  bacher_beeblebrox_reduction, qbin analysis: determinants of reductions mod 2
  and of the Beeblebrox zeta-character); the 2-adic ultrametric inequality is
  standard. Odlyzko 1993 (on disk) is the canonical treatment of the actual
  triangle and gives no valuation-from-valuations recursion — the object resists
  precisely this reduction.

grounding-note: >
  Genuine classical inputs (Kummer, Granville mod-4, ultrametricity), all
  correctly named and verifiable. But the mechanism's first step — an explicit
  valuation propagation from initial valuations — is blocked by the residue
  dependence of cancellation, a standard non-Archimedean fact. The lift is a
  legitimate re-framing but delivers the same count ν₂ = wt(Φ_n h) by way of
  cell valuations, and the valuations cannot be pushed forward without the full
  2-adic cell values (no better than re-deriving the fold). No source applies a
  Kummer fold to force ν₂ large from gap-valuation data; none plausibly could
  without the same parity barrier.

first-step: >
  Derive the explicit valuation propagation: express v₂(A_k(i)) as a function
  of the cancellation events v₂(A_{k−1}(i)) = v₂(A_{k−1}(i+1)) and the initial
  gap valuations v₂(q_{j+1}−q_j), then check the formula against the streaming
  absolute-difference triangle for n = 2..30, printing the 0-cells and 2-cells
  separately and confirming the formula splits them correctly. A formula that
  cannot be made to reproduce the 0/2 split is the falsifier; a formula that
  does reproduce it hands the next agent an exact valuation-operator to
  analyse.
```
