% Refutation of R-depth-k-finite (research/weakened/depth-survival-ladder.md).
%
% Claim (verbatim): "For every fixed k >= 1, the set S_k of gap words
%   (2, g_2, ..., g_k) with all g_i even positive satisfying A_k(1) in {0,2}
%   is FINITE: each gap is bounded by an explicit function of the others and k
%   (a nested absolute value is bounded above by the maximum gap, and the
%   condition A_k(1) <= 2 forces each gap below a computable bound)."
%
% Ladder's own defining formula (verbatim):
%   A_3(1) = ||g_1 - g_2| - |g_2 - g_3||
%
% Counterexample family: fix k=3, g_1=2, g_3=2, g_2 = 2M arbitrary.
% By |a-b| = |b-a|:  |2-g_2| = |g_2-2|, hence
%   A_3(1) = ||2-g_2| - |g_2-2|| = |X - X| = 0  in {0,2}.
% So (2, 2M, 2) in S_3 for EVERY even positive 2M: g_2 is UNBOUNDED while
% g_1, g_3 and k=3 are all fixed.  S_3 is infinite; the claim "each gap is
% bounded by a function of the others and k" is false.
%
% Machine check: encode the claim's negation as the conjecture and ask the
% model finder whether any model exists.  Concretely: can there exist g_2
% even-positive and g_3 = 2 (so g_1=2,g_3=2 fixed) with A_3(1) NOT in {0,2}?
% The finder must fail to build one: by |a-b|=|b-a| the value is identically 0.
%
% We encode the absolute difference and the doubled gaps in lambda-free FOL.
% The gap values live in a numeric sort; absdiff and the tripled function give
% the constraint.  Conjecture asserts a FAILING word, which is unsatisfiable.

tff(dom, type, num: $tType).
tff(decl, type, g1: num).          % = 2, fixed
tff(decl, type, g2: num).          % = 2M, the reason for the parameter
tff(decl, type, g3: num).          % = 2, fixed
tff(decl, type, absd: (num*num) > num).
tff(decl, type, surv: $o).         % survival predicate: A_3(1) in {0,2}

% absd is symmetric and A_3 = | |g1-g2| - |g2-g3| | ; survival means that
% quantity equals 0 or 2.  We axiomatise only the property the family needs:
% g1 = g3, so |g1-g2| = |g2-g3| and their absolute difference is 0, which is
% a survival value.  There is no way to pick g2 to break it.
tff(g1_is_g3, axiom, g1 = g3).
tff(abssym, axiom, ![X:num, Y:num]: absd(X,Y) = absd(Y,X)).
% survival = the two inner absdiffs are equal, i.e. their difference is 0
tff(surv_def, axiom, surv <=> (absd(absd(g1,g2), absd(g2,g3)) = zero)).
tff(zero_const, axiom, zero = zero).  % zero is a name; survival holds if inner equal
% The conjecture (attack): survival FAILS for some g2.  Unsat by symmetry.
fof(goal, conjecture, ~surv).
