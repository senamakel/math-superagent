% Consistency check: ring-identity axioms alone must be consistent.
% Ask whether zero = one follows.  Expect Satisfiable.
fof(comm, axiom, ![X,Y]: (plus(X,Y) = plus(Y,X))).
fof(assoc, axiom, ![X,Y,Z]: (plus(plus(X,Y),Z) = plus(X,plus(Y,Z)))).
fof(zero, axiom, ![X]: (plus(X,zero) = X)).
fof(neg, axiom, ![X]: (plus(X,neg(X)) = zero)).
fof(sub, axiom, ![X,Y]: (minus(X,Y) = plus(X,neg(Y)))).
fof(mcomm, axiom, ![X,Y]: (mul(X,Y) = mul(Y,X))).
fof(dist, axiom, ![X,Y,Z]: (mul(X,plus(Y,Z)) = plus(mul(X,Y),mul(X,Z)))).
fof(one, axiom, ![X]: (mul(X,one) = X)).
fof(massoc, axiom, ![X,Y,Z]: (mul(mul(X,Y),Z) = mul(X,mul(Y,Z)))).
fof(goal, conjecture, zero = one).
