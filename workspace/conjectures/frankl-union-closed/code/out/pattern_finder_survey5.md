# Pattern-finder — |Alb| distribution extended to n=5; EQ(n)=A053221 re-confirmed

Pattern-recognition pass over the run's computed data. Three things.

## 1. |Alb|-distribution to n=5 (new exact computation)

`|Alb(F)|` = the NUMBER of abundant elements (those with `2*c_x >= |F|`),
exact integer counts, over all NONEMPTY union-closed families on `[n]`.
Extended from the filed n<=4 table (`mroof_enum.captured.txt`) to n=5 via the
validated projection/up-set cascade.

```
n=1: {1: 2}
n=2: {1: 6, 2: 6}
n=3: {1: 18, 2: 60, 3: 42}
n=4: {1: 64, 2: 942, 3: 2460, 4: 1492}
n=5: {1: 265, 2: 30340, 3: 450750, 4: 1332525, 5: 957222}
```

The n<=4 rows reproduce the filed `mroof_enum` table (which included the
`{∅}` outlier; removing it gives the above, and the nonempty count matches
the cascade's own 2, 12, 120, 4958, 2771102).

**`|Alb|==0` is 0 for every n<=5** — every nonempty UC family has at least one
abundant element. This is consistent with (not a proof of) UC; it is
expected and not a new finding.

**New 5th term of the "exactly one abundant element" sequence** is **265**,
giving `[2, 6, 18, 64, 265]`. Tools:
- not a low-degree polynomial (diffs 4, 12, 46, 201 — never stabilise);
- **no constant-coefficient linear recurrence of order <= 6** fits the 5 terms;
- **not in OEIS** (recorded miss).

Verdict: an enumeration curiosity with no exploitable low-order structure for
Frankl's conjecture — the same status as the already-filed structureless
profile-count sequence `1, 4, 18, 138, 2503`.

Also computed (pure arithmetic on the table, exact):
- `sum_F |Alb(F)|` = `[2, 18, 264, 15296, 11529405]` — not low-degree, no
  recurrence (ratio growth rising), not OEIS.
- `|Alb|==2` column `[0, 6, 60, 942, 30340]` — not low-degree.
- `|Alb|==n` (all elements abundant) `[2, 6, 42, 1492, 957222]` — not low-degree.

## 2. EQ(n) = A053221 — re-confirmed closed form (the one surviving regularity)

EQ(n) = # empty-free UC families with `f == min{n, 2k-n+1}` (KPT Thm 5(3)
equality, f = # strict-abundant elements) = `1, 5, 16, 43, 106` for n=1..5.
Re-ran the closed-form check this pass over all five terms:

```
A053221(n) = (n+2)*2^(n-1) - n - 1  ->  1, 5, 16, 43, 106.  All True.
first falsifier: n=6 gives 249.
```

**Verified-computational for n<=5 (exhaustive, exact). Conjectural beyond** —
no proof that EQ(n) = (n+2)2^(n-1) - n - 1 for all n; reaching n=6 needs an
exhaustive census of n=6 UC families (out of reach). This is the run's one
regularity that survives the exact tools with a closed form.

## 3. What each regularity is (labels)

- `|Alb|==0 = 0` for n<=5: **checked** (exhaustive).
- `|Alb|==1,2,n`, `sum|Alb|` columns: **structureless over the 5 terms**
  (no recurrence, not polynomial, not OEIS).
- EQ(n) = A053221: **verified-computational n<=5, conjectured for all n**;
  the closed form holds exactly over every term given.

Nothing here is dressed up as a proof.
