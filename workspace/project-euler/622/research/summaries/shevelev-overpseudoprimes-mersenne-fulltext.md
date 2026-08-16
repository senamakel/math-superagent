# Shevelev et al. — Overpseudoprimes, and Mersenne and Fermat numbers as primover numbers

Source: https://arxiv.org/abs/1206.0606 (full text: https://ar5iv.labs.arxiv.org/html/1206.0606) ·
Full text: [[shevelev-overpseudoprimes-mersenne-fulltext.full]]

## What it establishes

Introduces "overpseudoprimes to base b" — composite n where the cyclotomic-coset
equation `n = r(n)·|2|_n + 1` holds (r(n) = number of cosets of 2 mod n), a
subclass of the Poulet (base-2 Fermat) pseudoprimes.

Two structural facts about multiplicative orders, relevant to PE622's
order-lattice of the divisors of 2^60−1:

- **Theorem 2**: an odd composite n is overpseudoprime to base 2 if and only if
  the multiplicative order |2|_n equals |2|_d for **every** divisor d > 1 of n —
  i.e. the order of 2 is *invariant across all proper divisors* of n.
- **Corollary 4**: for a prime p, M_p = 2^p − 1 is either prime or an
  overpseudoprime to base 2. Proof: any d > 1 dividing 2^p−1 has |2|_d | p,
  hence |2|_d = p for all such d — exactly the order-invariance criterion.
- **Corollary 3**: overpseudoprimes N_1, N_2 with |2|_{N_1} ≠ |2|_{N_2} are
  coprime.
- Generalisation to arbitrary base b (section 4): composite n overpseudoprime to
  base b iff |b|_d invariant over divisors d > 1; squares (and higher powers)
  of Wieferich primes are overpseudoprime to base b.

## Why it matters here

For each prime-power divisor class of 2^60−1, the order of 2 mod a Mersenne
divisor is locked to the exponent. In particular, whenever a proper divisor d of
2^p−1 (p prime) appears, ord_d(2) = p. This is a *secondary, independent*
confirmation of the run's divisor/lattice order structure
(`order-lcm-over-prime-powers`, `order-divisibility-conrad`) and of the
Wieferich-lift machinery: the same "|2|_d has a forced value inherited from the
Mersenne exponent" phenomenon that drives the enumeration of m with
ord_m(2) = 60. It connects Mersenne divisibility to order-invariance, exactly
the principle the inclusion-exclusion over divisors of 2^60−1 leans on.

## Does not settle

No new computed values, no enumeration of m with ord_m(2)=60, and it does not
give the factorization of 2^60−1. It is a structural/number-theoretic context
paper, not the computation.

## Status

Peer-style paper (Applicable Analysis & Discrete Mathematics, 2012); the
overpseudoprime / order-invariance Theorems 2 and 4 (Corollaries 3–5) are proved
in the paper. Hypotheses (odd composite Mersenne divisors, base 2) hold here.
No `claim` block added — it backs existing claims `order-lcm-over-prime-powers`
and `wieferich-lift-order` rather than introducing a new load-bearing statement.
