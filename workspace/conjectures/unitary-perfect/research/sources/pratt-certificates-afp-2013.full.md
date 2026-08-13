<!-- source: https://isa-afp.org/entries/Pratt_Certificate.html -->

# Pratt's Primality Certificates — Archive of Formal Proofs (Wimmer & Noschinski, 2013)

Web entry: https://isa-afp.org/entries/Pratt_Certificate.html
Formalisation: `Pratt_Certificate` theory in Isabelle/HOL's Archive of Formal
Proofs, by Simon Wimmer and Lars Noschinski (July 2013; bulk-certificate reading
added Nov 2024).

## What it establishes

A machine-checked formalisation of Pratt's (1975) primality-certificate proof
system: *p is prime iff a Pratt certificate for p exists*. It proves:

- **Soundness**: every predicate in a valid certificate holds — in particular
  `Prime(p)` appearing in a certificate means p is prime.
- **Completeness**: for every prime p there exists a certificate.
- **Succinctness**: a logarithmic (in p) upper bound on certificate size, so
  primality testing is in NP with SW via `build_fpc` (constructing a
  certificate for p from certificates for the primes dividing p−1).

## Why it matters for this run

This is **reference [17] of Maciejewski arXiv:2605.20475**, cited for the
paper's "Open Problem 5": a machine-checked reproduction of its Theorems 8–17
consists of (i) Pratt certificates for each 3-Higgs prime in `2^m + 1`, (ii)
certificates witnessing non-3-Higgs status (v₂ > 3 or a non-recursive
sub-prime), (iii) modular-exponentiation checks for BHV primitive-divisor
existence. The AFP entry shows exactly the reusable, previously-formalised
Pratt-certificate infrastructure for that program.

No mathematical bearing on the UPN conjecture itself; it is the formal-verification
infrastructure layer.

```claim
id: pratt-certificates-afp-sound-complete
statement: The Isabelle AFP Pratt_Certificate entry proves soundness,
  completeness, and logarithmic certificate-size bound for Pratt's (1975)
  primality-certificate proof system; a prime is prime iff it has a Pratt
  certificate, and certificates are built recursively from primes dividing p-1.
hypotheses: none beyond Pratt's constructive system
holds-here: applicable to the run's proposed Lean/Isabelle formalisation of
  Theorems 8-17 (Pratt certificates for 3-Higgs witnesses)
status: asserted by source; not re-derived here
bearing: supplies the reusable formalised Pratt-certificate machinery the
  Maciejewski paper names in its Open Problem 5 for machine-checking the
  Heven verification and the non-3-Higgs witnesses.
anchor: research/sources/pratt-certificates-afp-2013.full.md
answers: how-to-machine-check-the-3-higgs-verification
```
