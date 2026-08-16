# Heckman & Krakovski 2013 — Cubic planar graphs

Source: "Erdős–Gyárfás Conjecture for Cubic Planar Graphs", Electron. J.
Combin. 20(2) #P7 (2013). Full proof text held:
[[heckman-krakovski-cubic-planar-proof.full]] (114 KB). This is the one full
discharging proof in the library.

## What it establishes

**Theorem 1.1 (main):** Every 3-connected cubic planar graph contains a
2^m-cycle for some 2 ≤ m ≤ 7. (i.e. length in {4, 8, 16, 32, 64, 128}.)

- Proof: Discharging Method in a novel way; long and computer-based in parts.
- Not known whether 1.1 is tight; possibly m ∈ {2,3,4} suffices.

**Corollary 1.2 (bounded local structure):** There is an absolute constant c
such that every 3-connected cubic plane graph G has a face f with |f| ≤ 71
and a subgraph H ⊆ G with |V(H)| ≤ c such that: f ⊆ H; every v ∈ V(H) is
within path-distance ≤ 6 of some u ∈ V(f); and H contains a 2^m-cycle, 2 ≤ m
≤ 7. Implies a linear-time algorithm to detect a 2^m-cycle.

**Lemma 1.3 (face intersection):** In a 3-connected cubic plane graph, two
distinct faces are disjoint or meet in exactly two vertices u, v with uv an
edge. (Uses that the dual of a 3-connected plane graph is simple.)

**Context captured:** Markström verified cubic graphs of order ≤ 29 (the 29
in this paper's wording), the four 24-vertex no-C4/C8 cubic planar examples
(one is Fig 1, the smallest 3-connected cubic planar with no 4- or 8-cycle),
Shauger's K_{1,m}-free and Daniel–Shauger's planar claw-free results.

## What it implies here

- A settled restricted class with exact hypotheses (3-connected, cubic,
  planar) and a concrete conclusion (a 2^m-cycle, m ∈ [2,7]). One of the ≥ 3
  settled classes ROOT.md needs.
- The discharging local-structure corollary is the model for how a confined
  argument works on cubic graphs: find a small face/subgraph and locate a
  power-of-2 cycle inside a bounded ball. Any attack that hopes to transfer
  to general min-degree-3 will need an analogous local confinement, which is
  exactly what the sparse-powers obstruction says is hard in general.

```claim
id: hk-cubic-planar
statement: Every 3-connected cubic planar graph contains a cycle of length 2^m for some 2 ≤ m ≤ 7.
hypotheses: finite simple, 3-connected, cubic, planar
holds-here: yes (a settled restricted class, not the general problem)
status: proved (journal-published discharging proof, computer-assisted)
bearing: settled class; template for bounded-local confinement arguments
anchor: research/sources/heckman-krakovski-cubic-planar-proof.full.md
```

```claim
id: hk-face-local
statement: Every 3-connected cubic plane graph has a face f with |f| ≤ 71 and a bounded subgraph H (|V(H)| ≤ c) within distance 6 of f containing a 2^m-cycle.
hypotheses: 3-connected cubic planar
holds-here: yes
status: proved
bearing: locality template; linear-time detection corollary
anchor: research/sources/heckman-krakovski-cubic-planar-proof.full.md
```
