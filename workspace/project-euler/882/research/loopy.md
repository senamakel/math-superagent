# Loopy games — why the skip makes the DP a fixpoint, not a plain DAG

Source: https://en.wikipedia.org/wiki/Loopy_game

## What it establishes
- A **loopy game** is one where play can return to a previously reached position, creating cycles in the game tree. Loop-free finite games are **short games**.
- Loopy games can continue indefinitely, introducing a third outcome (draw/tie) beyond win/loss; a player "survives" by reaching a tie or win.
- Canonical loopy prototypes: `dud={dud|dud}` (universal draw), `on={on|}` (only Left can move, loops), etc.
- **Stoppers** are loopy games with no subposition allowing infinite alternating runs — they can never tie.

## Why it applies here
- The **skip** is a move from state (A,B) back to the SAME state (A,B) (just with turn flipped to One). This is a self-loop in the game graph, making `need_zeroturn`'s recursion self-referential. The run's `counting.py` resolves it as a fixpoint: Z(A,B) = min( O(A,B-1), 1+O(A,B) ) where O=need_oneturn — the "1+" is the cost of one skip.
- This game is ultimately a **stopper** (skips only delay; moves strictly decrease A or B, so every infinite-loop is avoidable and the tie is never forced), which is why a finite S(n) exists and the fixpoint is well-founded. The formal basis for analysing these value equations comes from Conway's loopy-game theory.

## Not settled
- Wikipedia's loopy article is thin on the algebraic theory (it leans on a single source). It does not give the quantitative account of S(n); the DP does. Use it only as the reason the self-loop is legitimate (a stopper, no forced tie).
