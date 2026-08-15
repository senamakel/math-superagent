% Forward +1 branch with the ALLEGED single map x=2a+1.  Premise a - c*s = 1.
% Claim: (2a+1)^2 - d*a*s = 1.  EXPECT FAIL (algebra gives 8a+1).
fof(comm, axiom, ![X,Y]: (plus(X,Y) = plus(Y,X))).
fof(assoc, axiom, ![X,Y,Z]: (plus(plus(X,Y),Z) = plus(X,plus(Y,Z)))).
fof(zero, axiom, ![X]: (plus(X,zero) = X)).
fof(neg, axiom, ![X]: (plus(X,neg(X)) = zero)).
fof(sub, axiom, ![X,Y]: (minus(X,Y) = plus(X,neg(Y)))).
fof(mcomm, axiom, ![X,Y]: (mul(X,Y) = mul(Y,X))).
fof(dist, axiom, ![X,Y,Z]: (mul(X,plus(Y,Z)) = plus(mul(X,Y),mul(X,Z)))).
fof(one, axiom, ![X]: (mul(X,one) = X)).
fof(massoc, axiom, ![X,Y,Z]: (mul(mul(X,Y),Z) = mul(X,mul(Y,Z)))).
fof(premise_plus, axiom, minus(a, mul(c,s)) = one).
fof(def_two, axiom, two = plus(one,one)).
fof(def_four, axiom, four = plus(two,two)).
fof(def_d, axiom, d = mul(four, c)).
fof(goal, conjecture, minus(mul(plus(mul(two,a),one), plus(mul(two,a),one)), mul(mul(d,a),s)) = one).
