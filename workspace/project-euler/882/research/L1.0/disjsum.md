# Disjunctive sum — the structural fact behind the (A,B) reduction

Source: https://en.wikipedia.org/wiki/Disjunctive_sum

## What it establishes
- The **sum / disjunctive sum** G+H of games: each player on a turn moves in exactly ONE of the two components; the game ends when no move exists in any component (normal play).
- Sum of any number of games defined similarly. Fundamental operation behind Sprague–Grundy (impartial) and the whole partisan theory.
- Sum is commutative and associative (Conway 1976). Negation −G trades player roles; G + (−G) is a zero game (second-player win by echoing), giving the games an abelian group structure; numbers (surreal values) add like integers.

## Why it applies here
- The full board "k copies of k, k=1..n" is a disjunctive sum of n subgames, one per number value (with multiplicities). Each turn a player selects exactly one number and deletes a bit — exactly one component at a time — which is the disjunctive-sum rule. Conway's Go-endgame motivation (decomposing a board into independent regions whose values add) is the template.

## The concrete structural result it yields (derived, checkable)
- Model each number with a 1-bits and b 0-bits as the game G(a,b) with G(0,0)=0, One-moves G(a-1,b), Zero-moves G(a,b-1). Inductively G(a,b) = the integer (a−b):
  - G(1,0)={0|}=1; G(0,1)={|0}=−1; G(1,1)={−1|1}=0 (simplest number strictly between −1 and 1).
  - G(a,b)={a-b-1 | a-b+1} whose simplest number is a-b.
- The disjunctive sum of the components therefore has value equal to the single integer **A−B** (A = total 1-bits, B = total 0-bits). This is the theoretical core of "the game reduces to counting bits":
  - Pure normal play, no skips: value A−B>0 matters, so One (Left) wins regardless of who starts — matching the problem's "Dr. Zero can never win".
  - Skips are not normal-play moves; they are the tempo tool (see zugzwang note).

## Caveat — the model vs the real bit game
- The value a−b is computed in the COUNTING model, which assumes a One-move consumes exactly one 1-bit and leaves B unchanged (and vice versa for Zero). In the REAL bit game, deleting the leading 1 of e.g. "1000" exposes leading zeros that are dropped ("1000"→"000"→0), destroying extra 0-bits in one move. So the counting model and the real game can differ in detail; whether they agree on S(n) is an empirical claim the run is checking (counting.py vs brute.py; given S(2)=2, S(5)=17, S(10)=64). The A−B score being a single number explains reducibility to the two numbers A,B, but the skip race still needs BOTH A and B (One's move potential and Zero's exhaustion constraint), which is why the DP is over (A,B) and not just A−B.
