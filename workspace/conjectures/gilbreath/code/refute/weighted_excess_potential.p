% Refute R-weighted-excess-potential (excess-energy-ladder).
%
% Claim: There exist summable weights w_i >= 0 with w_1 > 0 such that the
% weighted excess P(A) = sum_i w_i * max(0, A_i - 2) is non-increasing under
% the row operator A' = (|A_i - A_{i+1}|).
%
% One-line counterexample: A = (0,4,0)  ->  A' = (4,4).
%   P(A)  = w2*2
%   P(A') = w1*2 + w2*2
%   P(A') <= P(A)  ==>  w1 <= 0, contradicting w_1 > 0.
%
% Encodings:
%   - delta1: a row A' whose entries are the diffs of a row A, with the
%     defect-mass jump written as an inequality over the unknown weights.
%   - goal:   the negation of non-increase forced by the single spike
%     (0,4,0)->(4,4), i.e. we want a model where P(A') > P(A).
% A model satisfying axioms and goal falsifies "non-increasing for all rows".
%
% We must NOT assert w1 > 0 (that is part of the claim, being refuted here is
% the opposite direction); instead we let find_counterexample discover the
% contradiction: the spike forces P(A') = P(A) + w1, so any model has
% P(A') = P(A) + w1.  For a genuine refutation we add w1 > 0 as an axiom
% (allowed: it is a hypothesis of the existential claim being attacked) and
% try to satisfy P(A') <= P(A); that is UNSAT, showing the claimed class of
% weights cannot exist.

% Hypothesis of the claim: w1 > 0, w2 in Z (free), defect masses.
fof(spike_A, axiom, a0 = 0 & a1 = 4 & a2 = 0).
% A' = (4,4): difference row
fof(spike_Ap, axiom, ap0 = 4 & ap1 = 4).
% defect masses
fof(da0, axiom, da0 = max(0, a0 - 2)).
fof(da1, axiom, da1 = max(0, a1 - 2)).
fof(da2, axiom, da2 = max(0, a2 - 2)).
fof(dap0, axiom, dap0 = max(0, ap0 - 2)).
fof(dap1, axiom, dap1 = max(0, ap1 - 2)).
% weighted potentials
fof(PA, axiom, PA = w1*da1 + w2*da2).        % a0 has defect 0
fof(PAp, axiom, PAp = w1*dap0 + w2*dap1).
% hypothesis: w1 > 0
fof(hyp_w1, axiom, w1 > 0).
% non-increase for this row
fof(goal, conjecture, PAp <= PA).
