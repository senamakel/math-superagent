> **Summary — Martin, Yang, Bahrini, Bajpai, Benli, Downey, Li, Liang, Parvardi, Simpson, White, Yip**, *An annotated bibliography for comparative prime number theory*, arXiv:2309.08729 (v3, 11 Dec 2024), published *Expositiones Mathematicae* 43(3):125644 (2025), doi 10.1016/j.exmath.2024.125644.
> Full text: `research/sources/martin-annotated-bibliography-comparative-prime-number-theory.full.md` (73,722 words, indexed).

## What it is

The exhaustive, unified-notation survey of comparative prime number theory: the study of how prime-counting functions (and their normalized error terms) compare, from Chebyshev's 1853 observation of the mod-4 race through 2023/2024. It catalogues ~365 primary publications (each with a result summary), uniform notation (π, ψ, θ, ∆, E; GRH/σ₀-GRH, LI/GSH, HC, SA hypotheses), and the explicit-formula / power-sum / limiting-logarithmic-density machinery. It is **the** standard reference for the field feeding Granville's ν₂ supply.

## What it establishes (bearing on the run's G-supply / Route B)

The whole two-point **consecutive-pair mod-4** question is catalogued, and the strongest results are all on the **non-switch (equal-residue)** direction — not the switch count ν₂ needs:

1. **Knapowski–Turán [134] (1977, "On prime numbers ≡ 1 resp. 3 (mod 4)")**: unconditionally, the number of consecutive-prime pairs p_ν, p_{ν+1} with both ≡ 1 (mod 4) exceeds (log T)^B. Infinitude follows from Littlewood's mod-4 oscillation; no quantitative rate beyond the log^B lower bound. Identifies as **open**: infinitely many *triples* of consecutive primes ≡ 1 (mod 4); and that the four pair-classes (p_ν, p_{ν+1}) (mod 4) are "not equally likely" (before LOS 2016).

2. **Ruzsa [231] (2001, "Consecutive primes modulo 4", Indag. Math. 12(4) 489–503) — the reference the run listed as unobtainable.** The bibliography's abstract supplies its key result, closing the gap: **the number of pairs of consecutive primes ≤ x both ≡ 1 (mod 4) is ≫ x log log x / log² x, improving Shiu; a generalization holds where the single class 1 (mod 4) is replaced by any set of φ(q)/2 reduced residue classes mod q. Proof uses Maier's method.** This is the same *equal-residue* direction Shiu proved (correlated strings), and it is a **weak** (loglog/log²) lower bound, not positive density.

3. **Ruzsa's content is a weak infinitude/lower-bound, on the non-switch direction.** For ν₂, which counts **switch** pairs (gap ≡ 2 mod 4, i.e. p_{n+1} ≢ p_n mod 4), these results give **nothing**: they lower-bound the equal-residue pairs, the opposite statistic. The strongest unconditional consecutive-pair mod-4 bounds are all of the same non-switch, sub-density form; NO source in this comprehensive field survey gives a density lower bound on the switch count, which is exactly what ν₂ > n^β needs.

4. The one-sided Chebyshev-bias literature (Rubinstein–Sarnak [215], LOS [305]/[327]) confirms the run's held conclusion: the honest statement for the consecutive-pair statistic is a fluctuation/distribution law at GRH/LI+HL level, and the sign oscillates. The bibliography restates the LOS 2016 main observation (repeated residues less frequent than changing ones — i.e. a slight *switch excess*, consistent with ν₂/n ≈ 1/2 but not a proof).

## SSynthesis for the run

- `Ruzsa 2001`'s abstract-level result is now **held** (via this bibliography): the equal-residue pair count is ≫ x loglog x/log²x (Maier's method, sub-density). This confirms and sharpens what the run had at zbMATH abstract level, and re-states with authority that **no positive-density or ν₂-grade lower bound on the mod-4 switch count exists**.
- **G-supply remains open.** ν₂(q_n) > n^β (β>0.525) is not delivered by any catalogued result; the honest ceiling stays the **conditional** result at Hardy–Littlewood / LOS level (IF a two-point mod-4 switch bound THEN GC via the proved Lemma 5.4).
- **Do not re-search this line** unless genuinely new quantitative switch-density work appears: the field's own exhaustive survey (2024) shows nothing delivers it.

## Provenance & indexing

arXiv PDF 2309.08729 (arXiv, not paywalled; the Exp. Math. journal version is the same content). Indexed and searchable. Its citations added 17 rows to `research/FRONTIER.md`.
