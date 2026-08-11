# Pass/waiting moves in combinatorial games — Larsson, Nowakowski, Santos (2015)

Source: https://arxiv.org/abs/1505.01907 (Full text: research/L0/pass_waiting.full.full.md)
Larsson, U., Nowakowski, R. J., Santos, C. P. "When waiting moves you in scoring
combinatorial games." arXiv:1505.01907 [math.CO], 2015. DOI 10.48550/arXiv.1505.01907.

## What it establishes
- Studies **scoring games** (player with higher final score wins) with **passes /
  waiting moves** — an extra move that a player may take instead of a substantive one.
- Characterizes the class of scoring games where "extra pass moves for a player does
  **no harm**": they admit an **order-embedding into Conway's Normal-play games**, so
  their winner/structure reduces to the well-understood short-normal-play theory.
- Generalizes Ettinger's theory of dicot scoring games to a theorem for comparing
  games with scores (numbers), via the pass/waiting-move structure.
- **Zugzwang / tempo framing**: a waiting move is exactly the tool a player uses when
  *moving is a disadvantage* (zugzwang) — the position's value to the player who must
  move is lower than to the one who may pass. The paper analyzes how adding passes can
  hurt or help, i.e. how waiting moves "move" the score.
- (Compare: Morrison, Friedman & Landsberg 2011, "Combinatorial games with a pass: a
  dynamical systems approach", showed a pass can radically change Nim's structure.)

## Why it applies here
The problem's **skip** ("only Zero may skip; turn passes to One, skip count +1") is a
waiting move / pass. The running library's picture (zugzwang.md, loopy.md) is that One
is in zugzwang — forced to consume a 1-bit every One turn — and the skip costs Zero a
budgeted tempo. This source adds a *primary, math-rigorous* treatment of exactly that
phenomenon: it characterizes when the player with the pass is unharmed and frames the
pass as an order-embedding into normal-play values. It corroborates that a skip is not a
normal-play move but a well-studied pass/waiting-move device whose value is governed by
zugzwang, consistent with the run's A−B no-skip value and the (A,B)-skip DP.

## Caveat
- It is a **scoring-game** framework (maximize score), whereas the problem is a
  **normal-play, fixed-budget-skip** game; the theorem's hypotheses (pass does no harm)
  are not literally our rule (Zero's skip costs budget). It is a structural analogue,
  not a recipe for S(n). The quantitative S(n) still comes from the (A,B) minimax DP.
