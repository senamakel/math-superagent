# The Entropy-2024 quadratic closed form H(n)=2(n−1)(4(n−1)−2) is refuted

```claim
id: h16-quadratic-closed-form-refuted
statement: The proposed closed form H(n) = 2(n−1)(4(n−1)−2) (da Silva–Vieira–Leonel, "Exploring limit cycles of differential equations through information geometry unveils the solution to Hilbert's 16th problem", Entropy 26(9), 2024) is FALSE. Buzzi–Novaes 2024 (arXiv:2411.09594) give four independent reasons: (a) the form is quadratic in n, contradicting the n² log n lower growth (Christopher–Lloyd 1995, Han–Li 2012: liminf H(n)/((n+2)²log(n+2)) ≥ 1/(2 log 2)); (b) an explicit sequence (Li–Chan–Chung 2002, correcting Christopher–Lloyd) gives H(2k−1) ≥ S_k = 4^{k−1}(k − 13/6) + (2k−1)/3, which exceeds the claimed form for k ≥ 35; (c) its "limit cycle via information geometry" definition (counting singularities of |R| for a Fisher-information scalar curvature R) is neither necessary nor sufficient for limit cycles — explicit polynomial systems demonstrate both failures; (d) counting singularities of |R| therefore cannot bound the number of limit cycles.
hypotheses: the Entropy-2024 claimed closed form; the definition of limit cycle via information-geometry scalar curvature R; the n² log n lower growth.
holds-here: yes (the refutation holds)
status: asserted-by-source
evidence: sourced-held — Buzzi–Novaes 2024 full text (research/sources/buzzi-novaes-claim-h16.full.md), summarized in research/summaries/buzzi-novaes-claim-h16.md. The information-geometry definition failure is separately recorded as claim h16-geometry-limitcycle-defn-refuted.
falsifier: A correction of the Entropy-2024 computation that survives Buzzi–Novaes' four objections, or a source showing one of the four reasons is wrong, would reopen the claim. The refutation itself is the current standing.
sources: https://arxiv.org/abs/2411.09594 ; https://doi.org/10.3390/e26090783 (Entropy 2024, refuted)
anchors: research/sources/buzzi-novaes-claim-h16.full.md; research/summaries/buzzi-novaes-claim-h16.md lines 12-28
note: This is the refuted quadratic upper bound — the concrete target of the n² log n lower-growth test. The phantom id `quadratic-upper-bound` cited in h16-hn-lower-bound-asymptotic's contradicts line was this claim, never written as a block; this block is that missing record.
follows-from:
answers:
```

## Why this claim block exists

`h16-hn-lower-bound-asymptotic`'s `contradicts:` line was prose ("a quadratic-upper-bound
claim (none held except the refuted one)") that the ledger parser split into phantom ids
`a`, `claim`, `quadratic-upper-bound`. The real object — the refuted Entropy-2024 closed
form — had no claim block. This block records it with its Buzzi–Novaes anchor.
