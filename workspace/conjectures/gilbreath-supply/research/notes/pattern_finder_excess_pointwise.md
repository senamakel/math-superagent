# Pattern-finder: the pointwise excess IS the whole conjecture

```claim
id: excess-is-negative-character-sum
statement: >
  For the canonical fold form, ν₂(n) = #{d ∈ [2,n−1] : T(n,d)=1} with
  S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)}, the identity
  2·ν₂(n) − (n−2) = −S(n) holds EXACTLY; equivalently ν₂(n) = (n−2−S(n))/2.
hypotheses: the fold definition of problem.md fact 1 (ν₂ = wt(Φ_n h),
  T(n,d) the submask-XOR cell); pure counting over the n−2 depths.
holds-here: yes
status: checked — verified by two independent routes (lib.supply_fold.s_sos
  SOS path and lib.supply_fold.s_direct/t_direct brute submask-XOR path) for
  every n: SOS vs brute identity 2..4000, brute-only 2..60; ones==fold_nu2
  throughout.
bearing: >
  Makes pointwise SUPPLY ⟺ S(n) ≤ (1−2c)n − 2 eventually (limsup S/n < 1),
  so the endpoint-parity skeleton's G-arithmetic |S(n)|≤(1−2c₀)n is not merely
  sufficient but EQUIVALENT to pointwise SUPPLY. Measured S(n) is deeply
  sublinear (max|S| ≈ 634 at n=30000; max|S|/√n ≈ 3.2–3.8 across 1024..30000),
  supporting ν₂/n → 1/2, i.e. pointwise SUPPLY for every c < 1/2 — stronger
  than the averaged/density-1 form.
anchor: research/notes/pattern_finder_excess_pointwise.md
```

## The exact identity (verified computationally, every n in range)

For the canonical fold form, `ν₂(n) = #{ d ∈ [2,n−1] : T(n,d) = 1 }`, with
`S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)}` the endpoint character sum of
`research/backward/supply-from-endpoint-parity.md`:

    E2(n) := 2·ν₂(n) − (n−2)   (signed excess)
          = −S(n)               EXACTLY, checked n = 2..4000.

Proof sketch (identity, not arithmetic): there are n−2 depths d; if `ones` of
them are 1 then `Σ_d (−1)^{T(n,d)} = ones·(−1) + ((n−2)−ones)·(+1) = (n−2) −
2·ones`, and `ν₂ = ones`, so `S(n) = (n−2) − 2ν₂(n)`, i.e. `2ν₂ − (n−2) = −S`.
This is pure counting; no number theory. The run's `lib.nu2.fold_nu2` and
`lib.supply_fold.s_sos` agree on it to the full computed range.

## What it buys: SUPPLY pointwise is a statement about S(n) = o(n)

From the identity, `ν₂(n) = (n−2−S(n))/2`, so

    ν₂(n) ≥ c·n   ⟺   S(n) ≤ (1−2c)·n − 2   (eventually).

Hence **pointwise SUPPLY holds iff `limsup S(n)/n < 1`** (in fact iff `S(n)`
is eventually below `(1−2c)n`; any fixed `c<1/2` needs only `S(n) < (1−2c)n`).
This is the *exact* form of the endpoint-parity skeleton's G-arithmetic
(`|S(n)| ≤ (1−2c₀)n`), recovered as a tight equivalence rather than a
sufficient condition.

## Measured growth of S(n) (exact integers, real prime h)

| range | max|S(n)| | max|S|/√n | max|S|/n^0.6 |
| --- | --- | --- | --- |
| n ≤ 1024 | 104 | 3.25 | — |
| n ≤ 2048 | 120 | 2.65 | — |
| n ≤ 4000 | 220 | 3.49 | 2.28 |
| n ≤ 8000 | 289 | 3.24 | — |
| n ≤ 30000 | 634 | 3.82 | 2.77 |

`max|S|/n^0.6` is essentially constant ≈ 2.3–2.8 across 4000→30000, and
`max|S|/√n` ≈ 3.3–3.8. So S(n) is empirically **O(n^{1/2+ε})** — *deeply*
sublinear, far below the `(1−2c)n` threshold for any sensible c (even c=0.1
needs S < 0.8n; measured S/n ≤ 0.021 at n=30000, and it decays).

## Consequence

The pointwise conjecture (result 1 of problem.md, *not just* the averaged form
result 3) is supported by the data: ν₂(n)/n tracks (n−2)/(2n) ≈ 1/2 − 1/n to
within O(n^{-1/2+ε}), so ν₂ ≥ c·n for every fixed c < 1/2 from some n on.
The margin between measured S(n) and the fatal `(1−2c)n` line is enormous and
growing.

## What is NOT claimed

- This is measurement over n ≤ 30000, not a proof. `S(n) = o(n)` is the open
  arithmetic statement (balanced/uncorrelated mod-4 endpoint comparisons at
  binary-structured gaps); it has NOT been derived — it is the hard head of
  the endpoint-parity skeleton.
- Both `ν₂(n)` and the excess `E2(n)=−S(n)` sequences are **not in OEIS** and
  have **no constant-coefficient linear recurrence of order ≤ 8** and are not
  low-degree polynomials (find_linear_recurrence / analyze_sequence, exact over
  the terms supplied). So there is no recurrence-level shortcut to pointwise
  SUPPLY; the sublinearity of S is the only structure found, and it is an
  arithmetic (L-functions/parity-barrier) statement, not a combinatorial one.

## Priorities this supports

It sharpens GOAL priority 1/2: the averaged form is safe (it already holds
from just S=o(n) via Chebyshev), but the data suggest even the *pointwise* form
holds — the real target is therefore deriving `S(n)=o(n)` from a second-moment/
autocorrelation bound on the prime h read along binary-submask windows
(G-var-vanishing), which this note shows is *sufficient* for full SUPPLY, not
merely the density-1 form.
