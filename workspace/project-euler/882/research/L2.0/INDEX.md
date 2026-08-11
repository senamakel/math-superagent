# Index — research/L2.0

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L1.0.md` | Seal note for batch L1.0: the ten notes (a083652, bitcount, cgt, confusioninterval×3, disjsum, flajolet×2, li_zuchswang) establish the counting model of the bit game — board value A−B (structural fact), normal-play win condition, the skip as a loopy/stopper fixpoint — and the polylog arithmetic engine (A000788/A059015/A083652 recurrences, Trollope–Delange / weighted-moment closed forms) that lets the DP run at n=10^5. Sealed once, never revisited. |
| `counting-arithmetic.md` | L2 synthesis of the arithmetic engine: polylog evaluation of A(n)=sum k*popcount(k) and B(n)=sum k*zerocount(k) at the 10^5 scale via A000788/A059015/A083652 recurrences, Trollope-Delange fluctuation, and k-weighted moment closed forms; S(n) not in OEIS. |
| `game-reduction-and-pass.md` | L2 synthesis of the game: reduction to counters (A,B) with a budgeted skip, why the no-skip value is A-B yet S(n) differs (the (A,B) stopper/loopy minimax DP governs). Synthesizes the CGT/surreal/pass derived sources. |
