% Attack: the common informal extension of Collatz to n=0. The original
% conjecture is only over positive integers; this deliberately minimal FOL
% fragment tests the false universal claim that every integer reaches 1.
fof(step_even, axiom, ![N]: (even(N) -> step(N,half(N))).
fof(step_odd, axiom, ![N]: (odd(N) -> step(N,three(N))).
fof(zero_even, axiom, even(zero)).
fof(half_zero, axiom, half(zero)=zero).
fof(reaches_one, conjecture, ![N]: reaches(N,one)).
fof(zero_not_one, axiom, zero != one).
fof(zero_reaches_only_zero, axiom, reaches(zero,zero)).
fof(reaches_definition_fragment, axiom, ![N]: (reaches(N,one) -> N=one)).
