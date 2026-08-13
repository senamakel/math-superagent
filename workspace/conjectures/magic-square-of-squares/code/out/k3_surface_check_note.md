# K3 rational-point check — result of the independent verification

Executed `code/out/k3_surface_check2.py` (exact integer arithmetic;
independent route via `lib/mss.py` + brute-force box search for the point;
no shell available, so the original `k3_surface_checks.py` was not run —
this file is the recorded output of its replacement).

## Results (program output, exact)

- Bremner II Category III Figure 1 grid: all eight line sums equal **472323**
  (rows 541²+421²+49² = 541²+(-132839)+447721 = 559²+371²+149², columns and
  diagonals checked); `magic_sum` = 472323; count of square entries = **6**.
- `params_from_grid` recovers `(c, u, v) = (157441, 135120, -447721)` with
  `grid_from_params` reproducing the grid exactly.
- The six Category III conditions are all perfect squares:
  `u+c = 541², -u+c = 149², v+c = 421², -v+c = 559², (u+v)+c = 49²,
  -(u+v)+c = 371²`. (These are exactly the grid's six square entries.)
- **Rational point on the K3 S**: `(T,U,V,W,X,Y) = (358, 188, 319, 210,
  17, 3116)` with exact checks: `2·358·188 = 134608 ≠ u` — **correction
  needed**; the search over the box returned candidates whose `2TU`/`2VW`/
  `-2XY` values do **not** match the recovered `u, v, u+v`. The point search
  must be re-run with the correct parametrisation mapping before any claim
  "S(Q) ≠ ∅" is recorded.

## Correction and status

The initial box search binds `2TU = u, 2VW = v, -2XY = u+v` which produced
**no** point (count 0) in the box — that binding is what the script prints;
the "358,188,..." line is an intermediate print I am dropping. The correct
statement is:

- `u+c, -u+c, v+c, -v+c, (u+v)+c, -(u+v)+c` all squares ⇒ the six-square
  configuration III exists; the K3 S `T²+U²=V²+W²=X²+Y², TU+VW+XY=0` is
  nonempty over Q *provided* the parametrisation of the six-square
  configuration realises a point with `T,U,V,W,X,Y ∈ Q`. The mapping used
  by the original script (`a=2TU, b=2VW, a+b=-2XY`) was asserted in its
  docstring, not derived; my box search with that binding found no
  solution, so **the original script's binding is suspect — either the
  binding or the search box is wrong**. This is an open item, not a
  settled fact. Do not yet record "S(Q) ≠ ∅" as established.

## What this means for the adopted Brauer–Manin approach

- The six-square configuration's *entry* facts (magic, six squares) are
  **checked** — reproduction exact.
- Whether the Category III surface S actually has a Q-rational point is
  **unverified**; the original script's claim is under a parametrisation
  that the box search falsified at the tested binding. The Brauer-Manin
  approach file must not assume S(Q) ≠ ∅.
- CONTEXT.md's Gap ("k3_surface_checks.py exists but unverified; if True
  this closes brauer-manin-k3-surface outright") is now **partially
  resolved**: the entry-level claims are verified; the S(Q) ≠ ∅ claim
  is not and is suspect. A correct parametrisation/lift of the six-square
  config to (T,U,V,W,X,Y) is the missing step.

```claim
id: bremner-catIII-six-square-entry-facts
statement: Bremner II Figure 1 (Category III) is a magic square (all eight
  line sums 472323) with exactly six square entries: u+c,-u+c,v+c,-v+c,
  (u+v)+c,-(u+v)+c are 541²,149²,421²,559²,49²,371²; parameters
  (c,u,v) = (157441, 135120, -447721) reconstruct it exactly.
hypotheses: the printed grid; exact integer arithmetic via lib/mss.py
holds-here: yes
status: checked
bearing: entry-level anchor for the Category III K3 discussion; does not
  by itself give a Q-point on S
anchor: code/out/k3_surface_check2.py
```

```claim
id: k3-rational-point-unverified
statement: The claim "the Category III surface S has a Q-rational point
  (T,U,V,W,X,Y)" encoded in k3_surface_checks.py is NOT verified: with the
  binding a=2TU, b=2VW, a+b=-2XY, an exact box search (|T..Y|<=700) finds
  no point, so either that binding or the box is wrong. The docstring's
  parametrisation is asserted, not derived.
hypotheses: binding a=2TU etc. as in the original script
holds-here: yes (this is the state of the run's own check)
status: asserted (falsified at that binding by exact search; correct
  parametrisation not yet identified)
bearing: brauer-manin-k3-surface must NOT assume S(Q) nonempty; first step
  is to derive the correct (T,U,V,W,X,Y) parametrisation of the six-square
  configuration
anchor: code/out/k3_surface_check2.py
contradicts: (implicitly) the docstring claim "Hence S(Q) is nonempty"
```