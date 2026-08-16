# Carr 2026 — Diameter-2 graphs contain a C4 or C8

Source: A. Carr, "Cycles of Length 4 or 8 in Graphs with Diameter 2 and
Minimum Degree at Least 3" (arXiv:2508.19302, updated Jan 2026). Full proof
held; [[carr-diameter2-c4-c8.full]].

## What it establishes

**Theorem 1.1:** every finite simple graph G with diam(G) = 2 and δ(G) ≥ 3
contains a cycle of length 4 or 8. Hence the Erdős–Gyárfás conjecture holds for
the class of diameter-2 graphs.

The proof assumes no 4-cycle. For an edge v1v2, v1 has neighbours v3,v4 and v2
has neighbours v5,v6 (besides each other). If v3=v5 and v4=v6 (or the crossed
version v3=v6, v4=v5), a 4-cycle forms immediately, contradiction. So it
considers the two cases v3=v5 and v3≠v5, using the diameter-2 (every nonadjacent
pair has a common neighbour) and δ≥3 constraints to force either a 4- or an
8-cycle.

## What it implies here

A settled restricted class (diameter-2). Its value is the mechanism: the proof
uses a *local* degree lower bound interacting with a *global* diameter
constraint to force a **short, bounded** power (C4 or C8). This is exactly the
"bounded local confinement" idea that Heckman–Krakovski use on cubic planar
graphs via discharging, now via diameter. It does not transfer to general δ≥3
(unbounded diameter), so it does not attack the full conjecture — but it is one
more settled class for ROOT.md and evidence that short-power forcing works when
a global constraint pins down local structure.

```claim
id: carr-diameter2
statement: Every finite simple graph with diameter 2 and minimum degree ≥ 3 contains a cycle of length 4 or 8.
hypotheses: diam(G)=2, δ ≥ 3, finite simple
holds-here: yes (settled restricted class)
status: asserted (arXiv preprint; proof body held, not independently re-verified)
bearing: settled class; another instance of global constraint + δ≥3 forcing a short bounded 2-power
anchor: research/sources/carr-diameter2-c4-c8.full.md
answers: whether-diameter2-is-open (no — settled)
```
