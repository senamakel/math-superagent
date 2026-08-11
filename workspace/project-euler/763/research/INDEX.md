# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `CLAIMS.md` | Derived: every claim block in the notes, one row each, with whether its hypotheses hold here and what evidence stands behind it. Rewritten on every research write; do not edit. |
| `FRONTIER.md` | Derived: sources this library's own documents cite but the run has not read, ranked by how many of them cite each. Rewritten on every download; do not edit. |
| `L1.0/oeis_a001006.md` | OEIS A001006 (Motzkin numbers) lookup note: closed forms, recurrence, g.f., source https://oeis.org/A001006. Filed hunting a closed form for D(N); low terms 1,1,2,4,9,21,... diverge from D(N)=1,1,3,9,30,... at n=2 — dead end, not a candidate fit. |
| `L1.0/oeis_a005207.md` | OEIS lookup note for A005207 (a(n)=(F(2n-1)+F(n+1))/2, Fibonaccis; g.f. 1-x(1-2x-x^2+x^3)/((x^2+x-1)(x^2-3x+1)), source https://oeis.org/A005207): terms 1,1,2,4,9,21,51,127,322,826,.... Filed hunting a closed form for D(N); diverges from D(N) by term 3 (2 vs 3), so not a candidate fit. |
| `L1.0/oeis_a007902.md` | OEIS A007902 (number of pebbling configurations with n pebbles) lookup note, source https://oeis.org/A007902. Terms 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,... are identical to the run's computed 2D amoeba sequence D_2D(N) — an observable match worth pursuing, not yet read for its formula. |
| `L1.0/oeis_a086246.md` | OEIS lookup note for A086246 (Motzkin variant, g.f. (1+x-sqrt(1-2x-3x^2))/2, source https://oeis.org/A086246): terms 0,1,1,1,2,4,9,21,51,127,.... Filed while hunting a closed form for D(N); its low terms do not match D(N)=1,1,3,9,30,..., so not a candidate fit. |
| `L1.0/oeis_a168049.md` | OEIS A168049 (Motzkin variant, g.f. (3-x-sqrt(1-2x-3x^2))/2, source https://oeis.org/A168049): terms 1,0,1,1,2,4,9,21,51,127,... Filed while hunting a closed form for D(N); its low terms do not match D(N)=1,1,3,9,30,..., so not a candidate fit. |
| `L1.0/oeis_direct.md` | Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/ — from https://oeis.org/search?q=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063&fmt=text; not yet read, excerpt pending a scholar summary |
| `L1.0/oeis_partial.md` | Direct OEIS search of offset-1 11 terms: "No results". Confirms the absence of D(N) in OEIS regardless of offset. |
| `THREADS.md` | Derived: every direction of attack under research/threads/, what each rests on, and why the dead ones died. Rewritten on every research write; do not edit. |
| `amoeba_seq_oeis.md` | OEIS/literature status of the 3D-amoeba sequence D(N): confirmed not in OEIS (both direct queries return No results), closest structural relatives (directed lattice animals), and saved source URLs. The run-level note that no catalogued closed form exists. |
