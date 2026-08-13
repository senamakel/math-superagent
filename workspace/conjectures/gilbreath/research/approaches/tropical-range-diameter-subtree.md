```approach
idea: tropical-range-diameter-subtree
mechanism: |
  This was an EXACT-INTEGER invariant route using only |a-b| = max(a,b) - min(a,b),
  expanding A_k(1) as an alternating max/min of signed linear forms in
  p_2, …, p_{k+2} — the diameter of a tropical decision tree. The proof
  mechanism was a pairing/cancellation certificate: exhibit an involution on
  the leaves matching max-branch and min-branch monomials coefficient-by-coefficient
  on every p_j except a residual ≤ 2. This would prove the conjecture by induction
  without naming a block or intruder.
status: refuted
precedent: |
  > Run's own exhaustive check (code/out/check_runcount_lemma.py, 
  code/out/check_runcount_lemma_class.captured.txt): the lemma r(T(x)) ≤ r(x) 
  — the number of maximal constant runs is non-increasing under the 
  absolute-difference map — is FALSE. Counterexample within the actual 
  {0,2}-block regime: (0,0,1,1) → T(0,0,1,1) = (0,1,0), 2 runs → 3 runs 
  (halved form of {0,2}-block interior (0,0,2,2)). A pairing certificate 
  canceling all but ≤ 2 would imply r(T(x)) ≤ r(x) as a special case, which 
  is false. Exhaustive check: 6,725,600 strings length 1..8 values 0..6, 
  plus class-restricted check on even-valued {0,2,4,6} and halved {0,1,2,3} 
  strings — failures persist in all classes. 

  Additional structural problems: the leaf count grows as ~2^k (each |u-v| 
  branches into two), so no practical certificate exists even if the pairing 
  were true. The Ducci borderline classification (Chamberland 2003, Lemma 3.1: 
  (a,a,c,c) is exactly the rigid equality case where the max-factored potential 
  does NOT decrease) confirms this is not a bug but the structural equality case 
  — exactly the regime the conjecture targets.

killed-by: |
  The run-count lemma r(T(x)) ≤ r(x) is refuted within the actual {0,2}-block 
  regime (counterexample (0,0,1,1) = halved {0,2} interior). A pairing 
  certificate with residual ≤ 2 would imply this lemma, so the certificate 
  cannot exist. Additional: exponential leaf explosion (~2^k), and the Ducci 
  borderline classification (a,a,c,c) is exactly the rigidity where the 
  max-decrease potential stalls — the pairing fails exactly at the 
  combinatorially rigid case the conjecture must handle.
first-step: — (refuted)
```