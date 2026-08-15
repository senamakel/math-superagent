# h^-(Q(zeta_p)) — independent PARI/GP cross-check (bnfinit route)

**This is a numeric cross-check, not a proof.** The route differs genuinely from
the Bernoulli-product formula that the workspace's previous attempts used.

## Why this is a DIFFERENT route

The existing `code/hminus_full.py` computes h^- by the analytic class-number
formula:

    h^-(K) = 2p * ∏_{χ odd} (−½·B_{1,χ}),  B_{1,χ} = (1/p) Σ_a χ(a)·a

over Q(ζ_p), evaluating the Bernoulli-product in exact rational arithmetic.

The route here instead asks PARI/GP to **compute the class groups directly**,
via `bnfinit`, on the two internal class-number definitions:

    h^-(K) = h(K) / h(K^+) ,   K = Q(ζ_p),  K^+ = Q(ζ_p + ζ_p^{-1})
                                     (degree (p-1)/2, the maximal real subfield)

and *takes the ratio of two independently computed class numbers*. `bnfinit`
builds the number field's class group through the Buchmann–Lenstra "bnf"
machinery (Minkowski bound on ideal classes, HNF reduction), which never
evaluates the Bernoulli product. The two routes share no arithmetic expression;
agreement between them is evidence the Bernoulli formula is not a self-consistent
float artefact.

## Exact normalisation used

For each odd prime p:

- `Kpol = polcyclo(p)` — the cyclotomic polynomial, defining K = Q(ζ_p), degree p−1.
- `Kp_pol = polsubcyclo(p, (p-1)/2)` — a defining polynomial of the unique real
  subfield K^+ of degree (p−1)/2. For p = 3 this returns `x−1` (degree 1, Q),
  which is correct: Q(ζ_3)^+ = Q.
- `BK = bnfinit(Kpol)`, `BR = bnfinit(Kp_pol)`, then `hK = BK.clgp[1]`
  (= the class number), `hKp = BR.clgp[1]`, and `h^- = hK / hKp` (exact rational).

Both class numbers are integers from PARI's class-group computation; the ratio
is exact integer division. All h(K^+) came out 1 for every prime here, consistent
with the classical result that the class number of the real subfield is 1 for all
p ≤ 67 (indeed h^+(p)=1 for p < 71). p=3 needing h(K^+) = 1 = h(Q) = 1 confirms
the p=3 normalisation separately.

## Results (all 13 match the expected table)

| p | h(K) | h(K^+) | h^- (PARI ratio) | expected | match |
|---|------|--------|------------------|----------|-------|
| 3  | 1 | 1 | 1 | 1 | ✓ |
| 5  | 1 | 1 | 1 | 1 | ✓ |
| 7  | 1 | 1 | 1 | 1 | ✓ |
| 11 | 1 | 1 | 1 | 1 | ✓ |
| 13 | 1 | 1 | 1 | 1 | ✓ |
| 17 | 1 | 1 | 1 | 1 | ✓ |
| 19 | 1 | 1 | 1 | 1 | ✓ |
| 23 | 3 | 1 | 3 | 3 | ✓ |
| 29 | 8 | 1 | 8 | 8 | ✓ |
| 31 | 9 | 1 | 9 | 9 | ✓ |
| 37 | 37 | 1 | 37 | 37 | ✓ |
| 41 | 121 | 1 | 121 | 121 | ✓ |
| 43 | 211 | 1 | 211 | 211 | ✓ |

**13/13 matched.** No value differed.

## Command & capture

```
timeout 540 gp -q code/hminus_pari/hminus_pari.gp
```
GP/PARI Calculator Version 2.15.2 (amd64, GMP 6.2.1).
Stack raised with `default(parisizemax, 4e9)` (only ~128 MB actually used, the
rest is headroom). Captured output: `code/out/hminus_pari.captured.txt`.

Program: `code/hminus_pari/hminus_pari.gp`.

## Status classification

- **This confirms, by an independent implementation, the numeric values**
  1,1,1,1,1,1,1,3,8,9,37,121,211 for p = 3..43. It is a **verified numerical
  cross-check**, not a proof of the class-number formula for all p.
- The agreement between the exact Bernoulli-product route (`hminus_full.py`)
  and this direct bnfinit-ratio route (which share neither the arithmetic
  expression nor the evaluation method) upgrades the numerical evidence for the
  minus-class-number values from "checked against a catalogue by one formula"
  to "reproduced by two independent methods". Both still rest on the classical
  analytic class-number theorem, which remains sourced-not-proved in this run.
