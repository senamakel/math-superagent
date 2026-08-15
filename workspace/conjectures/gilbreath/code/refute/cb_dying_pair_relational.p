% Locate the defect in the open lemma CB-dying-pair.
%
% The lemma states (counterexample-backward skeleton), for a first failure at
% row K:
%   "the dying row K-1 satisfies b_{K-1} = 1, A_{K-1}(0) = 1, and
%    A_{K-1}(1) in {4,6,8,...}"
%
% But b is the leading-{0,2}-block length counting from position 1, so
%   b(r) = 1  <=>  A(r,1) in {0,2}  and  A(r,2) not in {0,2}.
% And "dying" means A_{K-1}(1) NOT in {0,2} (that is what makes
% |1 - A_{K-1}(1)| != 1, the failure at row K).
%
% So "dying" (A_{K-1}(1) not in {0,2}) and "b_{K-1}=1" (A_{K-1}(1) in {0,2})
% are contradictory.  In a real failing triangle (delete 7 from the primes):
%   row K-1 = [1, 4, 4, 2, ...]  with A_{K-1}(1)=4 and b_{K-1}=0.
% The block-length-1 row is K-2, not K-1.  The lemma's own edge/intruder
% analysis (e=A_{K-2}(1), y=A_{K-2}(2), |e-y|=A_{K-1}(1)) is at row K-2.

% Domain values for A(r,1) and A(r,2): {0,2,4,6}
fof(in02_0, axiom, in02(0)).
fof(in02_2, axiom, in02(2)).
fof(notin02_4, axiom, ~in02(4)).
fof(notin02_6, axiom, ~in02(6)).

% the leading block has length b (0 or 1) with
%   b=1  <=>  A(.,1) in {0,2} and A(.,2) not in {0,2}
%   b=0  <=>  A(.,1) not in {0,2}
fof(b_one_iff, axiom, (b=1) <=> (in02(a1) & ~in02(a2))).
fof(b_zero_iff, axiom, (b=0) <=> ~in02(a1)).

% dying: the dying row's second entry is NOT in {0,2}  (this is the
% hypothesis of the dying-row characterization, the thing that fails the
% next row)
fof(dying, axiom, ~in02(a1)).

% values live in the domain
fof(dom_a1, axiom, a1=0 | a1=2 | a1=4 | a1=6).
fof(dom_a2, axiom, a2=0 | a2=2 | a2=4 | a2=6).

% THE CLAIM UNDER ATTACK: the dying row has block length 1.
fof(dying_pair_claim, conjecture, b=1).
