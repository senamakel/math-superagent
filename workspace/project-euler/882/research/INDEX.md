# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0.0/li_zuchswang.md` | Li, "Sums of zugzwang games" (1976), the original zugzwang-game paper — NOT obtained (Elsevier paywall); recorded so the attempt is not repeated. Theory sourced instead via Siegel's survey. |
| `L0.1/siegel_zugzwang.md` | Summary of Siegel, "Coping with cycles" (Games of No Chance 3, 2009): partizan loopy CGT — stoppers, sides (on/off/over/dud), Li zugzwang games (x & y with dyadic x<=y), pseudonumbers. Warrants the (A,B) stopper/loopy model for the bit game's skip-as-pass loop; no formula for S(n). Reference analysis in L1.1/siegel_zugzwang.md. |
| `L0.2/simplicity_rule_dyadic.md` | Fenner & Rogers 2015 (arXiv:1505.07416): Simplicity Rule — each finite numeric game equals the simplest dyadic rational strictly between its Left/Right option values (v({0 |
| `L1.0/a083652.md` | OEIS A083652 summatory bit-length, exact O(1) closed form; third leg of total bits = ones+zeros. |
| `L1.0/bitcount.md` | OEIS A000788 summatory 1-bit count, O(log n) recurrences → A(n). |
| `L1.0/cgt.md` | CGT framework (Conway ONAG, Winning Ways): numbers as games, disjunctive sum; board decomposes. |
| `L1.0/disjsum.md` | Core structural fact: G(a,b)=a−b, board's no-skip value = A−B. |
| `L1.0/flajolet_weighted_digitalsums.md` | Cheung–Flajolet–Golin–Lee 2010 (arXiv:1003.0150): weighted binary digital sums have exact main-term + periodic-fluctuation closed forms → polylog warrant for k·-weighted A(n),B(n). |
| `L1.0/loopy.md` | Loopy games, stoppers: skip self-loop → DP fixpoint, finite S(n). |
| `L1.0/mfl_pass.md` | Morrison–Friedman–Landsberg 2011 (arXiv:1204.3222): a one-time pass can drastically change game structure (Nim vs Chomp) — S(n) not readable off no-skip value. |
| `L1.0/minabutdinov_qweighted.md` | Primary (arXiv) generalized Trollope–Delange for weighted digit sums with Takagi–Landsberg limit curves; corroborates that k·-weighted A(n),B(n) stay polylog-computable. |
| `L1.0/misfiled.md` | Ledger of four accidental arXiv downloads in L0/ unrelated to the problem (compression, KOTO, COHERENT, medical segmentation); dead. |
| `L1.0/normalplay.md` | Unable-to-move loses; A−B>0 ⇒ One wins without skips. |
| `L1.1/partisan.md` | Sprague–Grundy inapplicable (disjoint move sets); minimax over (A,B). |
| `L1.1/pass_waiting.md` | Larsson–Nowakowski–Santos 2015 (arXiv:1505.01907), primary pass/waiting-move theory. |
| `L1.1/raw_mfl_pass.md` | Raw arXiv abstract of 1204.3222; proper analysis in mfl_pass.md. |
| `L1.1/raw_pass_waiting_check.md` | Raw arXiv abstract of 1505.01907; proper analysis in pass_waiting.md. |
| `L1.1/siegel_zugzwang.md` | A. Siegel, "Coping with cycles" (2009): partizan loopy games, stoppers, Li zugzwang games; warrant for the (A,B) stopper/loopy model, not a formula for S(n). |
| `L1.1/strategy.md` | Dead end: generic strategy article, nothing relevant. |
| `L1.1/surreal.md` | Why a−b is exact (simplest surreal between options); skips outside short games ⇒ A−B ≠ S(n). |
| `L1.1/trollopedelange.md` | Girgensohn 2011 INTEGERS #A54: explicit Trollope–Delange closed forms (1-periodic fluctuation). |
| `L1.1/verify_trollopedelange.md` | Numeric check-list to run before quoting Girgensohn. |
| `L1.1/weightedmom.md` | Larcher & Pillichshammer 2005: k·-weighted moments admit Delange-type closed form (our k·-weighted A,B). |
| `L1.2/L0.0.md` | Seal note for batch L0.0: the 10 original notes (a083652, bitcount, cgt, confusioninterval×3, disjsum, flajolet×2, li_zuchswang) establish the game's no-skip value A−B, the polylog arithmetic engine, and record the misfiled li/confusion dead-ends. Wikilinks each covered note; sealed once, never revisited. |
| `L1.2/weightedsearch.md` | Dead end: OEIS search on sample S(n) → no result; S(n) ∉ OEIS. |
| `L1.2/zerocount.md` | OEIS A059015 summatory 0-bit count → B(n); identity A059015 = A083652 − A000788. |
| `L1.2/zugzwang.md` | Skip = "passing, if allowed, would be best"; One's forced 1-bit consumption → zugzwang. |
| `L2.0/counting-arithmetic.md` | L2 synthesis: polylog evaluation of A(n)=Σk·popcount(k) and B(n)=Σk·zerocount(k) at n=10^5 scale — summatory A000788/A059015 recurrences, Trollope–Delange structure, k·-weighted moment closed forms; S(n) ∉ OEIS. Synthesises bitcount/zerocount/a083652/trollopedelange/verify_trollopedelange/weightedmom/weightedsearch. |
| `L2.0/game-reduction-and-pass.md` | L2 synthesis of the game: reduction to counters (A,B) with a budgeted skip, why the no-skip value is A-B yet S(n) differs (the (A,B) stopper/loopy minimax DP governs). Synthesizes the CGT/surreal/pass derived sources. |
