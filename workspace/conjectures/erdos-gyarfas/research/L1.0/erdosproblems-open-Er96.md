<!-- source: https://www.erdosproblems.com/search_bib/Er96/open | converted from HTML -->

# Erdős problem #64 — primary statement, status, and the Liu–Montgomery resolution

This is the **primary source** (via erdosproblems.com, curated by T. F. Bloom; the page itself cites Erdős's own papers Er93 p.343, Er94b, Er95 p.174, Er96, Er97b, Er97c).

## The conjecture (stated as Erdős problem #64)

> Does every finite graph with minimum degree at least 3 contain a cycle of length $2^k$ for some $k \geq 2$?

Marked **FALSIFIABLE, open** — could be disproved with a finite counterexample; prize $1000. Status reflects current belief of the site owner, not proof of openness.

## What the page establishes beyond the statement

- Erdős and Gyárfás **believed the answer is negative**, and in fact believed that for every $r$ there is a graph of minimum degree at least $r$ with no cycle of length $2^k$ for any $k \geq 2$ (a strictly stronger conjecture).
- That stronger conjecture was **disproved by Liu and Montgomery [LiMo20]**: if the average degree of $G$ is sufficiently large then there is some large $\ell$ such that for every even integer $m \in [(\log \ell)^8, \ell]$, $G$ contains a cycle of length $m$. Since powers of 2 lie in that interval once $\ell$ is large, large average degree forces a 2-power cycle.
- An infinite tree of minimum degree 3 shows the answer is **trivially false for infinite graphs** (so finiteness is essential).
- The conjecture has been confirmed for various families (list in the comments; cf. the restricted-class notes in this batch).
- Note the site states the target as $2^k$ with $k \geq 2$, i.e. lengths $4, 8, 16, \ldots$; a length-2 cycle cannot exist in a simple graph, so this is not a substantive difference from "power of two".

```claim
id: eg-primary-statement
statement: Every finite simple graph with minimum degree at least 3 contains a simple cycle whose length is a power of 2 (equivalently 2^k for some k >= 2, i.e. length in {4,8,16,...}).
hypotheses: finite simple graph, min degree >= 3
holds-here: yes (this is the target statement the run must prove)
status: open — asserted as a conjecture, not proved; a finite counterexample would refute it
bearing: the exact statement to attack, with the length set pinned to {4,8,16,...} and finiteness shown essential (infinite min-degree-3 tree is a trivial counterexample)
anchor: research/L0.0/erdosproblems-open-Er96.full.md
```

```claim
id: eg-stronger-disproved
statement: The stronger conjecture (for every r a min-degree-r graph with no 2-power cycle) is false: every graph of sufficiently large average degree contains 2-power cycles, by Liu and Montgomery.
hypotheses: average degree >= d0 for a large absolute constant d0
holds-here: no — a general min-degree-3 graph need not have large average degree, so this does not resolve the conjecture; it only disproves the stronger belief
status: proved (Liu & Montgomery, cited)
bearing: the hard case is bounded average degree near 3; large-average-degree graphs are settled
anchor: research/L0.0/erdosproblems-open-Er96.full.md
```
