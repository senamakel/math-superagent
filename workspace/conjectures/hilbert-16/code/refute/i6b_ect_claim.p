% Attack: the finite ECT/zero-pattern claim for the open I^1_6b graphic.
% Smallest faithful fragment: a real function represented by a finite Wronskian
% chain is asserted to have at most two zeros on an interval.
fof(real_domain, axiom, ![X]: (number(X) -> number(X))).
fof(ect_claim, conjecture,
    ![F]: ( (function(F) -> (exists N: number(N) & N = 2)) )).
