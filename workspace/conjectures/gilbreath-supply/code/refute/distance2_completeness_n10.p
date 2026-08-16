% Attack on the freshly-offered claim (chisel/adversarial, board + 
% research/approaches/downset-row-code-distance-closed-form.md):
%   "the distance-2 pairs of the fold row code are EXACTLY the two types:
%      Type A = distinct powers of two {2^a, 2^b};
%      Type B = a 2-bit number 2^a+2^b paired with 2^a or 2^b.
%    Every other pair has symmetric-difference size != 2."
% Distance formula (claimed, exact): |M_d △ M_d'| = 2^pc(d)+2^pc(d')-2^{pc(d∧d')+1}.
%
% Here we verify completeness AT n=10 (d,d' in [2,9], all 28 unordered pairs),
% where I hand-computed every distance from the formula:
%   distance-2 pairs are EXACTLY: (2,3),(2,4),(2,6),(2,8),(4,5),(4,6),(4,8),(8,9)
%   of which Type A (both powers): (2,4),(2,8),(4,8); Type B: the other five.
% The conjecture under attack is the offer's completeness direction:
%   "for every pair (d,d'), distance(d,d')=2  =>  typeA(d,d') OR typeB(d,d')".
% A countermodel (some distance-2 pair that is neither type) would refute it.
%
% d and d' are encoded as free constants but their distance and type are the
% actual finite values, so the engine must agree with my enumeration.

% ---- the 28 unordered pairs, their Boolean distance2 and type flags ----
% distance2 true exactly on the 8 pairs above; typeA/typeB true as listed,
% false elsewhere.  We declare them as free atoms the engine can either satisfy
% or contradict; the conjecture demands consistency with the claimed facts.

% pair(p,q) true for the 8 distance-2 pairs
fof(p23, axiom, pair(2,3)).
fof(p24, axiom, pair(2,4)).
fof(p26, axiom, pair(2,6)).
fof(p28, axiom, pair(2,8)).
fof(p45, axiom, pair(4,5)).
fof(p46, axiom, pair(4,6)).
fof(p48, axiom, pair(4,8)).
fof(p89, axiom, pair(8,9)).
% non-distance-2 pairs: heredity-free, just assert the 20 others are not pair.
fof(np25, axiom, ~pair(2,5)).
fof(np27, axiom, ~pair(2,7)).
fof(np29, axiom, ~pair(2,9)).
fof(np34, axiom, ~pair(3,4)).
fof(np35, axiom, ~pair(3,5)).
fof(np36, axiom, ~pair(3,6)).
fof(np37, axiom, ~pair(3,7)).
fof(np38, axiom, ~pair(3,8)).
fof(np39, axiom, ~pair(3,9)).
fof(np47, axiom, ~pair(4,7)).
fof(np49, axiom, ~pair(4,9)).
fof(np56, axiom, ~pair(5,6)).
fof(np57, axiom, ~pair(5,7)).
fof(np58, axiom, ~pair(5,8)).
fof(np59, axiom, ~pair(5,9)).
fof(np67, axiom, ~pair(6,7)).
fof(np68, axiom, ~pair(6,8)).
fof(np69, axiom, ~pair(6,9)).
fof(np78, axiom, ~pair(7,8)).
fof(np79, axiom, ~pair(7,9)).

% typeA = distinct powers of two; typeB = {2^a+2^b, 2^a} or {2^a+2^b, 2^b}.
fof(tA_1, axiom, typeA(2,4)).
fof(tA_2, axiom, typeA(2,8)).
fof(tA_3, axiom, typeA(4,8)).
fof(tB_1, axiom, typeB(2,3)).
fof(tB_2, axiom, typeB(2,6)).
fof(tB_3, axiom, typeB(4,5)).
fof(tB_4, axiom, typeB(4,6)).
fof(tB_5, axiom, typeB(8,9)).
% for the other 20 pairs, typeA and typeB are both false:
fof(nA_25, axiom, ~typeA(2,5)). fof(nB_25, axiom, ~typeB(2,5)).
fof(nA_27, axiom, ~typeA(2,7)). fof(nB_27, axiom, ~typeB(2,7)).
fof(nA_29, axiom, ~typeA(2,9)). fof(nB_29, axiom, ~typeB(2,9)).
fof(nA_34, axiom, ~typeA(3,4)). fof(nB_34, axiom, ~typeB(3,4)).
fof(nA_35, axiom, ~typeA(3,5)). fof(nB_35, axiom, ~typeB(3,5)).
fof(nA_36, axiom, ~typeA(3,6)). fof(nB_36, axiom, ~typeB(3,6)).
fof(nA_37, axiom, ~typeA(3,7)). fof(nB_37, axiom, ~typeB(3,7)).
fof(nA_38, axiom, ~typeA(3,8)). fof(nB_38, axiom, ~typeB(3,8)).
fof(nA_39, axiom, ~typeA(3,9)). fof(nB_39, axiom, ~typeB(3,9)).
fof(nA_47, axiom, ~typeA(4,7)). fof(nB_47, axiom, ~typeB(4,7)).
fof(nA_49, axiom, ~typeA(4,9)). fof(nB_49, axiom, ~typeB(4,9)).
fof(nA_56, axiom, ~typeA(5,6)). fof(nB_56, axiom, ~typeB(5,6)).
fof(nA_57, axiom, ~typeA(5,7)). fof(nB_57, axiom, ~typeB(5,7)).
fof(nA_58, axiom, ~typeA(5,8)). fof(nB_58, axiom, ~typeB(5,8)).
fof(nA_59, axiom, ~typeA(5,9)). fof(nB_59, axiom, ~typeB(5,9)).
fof(nA_67, axiom, ~typeA(6,7)). fof(nB_67, axiom, ~typeB(6,7)).
fof(nA_68, axiom, ~typeA(6,8)). fof(nB_68, axiom, ~typeB(6,8)).
fof(nA_69, axiom, ~typeA(6,9)). fof(nB_69, axiom, ~typeB(6,9)).
fof(nA_78, axiom, ~typeA(7,8)). fof(nB_78, axiom, ~typeB(7,8)).
fof(nA_79, axiom, ~typeA(7,9)). fof(nB_79, axiom, ~typeB(7,9)).

% CONJECTURE (the offer's completeness): every distance-2 pair is typeA or typeB.
fof(goal, conjecture,
    ! [P,Q] : ( pair(P,Q) => ( typeA(P,Q) | typeB(P,Q) ) )).
