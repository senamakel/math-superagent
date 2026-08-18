% Attack: the uniform-finiteness step for a parameter family.
% The weakened claim says pointwise finite counts imply one finite uniform bound.
% This is the smallest abstract fragment: a nonempty family with natural-valued
% finite counts, but no asserted compactness/algebraicity or bound.
fof(nonempty_family, axiom, exists(X, parameter(X))).
fof(pointwise_finite, axiom, ! [X] : (parameter(X) -> exists(N, (natural(N) & count(X,N))))).
fof(unbounded_parameter_counts, axiom, ! [N] : exists(X, (parameter(X) & count(X,N)))).
fof(uniform_bound, conjecture, exists(B, ! [X,N] : ((parameter(X) & count(X,N)) -> leq(N,B)))).
