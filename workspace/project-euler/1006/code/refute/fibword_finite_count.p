% Attack: the finite-word assertion that S_4 already has k+1 factors
% for every positive k. This is deliberately the smallest finite fragment.
fof(k_positive, axiom, k >= 1).
fof(s4_length, axiom, length = 8).
fof(finite_count_claim, conjecture, count = k + 1).
