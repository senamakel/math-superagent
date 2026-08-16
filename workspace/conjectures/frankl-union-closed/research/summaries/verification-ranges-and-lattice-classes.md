# Verification ranges and settled classes — structured claims

Captures the phase-1 deliverables from ROOT.md as claim blocks so the claims
ledger can cite them precisely.

```claim
id: verified-n11
statement: Frankl's union-closed sets conjecture holds for every union-closed
  family F whose ground set (union of members) has size ≤ 11.
hypotheses: F union-closed, finite, F ≠ {∅}, |∪F| ≤ 11.
holds-here: true
status: sourced
bearing: any minimal counterexample must have |∪F| ≥ 12 (ground set ≥ 12).
anchor: Bošnjak & Marković, Electron. J. Combin. 15(1):R88 (2008), arXiv:0711.3298
```

```claim
id: verified-n12-comp
statement: Frankl's union-closed sets conjecture holds for every union-closed
  family on a ground set of size ≤ 12, by computer-assisted proof
  (Vučković–Živković).
hypotheses: F union-closed, finite, F ≠ {∅}, |∪F| ≤ 12.
holds-here: true
status: sourced (computer-assisted; announced/unpublished per Bruhn–Schaudt survey)
bearing: lower bound on the ground-set size of a minimal counterexample.
anchor: Bruhn & Schaudt survey arXiv:1309.3297; Das–Wu arXiv:2412.03862 restate it
```

```claim
id: verified-m-small
statement: Frankl's conjecture holds for union-closed families with |F| ≤ 50,
  and (Roberts–Simpson / Hu) any counterexample with minimal ground-set size q
  has |F| ≥ 4q−1, hence any counterexample has
  |F| ≥ 4·13−1 = 51 (using Živković–Vučković's improved m ≥ 13, per Hu's
  Theorem 1 and its final paragraph). NOTE: earlier records said ≥ 47 from
  m ≥ 12; the sourced value is 51. |F| ≤ 50 verified follows from 4·13−1 = 51
  strictly exceeding 50.
hypotheses: F union-closed, finite, F ≠ {∅}.
holds-here: true
status: sourced (Hu arXiv:1706.06167 Theorem 1 + final para; Živković–Vučković
  for m ≥ 13; Roberts–Simpson AJC 2010)
bearing: lower bound on |F| of a minimal counterexample: |F| ≥ 51.
anchor: Lo Faro; Roberts & Simpson (AJC 2010); Hu (arXiv:1706.06167);
  Živković–Vučković (2017); restated in Colbert 2025 and Das–Wu
```

```claim
id: lattice-poonen
statement: Frankl's conjecture is equivalent to: every finite lattice L with
  |L| ≥ 2 has a join-irreducible j with at most |L|/2 elements above it
  (Poonen lattice form, JCTA 1992).
hypotheses: finite lattice L, |L| ≥ 2.
holds-here: true (it is the standard equivalent form, restated in Bouchard 2025,
  Bruhn–Charbit–Schaudt–Telle 2015, Joshi–Waphare 2019)
status: sourced (via citing papers; the Poonen paper itself is paywalled,
  ScienceDirect returns 403)
bearing: lets lattice-class results transfer to UC.
anchor: Poonen JCTA 59(2):253-268 1992; Bouchard 2025 lattice formulation
```

```claim
id: lattice-settled-classes
statement: UC holds for distributive, complemented and geometric lattices
  (Poonen), modular lattices (Abe–Nakano 1998), lower semimodular lattices
  (Reinhold), planar and large semimodular lattices (Czédli–Schmidt 2008),
  breadth ≤ 2 and upper-semimodular with few join-irreducibles
  (Joshi–Waphare 2019), and (added this cycle) subgroup lattices of finite
  groups and all comodernistic lattices (Abdollahi–Woodroofe–Zaimi 2017).
  Upper semimodular in general: OPEN.
hypotheses: F = lattice of the stated class, |L| ≥ 2.
holds-here: true (these are the settled lattice classes)
status: sourced (Poonen 1992; Abe–Nakano; Reinhold; Czédli–Schmidt;
  Joshi–Waphare 2019 all held as full texts; AWZ 2017 subgroup lattices added)
bearing: the classes already settled, so a new class proof is a genuine result.
anchor: Poonen 1992; Abe–Nakano; Reinhold; Czédli–Schmidt; Joshi–Waphare 2019;
  Abdollahi–Woodroofe–Zaimi EJC 24(3):P3.25 (2017) — full text in source library
```

```claim
id: verified-n12-comp-primary
statement: The n ≤ 12 verification is now held as its PRIMARY source: Vučković
  & Živković, "The 12-Element Case of Frankl's Conjecture", IPSI BgD Trans.
  Internet Research 13(1):65–71 (2017), computer-assisted proof (Marković
  FC-families, weight criterion, 33 FC families, backtracking). Any
  counterexample has |∪F| ≥ 13.
hypotheses: F union-closed, finite, F ≠ {∅}, |∪F| ≤ 12.
holds-here: true
status: asserted-by-source (primary paper downloaded; not re-derived by the run's
  oracle, which checks n ≤ 4 only)
bearing: upgrades `verified-n12-comp` from survey-sourced to primary-sourced; the
  exact computational boundary (n=12) and its method.
anchor: research/sources/vuckovic-zivkovic-12-element-2017.full.md
```
