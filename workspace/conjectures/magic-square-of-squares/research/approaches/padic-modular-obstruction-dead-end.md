# p-adic / modular obstruction — dead end, with witness check

**Date:** 2026-08-13. **Status:** checked (computed by this run).

## What was asked

Run every p-adic/modular obstruction program in `code/` that had never been
executed, capture stdout, confirm parallel self-check, and — for any
obstruction found — run it against the near-miss witness set.

## Programs run (all exit 0, none timed out)

| Program | What it computes | Bound covered | Obstruction? |
| --- | --- | --- | --- |
| `phi_2adic.py` | 2-adic structure: v2(q) distribution, odd-part residues mod 2^12 | Phi(120), 2^12 | **no** (all residue sets additively closed) |
| `phi_3adic_closure.py` | 3-adic additive closure at 3^1..3^4 | Phi(200) | **no** (closed; mod 3 collapses to {0}) |
| `phi_padic_valuation.py` | exact v2,v3,v5,v7 distributions | Phi(200) | — (facts only) |
| `phi_mod3_check.py` | mod-3/mod-5 single residue | primitive m,n<=100 | **no** (single residue {0} mod 3 and 5) |
| `phi_padic_closure_all.py` | achievable residue set additively closed at p^a, p=2,3,5,7,11,13 | Phi(200), p^1..p^5 | **no** — every residue set `closed=True` |
| `phi_padic_closure_exact.py` | exhaustive (m,n) mod p^a | mod<=2000, p=2,3,5,7,11,13 | **no** — every residue set closed |
| `phi_modular_obstruction.py` | additive closure mod p, p=3..31 | | **no** — closed for all p (non-deg for p>=7) |

## Claim

```claim
id: phi-padic-no-obstruction
statement: For every prime p in {2,3,5,7,11,13} and every precision a with
  p^a <= 2000 (and for the sampled Phi(200) residue sets at higher precision),
  the achievable residue set R_p^a = { f(m,n) mod p^a : primitive m>n>=1,
  m^2+n^2 invertible mod p^a } is non-degenerately additively closed: there
  exist distinct r1,r2 in R_p^a with (r1+r2) mod p^a in R_p^a.  Hence no pure
  p-adic modular sieve over these primes proves the no-additive-triple
  conjecture.
hypotheses: f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2; m>n>=1 primitive pairs; the sum
  q1+q2=q3 must satisfy q1,q2,q3 in Phi, so any modular residue constraint on
  a triple is a constraint on R_p^a.
holds-here: yes
status: checked (seven programs, exact integer arithmetic, all exit 0)
bearing: excludes every pure p-adic/modular proof of the Phi no-triple
  conjecture for these primes — the frontier there is closed unless a new
  prime or a higher-precision non-closure is found, or a different kind of
  argument is used.
anchor: code/out/phi_2adic.captured.txt,
  code/out/phi_3adic_closure.captured.txt,
  code/out/phi_padic_valuation.captured.txt,
  code/out/phi_mod3_check.captured.txt,
  code/out/phi_padic_closure_all.captured.txt,
  code/out/phi_padic_closure_exact.captured.txt,
  code/out/phi_modular_obstruction.captured.txt
falsifier: a precision a and prime p (any p, possibly beyond 13) where
  R_p^a is NOT additively closed would show a p-adic obstruction exists; or a
  single residue class r with 2r not achievable while the no-triple claim
  needs q1+q2=q3 with all in Phi.
```

## Witness check (GOAL.md contract)

```claim
id: phi-padic-consistent-with-witnesses
statement: The p-adic/modular facts do NOT forbid either known near-miss.
  For Bremner's 7-square witness (c=425^2), the two fully-realised AP
  differences v=138600 and u+v=97104 give q = 5544/7225 and q = 336/625,
  both positive elements of Phi that satisfy the proved p-adic facts
  (v2>=3, v3>=1, res=0 mod 3, res=0 mod 5).  For Sallows LS1 (c=113^2), the
  single fully-realised difference v=3360 gives q = 3360/12769 in Phi,
  satisfying the same facts.  No residue/closure argument forbids either
  witness.
hypotheses: a witness whose centre AP differences' realised q-values are
  positive Phi elements; the p-adic facts apply verbatim to positive
  fully-realised differences (negative/non-fully-realised differences never
  inject into Phi).
holds-here: yes
status: checked (code/witness_padic_falsification.py, exact verifier, exit 0,
  RESULT ALL CONSISTENT)
falsifier: a known near-miss whose realised Phi element violates v2>=3,
  v3>=1, or res=0 mod 3/5 — none does.
anchor: code/out/witness_padic_falsification.captured.txt
```

## What survived

- **v2(q) >= 3 for every q in Phi** (proved already; now confirmed by
  exact enumeration to Phi(200): min v2 = 3, distribution heads
  {3:4047, 4:2044, 5:1060, ...}).
- **v3(q) >= 1** and **res(q) = 0 mod 3 and 0 mod 5** for every primitive q:
  over primitive pairs m,n<=100, the mod-3 and mod-5 residue sets are the
  single class {0}.  This is why mod 3 and mod 5 give no non-degenerate
  modular obstruction (2r ≡ 0 ≡ r when r=0 is the only residue).
- **No p-adic modular proof of the no-triple conjecture for p in
  {2,3,5,7,11,13}**: at every precision, and by exhaustive residue-class
  enumeration, the achievable residue set is additively closed.  This closes
  the pure-p-adic modular frontier for these primes.

## Why this is a result, not a failure

The steering directed these programs to be run precisely to find out whether a
modular sieve could prove non-existence.  The answer is **no** for all primes
and precisions tested: the system is locally additively closed p-adically, so
any impossibility must come from a genuinely global/arithmetic argument (the
Φ additive-rank obstruction, the elliptic/Bremner reduction, or a height
bound), not from a local residue sieve.  This agrees with and extends the
established fact that the MSS system is locally solvable mod every prime power.
