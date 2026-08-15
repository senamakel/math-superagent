tff(domain, type, thing: $tType).
tff(decl_p, type, p: thing > $o).
tff(decl_a, type, a: thing).
tff(decl_b, type, b: thing).
tff(distinct, axiom, a != b).
tff(p_at_a, axiom, p(a)).
tff(p_at_b, axiom, ~ p(b)).
% p not constant true -> the conjecture "p is true everywhere" is refutable
tff(goal, conjecture, p(a)).
