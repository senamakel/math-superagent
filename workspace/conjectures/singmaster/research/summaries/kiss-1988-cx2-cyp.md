# Kiss 1988 — C(x,2) = C(y,p), p prime: effectively finite

Source: P. Kiss, "On the number of solutions of the Diophantine equation
C(x,2) = C(y,p)", The Fibonacci Quarterly 26(2) (1988) 127–130. Primary;
scanned PDF held at `research/sources/kiss-1988-cx2-cyp.full.md` (OCR of the
article body is legible; the issue front-matter is garbled and ignored).

## Statement (from the primary text, read this run)

- **The infinite family (equation (1))**: restates the Lind/Singmaster/Tovey
  classification — the equation has infinitely many solutions, and (attributed
  to Tovey) *all* solutions are given by a Fibonacci parametrization.
- **Avanesov's complete solution of Sierpiński's conjecture**, recorded on
  p. 127: the triangular = tetrahedral equation has only the pairs
  `(x,y) = (3,2), (5,5), (10,16), (22,56), (36,120)`, i.e. `C(x,3) = C(y,2)`.
  Checked: C(5,3)=C(5,2)=10; C(10,3)=C(16,2)=120; C(22,3)=C(56,2)=1540;
  C(36,3)=C(120,2)=7140; (3,2) is the degenerate row C(3,3)=C(2,2)=1. The
  three nontrivial triangular=tetrahedral values **120, 1540, 7140 are three
  of the six N=6 witnesses** — so Avanesov's list is the oracle any (2,3)
  computation must reproduce.
- **Kiss's theorem**: for every fixed odd prime p ≥ 3, `C(y,p) = C(x,2)` has
  only finitely many positive integer solutions (x,y).
  - Proof mechanism: `C(y,p)=C(x,2)` ⟺ `y² − y = (2/p!)·(x)_p` ⟹ hyperelliptic
    equation `z² = (8/p!)·(x)_p + 1` with z = 2y−1.
  - Lemma 2: `f(x) = (x)_p + p!/8` has only simple roots (via
    `f(x) − x·f′(x)` being Eisenstein-irreducible at p for p>3; p=3 checked
    directly).
  - Lemma 1 is **Baker 1969** (superelliptic effective finiteness: f with ≥ 3
    simple roots ⟹ f(x) = b·z^m has finitely many solutions with an
    effectively computable bound).
  - So the theorem is **effective** (a computable C(p) exists) but **the
    constant is not evaluated in the paper**.

## Bearing for this run

- The k=2 column with p prime is effectively finite **per p** — the same shape
  as de Weger/BMSST (per-pair effective), **not uniform in k**. Baker's
  constant depends on the height of (8/p!)(x)_p+1, hence grows with p;
  this is `effective-methods-wall` again, now with a 1988 primary.
- **Genus consistency check**: the curve z² = (8/p!)(x)_p+1 has degree p in x
  with all roots simple, so hyperelliptic genus (p−1)/2 for odd p — exactly
  the run's closed form g(2,p) = ((1)·p − 0 − gcd(p,2))/2 = (p−1)/2 for p odd.
  p=3 gives genus 1 (Mordell elliptic curve); p=5 gives genus 2 (the BMSST
  hyperelliptic curve); p ≥ 7 gives genus ≥ 3, where Kiss's Baker-1969
  argument is the best known (no BMSST-style sieve exists there).

## Status

Sourced from the primary this run; the two parametrizations above were
re-verified numerically by hand-computation in this note (10, 120, 1540, 7140
checks). The Baker-1969 constant evaluation is not performed — that is a live
GOAL-eligible task (`G-constant-evaluation` in BACKWARD.md).

```claim
id: kiss-1988-cx2-cyp-effective-finiteness
statement: Kiss 1988 (Fibonacci Quart. 26(2) 127-130, primary, full text held):
  for each fixed odd prime p >= 3 the equation C(y,p)=C(x,2) has only finitely
  many positive integer solutions; the proof reduces to Baker 1969 (effectively
  computable bound) on z^2 = (8/p!)(x)_p + 1, whose degree-p polynomial has only
  simple roots (Eisenstein argument). The constant is effective but unevaluated
  in the paper and depends on p: per-p effective, NOT uniform in k. The same
  page records Avanesov's complete list for (2,3): C(x,3)=C(y,2) has exactly
  (x,y) = (3,2),(5,5),(10,16),(22,56),(36,120), giving witness values
  120, 1540, 7140.
hypotheses: p odd prime, fixed; effectivity per-p with unevaluated constant;
  the C(x,p)=C(y,2) labels in the theorem are symmetric in the equation.
holds-here: yes - the k=2 column carries all known witnesses; the (2,3) list
  is the check oracle for any (2,3)-specific computation.
status: sourced (primary, full text read this run; arithmetic re-verified here)
bearing: the k=2 column is effectively finite per prime p - NOT a uniform-in-k
  bound; consistent with effective-methods-wall; Avanesov's list constrains
  any N(a) counting argument at the (2,3) witnesses.
anchor: research/summaries/kiss-1988-cx2-cyp.md
```