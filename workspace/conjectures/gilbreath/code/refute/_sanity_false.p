% Sanity test that the falsifier works: claim that ALL integers are equal.
% Obviously false (0 != 1), so a size-2 model falsifies it.
tff(dom, type, elem: $i).
tff(decl, type, p: (elem * elem) > $o).
tff(eq0, axiom, p(a, b)).
tff(eq_ab, axiom, p(c, d)).
% conjecture: p is universal (always true) --- false on a 2-element domain.
fof(goal, conjecture, ![X:elem, Y:elem]: p(X, Y)).
