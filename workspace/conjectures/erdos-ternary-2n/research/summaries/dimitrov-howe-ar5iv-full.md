# Dimitrov–Howe: Powers of 3 with few nonzero bits and a conjecture of Erdős

**Source:** arXiv:2105.06440 (2021, v4 2023), Rocky Mountain J. Math. Full text at `research/sources/dimitrov-howe-ar5iv-full.full.md`.

## What it establishes

**Theorem 1.1:** The only powers of 3 that are sums of ≤22 distinct powers of 2 are 3^x for 0 ≤ x ≤ 25.

**Theorem 1.2 (the relevant one for Erdős):** The only powers of 2 that are sums of ≤25 distinct powers of 3 are
- 2^0 = 3^0 = 1
- 2^2 = 3^0 + 3^1 = 4
- 2^8 = 3^0 + 3^1 + 3^2 + 3^5 = 256

Equivalently: for x ∉ {0,2,8}, the base-3 expansion of 2^x either contains a digit 2 **or** contains at least twenty-six 1s.

This is the strongest known *provable* statement about the sparse side of the Erdős conjecture: a counterexample must have at least 26 ones.

## Method (important — it is the same shape this run's sieve takes)

- Work modulo a nested sequence of moduli M_1 | M_2 | ... (each M_i = product of carefully chosen factors m_i).
- At each stage enumerate solutions to 3^x ≡ Σ 2^(a_j) (mod M_i), then "lift" to M_{i+1}; stop when all summands are *determinate* (a power p^i is determinate mod M iff M is divisible by p^(i+1), i.e. it lies on the tail, not the cycle, of the powers-of-p diagram).
- Moduli chosen to make the orders of 2 and 3 mod the new prime p have the right 2- and 3-adic valuations (they need primes with O_3' divisible by large 2-powers and O_2' by large 3-powers).
- The technique is purely elementary (ring theory, CRT, discrete logs); proofs terminate because after finitely many lifts every power that appears is determinate.

## Implication for this run

The Erdős conjecture is *equivalent* to: no 2^x (x>8) is a sum of distinct powers of 3 with zero 2-digits and *arbitrarily many* 1s. Dimitrov–Howe close off the ≤25-ones cases; the residual is "≥26 ones and no 2s", which is exactly what the middle-digit structure must forbid. Their modulus-sequence philosophy is a cleaner template than a fixed 3^k sieve: sieve a sequence of moduli that the order structure makes determinate one stage at a time.

## Claims
```claim
id: DH-1
statement: For x ∉ {0,2,8}, the ternary expansion of 2^x contains a digit 2 or at least 26 digits equal to 1.
hypotheses: none beyond x integer.
holds-here: yes — direct partial resolution of the sparse side of the conjecture.
status: proved (elementary; computational proof in Magma, self-contained)
bearing: any counterexample to Erdős must have ≥ 26 ones; the "no-2" sieve must therefore survive at least 26 ones.
anchor: research/sources/dimitrov-howe-ar5iv-full.full.md
```
```claim
id: DH-2
statement: The nested-modulus method with determinate-power lifting solves 3^x = Σ 2^(a_i) (n ≤ 22 distinct) and 2^x = Σ 3^(a_i) (n ≤ 25 distinct) completely, and the computations terminate.
hypotheses: moduli chosen per their Table 3 and Lemma 3.1; prime factors p with ord_p(3) having large 2-part and ord_p(2) large 3-part.
holds-here: yes — this is the template for an exact modular sieve of the Erdős equation.
status: proved (with computational certificate; programs in supplementary Magma)
bearing: the run's sieve should mirror the determinate-power staging rather than a single-modulus sieve.
anchor: research/sources/dimitrov-howe-ar5iv-full.full.md
```