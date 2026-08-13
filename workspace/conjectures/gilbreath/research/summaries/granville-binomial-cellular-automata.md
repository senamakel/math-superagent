# Granville, Arithmetic Properties of Binomial Coefficients — chapters (Lucas/Kummer; cellular automata)

**Full texts:** `research/sources/granville-binomial-lucas-elementary.full.md` (ch. "Elementary Number Theory") and `research/sources/granville-binomial-cellular-automata.full.md` (ch. "Pascal's triangle via cellular automata") of Andrew Granville's dynamic e-survey at https://dms.umontreal.ca/~andrew/Binomial/ (root page `granville-arithmetic-properties-of-binomial-coefficients.full.md` is a table of contents).
**Source URLs:**
- https://dms.umontreal.ca/~andrew/Binomial/ (root TOC)
- https://dms.umontreal.ca/~andrew/Binomial/elementary.html (Lucas/Kummer chapter)
- https://dms.umontreal.ca/~andrew/Binomial/cellautom.html (cellular automata chapter)

## What these chapters establish (primary reference for the mod-2 microscope)

1. **Legendre's formula** (1808): the exact power of p dividing n! is v_p(n!) = Σ_j ⌊n/p^j⌋ = (n − s_p(n))/(p−1), where s_p(n) is the base-p digit sum.
2. **Kummer's theorem**: the exponent of p in binom(n,m) is the number of carries when adding m and n−m in base p.
3. The Anton–Stickelberger–Hensel refinement of Lucas' theorem: binom(n,m) mod p-congruences via digit expansions (eq. (19) and its generalization to prime powers, ch. "Generalization of Lucas' Theorem" — not downloaded; the elementary chapter proves the base cases and states the carry connection).
4. **Sierpiński/automaton structure (mod 2, p=2)**: Pascal's triangle modulo 2 is self-similar; row 2^j is all 1s between zeros; the 2^j-th row is two copies of the r-th row with zeros between (Wolfram's proof of **Glaisher's theorem**: the count of odd entries in row n is 2^{s_2(n)}); subtriangles of Pascal's triangle mod p obey the same addition law as the triangle itself (Long).

## Bearing on this run

This is the primary, cited source for the exact fact the rule90-regeneration thread and the mod-4 linearization rest on: within a {0,2} block, halved entries evolve under XOR (= addition mod 2 = Pascal mod 2), and at depth d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all m — so the halved entry is the XOR of the whole window (Sierpinski kernel). Glaisher's 2^{s_2(i)} odd-entries count is the same digit-sum statistic Ross 2026 finds modulating the decay constants c_i. The "subtriangles obey the same addition law" sentence is the Pascal-mod-2 analogue of the run's block-lemma diagonal-subtriangle argument.

## Status

Sourced (Granville's e-survey, author's own page — a canonical free primary/secondary reference; Fine 1947 AMM 54:589–592 is the original paper with the proof of the Lucas correspondence and is paywalled/unobtainable as a clean PDF here, recorded unobtainable). Downloaded chapters verified to contain the statements above. The modulo-prime-power generalization chapter (genlucas.html) is not downloaded — only needed if the run moves to mod-8/16 structure.