fof(axiom1, axiom, ! [N] : (even(N) => (even(N) <-> exists P : (prime(P) & exists Q : (prime(Q) & plus(P, Q, N)))))).
fof(axiom2, axiom, ! [N] : (even(N) => (even(N) = even(N)))).
fof(goal, conjecture, ! [N] : (even(N) => (N < 3 | (N = 4) | (N = 6) | exists P : (prime(P) & exists Q : (prime(Q) & plus(P, Q, N)))))).
