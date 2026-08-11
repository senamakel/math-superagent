# Partisan game — why Sprague–Grundy does not apply here

Source: https://en.wikipedia.org/wiki/Partisan_game (Berlekamp et al., *Winning Ways* vol.1 p.17; Conway ONAG 1976)

## What it establishes
- A game is **partisan (partizan)** if it is not impartial: some moves are available to one player and not the other, or payoffs are asymmetric.
- For partisan games the **Sprague–Grundy theorem does not apply** (there is no universal reduction to Nim heaps / nimbers). Analysis instead proceeds through numbers-as-games (surreal values) of Conway.

## Why it applies here
- Dr. One may only delete 1-bits; Dr. Zero may only delete 0-bits. These move sets are disjoint, so the game is strictly partisan. This is why the run cannot use Nim/Grundy values and instead uses a minimax over (A,B); citations confirm partisan games are exactly the case where Sprague–Grundy fails.

## Not settled
- Nothing about bit-deletion specifically; this is generic framing.
