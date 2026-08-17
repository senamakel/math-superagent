# Dumitrescu — "The Dirac–Goodman–Pollack Conjecture" (arXiv:2204.06101)

> **Source:** `https://arxiv.org/pdf/2204.06101` (held: `research/sources/dumitrescu-Dirac-Goodman-Pollack-conjecture-arxiv2204.06101.full.md` — this holds the arXiv abstract page; the digest below is from the abstract).

## What it establishes

**Dirac's conjecture** (geometric form): any set of $n$ noncollinear points in
the plane has a point incident to at least $c n$ connecting lines determined by
the point set (some constant $c>0$). Goodman–Pollack gave combinatorial
generalizations of this and two other problems in their allowable-sequences
framework; the conjectured generalization of Dirac is:

> Any nontrivial allowable $n$-sequence $\Sigma$ has a local sequence $\Lambda_i$
> whose **half-period** is at least $c n$.

**Result (this paper):** the Dirac–Goodman–Pollack conjecture is **confirmed with
concrete bound $c = 1/845$**.

## Bearing on this run — adjacent, not a tool

- The **Dirac conjecture / connecting-lines** question is about how many distinct
  connecting lines pass through a point — a different invariant from convex
  position. It is **adjacent** to ES(n) and does NOT bear on the upper bound
  $\mathrm{ES}(n)\le 2^{n-2}+1$.
- Its value here is methodological: it is a proof *within the* **allowable
  sequences** framework (the same order-type / allowable-sequence abstraction the
  run's structural thread and the signotope machinery use, cf.
  [[felsner-weil-sweeps-arrangements-signotopes-2001]]). It shows the
  allowable-sequence language supports clean quantitative (half-period / local
  sequence) statements — a model of the kind of structural lemma the
  [[extremal-structure]] thread wants, though for a different functional.
- For the full primary **framework digest** (circular/allowable-sequence
  definitions, local sequences, and the point-vs-pseudoline realizability
  distinction with claim `dumitrescu-allowable-framework-primary`), see the HTML
  version [[dumitrescu-Dirac-Goodman-Pollack-conjecture-arxiv2204.06101-html]].
- **Not** a restricted class of the ES conjecture and **not** evidence for
  $\mathrm{ES}(n)=2^{n-2}+1$. Do not let it drift into Established as such.

```claim
id: dumitrescu-dgp
statement: The Dirac-Goodman-Pollack conjecture — every nontrivial allowable n-sequence has a local sequence whose half-period is at least c n — is true with concrete bound c = 1/845 (extending Dirac's geometric conjecture that some point of an n-point noncollinear set lies on cn connecting lines).
hypotheses: allowable sequences (order-type abstraction) framework; n noncollinear points.
holds-here: no — adjacent problem (connecting lines / allowable-sequence half-period), NOT the convex-position ES(n) upper bound.
status: asserted-by-source (concrete bound c=1/845 confirmed in the paper; abstract/announcement held, full proof not in library).
bearing: methodological — a quantitative structural statement proved inside the same allowable-sequence/order-type language the run's extremal-structure thread works in; not a tool for the ES(n) constant.
anchor: research/summaries/dumitrescu-Dirac-Goodman-Pollack-conjecture-arxiv2204.06101.md
```
