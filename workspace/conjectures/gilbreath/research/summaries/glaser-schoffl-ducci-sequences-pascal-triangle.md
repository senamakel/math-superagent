# Glaser–Schöffl — Ducci-sequences and Pascal's triangle

**Full text:** `research/sources/glaser-schoffl-ducci-sequences-pascal-triangle.full.md`
**Source URL:** https://www.fq.math.ca/Scanned/33-4/glaser.pdf
**Published:** Fibonacci Quarterly 33.4 (1995) 313–324.

The paper that grounds the run's Rule-90 interior identification in the Ducci literature. It proves that the **basic Ducci sequence** (starting from `A0 = (0,…,0,1)`, cyclic length n, over Z₂) is **exactly the rows of Pascal's triangle modulo 2**, written as n-tuples by left-padding each row with zeros:
- entry `a_{k,i} = C(k, i−n+k) mod 2`; the recurrence `a_{k+1,i} = a_{k,i} + a_{k,i+1} (mod 2)` is Pascal's addition law. **Theorem 1:** the n rows of the modified Pascal triangle are A0..A_{n−1} of the basic-Ducci-sequence.
- This is the same Sierpinski/`binom(2^r, m) ≡ 0 (mod 2)` structure (Lemma 1, after Hinz) that CHT 2026 §1 point out for {0,d}-blocks and that this run proved as `rule90-interior-xor`: the halved entries of a {0,2} block evolve by XOR = Pascal mod 2.

**Exact results of the paper (cycle structure of the cyclic binary Ducci map):**
- Mod-2 reduction: `|a−b| ≡ a+b (mod 2)`; the map is `D = I + K` (identity + cyclic shift), `Kⁿ = I`.
- Ehrlich's theorems quoted: for the basic Ducci sequence, the max cycle length is `2P(n)` (their notation; `P` = their period, 2P(odd)-normalized); `2^m ≡ 1 mod n ⇒ Φ(n) | 2^m − 1`; `2^M ≡ −1 mod n ⇒ Φ(n) | n(2^M − 1)`; `n | 2P(n)` when n is not a power of 2; `2P(n) = 2^r Φ(ℓ)` for `n = 2^r·ℓ`, ℓ odd.
- **Theorem 4:** for n "with a −1" (odd n with some `2^M ≡ −1 mod n`), `Φ(n) = n(n−2)` iff `n = 2^r + 1`.
- **Theorem 5:** `n = 2^r + 2^s ⇒ Φ(n) = n(n−2^s+1)/2^s`·(their formula).
- **Theorems 7–9:** `Φ(n) = n` (the cycle length equals the vector length) iff `n = 2^r − 2^s`.
- **Theorems 11–15, Corollary 3–4:** classification of which n are "with a −1": for `p ≡ −1 mod 4`, p is with a −1 iff `(p²−1)/8` is odd; complete solution is linked to the [still open] Artin conjecture on primitive roots. This is the number-theoretic backbone of cyclic Ducci cycle lengths.

**What this establishes for this run:**
- **Primary, peer-reviewed, independent confirmation of the Pascal-mod-2/Rule-90 structure** of the iterated-difference map — the run's `rule90-interior-xor` is not just folklore or Wikipedia, it is the main theorem of a Fibonacci Quarterly paper (which traces it to Lucas and Glaisher via Hinz).
- The classical facts `binom(2^r −1, i) ≡ 1` (all-1s row at depth 2^r−1) and `binom(2^r, i) ≡ 0` for 0<i<2^r (all-0s interior at depth 2^r) — the exact kernel properties the `rule90-regeneration` thread uses to predict all-2 stretches at depths 2^j−1 — are **proved here** (properties (5),(6),(7) in the paper, also Stolarsky's digit-sum count `2^{s₂(k)}` ones in row k).
- Again: **cyclic** setting. The papers's "n-tuples" wrap around; the Gilbreath triangle is the non-cyclic half-infinite analogue. What transfers (the Pascal/XOR kernel, binomial-parity identities) transfers at the level of the local recurrence, not the global cycle-length conclusions.

**Status:** sourced (peer-reviewed primary). The power-of-2 all-1s/all-0s Pascal facts are now anchored in a primary Ducci source, strengthening `rule90-interior` and the `rule90-regeneration` thread's depth-2^j−1 prediction.