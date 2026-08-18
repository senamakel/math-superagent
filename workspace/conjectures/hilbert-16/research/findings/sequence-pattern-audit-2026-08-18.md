# Exact sequence audit

The investigation-produced Bautin focal-value monomial counts are
`a=[4,30,97,236,485,890,1505]` for degrees `d=4,6,...,16`. With
`h=d-2`, full homogeneous degree-h monomial dimension in five variables is
`C(h+4,4)`, and the complement `c=dimension-2a` is
`[7,10,16,23,31,40,50]`.

Executed `python code/sequence_tool_run.py`, plus the exact sequence tools.
For both sequences, all reported difference and recurrence statements are exact
on the supplied terms. Neither has a constant-coefficient linear recurrence of
order <=6; neither has constant finite differences through the tested levels;
OEIS lookup found no match.

A conjectural regularity survives every supplied term with h=4,6,...,14:
`c(h)=(h^2+14h+8)/8`, equivalently
`a=(C(h+4,4)-c(h))/2`. It is not valid at h=2: c=7 while the formula gives 5,
so h=2 is exceptional. This is a conjecture, not a theorem. Its first
uncomputed falsifier is h=16 (d=18), predicting c=61 and a=2392. The earlier
signed-permutation involution explanation was exactly refuted by the existing
finite search.
