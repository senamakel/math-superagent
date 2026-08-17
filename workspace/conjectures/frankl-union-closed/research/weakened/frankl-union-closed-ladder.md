# Ladder: Frankl's union-closed sets conjecture

Weakened targets for the run. The bottom rung is trivial; the top is the 3-set
fault line; the full conjecture is the implicit roof. Nothing here implies the
goal, by design. Every `off` entry is a difficulty declared below, and every
rung is stated with exactly the difficulties that were switched off when it was
settled or attacked — a weakened result reported without its weakening reads as
a proof of something it did not prove.

```ladder
goal: Frankl's union-closed sets conjecture — every finite union-closed family F ≠ {∅} has an element lying in at least |F|/2 of its members.
difficulties: unbounded-n, unbounded-F, no-class-restriction, tightness-at-half, entropy-coupling-cap, small-set-forcing
status: open
```

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
id: R-uc-upper-semimodular
statement: Every finite upper semimodular lattice L with |L| ≥ 2 has a join-irreducible element below at most half its elements (equivalently: UC holds for the union-closed families arising from upper semimodular lattices).
off: no-class-restriction
stance: open
merge: The genuine fault line of the lattice line. Lower semimodular, modular, geometric, planar semimodular are settled, but whether UC holds for *upper* semimodular lattices in general is OPEN (claim `upper-semimodular-open`; confirmed still open as of Joshi–Waphare 2019). A subclass is settled: upper semimodular with |J(L)\A(L)| ≤ 3 (claim `joshiwaphare-upper-semimodular-3`), and breadth ≤ 2 (claim `joshiwaphare-breadth2`) — so the run's first move is to push the |J(L)\A(L)| ≤ 3 line up or find a violation structure. The difficulty that bites is the absent semimodular-cover discipline on the join-irreducible side: the injection proof that works for lower semimodular / breadth ≤ 2 (constructing the majority set for one join-irreducible) has no upper-semimodular analogue. To climb to the settled lattice rungs' ceiling is exactly to turn no-class-restriction back on.
```

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
merge: Folklore / Sarvate–Renaud: one of x, y is abundant, by a local union argument (if not all members contain x, unioning with {x,y} drives up y's count). Still below the forcing boundary. To climb, go to a 3-element member — small-set-forcing fully re-engages, because the size-2 argument has no size-3 analogue.
```

```rung
id: R-uc-with-three-set
statement: Every union-closed family F ≠ {∅} that contains a 3-element set {x,y,z} has an element (not necessarily in {x,y,z}) in at least |F|/2 members.
off: no-class-restriction
stance: open
merge: This is the first hard rung and the fault line of the small-set-forcing axis. The forcing argument dies here. The claim `ellis-ivan-leader-small-set-3-fails` refutes only the *stronger* conjecture that one of x,y,z is abundant (for any ε>0 a UC family with smallest 3-set whose elements all appear in fraction (1+o(1))(log₂3)/6 < 1/2) — so the rung as stated (some element, possibly outside {x,y,z}) survives and stays open. Its bite is the missing guarantee that the abundant element lies in the forcing set: the local union trick gives nothing. Attack it with the FC-family machinery (Poonen weight criterion, claim `vuckovic-zivkovic-fc-lemma`): decide whether a 3-set is an FC-family, and if not locate the boundary. Note `maric-4-3subsets-7set-fc` shows four 3-subsets of [7] ARE FC, a data point for how much forcing a 3-set needs. The difficulty that bites is small-set-forcing.
```
