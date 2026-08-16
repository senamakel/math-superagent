# Goal

Settle **COLLAPSE** (`problem.md`) as a finite question about one explicit `F₂`
matrix. It is a linear-algebra and combinatorics problem. It contains no primes
and the answer must not depend on any.

## Why this run exists

A previous investigation built eight independent second-moment routes and every
one of them reduced, at the coarsest dyadic scale, to the same short-range
correlation statistic. That was observed eight times and never proved.

**This run decides whether that is a theorem or an artifact of the eight.**

Both answers are results and neither is a disappointment:

- **A theorem** says the fold `Φ` is structurally incapable of seeing past
  short-range correlations. Any problem downstream of `Φ` is then exactly as
  hard as the corresponding pair-correlation statement — no harder, and no
  easier. That closes a question about what is worth attempting.
- **A refutation** produces a functional that sees further, and with it a route
  nobody has taken.

Say which it is. Do not leave it indicated.

## Priorities

1. **Describe the multiset `{ M_d △ M_{d'} }` exactly.** The sizes are already
   known in closed form (imported result 3). What is missing is *which sets
   occur*, with multiplicity. This is a finite computation at small `n` and is
   very likely the crux — get it early and let it drive everything else.
2. **Compose items 4, 6 and 7 of `problem.md`.** A run collapses to its two
   endpoints; a fold cell is a product over run endpoints; pairwise symmetric
   differences are small. Those three facts are the collapse mechanism stated
   in three pieces. Determine whether they compose into a proof, and if they do
   not, name precisely the step that fails.
3. **Hunt for the witness in parallel.** Do not assume the collapse holds.
   Search small `n` exhaustively for two strings with identical pair
   correlations and different `S²`. If one exists the problem is over and a
   week of proof attempts is saved. This is cheap — do it first and keep doing
   it as the order of correlation is refined.

## Rules

- **Check before conjecturing.** At `n ≤ 20` everything here is exhaustively
  enumerable. A statement that has not been checked at small `n` should not be
  written down.
- **State the `n` range on every claim.** A fact verified to `n = 12` and a fact
  proved for all `n` are different objects and must never be filed as the same.
- **Every settled conclusion gets a fenced claim block** with `id`, `statement`,
  `hypotheses`, `holds-here`, `status`, `bearing`, `anchor`. Mirror the id in
  `research/ROOT.md`.
- **Negative control in every verification, shown failing.** The parent run
  shipped a capture of 51 million passes that measured nothing until a
  deliberately broken variant was run beside it and produced 438 failures.
- **One canonical oracle.** Write `Φ_n`, `M_d` and `S(n,h)` once, in `code/lib`,
  cross-checked against a brute-force submask enumeration. No role writes a
  second implementation.
- **Write to a temp file and move on exit 0.** Five captures in the parent run
  were found at zero bytes because a redirection truncated on open and the
  command then failed. An empty capture is a failed run, not a missing one.
- **Lean claims need `#print axioms`.** No `sorryAx` under a note calling a
  theorem sorry-free.

## Out of scope

Gilbreath's conjecture, the supply bound `ν₂ ≥ c·n`, prime gaps, the parity
barrier, and anything mod 4. Those belong to the parent problems and are
already proved, refuted or open there. If you find yourself needing a fact
about the primes, you have left this problem.
