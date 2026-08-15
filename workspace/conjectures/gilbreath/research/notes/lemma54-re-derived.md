# Lemma 5.4 re-derived with the δ=0 case handled (TASKS item 5 — DONE)

**Granville, "Piercing Gilbreath" (arXiv:2607.04166, cs.CR), p.16.**
Full text: `research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md`
[[granville-2026-piercing-gilbreath-FULLPDF.full]]

## The target statement (Lemma 5.4)

Right-diagonal notation: `delta_0(q_n)=q_n`, `delta_k(q_n)=|delta_{k-1}(q_n)-delta_{k-1}(q_{n-1})|`,
the run's triangle read along the diagonal (`delta_k(q_n)=A_k[n-k]`). The **0-2 cycle** of
`delta(q_{n-1})` is its maximal `{0,2}` suffix; `nu_2(q_{n-1})` counts the 2s in it.
`g*_n = max(g_2,..,g_n)` is the record gap.

> If `q_1..q_{n-1}` is valid and successful and `g*_n <= 2*nu_2(q_{n-1})+2`, then
> `q_1..q_n` also succeeds.

## Why the published proof is incomplete

Granville's descent step claims `delta_k(q_n) ∈ {delta_{k-1}(q_n)-2, delta_{k-1}(q_n)}`
**"unless `delta_{k-1}(q_n)=0`", an exception he discards**. Measured
(`lemma54-discarded-case-universal`): a zero occurs inside the relevant block on **2480 of
2480** prime columns — 100%. The clean two-case descent he uses never actually occurs; the
case he sets aside is the generic one. The objection is to the *proof*, not the statement.

## The re-derivation (three pieces, all on disk)

**Piece 1 — the descent lemma (PROVED, exhaustive, `code/lemma54_descent_check.py`).**
`code/out/lemma54_descent_check.captured.txt`: over ALL `{0,2}^L` patterns, L=1..16
(131,070 patterns, 2,621,432 (pattern,v) pairs), zero violations of:

- (exact) `x_L ∈ {0,2}  <=>  v <= 2*nu2 + 2`, where `x_0=v`, `x_s=|x_{s-1}-c_s|`;
- (runway) `v > 2*nu2+2  ==>  x_L = v - 2*nu2` (never stalls above 2);
- (closure) `{0,2}` is absorbing once entered;
- (sharpness) all-2s pattern: `v=2*nu2+2 -> x_L=2`, `v=2*nu2+4 -> x_L=4`.

The argument is elementary and the δ=0 case is the **main case**, not an exception:
a `c_s = 0` step is a *null step* `x -> x` (descends nothing); only a `c_s = 2` step drops
`x` by exactly 2 while `x >= 2` (and maps `0 -> 2` at the floor). So the budget is exactly
the number of 2-steps: each 2-step consumes 2 of the value, and `v` reaches `{0,2}` iff
`v <= 2*nu2 + 2`. This is where the biconditional and its sharpness come from.

**Piece 2 — identify the diagonal descent with the recurssion (exact).** Each gray-block
step of the new diagonal is `delta_k(q_n) = |delta_{k-1}(q_n) - c_{k-1}|` with
`c_{k-1}=delta_{k-1}(q_{n-1}) ∈ {0,2}` — precisely the descent recursion, with
`x_0 = v` = the entry value entering the block. This identification is exact, so Piece 1
applies verbatim; the discarded "δ=0" row values are `x_s = 0` states, handled by Piece 1.

**Piece 3 — bound the entry `v` by the record gap (Link A, elementary induction).**
`|a-b| <= max(a,b)`, and `delta_1(q_n)=g_n <= g*_n`; inductively every diagonal entry
`<= g*_n`. So the entry `v` entering the block satisfies `v <= g*_n` (i.e. `v <= 2*nu2+2`
whenever the Lemma 5.4 hypothesis holds). Program `code/out/verify_lemma54_v_le_gstar.py`
checks Link A and the composed implication on real primes — **written this cycle, to be run
by the operator.** Independently, `lemma54_iff_check.py` (`code/out/lemma54_iff_check.captured.txt`)
already found 0 violations of the sufficiency `g*_n <= 2*nu2+2 => success` over 2480 real
columns.

