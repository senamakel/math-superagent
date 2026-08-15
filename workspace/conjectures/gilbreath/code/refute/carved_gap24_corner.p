% Attack the carved-{2,4} class claim (R-carved-gap24 / R-gaps-24 /
% R-carved-gap24-no-first-failure):
%
%   Let A_0 = (2,3,x_1,x_2,...), x_1-3=2, x_{i+1}-x_i in {2,4} for all i>=1.
%   Then there is no first failure: A_k(1) in {0,2} for all k>=1.
%
% The corner argument: the gaps g_2,g_3,... all lie in {2,4}. Then
%   A_1 = (1, g_1, g_2, g_3, ...) = (1, 2, g_2, g_3, ...)
%   A_2(1) = |g_1 - g_2| in {0,2}
%   A_2(j) = |g_j - g_{j+1}| in {0,2} for j>=2
% so row 2 is the {0,2} corner and every later row begins with 1.
%
% Objects: gap values g1=2,g2,g3,g4,g5 each in {2,4}. Predicates:
%   even2(X): X in {0,2}
%   diff_in_02(X,Y): |X-Y| in {0,2}  (modelled for the {2,4} domain)
% Conjecture (what we want to be TRUE for the class, false would be a
% counterexample): a failure exists, i.e. some |g_i-g_j| NOT in {0,2}.
% Since every g in {2,4}, |g_i-g_{i+1}| in {0,2} always: the model finder
% should prove there is no such failure (=> the class never dies at row 2).
%
% We give the finder the domain {2,4} and ask whether a pair of gaps with
% difference outside {0,2} exists. If it returns 'proved' it confirms the
% corner class; if it finds a model with such a pair, that refutes the class.

tff(dom, type, gap: $i).
tff(decl, type, val2: gap > $o).   % value == 2
tff(decl, type, val4: gap > $o).   % value == 4
tff(decl, type, g1: gap).
tff(decl, type, g2: gap).
tff(decl, type, g3: gap).
tff(decl, type, g4: gap).
tff(decl, type, g5: gap).

% each gap is exactly one of {2,4}
tff(g1_v, axiom, ( val2(g1) & ~val4(g1) )).   % g1 = 2 forced by hypothesis
tff(g2_v, axiom, ( val2(g2) | val4(g2) ) & ~( val2(g2) & val4(g2) )).
tff(g3_v, axiom, ( val2(g3) | val4(g3) ) & ~( val2(g3) & val4(g3) )).
tff(g4_v, axiom, ( val2(g4) | val4(g4) ) & ~( val2(g4) & val4(g4) )).

% dist_eq(X,Y): |X-Y| in {0,2} iff both X,Y in {2,4} with equal or adjacent
% values (2-2:0, 2-4:2, 4-2:2, 4-4:0). Since the domain is exactly {2,4},
% |X-Y| in {0,2} ALWAYS.  Encode: for all pairs in the domain, dist_in_02.
tff(decl2, type, dist_in_02: gap > gap > $o).
% define dist_in_02 : always true on the {2,4} domain
tff(dist_def, axiom, ![X:gap, Y:gap]: dist_in_02(X,Y)).

% Row 2 second entry = |g1 - g2| must be in {0,2}, else failure
tff(row2_second, axiom, dist_in_02(g1, g2)).
% Row 2 entries j>=2 = |g_j - g_{j+1}| in {0,2}
tff(row2_3, axiom, dist_in_02(g2, g3)).
tff(row2_4, axiom, dist_in_02(g3, g4)).
tff(row2_5, axiom, dist_in_02(g4, g5)).

% Conjecture: there is a first failure -- A_2(1) NOT in {0,2}.
% (This is the negation of what the class claims; a model satisfying it
% would be a counterexample to the corner class.)
tff(goal, conjecture, ~ dist_in_02(g1, g2)).
