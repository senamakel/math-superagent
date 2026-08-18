% Attack: G4 claims a fixed-dimensional associative state with O(log k)
% composition computes the joint intercept second moment. The unrestricted
% algorithmic assertion is not first-order formalizable; encode its smallest
% concrete consequence: the proposed additive block summary must distinguish
% blocks whenever their one-symbol extensions can differ.
fof(binary, axiom, ![X] : (X = zero | X = one)).
fof(distinct_digits, axiom, zero != one).
fof(summary_collision, axiom, summary(block010) = summary(block101)).
fof(extension_difference, axiom, extend(block010,zero) != extend(block101,zero)).
fof(goal, conjecture, summary(block010) != summary(block101)).
