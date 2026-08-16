# Summary — Frequencies of Successive Pairs of Prime Residues

Source: A. Ash, L. Beltis, R. Gross, W. Sinnott, *Experiment. Math.* 20(4) (2011)
400–411. Source URL: http://fmwww.bc.edu/gross/ABGS.pdf. Full text:
`[[ash_beltis_gross_sinnott_prime_residues.full]]`.

## What this establishes

This is the parity-barrier source: the reduction of SUPPLY to mod-4 switch density
sits on its §9. It studies `N(a,d,m,x)` = # consecutive prime pairs `p<q`, `p<x`,
`p ≡ a`, `q ≡ a+d (mod m)`.

**The load-bearing statement (verbatim, §1, p.401):** *"To the best of our
knowledge, Problem 1.1 is wide open, and cannot be treated using L-functions,
unlike the case of Dirichlet's theorem."* Problem 1.1 is the asymptotics of
`N(a,d,m,x)`. So even the *frequency* of the differing-residue pairs SUPPLY needs
(positive mod-4 switch density) is unknown, and unconditionally inaccessible by
the standard L-function toolkit. This is the named open problem behind the parity
barrier.

**Proved symmetries of their *heuristic* formula** `P_J(a,d,m,x)` (the truncated
Pólya inclusion-exclusion "probability"):

- **Prop 4.1**: for `m = 2^k` a power of 2, `P_J(a,d,2^k,x)` is independent of `a`
  (odd `a`). Proof: if `S` contains any odd element then `α(S)=0`; if `S` has only
  even elements then `a+S` is all-odd, coprime to `m` regardless of `a`. This is a
  *heuristic* symmetry, not a theorem about actual counts.
- **Prop 4.2** (antidiagonal symmetry): `P_J(a,d,m,x) = P_J(−a−d, d, m, x)`.
- **Prop 4.3 / Cor 4.4** (vertical compatibility): if `m|n` then `P_J(a,d,m,x)` is
  a sum of the finer-modulus `P_{J'}(a',d',n,x)`.

It is **not** known whether the true ratio `N(a,d,m,x)/N(a',d',m,x)` tends to 1
(§9 open question). The heuristic's n(S)=2 terms diverge, so `lim_{J→∞} P_J` is
not known to exist — the "probability" is not an actual probability distribution.

**Measured mod-4 data (§7, x = 10^3..10^6)**, counts of consecutive-prime-pair
classes:
```
(1,1)=16574  (1,3)=22521
(3,1)=22520  (3,3)=16715
```
total = 78330. Switch pairs (1,3)+(3,1) = 45041 = 57.5%; equal (1,1)+(3,3) =
33289 = 42.5%. Switch/equal ≈ 1.353. Largest/smallest ratio = 22521/16574 ≈ 1.359.
The equal (diagonal) classes are measured *fewer* than the switch ones — the same
"diagonal bias" Lemke–Oliver–Soundararajan explain. The claimed numbers previously
recorded in the ledger ("16574/16715 range") were garbled; the correct asymmetry
is off-diagonal vs diagonal at ratio ≈1.36.

## What it implies here

Problem 1.1's openness is exactly why the reduction (`ν₂ ≥ c·n` ⟺ positive mod-4
switch density) is a dead end: the required arithmetic input is itself unnamed
open problem, not provable by L-functions. This is the entire justification for
attacking SUPPLY via the fold `Φ` directly, at the cost of closing doors
1–4 (the fold has low-weight images on rich inputs). The power-of-2 independence
(Prop 4.1) is consistent with why the mod-4 *pair* structure (not the single-residue
structure, which mod 4 is equidistributed by Dirichlet) is the delicate object.

## Not settled

It does *not* prove that positive switch density is equivalent to SUPPLY; that
equivalence is the run's own open question (GOAL priority 3), not something this
source states. It only establishes that switch density itself is unproved and
L-function-inaccessible.

```claim
id: abgs-p1-wide-open
statement: The asymptotic frequency of consecutive-prime pairs in a given ordered residue
  class (a, a+d) mod m — the asymptotics of N(a,d,m,x) — is an open problem that cannot
  be treated using L-functions, unlike Dirichlet's theorem for single primes.
hypotheses: m,a,d with (a,m)=(a+d,m)=1; Problem 1.1.
holds-here: yes — this is exactly the arithmetic input behind the switch-density reduction.
status: asserted (source's own assessment, p. 401)
bearing: the reduction of SUPPLY to switch density reduces it to an L-function-inaccessible
  open problem; motivates attacking the fold directly.
anchor: ash_beltis_gross_sinnott_prime_residues.full, §1 p.401
```

```claim
id: abgs-mod4-nonuniform-measured
statement: For m=4 over x=10^3..10^6 the consecutive-pair classes are measured
  non-uniform: switch pairs (1,3),(3,1) total 45041 (57.5%) vs equal (1,1),(3,3) 33289
  (42.5%); largest/smallest class ratio ≈ 1.359. Equal classes are measured fewer.
hypotheses: primes > 10^3, pairs ≤ q with p < 10^6.
holds-here: yes (raw measured count, finite range only).
status: asserted-by-source (measured, finite x; not a limiting statement)
bearing: numerical indication that switch density is positive (~0.575) in this range,
  consistent with measured ν₂/n ≈ 0.49; but no asymptotic theorem.
anchor: ash_beltis_gross_sinnott_prime_residues.full, §7 m=4 table
```

```claim
id: abgs-pair-frequency-equality-open
statement: Whether the ordered residue-pair classes of consecutive primes mod m occur
  asymptotically equally often — N(a,d,m,x)/N(a',d',m,x) → 1 for every permissible pair of
  classes — is open (§9).
hypotheses: m,a,d,a',d' with the residues coprime to m.
holds-here: yes.
status: asserted (source's §9 open question)
bearing: positive switch density is equivalent to a *non*-degenerate part of this; since
  even equality is open, positivity is also open — the parity barrier.
anchor: ash_beltis_gross_sinnott_prime_residues.full, §9
```
