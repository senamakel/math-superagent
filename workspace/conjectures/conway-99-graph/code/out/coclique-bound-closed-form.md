# Coclique bound closed form for the srg(v,k,1,2) family — pattern-finder finding

```claim
id: coclique-bound-closed-form
statement: For the family srg(v,k,1,2) with k = u^2 + u + 2 and v = 1 + k^2/2,
  the independence (coclique) bound alpha <= v*(-s)/(k-s), where s is the
  negative eigenvalue, has the exact closed form
      alpha = (u*k + 2)/2 = (u^3 + u^2 + 2u + 2)/2,
  which is always an integer (u*k is even). Equivalently, substituting
  s = -(u+1) (from 4k-7 = (2u+1)^2, so eigenvalues r=u, s=-(u+1)) gives
      alpha = v*(u+1)/(k+u+1).
  At the five feasible u in {1,3,4,10,31} the values are
      3, 22, 45, 561, 15408 — strictly increasing and pairwise distinct,
  so the srg(99,14,1,2) coclique bound (22) is parameter-specific.
hypotheses: srg(v,k,1,2) with k=u^2+u+2, v=1+k^2/2, min eigenvalue s=-(u+1).
holds-here: yes — 99 is the u=3 member with bound 22.
status: checked (sympy symbolic derivation proves the identity by direct
  substitution; plus exhaustive exact-integer scan over every u in [1,200]
  with zero mismatches). This is a derivation, not a fit.
bearing: promotes the coclique-design branch of the k14-l1-local thread. The
  threads record the raw 99 value (22) but not the closed form; the form shows
  all five feasible bounds are distinct, so a nonexistence argument exploiting
  the specific value 22 at 99 (a 22-coclique forcing a 2-(22,K,2) design, the
  direct analogue of the Wilbrink-Brouwer 2-(15,5,4) 15-coclique argument at
  (57,14,1,4)) is NOT refuted on arrival by the controls: rook(3) has bound 3
  and BvLS has bound 45, neither of which equals 22.
falsifier: any u in the family where v*(-s)/(k-s) != (u*k+2)/2, or any
  non-integer value; none found over u in [1,200] and the identity is provable.
anchor: code/out/coclique_closed_form.py, code/out/coclique_and_family_sequences.py,
  code/out/coclique-bound-verified.md
```

## What was checked

- **Symbolic identity.** With k=u^2+u+2, v=1+k^2/2, s=-(u+1), sympy simplifies
  v*(-s)/(k-s) to exactly (u^3+u^2+2u+2)/2 = (u*k+2)/2. Difference is identically 0.
- **Exhaustive scan.** For every u in [1,200], alpha = v*(-s)/(k-s) computed in
  exact integers; it equals (u*k+2)//2 in every case (0 mismatches), and is
  always an integer. Parity u*k even holds for all u in [1,1000].
- **Five feasible numbers.** u in {1,3,4,10,31} give alpha in {3,22,45,561,15408},
  strictly increasing and distinct. The 99 value is 22.

## Cross-checked values (exact)

| u | k | v | s | v(-s)/(k-s) | (u*k+2)/2 |
|---|---|---|---|---|---|
| 1 | 4 | 9 | -2 | 3 | 3 |
| 3 | 14 | 99 | -4 | 22 | 22 |
| 4 | 22 | 243 | -5 | 45 | 45 |
| 10 | 112 | 6273 | -11 | 561 | 561 |
| 31 | 994 | 494019 | -32 | 15408 | 15408 |

Eigenvalues: disc = 4k-7 = (2u+1)^2, roots r=(−1+d)/2=u, s=(−1−d)/2=−(u+1).

## What it does and does not settle

It does NOT rule out srg(99,14,1,2) — the bound alone forces nothing (the true
independence number could be anywhere below 22). Its value is that it is a
99-specific, non-spectral, exactly-derivable number: the single cleanest
candidate number for a Wilbrink–Brouwer-style coclique-design contradiction at
99, with the distinctness of the family bounds establishing that such an
argument is parameter-specific rather than refuted by 9 and 243.

Other family sequences examined (triangles 6,231,891,117096,81842481;
pentagons 0,33264,384912,1669320576,96451036488576; outer blocks;
distance-2 counts; eigenvalue multiplicities) show no additional law beyond
the quartic-in-u closed forms already catalogued (governed by k=u^2+u+2);
they fail low-order constant-coefficient linear recurrences, as established
in the earlier pattern-finder reports.

OEIS status: the coclique-bound sequence {3,22,45,561,15408} and the triangle
count sequence {6,231,891,117096,81842481} have NO OEIS entry (checked via
oeis_lookup). Not catalogued, so no closed form is looked up; both are the
quartic-in-u forms already derived here.

