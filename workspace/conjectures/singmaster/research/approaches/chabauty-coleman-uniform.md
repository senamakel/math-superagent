```approach
idea: Chabauty–Coleman uniform rank bound — prove that the Mordell–Weil rank of the Jacobian of C(x,k1)=C(y,k2) is uniformly bounded while genus grows, so Chabauty–Coleman applies for all large (k1,k2) with r < g, giving an effective uniform bound.

status: refuted
killed-by: Four independent obstructions. (1) The `effective-methods-wall` (grounded, held primaries) establishes that no effective integral-point method exists for genus ≥ 3 — Chabauty–Coleman is a RATIONAL-point method (it bounds #X(Q), not #X(Z)), and the binomial problem needs INTEGER points; a rational-point bound doesn't give an integer-point bound because the curve embeds differently in the integer lattice. (2) Even if Chabauty–Coleman applied to integer points, the method requires explicit p-adic integration on Jacobians, which is only implemented for genus 1 (elliptic logarithms) and genus 2 (Stoll's refinements of Coleman); the family leaves genus 2 immediately — `genus{2,n}=floor((n-1)/2)` and `{3,4}` is already genus 3 — so the practical computation doesn't exist beyond a tiny initial segment. (3) The uniform-rank conjecture is unproven and the proposed "Jacobian decomposes in a structured way" claim is speculative — Prym varieties of fiber products are not generally simpler than the original Jacobian, and there is no theorem bounding ranks of such families. (4) The Chabauty–Coleman bound `#X(Q) ≤ #X(F_p) + 2g - 2` (when it applies) GROWS with g, so even if the method worked uniformly it would give `#X(Q) ≤ O(g) = O(k1·k2)`, which is a function of the column indices — not a constant B, and not uniform in (k1,k2). The approach asks to solve a harder open problem (uniform MW rank bound for a high-genus family) to attack Singmaster, with the wrong direction of dependence — each barrier is independently fatal.
precedent:
  https://doi.org/10.1007/BF01393957 (Coleman 1985, effective Chabauty: #X(Q) <= #X(F_p)+2g-2 when r<g, p>2g of good reduction)
  https://arxiv.org/abs/0801.4459 (BMSST 2008, genus-3 effectivity gap)
  effective-methods-wall (this run's grounded impossibility result)
first-step: none — do not re-propose.
```
