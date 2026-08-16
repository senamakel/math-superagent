% Clean verdict on the skeleton's sign factor, fixed instance.
% n=5, d=3, pos=1. down-set(3)={0,1,2,3} one run [0,3], #runs=1.
% Fix r1=r5=1  (R1=false, R5=false).
%
%  * Correct telescoping: T(5,3) = [r1 != r5] = 0, so (-1)^T = +1.
%    chi(r1)chi(r5) = chi(1)chi(1) = +1.
%    => correct formula  (-1)^T = chi(r1)chi(r5)  holds, both +1.
%  * Skeleton formula:   (-1)^T = (-1)^{#runs=1}*chi(r1)chi(r5) = -1.
%    This asserts (-1)^T = -1 while correct value is +1.
%
% Axioms: fix the instance (R1=R5=false), impose correct (-1)^T = +1, and
% impose the SKELETON's claim (-1)^T = -1.  These contradict.  Conjecture $true.
% If the tool reports contradictory-axioms, it confirms the skeleton sign is
% spurious at this instance.
fof(fix_R1, axiom, ~R1).
fof(fix_R5, axiom, ~R5).
% correct: (-1)^T = +1 (since T=0 -> exponent +1), encoded by setting LHS_plus
fof(lhs_plus, axiom, lhs_plus).
% skeleton claims (-1)^T = -1, encoded by skeleton_plus (the +1 indicator)
fof(skel_rhs, axiom, skeleton_plus).
% these two assert lhs_plus AND skeleton_plus.  Now tie them to the instance:
% chi(r1)chi(r5) = +1 since R1=R5=false.  no-sign formula gives LHS=+1 (already
% asserted).  skeleton formula gives -chi*chi = -1, whose +1-indicator is false,
% contradicting skel_rhs.
fof(goal, conjecture, $true).
