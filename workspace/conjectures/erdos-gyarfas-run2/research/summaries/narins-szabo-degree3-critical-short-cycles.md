# Graphs without proper subgraphs of minimum degree 3 and short cycles

**Narins, Pokrovskiy, Szabó**. Combinatorica 37 (2017) 495–519;
arXiv:1408.5289. **FULL TEXT HELD** at
`research/sources/narins-szabo-degree3-critical-short-cycles.full.md`
(arXiv HTML, 71 KB). Earlier download was the paywalled Springer abstract;
this replace it.

<!-- source: https://ar5iv.labs.arxiv.org/html/1408.5289 -->

## What it establishes

Studies **degree-3-critical graphs**: $n$-vertex, $2n-2$ edges, no proper
*induced* subgraph of minimum degree 3. (Historical note: the original EFGS
"proper subgraph" wording is argued by NPS to mean induced; removing "induced"
completely changes Theorem 1.4.)

- **Theorem 1.2**: There is an infinite sequence of degree-3-critical graphs
  $(G_n)$ containing **no cycle of length 23**. This **disproves** the EFGS
  conjecture that every degree-3-critical graph has cycles of all lengths
  $3,4,5,\dots,C(n)$ with $C(n)\to\infty$. (Erdős et al. had shown lengths
  3,4,5 and $\lfloor\log_2 n\rfloor$; every degree-3-critical graph ≥6 vertices
  contains a C6, shown in Sec 5. So the shortest missing forced length is
  between 6 and 23.)
- **Theorem 1.3** (even 1–3 trees): (i) some $N_0$ with every even 1–3 tree of
  order ≥ $N_0$ having leaf-leaf paths of lengths $0,2,4,\dots,18$; (ii) an
  infinite family of even 1–3 trees with **no leaf-leaf path of length 20**.
  This is the engine of the counterexample.
- **Theorem 1.4**: If $G$ is $n$-vertex with $2n-2$ edges and **no proper
  (not necessarily induced) subgraph** of minimum degree 3, then $G$ is
  **pancyclic** (cycles of every length $3,\dots,n$). Follows from a
  structure theorem: only two families exist — wheels, and wheels with one
  edge replaced by another graph.
- **Construction G(T)** (Sec 2): for a tree $T$, add two new vertices $x,y$,
  edge $xy$, and join both $x,y$ to every leaf of $T$. If $T$ is a 1–3 tree,
  $G(T)$ is degree-3-critical.
- **Lemma 2.1** (cycle-length↔leaf-path dictionary): for even 1–3 tree $T$,
  (i) $G(T)$ has a $(2k+1)$-cycle ⟺ $T$ has a leaf-leaf path of length $2k-2$;
  (ii) $G(T)$ has a $2k$-cycle ⟺ $T$ has two vertex-disjoint leaf-leaf paths
  $P_1,P_2$ with $e(P_1)+e(P_2)=2k-4$, or a single leaf-leaf path of length
  $2k-2$.

## Relevance to this run

- This is the **primary source** that the held Di Braccio et al. (Combinatorica
  2026) and Rautenbach notes build on — now held in full. The G(T) construction
  and Lemma 2.1 give the exact mechanism by which **cycle lengths in a
  degree-3-critical graph are governed by leaf-leaf path lengths in a 1–3
  tree**, which is precisely the structural content the run's near-cubic spine
  needs.
- Degree-3-critical graphs are the exact structural class of the minimal
  counterexample spine (a minimal counterexample has no proper induced subgraph
  with δ ≥ 3). So Theorem 1.2 is a strong caution: **degree-3-critical graphs
  can avoid a specific cycle length (23) at arbitrarily large order** — the
  near-cubic spine alone does not force a power-of-two cycle; the degree-guard
  δ ≥ 3 is doing essential work beyond degree-3-criticality.
- The characterisation (degree-3-critical = unions of two edge-disjoint
  spanning trees via Nash-Williams; rigidity circuits via Laman) is a further
  structural handle.

## Status

Theorem statements are read from the source (full text); not independently
recomputed. The counterexample construction and Lemma 2.1 are verified as
present in the text but not machine-checked. This closes the open request for
the NPS full text.

```claim
id: nps-degree3-critical-no-23-cycle
statement: There is an infinite sequence of degree-3-critical graphs (n vertices, 2n-2 edges, no proper INDUCED subgraph of min degree 3) that contain no cycle of length 23; hence the EFGS conjecture (all cycles 3,4,...,C(n), C(n)->inf) is false.
hypotheses: G degree-3-critical (induced sense), arbitrarily large n
holds-here: yes (minimal E-G counterexamples are degree-3-closed downward, so this is the natural structural class; but it does NOT settle E-G)
status: asserted (full text held)
bearing: CAUTION for the near-cubic spine -- degree-3-critical graphs can avoid a fixed cycle length (23) at arbitrarily large order, so 3-criticality alone does not force a power-of-two cycle; the delta>=3 guard beyond 3-criticality does real work. Also gives the G(T) construction and Lemma 2.1 dictionary (2k±1-cycle in G(T) iff leaf-leaf path of related length in T).
anchor: research/sources/narins-szabo-degree3-critical-short-cycles.full.md
```

```claim
id: nps-even-13-tree-leaf-lengths
statement: Every even 1-3 tree (all degrees 1 or 3, all leaves in the same bipartition class) of order ≥ N0 has leaf-leaf paths of lengths 0,2,4,...,18; and there is an infinite family of even 1-3 trees with no leaf-leaf path of length 20.
hypotheses: even 1-3 tree; N0 a universal constant
holds-here: yes
status: asserted (full text held)
bearing: engine of the degree-3-critical counterexample (length-20-missing trees yield 23-cycle-missing graphs G(T)); quantifies the shortest leaf-leaf length NOT forced (20), so 1-3 trees realise all short even lengths 0..18 but miss 20 -- the kind of sparse-spectrum behaviour the near-cubic spine must contend with.
anchor: research/sources/narins-szabo-degree3-critical-short-cycles.full.md
```

```claim
id: nps-noninduced-degree3critical-pancyclic
statement: If G is n-vertex with 2n-2 edges and NO proper subgraph (not necessarily induced) of minimum degree 3, then G is pancyclic (cycles of every length 3,...,n); only two families exist (wheels, and wheels with one edge replaced).
hypotheses: G has 2n-2 edges, no proper subgraph of min degree 3 (non-induced sense)
holds-here: no single general subgraph of a minimal counterexample is guaranteed to satisfy this, so it is a weaker adjacent result; does not directly constrain a minimal E-G counterexample (which is 3-critical in the induced sense, not the non-induced sense)
status: asserted (full text held)
bearing: boundary marker -- the induced/non-induced distinction is decisive; Conjecture 1.1 is only false in the induced sense, and the characterisation (wheels etc.) shows how rigid the non-induced class is.
anchor: research/sources/narins-szabo-degree3-critical-short-cycles.full.md
```

