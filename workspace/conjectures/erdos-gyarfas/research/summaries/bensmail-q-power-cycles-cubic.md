# Bensmail, "On q-power cycles in cubic graphs", Discuss. Math. Graph Theory 37(1) (2017) 211–220

[[research/sources/bensmail-q-power-cycles-cubic.full.md]] · source URL: https://bibliotekanauki.pl/articles/31342133.pdf (arXiv/HAL mirror of DOI 10.7151/dmgt.1926)

## What it establishes

For any q ≥ 2, a **q-power cycle** is a cycle whose length is a power of q. The paper proves:

- **Theorem 9/14/18/22**: For every q ≥ 3, there exist **arbitrarily large planar cubic graphs with no q-power cycle** (q ≥ 6 as Theorem 9; then q=5, 4, 3 separately).
- **q = 2 case (Erdős–Gyárfás)**: There exist arbitrarily large cubic graphs **all of whose 2-power cycles have length 4 only, or 8 only**. The construction *cannot* eliminate 2-power cycles entirely — which is exactly why q=2 is the surviving hard case.

Also frames the two central conjectures:
- **Conjecture 1 (Erdős–Gyárfás)**: every graph with δ≥3 has a 2-power cycle.
- **Conjecture 2 (Caro)**: for every graph with δ≥3 there is a natural q≥2 such that G has a q^p-cycle for some p>1. EG (q=2) implies Caro's.

## Why it matters for this run

This is the decisive **counterexample-construction landscape** result. It shows:
1. The obstacle is q=2 specifically. For every q≥3 you can build arbitrarily large cubic graphs avoiding *all* q-power cycles; for q=2 you can thin 2-power cycles down to a single length (4 or 8) but not to none.
2. Therefore any proof of EG, and any would-be counterexample, is fighting over whether powers of two can be entirely excluded — and the known constructions cannot do it. This bounds how far a counterexample-searching SAT/SMS approach can plausibly push purely by construction: the sparsest known cubic graphs already contain length-4 or length-8 cycles.
3. Corollary 8 / Theorem 9 use **edge-gadgets** on planar cubic constructions — a technique a counterexample-builder would need, and which the run's structural approach must keep outside the reachable set.

**Claim block** (fenced for CLAIMS.md):

```claim
id: EG-Bensmail-q-power-constructions
statement: For every q≥3 there exist arbitrarily large planar cubic graphs with no q-power cycle. For q=2, there exist arbitrarily large cubic graphs whose only 2-power cycles have length 4 only, or 8 only.
hypotheses: simple cubic (and planar, for q≥3) graphs; explicit edge-gadget constructions.
holds-here: directly bounds the construction landscape for a counterexample to EG: known large cubic graphs still contain a 4- or an 8-cycle, so no known construction removes all 2-power cycles. It does NOT prove or disprove EG.
status: proved (source; constructions explicit, not machine-re-checked here)
bearing: the q=2 case is isolated as the hard one; a counterexample, if it exists, needs a construction technique the q≥3 literature does not provide.
anchor: research/summaries/bensmail-q-power-cycles-cubic.md
```
