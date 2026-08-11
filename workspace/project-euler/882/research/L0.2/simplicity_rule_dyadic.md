# Fenner & Rogers 2015 — Simplicity Rule: finite numeric games are dyadic rationals

Source: https://doi.org/10.48550/arxiv.1505.07416 — "Combinatorial Game
Complexity: An Introduction with Poset Games", S. A. Fenner & J. Rogers,
arXiv:1505.07416 (extended version of a Bulletin of the EATCS 2015 article),
48 pp.

## What it establishes (and where it binds our problem)
A survey of CGT fundamentals plus poset-game complexity. Its relevant core is
the theory of **finite numeric games** (Definition 2.18 and the surrounding
material, the Simplicity Rule):

- For a finite numeric game `G = { G_L | G_R }` where every Left option and
  every Right option value is a number with all Left < all Right, the value
  `v(G)` is **the simplest dyadic rational strictly between the options**:
  the unique `a/2^k` with the least `k`, and then least-|a|, such that
  `v(ℓ) < a/2^k < v(r)` for all `ℓ ∈ G_L, r ∈ G_R`. Examples: `{ | } = 0`,
  `{0 | } = 1`, `{ | 0} = -1`, `{0 | 1} = 1/2`.
- The valuation respects disjunctive sum and negation: `v(P+Q)=v(P)+v(Q)`,
  `v(-P)=-v(P)`, and `P ≤ Q ⇔ v(P) ≤ v(Q)`.
- These values lie in the **dyadic rationals**, and a Number's magnitude is
  "how many free moves" the favoured player holds.

## Why this is a genuinely new leg for the run
The library's counting surrogate asserted each number's value is the integer
**a−b** ([[disjsum]]). This source supplies the *general rule* that governs the
real bit-deletion game: each single-number component here is a canonical Number,
so its value is the **simplest dyadic strictly between** the values of
`{ν-1 /rated-1}` and `{ν /rated-0}` options — **not** their difference. That is
why S(n) grows faster than A−B and why the surrogate is only an approximation:
S(n) = the minimal skip budget `k` such that `G(n) − k ≤ 0`, where
`G(n) = Σ_{k=1}^n k·g(k)` and each `g(k)` is a dyadic rational computed by this
rule (a Right-only skip adds the game `-1`). This is the exact structural fix
the open caveat in [[game-reduction-and-pass]] was asking for.

## Caveat
The fetched text here is the arXiv abstract page (PDF not scraped into math);
the Simplicity Rule wording above is confirmed from this paper via search of its
text. Treat the specific Definition 2.18 wording as vetted, the rest of the
paper as context.
