# Brouwer–Neumaier 1988, "A remark on partial linear spaces of girth 5…" — primary-source finding

Full text read and cited: `research/sources/brouwer-neumaier-1988-combinatorica.full.md`
(Combinatorica 8(1), 57–61, DOI 10.1007/BF02122552; final version PDF from CWI:
https://ir.cwi.nl/pub/1721/1721D.pdf).

## What the paper actually proves (Section 2, SRGs with μ=2)

**Theorem (Section 1):** a connected partial linear space of girth ≥ 5 and more
than one line, every point on λ neighbours, has *k ≥ λ(λ+3)/2* points.

**Corollary (Section 2):** *"A strongly regular graph with μ=2 and
k < λ(λ+3)/2 is a partial quadrangle; in particular it satisfies the divisibility
condition (λ+1)|k."*

In the SRG derivation: G regular of valency k, each edge in exactly λ triangles,
nonadjacent pairs have ≤2 common neighbours. Form H=Γ(x) (subgraph on neighbours
of x); points & maximal cliques of H form a partial linear space of girth ≥5.
By the Theorem, either k ≥ λ(λ+3)/2, or Γ(x) is a disjoint union of lines of
size λ+1 (then (λ+1)|k and G is itself a partial linear space).

## What this *means for (99,14,1,2)* — a correction of a false summary

A search summary earlier claimed Brouwer–Neumaier 1988 "eliminates"
(99,14,1,2). **That is FALSE.** The paper's own table of feasible μ=2 parameters
lists, verbatim:

```
99  14  1   3  -4   54  44   ?
```

with `?` = existence unknown. The corollary applies only when k < λ(λ+3)/2;
for (99,14,1,2) we have λ=1 so λ(λ+3)/2 = 2, and k=14 ≥ 2, so the corollary's
partial-quadrange conclusion (and its (λ+1)|k = 2|14) does **not** force a
contradiction. (Even if it did: 2|14 holds trivially.) The 1988 paper does NOT
resolve the 99 problem; it leaves it open. 243 is marked
"Berlekamp-Seidel-van Lint graph" (exists).

This also **kills claim c6's worry** about the 99 case from this direction: the
relevant bound for 99 is λ(λ+3)/2, satisfied, not 12λ(λ+3).

## The Bagchi "12λ(λ+3)" discrepancy that persists — needs the oracle

Bagchi (Discrete Math. 2006), Theorem 4 as reported: *"any SRG with μ=2 is
either a grid graph or k ≥ 12λ(λ+3)"*, proof via: k<12λ(λ+3) ⇒ (by
Brouwer–Neumaier [5]) the graph is K_{1,1,2}-free ⇒ (Lemma 1) collinearity graph
of a GQ, and t+1=μ=2 ⇒ grid.

**Apparent contradiction:** BvLS (243,22,1,2) exists, λ=1 ⇒ 12λ(λ+3)=48, k=22<48,
yet BvLS is not an n×n grid (grids have v=n²; 243 is not a square and the only
μ=2 lattice L₂(n) has λ=n−2=1 ⇒ n=3 ⇒ v=9, not 243). So Bagchi's Theorem 4 as
quoted would rule out the real BvLS graph.

