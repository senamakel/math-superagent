# Research requests — what this run needs and has not found

Open rows are gaps other roles walked into and stated precisely. Work the rows
before inventing new queries. `falsifies` says what a source would have to
settle to be useful.

| Need | Why | Falsifies | Status |
| --- | --- | --- | --- |
| Frei 1978 full text, "Über unitar perfekte Zahlen", Elem. Math. 33 (1978) 95–96 | The OEIS statement (a UPN not divisible by 3 needs m ≥ 144, ω ≥ 144, n > 10^440) is load-bearing for "is 3 \| n forced?" and is only OEIS-recorded, not primary-verified | A weaker or corrected bound; or a counterexample UPN not divisible by 3 below those bounds would refute the OEIS claim | OPEN — captcha-walled at e-periodica; no alternate source located |
| Goto 2007 full text, RMJM 37 (2007) 1557–1576 | The OEIS-recorded bound m < 2^(2^k) for ω(m) = k is used as a finiteness-adjacent constraint; primary verification wanted | A counterexample to the upper bound | OPEN — paywalled at Project Euclid; MaRDI item + Goto publication list held (bibliographic only) |
| Wall's 10^102 search bound primary statement | GOAL.md and both notes carry "Wall searched past 10^102" as a literature fact | A different stated search bound | RESOLVED — the held Wall 1975 primary text contains NO 10^102; actual bound N < W ≈ 1.46e23. 10^102 is an orphan claim; see research/notes/wall-1975-bounds-and-102-claim.md |
| Primary source for the supplementary law of biquadratic reciprocity `(1+i/π)_4`, `(i/π)_4`, `[2/π]=i^{-b/2}` | The adopted second-moment-character-mod16 approach evaluates the first moment S_χ = Σ_{r\|Φ_{4p}(2)}(2/r)_4 via quartic reciprocity in Z[i]; these laws were previously held only as asserted-from-Wikipedia | A primary statement that differs from the Wikipedia formulas | RESOLVED — Williams (1976) Proc. AMS 59:19-22 held and digested at research/summaries/williams-1976-supplement-biquadratic-reciprocity.md; a numerical check (code/verify_biquadratic_supplement.py) is staged to confirm [2/π]=i^{-b/2} from the primary anchors |
| Wall 1975 full text ("The fifth unitary perfect number", CMB 18 (1975) 115–122) | Primary proof that W is the next UPN after 87360 | A different factorization or missed smaller UPN | RESOLVED — held at research/sources/wall-1975-fifth-unitary-perfect-number-pdf.full.md |
