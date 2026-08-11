# Working memory

## Problem

PE591: find the quadratic integer a + b·sqrt(d), |a|,|b| ≤ n = 10^13, d non-square < 100,
closest to pi. BQA_d(pi,n) = that closest value; answer = Σ |I_d(BQA_d(pi,n))| = Σ |a|.

Given (verified statement): BQA_2(pi,10)=6−2√2; BQA_5(pi,100)=26√5−55;
BQA_7(pi,10^6)=560323−211781√7; I_2(BQA_2(pi,10^13))=−6188084046055.

## Established results

Reduction: s=√d, α={√d}=s−⌊s⌋∈(0,1), β={π}.
- Fixed b: best a = round(π−b·s); error = ‖π−b·s‖ = ‖π−b·α‖ (distance to nearest integer)
  = circular distance from {bα} to β.
- b≥0: target β={π}; b<0: t=−b≥0, target {−π}=1−β.
- Feasible bounds: B⁺ = ⌊(n+π)/√d⌋, B⁻ = ⌊(n−π)/√d⌋ (clamp to [0,n]).
- Core subproblem reduced to: irrational α∈(0,1), target β∈[0,1), bound B;
  find b∈[0,B] minimizing dist_circ({bα}, β) — the inhomogeneous Diophantine
  / best left-right approximation problem.

Primary algorithm (Cabanillas-López & Labbé arXiv:1904.01874, Props 9 & 10, Alg 3):
  - CF of α: a_k, q_k (q_{-1}=0,q_0=1, q_n=a_n q_{n-1}+q_{n-2})
  - δ_{-1}=1, δ_0=α, δ_n = −a_n δ_{n-1} + δ_{n-2}   (= (−1)^n(q_n α−p_n) > 0, ↓0)
  - α-numeration digits of β: b_k = min(a_k, ⌈β_{k-1}/δ_{k-1}⌉); β_k = b_k δ_{k-1} − β_{k-1}
  - Best RIGHT candidates (Prop 9): n=0, terminal prefix Σ_{i≤s} b_i q_{i-1}, and
        n = Σ_{i=1..2k−1} b_i q_{i−1} + j q_{2k−1}, j∈{0..b_{2k}−1}, k≥1
  - Best LEFT candidates (Prop 10): terminal prefix, and
        n = Σ_{i=1..2k} b_i q_{i−1} + j q_{2k}, j∈{0..b_{2k+1}−1}, k≥0
  - Global best in [0,B] among these O(log B) candidates.
  - Complexity O(log B): q_n grows exponentially (continuant ~ const·θ^n for quadratic α).
- Negative b: same routine with target 1−β.

## Failed approaches

- (Not attempted at full size — prohibited.) Plain scan over b is O(B) — wrong method.
- Enumerating all (a,b) pairs is O(n^2) — wrong.
- A "nearest-rational / Farey-enclosing" approach on the SINGLE number works for
  homogeneous approximation but not for the inhomogeneous shift β with two-sided (left+right)
  closest point — the α-numeration best left/right characterization is the correct structure.

## Open questions

- (For the solver agent.) Confirm verification script runs 0-mismatch before trusting the
  enumerated candidates; the current workspace couldn't execute it (no exec tool here).
- Tie-breaking among equal |a| is unspecified by the statement; the reference given
  BQA_2(pi,10)=6−2√2 is used to disambiguate the convention. I_2(pi,10^13)=−6188084046055
  pins the d=2, n=10^13 answer.