The only consistent escape: **BvLS is NOT K_{1,1,2}-free** (so it falls outside
the theorem's force), or the "12λ(λ+3)" bound is misquoted. NOTE: this is a
genuine unresolved discrepancy in the library. The oracle (tool_builder / coder)
must determine whether BvLS contains an induced K_{1,1,2}. If it does, Bagchi's
theorem does not apply to it and there is no contradiction; if it does not,
Bagchi's Theorem 4 as reported is wrong or misquoted and must NOT be relied on
against (99,14,1,2).

**Consequence for the run:** do NOT use Bagchi's "grid or k≥12λ(λ+3)" as a
nonexistence weapon for (99,14,1,2) until the BvLS/K_{1,1,2} question is settled
by computation. The 243 graph is the canonical counterexample test.

## Also recorded (from the BN1988 table)

The feasible μ=2 sub-2000 parameter list (v,k,λ | exist): 4,2,0 (C4, unique);
16,5,0 (Clebsch, unique); 56,10,0 (Gewirtz, unique); 85,14,3 (?); 99,14,1 (?);
243,22,1 (BvLS); 300,26,4 (?); 352,26,0 (?); 456,35,10 (claw-bound ruled out);
630,37,4 (?); 704,37,0 (?); 736,42,8 (ruled out here); 875,46,9 (ruled out here);
1176,50,4 (?); 1276,50,0 (?); 1625,58,3 (?); 1944,67,10 (ruled out here);
1961,70,15 (ruled out here).

This is the definitive 1980s classification of μ=2 feasibility < 2000. (99,14,1,2)
and 243 both table-listed open/existing — consistent with the whole literature.

---

```claim
id: brouwer-neumaier-1988-99-open
statement: Brouwer-Neumaier 1988 (Combinatorica 8:57-61) does NOT rule out
  srg(99,14,1,2); its μ=2 table lists (99,14,1) with eigenvalue spectrum
  3^54, -4^44 and status '?' (open). The paper's corollary (SRG with μ=2 and
  k < λ(λ+3)/2 is a partial quadrangle with (λ+1)|k) does not apply to
  (99,14,1,2), for which λ=1, λ(λ+3)/2=2, and k=14 ≥ 2.
hypotheses: none beyond reading the paper's own full text.
holds-here: yes — directly fixes the status of the 99 case from the primary
  source and corrects a false secondary summary.
status: sourced (full text read and quoted).
bearing: prevents the run from spending effort proving 99 nonexistence with
  a theorem the paper does not state; resets (99,14,1,2) to genuinely open.
anchor: research/sources/brouwer-neumaier-1988-combinatorica.full.md,
  research/notes/brouwer-neumaier-1988-finding.md
```

```claim
id: bagchi-bvls-contradiction-pending
statement: RESOLVED — superseded by c6-resolved-no-bite. The naive reading of
  Bagchi 2006 Thm 4 ("SRG with μ=2 is a grid or k ≥ 12λ(λ+3)") appears to
  contradict the existence of BvLS (243,22,1,2): λ=1 ⇒ 12λ(λ+3)=48, k=22<48,
  and BvLS is not an n×n grid. The contradiction dissolves once Lemma 1's
  second branch is restored: BN1988 gives that a μ=2 SRG with k<12λ(λ+3)
  (=48) is K_{1,1,2}-free — so BvLS (k=22<48) IS K_{1,1,2}-free — and Lemma 1
  then says a K_{1,1,2}-free SRG is either a GQ collinearity graph or else
  k ≥ (λ+1)(λ+2)=6; BvLS (k=22) and 99 (k=14) both satisfy k ≥ 6, so neither
  is forced to be a grid. No contradiction; the reported "grid or k≥48"
  statement is a simplification, and the decisive step failing for both 99
  and 243 is condition (ii) k ≥ (λ+1)(λ+2).
hypotheses: Bagchi's theorem as reported by the two library summaries; Lemma 1
  quoted verbatim in bagchi-mu2-dichotomy-resolution.md (primary Bagchi full
  text paywalled 403).
holds-here: yes — resolved; BvLS/99 both escape via branch (ii). No oracle
  K_{1,1,2} computation is needed because BN1988 already forces BvLS to be
  K_{1,1,2}-free (k=22<48), and the escape is branch (ii), not non-freeness.
status: resolved (reasoned: the naive route would rule out the existing BvLS
  graph, so it is refuted on arrival; consistent with the BN1988 primary full
  text in-library).
bearing: Bagchi Thm 4 must NOT be cited as a 99-nonexistence route; the exact
  failing step is condition (ii) k ≥ (λ+1)(λ+2)=6, satisfied by both 99 (k=14)
  and 243 (k=22). Contradicts superseded phrasing that called this unresolved.
anchor: research/notes/brouwer-neumaier-1988-finding.md,
  research/notes/bagchi-mu2-dichotomy-resolution.md
```
<!-- reconciled in scholar-digest-pass-3; superseded by bagchi-bvls-contradiction-resolved -->
```
