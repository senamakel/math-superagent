# Fibonacci family is boundary — proved

**Claim id:** `fibonacci-family-is-boundary`
**Status:** proved (structural + numerical cross-check)
**Anchor:** `code/out/boundary_family_always_boundary.captured.txt` (EXIT_CODE=0, j=1..12 all boundary)

## Statement

For the MRSTT boundary cut with any fixed ε > 1/3, every sufficiently large
member of the infinite Fibonacci family `C(n+1,k+1) = C(n,k+2)` lies in the
MRSTT-open boundary region `k < exp((log n)^(2/3+ε))`. For ε ≤ 1/3 the family
may eventually leave the boundary; for ε > 1/3 the cut-to-k ratio diverges as
`(log n)^(ε − 1/3) → ∞`, so the family stays boundary forever.

## Attributes

- **Effective:** yes — the threshold j₀(ε) is computable (the first j where
  (log n_j)^(ε − 1/3) exceeds a constant from the leading-term approximation).
- **Uniform in j:** yes — the proof holds for all j simultaneously via the
  limit ratio.

## Proof (two lines)

1. **Asymptotic ratio.** From the Lind/Singmaster parametrisation:
   `n_j = F_{2j+2}F_{2j+3} − 1`, `k_j = F_{2j}F_{2j+3} − 1`. Cancel the
   shared factor `F_{2j+3}`: `k_j/n_j = F_{2j}F_{2j+3} / (F_{2j+2}F_{2j+3})
   = F_{2j}/F_{2j+2} → 1/φ^2 ≈ 0.381966`. So `k/n → 1/φ^2` exactly along
   the family.

2. **Boundary verdict.** For ε > 1/3, the exponent in the cut is
   `2/3 + ε > 1`. Then
   `log(cut) / log(k) = (log n)^{2/3+ε} / log k`.
   Since `log k ∼ log n` (both ∼ 4j log φ), this is
   `(log n)^{2/3+ε − 1} = (log n)^{ε − 1/3} → ∞`.
   Hence `cut/k → ∞`: for sufficiently large j, `k < cut`, i.e. boundary.
   For ε = 1/2 (the run's standard) the exponent is 7/6 and the ratio is
   `(log n)^{1/6} → ∞`.

## Numerical verification

All 24 representatives for j=1..12 are boundary under ε=1/2 (capture above).

## Bearing on G-boundary-uniform-count

Each family member a_j carries at least 2 nontrivial boundary representatives
(the (k,k+1) collision pair). For j=1 (a=3003) there are 3 boundary reps
((78,2),(15,5),(14,6)). The question is whether other j have exactly 2, or
whether additional boundary reps appear — which would determine whether C ≥ 3
or C is unbounded.