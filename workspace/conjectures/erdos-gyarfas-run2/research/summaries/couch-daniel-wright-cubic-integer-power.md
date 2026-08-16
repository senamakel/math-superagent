# Couch, Daniel & Wright 2021 — integer-power cycles in cubic graph classes

Source: P. J. Couch, B. D. Daniel, W. P. Wright, "Classes of cubic graphs
containing cycles of integer-power lengths", Australas. J. Combin. 79(1)
(2021) 100–105. Full text held; [[couch-daniel-wright-cubic-integer-power.full]].

## What it establishes

Addresses **Caro's question** (weaker than E-G): every δ ≥ 3 graph has a cycle
of length a^k for some integers a ≥ 2, k ≥ 2 (a nontrivial power of some
natural number).

- **Lemma 1 (Paz's theorem 7.3):** For every positive integer m, and every n >
  14.4 |√[m]{1.5} − 1|^{−m}, there is a positive integer a with n < a^m < (3/2)n.
  Used to find integer powers in short intervals [2n, 3n].
- **Theorem 1:** a graph G containing a cycle D (not length 10; each vertex of D
  degree 3, each vertex of D in exactly one triangle, D meets each triangle in
  ≤ 1 edge) has a cycle of length a^k, a ≥ 2, k ≥ 2. (Contract triangles; use
  the [2n,3n] power table + Paz.)
- **Corollary 1:** every claw-free graph with δ ≥ 3 has a cycle of length a^k
  (a ≥ 2, k ≥ 2) — i.e. **Caro's question holds for claw-free graphs**.
  Corollary 2: claw-free δ ≥ 2, Δ ≤ 3, ≤ 2 degree-2 vertices, same. (Covers the
  Debose–Erdős–Hobbs narrowing.)
- **Theorem 2:** every graph with δ ≥ 3 whose set of **centers of induced claws
  is independent** has a cycle of length a^k. (Proof "left to the reader".)
- **Theorem 3:** every **almost claw-free** graph (centers of induced claws
  independent + for every x, γ(G[N(x)]) ≤ 2) with δ ≥ 3 has a cycle of length
  a^k.
- Remaining questions list restates the open E-G (power of 2), the open
  claw-free-power-of-2, and Caro's question.

## What it implies here

This is a settled-class result for **Caro's weaker question** (integer powers),
not for E-G's powers of 2. It confirms E-G's long-list of settled subclasses
claw-free almost-claw-free) only in the *weakened* integer-power form — the
power-of-2 version for claw-free is still open (Q2). The distinction matters:
it shows the claw-free direction is genuinely a Caro result, and that E-G's
stronger power-of-2 form is not yet settled even there. Also independently
**corroborates Bensmail** ("there exist arbitrarily large cubic graphs all of
whose 2-power cycles have length 4 only, or 8 only", cited as [1]).

```claim
id: cdw-clawfree-caro
statement: Every claw-free graph with δ ≥ 3 has a cycle of length a^k for some integers a ≥ 2, k ≥ 2 (Caro's weaker question), but not (yet) a power of 2.
hypotheses: claw-free, δ ≥ 3
holds-here: yes as a settled Caro result; the power-of-2 form stays open
status: proved (full text held)
bearing: distinguishes Caro's integer-power question (settled for claw-free) from E-G's power-of-2 question (still open); corroborates Bensmail
anchor: research/sources/couch-daniel-wright-cubic-integer-power.full.md
```

```claim
id: cdw-almost-clawfree-caro
statement: Almost claw-free graphs (centers of induced claws independent, every neighbourhood has domination number ≤ 2) with δ ≥ 3 have a cycle of length a^k.
hypotheses: almost claw-free, δ ≥ 3
holds-here: yes (weakened integer-power form only)
status: proved (full text held)
bearing: extends the claw-free settled class to almost-claw-free, again only in Caro's form
anchor: research/sources/couch-daniel-wright-cubic-integer-power.full.md
```

## What it does not settle

The power-of-2 case for claw-free graphs remains open (their Q2). Their
Theorem 2's proof is left to the reader (asserted, not shown).
