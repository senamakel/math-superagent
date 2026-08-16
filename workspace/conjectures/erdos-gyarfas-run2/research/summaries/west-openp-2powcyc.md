# West — Open Problems page (2powcyc)

Source: https://dwest.web.illinois.edu/openp/2powcyc.html (D. West,
"Erdős-Gyárfás Conjecture on 2-power Cycle Lengths"). Full text held in this
summary; [[west-openp-2powcyc]].

## Statement

**Conjecture:** every graph with minimum degree 3 has a cycle whose length is
a power of 2.

**Caro's weaker variant (suggested):** whether every such graph has a cycle
whose length is a **non-trivial power of some natural number** (not
necessarily 2). This is a strictly easier question and is the natural
stepping-stone the run could weaken to.

## Partial results (exact hypotheses, authoritative from West)

- **Daniel & Shauger [DS]** proved the conjecture for **planar claw-free**
  graphs. (Congr. Numer. 153 (2001) 129–139.)
- **Shauger [S]** proved it for **K_{1,m}-free graphs having minimum degree
  at least m+1 OR maximum degree at least 2m−1**. (Congr. Numer. 134 (1998)
  61–65.)

## For this problem

West is the authority for the exact hypotheses of the two conference-paper
results (Daniel–Shauger; Shauger) whose full texts were not obtainable. It is
also the origin of Caro's weakening. Both settle classes: planar-claw-free,
and K_{1,m}-free under the stated degree conditions.

```claim
id: west-settled-classes
statement: E-G holds for (a) planar claw-free graphs and (b) K_{1,m}-free graphs with minimum degree ≥ m+1 or maximum degree ≥ 2m-1.
hypotheses: (a) planar + claw-free, δ≥3; (b) K_{1,m}-free with the stated degree condition
holds-here: yes (settled restricted classes; primary proofs are conference papers not held)
status: asserted (West's authoritative summary)
bearing: two of the settled classes ROOT.md must state exactly
anchor: research/notes/library-holdings.md
```

```claim
id: caro-weakening
statement: Caro asks whether every δ ≥ 3 graph has a cycle whose length is a nontrivial power of some natural number (weaker than power-of-2).
hypotheses: δ ≥ 3
holds-here: yes — a strictly easier target usable as a rung on the weakened ladder
status: sourced (West)
bearing: a rigorous weaken-the-goal rung; proving it would be a genuine partial result even though it does not settle E-G
anchor: research/notes/library-holdings.md
```
