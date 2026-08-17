# Christoffel conjugacy class + autocorrelation of a single word

```approach
idea: The k+1 length-k factors of slope 1/φ² are (up to a small number of "singular"
  factors, counted by the Ostrowski position of k) the cyclic shifts of a single
  Christoffel word C_k. Then Ψ(k) = Σ_r val(shift_r(C_k))² + (singular terms), and the
  sum over cyclic shifts of a binary word reduces to its autocorrelation c(d), which
  for a Christoffel word is a known three-gap closed form in k and d.
mechanism: Perrin–Restivo (in library) already gives the prototype: the 9 length-8
  factors are 8 conjugates of abaababa plus the singular babaabab. In general the factor
  set is a Christoffel conjugacy class (the k conjugates of the Christoffel word of the
  appropriate level) plus a bounded-to-log number of singular words. For a binary word w
  of length k, Σ_r val(shift_r w)² = Σ_{i,l} c(l−i)·10^{2k−2−i−l} where c(d) = Σ_j w_j w_{j+d}
  is the autocorrelation; this collapses the 2D double sum over column intersections to
  a 1D autocorrelation. A Christoffel word's 1-set is a Beatty sequence mod k, so c(d)
  has an explicit piecewise-closed form from the three-gap structure of its 1-positions,
  computable in poly-log(k) via the continued fraction of 1/φ².
status: proposed
first-step: For k ≤ 40, verify (against code/out/factors_k40.json) that the factor set is
  exactly {cyclic shifts of a Christoffel word C_k} ∪ {singular factors}, identify C_k's
  1-positions as ⌊j·(something)⌋ mod k, and check the autocorrelation formula for c(d)
  against the pair-correlation table A(i,l) already computed in
  code/out/PE1006_report_tasks_ABC.txt (Task C4).
```

## Established vs speculation

- **Established (sourced):** Christoffel conjugacy structure of Sturmian factor sets
  (`christoffel-conjugate-and-forest`, Perrin–Restivo Example 10 / Table 1 in library).
  The run's own Task C4 already computed the pair-correlation table A(i,l) as circular
  interval intersections, which is the same object as the autocorrelation.
- **Speculation:** the sharp statement that only a *log-bounded* number of singular
  factors appear for general k (rather than O(k)), which is what makes the sum a
  single-word autocorrelation plus a small correction; and the exact three-gap closed
  form for Christoffel autocorrelation. Both are to be confirmed by research.

## Why different from the run

The run's Task C treats the (k+1)×k factor matrix column-by-column and gets stuck on
pairwise intersections of *arbitrary* circular intervals. This approach reorganises the
same sum around one fixed word and its autocorrelation — a 1D object with a known
three-gap closed form — which is a genuinely different representation of the double sum
and a candidate way to dissolve the pair-correlation block.
