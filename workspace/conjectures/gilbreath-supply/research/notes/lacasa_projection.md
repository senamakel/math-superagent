# Parity-projection erasure: CRT second route + NEW LOS orientation-merge

This note records two things for the reopened `1 < K ≲ n/2` question.

## 1. CRT: a second independent proof of the settled Lacasa erasure

The claim `lacasa-mod6-forbidden-blocks-parity-invisible`
(`research/notes/lacasa_parity_projection_transfer.md`) is already PROVED for all
m (per-coordinate bijection: with gap `g=6a+c`, `c∈{0,2,4}`, the fold bit
`h[j]=(g/2) mod 2 = (a mod 2) ⊕ (c/2 mod 2)`; the free `a mod 2` is a bijection
swamping the fixed class term, so every binary block is realisable from both an
admissible and a forbidden mod-6 block).

**This pass contributes an independent proof route via the Chinese Remainder
Theorem** — a second, different derivation of the same conclusion, in the spirit
of verify-by-a-second-route (rule 11). Lacasa's symbols are indexed by half-gap
mod 3; the fold keeps half-gap mod 2; since gcd(2,3)=1, CRT gives that every
symbol class mod 3 is realisable with every parity mod 2 independently. The
mod-2 parity carries no mod-3 (hence no mod-6) information. This confirms, by a
different argument, the settled claim. It is NOT a new claim.

Note the small index discrepancy worth recording (not a contradiction): the two
routes phrase the same projection with the class in `{0,2,4}` (the gap residue
mod 6) versus the half-gap mod 3. They are the same thing — `symbol = 2·(half-gap
mod 3)` — and both conclude the parity string is decorrelated from the class.

## 2. NEW: LOS secondary-bias orientation is also erased (odd C(k))

The fold bit is `h[j] = [q_{j+1} ≢ q_j mod 4]` — the **unoriented** mod-4 switch
indicator. It merges the two oriented switch pairs `(1,3)` and `(3,1)` into a
single bit.

The LOS secondary (K≥2) bias term `c₂(q;(a,b))`, or its normalized `C(k)`, is
**odd**: only odd characters contribute (`L(0,χ)=0` for even χ), so
`C(k) = −C(−k)` — it *distinguishes* the oriented pair `(a,b)` from `(b,a)`.
Because the fold bit is unoriented, it cannot read this orientation-dependence:
the odd part of the K≥2 term is invisible to `h`. (Even the switch density itself
is the *sum* over both orientations — `[a≢b]` — which at K=1 is parity-visible,
but the K≥2 *oriented* correction `C(b−a)`, odd in `b−a`, is not.)

This is a genuinely new observation in the library (the LOS summary
`los-sawtooth-secondary-bias-term` does not record it), and it reinforces the
same theme: the fold's parity reading erases both the unconditional K>1 mod-6
structure (Lacasa) and the orientation-carrying K≥2 bias structure (LOS).

```claim
id: los-secondary-bias-orientation-invisible-to-fold
statement: The LOS secondary (K>=2) consecutive-prime residue bias term C(b-a) (normalized
  from c_2(q;(a,b))) is ODD in the oriented displacement, C(k)=-C(-k), because only odd
  characters contribute. The fold's bit h[j]=[q_{j+1} != q_j mod 4] is the UNORIENTED mod-4
  switch indicator, merging the oriented pairs (1,3) and (3,1) into one bit; hence the odd
  orientation part of the K>=2 bias is invisible to h. The order-1 switch density (sum over
  both orientations) remains the finest parity-visible structure.
hypotheses: LOS c_2/C(k) machinery (arXiv:1709.06168, Thms 1.1/4.1/4.2); fold bit = unoriented
  mod-4 switch (problem.md fact 1); C(k)=-C(-k) from odd-character contributions.
holds-here: yes — reinforces that the fold sees no K>=2 structure beyond the parity-visible
  order-1 switch; the reopened question keeps no depth-2 orientation input from LOS either.
status: proved (from LOS C(k) odd + fold bit unoriented; a direct reading of the source, not a
  further theorem)
bearing: extends the Lacasa-erasure theme to the LOS K>=2 term: the only structure that survives
  to the fold's parity input is the order-K=1 switch density (and the mod-4 non-uniformity of it),
  while the higher-order oriented corrections the primes provably carry [catalogue] are erased.
  Supports the conclusion that a K>1 functional of the fold, if it exists, must be driven by the
  fold's OWN submask-correlation reading, not by an additive residue-pattern input.
contradicts: (none) — confirms and extends lacasa-mod6-forbidden-blocks-parity-invisible
follows-from: los-sawtooth-secondary-bias-term
anchor: lemke_oliver_soundararajan_sawtooth.full (§2-3: C(k) odd from odd characters); note
  research/notes/lacasa_projection.md
```

## Where this leaves the reopened question

Two independent parity-barrier analogues now known:
- Lacasa unconditional K>1 mod-6 forbidden blocks → erased by parity (settled,
  `lacasa-mod6-forbidden-blocks-parity-invisible`; CRT second route here).
- LOS K≥2 *oriented* bias → erased by the unoriented switch bit (new,
  `los-secondary-bias-orientation-invisible-to-fold`).

The order-1 mod-4 switch density (and its non-uniformity) is the only
residue-pattern input known to survive to the fold's parity string. GOAL
priority 2/3 stays open: whether the fold's own submask-correlation reading
(Lucas/kernel/second-moment) admits an input strictly weaker than that.

## Corroboration (numerical, not the evidence)

`code/scholar/projection_erasure_check.py` (part A: every F₂^m parity string
realizable by an admissible 6-block — confirms CRT/Lacasa accounting; part B:
the mod-4 switch bit merges both orientations so the odd C(k) term is invisible —
confirms the LOS observation). These are cross-checks of the proved conclusions.
