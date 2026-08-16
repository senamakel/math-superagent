# ROOT — where the run stands, and the live line of attack

The phase-1 completion condition: the structure of a minimal counterexample, the
current verification bound, and the restricted classes already settled with their
hypotheses. Everything here traces to a claim block under `research/summaries/`
or `code/out/`; the full ledger is `research/CLAIMS.md`.

## Problem (restated)

Erdős (1979): for `n > 8`, the base-3 expansion of `2^n` contains a digit 2. The
only digit-2-free powers are `2^0=1=(1)_3`, `2^2=4=(11)_3`, `2^8=256=(100111)_3`.
Open since 1979; believed true; `research/CLAIMS.md` holds the sourced/verified
statement.

## Structure a minimal counterexample must have

A counterexample is `n > 8` with `2^n = Σ_{a∈A} 3^a`, `A` distinct, `A` containing
no `2`-digit — i.e. `2^n = Σ_{a∈A} 3^a` is a sum of *distinct* powers of 3. Forces on it:

- **n even.** `2^n ≡ 1 (mod 3)` iff `n` even, so a digit-2-free `2^n` (last digit 1) has
  `n` even. (`OEIS-PARITY-CONSTRAINT`, proved.)
- **n ≡ 0 (mod 8)? not forced — `n=8` is a witness and `n=0,2` too.** A *minimal* counterexample
  is the least `n>8` digit-2-free; nothing forces its congruence beyond `n` even.
- **The counterexample is `4^e` with `e = n/2`.** Parity reduction (`2^{2e}`); run under
  `x↦4x` capture in the Spencer refutation note (`SPENCER-CARRY-PACKET-UNSOUND`, arithmetic only).
- **It must be digit-{0,1} in ternary with ≥ 26 ones.** `DIMITROV-HOWE-26-ONES` (proved,
  Rocky Mountain J. Math): outside `{0,2,8}`, `2^x` has a digit 2 *or* ≥ 26 ones. So
  a digit-2-free counterexample must have **≥ 26 ones** and **zero 2s** — the residual open case.
- **Its low-k ternary tail is unconstrained for every finite k.** `R-low-k` (failed rung):
  every `n ≡ 8 (mod 2·3^(k-1))` has `2^n ≡ 2^8 ≡ 100111_3 (mod 3^k)`, all digits in {0,1}.
  So no fixed low-k sieve ever closes on the residue class of `n=8`. This is the
  `|A_k|=2^(k-1)` counting obstruction (`SIEVE-EXACT-COUNT`, verified k=1..26 by the
  captured oracle `code/out/oracle_verify.captured.txt`).
- **Any 2-inforcing or parity obstruction must fail n=0,2,8.** The falsification oracle.

## Current verification bound

- **`n ≤ 2·3^45 ≈ 5.9×10^21`** — `SAYE-VERIFICATION-BOUND` (verboatim in Saye 2022
  full text: "every possible ternary digit, for all 16 ≤ n ≤ 2·3^45"). Sourced, not
  reproduced in this run; the run's own modest oracle (`code/out/oracle_verify.captured.txt`)
  covers finite_check over `[1,1000]` = {2,8} and `|A_k|=2^(k-1)` for k=1..26.
- **Narkiewicz 1980:** `#{n ≤ X : (2^n)_3 omits 2} ≤ 1.62·X^(log_3 2)`, `log_3 2 ≈ 0.63092`
  (verboatim in Lagarias 2009). `LAGARIAS-NARKIEWICZ-BOUND`.
- **Dimitrov–Howe:** the residual is "≥ 26 ones, no 2s" (`DIMITROV-HOWE-26-ONES`).

## Restricted classes already settled (with hypotheses)

1. **Witness set `n ≤ 8`** (`R-witness`, settled): digit-2-free among `{0..8}` exactly at
   `{0,2,8}`. Hypothesis: `n ≤ 8`.
2. **Bounded ones-count** (`R-bounded-ones`, settled; `DIMITROV-HOWE-26-ONES`): `2^x` writable
   as a sum of ≤ 25 distinct powers of 3 are exactly `2^0,2^2,2^8`. Hypothesis: at most 25 ones.
   Proved by elementary congruences (Dimitrov–Howe 2021 Thm 1.2).
3. **Sieve counting** (`SIEVE-EXACT-COUNT`, verified): `|A_k|=2^(k-1)`; the modular sieve can
   never close at finite k. Hypotheses: `ord_{3^k}(2)=2·3^(k-1)`.
4. **c1 even** (`c1-even-parity`, proved): the number `c1(n)` of digit-1s in `(2^n)_3` is even
   for all `n ≥ 1`. Hypotheses: `n ≥ 1`. Any counterexample therefore has an even number of ones.
