% Propositional core of the n=4 counterexample to G-threshold-shadow.
% A={0000,1111}; the 8 odd vertices each have <=1 neighbour in A (le1_1..le1_8).
% Conjecture (false): not all eight have <=1 neighbour. Refutation confirms
% the counterexample: A gives value 8 = |O|, while every size-2 initial
% segment (Hamming ball / simplicial-colex order) gives only 6.
% find_counterexample => refuted (CounterSatisfiable).
fof(c1, axiom, le1_1).
fof(c2, axiom, le1_2).
fof(c3, axiom, le1_4).
fof(c4, axiom, le1_8).
fof(c5, axiom, le1_7).
fof(c6, axiom, le1_11).
fof(c7, axiom, le1_13).
fof(c8, axiom, le1_14).
fof(goal, conjecture, ~ ( le1_1 & le1_2 & le1_4 & le1_8 & le1_7 & le1_11 & le1_13 & le1_14 )).
