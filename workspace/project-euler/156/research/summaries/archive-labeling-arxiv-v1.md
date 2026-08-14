# Khovanova & Marton, "Archive Labeling Sequences" — arXiv v1 (25 Apr 2023)

**Source:** https://arxiv.org/pdf/2305.10357v1 . Full text: `[[archive-labeling-arxiv-v1.full]]` — `research/sources/archive-labeling-arxiv-v1.full.md`.

The first arXiv version of the paper that governs PE156. **Superseded for the run's purposes by v2** (`research/sources/archive-labeling-arxiv-latest.full.md`) and the published AMM version (`research/sources/archive-labeling-amm-published.full.md`): v1 lacks Section 9, so it does **not** contain Proposition 9.1 (the bound x ≤ d·b^b). It is kept on disk for provenance and because it contains the d=0 lemmas.

## What it establishes (that later versions also carry)

- **Setup:** the VHS-sticker puzzle and the Google Labs formulation (f(x) = number of 1s in 0..x; f(13)=6, f(1)=1; find next x with f(x)=x).
- **Lemma 5.1:** for any integer x > 10^10, f_0(x + 10^10) ≥ f_0(x) + 10^10 (any block of 10^10 consecutive numbers contains at least 10^10 zeroes). This is the lemma later converted to base b in the proof of Prop 9.1.
- **Theorem 5.2:** a_=(0) is not well-defined in base 10 — no n with f_0(n) = n. (Relevant to PE156 only as a negative: the problem's d ranges over 1..9, so the d=0 nonexistence does not affect the answer.)
- **Lemma 6.1:** if a_≥(0) > x and z(y) < x for some y > x, then a_≥(0) > y — the skip lemma, for d=0 (the general d>0 version is Lemma 7.1 of v2).

## What it does NOT contain

- No Section 9, so **no Proposition 9.1**, no general-base bound x ≤ d·b^b, no A226238/A165617 context, no Prop 9.3 (d=0 base bound). Anyone citing "the bound" must cite v2 or the AMM paper, not v1.

## Hypotheses and hold-here

- Lemma 5.1 and Thm 5.2 concern digit 0; PE156 uses d ∈ {1..9}, so they hold but are not load-bearing for the answer.

## Implication for this run

Do not use v1 as the source for the finite bound (G2). The bound's citable source is v2 Prop 9.1 / AMM §4. v1's value here is provenance and the d=0 negative result.

## Does not settle

Anything about the sum; nothing about digits 1..9 bounds (beyond the puzzle's d=1 case, which is not even bounded in v1 beyond existence).

```claim
id: km-v1-superseded
statement: arXiv:2305.10357v1 contains Lemma 5.1 (f_0(x+10^10) ≥ f_0(x)+10^10 for x>10^10), Theorem 5.2 (a_=(0) undefined in base 10), and Lemma 6.1 (skip lemma, d=0 form), but lacks Section 9 and therefore lacks Proposition 9.1's bound x ≤ d·b^b.
hypotheses: d=0 lemmas; decimal base for Thm 5.2.
holds-here: yes (as context; PE156's d ∈ {1..9} makes these non-load-bearing)
status: asserted (paper preprint)
bearing: v1 must not be cited for the finite search bound; cite v2/AMM instead. Confirms the d=0 no-solution result for completeness of the problem statement's d=1..9 range.
anchor: research/sources/archive-labeling-arxiv-v1.full.md
```
