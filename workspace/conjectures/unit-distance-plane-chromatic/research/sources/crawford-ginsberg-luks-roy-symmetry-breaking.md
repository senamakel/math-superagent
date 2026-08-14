# Symmetry-breaking predicates for search problems — Crawford, Ginsberg, Luks, Roy 1996

**Source:** James Crawford, Matthew Ginsberg, Eugene Luks, Amitabha Roy,
"Symmetry-Breaking Predicates for Search Problems", in *Principles of Knowledge
Representation and Reasoning (KR-96)*, Morgan Kaufmann, 1996, pp. 148–159.
URL: https://www.cs.uoregon.edu/frames/reports.php?report=TR-1996-012
(technical report version; also bibtex.github.io/KR-1996-CrawfordGLR.html).
Fetched server-side via read_sources.

## What this establishes

A general scheme for exploiting symmetry in propositional (SAT) and constraint
satisfaction problems by **adding symmetry-breaking predicates** to the theory:

- Works on any propositional satisfiability problem, and as a pre-processor to
  any systematic or non-systematic reasoning method.
- **Full** symmetry breaking is intractable in general, but **partial**
  symmetry-breaking predicates can be generated efficiently.
- For several specific symmetry groups, symmetries can be broken fully or
  partially with a **polynomial number of predicates**.
- Implemented and tested on two classes of constraint-satisfaction problems.

## Why it matters here

The run's complete k-colourability oracle (GOAL.md oracle 2) is an exhaustive
or SAT-based colouring test. A k-colouring problem has an enormous symmetry
group — the k! relabellings of the colour classes — and any search over
colourings wastes nearly all its time rediscovering permutations of one
colouring. This paper is the standard technique for breaking exactly that
symmetry with added predicates (e.g. lex-leader constraints
colour(v1) <= colour(v2) <= ... <= colour(vk) fixing the first occurrence order
per colour), which is the difference between a colouring search that terminates
in seconds on a few hundred vertices and one that does not terminate at all.
The run already uses symmetry-broken colouring search (claim G-oracle-calibrated
mentions "complete symmetry-broken k-colourability"); this source is the
primary justification for that design.

## Venue correction for FRONTIER

The frontier's row for this paper says "cited by Computing Small Unit-Distance
Graphs with Chromatic Number 5 (1996, cited 420 times)" — that row carries a
misleading date/venue. The paper is KR 1996 (Fifth International Conference on
Principles of Knowledge Representation and Reasoning), pp. 148–159, Morgan
Kaufmann. It is not an AAAI paper. Authors: Crawford, Ginsberg, Luks, Roy.
(When the citation graph row is re-derived, the venue is KR-96.)

## Note on download

Downloaded via server-side read_sources (Oregon technical report page + KipHub
bibliographic entry). Technique-tier source (symmetry breaking for SAT/CSP), not
answer-tier material for the Hadwiger–Nelson problem.

```claim
id: symmetry-breaking-sat-technique
statement: Adding symmetry-breaking predicates to a propositional theory is a sound, general technique for reducing redundant search in SAT/CSP (Crawford, Ginsberg, Luks, Roy, KR 1996, pp. 148-159): full breaking is intractable in general, but partial breaking with a polynomial number of predicates works for several common symmetry groups. For graph colouring the colour-permutation symmetry can be broken by lex-leader-style constraints fixing the order in which colours first appear.
hypotheses: propositional satisfiability / constraint satisfaction problem with a known symmetry group (e.g. colour relabellings); predicates added are sound (do not remove all solutions unless symmetry-equivalent).
holds-here: yes — the run's complete colouring oracle is a symmetry-broken SAT/exhaustive k-colouring search; this is the primary source for that design, and it justifies expecting the oracle to terminate quickly on a few hundred vertices.
status: sourced (abstract read verbatim; the colouring-symmetry application is the standard textbook use of the technique)
bearing: underpins oracle 2's design (GOAL.md); a faster, complete colouring test is what lets the construction loop test larger graphs.
anchor: research/sources/crawford-ginsberg-luks-roy-symmetry-breaking.md
```