% Attack: naive closure of four second-type Dulac passage ECT systems.
% The exact dynamical claim is not first-order formalizable here; this is the
% smallest algebraic fragment: each pair has nonzero Wronskian, but their sum
% need not. The conjecture therefore encodes that implication.
fof(pair1_ect, axiom, wronskian(pair1, nonzero)).
fof(pair2_ect, axiom, wronskian(pair2, nonzero)).
fof(sum_ect, conjecture, wronskian(sum_pair, nonzero)).
