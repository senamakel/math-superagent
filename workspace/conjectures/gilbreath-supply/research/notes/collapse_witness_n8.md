# Collapse witness — S² is not a K=1 functional

This files the witness that refutes the first pass's collapse hypothesis
(`research/REOPENED.md`) as a claim block, so the weakened-ledger rung
`R-k1-witness` (research/weakened/supply-order-k.md) has a named establishing
claim.

The witness: at `n = 8`, two strings with identical order-1 correlation
vectors but different fold weight.

```claim
id: collapse-witness-n8-kstar-ge-2
statement: There exist n and distinct binary strings h, h' with identical C₁ (identical 2-gram count vectors) but different fold weight. At n=8, h=00000010 (1 at index 6) and h'=00000100 (1 at index 5) both have C₁ = (5,1,1,0) — 2-grams (00)×5, (01)×1, (10)×1, (11)×0 — yet ν₂(h)=3 and ν₂(h')=4, equivalently S=0 vs −2 and S²=0 vs 4, where S(n)=(n−2)−2ν₂(n) is the signed fold excess. Hence S² is NOT a K=1 functional and K*(8) ≥ 2 (in fact K*(8)=4 by the n=4..20 measurement).
hypotheses: canonical floored fold, d∈[2,n−1]; fold cell T(n,d)=⊕_{o⊆d}h[n−1−d+o] (problem.md facts 1-2); C_K(h) the empirical (K+1)-gram count vector of h, so C₁ counts the 2-grams.
holds-here: yes — this is the whole point of REOPENED.md, and it is pure combinatorics of Φ_8, no primes, no arithmetic.
status: checked (hand-verified) — cell counts: h (1 at index 6) is read by depth d exactly when the offset o=d−(n−1−6)=d−1 is a submask of d, true for d=3,5,7 (d−1 = 2,4,6 ⊆ d), so ν₂=3 and S=6−2·3=0; h' (1 at index 5) is read when o=d−2 ⊆ d, true for d=2,3,6,7 (d−2 = 0,1,4,5 ⊆ d), so ν₂=4 and S=6−2·4=−2, S²=4. The C₁ equality is the single-1 fact: an interior 1 (index 1..n−2) has 2-grams (00)×(n−3), (01)×1, (10)×1, (11)×0, independent of position.
bearing: refutes the first pass's collapse hypothesis (that every functional of the fold factors through pair correlations / K=1). S² itself is a K>1 functional, so the second-moment route does not reduce to mod-4 switch-pair correlation. This is the seed for R-explicit-k-functional and the anchor of the budget ladder supply-order-k.
anchor: research/REOPENED.md (the witness and its hand-verification); research/witness-crosscheck-imported.txt (independent crosscheck n=4..12 flags the same witness and the n=5 mismatch); research/witness-hunt-n20-imported.txt (the n=4..20 table).
```
