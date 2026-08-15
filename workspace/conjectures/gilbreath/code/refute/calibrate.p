% Calibration: trivially refutable. Two elements a,b. Axiom ~p(b).
% Conjecture: every element satisfies p. Model: p(a), ~p(b) falsifies it.
tff(dom, type, el: $i).
tff(decl, type, p: el > $o).
tff(decl, type, a: el).
tff(decl, type, b: el).
tff(a_neq_b, axiom, a != b).
tff(b_not_p, axiom, ~p(b)).
tff(conj, conjecture, ![X:el]: p(X)).
