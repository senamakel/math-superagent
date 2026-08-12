```thread
question: >
  Which crossings of f(d)=Q_p−Q_q on (DL,DU) correspond to physically
  distinct, admissible gear arrangements, and which are spurious — so that
  g(c,s,p,q) correctly counts the PE620 arrangements?
status: open — sign convention settled; admissibility rule being diagnosed
rests-on:
  - tangency_enum_oracle_match
  - g20_overcount_by_eight
blocked-by: []
next:
  - Run G_sum(20) verbose per-tuple, compare against n_integer_count oracle
    per-tuple table, save to code/out/G20_diagnostic.txt (TASKS.md item 1)
  - Identify which tuples differ and inspect the spurious d values
  - Fix the admissibility rule in fast_g.py's g_fast()
  - Validate G(16)=9, G(20)=205
```

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

The grid-enumeration model `code/pattern/n_integer_count.py` (conditions:
n_p∈ℤ, n_q∈ℤ, n_p−n_q≡p−q (mod 2), y>ε) reproduces all three oracle values,
including the per-tuple G(20) table at `code/out/n_integer_model.txt`. This
is the reference for diagnosing which fast_g.py crossings are spurious.

## Candidates for the 8 spurious crossings

1. **d = d_min ≅ 1/(2π).** The two p-planets coincide here (degenerate
   endpoint). The grid model excludes this via y>ε.
2. **Endpoint crossings.** f crosses an integer exactly at DL or DU. The
   strict inequality `f(DL) < m < f(DU)` should exclude these, but numerical
   floor/ceil on mpmath values may admit one.
3. **Planet coincidence at interior d.** A crossing where y_p or y_q ≈ 0
   (planets not distinct) — the grid model's y>ε filter catches these.
4. **Other degeneracy.** Two same-size planets landing at the same position
   (not just coincident — exactly the same coordinates).

## What is NOT wrong

- The sign convention. All eight variants tested; only (-1,-1,-1) gives 9.
- The f-crossing monotonicity. Verified numerically per case.
- The residue formula Q_t(d) = (c-t)*β + (s+t)*μ.
- The DL/DU bounds (tangency existence + 1cm gap).
