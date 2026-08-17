% Refute the G-stabilization candidate threshold for k=3.
%
% Claim: n0(k) = smallest n with |S_{n-1}| >= k is a valid stabilization
% threshold.  For k=3, |S_2| = 3 >= 3 so n0(3) = 3, whose word is S_3 = "01001".
%
% We exhibit a finite model M = the actual word "01001" (5 positions, 2-symbol
% alphabet {s0,s1}) in which:
%    - the axioms (each position holds exactly one symbol; the specific word
%      bits are fixed) hold, and
%    - the conjecture "S_3 contains the factor 101" is FALSE.
%
% That model is a counterexample to "S_{n0(3)} already contains all k+1
% (here all four) length-3 factors of f".  Since f's length-3 factors are
% {001,010,100,101} and "101" is one of them, the candidate threshold misses a
% factor -> the candidate n0 is too small -> claim as stated is FALSE.
%
% Axioms: word cells c0..c4 = 0,1,0,0,1  (the string "01001").
fof(a0, axiom, c0 = 0).
fof(a1, axiom, c1 = 1).
fof(a2, axiom, c2 = 0).
fof(a3, axiom, c3 = 0).
fof(a4, axiom, c4 = 1).

% Conjecture: the length-3 factor "101" occurs somewhere in this word.
fof(has_101, conjecture,
    ( (c0 = 1 & c1 = 0 & c2 = 1)
    | (c1 = 1 & c2 = 0 & c3 = 1)
    | (c2 = 1 & c3 = 0 & c4 = 1) ) ).
