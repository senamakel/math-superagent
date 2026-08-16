# Ordinary vs Hasse derivatives in char p — the bad-prime convention

## Resolution (computed + sourced, 2026-03)

The published small-degree bad-prime lists are HASSE-derivative lists:

- n = 3: bad primes {2} — Castryck–Laterveer–Ounaïes 2012, Theorem 4
  ("p = 2 is the sole bad prime for degree d = 3")
  `research/sources/castryck2012_degree12_html.full.md` line 135.
- n = 4: bad primes {3,5,7} — De Jong–Draisma, quoted in the same paper,
  line 135 ("the bad primes for degree d = 4 are p = 3,5,7").

The definition of a CA polynomial in char p uses the i-th Hasse derivative
H_i(f) = sum_j C(j,i) c_j x^(j-i) — Schaub–Spivakovsky 2024, Definition 1.1
and the arXiv abstract (`research/sources/schaub_spivakovsky_bad-primes_2024.full.md`,
line 1 "having a common factor with each of its derivatives Hi(f)"; the 2023
note line 1: "Hi(f) is the i-th Hasse derivative"; castryck2012 §1.7 line 135
"CA-polynomials of degree d in characteristic p").

The ordinary i-th derivative f^(i) satisfies f^(i) = i! · H_i(f), and i! = 0
in F_p for i >= p, so over F_p the ordinary hypothesis degenerates: for
n > p the equations f^(i)(r_i) = 0 with i >= p become 0 = 0, so e.g.
x^4 + x^2 over F_2 has every ordinary derivative zero and satisfies the
ordinary hypothesis vacuously (is_ca True, is_pure_power False) while
H_2(x^4+x^2) = 1 is a nonzero constant, so it FAILS the Hasse hypothesis.
The ordinary and Hasse formulations agree in characteristic 0 and for p >= n;
they differ exactly when p < n.

## Computed facts (code/badprimes, all exact over GF(p))

Hasse scheme rad(I_n) = rad(P_n) (direction1 P_n ⊆ rad(I_n) by Rabinowitsch,
direction2 automatic) over all 17 primes p < 60:

- n = 3: CA FAILS (bad) only at p = 2; holds at p = 3,5,7,11,13,17,19,23,
  29,31,37,41,43,47,53,59.  [matches published {2}]
- n = 4: CA FAILS (bad) at p = 3,5,7; holds at p = 2 and at all p in
  11..59.  [matches published {3,5,7}]

Second route (bounded oracle, lib.casas_alvero.is_ca_hasse, all monic polys
over F_p, p in {2,3,5,7} <= 2401 polys): Hasse counterexample counts
n=3: {2:2, 3:0, 5:0, 7:0};  n=4: {2:0, 3:6, 5:20, 7:42}.  Agrees with the
scheme verdicts and with the published lists exactly.

Contrast (ordinary scheme): n=3 bad {2} (agrees — p = 2 < n=3 degeneracy);
n=4 bad {2,3,5,7} (p=2 wrongly bad: vacuous ordinary hypothesis).
The ordinary list {2,3,5,7} for n=4 must NOT be quoted as the published list.

## Ripple re-checks (all done)

- Oracle guards: all PASS after adding is_ca_hasse (code/out/oracle_guard.captured.txt).
- Ghosh break verification: uses lib.ghosh2025 (Hasse–Schmidt multivariate
  derivation of eq (2.1)) + is_ca/is_pure_power on the degree-(p+1) witness;
  all 1313 checks still PASS; the witness satisfies BOTH ordinary and Hasse
  hypotheses; the Φ^#/HD break step is characteristic-independent, so the
  ordinary-vs-Hasse distinction does not touch it.
- Refuter TPTP encoding (code/refute/ca_deg3_char2.p, code/out/refute_char2.md):
  degree 3, p = 2 — ordinary and Hasse coincide there (p = n, and for i < p
  ordinary == Hasse up to nonzero unit); verdict unchanged (CHAR-P FALSE).

## Files

- code/badprimes/verify_badprimes_sn.py — the S_n-scheme verification
- code/out/badprimes_sn.captured.txt — capture, exit 0, ALL CHECKS PASSED
- code/lib/casas_alvero.py is_ca_hasse — Hasse hypothesis oracle
- code/lib/casasalvero.py hasse_sn_equations — Hasse S_n scheme

## Claims

```claim
id: bad-prime-lists-hasse-formulation
statement: The published small-degree bad-prime lists are for the HASSE
  formulation of the CA hypothesis (H_i(f) Hasse derivatives): n=3 bad primes
  {2} (Castryck et al. 2012, Thm 4, line 135 of the held source) and n=4 bad
  primes {3,5,7} (De Jong-Draisma, quoted there).  The ordinary-derivative
  hypothesis f^(i) = i! H_i(f) degenerates in char p for i >= p (i! = 0), so
  the ordinary S_n scheme marks p=2 bad for n=4 (x^4+x^2 over F_2: every
  ordinary derivative zero, hypothesis holds vacuously) while the Hasse scheme
  marks p=2 good (H_2 = 1, nonzero constant).  The two formulations agree in
  characteristic 0 and for p >= n.
hypotheses: characteristic p prime, degree n in {3,4}, published lists of
  Castryck et al. 2012 / De Jong-Draisma
holds-here: yes — this is exactly the bad-prime verification target of the
  run's second route
status: checked — reproduced by code/badprimes/verify_badprimes_sn.py over
  GF(p) for all 17 primes p < 60 and by bounded F_p enumeration via
  lib.casas_alvero.is_ca_hasse (p in {2,3,5,7}); capture code/out/badprimes_sn.captured.txt
bearing: any char-p claim made with the ordinary-derivative oracle must state
  that it is the ordinary notion; the published bad-prime lists are Hasse
anchor: research/notes/ordinary-vs-hasse-badprimes.md
falsifies: if a held source listed p=2 as bad for degree 4 under its own
  Hasse definition, the claim would be wrong
```
