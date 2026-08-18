# Sequence audit rerun

Executed `python code/sequence_extract_rerun.py` on exact computed Bautin focal-value monomial counts
`a=[4,30,97,236,485,890,1505]`, with degrees `d=4,6,...,16`, and complements
`c=[7,10,16,23,31,40,50]`, where `c=binomial(h+4,4)-2a` and `h=d-2`.

The formula `c(h)=(h^2+14h+8)/8` matches exactly at `h=4,6,8,10,12,14`, but fails at `h=2` (actual 7, formula 5). Its first uncomputed falsifier is `h=16` (`d=18`), predicting `c=61` and `a=2392`.

Exact sequence-tool checks: neither sequence has a constant-coefficient recurrence of order <=6 over all seven supplied terms; `analyze_sequence` finds no low-degree polynomial for either. OEIS lookup found no match for either sequence. Existing d=18 computation stopped after degree 17, so the first falsifier remains uncomputed. No new regularity is established.