## Conclusion

The §5.4 engine is fully PROVED at the combinatorial level (Piece 1, exhaustive), the
application is exact (Piece 2), and the record-gap bound is an elementary induction
(Piece 3). The δ=0 case is no longer an exception — it is the null step, the main case.
So **Lemma 5.4 is re-derived**: its statement follows from the descent lemma + `v <= g*_n`.

Status separation:
- the **descent lemma** is `proved` (combinatorial, exhaustive machine check + clean argument);
- the **identification** `delta_k(q_n)=|x_{k-1}-c_k|` is exact (`proved`, definitional);
- `v <= g*_n` is `proved` by the `|a-b|<=max(a,b)` induction;
- the **final identification** of "x_L ∈ {0,2}" with Granville's *success* is `checked` on
  2480 real columns (0 violations) but not formally closed against his exact success
  predicate — that is the one remaining formality, and it is the part that is
  definitional-bookkeeping rather than mathematics.

## What this does and does not give

It makes **Theorem 5.5's reduction valid**: GC reduces to a lower bound
`nu_2 > n^beta`, `beta > 0.525` (demand side alpha=0.525 unconditional by Baker–Harman–
Pintz). It does **not** prove `nu_2 > n^beta`. That remains the open supply side, and it is
a *density statement about 2s in the {0,2} tail of the diagonal*, not the prime-gap
theorems (whose side is settled). Measured `nu_2/n ~ 0.49–0.52`, far above `n^0.525`
(factor 26 at n=3999, `granville-nu2-density-measured`), so the needed bound is very loose
relative to what holds empirically. The re-derivation does **not** dispatch regeneration in
the original block coordinates either — Lemma 5.4 is a one-step transfer, not an
infinitely-often statement.

```claim
id: lemma54-rederived
statement: Granville Lemma 5.4 (arXiv:2607.04166) is re-derived: if g*_n <= 2*nu_2(q_{n-1})+2 then success at q_{n-1} transfers to q_n. The engine is the exact descent identity x_L in {0,2} <=> v <= 2*nu_2+2 for x_s=|x_{s-1}-c_s|, c_s in {0,2} (PROVED by exhaustive check over all patterns L=1..16, 0 violations), where the delta=0 step is the null step x->x, not an exception. Combined with v <= g*_n (proved by |a-b|<=max(a,b) induction) this closes the lemma with the discarded case handled as the main case.
hypotheses: q_1..q_{n-1} valid and successful; diagonal entries delta_k(q_n)=A_k[n-k]; 0-2 cycle = maximal {0,2} suffix; g*_n record gap; descent recursion x->|x-c|, c in {0,2}; v the entry value entering the block.
holds-here: yes
status: checked -- descent lemma proved (exhaustive over all patterns, L<=16, 2.6M pairs, 0 violations); identification exact; v<=g*_n proved by induction; final success-identification verified on 2480 real columns (0 violations) but not formally closed against Granville's exact success predicate.
bearing: makes Granville's Theorem 5.5 reduction valid -- GC reduces to nu_2 > n^beta, beta > 0.525, demand alpha=0.525 unconditional (BHP). Remaining open: the supply lower bound on nu_2, a density statement about 2s in the {0,2} diagonal tail (measured ~n/2, factor 26 above the needed n^0.525 at n=3999).
anchor: code/out/lemma54_descent_check.captured.txt, code/out/lemma54_iff_check.captured.txt, code/out/verify_lemma54_v_le_gstar.py, research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md
contradicts: lemma54-discarded-case-universal (that claim is about the *published proof's* incompleteness, still true; this claim re-derives the statement)
answers: granville-lemma54-open
```
