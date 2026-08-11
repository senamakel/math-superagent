# Zugzwang — the mechanism the skip exploits

Source: https://en.wikipedia.org/wiki/Zugzwang

## What it establishes
- **Zugzwang** (German "compulsion to move"): a player is disadvantaged because of the obligation to make a move; every legal move worsens their position.
- In combinatorial game theory it is used specifically for "a move that directly changes the outcome of the game from a win to a loss."
- The Zugzwang article states (general usage): "a situation where **passing the turn, if this were allowed, would be the best move**" — i.e. the ability to pass is a tool for escaping a forced move. This is the closest classical description of this problem's skip rule.

## Why it applies here
- Dr. One is forced to consume a 1-bit on every One turn while A>0. Once A would reach 0 on One's turn, One is in zugzwang: obliged to move but any move is fatal (the position becomes a One-loss). This is precisely why the run's DP treats "A==0 on One's turn" as Zero-won.
- Zero's skips are the pass mechanism from the quoted general usage: Zero converts its own move obligation into an extra One turn, escalating One's zugzwang (consuming more 1-bits per cycle) and relieving Zero's own obligation to consume a 0-bit (which can otherwise exhaust B and make Zero the one stuck).

## Not settled
- Zugzwang describes the qualitative mechanism; it gives no formula. It does not explain the quantity S(n) or its closed form — the DP is required.
