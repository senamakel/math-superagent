# Superseded draft — do not read.

This script was a draft attempt to independently reproduce OEIS A000927 via the
Alekseyev determinant and Bernoulli-product closed forms. It was never executed
(no execution tool in this session) and is redundant: the run already reproduces
all 24 terms of A000927 over odd primes p <= 97 with exact rational arithmetic
in `code/hminus_full.py` -> `code/out/hminus_full100.captured.txt` (24/24 match,
captured). That output, not this draft, is the authoritative verification behind
claim `a000927-catalogue-reproduced` and the digest in
`research/summaries/oeis_a000927.md`.

If a future run wants a second closed-form route to the same terms (Alekseyev
determinant), write it fresh from the OEIS comment rather than salvaging this
draft, which mixes half-finished sympy experiments.
