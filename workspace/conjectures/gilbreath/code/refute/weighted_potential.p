% Refutation check for R-weighted-excess-potential.
% Defect d_i = max(0, A(i) - 2). The rung claims there exist weights w_i>=0,
% w_1>0 with P = sum w_i d_i non-increasing for ALL arrays.
%
% Counterexample array: parent interior (4,12,24,48,...), child interior
% (8,12,24,48,...). Child defect at position 1 = 6 > parent defect 2, and
% child defects at i>=2 equal parent's.
%
% Axiom: the concrete parent and child defects.
% Conjecture (attacked): position-1 defect does NOT strictly increase while
% all i>=2 do not decrease. A finite model falsifying this = find d'_1>d_1
% with d'_i>=d_i.
%
% We encode the parent interior values a2=4,a3=12,a4=24,a5=48 and child
% interior values from |a_i - a_{i+1}|: b2=8,b3=12,b4=24,b5=48.
fof(d1p, axiom, dp1 = 2).
fof(d2p, axiom, dp2 = 10).
fof(d3p, axiom, dp3 = 22).
fof(d4p, axiom, dp4 = 46).
fof(d1c, axiom, dc1 = 6).
fof(d2c, axiom, dc2 = 10).
fof(d3c, axiom, dc3 = 22).
fof(d4c, axiom, dc4 = 46).
% conjecture: the potential-increase configuration does NOT exist.
% (falsifying model = dc1 > dp1 and all i>=2 dc_i >= dp_i)
fof(goal, conjecture, ~( dc1 > dp1 & dc2 >= dp2 & dc3 >= dp3 & dc4 >= dp4 )).
