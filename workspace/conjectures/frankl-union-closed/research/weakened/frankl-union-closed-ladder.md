# Ladder: Frankl's union-closed sets conjecture

Weakened targets for the run. The bottom rung is trivial; the top open rung is
the 3-set fault line; the full conjecture is the implicit roof. Nothing here
implies the goal, by design.

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
merge: The only such families are {{x}} and {∅,{x}}, so x is in everything. To climb, lift the ground-set bound — the first move is the exact in-repo oracle deciding n ≤ 3 by exhaustion, which is the seed for R-uc-small-n. The difficulty that comes back on is unbounded-n.
```

```rung
id: R-uc-small-n
statement: Every union-closed family F ≠ {∅} with |∪F| ≤ 11 has an element in at least |F|/2 members.
off: unbounded-n, unbounded-F
stance: settled
merge: Settled in the literature (Bošnjak–Marković 2008, EJC 15 #R88: UC holds when |∪F| ≤ 11). Source is in the library; not yet re-derived by this run — the oracle phase should re-verify n ≤ 4 or 5 cheaply before trusting the citation. To climb past n = 11, brute force dies (2^{2^n} families), so the next move is a minimal-counterexample reduction, not a bigger search. The difficulty that bites is unbounded-n.
```

```rung
id: R-uc-small-F
statement: Every union-closed family F ≠ {∅} with |F| ≤ 50 has an element in at least |F|/2 members.
off: unbounded-F
stance: settled
merge: Recalled in problem.md (Roberts–Simpson / Faro et al.); primary source not yet in the library, so this row is `settled` on the field's word and must be confirmed before it is banked as a claim. Note |F| ≤ 50 does not bound |∪F| — a member may carry a fresh element — so unbounded-n is already on here; this rung is a different axis from R-uc-small-n, and the two do not nest.
```

```rung
id: R-uc-lattice-classes
statement: Every finite lattice in a settled class — lower semimodular, modular, geometric, distributive — has a join-irreducible element below at most half its elements (equivalently: UC holds for the union-closed families arising from such lattices).
off: no-class-restriction
stance: settled
merge: Settled in the literature (Czédli–Schmidt, Abe–Nakano, Reinhold, and others; surveyed in Bruhn–Schaudt 2013). Confirm per-class attribution from the survey before relying. The exploited hypothesis is semimodularity, which disciplines the cover relations of join-irreducibles; turning no-class-restriction back on means arbitrary lattices where that structure is absent.
```

```rung
id: R-constant-gilmer
statement: There is an absolute constant c > 0 such that every union-closed family F ≠ {∅} has an element in at least c·|F| members.
off: tightness-at-half, entropy-coupling-cap
stance: settled
merge: Settled (Gilmer 2022, arXiv:2211.09055; the argument yields c ≈ 0.01). Both named difficulties are off: no sharpness is demanded and the constant is far below the coupling's saturation. To climb, push c up to (3−√5)/2 — entropy-coupling-cap comes back on as the underlying one-variable entropy inequality is driven to its tight point.
```

```rung
id: R-constant-silver
statement: Every union-closed family F ≠ {∅} has an element in at least ((3−√5)/2)·|F| ≈ 0.38197·|F| members.
off: tightness-at-half
stance: settled
merge: Settled independently (Alweiss–Huang–Sellke, Chase–Lovett, Pebody, late 2022; all in the library). This is exactly where Gilmer's i.i.d. two-copy entropy inequality saturates, so the rung sits on the cap. The difficulty that comes back on is entropy-coupling-cap: passing this value needs a new coupling (dependent samples, max-entropy), not better estimates of the same inequality.
```

```rung
id: R-constant-beyond-silver
statement: Every union-closed family F ≠ {∅} has an element in at least c·|F| members for some c > (3−√5)/2 — the current record being c ≈ 0.38234.
off: tightness-at-half
stance: settled
merge: Settled (Sawin 2022; Cambie 2022; Yu 2023; Liu 2023 — all in the library; the ≈ 0.38234 value is credited to Yu/Cambie). The cap was beaten only by changing the coupling, and only to ~0.38234, leaving a gap of ~0.118 to 1/2. The remaining difficulty is not a better coupling alone: closing the whole gap turns tightness-at-half back on and would be the conjecture. The first move is to formalise "entropy argument of Gilmer shape" precisely enough to ask whether any coupling can reach 1/2 — that question is the live frontier.
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
merge: Folklore / Sarvate–Renaud: one of x, y is abundant, by a local union argument (if not all members contain x, then unioning with {x,y} drives up y's count). Still below the forcing boundary. To climb, go to a 3-element member — small-set-forcing fully re-engages, because the size-2 argument has no size-3 analogue.
```

```rung
id: R-uc-with-three-set
statement: Every union-closed family F ≠ {∅} that contains a 3-element set {x,y,z} has an element (not necessarily in {x,y,z}) in at least |F|/2 members.
off: no-class-restriction
stance: open
merge: This is the first hard rung and the fault line. The forcing argument dies here: it is not generally true that one of x,y,z is abundant, so the abundant element may lie outside the 3-set and the local union trick gives nothing. Attack it with the FC-family machinery — decide whether {x,y,z} is an FC-family via the finite weight/LP computation, and if not, locate the boundary cases. The difficulty that bites is small-set-forcing: every union-closed family containing a 3-set is still conjectured to satisfy UC, but no local argument certifies it, which is exactly where the real obstruction sits.
```
