# Quantifier elimination for real closed fields by cylindrical algebraic decomposition — Collins

**Source:** G.E. Collins, "Quantifier Elimination for Real Closed Fields by
Cylindrical Algebraic Decomposition", Lecture Notes in Computer Science 33
(Springer 1975), 134–183; preliminary report SIGSAM Bulletin 8(3) (1974),
80–90; exposition ACM SIGSAM Bulletin 10(1) (1976),
doi.org/10.1145/1093390.1093393
**Full text:** NOT on disk — read via server-side search results and citations
in the AMP paper ("double exponential runtime... impractical for graphs on at
least 10 vertices").

## What this establishes — the decision procedure for the G-exhaust sentence

- **Tarski's theorem (basis).** The elementary (first-order) theory of real
  closed fields admits quantifier elimination, hence a decision method: every
  first-order sentence over the reals is decidable.
- **Collins's CAD (algorithm).** Cylindrical algebraic decomposition makes
  quantifier elimination algorithmic: decompose R^r into cylindrically arranged
  cells on which the input polynomials have constant sign, then read off the
  truth of the quantified sentence. This is the standard general-purpose way to
  decide sentences like "there exist n points whose pairwise squared distances
  lie in {0,1} and whose induced graph is not 4-colourable".
- **Complexity.** The decision method is (in practice) doubly exponential in
  the variables/degrees — Collins 1975/1976 with rigorous time analysis; the
  AMP embeddability paper states CAD is impractical for graphs on ≥ ~10
  vertices. This is precisely why the run's oracle must be an exact
  embedder/unit_graph pair rather than a CAD call at full size.

## Why it matters here

The size-lower-bound skeleton's `G-exhaust` gap is the sentence "no 5-critical
unit-distance graph on ≤ N vertices exists", which is a first-order sentence
over R (existential over points with pairwise squared distances in {0,1},
universal over 4-colourings after expanding the finite colouring quantifiers
into a disjunction of polynomial sign conditions — to be developed by
symbolic_math). CAD/Tarski give the *decision-theoretic guarantee* that this is
decidable exactly, while the complexity note justifies the run's practical
choice: exact symbolic construction plus SAT for the colouring test, with CAD
only a fallback for tiny N.

```claim
id: cad-decidability-exhaust
statement: The first-order theory of real closed fields is decidable (Tarski 1948; Collins CAD 1975 gives an algorithm), so the sentence "there exist n <= N points in R^2 with pairwise squared distances in {0,1} whose induced graph is not 4-colourable" is a decidable sentence; CAD is however doubly exponential in practice and impractical beyond small instances.
hypotheses: real closed fields = the ordered field R; the sentence must be first-order with polynomial predicates.
holds-here: yes - the G-exhaust sentence is first-order over R; practical oracle must avoid full CAD.
status: sourced (Collins 1974/1975/1976; Tarski 1948; complexity per Amp 2412.11914's statement)
bearing: decision-theoretic grounding of G-exhaust as a decidable finite question; justifies exact-construction + SAT over CAD at full size.
anchor: research/sources/collins-cad-1975.md
```

## Note on download

Full text not on disk (publisher blocked; ACM SIGSAM Bulletin not downloaded).
Status: **sourced via search results and citation context; full text not on
disk**.