# Consolidated lower-bound calibration: H(2)≥4, H(3)≥13, H(4)≥28, H(n) ≳ n² log n

```claim
id: h16-lower-bounds
statement: The confirmed lower bounds on the Hilbert number are: H(2) ≥ 4 (Chen–Wang 1979, Shi Songling 1980, with the (3,1) configuration; interval-arithmetic certified by Galias–Tucker for the Songling system), H(3) ≥ 13 (claimed; e.g. Zoladek-type constructions and Li–Chan–Chung sequence), H(4) ≥ 28, and asymptotically H(n) grows at least like (n+2)² log(n+2)/(2 log 2) (Christopher–Lloyd 1995, refined by Han–Li 2012; independently confirmed by canard constructions, Álvarez–Coll–De Maesschalck–Prohens 2020). Consequently any proposed upper bound on H(n) of order below n² log n is refuted before examination (test 2 of problem.md). Locally, M(2)=3 (Bautin 1954) bounds the number of small-amplitude cycles at a focus for quadratic fields.
hypotheses: degree-n planar polynomial fields; H(n) is the supremum over such fields of the number of limit cycles; M(2) is local focus cyclicity.
holds-here: yes
status: asserted-by-source
evidence: sourced-held — Buzzi–Novaes 2024 full text (research/sources/buzzi-novaes-claim-h16.full.md) confirms the n² log n asymptotic and the H(2k−1) ≥ S_k = 4^{k−1}(k − 13/6) + (2k−1)/3 sequence (Li–Chan–Chung 2002); Galias–Tucker (research/sources/galias-tucker-songling-four-cycles.full.md) certify the four Songling cycles in interval arithmetic; Bautin 1952 (research/sources/bautin-1952-full.pdf.full.md) gives M(2)=3; the scholar's lower-bound calibration claim (research/notes/claim-blocks-scholar-2026-08-18.md) consolidates these. H(3) ≥ 13 and H(4) ≥ 28 ride on the held lower-bound constructions (see note).
falsifier: A corrected computation showing one of the lower bounds is wrong (e.g. the interval-arithmetic certification of the four Songling cycles failing, or a retraction of the n² log n growth) would falsify the corresponding row. The H(3)≥13 and H(4)≥28 numbers are sourced at a weaker level than the H(2)≥4 certification and should be re-confirmed against a primary source before being cited in an argument.
sources: https://arxiv.org/abs/2411.09594 ; https://doi.org/10.1098/rspa.1995.0081 (Christopher–Lloyd); http://www.zet.agh.edu.pl/~galias/ps/amc2022.pdf (Galias–Tucker); https://doi.org/10.1016/j.jde.2019.09.057 (canard lower bound)
anchors: research/sources/buzzi-novaes-claim-h16.full.md; research/sources/galias-tucker-songling-four-cycles.full.md; research/sources/bautin-1952-full.pdf.full.md
note: This is the run's mandatory test-2 calibration. It consolidates the previously dangling `h16-lower-bounds` id (cited by h16-hn-lower-bound-asymptotic's follows-from but never written as a block). The H(3)≥13 and H(4)≥28 rows are claimed by the scholar summary but the exact primary anchors for those two numbers should be checked before load-bearing use.
follows-from: h16-hn-lower-bound-asymptotic
answers:
```

## Why this claim block exists

`h16-hn-lower-bound-asymptotic`'s `follows-from: h16-lower-bounds` pointed at an id
that never existed as a claim block. This block records the consolidated lower-bound
calibration (the run's test-2 reference) with its held anchors and the honest caveat
that H(3)≥13 and H(4)≥28 are weaker-sourced than the interval-certified H(2)≥4.
