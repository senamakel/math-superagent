from sympy import symbols
x = symbols('x')
# f=(x-2)^19*(x-18/19): root 2 mult 19 covers derivatives 1..18;
# hypothesis: f^(19) root = 2 as well -> would score 19. TEST the conjecture door.
f = (x-2)**19 * (x - Rational(18,19))
