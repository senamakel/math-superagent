% Attack: finite cyclicity of the full quadratic DRR graphic I^1_6b.
% Small fragment: abstractly encode the claimed uniform finite bound for a
% nonempty parameter family; this intentionally tests whether the hypotheses
% as written force a bound without an analytic/uniformity axiom.
fof(nonempty_family, axiom, exists(x, parameter(x))).
fof(unbounded_counts, axiom, ! [X] : (parameter(X) -> exists(Y, count(X,Y)))).
fof(counts_are_natural, axiom, ! [X,Y] : (count(X,Y) -> natural(Y))).
fof(goal, conjecture, exists(B, ! [X,Y] : ((parameter(X) & count(X,Y)) -> leq(Y,B)))).
