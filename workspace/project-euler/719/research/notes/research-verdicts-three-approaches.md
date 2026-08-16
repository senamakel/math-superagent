# Research verdicts on the three proposed reformulations (PE 719)

Researcher's literature check of the inventor's three candidate lines of attack,
each already written to `research/approaches/`. Field filled: `precedent`;
`status` set. All reasoning and full statement in the individual approach files.

## 1. repunit-linear-representation — status: grounded (mechanism), payoff open

The identity m(m−1)/9 = Σ bᵢ R_{Lᵢ} (R_L = (10^L−1)/9, Lᵢ = decimal digits strictly
to the right of block bᵢ) is correct and is the full Butler–Graham–Stong
partition-and-sum structure (arXiv:1501.04067). Verified by hand on the
statement's witnesses:
  - 82² = 6724 = 6|72|4: 82·81/9 = 738 = 6·R₃ + 72·R₁ + 0·R₀ = 666+72+0 ✓
  - 91² = 8281, 99² = 9801: two-block collapse gives (10^L−1) | m(m−1), the
    Kaprekar/torn-number congruence (claims `iannucci-kaprekar-divisor-formula`,
    `dudeney-torn-number-two-block`).
New claim filed `repunit-witness-identity` (status: checked).
The mod-9 invariant (`partition-sum-invariant-mod9`) is exactly this identity mod 9.
**Not settled by literature:** whether the k ≥ 3 block equation admits a compact
parametrisation. No published treatment found; no counterexample found either.
This is a genuinely open research question.

## 2. k-automaticity-cobham — status: proposed (ungrounded), not refuted

- Cobham's dichotomy cannot settle "is 1_S base-10 automatic": it needs a second,
  multiplicatively independent base, which is no easier to establish.
- Christol's theorem characterises *prime* p-automatic sequences, not composite-base
  recognisability; base 10 is composite (ℤ₂×ℤ₅).
- Settled negatives: {n^t} is not k-recognizable for any base (Rigo/Eilenberg);
  the squares' characteristic sequence s1 is nonautomatic (hal-04504166).
- These do NOT refute automaticity of the subset 1_S.
- No source found proving or refuting "1_S is base-10 automatic". The intended
  O(log N)-type payoff is unsupported; the carry state has no boundedness argument.

## 3. hensel-digit-lifting — status: grounded (technique), payoff open

- Mechanism (digit-by-digit square lifting / Hensel over ℤ₁₀=ℤ₂×ℤ₅, constraint
  propagation over decimal digits, long-division square roots) is a real,
  literature-confirmed technique (arXiv:2601.02703; Zambaldi Garcia et al. 2026;
  Zerzaihi–Kecies–Knapp 2010; relaxed Hensel lifting).
- Its application to the split-and-sum-to-root predicate is novel (no precedent found).
- It offers no N-independent gain; worst case equals the settled O(sqrt N) scan.
  Whether block-boundary pruning wins is an empirical measurement, not a theorem.

## Sources

- Butler, Graham, Stong, "Partition and sum is fast", arXiv:1501.04067 (https://arxiv.org/html/1501.04067v1)
- Rigo, "Recognizable sets of integers" (https://pdfs.semanticscholar.org/454e/1760e9e7c4152e41cfbce85de2632ce9354a.pdf)
- hal-04504166 (square-sum indicators nonautomaticity) (https://hal.science/hal-04504166v1/document)
- Goč–Schaeffer–Shallit arXiv:1206.5352 (subword complexity of automatic sequences)
- Allouche–Shallit–Yassawi arXiv:2104.13072 ("How to prove that a sequence is not automatic")
- arXiv:2601.02703 (exact digit-by-digit e-th root extraction)
- Zerzaihi–Kecies–Knapp 2010 DOI 10.2298/aadm1000009m (Hensel codes of p-adic square roots)
- Pandichelvi & Umamaheswari IJARSET 2024 DOI 10.22214/ijraset.2024.63251 (nearest attempt at
  multi-part Kaprekar parametrisation; no closed form / enumeration)
