# Dr(q) = F_q and the corrected mixed-modulus sieve — claim

Program: `code/erdos/dr_surjectivity.py`, capture: `code/out/dr_surjectivity.captured.txt`,
EXIT_CODE=0, elapsed 4.93 s.

```claim
id: DR-SURJECTIVITY-ALL-Q
statement: For every q >= 2 with gcd(3, q) = 1, Dr(q) := { s mod q : s is a
  digit-{0,1} ternary integer } equals all of F_q.  Proof (exhibited and
  verified by construction in the program): with m = ord_q(3), the powers
  3^0, 3^m, 3^(2m), ... are distinct powers of 3 each ≡ 1 (mod q), so
  S_t = sum_{j<t} 3^(j*m) is digit-{0,1} (distinct powers never carry) and
  S_t ≡ t (mod q); t = 0..q-1 covers every residue.  The theorem is
  unconditional (a proof, not a numerical check); the program additionally
  verifies it by construction for all 199 moduli q in [5,300] with 3∤q plus
  257, 641, 1021, for every residue t.
hypotheses: gcd(3, q) = 1, q >= 2.  These hold for every mixed modulus
  M' coprime to 6 in the cross-modulus route.
holds-here: yes — every mixed modulus in the adopted ladder has M' coprime
  to 6, hence to 3.
status: proved (with exhaustive-by-construction verification over the stated
  finite grid, 199 moduli × all residues).
bearing: makes the corrected mod-q consistency (b') of the mixed-modulus
  sieve VACUOUS: for a survivor r with 2^r = L_r + 3^k s, the required
  residue of the digit-free high part s exists for every r, so no mixed
  modulus kills any survivor class.
anchor: code/erdos/dr_surjectivity.py, code/out/dr_surjectivity.captured.txt
```

```claim
id: CROSS-MODULUS-H1-REFUTED
statement: Hypothesis H1 of CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES (a mixed
  modulus M = 2^u 3^v M' whose cross-orders force the survivor count strictly
  below 2^(k-1)) is refuted as a counting mechanism at the mod-q consistency
  level: because Dr(q) = F_q for every q coprime to 3 (DR-SURJECTIVITY-ALL-Q),
  the mod-q consistency (b') never eliminates a survivor class.  On the grid
  q in {5,7,11,13,17,19,29,41,193,257}, k in 1..9, capped at
  lcm(2*3^(k-1), ord_q(2)) <= 3e5 (90 pairs), the corrected mixed sieve gives
  mixed_count == pure == 2^(k-1) for every (q,k).
hypotheses: H1 as stated in the claim; the route's later steps (H2, the
  k+1-term generalisation of Lemma 3.1) are untouched by this refutation.
holds-here: yes.
status: checked (all 90 (q,k) pairs machine-verified by the program,
  resting on the unconditional theorem DR-SURJECTIVITY-ALL-Q for the vacuity;
  evidence class: verified-numerically + proved vacuity).
bearing: the pure 3-adic sieve's |A_k| = 2^(k-1) is not beaten by any
  modulus coprime to 3; the cross-modulus route must find its leverage
  elsewhere (e.g. H2's k+1-term structure, or the 2^u 3^v part of M).
anchor: code/erdos/dr_surjectivity.py, code/out/dr_surjectivity.captured.txt
```

## What the program established (all exact integer arithmetic)

- Oracle reproduction: `digit_free(2^0)=True (1_3)`, `digit_free(2^2)=True (11_3)`,
  `digit_free(2^8)=True (100111_3)`, `digit_free(2^5)=False (1012_3)` — PASS.
- Surjectivity: all 199 moduli, every residue — PASS (ord_q(3) sample rows:
  q=19 → 18, q=257 → 256, q=641 → 640, q=1021 → 34).
- Mixed sieve: pure == mixed == 2^(k-1) on all 90 (q,k) pairs; brute-force
  oracle agrees with the lifting sieve for k = 1,2,3.
- 2^n is never materialised; all work mod 3^k, exact.

## Status vs the run's ledgers

The prior probes `cross_modulus_sieve.py` (uncorrected condition (b), which
killed classes only at q=19) and `cross_modulus_corrected.py` /
`cross_modulus_coverage_general.py` (Dr(q)=F_q for a limited list of q) are
superseded by the unconditional theorem and the full-grid verification here.
