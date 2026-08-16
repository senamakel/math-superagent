# Large-family regime — settled threshold progression (structured claims)

```claim
id: large-family-progression
statement: Frankl's conjecture is settled for union-closed families F ⊆ 2^[n]
  that are large, with a progression of thresholds: |F| ≥ 2^n − 2^{n/2}
  (Czédli); |F| ≥ (2/3)·2^n (Balla–Bollobás–Eccles, JCTA 2012, per the
  primary source and survey Thm 30); |F| ≥ (2/3 − 1/104)·2^n (Eccles 2015);
  and |F| ≥ 2^{n−1} (Karpas, arXiv:1708.01434, Theorem 1.2, via Boolean
  analysis). At these thresholds some element is in at least |F|/2 sets.
hypotheses: F union-closed subset of 2^[n], |F| above the stated threshold.
holds-here: true
status: sourced (BBE JCTA 10.1016/j.jcta.2012.10.005; Eccles arXiv:1311.2298
  CP&C 25(3):399-418, 2016; Karpas arXiv:1708.01434; restated in the
  Bruhn–Schaudt survey)
bearing: the "large families" settled class, with the exact modern threshold
  |F| ≥ 2^{n−1} due to Karpas. A counterexample thus has |F| < 2^{n−1}.
anchor: Karpas Theorem 1.2 (already in library);
  Eccles arXiv:1311.2298 (research/sources/eccles-stability-result-2015-html.full.md)
```

## Correction note (librarian, this run)

The status/anchor previously cited Eccles as **arXiv:1210.2044**. That ID is
**wrong** — it is Brackx–De Bie–De Schepper's Clifford harmonic-potentials
paper. The correct Eccles full body is arXiv:1311.2298, downloaded and
indexed at `research/sources/eccles-stability-result-2015-html.full.md`
(and `-ar5iv.full.md`). The wrong-number file
`research/sources/eccles-stability-result-2015.full.md` now carries a loud
defective marker so nobody reads the Clifford paper as Eccles. See
`research/summaries/eccles-stability-result-2015.md` for the full corrected
claim and the explicit c₁≥1/24, c₂≥1/104.
