# Pattern-finder pass — extended tables to n=5; EQ(n) = A053221

What ran: `code/out/extend_tables_n5.py` — the validated canonical cascade
(`profile_count_cascade` machinery: projection + (R1,R2) up-set lift),
extended from n=1..4 to n=5, exact integer arithmetic, no floats.
Guard: level counts reproduce A121921 minus trivial {empty}
(2, 12, 120, 4958, 2771102) — ALL OK.
Range: all union-closed families on [n], n=1..5 (~2.77M at n=5).
Elapsed 113.4s, exit 0.

## The four tables, extended

| n | degree1 | eq3 (KPT Thm 5(3) equality) | emptyfree | A-sat (n_max ≥ 2k_min+1) |
|---|---|---|---|---|
| 1 |  2 |   1 |     1 |     0 |
| 2 | 10 |   5 |     6 |     0 |
| 3 | 56 |  16 |    60 |    37 |
| 4 | 590 |  43 |  2479 |  2041 |
| 5 | 26182 | 106 | 1385551 | 1378591 |

Semantics (copied from the original source runs):
- **degree1** = # UC families with some present element in exactly one set
  (combine_constraints.py claim-D counts; original n≤4 values 2,10,56,590,
  reproduced exactly).
- **eq3** = # empty-free UC families with f == min{n, 2k−n+1}, f = # elements
  with strict abundance 2c > |F|, k = min set size, n = max set size
  (kpt_thm5_verify.py; original 1,5,16,43 reproduced exactly).
- **emptyfree** = # empty-free UC families (original 1,6,60,2479 reproduced).
- **A-sat** = # empty-free UC families with n_max ≥ 2·k_min + 1 (the
  counterexample-corollary regime of KPT Thm 5(3); original 0,0,37,2041
  reproduced).

## The one regularity that survives attack: EQ(n) = eq3 = A053221

```
eq3:  1, 5, 16, 43, 106   (n = 1..5, exhaustive, exact)
A053221(n) = (n+2)·2^{n−1} − n − 1:   1, 5, 16, 43, 106   — exact match,
  verified term-by-term over all five terms.
```

OEIS lookup of [1,5,16,43,106] returns exactly three entries sharing the
prefix — A053221 (closed form above), A036888 (partitions mod-5 counts),
A034358 (binary [n,4] codes) — none of which is otherwise related to UC
families. The closed form is A053221's; the other two are prefix coincidences
(no hypothesis connects them to KPT equality). **First falsifier:** n=6,
where the formula gives EQ(6) = 249. Reaching it requires an exhaustive census
of n=6 UC families, out of reach of the current cascade (~2.77M level-5
families each branching over valid (R1,R2) lifts).

**Status: verified-computational for n ≤ 5 (exhaustive, exact). Conjectural
beyond — no proof that EQ(n) = (n+2)2^{n−1} − n − 1 for all n.** The regularity
is labelled a conjecture, not a theorem, and its verification chain is: the
cascade (validated against A121921 at every level AND against the original
lib.uc-based n≤4 enumerations, which it reproduces exactly) → EQ(n).

## The other tables: no structure (exact over the terms given)

All were run through analyze_sequence / find_linear_recurrence / oeis_lookup
(with the 5-term extensions; lookups with only 4 terms are weak and were not
relied on):

- degree1  [2, 10, 56, 590, 26182]: not low-degree; no constant-coefficient
  linear recurrence of order ≤ 4; OEIS miss (recorded).
- emptyfree [1, 6, 60, 2479, 1385551]: no recurrence ≤ 4; OEIS miss.
- A-sat    [0, 0, 37, 2041, 1378591]: no recurrence ≤ 4; OEIS miss.
- no-degree-1 UC families (excl. trivial {empty}) = total − degree1:
  [0, 2, 64, 4368, 2744920] — OEIS miss (recorded); no closed form apparent.
- any-element-at-density-1/2 [1, 6, 56, 1869, 752457] (from
  half_density_front.captured.txt, n≤5): OEIS miss (recorded).
- M♮-certificate sweep columns [0,2,24,686] over, [0,2,46,2992] under,
  [3,9,51,1281] Cert==Alb, [1,3,41,2789] totally-unc (from
  mroof_sweep.captured.txt, n≤4): no low-degree/recurrence structure; OEIS
  misses (recorded). Note the "totally-unc" counts include the degenerate
  F={∅} outlier (1 at n=1); among nonempty-Alb families: 0,2,40,2788.
- KPT (1)-tightness families (f==k, k≥n−3) total 139 at n≤4 — a single total,
  not a sequence.

## What this means for the run

- EQ(n) being a clean closed form is a counting coincidence with a *derivable
  target*: if a later pass can characterise the KPT-equality families (those
  with f = min{n, 2k−n+1}, forced k ≥ (n−1)/2 so only large-minimum-set
  families count), the identity EQ(n) = (n+2)2^{n−1} − n − 1 becomes a
  theorem instead of a conjecture. This is the most likely regularity here to
  yield a derivation.
- The other tables carry no exploitable low-order structure over the terms
  given; each is an enumeration curiosity. All OEIS misses are recorded so
  nobody looks again.