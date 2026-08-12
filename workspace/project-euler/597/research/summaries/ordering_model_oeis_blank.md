# OEIS lookup result: pure-bump ORDERING-MODEL even-parity counts

Terms searched: 1, 2, 13, 67, 349, 2459, 20205 (n=2..8)

These are the exact numbers of speed-ORDERINGS (out of n!) whose pure-bump
(no-finish) race gives an even-permutation final order. A program computed them
exactly: code/ordering_model_seq.py. Fractions: 1/2, 1/3, 13/24, 67/120,
349/720, 2459/5040, 449/896.

## Result: NO OEIS ENTRY matches. (blank — recorded as a dead thread)

## CRITICAL CAVEAT
This MODEL is REFUTED as an exact description of the torpids race:
- it gives p(3,inf)=1/3, p(4,inf)=13/24, p(5,inf)=67/120 ...
- the TRUE large-L limits are p(2,inf)=1/2, p(3,inf)=7/18, p(4,inf)=19/36
  (exact, from verified closed forms), MC 0.532/0.485 for n=5/6.
Magnitudes matter, not just the speed order (CONTEXT.md "pure-bump-ordering-count
model REFUTED"). These counts were catalogued only as an exact mathematical
sequence; they must NEVER be used as a proxy for p(n,L).
