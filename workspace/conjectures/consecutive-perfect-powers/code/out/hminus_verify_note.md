# Minus class number formula — verified by two independent routes

## Claim (closed)

For K = Q(zeta_p), p an odd prime, the relative (minus) class number is

    h^-(K) = 2p * prod_{chi odd mod p} (-1/2 * B_{1,chi})

with B_{1,chi} = (1/p) * sum_{a=1}^{p-1} chi(a) * a for non-trivial odd chi.
(Source: Washington's Introduction to Cyclotomic Fields; claim
`minus-class-number-formula` in research/CLAIMS.md was previously `unchecked`.)

```claim
id: minus-class-number-formula
statement: |
  For K = Q(zeta_p), p an odd prime, h^-(K) = 2p * prod_{chi odd mod p}
  (-1/2 * B_{1,chi}), B_{1,chi} = (1/p) sum_{a=1}^{p-1} chi(a) a,
  B_{1,1} = -1/2.
hypotheses: p an odd prime; chi runs over odd Dirichlet characters mod p (with trivial char giving B_{1,1}=-1/2).
holds-here: yes — this is the class-number formula used in the cyclotomic setting of x^p-y^q=1.
status: checked
bearing: h^- controls the minus part of the class group, the obstruction in both-odd-prime case.
anchor: code/out/hminus_exact.captured.txt, code/out/verify_claims.captured.txt
verification: exact rational computation over Q(zeta_p) reproduces OEIS A000927
  for all 24 odd primes p <= 97 (code/hminus_full.py -> code/out/hminus_full100.captured.txt);
  the two float routes (verify_claims.py, hminus_exact.py) formerly cited as
  "two independent routes" evaluate the same product and are NOT independent —
  the exact exhaustive run is the source of the checked status.

```

## CORRECTION (scholar 2025): "two independent routes" was overstated

The claim block below says "verified by two independent routes":
1. `code/out/verify_claims.py` — sympy `exp(I*2*pi*k*e/p)` then
   `N(re(h_rel),12)` (FLOAT rounding of a sympy complex expression).
2. `code/out/hminus_exact.py` — mpmath float.

An adversarial review on the board was right that these two are NOT
independent: both evaluate the SAME Bernoulli product ∏(−½B_{1,χ}) in
floating point and compare to the SAME hardcoded table {3:1,...,43:211}.
That is one implementation, numerically checked against a table, not two
independent derivations, and neither is "exact rational arithmetic".

The formula IS nevertheless genuinely established numerically, by a third,
exact route the claim did not cite: `code/hminus_full.py` (via
`code/lib/cyclo.py`, exact sympy.Rational arithmetic over Q(ζ_p), no floats)
reproduces OEIS A000927 EXHAUSTIVELY for all 24 odd primes p ≤ 97,
consecutive and without reading the catalogue
(`code/out/hminus_full100.captured.txt`). That is the source of record for
`status: checked`, not the two float routes. The catalogued exact values
(p=23→3, 29→8, 37→37, 41→121, 43→211, 47→695, … 97→411322824001) also expose
the Washington 1st-edition errata (p=59, 97). Keep `minus-class-number-formula`
as `checked` but with `verification` anchored to `hminus_full100.captured.txt`,
and treat the two float programs as a single non-independent check.

## Bug found and fixed

Both programs' `primitive_root` first versions tested only the r=2 condition
`pow(g,(p-1)//2,p) != 1`, returning a quadratic-nonresidue that is NOT a
primitive root when p-1 has more prime divisors. It silently crashed at p=43
(KeyError). Fixed to require `g^((p-1)/r) != 1` for every prime divisor r of
p-1. This is a genuine correctness bug the attempted run would have hit — worth
recording because any later primitive-root use needs the full test, and the
original would have produced wrong answers for p with composite p-1.
