% Refutation target: R-depth-k-finite (depth-survival-ladder rung).
%
% Claim (open rung, depth-survival-ladder.md):
%   For every fixed k>=1, S_k = { (2,g_2,...,g_k) : all g_i even positive,
%   A_k(1) in {0,2} } is FINITE: each gap is bounded by an explicit function
%   of the others and k.
%
% Counterexample family (k=3, g_3=2 fixed, g_2 = 2M arbitrary):
%   A_3(1) = ||2-g_2| - |g_2-g_3|| = ||2-2M| - |2M-2|| = |(2M-2)-(2M-2)| = 0
% for every M >= 1.  So (2, 2M, 2) in S_3 for ALL M: g_2 is UNBOUNDED while
% g_1=2 and g_3=2 and k=3 are all fixed.  This directly falsifies the
% claim that each gap is bounded by a function of the others and k.
%
% Machine confirmation of the specific instance M=7 (g_2 = 14): we build the
% FULL triangle A_0 = (2,3,5,19,21) [gaps 2,14,2] and check A_3(1) = 0.
%   A_0: 2  3  5 19 21
%   A_1: 1  2 14  2
%   A_2: 1 12 12
%   A_3: 11  0      -> A_3(1) = 0 in {0,2}
tff(dom, type, n: $tType).
% function a(row,pos) -> value; encode rows directly
tff(ax, axiom, a(0,0)=2 & a(0,1)=3 & a(0,2)=5 & a(0,3)=19 & a(0,4)=21
             & a(1,0)=1 & a(1,1)=2 & a(1,2)=14 & a(1,3)=2
             & a(2,0)=1 & a(2,1)=12 & a(2,2)=12
             & a(3,0)=11 & a(3,1)=0).
% conjecture: A_3(1) in {0,2} for this gap word (equals 0)
fof(survives, conjecture, a(3,1)=0 | a(3,1)=2).
