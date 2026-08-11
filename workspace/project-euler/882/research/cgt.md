# Combinatorial game theory (CGT) — framework for the bit-deletion game

Source: https://en.wikipedia.org/wiki/Combinatorial_game_theory
(Covers Conway/Berlekamp/Guy; primary texts: Conway, *On Numbers and Games*, Academic Press 1976; Berlekamp/Conway/Guy, *Winning Ways*, 1982.)

## What it establishes
- A **partisan game** is one where the move sets of the two players differ (relaxation of the impartial condition). The theory of partisan games was introduced by Berlekamp, Conway, Guy (Winning Ways 1982), first published in Conway's ONAG (1976).
- The recursive definition: a position is `{L | R}`, `L` the set of moves open to Left, `R` the moves open to Right; each option is itself a game. Alternation of turns is implicit.
- The **zero game** `0 = {|}`, where neither player can move; the player whose turn it is loses.
- **Numbers as games**: positive = advantage to Left, negative = advantage to Right; e.g. `1={0|}`, `-1={|0}`, and sums behave like integer arithmetic. Games that are numbers belong to the surreal numbers.
- The **disjunctive sum** G+H: each player per turn moves in exactly one of the two components; game ends when no move exists in any component. This leads to the group/abelian structure of games and is the fundamental reduction tool.
- Outcome is a function of the position's value: when a game is a number, its sign (and who is to move) determines the winner.

## Why it applies to this problem
- The whole board is a **disjunctive sum** of one subgame per number: each turn a player picks exactly one number and alters it. That is precisely the definition of a disjunctive sum (source, "Disjunctive sum" section and "Difference with traditional game theory" re: Go decompositions).
- In the run's counting reduction, each number x with a 1-bits and b 0-bits is modelled as the game `{G(a-1,b) | G(a,b-1)}`, G(0,0)=0. One can show by induction this equals the integer `a-b`: the position's total value is therefore `A-B`, an integer (surreal number). Hence the outcome without skips is decided by the sign of `A-B`.
- The run's `counting.py` is exactly this sum-of-numbers model plus a pass option.

## What it does NOT settle
- The CGT value `a-b` is derived in the *counting* model, which assumes a One-move removes exactly one 1-bit and leaves B unchanged. In the real bit game, deleting the leading 1 of e.g. "1000" exposes leading zeros that are dropped, destroying additional 0-bits. CGT alone does not prove the counting model equals the real game; that equivalence is an empirical conjecture the run is validating (given values S(2)=2, S(5)=17, S(10)=64). Sources do not discuss bit-deletion games.
