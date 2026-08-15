# Ramification (1-zeta_p)^{p-1} = p*u verified for odd primes p <= 97

The two scripts CONTEXT.md flagged as written-but-never-run
(`verify_ram_fast.py`, `verify_ramification.py`) are now executed, each with
captured output.

```claim
id: ramify-p-eq-prime-checked
statement: For every odd prime p <= 97, in Q(zeta_p) with P = (1-zeta_p),
  the ideal equality (p) = P^{p-1} holds: (1-zeta_p)^{p-1} = p*u for a
  cyclotomic unit u in Z[zeta_p], and N(1-zeta_p) = p.
hypotheses: p an odd prime, p <= 97 (finite exact check, not a proof).
holds-here: yes
status: checked
bearing: Foundational ramification of Q(zeta_p); underpins the cyclotomic
  ideal factorisation in the both-odd-primes descent.
falsifier: any p where the reduced remainder of (1-x)^{p-1} mod Phi_p has a
  coefficient not divisible by p.
anchor: code/out/verify_ram_fast.captured.txt
```
