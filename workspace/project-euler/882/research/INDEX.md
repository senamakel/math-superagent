# Index — research

Externally sourced material. One file per source; the run's own derivations and
programs do not belong here.

A downloaded source is stored twice: `<name>.md` is the summary — read this
first — and `<name>.full.md` is the complete converted text, for when the
summary does not answer the question. The rows below describe the summaries.

| File | Purpose |
| --- | --- |
| `cgt.md` | CGT framework: partisan games, {L|R} recursion, zero game, numbers-as-games, disjunctive sum. Basis for viewing the board as a disjunctive sum whose value is integer A−B. |
| `disjsum.md` | Core structural result: each number is G(a,b)={a-b-1|a-b+1}=integer (a−b); the disjunctive sum of all numbers has value A−B — the theory behind the counting reduction. Includes the real-game-vs-model caveat. |
| `loopy.md` | Why the skip creates a self-loop in the DP, resolved as a fixpoint; the game is a stopper so a finite S(n) exists. |
| `normalplay.md` | Connects "unable to move loses" to the normal-play convention; why One (Left) wins without skips given A−B>0. |
| `partisan.md` | Why Sprague–Grundy does NOT apply (disjoint move sets: One deletes 1-bits, Zero deletes 0-bits), so the run uses minimax over (A,B) not nimbers. |
| `strategy.md` | Dead end: generic strategy article, nothing relevant. Marked as examined so nobody reads it again. |
| `surreal.md` | Why G(a,b)=a−b is EXACT (simplest number strictly between left/right options); skips fall outside short-game numbers, so value A−B alone does not give S(n). |
| `zugzwang.md` | Mechanism the skip exploits: One is forced to consume 1-bits each turn (zugzwang); "passing, if allowed, would be best" is the classical description of the skip. |
