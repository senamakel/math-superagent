# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

Summaries live in `L1/` and their full source texts in `L0/` (fallback — read the summary first). One source, one summary; the index describes the summary.

## Relevant — game theory / structure

| File | Purpose |
| --- | --- |
| `L1/cgt.md` / `L0/cgt.full.md` | CGT framework: partisan games and the recursive position form (set of Left moves, set of Right moves); numbers as games; disjunctive sums. Justifies the board decomposing into a sum of subgames. |
| `L1/disjsum.md` / `L0/disjsum.full.md` | Core structural result: each number with a 1-bits and b 0-bits is the game G(a,b) that equals the integer a-b, so the whole board reduces to the two totals A,B. |
| `L1/loopy.md` / `L0/loopy.full.md` | Why the skip creates a self-loop in the DP, resolved as a fixpoint; the game is a stopper so a finite S(n) exists. |
| `L1/normalplay.md` | Connects "unable to move loses" to the normal-play convention; why One (Left) wins without skips given A−B>0. |
| `L1/partisan.md` | Why Sprague–Grundy does NOT apply (disjoint move sets: One deletes 1-bits, Zero deletes 0-bits), so the run uses minimax over (A,B) not nimbers. |
| `L1/surreal.md` / `L0/surreal.full.md` | Why G(a,b)=a−b is EXACT (simplest number strictly between left/right options); skips fall outside short-game numbers, so value A−B alone does not give S(n). |
| `L1/zugzwang.md` / `L0/zugzwang.full.md` | Mechanism the skip exploits: One is forced to consume 1-bits each turn (zugzwang); "passing, if allowed, would be best" is the classical description of the skip. |

## Relevant — arithmetic engine (A(n), B(n))

| File | Purpose |
| --- | --- |
| `L1/bitcount.md` / `L0/bitcount.full.md` | OEIS A000788: summatory binary 1-bit count (popcount) with O(log n) divide-and-conquer recurrences; supplies A(n) for the (A,B) counting game at n=10^5. |
| `L1/zerocount.md` / `L0/zerocount.full.md` | OEIS A059015: summatory binary 0-bit count with O(log n) recurrences and identity A059015 = A083652 − A000788; supplies B(n) for the (A,B) counting game. |
| `L1/trollopedelange.md` / `L0/trollopedelange.full.md` | Girgensohn (2011) INTEGERS #A54, "Digital sums and functional equations": primary proof of the explicit Trollope–Delange formulas (main term + continuous periodic fluctuation, O(log n) recurrences) for both summatory 1-bit and 0-bit counts; unweighted engine behind the k·-weighted A(n), B(n) that run the (A,B) minimax DP. |
| `L1/verify_trollopedelange.md` | Hand-off checklist for tool_builder: concrete numeric checks (ones summatory recurrences, Trollope-Delange formula 35, zero-count analogue) that must be run before any Girgensohn result is quoted. Do not delete. |
| `L1/weightedmom.md` / `L0/weightedmom.full.md` | Larcher & Pillichshammer (2005), "Moments of the weighted sum-of-digits function": the governing theory for the run's weighted board totals A(n)=Σk·popcount(k) and B(n)=Σk·zerocount(k). Establishes that first-moment digit sums admit Delange-type closed forms (main term + fluctuation), warranting O(poly log n) evaluation. Only the abstract is locally available (PDF gated). |

## Dead ends / noise — examined, do not re-read

| File | Purpose |
| --- | --- |
| `L1/strategy.md` / `L0/strategy.full.md` | Dead end: generic strategy article, nothing relevant. Marked as examined so nobody reads it again. |
| `L1/weightedsearch.md` | Dead end: OEIS search on the sample 1,3,9,13,23,35,56,64 returned NO results — the sequence is not in OEIS, so no closed-form lead there. Marked examined. |
| `L0/confusioninterval.full.md` (+ `.full.full.md`) | OFF-TOPIC NOISE: lossless-compression / Slepian-Wolf coding theory (Bauwens & Zimand, arXiv:1911.04268). Nothing to do with the bit-deletion game. Downloads fired by a misfiring librarian; do not read again. |
| `L0/confusioninterval2.full.md` (+ `.full.full.md`) | OFF-TOPIC NOISE: particle physics — "Light Scalars and the KOTO Anomaly" (arXiv:1911.10203). Do not read again. |
| `L0/confusioninterval3.full.md` (+ `.full.full.md`) | OFF-TOPIC NOISE: particle physics (arXiv:1908.06045). Do not read again. |
| `L0/temperature_passing.full.md` (+ `.full.full.md`) | OFF-TOPIC NOISE: medical-image segmentation — "Learn to Segment Organs with a Few Bounding Boxes" (arXiv:1909.07809). Do not read again. |
