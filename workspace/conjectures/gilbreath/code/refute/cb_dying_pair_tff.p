% CB-dying-pair defect check, typed TFF.
%
% Open lemma (counterexample-backward skeleton) states, for a first failure
% at row K:
%   "the dying row K-1 satisfies b_{K-1} = 1, A_{K-1}(0) = 1, and
%    A_{K-1}(1) in {4,6,8,...}"
%
% Definitions used by the run:
%   b(r) = number of leading entries at positions 1,2,3,... lying in {0,2}
%          (block_profile: counts row[1:] memberships, starting at pos 1)
%   b(r)=0  <=>  A(r,1) not in {0,2}
%   b(r)=1  <=>  A(r,1) in {0,2}  and  A(r,2) not in {0,2}
%
% The DYING condition at row K-1 (the thing whose failure causes A_K(0)!=1,
% by the reduction A_K(0)=|1-A_{K-1}(1)|) is that the second entry is NOT in
% {0,2}:  A(K-1,1) not in {0,2}.
%
% So "dying" forces b(K-1)=0, while the lemma simultaneously asserts
% b(K-1)=1.  We ask for a model satisfying the definitions and the dying
% condition that nonetheless has the dying row's block length equal to 1
% (the claim).  No such model can exist: the two are contradictory.

tff(dom, type, nr: $i).
tff(dom2, type, elt: $tType).
tff(decl_in02, type, in02: elt > $o).
tff(decl_a, type, a: nr > elt).      % a(r) = A(r,1), the second entry
tff(decl_b, type, b: nr > $rf).
tff(decl_zero, type, zero: nr).
tff(decl_one, type, one: nr).

% b(r)=0 <=> A(r,1) not in {0,2}
tff(def_b0, axiom, ![R:nr]: ( b(R) = $to_rat(0) <=> ~ in02(a(R)) )).
% b(r)=1 <=> A(r,1) in {0,2}  (block length 1 means first position in block)
tff(def_b1, axiom, ![R:nr]: ( b(R) = $to_rat(1) <=> in02(a(R)) )).

% dying condition at row K-1 = "one": second entry not in {0,2}
tff(dying, axiom, ~ in02(a(one))).

% a(one) is one of the four even values under discussion
tff(dom_a, axiom, a(one)=zero | a(one)=$to_int(2) | a(one)=$to_int(4) | a(one)=$to_int(6)).
tff(in02_zero, axiom, in02(zero)).
tff(in02_two, axiom, in02($to_int(2))).
tff(nin02_four, axiom, ~ in02($to_int(4))).
tff(nin02_six, axiom, ~ in02($to_int(6))).

% THE CLAIM UNDER ATTACK: the dying row has block length 1.
tff(dying_pair_claim, conjecture, b(one) = $to_rat(1)).
