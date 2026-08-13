```approach
idea: Chamberland Type-II generating functions as an alternative to Salez's seven equations — sub-progression families from `n = q·r(k) − 4s₁s₂`
mechanism: The run has covered 94.72% of n ≡ 1 (mod 840) using Salez's seven converse equations (degree-1 linear forms in k). Chamberland 2026 (Integers #A42) provides a second, independent generating mechanism for Type-II families: for each q ≡ 3 (mod 4) and s₁,s₂ | (q+1)/4, the identity

  4/(q·r − 4s₁s₂) = 1/(r·T − s₁s₂) + 1/(T·(qr−4s₁s₂)) + s₁s₂/(T·(rT−s₁s₂)·(qr−4s₁s₂))

with T = (q+1)/4 is an exact unit-fraction identity. Setting n(k) = a·k + b and factoring n(k) + 4s₁s₂ as q·r(k) with r(k) polynomial yields a polynomial family whose denominators have degrees 1, 1, and 2 in k — outside Salez's degree-1 classification. These families are genuinely new shapes: they are not captured by Salez's seven equations (which are complete for degree-1 linear forms), and they reach residue classes by a different arithmetic constraint (q divides n + 4s₁s₂) than the Salez constraint (the converse equation conditions). The sub-progression machinery is the same: Schinzel-legal sub-progressions where the residue is a QNR, just with Chamberland as the identity generator instead of Salez.

status: adopted
precedent: Chamberland 2026 (Integers 26 #A42, Theorem 1, read and summarized); Schuh 2025 Theorem 2B (equivalent parametrisation); Schinzel 2000 Theorem 1 (the QNR constraint on the sub-progression)
first-step: Write a script `code/search_chamberland.py` that, for each q ≡ 3 (mod 4) up to some bound (start q ≤ 47) and each s₁,s₂ | (q+1)/4, enumerates sub-progressions n = a·k + b with b ≡ 1 (mod 840) such that b + 4s₁s₂ ≡ 0 (mod q), making r(k) = (a·k + b + 4s₁s₂)/q a linear polynomial. For each such (a,b,q,s₁,s₂), construct the Chamberland identity, verify it symbolically with is_identity, check integrality and positivity, and measure the union density. Compare the covered residue classes against the 5.28% gap left by the Salez sweep.
killed-by:
```