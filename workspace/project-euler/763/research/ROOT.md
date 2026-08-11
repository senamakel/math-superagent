# research — what this now establishes

Top of the tree. Batches of originals in `L0.<n>/`; seals a level up. What
the whole library lets this run treat as known, under 1000 tokens, each claim
wikilinked to its note.

## The OEIS hunt for a closed form for the 3D D(N)

Closed: **D(N) is not any catalogued closed-form sequence; OEIS has no entry
for it and no formula.**

- [[oeis_direct]] and [[oeis_partial]]: direct OEIS queries of the full
  15-term and offset-1 11-term D(N) both return "No results". D(N) is not
  catalogued (status: asserted — machine-query outcome).
- [[oeis_a001006]] Motzkin: diverges from D(N) at n=2 (2 vs 3).
- [[oeis_a005207]] Fibonacci family: diverges at n=2.
- [[oeis_a086246]], [[oeis_a168049]] Motzkin variants: not D(N).
- [[oeis_a007902]] pebbling configurations: **not the 3D D(N)** (differs at
  n=2); IS the 2D amoeba sequence (below).

Net: the 3D D(10000) cannot be looked up. Its growth (~x3.4/division) is not
reproduced by any tree-family with a closed form; the structure must come from
the problem itself (the run's own BFS/DP route).

## A genuine identification: the 2D analogue is A007902

The run's 2D amoeba sequence D_2D(N) (BFS-verified N=0..20,
`code/out/d2_values.txt`) equals **OEIS A007902(N+1)** — "number of pebbling
configurations with n pebbles" — on every published term:
1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,87426,202961,471150,
1093819,2539348,5895408. This is the run's strongest structural handle: the
2D amoeba is a named pebbling object. But A007902 itself has no closed form
(asymptotic ~0.1227*2.3216^n, memoized recurrence only), so even the 2D genus
is not reducible to an evaluation, and it gives no closed form for 3D D(N).

## Bottom line

No catalogued closed form exists for 3D D(N). The 2D analogue is identified
(pebbling/A007902) but itself unresolved in closed form. The run must keep
deriving D(10000) from the problem's own structure; literature lookup is
exhausted as a route.
