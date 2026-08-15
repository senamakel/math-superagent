% Trivial test: find a model of p(0)&p(1)&p(2) falsifying p(3).
% Domain is just {0,1,2,3} via explicit atoms.
fof(a1, axiom, p(0)).
fof(a2, axiom, p(1)).
fof(a3, axiom, p(2)).
fof(a4, axiom, ~p(3)).
fof(goal, conjecture, p(3)).
