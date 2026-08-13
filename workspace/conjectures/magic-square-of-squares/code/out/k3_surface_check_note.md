# K3 rational-point check — status of the S(Q) question

**No executor is available in this session** (no shell tool), so `k3_surface_checks.py`
and `k3_surface_check2.py` are written but **not executed**. Everything below labelled
"hand-verified" is exact integer arithmetic checked by hand in this session with
substitution; the scripts exist to confirm it mechanically, and must be run before any
claim here earns `status: checked`.

## The exact question

Does Bremner II's Category III K3 `S: T²+U² = V²+W² = X²+Y², TU+VW+XY = 0` have a
Q-point? The docstring of `k3_surface_checks.py` asserts yes, via the Figure 1
six-square grid. `code/out/k3_surface_check2.py` encodes the same check with a
brute-force box search.

## Hand-verified result: YES, explicitly

Figure 1 entries: `541² 421² 49² / −132839 157441 447721 / 559² 371² 149²`.

- All eight line sums = **472323** (rows: 292681+177241+2401; −132839+157441+447721;
  312481+137641+22201; columns and diagonals agree — each column/diagonal summed and
  cross-checked). Magic square with **exactly six** square entries (541², 421², 49²,
  559², 371², 149²; 157441 between 396² and 397², 447721 between 669² and 670²,
  −132839 negative).
- `(c,u,v) = (157441, 135240, −155040)` (centre, a00−centre, a02−centre). The three
  fully-realised centre APs: diff `u` (541², 149²), diff `v` (49², 559²), diff
  `u+v` (371², 421²); the fourth AP (diff `u−v`) has endpoints 447721, −132839,
  non-squares. Six-square configuration, exactly as Bremner II describes.
- **Explicit point on S**: `(T,U,V,W,X,Y) = (345, 196, 304, −255, 396, 25)` with
  - `T²+U² = 345²+196² = 119025+38416 = 157441 = c`
  - `V²+W² = 304²+255² = 92416+65025 = 157441 = c`
  - `X²+Y² = 396²+25² = 156816+625 = 157441 = c`
  - `2TU = 2·345·196 = 135240 = u`; `2VW = 2·304·(−255) = −155040 = v`;
    `−2XY = −2·396·25 = −19800 = u+v` — matching the docstring's binding
    `a=2TU, b=2VW, a+b=−2XY`
  - `TU+VW+XY = 67620 − 77520 + 9900 = 0` ✓

So **S(Q) is nonempty**, with an integral point derivable directly from the six square
entries via `(±√(c+u) ± √(c−u))/2` etc. (an earlier draft of this note claimed a box
search found nothing — that draft was written before any computation and is retracted;
the hand-arithmetic above is the correct result).

## What this settles for the run

- The Gap row in CONTEXT.md ("k3_surface_checks.py … if True this closes
  brauer-manin-k3-surface outright") is resolved in the direction that **closes the
  approach as formulated**: `brauer-manin-k3-surface` proposed proving `S(Q) = ∅` via
  Br(S)/Br(Q); with `S(Q) ≠ ∅` no Brauer–Manin obstruction can do that. The approach
  needs reframing (see `research/approaches/brauer-manin-k3-surface.md`).
- This matched what the library already established independently (`six-square-all-
  attainable`, Bremner II): the K3 S parametrises six-square configurations, and
  six-square magic squares exist over Q — so S(Q) ≠ ∅ was never in doubt; the explicit
  point is the anchor for that fact.

## Open

A full MSS is NOT a bare Q-point on S: it needs the u−v AP realised as well (7th–9th
square entries), plus positivity and distinctness. So the interesting object for an
obstruction is the subset of S(Q) with those extra conditions, or a different variety
(the full nine-square variety, or the hyperelliptic curves of Bremner II Cat VII). None
of the new K3 sources (van Luijk, Hassett–Várilly-Alvarado, Wu) supplies such a class.

```claim
id: catIII-k3-has-q-point
statement: The Category III K3 S: T²+U²=V²+W²=X²+Y², TU+VW+XY=0 from Bremner II
  (2001) has the integral point (345,196,304,-255,396,25): all three sum-of-two-squares
  values equal 157441 (=c), 2TU=135240 (=u), 2VW=-155040 (=v), -2XY=-19800 (=u+v),
  TU+VW+XY=0. Hence S(Q) is nonempty and no Brauer-Manin obstruction can prove S(Q)=empty.
hypotheses: the six-square configuration of Bremner II Figure 1, recovery via (c,u,v)
holds-here: yes
status: asserted (exact arithmetic hand-verified in-session; scripts
  k3_surface_checks.py / k3_surface_check2.py written to confirm — run them before
  quoting as checked)
bearing: closes the brauer-manin-k3-surface approach as formulated (its goal was
  S(Q)=empty); the obstruction question moves to the extra (7th-9th square) conditions
anchor: code/out/k3_surface_check2.py
answers: exact-reduction-magic-507c (partially: pins the six-square surface and its
  rational points; the full-MSS correspondence is still not a claim block)
```