5. **Carry equivalence** (`carry-count-zero-iff-digitfree`, proved): zero base-3 carries when
   doubling `2^n` ⟺ `2^n` digit-2-free. A carry-language restatement of the predicate.
6. **Density-1 digit-0** (`DEFARIA-TRESSER-DENSITY-1-DIGIT-ZERO`, proved): `{n : 2^n has a 0
   digit base 3}` has asymptotic density 1. Management background, not a proof of Erdős.
7. **Narkiewicz count bound** (`LAGARIAS-NARKIEWICZ-BOUND`, sourced/proved-in-source):
   `N1(X) ≤ 1.62 X^α0`.

## The live line of attack

`research/backward/erdos-via-symbolic-invariant.md` — a finite-transducer statistic `Φ` on the
`{2^n}` orbit (the `x↦2x` carry), with `Φ(0),Φ(2),Φ(8) ∈ W`, `2^n∈S ⇒ Φ(n)∈W`, and
`n>8 ⇒ Φ(n)∉W`. The whole question is the middle-digit coupling that the sieve (low digits)
and size arguments (high digits) never reach. Reference points:

- **The statistic cannot be a continuous function of the 3-adic point**: the `{2^n}` orbit is
  dense in `Z_3^×` (met in BACKWARD.md), so a continuous `×2`-invariant is constant on the
  closure and cannot separate `S`. Must be a transducer statistic on the digit strings.
- **The only live lemma** is `G-invariant`; `G-cong` is discharged. The reference library
  strengthens the known negatives: `ALBAYRAK-BELL` proves no Cobham/Walnut decidability
  machinery reaches the sparse × zero-density intersection; the weighted-polarity SMT
  candidates were **refuted at n=0** (`research/approaches/smt-weighted-polarity-refuted.md`);
  the Spencer carry-packet proof is **unsound** at its completeness step
  (`SPENCER-CARRY-PACKET-UNSOUND`).

## What the memory holds that the workspace must keep separate

The three verification bounds (Gupta `n<4374`, Vardi `n≤2·3^20`, Saye `n≤2·3^45`) are
**sourced but not reproduced in this run**; the run's own oracle bound (`[1,1000]`, `k≤26`) is
separate and recorded separately. `|A_k|=2^(k-1)` is **verified in this workspace** by the
captured oracle — the earlier `2^k` memory value is refuted and the CONTEXT.md contradiction
is resolved in favour of `2^(k-1)`.

## Gap: the cross-modulus route to the unbounded case is open

*(Research findings, this pass; each labelled asserted-by-source vs verified.)*

- **The >25-ones case is the residual open case, and the cross-modulus route has no
  published precedent for it.** `DIMITROV-HOWE-26-ONES` (proved, published) reduces the
  conjecture to "≥ 26 ones, no 2s" — i.e. equation (2) `2^x = Σ_{a∈A} 3^a` with |A|
  **unbounded**. A survey (Lagarias 2009, Saye 2022, Li–Zhao 2026, Roettger–Ren 2025,
  Bertók–Hajdu 2015, and DH themselves) found **no published application** of the
  Dimitrov–Howe mixed-modulus / cross-order ladder, or the Bertók–Hajdu / Skolem lifting
  conjecture, to the unbounded-|A| case. *asserted-by-source* (absence-of-result is a fact
  about the literature as searched).
- **No published result mixes primes other than 3 into the modulus to reduce the survivor
  count `|A_k|` below `2^(k-1)`.** The pure 3-adic sieve is the degenerate `M'=1` case of
  Lemma 3.1 (`O'2 = O'3 = 1`), where no extraneous solution is ever forced, so `|A_k| =
  2^(k-1)` never closes. Whether a mixed modulus `M = 2^u 3^v M'` can beat this is **open**.
  *asserted-by-source* (gap statement), with the elementary facts (`M'=1 ⇒ O'2=O'3=1`;
  tail length = `v2(M)`) *verified* by hand here.
- **The one verified anchor:** the DH n=3 examples reproduce exactly as written — `M1 = 5440
  = 2^6·5·17` has extraneous solutions (unique non-trivial one `3^4 = 2^0+2^4+2^6` with `2^6`
  indeterminate, on the 8-loop), and `M2 = 2^7·5·17·257` is clean (all three summands
  determinate, tail length 7; `ord_257(3)=256` a multiple of `2^5` defeats Lemma 3.1).
  *verified* (exact small-integer arithmetic; see `DH-N3-EXAMPLES-VERIFIED`).
- **What would falsify the claim that the ladder beats the pure 3-adic sieve**
  (`CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES`): a mixed modulus for which Lemma 3.1's
  generalisation forces all-but-{0,2,8} classes to involve an indeterminate power but the
  survivor count is *not* reduced below `2^(k-1)`; or a k+1-term generalisation of Lemma 3.1
  that fails to reproduce the DH n=3 examples and the sieve count. *derived-here, unverified*.
