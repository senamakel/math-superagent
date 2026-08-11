# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bitcount.md` | OEIS A000788: summatory binary 1-bit count (popcount) with O(log n) divide-and-conquer recurrences; supplies A(n) for the (A,B) counting game at n=10^5. |
| `cgt.md` | CGT framework: partisan games and the recursive position form (set of Left moves, set of Right moves); numbers as games; disjunctive sums. Justifies the board decomposing into a sum of subgames. |
| `disjsum.md` | Core structural result: each number with a 1-bits and b 0-bits is the game G(a,b) that equals the integer a-b, so the whole board reduces to the two totals A,B. |
| `loopy.md` | Why the skip creates a self-loop in the DP, resolved as a fixpoint; the game is a stopper so a finite S(n) exists. |
| `normalplay.md` | Connects "unable to move loses" to the normal-play convention; why One (Left) wins without skips given A−B>0. |
| `partisan.md` | Why Sprague–Grundy does NOT apply (disjoint move sets: One deletes 1-bits, Zero deletes 0-bits), so the run uses minimax over (A,B) not nimbers. |
| `strategy.md` | Dead end: generic strategy article, nothing relevant. Marked as examined so nobody reads it again. |
| `surreal.md` | Why G(a,b)=a−b is EXACT (simplest number strictly between left/right options); skips fall outside short-game numbers, so value A−B alone does not give S(n). |
| `trollopedelange.full.md` | Complete text of Girgensohn (2011) INTEGERS paper, "Digital sums and functional equations" — full derivations of Trollope–Delange formulas, power sums, and zero-count analogues, with functional-equation proofs. |
| `trollopedelange.md` | A54 INTEGERS 11 (2011) — from https://emis.muni.cz/journals/INTEGERS/papers/l54/l54.pdf; not yet read, excerpt pending a scholar summary |
| `weightedmom.md` | Larcher & Pillichshammer (2005), "Moments of the weighted sum-of-digits function": the governing theory for the run's weighted board totals A(n)=Σk·popcount(k) and B(n)=Σk·zerocount(k). Establishes that first-moment digit sums admit Delange-type closed forms (main term + fluctuation), warranting O(poly log n) evaluation. Only abstract obtainable (PDF gated). |
| `weightedsearch.md` | OEIS search on the given S(n) sample 1,3,9,13,23,35,56,64; excerpt pulled, full results not yet summarised. |
| `zerocount.md` | OEIS A059015: summatory binary 0-bit count with O(log n) recurrences and identity A059015 = A083652 − A000788; supplies B(n) for the (A,B) counting game. |
| `zugzwang.md` | Mechanism the skip exploits: One is forced to consume 1-bits each turn (zugzwang); "passing, if allowed, would be best" is the classical description of the skip. |
