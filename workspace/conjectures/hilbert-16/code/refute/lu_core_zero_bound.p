% Attack: the finite algebraic core of Lu's claimed H_14^3 result.
% Symbols represent the five chart parameters; axioms encode only the
% displayed degree-4 and degree-6 obstruction equations.
fof(l4_zero, axiom, l4 = 0).
fof(l6_zero, axiom, l6 = 0).
fof(l4_formula, axiom, l4 = (a*c + c*d + 2*d*f - e*f)/8).
fof(l6_formula, axiom, l6 = 1).
fof(goal, conjecture, l6 = 0).
