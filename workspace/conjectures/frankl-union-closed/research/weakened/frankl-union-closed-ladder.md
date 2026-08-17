# Ladder: Frankl's union-closed sets conjecture

Weakened targets for the run. The bottom rung is trivial; the top is the 3-set
fault line; the full conjecture is the implicit roof. Nothing here implies the
goal, by design. Every `off` entry is a difficulty declared below, and every
rung is stated with exactly the difficulties that were switched off when it was
settled or attacked — a weakened result reported without its weakening reads as
a proof of something it did not prove.

```ladder
goal: Frankl's union-closed sets conjecture — every finite union-closed family F ≠ {∅} has an element lying in at least |F|/2 of its members.
difficulties: unbounded-n, unbounded-F, no-class-restriction, tightness-at-half, entropy-coupling-cap, small-set-forcing, unbounded-chain-length, graph-bipartite-hard
status: open
```

## Lattice / family-restriction axis

```rung
id: R-uc-n1
statement: Every union-closed family F ≠ {∅} on a ground set with |∪F| ≤ 1 has an element in at least |F|/2 members.
off: unbounded-n, unbounded-F
stance: settled
merge: The only such families are {{x}} and {∅,{x}}, so x is in everything. To climb, lift the ground-set bound — the exact in-repo oracle code/lib/uc.py decides n ≤ 3 by exhaustion and is the seed for R-uc-small-n. The difficulty that comes back on is unbounded-n.
```

```rung
id: R-uc-small-n
statement: Every union-closed family F ≠ {∅} with |∪F| ≤ 12 has an element in at least |F|/2 members.
off: unbounded-n, unbounded-F
stance: settled
merge: The largest ground-set size machine-verified. n ≤ 11 proved by Bošnjak–Marković (EJC 15 #R88, 2008); n ≤ 12 by Vučković–Živković (IPSI BgD, 2017, computer-assisted via 33 Marković FC-families and the weight criterion) — claim `vuckovic-zivkovic-n12` in the library. So any counterexample has |∪F| ≥ 13. To climb past 12, brute force dies (2^{2^n} families), so the next move is the minimal-counterexample reduction (Bouchard's UC_{n−1} ⟹ UC_n shows the (n−1)-set complementary class is the hinge), not a bigger search. The difficulty that bites is unbounded-n.
```

```rung
id: R-uc-small-F
statement: Every union-closed family F ≠ {∅} with |F| ≤ 50 has an element in at least |F|/2 members.
off: unbounded-F
stance: settled
merge: Via the minimal-counterexample lower bound |F| ≥ 4n−1 (Roberts–Simpson / Lo Faro; Hu's full proof arXiv:1706.06167) combined with n ≥ 13: a counterexample would need |F| ≥ 4·13−1 = 51 (claim `hu-theorem1-4m-minus-1`); separately the |F| ≤ 40 route (claim `faro-roberts-simpson-40`). Note |F| ≤ 50 does not bound |∪F| — a member may carry a fresh element — so unbounded-n is already on here; this rung is a different axis from R-uc-small-n, and the two do not nest.
```

```rung
id: R-uc-lattice-classes
statement: Every finite lattice in a settled class — lower semimodular, modular, geometric, distributive, planar semimodular, breadth ≤ 2 — has a join-irreducible element below at most half its elements (equivalently: UC holds for the union-closed families arising from such lattices).
off: no-class-restriction
stance: settled
merge: Settled in the literature (Czédli–Schmidt, Abe–Nakano, Reinhold, Poonen, Joshi–Waphare; claim `lattice-settled-classes`). The exploited hypotheses are semimodularity for the lower/planar classes and the breadth bound for breadth ≤ 2, each disciplining the cover relations of join-irreducibles. Turning no-class-restriction back on means arbitrary lattices where that structure is absent — and the first class where it is genuinely unknown is upper semimodular (next rung).
```

