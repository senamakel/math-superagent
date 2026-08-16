# Maßberg, "The Union-Closed Sets Conjecture for Small Families" (arXiv:1508.05718, 2015)

Full text (read): [[massberg-separating-small-families-2015.full]] · Source: https://arxiv.org/html/1508.05718

## What it establishes (primary source, statements read)

**Main theorem (Theorem 2.1).** The Union-Closed Sets Conjecture holds for every
*separating* union-closed family `𝒜` whose universe has `m` elements and whose
size satisfies

```
|𝒜| ≤ 2·( m + m/(log₂ m − log₂ log₂ m) ).
```

For large `m` this is just over `2m`, converging to `2m` from above. This
improves Falgas-Ravry's `|𝒜| ≤ 2m`.

**Supporting results:**
- **Theorem 1.2 (Falgas-Ravry).** In a separating union-closed family with
  elements `x₁,…,x_m` labelled by increasing frequency, there are sets
  `X₀,…,X_m ∈ 𝒜` with `xᵢ ∉ Xᵢ` (i = 1..m) and `{x_{i+1},…,x_m} ⊂ Xᵢ`
  (i = 0..m).
- **Lemma 1.3 (consequence).** Any separating family on `m` elements with
  `≤ 2m` member sets satisfies UC (the most frequent element `x_m` lies in the
  `m` pairwise-different sets `X₀,…,X_{m−1}`).
- **Theorem 1.4 (Hu).** If some `c > 2` works for *all* separating families with
  `|𝒜′| ≤ c·|U(𝒜′)|`, then every union-closed family has an element of frequency
  `≥ (c−2)/(2(c−1))·|𝒜|`. So a theorem for the "small family" regime at ratio
  `c` yields a constant fraction for ALL families.

## Why it matters for this run

- **Small-family verified range.** UC holds for *separating* families with
  `|𝒜| ≤ 2(m + m/(log₂m − log₂log₂m))` — the ROOT.md "separating families,
  |F| ≤ 2·n + n·log₂n − log₂log₂n" row. (Note the correct form: `2(m + m/(log₂m − log₂log₂m))`.)
- **Hu's reduction.** A `c > 2` constant-density theorem at the small-family
  boundary would yield a constant fraction for all families — so a minimal
  counterexample, if it exists, must be *separating* with size ratio
  `> 2(m + m/(log…))`, i.e. "medium"-sized. This connects the small/large
  verified regimes to the constant question.
- Separating can be assumed WLOG (identified elements collapse without changing
  `|𝒜|` or union-closure).

```claim
id: massberg-small-families
statement: UC holds for every separating union-closed family A with
  |A| <= 2(m + m/(log2 m - log2 log2 m)) elements, m = |U(A)|; improves
  Falgas-Ravry's 2m.
hypotheses: A separating union-closed, m = |U(A)|
holds-here: yes (separating is WLOG for UC)
status: proved (Theorem 2.1, in-paper)
bearing: a minimal counterexample must be separating with
  |A| > 2(m + m/(log2 m - log2 log2 m)) -- the small-family end of the
  "medium-sized" regime
anchor: research/sources/massberg-separating-small-families-2015.full.md (Thm 2.1)
follows-from: falgas-ravry-separating-degree (the A_i-set construction, Maßberg's Thm 1.2), hu-small-family-to-constant
```

```claim
id: hu-small-family-to-constant
statement: If some c > 2 satisfies UC for ALL separating families with
  |A'| <= c|U(A')|, then every union-closed family has an element of frequency
  >= (c-2)/(2(c-1)) |A|.
hypotheses: a c > 2 with small-family UC at that ratio
holds-here: yes (statement is conditional, sourced to Hu)
status: asserted-by-source (Hu [5], quoted in Maßberg)
bearing: a bounded constant-density theorem from a small-family regime theorem;
  the channel through which small-family progress becomes global constant
  progress
anchor: research/sources/massberg-separating-small-families-2015.full.md (Thm 1.4)
```

## Status
Statements read and confirmed in the full body. Not numerically re-checked
(oracle is n ≤ 4, where the bound is trivially satisfied). The exact bound form
`2(m + m/(log₂m − log₂log₂m))` corrects the ROOT.md row, which omitted the
inner `m/(...)` normalisation.
