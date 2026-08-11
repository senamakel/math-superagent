# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0/INDEX.md` | Index of the `.full.md` full-text companions to the L1 summaries, including misfiled/accidental downloads. |
| `L0/li_zuchswang.md` | Failed-download note: Li 1976 'Sums of Zuchswang games' is paywalled (DOI redirect, ScienceDirect 403); records what could not be obtained and points to Siegel for the zugzwang-game theory. |
| `L0/siegel_zugzwang.md` | !3 — from https://library.slmath.org/books/Book56/files/12siegel.pdf; not yet read, excerpt pending a scholar summary |
| `L1/INDEX.md` | Index of per-source L1 summaries; read it first to find a source's one-line purpose. |
| `L1/a083652.md` | OEIS A083652 summatory bit-length, exact O(1) closed form; third leg of total bits = ones+zeros. |
| `L1/bitcount.md` | OEIS A000788 summatory 1-bit count, O(log n) recurrences → A(n). |
| `L1/cgt.md` | CGT framework (Conway ONAG, Winning Ways): numbers as games, disjunctive sum; board decomposes. |
| `L1/disjsum.md` | Core structural fact: G(a,b)=a−b, board's no-skip value = A−B. |
| `L1/loopy.md` | Loopy games, stoppers: skip self-loop → DP fixpoint, finite S(n). |
| `L1/mfl_pass.md` | Morrison–Friedman–Landsberg 2011 (arXiv:1204.3222): a one-time pass can drastically change game structure (Nim vs Chomp) — S(n) not readable off no-skip value. |
| `L1/misfiled.md` | Ledger of four accidental arXiv downloads in L0/ unrelated to the problem (compression, KOTO, COHERENT, medical segmentation); dead. |
| `L1/normalplay.md` | Unable-to-move loses; A−B>0 ⇒ One wins without skips. |
| `L1/partisan.md` | Sprague–Grundy inapplicable (disjoint move sets); minimax over (A,B). |
| `L1/pass_waiting.md` | Larsson–Nowakowski–Santos 2015 (arXiv:1505.01907), primary pass/waiting-move theory. |
| `L1/raw_mfl_pass.md` | Raw arXiv abstract of 1204.3222; proper analysis in mfl_pass.md. |
| `L1/raw_pass_waiting_check.md` | Raw arXiv abstract of 1505.01907; proper analysis in pass_waiting.md. |
| `L1/siegel_zugzwang.md` | _(undescribed)_ |
| `L1/strategy.md` | Dead end: generic strategy article, nothing relevant. |
| `L1/surreal.md` | Why a−b is exact (simplest surreal between options); skips outside short games ⇒ A−B ≠ S(n). |
| `L1/trollopedelange.md` | Girgensohn 2011 INTEGERS #A54: explicit Trollope–Delange closed forms (1-periodic fluctuation). |
| `L1/verify_trollopedelange.md` | Numeric check-list to run before quoting Girgensohn. |
| `L1/weightedmom.md` | Larcher & Pillichshammer 2005: k·-weighted moments admit Delange-type closed form (our k·-weighted A,B). |
| `L1/weightedsearch.md` | Dead end: OEIS search on sample S(n) → no result; S(n) ∉ OEIS. |
| `L1/zerocount.md` | OEIS A059015 summatory 0-bit count → B(n); identity A059015 = A083652 − A000788. |
| `L1/zugzwang.md` | Skip = "passing, if allowed, would be best"; One's forced 1-bit consumption → zugzwang. |
| `L2/INDEX.md` | Index of the two synthesis notes (counting arithmetic; game reduction + pass). |
| `L2/counting-arithmetic.md` | Polylog evaluation of A(n)=Σ k·popcount(k) and B(n)=Σ k·zerocount(k) at the n=10^5 scale (A000788 / A059015 / A083652, Trollope–Delange, weighted moments); negative result S(n) ∉ OEIS. |
| `L2/game-reduction-and-pass.md` | The partisan game reduced to counters (A,B); why the no-skip value is A−B but S(n) comes from the budgeted-skip DP (pass theory). |
