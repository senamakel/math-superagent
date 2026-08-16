# Ilan Karpas, "Two Results on Union-Closed Families" — arXiv:1708.01434 (2017)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/1708.01434 (also arxiv.org/pdf/1708.01434).
> Full text: `research/sources/karpas-two-results-union-closed-2017.html.full.md`.

The paper behind the **large-family bound** in ROOT.md: UC holds once
`|ℱ|` is close enough to `2^n`.

## What it establishes

- **Result 1 (large families).** There is an absolute constant `c > 0` such
  that for any union-closed family `ℱ ⊆ 2^[n]`, if
  `|ℱ| ≥ (1/2 − c)·2^n`, then some element `i` appears in at least half the
  sets of `ℱ`. (I.e. UC holds — at the full `1/2` threshold — for families
  containing a density-`≥ (1/2−c)` fraction of the whole cube.)
- **Result 2.** For any union-closed family `ℱ ⊆ 2^[n]`, the number of sets not
  in `ℱ` that cover a set in `ℱ` is at most `2^{n−1}`; this is tight.
- The earlier large-family bound (Balla–Bollobás–Eccles, `|ℱ| ≥ (2/3)2^n`,
  per the primary source and survey Thm 30 — NOT `2^((3/2)n)`, which is a
  transcription error in ROOT.md / large-family-progression.md) is improved by
  Result 1 to `|ℱ| ≥ (1/2−c)2^n`.

## Hypotheses and holds-here

- `ℱ` finite union-closed. **Holds-here: yes.** This is the "large-family"
  settled class in ROOT.md, now sourced in body form.

## What it lets the run do

- The large-family regime (`|ℱ| ≥ (1/2−c)2^n`) is exactly settled at density
  `1/2`. Any minimal counterexample therefore has `|ℱ| < (1/2−c)2^n`, so it
  occupies a smallish fraction of the cube — a genuine structural constraint on
  a counterexample.

```claim
id: karpas-large-family-1-2
statement: There is c>0 such that any union-closed ℱ⊆2^[n] with
  |ℱ| ≥ (1/2−c)2^n has an element in at least half the sets (UC holds); and
  the number of non-members that cover a member is at most 2^{n−1}, tight.
hypotheses: ℱ finite union-closed
holds-here: yes
status: proved (in-paper)
bearing: large-family regime settled at density 1/2; a minimal counterexample
  must satisfy |ℱ| < (1/2−c)2^n
anchor: research/sources/karpas-two-results-union-closed-2017.html.full.md
```
