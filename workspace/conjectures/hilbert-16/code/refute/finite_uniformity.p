% Attack: pointwise finite cyclicity implies a uniform bound over parameters.
% This deliberately isolates the weakest potentially false bridge in G-uniform.
fof(pointwise, axiom,
    ![P] : $finite(P) ).
fof(goal, conjecture,
    ?[N] : ![P] : $cardinality(P,N) ).
