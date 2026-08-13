# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it. It carries what an agent would otherwise
rebuild from disk, from the note store, or from a session it was not present
for. Not a file catalogue (`research/INDEX.md` is) and not a narration of what
agents did.

Token budget 10,000; file is re-sent on nearly every model call, so length is a
bill the whole run pays many times over. Link the file that holds detail
compressed away.

## Established

- **The three witnesses, computed and checked** (exact integer arithmetic, `code/out/witnesses.json`):
  `2^0 = 1 = 1_3`, `2^2 = 4 = 11_3`, `2^8 = 256 = 100111_3`. These are the
  falsification oracle: **every claimed obstruction must be run against them**.
  A lemma that forbids digit-free `2^n` for all `n` above some point, but also
  forbids `n = 8`, is false — record it as refuted, not weakened. A lemma not
  run against the witnesses is `asserted`, never `checked`.
- **Verification bound reproduced, computed and checked**: exhaustive `n=0..2000`
  by exact big-int base-3 expansion finds **no digit-`2`-free value of `2^n`
  besides `0, 2, 8`** (`witnesses.json`). This is the bound the run has actually
  reproduced; anything computed past it is new.
- **Structure, sourced** (standard, stated in `problem.md`): the multiplicative
  order of `2` mod `3^k` is `2·3^(k-1)` for `k ≥ 1`. Hence `2^n mod 3^k` depends
  only on `n mod 2·3^(k-1)`, and the digit-avoidance sieve on residue classes is
  `A_k = { n mod 2·3^(k-1) : low k ternary digits of 2^n mod 3^k lie in {0,1} }`.
  `|S_k| = 2^k` out of `3^k`; `A_{k+1}` refines `A_k`.
- **Shape of a proof (conjectured, not shown)**: if `|A_k| → 0` after removing
  the classes containing `n = 0, 2, 8`, the conjecture is proved for all `n`
  outside those classes. Whether `|A_k| → 0` or stabilises is the central open
  question; **`|A_k|` as a function of `k` is the first experiment and has not
  been computed yet.**

## Ruled out

No run-approach has been attempted yet, so nothing is closed. Two arguments are
already known to be true-and-irrelevant heuristics, never proofs (`problem.md`,
`GOAL.md`):
- **Density argument**: "density of integers whose ternary expansion avoids `2`
  tends to 0" is true but says nothing about the thin sequence `2^n`.
- **i.i.d.-digits heuristic**: gives `(2/3)^k`, explains why the conjecture is
  believed, proves nothing (no mechanism exhibited).
Neither is to be recorded as a proof.

## Numbers

- Witnesses verified: `1_3`, `11_3`, `100111_3` for `n = 0, 2, 8`.
- Exhaustive digit-free search, `n = 0..2000`: none besides `0, 2, 8`.
- `|A_k|` sieve counts: **not yet computed** — first open experiment.

## Recalled

No durable Cognee memory on this problem yet (recall_memory/relate_memory and
search_claims both empty). Nothing to import; hypotheses of any future recalled
claim must be checked against this problem before relying on it.

## Contradictions

- The **naive count obstruction** (`problem.md`, `GOAL.md`): `|A_k| ≈ 2·3^(k-1)·(2/3)^k ≈ 2^k/3` — the naive estimate **grows**, does not tend to 0. So `|S_k|/3^k → 0` (good) yet the indexed count needed is not monotone-down from this estimate. Any approach must say how it beats this estimate or why it is wrong. State it in `research/ROOT.md` before proposing an approach.

## Gaps

- `|A_k|` counts across `k` (and which classes survive with `n = 0, 2, 8` identified among them).
- Narkiewicz (1980) bound: exact statement, explicit constant, and method not yet found/reproduced — unverified until reproduced here or attributed to a primary source.
- Digit-omission literature (`a^n` in base `b` omitting a fixed digit) and the finite-automaton / Cobham-angle not yet gathered.
- `research/ROOT.md`, `FRONTIER.md`, `CLAIMS.md` not yet written; neither is `code/lib` populated (no `sieve(k)` / `digit_free` helpers yet — `code/lib/INDEX.md` lists none).
