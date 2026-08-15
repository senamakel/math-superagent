% Concrete member of the refuting family for R-depth-k-finite.
% gaps (2,14,2) i.e. g1=2, g2=14, g3=2.  Full triangle:
%   A_0: 2  3  5 19 21
%   A_1: 1  2 14  2
%   A_2: 1 12 12
%   A_3: 11  0
% A_3(1) = 0 in {0,2}, so this word survives depth 3.
% Encode: a(row,pos) = value.  Conjecture: it FAILS to survive (A_3(1) not
% in {0,2}).  This is false; find_counterexample should find no finite model
% (proved/undecided), confirming survival of this (2,14,2) member.
tff(dom, type, n: $tType).
tff(decl, type, a: (n*n) > $tType).
tff(ax, axiom,
    a(0,0)=2 & a(0,1)=3 & a(0,2)=5 & a(0,3)=19 & a(0,4)=21
    & a(1,0)=1 & a(1,1)=2 & a(1,2)=14 & a(1,3)=2
    & a(2,0)=1 & a(2,1)=12 & a(2,2)=12
    & a(3,0)=11 & a(3,1)=0).
% claim being attacked: A_3(1) NOT in {0,2} for this word (fails-to-survive)
fof(goal, conjecture, ~(a(3,1)=0 | a(3,1)=2)).
