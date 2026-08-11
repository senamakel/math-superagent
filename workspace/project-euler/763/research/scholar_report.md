I read the batch in `research/L1.0/` and the surrounding run-level notes. The material is entirely OEIS lookups filed while hunting a closed form for the **3D** amoeba D(N). Here is what each establishes, and the one correction-worthy thing I found.

## Sources that do not help (ruled-out closed forms for 3D D(N))

All four tree-family/Fibonacci candidates are **dead ends** — none matches D(N)=1,1,3,9,30,99,336,.... They proved a single negative: D(N) is not any catalogued Motzkin/Fibonacci-family sequence, diverging at n=2.

- **A001006 (Motzkin)** 1,1,2,4,9,21,... — diverges at n=2 (2 vs 3). Has a clean D-finite recurrence and closed form, but it governs a different object.
- **A005207** (F(2n-1)+F(n+1))/2 = 1,1,2,4,9,21,... — diverges at n=2; linear-recurrence growth ~2.6 also unlike D(N)'s ~×3.4.
- **A086246, A168049** (Motzkin variants) — 0,1,1,1,2,4,9,... and 1,0,1,1,2,4,9,... respectively; neither matches.

Each is recorded as a claim (dN-not-motzkin, dN-not-fibonacci-f2n1, dN-not-a086246, dN-not-a168049) so nobody re-chases them.

## The two direct OEIS searches: authoritative negatives

- **oeis_direct** and **oeis_partial** — direct `fmt=text` queries of the full 15-term and offset-1 11-term D(N) both return **"No results."** This is a machine outcome (status: asserted), establishing D(N) is not catalogued, so there is **no closed form to look up**. This is the key structural conclusion: D(10000) cannot come from a lookup; it must come from the problem's own structure.

## The real finding I initially got wrong

- **A007902 (number of pebbling configurations)**: my first read dismissed it as "diverges from D(N) at n=2" — but that compared it to the **3D** sequence. The pre-existing index description flagged that its terms match the run's **2D amoeba** sequence, and it was right. **The 2D analogue of the PE763 amoeba IS OEIS A007902** (D_2D(N)=A007902(N+1)): the run's BFS-verified 2D values 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,87426,202961,471150,1093819,2539348,5895408 match all 21 published terms. Requirement 10 (independent verification): this is checked against the run's own double-BFS-verified d2_values.txt, itself produced by two independent implementations — so the match is real, though it remains an observational identification (no bijective proof in the source).

A companion run-level note **amoeba2d_pebbling_a007902.md** (which I found in the index) independently establishes the same thing and goes further: this is the **classical chessboard-pebbling problem** of Kontsevich/Khodulev, enumerated by Chung–Graham–Morrison–Odlyzko (Amer. Math. Monthly 102 (1995)), with an exact G(k,m) recurrence and a polyominoid/voidance-set bijective structure. It calls the 3D D(N) the higher-dimensional cousin.

## Bearing on the goal (3D D(10000))

- **No catalogued closed form exists for 3D D(N)** — this is now firmly established by the two "No results" queries plus the four excluded families. The lookup route is exhausted.
- The A007902 identification is the strongest structural handle the run has, but it does **not** hand over a closed form: even the 2D genus has only an asymptotic (~0.1227·2.32ⁿ, Knessl) and a memoized recurrence, and its ratio ~2.32 is far from 3D D(N)'s ~×3.4. So it points the direction (the 2D pebbling toolkit is the model to try lifting to 3D) but does not solve 3D.
- **Contradiction check:** none between sources. The one brief mismatch (a005207 claim was initially tagged as contradicting a nonexistent claim) was a typo I fixed — no real conflict. Nothing contradicts MEMORY.md's D(0..14) values; in fact the A007902 match confirms the run's 2D values are right.

## Records written

- Replaced all six placeholder notes in `L1.0/` with real summaries (each with a claim block, under 1000 tokens), and wrote the A007902 note twice-corrected (first read, then the corrected identification) — final version names the D_2D match.
- Updated `L1.0/INDEX.md`, `research/INDEX.md` (all 12 files described), `ROOT.md`, `CONTEXT.md`, and the CLAMS ledger.
- remembered_research the A007902 = 2D-amoeba identification.
- Cleaned two stale index rows (oeis_direct labeled "not yet read").
- Dropped my scratch `code/amoeba_2d.py` intent (it duplicated existing run code in `amoeba2d/d2d.py` and `lib/amoeba2d.py` — I used the run's verified data instead of re-running).

## What the run still lacks

A structural formula/recurrence for the **3D** D(N) at N=10000. Literature lookup is closed; the next step is to try to lift the 2D pebbling structure (G(k,m)-style recurrence, polyominoid/voidance bijection) to 3D — the direction both the A007902 identification and the existing level-histogram/bbox data (`data/level_N.txt`) point to.
