# The 3×3 magic square of squares

## Statement

> Do there exist nine **distinct positive integers** whose squares can be placed
> in a 3×3 grid so that all three rows, all three columns, and both main
> diagonals have the same sum?

Formally: do there exist distinct positive integers $a_1,\dots,a_9$ and a
constant $M$ such that the grid of $a_i^2$ has every row, column, and main
diagonal summing to $M$?

The question is **open**. No such square has been found and no proof of
non-existence is known. Popularised by Martin Gardner, who offered $100 for one;
raised in this form by Martin LaBar in 1984. Euler constructed a 4×4 magic
square of squares, which is *not* this problem — the 3×3 case is the hard one,
and the difference is structural rather than one of size.

**Read this before choosing a direction.** The working assumption for this run
is that a full resolution is out of reach, and the deliverable is a genuine
partial result stated exactly, with its hypotheses, not a claim of the
conjecture in either direction.

## The parametrisation, which is where every attack starts

Any 3×3 magic square with magic constant $M$ has centre $M/3$, and is fully
determined by its centre $c$ and two parameters $u, v$:

```
  c + u        c - u - v    c + v
  c - u + v    c            c + u - v
  c - v        c + u + v    c - u
```

So the problem is: choose $c, u, v$ such that **all nine of those entries are
perfect squares**, and the nine are distinct and positive.

Two consequences that a first attempt must not rediscover:

- The centre is itself a square, $c = e^2$.
- The four lines through the centre — two diagonals, the middle row, the middle
  column — are four **three-term arithmetic progressions of squares** all
  sharing the same middle term $e^2$, with common differences $u$, $v$,
  $u+v$, $u-v$. Every attack has to confront that: the four differences are not
  independent, and it is that dependence, not the existence of APs of squares,
  that is doing the work.

Three-term arithmetic progressions of squares are plentiful and completely
understood; a middle term lying in *four* of them with those four differences in
that additive relation is what nobody can rule out and nobody can produce.

## What is known, as leads to verify rather than as facts

Everything below is a **lead**. Verify each against a primary source, record it
in `research/CLAIMS.md` with its exact hypotheses and a `status`, and correct
this file where it is wrong. Do not build on any of it until it is anchored.

- **Near-misses with seven square entries exist.** Several are known, and one
  is famous enough to have a name — the "Parker square", which fails as a magic
  square rather than merely as a square-entry one. Andrew Bremner and Lee
  Sallows are the names to search on. *This is the single most important thing
  to establish precisely, for the reason in the oracle section below.*
- **Eight square entries.** Whether eight is attainable, and whether any
  example is known, is a distinct question from seven. Establish which of
  seven, eight, nine is actually open and what the best construction is.
- **The elliptic-curve reformulation.** The system is widely reported to reduce
  to rational points on a surface — an elliptic surface or a K3 — where the
  question becomes one about ranks or about rational points on a curve of
  higher genus. Bremner, *On squares of squares* (Acta Arithmetica), is the
  paper to find. Get the reduction *exactly*: which variety, which points
  correspond to solutions, and what is actually proved about it. A vague
  "it's an elliptic curve" is worth nothing here.
- **Congruent numbers and concordant forms.** Three-term APs of squares with
  common difference $d$ are the classical congruent-number setup. Whether the
  four-difference condition maps onto a known concordant-forms problem is worth
  settling early, because if it does, a large literature applies.
- **The computational bound.** Exhaustive searches are reported past $10^{25}$.
  Find the actual bound, whose search it was, what exactly was searched (centre?
  magic constant? entries?), and by what method. A search bound is a fact about
  a range, not evidence about the answer, and it must be stated as one.

## The obstruction, stated as the thing to beat

A proof of non-existence must produce a contradiction from the nine
square conditions. Every cheap route is already known to fail:

- **Congruences alone will not do it.** Squares are constrained mod 8, mod 16,
  mod 3, mod 5, and one can derive real restrictions on $c, u, v$ from them.
  But a sieve that only uses congruences cannot succeed, because the system is
  locally solvable — there are solutions modulo every prime power. Any argument
  that appears to work purely modularly has an error in it, and the way to find
  the error is in the oracle section below.
- **Descent needs the right variety.** An infinite-descent or Fermat-style
  argument needs the reduction to be exact first. Do the geometry before the
  descent.
- **A search is not a proof and never becomes one.** Extending a bound from
  $10^{25}$ to $10^{27}$ is a fact about a range. It is worth doing only if it
  falsifies a structural claim this run made, and it should be stated that way.

## Which direction to attack

The user's brief asks for a proof of **non-existence**. Take that as the primary
direction, and record honestly that it may be the wrong one: a finite search
bound is not evidence of impossibility, several experts regard existence as open
in both directions, and a run that spends its whole budget trying to prove a
false statement has produced nothing. So:

- Pursue non-existence as the main line.
- Keep one thread open on **existence**: what would a construction have to look
  like, which parametrised families have been exhausted, and does any partial
  result *predict* where a solution would live?
- If the non-existence line produces a lemma that also forbids a **known**
  near-miss, that lemma is false and the run has learned something real. Say so
  loudly rather than quietly dropping it.
