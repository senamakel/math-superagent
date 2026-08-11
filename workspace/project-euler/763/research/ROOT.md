# research — what this now establishes

Top of the tree. Batches of originals in `L0.<n>/`; one seal note per
sealed batch a level up. What the whole library lets this run treat as
known, under 1000 tokens, each claim wikilinking its note.

## Established

The OEIS closed-form hunt for D(N) is closed: **D(N) is not a
Motzkin-family sequence; no catalogued closed form found.** Four Motzkin
variants were checked; all agree it is not one, so this is established,
not conjectured.

- **The family diverges at term 3.** D(N) = 1,1,3,9,30,99,336,...
  (BFS-verified, `MEMORY.md`). Every candidate gives Motzkin's
  1,1,2,4,9,21,... or a shift — close-looking, divergent at n=2.
- [[oeis_a001006]] Motzkin numbers (main entry; closed forms,
  recurrence): NOT D(N), mismatch from n=2.
- [[oeis_a086246]] Motzkin variant 0,1,1,1,2,4,9...: matches through
  n=1 only; not D(N).
- [[oeis_a168049]] Motzkin variant 1,0,1,1,2,4,9...: matches through
  n=0 only; "essentially A086246"; not D(N).
- [[oeis_a005207]] (F(2n-1)+F(n+1))/2 = 1,1,2,4,9,21,51,...: diverges
  from D(N) at n=2; not D(N).

## The four notes are recorded dead ends

Each was filed to see whether a catalogued closed form would turn D(N)'s
enumeration into an evaluation; each was ruled out on its low terms. The
run should not pursue a Motzkin/Fibonacci closed form for D(N) — D(N)'s
growth (×3.4 frontier factor per division, `MEMORY.md`) is not reproduced
by these sub-exponential families past a few terms. Look for genuinely
different structure (the amoeba's crossings/shortfall) instead.
