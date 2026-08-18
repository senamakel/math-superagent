% Attack: the weakest plausible inference used in G-transition/G-zeros:
% finite asymptotic data plus flat remainder implies finitely many zeros.
% This is deliberately the smallest first-order fragment; it is schematic,
% not a faithful encoding of a quadratic vector field.
fof(flat_remainder_axiom, axiom,
    ! [X] : (positive(X) -> (remainder(X) = exp_neg(X) * sine(inv(X))))).
fof(finite_zeros_conjecture, conjecture,
    ? [N] : ! [X] : (positive(X) & X < one ->
      (zero(remainder(X)) -> X = inv(pi * N)))).
