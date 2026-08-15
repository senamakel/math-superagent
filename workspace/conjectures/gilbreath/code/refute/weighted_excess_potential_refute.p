% Universal refutation of R-weighted-excess-potential.
%
% Claim: exists summable weights w_i>=0, w_1>0, with defect d_i=max(0,A(i)-2),
% such that P(A')=sum w_i d'_i <= P(A)=sum w_i d_i for EVERY absolute-difference
% array A (A' = row operator image).
%
% Counterexample array (interior): parent A=(1,4,12,0), child A'=(3,8,12).
%   parent defects d = (2, 10, 0)   [cols 1,2,3]
%   child  defects d'= (6, 10)      [cols 1,2]
% P(A')-P(A) = (6-2)w_1 + (10-10)w_2 - 0*w_3 = 4 w_1 > 0  for all w_1>0.
% So no weight sequence works; potential is NOT monotone on this pair.
%
% The row operator: A'(i)=|A(i)-A(i+1)| with A(0)=1 leading, interiors even.
fof(parent1, axiom, dp1 = 2).   % d_1 = max(0,4-2)
fof(parent2, axiom, dp2 = 10).  % d_2 = max(0,12-2)
fof(parent3, axiom, dp3 = 0).   % d_3 = max(0,0-2) dropped column
fof(child1,  axiom, dc1 = 6).   % d'_1 = max(0,8-2)
fof(child2,  axiom, dc2 = 10).  % d'_2 = max(0,12-2)
% w_1 > 0 required by the claim.
fof(w1pos, axiom, w1 > 0).
% Conjecture (the thing being attacked): the weighted potential IS non-increasing
% on this pair, i.e. 6 w1 + 10 w2 <= 2 w1 + 10 w2 + 0 w3  (=> 4 w1 <= 0).
% A model satisfying the negation (4 w1 > 0) falsifies the conjecture -> refutes
% the universal monotonicity for ANY weights with w1>0.
fof(goal, conjecture, (6*w1 + 10*w2) <= (2*w1 + 10*w2 + 0*w3)).
