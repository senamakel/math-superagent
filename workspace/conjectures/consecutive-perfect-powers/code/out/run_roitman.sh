# Roitman primary-claim corroboration — no new run needed

The exact mechanism Roitman asserts (a primitive divisor r of Phi_p(x) has
ord_r(x)=p, hence r ≡ 1 mod p) is ALREADY verified in-workspace by the checked
claim `prim-div-lucas-verified` (odd primes p in {3,...,23}, x in [2,Xmax_p],
0 failures) and the direct multiplicative-order cross-check in
code/out/primitive_div_crosscheck.captured.txt (102 (p,x) cases, all
ord(x mod r)=p PASS). So the Roitman source CORROBORATES existing checked
computation; a further script here would be a redundant third copy and is
withheld. See the durable memory stored this run.

Scope (from mirror-prim-div-scope): the primitive-divisor engine supplies
r ≡ 1 mod p with r | y — a necessary, not sufficient, condition; it does NOT
give Cassels' p | y. 1967 non-solutions satisfy all elementary conditions.
Not run (nothing new to settle).
