# Index — code/lean

The Lean development. `Lib/` holds the statements; this folder holds nothing
else. `derived/LEMMAS.md` is derived from the files themselves and is the
authority on what has been checked — this index says what each file is *for*.

| File | Purpose |
| --- | --- |
| `Lib/Statement.lean` | The conjecture itself, as a type carrying every hypothesis, ending in `:= by sorry` |
| `Scratch/GoldbachSanity.lean` | Sanity-check of `IsGoldbach` against the problem's own examples (4=2+2, ¬2, 6, 8, 10, Even 2); `formalised` verdict, no sorries |
