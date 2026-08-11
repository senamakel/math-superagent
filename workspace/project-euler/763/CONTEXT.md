# Shared context

What the run's reference library establishes, in the run's words. The
research team writes this; everyone reads it.

## Established

- **3D D(N) is not in OEIS.** Direct queries of the full 15-term and offset-1
  11-term sequence both return "No results" ([[L1.0/oeis_direct]], [[L1.0/oeis_partial]]). No catalogued closed form to look up.
- **No tree/fibonacci/Motzkin family fits 3D D(N).** Motzkin (A001006), Motzkin
  variants (A086246, A168049), and Fibonacci family (A005207) all diverge from
  D(N)=1,1,3,9,30,99,336,... at n=2. D(N)'s ~x3.4/division growth is unlike any
  of these. (Claims dN-not-motzkin, dN-not-a086246, dN-not-a168049,
  dN-not-fibonacci-f2n1.)
- **The 2D analogue of the amoeba is OEIS A007902 (pebbling configurations).**
  D_2D(N)=A007902(N+1) on every published term: 1,1,2,4,9,20,46,...,5895408
  (run BFS-verified N=0..20; claim d2d-equals-a007902). A007902 is NOT the 3D
  D(N). It has only an asymptotic (~0.1227*2.32^n, Knessl) and a memoized
  recurrence, **no closed form** — so even the 2D genus is not reducible to an
  evaluation, and it hands over no closed form for 3D D(10000).
- **The 3D D(N) is a folded-polyominoid reachable-position count.** Sourced
  from Eriksson, "Pebblings", EJC 2 (1995) #R7, and verified here against the
  full text ([[L2.0/pebbling_ejc_survey]]): the PE763 amoeba is exactly
  Eriksson/Vaderlind's n=3 pebbling game, so **no cell is ever played twice**
  (Prop 24), and reachable positions, voidance sets and folded polyominoids
  coincide bijectively (Theorem 9; claims n3-folded-polyominoid-voidance,
  d2-positions-are-polyominoid-voidance, both holds-here=yes). This is the
  correct counting object for D(N) and the ladder to lift the 2D G(k,m)
  machinery to 3D — but Eriksson himself has no closed form for the folded-
  polyominoid numbers, so the numeric D(10000) still needs the run's own
  DP/BFS.

## Contradictions

- None between sources. (The a005207 note was briefly mislabelled as
  contradicting a nonexistent claim; fixed — no real conflict.)

## Gaps

- A structural/combinatorial formula or recurrence for the **3D** D(N) at
  N=10000 remains unknown. Literature lookup is exhausted: not in OEIS, and
  the only identified relative (pebbling, 2D) itself lacks a closed form.
  Eriksson names the counting object (folded polyominoids, n=3) but offers no
  closed form for those either (Fig. 3 is a raw small-N table only). The next
  direction must lift the 2D G(k,m)-style recurrence / voidance-set structure
  to 3D, using the level-histogram / bounding-box data already dumped for
  N=2..12.
