Solve by algebraic number theory, with an exact-integer oracle underneath every
claim. The elementary cases (one exponent equal to 2) are closed by
factorisation in Z and Z[i] and must be redone here first; the open content is
both exponents odd prime, where the equation forces an ideal factorisation in
the cyclotomic ring Z[zeta_p] and the obstruction is the class group.

The oracle for this problem is a bounded exact search returning every solution
of x^p - y^q = 1 below a stated bound — which must return exactly (3,2,2,3) —
together with a direct evaluator for the necessary divisibility conditions on a
hypothetical solution, calibrated so that the known solution satisfies them.

Every lemma is evaluated at 3^2 - 2^3 = 1 before it is believed. The conjecture
asserts that no second solution exists, so a lemma implying no solution exists
at all is refuted, not weakened. Use symbolic_math for the cyclotomic
arithmetic rather than doing it in prose.
