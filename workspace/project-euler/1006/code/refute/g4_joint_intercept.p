% Small finite abstraction of the claimed G4 aggregation.
% Domain elements are intercept indices m; v is the decimal value.
fof(value_def, axiom, ![M,V] : (value(M,V) -> integer(V))).
fof(distinct_indices, axiom, ![M,N] : (M != N -> intercept(M) & intercept(N))).
fof(j_claim, conjecture, ![K] : (positive(K) -> exists(J, aggregate(K,J)))).
