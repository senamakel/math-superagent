# Pattern-finder second pass — residue & parity structure of the digit counts

Follow-on to `regularity_findings.md`. Extends the survivor-residue and
digit-count analysis with the survivor sets to k=17 and the digit-count parities
to n=400.

## Sequences examined (all exact over the terms computed)

- `c0(n)` = number of zeros in base-3 of `2^n` = OEIS A104320 (new lookup this pass).
- `c1(n)` = number of ones = A036461.
- `c2(n)` = number of twos = A260683.
- survivor sets `A_k` (residues r mod 2·3^(k-1) with 2^r mod 3^k digit-{0,1}-free)
  computed to k=17 by exact survivor lifting.

## The exact regularities that hold

### P1 — c1(n) is even for every n ≥ 1  (PROVED, re-confirmed)
2^n ≡ Σ a_i (mod 2) because every 3^i ≡ 1 (mod 2); for n≥1 the LHS is 0, so the
number of ones is even. Verified n=1..400, no exception. Not a new finding (prior
pass proved it), confirmed on fresh terms.

### P2 — |A_k| = 2^(k-1), and survivors fill exactly the even residues mod 2^m
`|A_k| = 2^(k-1)` re-confirmed for k=1..17 (every survivor is even, forced by
2^n ≡ 1 mod 3 ⟹ n even). New this pass: for every small modulus 2^m tested
(k=12, mod 2^m for m=3..8), the survivor residues hit **every even class and no
odd class** — counts are spread (roughly uniform) over the even classes, never
concentrated. So there is NO 2-adic modular obstruction among survivors beyond
evenness: no finer congruence class modulo a power of 2 is avoided by the
survivor exponents. A symbolic invariant cannot come from residue mod 2^m.

- k=12, mod 256: all 128 even classes hit, none odd; counts 9–28 spread evenly.
- Not a proof for all m (finite check), but a clean negative over the data.

### The digit-length parity consequence (corrected)
`c0 + c1 + c2 = L`(number of ternary digits). Mod 2: `c0 + c1 + c2 ≡ L`.
With c1 even this gives **c0 ≡ c2 + L (mod 2)** — the parities of c0 and c2 are
NOT equal in general.

## What was refuted this pass

### FA — c0(n) ≡ c2(n) (mod 2) is FALSE
Hypothesis that the zero-count and two-count have equal parity. Refuted: 197
counterexamples in n=1..400 (first at n=1,4,7,10,11,13,...). Only c1-even is a
theorem; c0/c2 parity flips with the ternary digit-length parity. Recorded to
stop anyone else proposing it.

### FB — max survivor = period − 12 is small-scale only
`max A_k = period − 12` holds for k=4..11 (period = 2·3^(k-1)) but breaks at
k=12 (period−142), then period−142 for k=12..15, period−424 at k=16,
period−846 at k=17. Not an invariant; the deficit is a fixed small offset that
steps up irregularly. Dead end, recorded so nobody searches it again.

## What the tools did NOT find
- `c0` (A104320): `find_linear_recurrence` finds no constant-coefficient
  recurrence of order ≤ 12 over 81 terms. `analyze_sequence` confirms no
  polynomial fit. (Same negative already recorded for c2.)
- OEIS has no catalogued structure for the survivor residues (prior pass), and
  A104320/A260683 carry no closed form applicable here — they are defined by
  the very digit counts, so a match would explain nothing.

## Where this leaves the symbolic-invariant route
The survivor exponents carry NO modular-2 closure structure beyond evenness
(fill every even class) and NO low-order recurrence/polynomial structure in the
digit counts. The only exact parity fact is c1-even. This pushes the invariant
onto the carry/transducer coupling (the base-2 → base-3 digits) rather than any
residue or simple count statistic — consistent with `research/backward/
erdos-via-symbolic-invariant.md`'s narrowing to a finite-transducer statistic.
