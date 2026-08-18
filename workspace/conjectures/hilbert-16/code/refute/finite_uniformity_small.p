% Attack: pointwise finite cyclicity implies a uniform bound on a compact parameter family.
% This is the smallest abstract fragment; parameters are represented by a finite set.
fof(pointwise, axiom,
    ![X] : member(X, a) | member(X, b) -> finite_cycles(X)).
fof(compact_parameter_space, axiom,
    finite_set(a,b)).
fof(goal, conjecture,
    ?[N] : ![X] : member(X, a) | member(X, b) -> cycles_leq(X,N)).
