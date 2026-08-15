# The primitive-divisor primary tier: Roitman (1997) and Voutier (1998)

Two primary sources added by librarian to close the adopted `lucas-primitive-
divisors` approach's technique gap. Full records (with claim blocks) in
`research/sources/roitman-zsigmondy-primes.primary.md` and
`research/sources/voutier-primitive-divisors-III.primary.md`. Both obtained
server-side via `read_sources` (download_document is blocked for every host).

## What they establish (sourced, asserted-by-source, not yet re-derived)

### Roitman 1997 — Zsigmondy primes carry the order congruence
A prime `r` is a **Zsigmondy prime for (a,n)** (`a,n > 1`) iff it is a prime
divisor of `a^n - 1` that divides no `a^j - 1` for `0 < j < n`, equivalently
`ord_r(a) = n`. Consequently `n | r - 1`, so `r ≡ 1 (mod n)` and `r ≥ n+1`.
A "large" Zsigmondy prime has `r > n+1` or `r^2 | a^n - 1`.
Zsigmondy's theorem (Theorem 3) gives the explicit finite exception list.
For **odd prime `p ≥ 3`**, `x ≥ 2`, a primitive divisor `r` of
`Phi_p(x) = (x^p-1)/(x-1)` satisfies `r ≡ 1 (mod p)` — the congruence engine
of the Lucas approach.

### Voutier 1998 — the universal existence threshold
Classifies when primitive divisors fail. Theorem 1: for all `n > 30030` the
`n`-th element of any Lucas or Lehmer sequence has a primitive divisor, proved
by the `ω(n)` split (ω=6 → n>30030, ω=5 → n>28980, ω=4 → n>26880, ω=3 →
n>23040) plus direct computation. The bound is conservative; the conjecture is
`n > 30`. The exceptional cases (`n <= 30`) were enumerated in the series'
first two papers.

## How they bear on the run

- They give the **existence** (Voutier) and **congruence** (Roitman) halves of
  `prim-div-lucas` / `zsigmondy-bhv-primitive-divisor`, marking those claims
  `asserted-by-source` from a primary, citable anchor rather than from the
  problem hint. The run's prime index `p` is never exceptional.
- They make "no primitive divisor" a bounded, checkable finite list rather
  than an open condition.
- **Falsifier check:** the known solution is at `(x,p) = (3,2)`, index `p = 2`
  — the even exceptional index, where `Phi_2(3) = 4` has no primitive divisor
  with `r ≡ 1 (mod 2)`. The odd-prime hypothesis excludes it by hypothesis,
  not by luck; neither claim eliminates the known solution.

## Not changed

These are technique-tier. The four answer-bearing REQUESTS.md rows (Mihailescu
closing step, Cassels theorem, descent, full statement) remain open and
unfetchable-by-design; they must be re-derived in-workspace. PROVENANCE.md
records the two new sources and the screens.
