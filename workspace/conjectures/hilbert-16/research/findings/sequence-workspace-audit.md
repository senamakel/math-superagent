# Pattern pass — workspace sequence audit (pattern_finder)

Full audit of every integer sequence on disk (commands.log 6592 lines, all
findings, claims ledger, all `sk_*`/`mono_counts`/`lyap` scripts read and the
executable ones re-run).

## Sequences and their status

1. **S_k = 4^(k−1)(k − 13/6) + (2k−1)/3** — Buzzi–Novaes/Li et al. H(n)
   lower-bound family. Fully derived from the paper's closed form; order-4
   annihilator (E−4)²(E−1)² verified k=1..399, 0 failures; S_k integer ⇔ 3|k.
   Not a new finding; already filed.

2. **a_j = S_{3j}** — guaranteed-count integers. Order-4 (E−64)²(E−1)²,
   0 failures. Fully derived; already filed.

3. **c_k = ceil(S_k)** — order-6 (E−4)²(E−1)²(E²+E+1) =
   E^6−9E^5+24E^4−17E^3+9E^2−24E+16, re-verified k=2..199 failures=0;
   order-5 minimality confirmed (fails at term 5). This closes the loose end
   left in `findings/sequence-ceil-sk-findings.md` and is fully derived from
   the closed form. **NOW also run through OEIS (was never submitted):**
   terms [0,1,15,120,729,3929,19802,95579,447835] → **no match**. Recorded so
   nobody searches again.

4. **a_d = Bautin focal-value monomial counts** (4,30,97,236,485,890) — the
   run's note says no clean structure. I attacked one new claim: the sequence
   c = dim_5(h) − 2·a_d = (7,10,16,23,31,40), first diffs (3,6,7,8,9), second
   diffs (3,1,1,1) — momentarily looked quadratic with second diff 1.
   **REFUTED by parity alone**: the continuation needs c_14 = 49 (odd), but
   dim_14 = C(18,4) = 3060 (even), so a_16 = (3060−49)/2 = 1505.5 — not an
   integer, impossible for a monomial count. Clean closed dead-end; **no
   structure to report.** OEIS submittal of [7,10,16,23,31,40] → no match.

## Closed dead-end never previously filed

`code/sk_weight_hypothesis.py` — the rotational-weight-0 monomial-count
explanation of a_d — WAS run (commands.log line ~4803) and **REFUTED**:
`match=False` on all six terms (weight-0 counts 6,18,40,75,126,196 vs actual
4,30,97,236,485,890). This closed direction was never recorded as such; this
file records it.

## Tool caveat (re-confirmed, already filed)

`find_linear_recurrence` gives BOTH a false positive (spurious order-3
rational fit on a_d's 6 terms, coeffs 51814/10257, −95987/10257, 68576/10257
— does not survive) and a false negative (order-6 "no fit" on the true
order-4 a_j). Never trust it on huge/exponential sequences; verify with exact
elimination.

## Verdict

No new exact regularity to conjecture. Every sequence on disk is either fully
derived (the S_k family) or shows no clean structure (monomial counts, whose
several candidate regularities each die to a quick exact attack). NOTHING
FURTHER is warranted from this pass.
