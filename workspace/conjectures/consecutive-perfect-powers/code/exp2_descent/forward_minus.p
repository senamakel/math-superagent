% Forward direction, -1 branch.  a=r^q, s=s^q, c=2^{mq-2}, d=2^{mq}=4c.
% Premise (descent -1):  a + 1 = c*s.
% Claim: (2a+1)^2 - d*a*s = 1  with x=2a+1.
fof(comm, axiom, ![X,Y]: (plus(X,Y) = plus(Y,X))).
fof(assoc, axiom, ![X,Y,Z]: (plus(plus(X,Y),Z) = plus(X,plus(Y,Z)))).
fof(zero, axiom, ![X]: (plus(X,zero) = X)).
fof(neg, axiom, ![X]: (plus(X,neg(X)) = zero)).
fof(sub, axiom, ![X,Y]: (minus(X,Y) = plus(X,neg(Y)))).
fof(mcomm, axiom, ![X,Y]: (mul(X,Y) = mul(Y,X))).
fof(dist, axiom, ![X,Y,Z]: (mul(X,plus(Y,Z)) = plus(mul(X,Y),mul(X,Z)))).
fof(one, axiom, ![X]: (mul(X,one) = X)).
fof(massoc, axiom, ![X,Y,Z]: (mul(mul(X,Y),Z) = mul(X,mul(Y,Z)))).
% premise, -1 branch: a + 1 = c*s
fof(premise_minus, axiom, plus(a, one) = mul(c,s)).
% two = 2, four = 4, d = 4c
fof(def_two, axiom, two = plus(one,one)).
fof(def_four, axiom, four = plus(two,two)).
fof(def_d, axiom, d = mul(four, c)).
% goal: (2a+1)^2 - d*a*s = 1, x = plus(mul(two,a),one)
fof(goal, conjecture, minus(mul(plus(mul(two,a),one), plus(mul(two,a),one)), mul(mul(d,a),s)) = one).
