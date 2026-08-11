# Coping with cycles — A. Siegel (2009), loopy games & Li's zugzwang games

Source: https://library.slmath.org/books/Book56/files/12siegel.pdf (Games of No
Chance 3, MSRI Publ. 56, 2009; full text `research/L0/siegel_zugzwang.full.md`).

## What it establishes
A primary, theorem-level treatment of **partizan loopy games** — the exact
framework the skip makes this problem:
- **Stopper** = loopy game with no infinite alternating play from any subposition;
  stoppers always terminate in isolation and admit canonical form
  (Theorem 1, 2, Conway). The bit game without skips is a stopper, so its
  value is a well-founded canonical game.
- **Sides/canonical `s & t`** (Theorem 5, Swivel Chair): a loopy game's behaviour
  is captured by its onside/offside stoppers. Pass moves are exactly the loops
  (`f0|passg = over`, `fpass|g = on`, `fpass|passg = dud`).
- **Zugzwang games (Li, 1976)** — games where moving is a disadvantage:
  Definition: every follower has all Left options `<` it and all Right options `>` it.
  **Li's Theorem 7:** a loopy game equals a zugzwang game iff it is `x & y` for
  *dyadic rationals* `x ≤ y`. Weak zugzwang games (theorem 9) are exactly the
  `x & y` with each side `on/off/dyadic/z±over/z±under`.
- **Pseudonumbers** = infinite stoppers generalising surreals (surd = well-founded
  pseudonumber); `bZ = f0,1,2,...|passg = ω : off` is the least upper bound of the
  integers.

## Why it applies here
The library's skip picture was Wikipedia-level ([[zugzwang]], [[loopy]]). This
source is the rigorous theory: each number's game `G(a,b)={G(a-1,b)|G(a,b-1)}` is
the loopfree integer `a−b` (a well-founded pseudo/surreal), and the board is the
disjunctive sum of these stoppers. Adding Zero's skip introduces a `pass` loop, so
the comparative value is governed by the stopper/loopy theory here — Li's
zugzwang games generalise ordinary numbers precisely because in zugzwang it is
disadvantageous to move, which is exactly One's situation (forced 1-bit
consumption). It corroborates that a *pass* is not a normal-play move and is why
S(n) ≠ A−B and needs the (A,B) minimax DP.

## Caveat
This is normal-play/loopy value theory (who wins, values in sums); it does **not**
give the *budgeted* minimum-skip count S(n). Our skip costs budget and Zero alone
may use it — outside this theory's comparison framing. The quantitative S(n)
still comes from the run's (A,B) fixpoint DP. It is warrant for the structural
model, not a formula.
