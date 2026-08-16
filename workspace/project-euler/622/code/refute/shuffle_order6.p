% Attack on the structural core of G-shuffle-order at deck size n=6.
% The out-faro shuffle s is a permutation on positions 0..5 with the values
% given by the physical interleave (split in half, interleave).  The run claims
% its order equals ord_{n-1}(2) = ord_5(2) = 4.
%
% s (one shuffle), from the interleave of [0,1,2,3,4,5]:
%   0->0, 1->2, 2->4, 3->1, 4->3, 5->5.
% We encode s and its powers s2=s∘s, s3=s∘s∘s, s4=s∘s∘s∘s via axioms, then
% attack the claim "s has order exactly 4" (s4 = identity, s2 != id, s3 != id).

fof(s_0, axiom, s(0) = 0).
fof(s_1, axiom, s(1) = 2).
fof(s_2, axiom, s(2) = 4).
fof(s_3, axiom, s(3) = 1).
fof(s_4, axiom, s(4) = 3).
fof(s_5, axiom, s(5) = 5).

% s2 = s∘s
fof(s2_0, axiom, s2(0) = 0).
fof(s2_1, axiom, s2(1) = 4).
fof(s2_2, axiom, s2(2) = 3).
fof(s2_3, axiom, s2(3) = 2).
fof(s2_4, axiom, s2(4) = 1).
fof(s2_5, axiom, s2(5) = 5).

% s3 = s∘s2
fof(s3_0, axiom, s3(0) = 0).
fof(s3_1, axiom, s3(1) = 3).
fof(s3_2, axiom, s3(2) = 1).
fof(s3_3, axiom, s3(3) = 4).
fof(s3_4, axiom, s3(4) = 2).
fof(s3_5, axiom, s3(5) = 5).

% s4 = s∘s3  (should be identity if order divides 4)
fof(s4_0, axiom, s4(0) = 0).
fof(s4_1, axiom, s4(1) = 1).
fof(s4_2, axiom, s4(2) = 2).
fof(s4_3, axiom, s4(3) = 3).
fof(s4_4, axiom, s4(4) = 4).
fof(s4_5, axiom, s4(5) = 5).

% Conjecture: s has order exactly 4, i.e. s4 = id and s2 != id, s3 != id.
fof(goal, conjecture,
    ( (s2(0)≠0 | s2(1)≠1 | s2(2)≠2 | s2(3)≠3 | s2(4)≠4 | s2(5)≠5) &
      (s3(0)≠0 | s3(1)≠1 | s3(2)≠2 | s3(3)≠3 | s3(4)≠4 | s3(5)≠5) )).
