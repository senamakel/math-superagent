# Hegde, Sandeep & Shashank 2024 — P13-free graphs (computer-assisted)

Source: arXiv:2410.22842 "Erdős-Gyárfás conjecture on graphs without long
induced paths". Full text held as landing page / abstract only;
[[hegde-etal-p13-free.full]].

## Establishes

**Theorem:** every P13-free graph (no induced path on 13 vertices) with
minimum degree ≥ 3 contains a 2-power cycle; the argument uses a computer
search. (Survey cites the conjecture true for P13-free.) Hegde et al. state
the conclusion as C4 or C8 (same bounded form as the P8/P10 results).

## For this problem

The current frontier of the "no long induced path" direction, and the first
of the settled classes in this family to be *computer-assisted*. It shows the
P_k-free chain is still open, and that machine search is being used as a
lemma inside a proof — a precedent for how the oracle/SAT work slots into a
structural argument.

```claim
id: hegde-p13-free
statement: Every P13-free graph with δ ≥ 3 contains a cycle of length a power of two (computer-assisted proof).
hypotheses: P13-free, finite simple, δ ≥ 3
holds-here: yes (settled class)
status: asserted (abstract; proof body not held)
bearing: current endpoint of the P_k-free settled chain; precedent for computer-assistance inside a proof
anchor: research/sources/hegde-etal-p13-free.full.md
```
