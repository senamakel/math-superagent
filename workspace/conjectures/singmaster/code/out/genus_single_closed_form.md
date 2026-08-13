# One closed form for the genus of C(x,m) = C(y,n), checked against every entry

The run's `pattern_verify_genus_formula.captured.txt` ends with a single
formula. It is not recorded in `research/CLAIMS.md`, and it subsumes the three
separate per-family formulas in `genus_table.captured.txt`. The operator
re-checked it against every computed genus in this workspace.

## The formula

For distinct `m, n >= 2`, the geometric genus of the projective closure of
`C(x,m) = C(y,n)` is

```
g(m,n) = ( (m-1)*n - (m-2) - gcd(n,m) ) / 2
```

It is symmetric in `m` and `n` despite not looking it, and the numerator is
always even.

## The check

Every genus value produced by this workspace was collected into one table:
the 8x11 grid of `genus_table.captured.txt`, its three extended rows
(`k2 = 3, 4, 5` out to `k1 = 24`), and the 23 rows Singular computed since
(`pattern_extend_k2_6.captured.txt`, `pattern_extend_7_10.captured.txt`).

```
entries tested: 111   mismatches: 0
genus < 2 entries: [((2,3),1), ((2,4),1)]
formula genus < 2 over 2 <= m < n <= 119: [(2,3,1), (2,4,1)]
```

The formula also reproduces all three per-family closed forms in
`genus_table.captured.txt` by direct substitution, rather than agreeing with
them numerically:

- `m = 2`: `(n - gcd(n,2))/2 = floor((n-1)/2)`, the hyperelliptic value.
- `m = 3`: `(2n - 1 - gcd(n,3))/2`, which is `n-1` when `3` does not divide `n`
  and `n-2` when it does.
- `m = 4`: `(3n - 2 - gcd(n,4))/2`, which is `3(n-1)/2` for odd `n`,
  `3(n-2)/2 + 1` for `n = 2 mod 4`, and `3(n-2)/2` for `n = 0 mod 4`.
- adjacent pairs `m = n-1`: `gcd(n,n-1) = 1` gives `(n-1)(n-2)/2`, the
  smooth-plane-curve value the table cross-checks against.

## What it settles and what it does not

It settles the Faltings threshold in closed form rather than by table lookup:
over the whole range `2 <= m < n <= 119` the only pairs with genus below 2 are
`{2,3}` and `{2,4}`, exactly the two the table names. So Faltings applies to
every other fixed pair, uniformly stated and no longer dependent on how far the
grid was computed.

It does **not** touch the run's actual blocker. Faltings is per-`(k1,k2)` and
ineffective; a closed form for the genus makes the hypothesis easy to check for
any pair but supplies no bound on the number of solutions and nothing uniform
in `k`. It is a clean statement about which curves the theorem reaches, not a
step toward the uniformity Singmaster needs.

Two scope notes the run should carry with it. The formula is verified, not
derived — every value it is checked against came from Singular, so it is
`checked` and becomes `proved` only when a Riemann-Hurwitz or Plucker
computation produces it. And `genus_table.captured.txt` describes its values as
agreeing across "two independent CAS", which is true of the original grid but
not of the 23 rows added since: `pattern_sage_check_k2_6.captured.txt` is a
`NameError: name 'PolynomialRing' is not defined`, so Sage never ran on the new
rows and they rest on Singular alone.

```claim
id: genus-single-closed-form-all-pairs
statement: For distinct m, n >= 2 the geometric genus of the projective closure
  of C(x,m) = C(y,n) is g(m,n) = ((m-1)*n - (m-2) - gcd(n,m))/2. Checked
  against all 111 genus values computed in this workspace - the 8x11 grid of
  genus_table.captured.txt, its extended k2 = 3, 4, 5 rows to k1 = 24, and the
  23 rows from pattern_extend_k2_6 and pattern_extend_7_10 - with zero
  mismatches, and the numerator even in every case. It reduces by substitution
  to all three per-family closed forms already recorded, and to the
  smooth-plane-curve value (n-1)(n-2)/2 on adjacent pairs. Over
  2 <= m < n <= 119 it gives genus < 2 for exactly {2,3} and {2,4}, so Faltings
  applies to every other fixed pair.
hypotheses: genus is of the projective closure of the affine curve, diagonal
  pairs m = n excluded as reducible, and the computed values it is checked
  against are Singular's
holds-here: yes for the Faltings threshold, which it states in closed form
  instead of by table extent. No for the conjecture: Faltings is per-pair and
  ineffective, so a genus formula supplies no bound and nothing uniform in k
status: checked
bearing: replaces three per-family formulas and a finite table with one
  expression, so the genus >= 2 hypothesis is decidable for any pair without
  further CAS time. Becomes proved when derived by Riemann-Hurwitz or Plucker
  rather than verified. Note the two-CAS claim in genus_table.captured.txt does
  not cover the 23 newest rows - pattern_sage_check_k2_6.captured.txt is a
  NameError and Sage never ran on them
anchor: code/out/pattern_verify_genus_formula.captured.txt;
  code/out/genus_table.captured.txt; code/out/pattern_extend_k2_6.captured.txt;
  code/out/pattern_extend_7_10.captured.txt;
  code/out/pattern_sage_check_k2_6.captured.txt
source: operator-computation
```
