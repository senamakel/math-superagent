# Shared context

Token budget 10,000; currently ~430 tokens. This file is re-sent on every model
call in every reading role, so keep it to what an agent would otherwise rebuild
from disk (established results with basis, dead ends, computed numbers, recalled
memory, contradictions, gaps). Link the file holding compressed detail. Durable
findings go to Cognee, not here.

## Established

- **Problem (sourced, `[[problem.md]]`).** PE 241. For positive integer n let
  σ(n) = sum of all divisors of n. Perfection quotient p(n) = σ(n)/n. Find the
  sum of all positive integers n ≤ 10^18 with p(n) = k + 1/2, k integer. Equivalently
  2σ(n) = (2k+1)·n. Worked example: σ(6)=12. (Perfect numbers are the k=1 case σ(n)=2n.)
- **Governing structure (conjectured direction, not yet executed).** p(n) is
  multiplicative: if n = ∏ p_i^{a_i} then σ(n)/n = ∏ (p^{a+1}−1)/(p^a(p−1)).
  The half-integer condition is the 2-adic equation 2σ(n)=m·n with m=2k+1 odd.
  NaN constraint: if a = v2(n), u = n/2^a odd, then v2(σ(u)) = a−1 forces the
  2-adic structure of σ(n). Effective algorithm expected to be a finite DFS over
  prime factors (each added p^e maps the quotient p(n) geometrically), NOT a scan
  up to 10^18. Nothing at full size computed yet.

## Ruled out

- None yet. (This is cycle one; no approach has failed and none validated.)

## Numbers

- Oracle: σ(6)=12 (from statement). No computed terms yet — brute.py, the
  obvious naive program that reproduces the statement's example, is the next
  required artifact and is not yet written.

## Recalled

- No durable memory bears on this problem or on abundancy/multiply-perfect
  theory. Durable brain holds only unrelated Erdős–Gyárfás cubic-bipartite
  findings. Do not import those; hypotheses are unchecked here.

## Contradictions

- None yet.

## Gaps

- The governing theory request is open: `research/REQUESTS.md` id
  theory-numbers-with-88d5 (bounding/recursion over 2σ(n)=m·n, m odd, for
  n≤10^18). It closes when a note records a claim block with
  `answers: theory-numbers-with-88d5`. The efficient method in step 3 depends on
  this being filled.
