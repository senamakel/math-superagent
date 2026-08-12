---
thread:
  question: >
    Which crossings of f(d)=Q_p-Q_q on (DL,DU) correspond to physically
    distinct, admissible gear arrangements, and which are spurious — so that
    g(c,s,p,q) correctly counts the PE620 "perfectly meshing" arrangements?
  status: open — sign convention settled; admissibility rule being diagnosed
  rests-on:
    - tangency_enum_oracle_match          # (sigma,eta,theta)=(-1,-1,-1) gives 9
    - g20_overcount_by_eight              # fast_g.py gives G(20)=213 vs 205
  blocked-by: []
  next:
    - Run G_sum(20) verbose per-tuple, compare against grid-enumeration oracle
      per tuple, save to code/out/G20_diagnostic.txt (TASKS.md item 1)
    - Identify which tuples differ and inspect the spurious d values
    - Fix the admissibility rule in fast_g.py's g_fast()
    - Validate G(16)=9, G(20)=205
---

# Off-centre mesh phase model — admissibility fix

The residue form is settled. The sign convention `(sigma, eta, theta) = (-1,
-1, -1)` is the only one of eight that reproduces g(16,5,5,6)=9 (claim
`tangency_enum_oracle_match`, anchor `code/out/tangency_enum.txt`).

The monotone f-crossing model (`code/pattern/fast_g.py`) implements this
correctly and gives g(16,5,5,6)=9. It counts integer levels `m` of
`f(d) = Q_p(d) - Q_q(d)` strictly between f(DL) and f(DU), with each m
crossed once (monotonicity verified per case).

The problem: G(20) sums to 213 against oracle 205, an overcount of 8 across
22 tuples (claim `g20_overcount_by_eight`, anchor
`code/out/G20_overcount.md`).

## Candidates for the 8 spurious crossings

1. **d = d_min ≅ 1/(2π).** The two p-planets coincide here (degenerate
   endpoint of the valid d interval). Excluded in the original
   `oracle-model-broken.md` diagnosis; crossing count may re-admit it via
   an integer m at f(DL) or just above.
2. **Endpoint crossings.** `#{m: f(DL) < m < f(DU)}` is strict at both ends.
   A crossing exactly at f(DL) or f(DU) is excluded by the current rule.
   But numerical f(DL), f(DU) are mpmath-approximate; the floor/ceil may
   include a boundary m that should be excluded.
3. **Planet coincidence.** Within a tuple, the two p-planets or two q-planets
   can coincide at particular d (not just at d_min). These are distinct
   arrangements geometrically but may not be "valid" under some reading.
4. **Same-size planet overlap at the same position.** The statement permits
   planets to overlap but two same-size planets at the same d (mirror pair
   U/L) may be double-counted.

## What is NOT wrong

- The sign convention. All eight variants tested; only (-1,-1,-1) gives 9.
- The f-crossing monotonicity. Verified numerically per case.
- The residue formula Q_t(d) = (c-t)*B_t + (s+t)*G_t.
- The DL/DU bounds (tangency existence + 1cm gap).
