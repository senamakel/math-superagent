# Thread: Cassels divisibility `q | x, p | y` for the both-odd case

The load-bearing first rung of the both-odd-prime chain for
`x^p - y^q = 1`. The valuation machinery that reduces it to a
unit-group/ideal-power argument is now `checked` in this run; the
argument itself is not yet completed in-workspace.

```thread
question: Can the run turn the (now checked) valuation and cyclotomic
  coprimality facts into a full in-workspace proof that a solution of
  x^p - y^q = 1 with p, q distinct odd primes has q | x and p | y?
status: open — input machinery verified, concluding unit/ideal-power step not done
rests-on: cassels-valuation-lte-and-cyclotomic, valuation-identity-xp-1,
  faktor-pairwise-coprime-off-ramified, zeta-p-ring-and-ramification,
  lifting-the-exponent, fermat-little-theorem
blocked-by: none in the technique tier; the concluding step needs the
  ideal-power-to-element-power promotion in Q(zeta_p) (and mirror in
  Q(zeta_q)) that the class-group/Stickelberger machinery supports but
  the valuation note does not carry out.
next: >
  Write the ideal-power step: from y^q = prod_{i=0}^{p-1}(x - zeta_p^i)
  with the factors pairwise coprime off (1-zeta_p), each (x-zeta_p^i) is a
  q-th power of an ideal away from the ramified prime; compare q-th-power
  valuations at primes over other rational primes to force p | y, and mirror
  in Q(zeta_q) for q | x. Verify the divisibility q|x, p|y numerically
  against check_conditions / a small (p,q,x,y) oracle first so the lemma
  state "where the known solution sits" is explicit (known solution has
  p=2, excluded by hypothesis, and happens to satisfy q|x=3|3, p|y=2|2).
```

Why this direction matters: it is the first rung every both-odd argument
(Cassels → double-Wieferich → class-group descent) rests on, and its
valuation/cyclotomic prerequisites are now the best-verified part of the
library. The next rung (double-Wieferich congruences) is currently only
`reconstructed/heuristic` because the primary Cassels/Mihailescu texts are
screened; a self-contained proof of `q|x, p|y` here would upgrade that too.

## Relation to the known solution (falsifier)

The known solution `(3,2,2,3) = 3^2 - 2^3 = 1` has `p = 2` even, so it sits
outside the "p, q odd" hypothesis of this lemma. The conclusion `q|x = 3|3`
and `p|y = 2|2` happens to hold there; the lemma is excluded-by-hypothesis,
not refuted. Any completed proof must state this placement explicitly.
