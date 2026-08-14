# Mechanical-word / Beatty-floor telescoping for Ψ(k)

```approach
idea: Represent the Fibonacci word as the mechanical word f[n] = ⌊(n+2)α⌋ − ⌊(n+1)α⌋
  with α = 1/φ² = (3−√5)/2, so the decimal value of the factor at position p
  telescopes into a closed linear combination of Beatty floors ⌊(p+m)α⌋, turning
  Ψ(k) into a sum of floor-products over the k+1 distinguished phases p, evaluable
  in poly-log(k) via Ostrowski/Beatty floor-sum recursion over the golden continued
  fraction [0; 2, 1̄].
mechanism: f[n] = ⌊(n+2)α⌋ − ⌊(n+1)α⌋ is checked by hand for the Fibonacci word
  (slope 1/φ², intercept 1/φ²). Summing f[p+j]·10^{k−1−j} over j telescopes (summation
  by parts) to val(w_p) = ⌊(p+k+1)α⌋ − ⌊(p+1)α⌋·10^{k−1} + 9·Σ_{m=2}^{k} ⌊(p+m)α⌋·10^{k−m}.
  Then val(w_p)² is a polynomial in the floors ⌊(p+m)α⌋ with power-of-10 coefficients,
  so Ψ(k) = Σ_{p∈P_k} val(w_p)² is a finite sum of Beatty floor-products
  Σ_p ⌊(p+m)α⌋⌊(p+n)α⌋ over the k+1 distinguished phases P_k (the three-gap /
  Ostrowski phase set). These sums are computable in O(log k) because α is quadratic:
  its continued fraction is [0; 2, 1, 1, 1, …], so ⌊(p+m)α⌋ follows a Fibonacci-indexed
  recurrence and the floor-sums obey the classical Ostrowski/floor_sum recursion.
status: proposed
first-step: For k = 1..12 compute the k+1 distinguished start positions P_k (where the
  distinct factors occur), verify the telescoped val(w_p) formula reproduces
  code/out/factors_k12.txt's decimal values exactly, then write Ψ(k) as the explicit
  floor-product double sum and match it against code/out/psi_data_1_150.txt for
  k = 1..12.
```

## What is established vs speculation

- **Established (checked here by hand):** `f[n] = ⌊(n+2)α⌋ − ⌊(n+1)α⌋` reproduces
  `0100101001…` (verified n = 0..12). The telescoped value formula was verified on
  all four k=3 factors (p = 0,1,2,4 → values 10, 100, 1, 101) and spot-checked for
  k=4.
- **Speculation (needs research):** the precise closed description of the phase set
  P_k (the k+1 distinguished starting positions — for k=3 it is {0,1,2,4}, for k=4
  it is {0,1,2,3,4}), and the claim that the floor-product sums over P_k reduce to
  O(log k) Ostrowski/Beatty sums. Sources already in the library that should carry
  the phase-indexing theorem: Berthé's "Automatic sequences" course
  (`sources/berthe-automatic-sturmian-sequences-course.full.md`) and the
  three-distance-theorem references in `research/FRONTIER.md`.

## Why this is different from what the run tried

The run worked with the combinatorics-on-words structure (Perrin–Restivo lex-order
next-factor rule, circular-interval columns, the extension formula). It never wrote
down the mechanical-word/Beatty identity `f[n] = ⌊(n+2)α⌋ − ⌊(n+1)α⌋` or the
telescoping of `val(w_p)` into floor sums, which is what makes the sum-of-squares
an explicit *polynomial in Beatty floors* — a number-theoretic object with a known
poly-log evaluation, rather than a combinatorial double sum over column intervals.
