% Definitive verdict: the skeleton's (-1)^{#runs(d)} sign factor is spurious.
%
% Instance n=5, d=3, pos=1.  down-set(3)={0,1,2,3}=one run [0,3], #runs=1.
% Fix the residues r1=r5=1, so:
%   * T(5,3) = h1^h2^h3^h4 = [r1 != r5] = 0  (telescope), so (-1)^T = +1.
%   * chi(r1)chi(r5) = +1.
%   * correct formula  (-1)^T = chi(r1)chi(r5) = +1.
%   * skeleton formula (-1)^T = (-1)^#runs * chi(r1)chi(r5) = -1.
% The two disagree at this instance, so "skeleton formula is correct" is
% FALSE.  We encode: axioms fix the instance and the correct value = +1.
% Conjecture: the skeleton formula also gives +1.  Axiom-consistent (the
% instance exists, correct value +1) but skeleton gives -1, so the conjecture
% is falsified by the instance -> refuted.
%
% Encoding: R_j := (r_j = 3).  r1=r5=1 -> R1=false, R5=false.
%   correct_plus (indicator that (-1)^T = +1) = true.
%   skeleton_plus (indicator that skeleton formula says +1) = chi(r1)chi(r5)
%     negated (because of the #runs=1 factor) = NOT(+1) = false.

fof(fix_R1, axiom, ~R1).
fof(fix_R5, axiom, ~R5).
% correct value: (-1)^T = +1
fof(correct, axiom, correct_plus).
% tie correct_plus to the telescoping truth: (+1) := (r1 == r5), which holds
fof(tie_correct, axiom, ( correct_plus <=> ( (R1 & R5) | (~R1 & ~R5) ) )).
% skeleton says: (-1)^T = -chi(r1)chi(r5), so its +1-indicator = NOT(R1==R5)
fof(tie_skel, axiom, ( skeleton_plus <=> ~( (R1 & R5) | (~R1 & ~R5) ) )).
% Conjecture: skeleton agrees with correct (both +1).
fof(goal, conjecture, ( correct_plus <=> skeleton_plus )).
