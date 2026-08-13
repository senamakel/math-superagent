# Genus closed form — out-of-sample Singular falsification

`code/out/genus_falsify.captured.txt` is the out-of-sample test of the closed
form

```
g(m,n) = ( (m-1)*n - (m-2) - gcd(n,m) ) / 2
```

for the geometric genus of the projective closure of `C(x,m) = C(y,n)`,
`m != n`, `m,n >= 2`.

The run predicted each of 17 pairs **first from the closed form**, then
recomputed the genus independently in Singular. This is the difference between
in-sample agreement (the same values the formula was fitted to) and
out-of-sample confirmation: none of the 17 pairs appears in the grid the
formula was originally checked against (`genus_table.captured.txt` and its
extensions, which span `2 <= k1 <= 12`, `2 <= k2 <= 9`). All 17 are outside
that grid.

Result: **17 of 17 returned, 0 mismatches**, including the high-gcd cases
`{13,26}` (gcd 13 → genus 144), `{14,28}` (gcd 14 → 169), and `{16,26}`
(gcd 2 → 187). The pairs span `m` in `2..16` and `n` in `13..28`.

Two attributes, stated per the standing requirement:

- **effective: yes** — a finite, exact CAS recomputation of 17 specific pairs,
  no ineffective input and no unspecified constant.
- **uniform in k: no** — it confirms 17 specific pairs, not all pairs at once.
  Uniformity of the formula remains `checked`, not `proved`; this test is
  evidence for the formula, not a derivation of it.

```claim
id: genus-closed-form-out-of-sample-verified
statement: The genus closed form g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2 for
  the projective closure of C(x,m) = C(y,n) (m != n, m,n >= 2) was predicted
  first from the formula and then recomputed independently in Singular for 17
  out-of-sample pairs, all outside the 2..12 x 2..9 grid the formula was
  originally checked against. 17 of 17 returned with 0 mismatches, including
  {13,26} gcd=13 -> 144, {14,28} gcd=14 -> 169, {16,26} gcd=2 -> 187. The
  pairs span m in 2..16 and n in 13..28. Effective: yes (finite exact CAS
  recomputation). Uniform in k: no (17 specific pairs, not all pairs).
hypotheses: distinct m,n >= 2; genus computed by Singular on the projective
  closure; the 17 pairs are out-of-sample relative to the earlier grid.
holds-here: yes
status: checked
bearing: out-of-sample predict-then-recompute-by-another-route is genuine
  falsification methodology, stronger than in-sample agreement. It confirms the
  closed form beyond the fitted grid but does not prove it: uniformity over all
  (m,n) remains to be established by a derivation (Riemann-Hurwitz/Plucker with
  the singularity delta-invariant). Effective but not uniform in k, so it is a
  verified instance, not a bound and not a uniform theorem.
anchor: code/out/genus_falsify.captured.txt
```
