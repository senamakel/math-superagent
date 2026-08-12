# Michaud-Rodgers, "Magic Squares of Squares", Warwick talk, 2019

[[michaud-rodgers-warwick-talk-2019]]

An undergraduate-level talk framing the full MSS problem as arithmetic geometry on the
"magic square variety" `X ⊂ P⁸` (the zero set of the seven homogeneous line-sum equalities,
with the entries' squares as the coordinates).

## What it claims (mostly sketch-level, not proof-level)

- **Dimension:** Hilbert polynomial of a Gröbner basis of `I(X)` has degree 2, so the magic
  square variety is a **surface**.
- **Singular points:** over C there are precisely **256 singular points**, each with three
  zero entries (three explicit families of matrices given, plus transposes / reflections).
- **Lines:** the full magic square variety **contains no lines**; the magic hourglass variety
  contains no lines; the *near* magic square variety (7 of 8 sums) contains infinitely many
  lines, a two-dimensional family (this explains the LS1-type squared-square abundance).
- **Curves:** eliminating variables lifts lines to curves; on the magic square variety there
  is a class of **degree-8 curves** (one explicit system given with `α=1/√−3`), but **none
  goes through any rational point** — presented as weak evidence for non-existence.
- Repeats Euler's 4×4 (sum 8515) and the `centre > 25×10²⁴` heuristic (attributed loosely).

## Implications for this run

- The "no lines on X" and "no rational point on the degree-8 curves" claims, if they can be
  pinned to precise statements, are geometric support for non-existence. But this is a
  *talk*, statements are asserted without proof and some are heuristic ("probably not,
  not a very convincing argument"). **Not a citable proof-level source**; verify each claim
  against a written source before relying.
- The full-MSS variety is a surface in P⁸ (intersection of six quadrics per Bremner II),
  whereas Bremner's K3 is a *six-square* surface — do not conflate the two objects.

## Does not help

As the talk itself disclaims, the centre bound and the "probably not" is explicitly admitted
to be unconvincing. The degree-8-curve-with-no-rational-points claim needs a written proof.

```claim
id: magic-variety-is-surface-no-lines
statement: The magic square variety X⊂P⁸ (coordinates are the entries; 7 homogeneous
  line-sum equations) is a surface with 256 singular points (over C); X contains no lines.
hypotheses: over C; X = full magic square variety
holds-here: unchecked (talk-level, no proof given)
status: asserted
bearing: candidate geometric support for non-existence; must be verified from a written source
anchor: research/sources/michaud-rodgers-warwick-talk-2019.full.md
```
