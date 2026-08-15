# Ramification (1-zeta_p)^{p-1} = p*u verified for all odd primes p <= 97

Executed the two scripts that CONTEXT.md's "UNRUN-script guard" flagged as
written-but-never-run. Both now have captured output.

```claim
id: ramify-p-eq-P-checked
statement: For every odd prime p <= 97, in Q(zeta_p) with P = (1-zeta_p),
  the ideal equality (p) = P^{p-1} holds, equivalently (1-zeta_p)^{p-1}
  = p*u for a cyclotomic unit u in Z[zeta_p], and N(1-zeta_p) = p.
hypotheses: p an odd prime, p <= 97 (finite exact check, not a proof).
holds-here: yes
status: checked
bearing: Foundational ramification of Q(zeta_p); underpins every cyclotomic
  step of the both-odd-primes descent.
falsifier: any p where the reduced remainder of (1-x)^{p-1} mod Phi_p has a
  coefficient not divisible by p.
anchor: code/out/verify_ram_fast.captured.txt
```

## Routes

`verify_ram_fast.py` reduces (1-x)^{p-1} modulo Phi_p by exact integer
polynomial division and checks every remainder coefficient is divisible by
p, so u has integer coefficients; norm argument then gives N(u)=1. Also
checks Phi_p(1) = p. PASS for all 24 odd primes <= 97.

`verify_ramification.py` uses lib.cyclo exact rational elements and true
resultant field norms: N(1-zeta)=p, N(u)=+-1, u integral, p/(1-z) integral.
PASS for p in {3,5,7,11,13,17,19,23,29,31,37}.

Two independent exact routes agree; the fast route covers all odd primes
through 97. Finite numeric check, not a proof — the general theorem is the
separate asserted-by-source claim zeta-p-ring-of-integers-and-ramification.

The known solution 3^2-2^3=1 engages this at p=3; the ramification geometry
holds there, so the lemma does not exclude the known solution.
