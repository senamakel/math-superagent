fof(remainders_small, axiom,
  ! [H1,H2] : ( ! [X] : (0 < X & X < 1 => abs(H1(X)) < 1/10 & abs(H2(X)) < 1/10) )).
fof(monomials, axiom,
  ! [X] : (0 < X & X < 1 => (X = X))).
fof(goal, conjecture,
  ! [H1,H2] : ( ! [X] : (0 < X & X < 1 => abs(H1(X)) < 1/10 & abs(H2(X)) < 1/10) )
    => ! [Z] : (Z = 1)).
