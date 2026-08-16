# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Reduction.lean` | PE622 central reduction as a Lean statement: `OutShuffle.s_eq_orderOf` — for even n>=4, s(n) (out-shuffle restoration count) = orderOf (ZMod.unitOfCoprime 2 h), i.e. the multiplicative order of 2 mod n-1. Ends in `by sorry` (statement-first, as the directive requires); elaborates cleanly but not yet proved — lean-verdict outcome failed / 1 sorry, expected at this stage. |
| `Shuffle.lean` | PE622 out-faro shuffle formalisation. `OutShuffle.outShuffle n hpos h : Equiv.Perm (ZMod (n-1))` — one perfect riffle as multiplication-by-2 on the n-1 movable positions (requires 0<n-1 and Coprime 2 (n-1)). `OutShuffle.s n hpos h : ℕ` — minimal shuffles to restore, its `orderOf`. Verified by lean-verdict (outcome verified, axioms propext/Quot.sound/Classical.choice). First file in code/lean/Lib/ per the statement-first directive. |
