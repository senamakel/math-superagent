fof(one_plus_one, axiom, plus(one, one, two)).
fof(even_def, axiom, ! [N] : (even(N) <-> exists K : (plus(K,K,N)))).
fof(prime_def, axiom, ! [P] : (prime(P) -> (exists A : (plus(A, one, P)) & forall D : (divisor(D,P) -> (D = one | D = P)))))).
fof(goldbach_conj, conjecture, ! [N] : (even(N) -> (N = two | N = four | exists P : (prime(P) & exists Q : (prime(Q) & plus(P,Q,N)))))).
