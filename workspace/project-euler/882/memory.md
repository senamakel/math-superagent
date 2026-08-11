# Working memory

## Problem
Partisan bit-deletion game. Start with k copies of k, k=1..n. One deletes a
1-bit from a number's binary string (leading zeros dropped; empty -> 0). Zero
deletes a 0-bit. A player unable to move loses. Zero wins iff One cannot move
on One's turn. Only Zero may skip (turn passes to One, skip count +1). S(n) =
minimal total skip budget so Zero has a forced win.

Given: S(2)=2, S(5)=17, S(10)=64. Need S(10^5) ultimately; this task first
builds and validates the two DP programs (real-game brute up to n=8, counting
game up to n=10).

## Established results
(Not yet computed — will fill after running programs.)

## Failed approaches
(none yet)

## Open questions
- Do real-game and (A,B) counting-game S(n) agree for all n where both run?
- What is the closed-form/structure for S(n)?
