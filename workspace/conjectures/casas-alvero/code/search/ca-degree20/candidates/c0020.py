from sympy import symbols
x = symbols('x')
# f^(19) = 20!x + 19!*a_1, root r = -a_1/20.
# Set a_1 = -20 so r = 1, and force f(1)=0 via other coeffs; share j=19.
# Then also want 1..18 sharing: put root 1 mult 2 (covers j=1), and arrange
# coeffs so f^(2..18)(1)=0 too via multiplicity -> need mult 19. But then j=19
# root must be the same 1. Try: f=(x-1)^19*(x-1)=trivial. Non-trivial attempt.
# Instead: root 1 mult 18 (covers 1..17), r=1 line for j=19, plus make f^(18) share.
f = (x-1)**18 * (x+2)*(x+3)
