# Katz, "Wieferich Past and Future" — reference tier (double-Wieferich background)

**Source URL:** https://web.math.princeton.edu/~nmk/wieferich37.pdf (freely hosted
reprint). Published version: Nicholas M. Katz, "Wieferich past and future", in
*Topics in Finite Fields*, Contemporary Mathematics **632**, Amer. Math. Soc.
(2015). DOI 10.1090/conm/632/12632.

**Author/venue:** Nicholas M. Katz (Princeton). Conference survey volume.

**Type:** Research survey (primary, freely hosted). **How obtained:** server-side
full-text readout via `read_sources` (host blocked for `download_document` —
Princeton PDF host and the AMS DOI both unreachable from the network boundary).

**Status:** CAPTURED summary + exact statements via `read_sources`. Not stored as
a full text; exact statements quoted in-document below from the readout.

## Why this is in the library

This is the FRONTIER's top-cited non-answer source for this run (cited 3 times
by the library's own sources as a reference on Wieferich primes). It bears on
the **double-Wieferich gap** (`research/REQUESTS.md` row
`exact-statement-citable-f890`) and on the Wieferich machinery the run's
both-odd-prime descent uses. It is **not** answer-bearing for `problem.md`: it
is about base-`a` Wieferich primes and their conjectured *distribution*, not
about the Catalan closure step, so it does not trip the evidence screener.

## Exact statements captured

- **Wieferich's theorem (Thm 1.1).** Let `p ≥ 5` be a prime. If the first case
  of Fermat's Last Theorem is false for `p`, then `2^{p−1} ≡ 1 (mod p²)`. A
  prime with `2^{p−1} ≡ 1 (mod p²)` is a **Wieferich prime (to base 2)**.
- **Mirimanoff's theorem (Thm 1.2).** Same hypothesis gives `3^{p−1} ≡ 1
  (mod p²)`; such primes are "Wieferich primes to base 3".
- **Vandiver's theorem (Thm 1.3).** Same hypothesis gives `5^{p−1} ≡ 1
  (mod p²)` (base 5).
- **Wieferich quotient (definition).** For a nonzero integer `a` and a prime
  `p ∤ a`, the Wieferich quotient is `W_a(p) := (a^{p−1} − 1)/p ∈ (1/p)Z/Z ⊂ Q/Z ⊂ R/Z`.
- **Wieferich conjecture (first form, Conj 3.1).** For any integer `a ≠ 0, ±1`,
  the sequence of Wieferich quotients `W_a(p)`, indexed by primes `p ∤ a`, is
  equidistributed in `R/Z` for its Haar measure of total mass one; equivalently
  `exp(2πi·W_a(p))` is equidistributed on the unit circle.

## Numerical facts (as stated by Katz)

- Base 2: only two known Wieferich primes, **1093** (Meissner 1913) and **3511**
  (Beeger 1922); the next, if any, exceeds `6.7 × 10^15` (Dorais–Klyve search).
- Base 3: first is 11; next is 1006003 (Kloss 1965); next exceeds `9.7 × 10^14`.
- Base 5: six known — 20771, 40487, 53471161, 1645333507, 6692367337, 188748146801.

## Relation to the run's question (double-Wieferich)

The run's both-odd-prime case uses *double*-Wieferich congruences
`q^{p−1} ≡ 1 (mod p²)` and `p^{q−1} ≡ 1 (mod q²)`, which are **cross-base**
(the base differs from the modulus: base `q` mod `p²`). Katz's survey concerns
single-base Wieferich primes `a^{p−1} ≡ 1 (mod p²)` with `a` fixed and `p`
varying, so it is background — it fixes the definition and the Fermat-first-case
origin of the name — but it does **not** supply the double-Wieferich condition
itself, which must be re-derived from Cassels's divisibility (`request
exact-statement-citable-f890`). It confirms that single-base Wieferich primes
are sparse (heuristic: O(log log x) up to x, see also Crandall–Dilcher–Pomerance
search, base 2 only 1093, 3511 < 1.25×10^15).

## Claims

```claim
id: wieferich-primes-two-known-base2
statement: > A prime p with 2^{p-1} ≡ 1 (mod p^2) is a Wieferich prime (base 2); the only known ones are 1093 and 3511, and any further one exceeds 6.7e15.
hypotheses: p prime, p >= 5
holds-here: yes (background to the double-Wieferich gap; not itself the gap)
status: asserted
bearing: fixes the definition and search-record for the Wieferich congruences the both-odd-prime analysis needs; confirms sparsity heuristic.
anchor: research/sources/katz-wieferich-past-and-future.md
```

```claim
id: wieferich-criterion-first-case-flt
statement: > (Wieferich, via Katz Thm 1.1) If the first case of FLT fails for a prime p >= 5 then 2^{p-1} ≡ 1 (mod p^2). Mirimanoff: base 3; Vandiver: base 5.
hypotheses: p prime >= 5, first case of FLT false for exponent p
holds-here: no (this problem is x^p - y^q = 1, not FLT; the stated hypotheses do not hold here). Background only.
status: asserted
bearing: the historical origin of the name "Wieferich" — the same congruence shape (base^{p-1} ≡ 1 mod p^2) that the double-Wieferich gap reuses.
anchor: research/sources/katz-wieferich-past-and-future.md
```

## Falsifier note

`holds-here: no` for the FLT-criterion claim is deliberate: it is a theorem
about FLT, and its hypothesis (first case of FLT false) is never satisfied by
the run's problem. It is recorded for the definition and the name, not as a
lemma in the run's chain. The `wieferich-primes-two-known-base2` fact is
numerical background, not load-bearing for any proof step.
