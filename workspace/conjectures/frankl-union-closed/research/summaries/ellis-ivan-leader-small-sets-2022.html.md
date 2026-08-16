# Ellis–Ivan–Leader, "Small Sets in Union-Closed Families" — arXiv:2201.11484 (2022)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2201.11484 (also arxiv.org/pdf/2201.11484).
> Full text: `research/sources/ellis-ivan-leader-small-sets-2022.html.full.md`.

The paper that settles the **3-set fault line**: containing a 3-element set
does **not** force the union-closed conjecture.

## What it establishes

- **Main theorem.** For any `ε > 0`, there exists a union-closed family `ℱ`
  with (unique) smallest set `S` such that no element of `S` belongs to more
  than a fraction `ε` of the sets in `ℱ`. More precisely: for each `k` there is
  a union-closed family with a smallest set of size `k` such that no element of
  that set belongs to more than a fraction `(1+o(1))·(log₂k)/(2k)` of the sets.
- For `k = 3` this is `(1+o(1))·(log₂3)/6 ≈ 0.264 < 1/2`. So a union-closed
  family can contain a 3-element set `S` with all three of its elements below
  `1/2` density — **UC is not a consequence of "contains a small set"**.
- **Contrast, precisely**: containing a singleton forces UC (that element is
  abundant); containing a 2-set forces UC (one of its two elements abundant,
  Sarvate–Renaud folklore); the 3-set case fails. This is exactly the fault
  line `problem.md` flags.

## Hypotheses and holds-here

- `ℱ` union-closed, finite. **Holds-here: yes.** This is a *counterexample to
  the small-set implication*, not to UC itself — these families may still
  satisfy UC via an element outside `S` or via a larger set. The construction
  shows the "unique smallest set is rare" route to a counterexample fails at
  `k=3`.

## What it lets the run do

- Disposes of "contains a 3-set forces UC" as a possibility; the elementary
  `k=1,2` cases are the only small-set implications that survive. Any approach
  that tries to prove UC for families containing a small set must *not* rely on
  the 3-set elements being abundant.

```claim
id: ellis-ivan-leader-small-set-3-fails
statement: For every ε>0 there is a union-closed family with unique smallest
  set S of size k such that no element of S is in more than
  (1+o(1))log₂k/(2k) of the sets; for k=3 this is ≈(1+o(1))log₂3/6<1/2. Hence
  containing a 3-element set does not force UC (contrast: singleton and 2-set
  do).
hypotheses: ℱ finite union-closed
holds-here: yes
status: proved (construction in-paper)
bearing: settles the 3-set fault line; only k=1,2 small-set implications survive
anchor: research/sources/ellis-ivan-leader-small-sets-2022.html.full.md
```
