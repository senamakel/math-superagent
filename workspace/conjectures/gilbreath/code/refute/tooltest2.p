% Test that the engine can find a finite model at all.
% Domain: {0,1}. Predicate p: true at 0, false at 1.
fof(domain, axiom, ![X]: (X=0 | X=1)).
fof(p0, axiom, p(0)).
fof(p1, axiom, ~p(1)).
% Claim: p is true for all domain elements.
fof(goal, conjecture, ![X]: p(X)).
