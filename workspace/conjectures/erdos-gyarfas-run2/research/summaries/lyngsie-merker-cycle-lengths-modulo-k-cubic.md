# Lyngsie–Merker, "Cycle lengths modulo k in large 3-connected cubic graphs"

**Source:** Kasper S. Lyngsie and Martin Merker, *Advances in Combinatorics* (2021),
doi:10.19086/aic.18971. Full text held at `sources/lyngsie-merker-cycle-lengths-modulo-k-cubic.full.md`
(arXiv PDF 1904.05076v2, open access). Landing page (Advances in Combinatorics, ccby-4.0)
held as material but the substantive article is the arXiv PDF.

## What it establishes (primary text)

**Theorem 1.1.** For every odd natural number k there exists N(k) such that every
3-connected cubic graph with at least N(k) vertices contains a cycle of length m modulo k
for every natural number m.

- Odd k is forced: bipartite graphs have no odd cycle, so even k fails.
- For even k not divisible by 4, the methods give that a sufficiently large 3-connected
  cubic graph has all odd residues or all even residues modulo k.
- For k divisible by 4, at least a quarter of residues are realized (all residues ≡ i mod 4
  for some i ∈ {0,1,2,3}).
- Best possible: the conclusion fails for 2-connected cubic graphs (constructed family
  when m, k divisible by 3 and k ≥ 12) and for 3-connected graphs of minimum degree 3.
- Theorem 1.1 extends Thomassen's 1983 conjecture (δ ≥ k+1 forces a cycle of length 2m
  mod k) to the sparse 3-connected cubic regime.

## Relevance to the Erdős–Gyárfás run

This is an *adjacent* congruence-class result on the class the run's strongest held proof
targets (3-connected cubic — where Heckman–Krakovski already proved the full E–G conjecture
in the planar case). It confirms that 3-connected cubic graphs have very rich cycle-length
spectra modulo odd k. But it realises lengths *in a residue class*, never a prescribed power
of two — so, exactly as the obstruction in problem.md states, it cannot by itself settle E–G
(a power of two is a specific integer, strictly stronger than membership in any residue
class). It is therefore context for the "congruence results don't get you to a power of two"
obstruction, and a reference anchor for the negative constructions it gives (2-connected
cubic graphs can avoid residue classes), not a proof step.

## Claim filed

`lm-modd-k-cubic`: Theorem 1.1 (3-connected cubic graphs of order ≥ N(k), k odd, realise
every residue class mod k), plus the best-possible / 2-connected-negative statement. Status
`asserted-by-source`, verified against full text. Holds-here: n/a (general structural fact).
Falsifier: a 3-connected cubic graph of order ≥ N(k) with no cycle of length ≡ m mod k for
some odd k and some m — would contradict the theorem, none known.

```claim
id: lm-modd-k-cubic
statement: For every odd k there is N(k) such that every 3-connected cubic graph with at least N(k) vertices contains a cycle of length m modulo k for every m. False for 2-connected cubic (constructed family when m,k divisible by 3, k ≥ 12) and false for 3-connected min-degree-3.
hypotheses: 3-connected cubic graphs, order ≥ N(k), k odd
holds-here: n/a — a general structural fact about the class the run's strongest held proof (Heckman–Krakovski, 3-connected cubic planar) targets; the run's δ ≥ 3 regime is broader
status: proved (full text held, source-verified)
bearing: 3-connected cubic graphs have very rich cycle spectra modulo odd k, but this realises lengths in a residue class, never a prescribed power of two — confirmation, at the strongest-sparse-class level, that congruence machinery cannot by itself settle E–G
anchor: research/sources/lyngsie-merker-cycle-lengths-modulo-k-cubic.full.md
answers: can-congruence-class-results-reach-a-prescribed-power-of-two (no, not by themselves)
```
