# p-adic witness falsification claim — mirrored from code/out/

The claim below is a computed fact from this run's own exact programs.
The evidence is in `code/out/witness_padic_closure_claim.md` and the captures
it references; this note exists because `research/CLAIMS.md` is derived from
notes under `research/` and claim blocks in `code/out/` alone are invisible
to it.

```claim
id: witness-padic-falsification
statement: For every prime power in the tested set (p=2 up to 32; p=3 up to
  243; p=5 up to 3125; p=7 up to 16807; p=11 up to 161051; p=13 up to 371293),
  every achievable residue set R of the universal set Phi = {f(m,n)} is
  additively closed: whenever r1, r2 in R then r1 + r2 is achievable mod that
  prime power (and mod 3, mod 5 the residue set collapses to the single class
  0). Hence no pure p-adic or modular obstruction proof of the Phi-no-triple
  conjecture exists at these moduli: such an argument would need an identity
  of residue sets that is never present. Both known 7-square witnesses satisfy
  all proved p-adic facts (v2>=3, v3>=1, residue 0 mod 3), so no residue/closure
  argument forbids either witness.
hypotheses: the run's exact Phi-membership test and residue-set construction,
  as implemented in witness_padic_falsification.py / phi_padic_closure_all.py;
  the specific primes p in {2,3,5,7,11,13,17,19,23} and the specific prime
  powers tabulated above.
holds-here: yes, on the tested moduli only
status: checked
bearing: rules out the pure modular-sieve line of attack at the tested primes
  and prime powers; deliberately NOT an unbounded statement — no conclusion is
  drawn about primes or prime powers outside the tested set.
anchor: code/out/witness_padic_closure_claim.md;
  code/out/witness_padic_falsification.py;
  code/out/phi_padic_closure_all.py;
  code/out/witness_padic_falsification.captured.txt;
  code/out/phi_padic_closure_all.captured.txt
source: operator-computation (this run)
```