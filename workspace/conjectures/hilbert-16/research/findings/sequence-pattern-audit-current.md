# Current exact sequence audit

Executed `python code/sequence_current_patterns.py` on the computed Bautin monomial counts
`a=[4,30,97,236,485,890,1505]` and complements `c=[7,10,16,23,31,40,50]`.

Exact results: neither sequence is a low-degree polynomial over supplied terms; exact
constant-coefficient recurrence search finds none of order <=6 for either sequence. OEIS
lookup finds no match for either sequence. The complement formula
`c=(h^2+14h+8)/8`, h=d-2, holds for h=4,6,...,14 and fails at h=2 (actual 7 versus
predicted 5). The first not-yet-computed test term for that conjecture is h=16 (d=18).
No new regularity is supported. This is provisional because no derivation exists.
