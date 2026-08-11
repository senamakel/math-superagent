# Index — research

What each file in this folder is for. Keep it current. Summaries live in `L1/`;
their full source texts in `L0/` (fallback — read the summary first). The two
levels below are the tree; this page is the root that links them.

## Relevant — game theory / structure

| File | Purpose |
| --- | --- |
| `L1/cgt.md` / `L0/cgt.full.md` | CGT framework: partisan games, recursive position form, numbers as games, disjunctive sums. Justifies the board decomposing into a sum of subgames. |
| `L1/disjsum.md` / `L0/disjsum.full.md` | Core structural result: each number with a 1-bits and b 0-bits is the game G(a,b) = integer a-b, so the board reduces to the two totals A,B. |
| `L1/loopy.md` / `L0/loopy.full.md` | Why the skip creates a self-loop in the DP, resolved as a fixpoint; the game is a stopper so a finite S(n) exists. |
| `L1/normalplay.md` | "Unable to move loses" = normal play; why One (Left) wins without skips given A−B>0. |
| `L1/pass_waiting.md` / `L0/pass_waiting.full.md` | Larsson–Nowakowski–Santos (2015), "When waiting moves you in scoring combinatorial games" (arXiv:1505.01907): primary math treatment of passes/waiting moves — when extra passes "do no harm" (order-embedding into Conway normal-play) and the pass as zugzwang/tempo tool. Structural analogue of the problem's Zero-skip. |
| `L1/partisan.md` | Why Sprague–Grundy does NOT apply (disjoint move sets: One deletes 1-bits, Zero deletes 0-bits), so minimax over (A,B) not nimbers. |
| `L1/surreal.md` / `L0/surreal.full.md` | Why G(a,b)=a−b is EXACT (simplest number between options); skips fall outside short-game numbers, so value A−B alone does not give S(n). |
| `L1/zugzwang.md` / `L0/zugzwang.full.md` | Mechanism the skip exploits: One forced to consume a 1-bit each turn; "passing, if allowed, would be best" is the classical description of the skip. |

## Relevant — arithmetic engine (A(n), B(n))

| File | Purpose |
| --- | --- |
| `L1/bitcount.md` / `L0/bitcount.full.md` | OEIS A000788: summatory binary 1-bit count with O(log n) recurrences; supplies A(n) at n=10^5. |
| `L1/zerocount.md` / `L0/zerocount.full.md` | OEIS A059015: summatory binary 0-bit count with O(log n) recurrences, zeros = total-digits − ones; supplies B(n). |
| `L1/trollopedelange.md` / `L0/trollopedelange.full.md` | Girgensohn (2011) INTEGERS #A54: primary proof of explicit Trollope–Delange formulas (main term + continuous 1-periodic fluctuation, O(log n) recurrences) for summatory 1- and 0-bit counts; unweighted engine behind the k·-weighted A(n), B(n). |
| `L1/verify_trollopedelange.md` | Hand-off checklist for tool_builder: numeric checks (ones summatory recurrences, Delange formula 35, zero-count analogue) to run before quoting Girgensohn. Do not delete. |
| `L1/weightedmom.md` / `L0/weightedmom.full.md` | Larcher & Pillichshammer (2005), "Moments of the weighted sum-of-digits function": governing theory for the run's weighted totals A(n)=Σk·popcount(k), B(n)=Σk·zerocount(k); first-moment digit sums admit Delange-type closed forms. Only abstract local (PDF gated). |

## Dead ends / noise — examined, do not re-read

| File | Purpose |
| --- | --- |
| `L1/strategy.md` / `L0/strategy.full.md` | Dead end: generic strategy article, nothing relevant. |
| `L1/weightedsearch.md` | Dead end: OEIS search on sample 1,3,9,13,23,35,56,64 returned nothing; sequence not in OEIS. |
| `L0/confusioninterval.full.md` | OFF-TOPIC: compression/Slepian-Wolf coding (Bauwens & Zimand arXiv:1911.04268). Do not re-read. |
| `L0/confusioninterval2.full.md` | OFF-TOPIC: particle physics (arXiv:1911.10203). Do not re-read. |
| `L0/confusioninterval3.full.md` | OFF-TOPIC: particle physics (arXiv:1908.06045). Do not re-read. |
| `L0/temperature_passing.full.md` | OFF-TOPIC: medical-image segmentation (arXiv:1909.07809). Do not re-read. |
