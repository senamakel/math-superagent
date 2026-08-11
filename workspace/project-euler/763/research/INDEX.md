# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `CLAIMS.md` | Derived: every claim block in the notes, one row each, with whether its hypotheses hold here and what evidence stands behind it. Rewritten on every research write; do not edit. |
| `FRONTIER.md` | Derived: sources this library's own documents cite but the run has not read, ranked by how many of them cite each. Rewritten on every download; do not edit. |
| `L1.0/oeis_a001006.md` | OEIS A001006 (Motzkin numbers) lookup note: closed forms, recurrence, g.f., source https://oeis.org/A001006. Filed hunting a closed form for D(N); low terms 1,1,2,4,9,21,... diverge from D(N)=1,1,3,9,30,... at n=2 — dead end, not a candidate fit. |
| `L1.0/oeis_a005207.md` | OEIS lookup note for A005207 (a(n)=(F(2n-1)+F(n+1))/2, Fibonaccis; g.f. 1-x(1-2x-x^2+x^3)/((x^2+x-1)(x^2-3x+1)), source https://oeis.org/A005207): terms 1,1,2,4,9,21,51,127,322,826,.... Filed hunting a closed form for D(N); diverges from D(N) by term 3 (2 vs 3), so not a candidate fit. |
| `L1.0/oeis_a007902.md` | A007902 (pebbling configurations) = the run's 2D amoeba sequence D_2D(N), matched on every published term (D_2D(N)=A007902(N+1)). Names the 2D analogue; has no closed form, only asymptotic (~2.32^n) and a memoized recurrence. Not the 3D D(N). |
| `L1.0/oeis_a086246.md` | OEIS lookup note for A086246 (Motzkin variant, g.f. (1+x-sqrt(1-2x-3x^2))/2, source https://oeis.org/A086246): terms 0,1,1,1,2,4,9,21,51,127,.... Filed while hunting a closed form for D(N); its low terms do not match D(N)=1,1,3,9,30,..., so not a candidate fit. |
| `L1.0/oeis_a168049.md` | OEIS A168049 (Motzkin variant, g.f. (3-x-sqrt(1-2x-3x^2))/2, source https://oeis.org/A168049): terms 1,0,1,1,2,4,9,21,51,127,... Filed while hunting a closed form for D(N); its low terms do not match D(N)=1,1,3,9,30,..., so not a candidate fit. |
| `L1.0/oeis_direct.md` | Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/ — from https://oeis.org/search?q=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063&fmt=text; not yet read, excerpt pending a scholar summary |
| `L1.0/oeis_partial.md` | Record of the direct OEIS search for the offset-1 11-term partial sequence 1,3,9,30,...,44499 (https://oeis.org/search?q=1,3,9,30,99,336,1134,3855,13086,44499&fmt=text): also 'No results', confirming D(N) is absent from OEIS regardless of offset. Claim dN-offset-also-not-in-oeis. |
| `THREADS.md` | Derived: every direction of attack under research/threads/, what each rests on, and why the dead ones died. Rewritten on every research write; do not edit. |
| `amoeba2d_pebbling_a007902.md` | Establishes that the 2D amoeba process is exactly the classical pebbling problem (A007902, Chung-Graham-Morrison-Odlyzko "Pebbling a chessboard"): offset mapping D(N)=a(N+1), the exact G(k,m) recurrence, the polyominoid/voidance-set bijective structure, and growth asymptotics. Positions it as the structural model to lift to 3D for PE763 D(N). |
| `amoeba_seq_oeis.md` | OEIS/literature status of the 3D-amoeba sequence D(N): confirmed not in OEIS (both direct queries return No results), closest structural relatives (directed lattice animals), and saved source URLs. The run-level note that no catalogued closed form exists. |
