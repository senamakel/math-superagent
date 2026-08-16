# OEIS lookup: the feasible-family vertex counts are not a catalogued sequence

An OEIS lookup on the five feasible members of the srg(v,k,1,2) family,
v ∈ {9, 99, 243, 6273, 494019}, returned **no match**. This is a finding, not a
dead end: the sequence is not catalogued, so no closed form is available from
OEIS.

The structure must come from the problem itself: k = u²+u+2 with
u ∈ {1, 3, 4, 10, 31} and v = 1 + k + k(k−2)/2
(Makhnev–Minakova classification, confirmed by this run's exact integrality
computation — see code/out/feasibility-candidates-corrected.md and claim
`integrality-five-members`). Recorded so nobody searches OEIS for it again.
