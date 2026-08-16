# Summary — MacWilliams identity (encyclopedic statement)

Source: Wikipedia, "Enumerator polynomial" / "MacWilliams identity". Source URL: https://en.wikipedia.org/wiki/MacWilliams_identity. Full text: [[research/sources/wikipedia_macwilliams_identity.full]].

## What this establishes

The clean encyclopedic statement of the MacWilliams identity. For a binary linear code `C ⊂ F_2^n` with weight enumerator `W(C;x,y) = Σ_w A_w x^w y^{n−w}` (`A_w` = # words of weight `w`) and dual code `C^⊥ = {x : ⟨x,c⟩=0 ∀c∈C}`:

**`W(C^⊥;x,y) = (1/|C|)·W(C; y−x, y+x)`.**

Also gives the basic weight-enumerator facts (`W(C;1,1)=|C|`, `W(C;1,−1)` = the "excess" alternating sum, etc.), and defines the in inner/outer distance distribution and regular codes (those whose outer-distribution rows over codewords are equal).

## Why it matters for SUPPLY

The weight enumerator of the dual is obtained from the primal by substituting `(x,y)↦(y−x,y+x)` — the Walsh/Hadamard transform in disguise. This is the standard, quotable statement of the identity that every weight-of-image lower bound over `F_2^n` ultimately leans on (via its Krawtchouk diagonalisation). For the open `walsh-spectral-subset-b904` request it is the canonical reference for *what duality does to weight distributions*, and confirms `wt(Φ_n h)` is the kind of object this machinery can in principle reach — but the identity itself is exact and distribution-level, not a lower bound for a fixed input.

## Evidence class / falsifier

Proved identity (standard coding theory). Would be misapplied as giving `wt(Φ_n h) ≥ c·n` directly, since it relates weight *distributions* (code-wide) and carries no input-hypothesis dependence.

```claim
id: macwilliams-identity-statement
statement: For a binary linear code C ⊂ F_2^n with weight enumerator W and dual C^⊥, W(C^⊥;x,y) = (1/|C|) W(C;y−x,y+x). Equivalently the dual weight distribution is the (Krawtchouk/Walsh) transform of C's.
hypotheses: C linear; F_2^n with the standard dot product.
holds-here: Yes — standard statement over F_2^n, the cube on which the fold Φ acts.
status: proved (MacWilliams 1963; this is the standard encyclopedic statement)
bearing: Canonical quotable form of the Walsh duality on the cube; establishes the transform-coordinate setting for weight questions, context for request walsh-spectral-subset-b904, not itself an input-dependent lower bound.
anchor: research/sources/wikipedia_macwilliams_identity.full.md, "MacWilliams identity"
```
