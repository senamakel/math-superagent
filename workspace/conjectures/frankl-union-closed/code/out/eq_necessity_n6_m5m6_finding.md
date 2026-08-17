# Pattern-finder pass — EQ(n) = A053221 necessity lemma extended to n=6, |F| ≤ 7

## The surviving regularity, restated

**EQ(n)** = # empty-free union-closed families on `[n]` with
`f == min{N, 2k−N+1}` (KPT Thm 5(3) equality; f = # strict-abundant
elements, k = min set size, N = max set size). Verified:

```
EQ(1..5) = 1, 5, 16, 43, 106
A053221(n) = (n+2)·2^{n−1} − n − 1  →  1, 5, 16, 43, 106   EXACT
```

This is the run's **one closed-form regularity that survives the exact
sequence tools** (all other tables are structureless / uncatalogued / too
short). Status: **verified-computational n≤5, conjectural for all n**.

## The crux and its first falsifier

The single step separating the identity from a theorem is the **necessity
half**: is every EQ family a *singleton* `{A}` or a *strict two-chain*
`{A, A∪{x}}`? Equivalently, **is there NO EQ family with ≥ 3 sets?** If none
exists, the decomposition (singletons: `2^n − 1`; two-chains:
`n(2^{n−1} − 1)`) gives the closed form exactly.

**First falsifier:** an empty-free union-closed family on `n ≥ 6` with ≥ 3
sets achieving `f == min{N, 2k−N+1}`. At n=6 the closed form predicts
EQ(6) = 8·32 − 7 = **249 = 63 singletons + 186 two-chains**, so any ≥3-set
EQ family at n=6 refutes the lemma outright.

## New computation this pass

Prior work verified the necessity lemma (no ≥3-set EQ family) exhaustively at
n≤5 (all families) and at n=6 only for `|F| ∈ {2,3,4}`.
`code/out/eq_necessity_n6_m5m6.py` extends the n=6 check to **all family
sizes |F| = 5, 6, 7**, exhaustive (via `lib.uc`, exact integers).

```
range : ALL empty-free UC families on [6] with |F| in {5,6,7}, exhaustive
  |F|=5: UC families=57015  eq=0  non-single/twochain-equality=0  (2.4s)
  |F|=6: UC families=187997 eq=0  non-single/twochain-equality=0  (18.5s)
  |F|=7: UC families=553283 eq=0  non-single/twochain-equality=0  (146.2s)
TOTAL EQ families (|F|=5,6,7, n=6): 0
counterexamples to lemma (>=3-set EQ family): 0
```

**Result:** ZERO ≥3-set EQ families among all empty-free UC families on [6]
with |F| ≤ 7 (798,295 UC families checked). The first falsifier that was
being hunted is **not found** in this range.

## Status

- The necessity lemma (no ≥3-set EQ family) now holds exhaustively at n=6 for
  all |F| ≤ 7 (and all |F| at n≤5).
- **Still not a theorem.** |F| = 8 at n=6 is C(63,8) ≈ 9.9e9 subfamilies —
  beyond this run. And n=7 is entirely open. The lemma remains a structural
  conjecture for general n; the closed form EQ(n) = A053221 remains
  conjectural (verified-computational) beyond its derivation.

## Labels

- EQ(1..5) = A053221: **verified-computational** (exhaustive), closed form
  **derived** (sufficiency) / **conjectured** (necessity).
- n=6, |F| ≤ 7 lemma extension: **checked** (exhaustive, exact).
- Everything beyond (|F|=8 at n=6, all n≥7): **open**.

## Files

- `code/out/eq_necessity_n6_m5m6.py` — this pass's exhaustive check.
- `code/out/eq_necessity_n6_m5m6.captured.txt` — captured output.
- Prior: `code/out/eq_necessity_n6.py` (|F|∈{2,3,4}), `eq_clean_verify.py`,
  `eq_decomposition_verify.py`, `eq_a053221_derivation.md`.
