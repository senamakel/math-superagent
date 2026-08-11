# L2 fold: The partisan game, its (A,B) reduction, and the skip/pass

Ten L1 notes cohere into one subject: **what the game is and why it reduces to
the two counters (A,B) with a budgeted skip**. Together they establish:

- The board is a **disjunctive sum** of subgames, one per number
  ([[cgt]], [[disjsum]]): each turn a player changes exactly one number.
- Under CGT each number with `a` 1-bits and `b` 0-bits is the game
  `G(a,b)={G(a-1,b)|G(a,b-1)}` = the integer **a−b** ([[disjsum]], [[surreal]]),
  so the no-skip value of the whole board is the single integer **A−B**
  (A = total 1-bits, B = total 0-bits).
- The game is **strictly partisan** — One deletes only 1-bits, Zero only 0-bits —
  so **Sprague–Grundy does not apply** ([[partisan]]); outcome is decided by
  normal play, unable-to-move loses, and A−B>0 means One wins without skips
  ([[normalplay]]).
- The **skip is a zugzwang escape**: One is forced to consume a 1-bit while
  A>0, and passing (if allowed) would be One's best move ([[zugzwang]]). The
  skip is a self-loop making the DP a fixpoint, but the game is a stopper so a
  finite S(n) exists ([[loopy]]).
- **Pass theory** is a primary, studied topic: [[pass_waiting]] (Larsson–
  Nowakowski–Santos 2015) gives the rigorous scoring-game treatment of passes/
  waiting moves (when extra passes do no harm, order-embedding into normal
  play); [[mfl_pass]] (Morrison–Friedman–Landsberg 2011, arXiv:1204.3222) shows
  dynamically that a pass can *dramatically* change a game's structure (Nim),
  so S(n) cannot be read off the no-skip value and must come from the DP.
  The rigorous *loopy-game* frame for the pass as a 1-cycle, and **Li's zugzwang-
  game theory** (zugzwang games are exactly `x & y` for dyadic `x≤y`), is now the
  primary source [[siegel_zugzwang]] (Siegel 2009, Games of No Chance 3) — the
  theorem-level basis for [[zugzwang]]/[[loopy]]: the no-skip board is a stopper,
  the skip is a pass loop, One is in zugzwang.
- [[strategy]] is a dead end here: generic strategic game theory contributes
  nothing to computing S(n).

**Net result:** the game reduces to the totals (A,B); S(n) is the minimal skip
budget for Zero to win, computed by the (A,B) minimax DP — not from A−B and not
from any closed-form CGT value.
