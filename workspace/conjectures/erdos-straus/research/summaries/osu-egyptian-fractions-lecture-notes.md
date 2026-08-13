# OSU lecture notes, "Egyptian fractions, Sylvester's sequence, and the Erdős-Straus conjecture"

Source: Ji Hoon Chun, "Egyptian fractions, Sylvester's sequence, and the Erdős-Straus
conjecture" (Ohio State University seminar notes, 2011-08-01).
Full text: `research/sources/osu-egyptian-fractions-lecture-notes.full.md`
(converted from https://math.osu.edu/sites/math.osu.edu/files/Egyptian_Fractions.pdf)

## What it establishes (course-note tier; orientation and classical background)

- **Greedy expansion length theorem**: for `m ≥ 2`, a fraction `m/n` has exactly
  `m` terms in its greedy (Fibonacci–Sylvester) expansion iff `n = km! + sm + 1`
  with `s ∈ S_m` (the set of residues of the greedy expansion of `m−1` mod `m`),
  `k ≥ 0`, not both zero. For `m = 4`, `S_4 = {0, 4}` (Theorem 3; a restatement of
  the classical a/m! + s/m + 1 criterion).
- **Consequence for Erdős–Straus**: the greedy algorithm produces 4-term (not
  3-term) expansions for `n ≡ 1 or 17 (mod 24)`. The 17 (mod 24) case is
  contained in `n ≡ 2 (mod 3)`, covered by the standard identity; the `1 (mod 24)`
  case is NOT covered by that shape ("No similar solution exists for the case
  n = 1 (mod 24) (Mordell 1967)") — the classical statement that the least
  reduced residue class needing special treatment is `1 mod 24`.
- **Context facts**: Stewart's two-unit-fraction theorem (reduced `m/n` is a sum
  of two unit fractions iff `m | n₁+n₂` for some factorization `n = n₁n₂` with
  coprime parts — stated as background); Webb's 1970 asymptotic density result
  (the proportion of possible counterexamples up to N tends to 0); the
  verification to `10^14` (Swett); the Sierpiński (`m=5`) and Schinzel
  (general `m`, `n ≥ n_0(m)`) generalizations.
- **History section**: Egyptian fraction origins (Rhind papyrus, 2/n table),
  Sylvester's sequence `e_0 = 2, e_n = e_{n-1}(e_{n-1}−1)+1`, and the classical
  `1 = Σ 1/e_n` identity.

## Relation to the library

- Course-note tier only: nothing here is load-bearing that is not already
  sourced from primary papers (Elsholtz–Tao, Salez, Schinzel, the Bloom–Elsholtz
  survey). Its unique value is the **exact statement and proof sketch of the
  greedy-expansion length theorem**, which explains *why* `n ≡ 1 (mod 24)`
  is the residue the greedy algorithm cannot resolve in three terms — the same
  residue all six open classes sit in.
- The "No similar solution exists for n = 1 (mod 24) (Mordell 1967)" sentence
  is an independent restatement of the Schinzel obstruction (b = 1 is a square
  mod 24, so no polynomial identity of the standard shape) from a lecture-note
  source; the precise theorem with proof is `research/sources/schinzel-three-unit-fractions.full.md`.

## Consequence for this run

None new: the six-class target set and the polynomial-identity obstruction are
already established from primary sources. This note adds only the greedy-length
backstory locating `1 mod 24` as the unavoidable residue.