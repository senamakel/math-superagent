# Giacomelli 2021 — "p-adic Ducci Sequences: a short note" (arXiv:2104.06491)

**Full text:** `research/sources/giacomelli-2021-p-adic-ducci-sequences-short-note-html.full.md`
(the `.full.md` from the `/abs/` landing page is only the arXiv metadata page; the HTML full text is `-html.full.md`).
**Source:** Piero Giacomelli, arXiv:2104.06491v2 [math.NT], Dec 2021, doi 10.48550/arXiv.2104.06491.

## What it is and why it matters to this run

The run's `p-adic-valuation-carry-dynamics` approach (the 2-adic valuation
`v_2(|a−b|)` carry cascade), and the REQUESTS row asking whether the
valuation/carry structure of the iterated absolute-difference map appears in
the p-adic/Ducci literature, previously had "NO source found". This paper and
its 2025 companion (Giacomelli 2025, `ducci-matrices-p-adic-context`) are the
closest the literature comes. They study a *p-adic-norm* Ducci operator, not
the integer absolute-difference map.

## What it establishes (the operator and its structure)

Define the p-adic Ducci operator on `(a_1,...,a_n) ∈ Q_p^n` by componentwise
`D_p(a_1,...,a_n) = (|a_1−a_2|_p, ..., |a_n−a_1|_p)` where
`|x|_p = 1/p^{ord_p(x)}`. Outputs are always powers of p (or 0).

- **Linearity:** `D_p(0)=0`, and `D_p(a·α) = a·D_p(α)` for `a ∈ Q_p`.
- **Lemma 1:** if the seed `α ∈ Z_p^n` (p-adic integers), the p-adic Ducci
  sequence is the null sequence with period 1 (all terms eventually 0).
- **Lemma 2:** every p-adic Ducci sequence is ultimately periodic (bounded in
  `P^n`, pigeonhole).
- **Mod-2 reduction (the part relevant to this run):** `|a_i − a_{i+1}|_p ≡
  a_i + a_{i+1} (mod 2)` when entries are powers of p (or 0), and the ultrametric
  law `|x−y|_p = max(|x|_p,|y|_p)` for `x≠y`, `0` for `x=y`. Hence the p-adic
  dynamics reduce to the mod-2/𝔽₂ level, and for `n` a power of 2 the sequence
  reaches 0 in finitely many steps.

## Why it does NOT close the run's REQUESTS row

This is the p-adic *norm* operator, whose output is a power of p, applied to
tuples over `Q_p`. It is **not** the integer absolute-difference map
`|a−b|` (integer output, carries through `|a−b|`). The run's open question is
the exact 2-adic valuation law of integer `|a−b|` iterated — whether
`v_2(|a−b|) ≥ min(v_2 a, v_2 b)` with equality/carry structure — which does
**not** appear here. What this paper independently corroborates is the same
mod-2/𝔽₂ level the run already proved (Rule-90 interior), from a different
angle. The `p-adic-valuation-carry-dynamics` direction remains the run's own,
unproved, with this paper recorded as the closest external treatment found.

```claim
id: giacomelli-2021-padic-ducci-mod2-reduction
statement: The p-adic-norm Ducci operator D_p(a_i)=|a_i−a_{i+1}|_p on Q_p^n outputs powers of p, is linear (D_p(a·α)=a·D_p(α)), maps integer seeds to the null sequence (Lemma 1), is ultimately periodic (Lemma 2), and reduces mod 2 to the 𝔽_2 level via |x−y|_p ≡ x+y (mod 2): for n a power of 2 it reaches 0 in finitely many steps.
hypotheses: D_p uses the p-adic norm |x|_p = p^{−ord_p(x)}; tuples over Q_p; seed in Z_p for Lemma 1.
holds-here: no — this is the p-adic-norm operator, not the integer absolute-difference map |a−b| with 2-adic carry that the run's p-adic-valuation-carry-dynamics approach needs. Its mod-2 reduction is the same 𝔽_2/Pascal level the run already proved.
status: asserted (abstracted from the primary text)
bearing: closes the "is the 2-adic carry structure of integer |a−b| in the literature?" request in the negative — the p-adic Ducci literature uses the norm operator and does not contain the run's carry law; the direction is the run's own.
anchor: research/sources/giacomelli-2021-p-adic-ducci-sequences-short-note-html.full.md
answers: p-adic-valuation-carry-direction-grounding
```