```rung
id: R-uc-graph-classes
statement: UC (in the Bruhn–Charbit–Schaudt–Telle graph form) holds for every graph in a settled class: chordal bipartite, subcubic bipartite, bipartite series-parallel, and bipartitioned circular interval graphs — each has two adjacent vertices in at most half its maximal stable sets.
off: no-class-restriction
stance: settled
merge: This is the graph-formulation axis, distinct from the lattice axis: the objects are graphs, not lattices, and the equivalence (claim `graph-formulation`) makes general-bipartite the whole conjecture. Settled classes are `graph-settled-classes` (chordal bipartite, subcubic bipartite, bipartite series-parallel, bipartitioned circular interval). To climb, there is no intermediate rung — general bipartite IS the full conjecture (`graph-bipartite-equivalent`), so the only next class is a *new* graph class, and the run's one attackable candidate is Nived's 2-layered decomposition hypothesis (claim `nived-graph-decomposition-class`, Theorem 3.2–3.3: products of maximal-stable-set counts under a 2-layered/common-vertex condition). The difficulty that bites is graph-bipartite-hard: the bipartite heart has no reduction that loses anything.
```

```rung
id: R-uc-dimension-2
statement: Every nontrivial union-closed family of dimension at most two (every chain of sets has at most 3 members, i.e. length |C|−1 ≤ 2) has an abundant element; both finite and infinite families.
off: unbounded-chain-length
stance: settled
merge: Settled by Colbert (dimension ≤ 1 is a lemma; Prop 3.9 / Thm 3.17 of the Order 43 (2026) version of record — claims `colbert-dim-at-most-2`, `colbert-order-2026-version-of-record`). The proof is an injection F∖F_x → F_x that the dimension-2 chain discipline makes available. To climb, lift the dimension bound to ≤ 3 — the difficulty that bites is unbounded-chain-length coming back on, because the injection no longer exists at chain length 4 and no settled result for dimension ≤ 3 is in the library. Note this axis is independent of the n/|F| axes (dimension can be small even with unbounded n).
```

```rung
id: R-uc-upper-semimodular
statement: Every finite upper semimodular lattice L with |L| ≥ 2 has a join-irreducible element below at most half its elements (equivalently: UC holds for the union-closed families arising from upper semimodular lattices).
off: no-class-restriction
stance: open
merge: The genuine fault line of the lattice line. Lower semimodular, modular, geometric, planar semimodular are settled, but whether UC holds for *upper* semimodular lattices in general is OPEN (claim `upper-semimodular-open`; confirmed still open as of Joshi–Waphare 2019). A subclass is settled: upper semimodular with |J(L)\A(L)| ≤ 3 (claim `joshiwaphare-upper-semimodular-3`), and breadth ≤ 2 (claim `joshiwaphare-breadth2`) — so the run's first move is to push the |J(L)\A(L)| ≤ 3 line up or find a violation structure. The difficulty that bites is the absent semimodular-cover discipline on the join-irreducible side: the injection proof that works for lower semimodular / breadth ≤ 2 (constructing the majority set for one join-irreducible) has no upper-semimodular analogue. To climb to the settled lattice rungs' ceiling is exactly to turn no-class-restriction back on.
```

## Constant / entropy axis

```rung
id: R-constant-gilmer
statement: There is an absolute constant c > 0 such that every union-closed family F ≠ {∅} has an element in at least c·|F| members.
off: tightness-at-half, entropy-coupling-cap
stance: settled
merge: Settled (Gilmer 2022, arXiv:2211.09055; the argument yields c ≈ 0.01, re-derived in the library). Both named difficulties are off: no sharpness is demanded and the constant is far below the coupling's saturation. To climb, push c up to (3−√5)/2 — entropy-coupling-cap comes back on as the one-variable entropy inequality is driven to its tight point.
```

