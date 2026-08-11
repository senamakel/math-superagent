# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L1/bitcount.md` | OEIS A000788: summatory binary 1-bit count (popcount) with O(log n) divide-and-conquer recurrences; supplies A(n) for the (A,B) counting game at n=10^5. Full source text in bitcount.full.md (fallback — read the summary first). |
| `L1/cgt.md` | CGT framework: partisan games and the recursive position form (set of Left moves, set of Right moves); numbers as games; disjunctive sums. Justifies the board decomposing into a sum of subgames. Full source text in cgt.full.md (fallback — read the summary first). |
| `L1/disjsum.md` | Core structural result: each number with a 1-bits and b 0-bits is the game G(a,b) that equals the integer a-b, so the whole board reduces to the two totals A,B. Full source text in disjsum.full.md (fallback — read the summary first). |
| `L1/loopy.md` | Why the skip creates a self-loop in the DP, resolved as a fixpoint; the game is a stopper so a finite S(n) exists. Full source text in loopy.full.md (fallback — read the summary first). |
| `L1/normalplay.md` | Connects "unable to move loses" to the normal-play convention; why One (Left) wins without skips given A−B>0. |
| `L1/partisan.md` | Why Sprague–Grundy does NOT apply (disjoint move sets: One deletes 1-bits, Zero deletes 0-bits), so the run uses minimax over (A,B) not nimbers. |
| `L1/pass_waiting.md` | Larsson–Nowakowski–Santos (2015) arXiv:1505.01907 on passes/waiting moves in combinatorial games: primary, math-rigorous treatment of the skip as a zugzwang/tempo tool (order-embedding into normal-play when passes do no harm). Structural analogue of the problem's Zero-skip; corroborates zugzwang.md/loopy.md. |
| `L1/strategy.md` | Dead end: generic strategy article, nothing relevant. Marked as examined so nobody reads it again. Full source text in strategy.full.md (fallback — read the summary first). |
| `L1/surreal.md` | Why G(a,b)=a−b is EXACT (simplest number strictly between left/right options); skips fall outside short-game numbers, so value A−B alone does not give S(n). Full source text in surreal.full.md (fallback — read the summary first). |
| `L1/trollopedelange.md` | Girgensohn (2011) INTEGERS #A54, "Digital sums and functional equations": primary proof of the explicit Trollope–Delange formulas (main term + continuous periodic fluctuation, O(log n) recurrences) for both summatory 1-bit and 0-bit counts; unweighted engine behind the k·-weighted A(n), B(n) that run the (A,B) minimax DP. Full text at trollopedelange.full.md. |
| `L1/verify_trollopedelange.md` | Hand-off checklist for tool_builder: concrete numeric checks (ones summatory recurrences, Trollope-Delange formula 35, zero-count analogue) that must be run before any Girgensohn result is quoted. Do not delete. |
| `L1/weightedmom.md` | Larcher & Pillichshammer (2005), "Moments of the weighted sum-of-digits function": the governing theory for the run's weighted board totals A(n)=Σk·popcount(k) and B(n)=Σk·zerocount(k). Establishes that first-moment digit sums admit Delange-type closed forms (main term + fluctuation), warranting O(poly log n) evaluation. Only the abstract is locally available (PDF gated); weightedmom.full.md holds the AJOL landing page with the same abstract (fallback — read the summary first). |
| `L1/weightedsearch.md` | Dead end: OEIS search on the sample 1,3,9,13,23,35,56,64 returned NO results — the sequence is not in OEIS, so no closed-form lead there. Marked examined. |
| `L1/zerocount.md` | OEIS A059015: summatory binary 0-bit count with O(log n) recurrences and identity A059015 = A083652 − A000788; supplies B(n) for the (A,B) counting game. Full source text in zerocount.full.md (fallback — read the summary first). |
| `L1/zugzwang.md` | Mechanism the skip exploits: One is forced to consume 1-bits each turn (zugzwang); "passing, if allowed, would be best" is the classical description of the skip. Full source text in zugzwang.full.md (fallback — read the summary first). |
