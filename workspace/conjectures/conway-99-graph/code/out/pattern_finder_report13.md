# Pattern-finder report — round 13: independent re-derivation of report-12's tight-coclique identities; catalogue re-confirmed exhausted

## What changed since round 12

Round 12's `d_C = −s` and `r = k` family identities were asserted from a sympy
derivation and a 5-member table, but rounds 10–11 established the exact pattern
of error that survives until it is *re-derived by a second route*: a
parameter-identity missing a factor of 2 (the induced-C4 count was 2× too large
until independently brute-forced). Round 13 withholds report 12's claimed forms
and re-derives them from first principles, to decide whether they are a hardened
family theorem or an uncaught arithmetic slip.

## Finding — report 12's identities re-derive exactly from the SRG definitions (CONFIRMED, independent route)

Take a coclique `C` of an `srg(v,k,1,2)` meeting the Hoffman ratio bound
(`|C| = α = v·(−s)/(k−s)`). Equality forces the indicator vector
`f = 1_C − (α/v)·1` into the `s`-eigenspace. For any outside vertex `x` with
`d_C := |N(x) ∩ C|`:

```
(A f)_x = d_C·(1−α/v) + (k−d_C)·(−α/v) = d_C − α·k/v  =  s·(−α/v)   [equality]
   ⇒   d_C = α·(k−s)/v .
```

With `k = u²+u+2`, `v = 1+k²/2`, `s = −(u+1)`, sympy over symbolic `u` derives
the full set *without* being handed any claimed form:

```
α      = (u+1)(u²+2)/2
d_C    = u+1            ⇒  d_C − (−s) ≡ 0        (report 12's claim 1)
b = v−α = (u²+2)(u²+u+2)/2
r = λ(v'−1)/(k'−1) = u²+u+2 = k   ⇒  r − k ≡ 0    (report 12's claim 2)
b·k' − v'·r ≡ 0 ,  b·C(k',2) − λ·C(v',2) ≡ 0        (both design identities)
```

**Exact integer table** (all five feasible members `u∈{1,3,4,10,31}`):

| u | k | v | s | α | d_C | b | r | d_C=−s | r=k |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 9 | −2 | 3 | 2 | 6 | 4 | True | True |
| 3 | 14 | 99 | −4 | 22 | 4 | 77 | 14 | True | True |
| 4 | 22 | 243 | −5 | 45 | 5 | 198 | 22 | True | True |
| 10 | 112 | 6273 | −11 | 561 | 11 | 5712 | 112 | True | True |
| 31 | 994 | 494019 | −32 | 15408 | 32 | 478611 | 994 | True | True |

This is a **derivation** (every identity is a polynomial identity in `u`,
zero to sympy's exact simplification), not a fit. It cannot be falsified by any
member of the λ=1/tight-coclique family — it inherits from the SRG definition +
the equality-force hypothesis. The first-falsifying term is empty because the
identities are exact identities of the parameterization, and the only hypothesis
is *existence of a Hoffman-bound coclique*, which is the open question itself.
So they give a hard target a candidate graph must meet, not a nonexistence
force: `2-(22,4,2)` at 99 (`d_C=4, r=14, b=77`) is arithmetically feasible
(round 12's separate check). None of this separates 99 from the controls 9 and
243 (rook `2-(3,2,2)`, BvLS `2-(45,5,2)`).

## Sequence-tool sweep (exact over the terms, no new structure)

The `d_C` family `[2,4,5,11,32]` is exactly the linear `u+1` in the sparse
`a|63`-governed index set `u∈{1,3,4,10,31}` — not an independent recurrence.
The `b` family `[6,77,198,5712,478611]` has no order-≤4 constant-coefficient
recurrence and is the quartic `(u²+2)(u²+u+2)/2`. Both match the standing
catalogue rule: every parameter-determined family count is the same `a|63`
quartic family and none separates 99.

## Sequence-catalogue status: exhausted (re-affirmed)

No result files have appeared newer than `pattern_finder_report12.md` (only
`INDEX.md` and `commands.log`, the runtime's own, are newer). All 12 prior
rounds' sequences were re-confirmed already in rounds 11/12's independent
passes, and this round independently hardens the newest (report-12) claim.
The catalogue stands:

- **Parameter-determined family counts** (quartic-in-`u` closed forms from
  `k=u²+u+2`, `v=1+k²/2`, `a=2u+1|63`; all verified on both existing members;
  **none separates 99**): triangles, pentagons, hexagons, induced C4 (corrected,
  round 11), induced C5, K4−e (identically 0, a proof), outer blocks,
  distance-2, coclique bounds `{3,22,45,561,15408}`, eigenvalue multiplicities,
  C3 spectra (round 7), n3 cap `v·k(k−2)/4`, tight-coclique design `d_C=−s`,
  `r=k` (this round, hardened).
- **The only 99-specific quantities** that separate 99 from both controls
  remain exactly two: the **coclique bound 22** (round 3) and the forced
  **n3≥1 hence n3≥3** (Makhnev conditional, rounds 2/6). Neither has a
  parameter-determined sequence behind it — both are 99-specific values, and
  the live n3-lever was already shown to extend locally to every radius under
  the sound criterion (round 8 fixpoint).
- **The incidence p-rank** (round 9) is LIVE (varies between family members,
  3-rank 5 vs 231) but the 99 value is open and uncomputable without a graph.

## Bearing

The sequence line is genuinely done. Every parameter-determined count is the
same `a|63` quartic and is verified on both existing members; the two
99-specific levers (22-coclique design branch; forced n3≥3) are structural
values the sequence tools cannot extend or separate. The independent confirmation
of `d_C=−s` hardens the coclique-design foundation against the factor-2 class of
error, which is real value — but it opens no new 99-separating ceiling, and I
have twice now confirmed the same exhaustive conclusion rather than reaching.

## Files

- `code/out/pf_verify_round12_independent.py` — sympy first-principles re-derivation (input).
- Real output: the `d_C == −s` / `r == k` polynomial identities + the 5-member exact table (all True).
- `code/out/c3_spectrum_check.py` (re-run) — direct C3 spectrum confirms the corrected pairing on BvLS.
- This report.