```rung
id: R-constant-silver
statement: Every union-closed family F ≠ {∅} has an element in at least ((3−√5)/2)·|F| ≈ 0.38197·|F| members.
off: tightness-at-half
stance: settled
merge: Settled independently (Alweiss–Huang–Sellke, Chase–Lovett, Pebody, late 2022; all in the library). This is exactly where Gilmer's iid two-copy entropy inequality saturates (the one-variable inequality h(x²) ≥ φ·x·h(x), φ the golden ratio, Boppana), so the rung sits on the cap. The difficulty that comes back on is entropy-coupling-cap: passing this value needs a new coupling (dependent samples), not better estimates of the same inequality.
```

```rung
id: R-constant-beyond-silver
statement: Every union-closed family F ≠ {∅} has an element in at least c·|F| members for some c > (3−√5)/2 — the current record being c ≈ 0.38234.
off: tightness-at-half
stance: settled
merge: Settled (Sawin 2022; Cambie 2022; Yu 2023; Liu 2023 conditionally — all in the library; the ≈ 0.38234 value is credited to Yu/Cambie). The cap was beaten only by changing the coupling (dependent / conditionally-iid samples), and only to ~0.38234, leaving a gap of ~0.118 to 1/2. The remaining difficulty is not a better coupling alone: closing the whole gap turns tightness-at-half back on and would be the conjecture. The first move is to formalise "entropy argument of Gilmer shape" precisely enough to ask whether any coupling can reach 1/2 — the live frontier, and the run's own coupling work shows the two-atom class caps below it (Ruled out in CONTEXT.md).
```

## Small-set-forcing axis

```rung
id: R-uc-with-singleton
statement: Every union-closed family F ≠ {∅} that contains a singleton {x} has an element in at least |F|/2 members.
off: no-class-restriction, small-set-forcing
stance: settled
merge: Trivial and folklore: union-closure forces every other member to contain x, so x is in |F| members. The local argument is automatic here. To climb, move the forced member up to size 2 — the difficulty that partially re-engages is small-set-forcing.
```

```rung
id: R-uc-with-two-set
statement: Every union-closed family F ≠ {∅} that contains a 2-element set {x,y} has an element in at least |F|/2 members.
off: no-class-restriction, small-set-forcing
stance: settled
merge: Folklore / Sarvate–Renaud / Hu–Shi–Zhou (Prop 3.3: any |A| ≥ 2 member has an element of density ≥ |F|/(2^{|A|−2}+1), tight for 2-sets): one of x, y is abundant. Still below the forcing boundary. To climb, go to a 3-element member — small-set-forcing fully re-engages, because the size-2 argument gives density ≥ 1/2 but the size-3 argument only gives ≥ 1/3, which is below the abundant threshold.
```

```rung
id: R-uc-with-three-set
statement: Every union-closed family F ≠ {∅} that contains a 3-element set {x,y,z} has an element (not necessarily in {x,y,z}) in at least |F|/2 members.
off: no-class-restriction
stance: open
merge: This is the first hard rung and the fault line of the small-set-forcing axis. The forcing argument dies here: the size-2 density transfer gives only ≥ 1/3 for 3-sets (claim `hsz-one-element-of-any-2set-dense`). The claim `ellis-ivan-leader-small-set-3-fails` refutes only the *stronger* conjecture that one of x,y,z is abundant (for any ε>0 a UC family with smallest 3-set whose elements all appear in fraction (1+o(1))(log₂3)/6 < 1/2) — so the rung as stated (some element, possibly outside {x,y,z}) survives and stays open. Its bite is the missing guarantee that the abundant element lies in the forcing set: the local union trick gives nothing. Attack it with the FC-family machinery (Poonen weight criterion, claim `vuckovic-zivkovic-fc-lemma`): decide whether a 3-set is an FC-family, and if not locate the boundary. Data points on how much forcing a 3-set needs: `maric-4-3subsets-7set-fc` (four 3-subsets of [7] ARE FC) and `no-two-abundant-k3-n7-found` (no (2,3,7)-construction in 190k families; the k=3 abundance floor is 3, and whether any family has exactly 2 abundant elements at n=7 stays open). The difficulty that bites is small-set-forcing.
```
