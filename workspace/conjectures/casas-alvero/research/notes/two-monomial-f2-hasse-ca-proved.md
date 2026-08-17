# Two-monomial F2 Hasse-CA structure — PROVED

**Statement.** Let `g(x) = x^n + x^a` over `F_2`, with `0 < a < n`. Then `g`
satisfies Hasse-Casas-Alvero (gcd with every Hasse derivative `H_i(g)`,
`i=1..n-1`, is non-constant) **iff** `C(n,a)` is odd, i.e. iff `(a & n) == a`,
i.e. iff `a` is a subset-sum of the set bits of `n`.

**Proof.** Write `g = x^a (x^{n-a} + 1)`. The i-th Hasse derivative (no `i!`
factor) is

    H_i(g) = C(n,i) x^{n-i} + C(a,i) x^{a-i}   over F_2.

Only the derivative `i = a` can ever fail.  Three cases:

- `i < a`: both exponents `n-i, a-i > 0`, so the constant term of `H_i(g)` is
  `0`, hence `x | H_i(g)`, so `gcd(g,H_i)` contains `x`, non-constant.  Passes.
- `i > a`: `C(a,i) = 0`, so `H_i(g) = C(n,i) x^{n-i}` is an `x`-power
  (`n-i >= 1`), so `gcd(g,H_i)` contains `x`, non-constant.  Passes.
- `i = a`: `H_a(g) = C(n,a) x^{n-a} + C(a,a) = C(n,a) x^{n-a} + 1`.
  `gcd(x^a, H_a) = 1` (constant term `1`), and
  `gcd(x^{n-a}+1, C(n,a) x^{n-a} + 1) = 1` iff `C(n,a)` is even, and equals
  `x^{n-a}+1` (non-constant) iff `C(n,a)` is odd.

So Hasse-CA holds iff `C(n,a)` is odd.  By Lucas's theorem, `C(n,a)` odd iff
`(a & n) == a` (every set bit of `a` is a set bit of `n`), i.e. `a` is a
subset-sum of `n`'s set bits.  ∎

**Consequences (both now proved, not merely verified).**

1. The **support-2 counterexample law**: the support-2 F2 Hasse-CA
   counterexamples of degree `n` are exactly
   `{ x^n + x^a : 0 < a < n, (a & n) == a }`.  Their number is `2^pc(n) - 2`
   (the `2^pc(n)` subset-sums of the set bits, minus the empty sum `0` and the
   full sum `n`, both excluded by `0 < a < n`).  None of these is a pure power
   (`x^n` and `(x+1)^n` are the only degree-`n` pure powers over F_2; `x^n+x^a`
   matches neither for `0<a<n`).  This law was previously only verified over
   the suggesting range; it is now a theorem for every `n`.

2. **Failing-index rigidity**: when a two-monomial `x^n+x^a` fails Hasse-CA, it
   fails at derivative `i = a` and only there — no other derivative can fail
   (proved by the three-case argument above, independent of both monomials'
   exponents beyond the `i > a` and `i < a` splits).

**Verification beyond the suggesting data.** The structural facts S1–S3
(Hasse-CA ⟺ `(a&n)==a`; failing index `== a`; no `i != a` fails) were checked
EXACTLY for all `n = 3..64` and all `a` in `1..n-1` (2015 candidate
polynomials; 602 legal subset-sum cases; 1413 illegal cases; the set-bits
scan for `i != a` on every illegal `a`) — see the code below.  Zero mismatches.
That range includes popcount classes 5 and 6 (`n = 31..63`), which the earlier
exhaustive enumeration (limited to `2^n <= 2^28`) could never reach; testing
the law requires only the `2^pc - 2` candidates per `n`, not all `2^n` monic
polynomials.

**Why this is exploitable structure, not just a fit.** The law does not depend
on a best-fit recurrence; it is forced by a single derivative (`i = a`) whose
sufficiency/failure reduces to a single binomial coefficient modulo 2, where
Lucas's theorem gives a closed characterization.  The raw multiplier sequence
`m(n,2)` in `n` is irregular (no polynomial fit to 12 difference levels, no
constant-coefficient linear recurrence to order 8, no OEIS match) precisely
because it is governed by this popcount/subset-sum structure, not by `n`
linearly.

**Compute log.** Scripts (exact bit-arithmetic, no floats, no sympy in the
hot loop; oracle-checked against `lib.casas_alvero.is_ca_hasse` at small `n` in
the earlier run files):
- `code/out/twoterm_submask_wide.py` — law over n=3..64, 2015 candidates, 0
  mismatches (captured exhaustively above).
- `code/out/twoterm_structure.py` — the failing-index observation (always `a`).
- `code/out/twoterm_sharp2.py` — S1/S2/S3 confirmed exactly, n=3..64.

All three ran exit 0 / printed HOLDS.
