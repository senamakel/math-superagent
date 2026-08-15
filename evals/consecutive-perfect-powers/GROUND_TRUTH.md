# Ground truth — consecutive-perfect-powers

**This file must never enter the container.** It lives at the repository root,
outside `workspace/`, the only tree bind-mounted at `/workspace`. It is read by
`scripts/eval-report` on the host and by nothing else.

## What this problem really is

**Catalan's conjecture**, stated by Eugène Charles Catalan in 1844: `8` and `9`
are the only consecutive perfect powers.

The state of the art the seed freezes at is roughly **1999–2000**:

- **V. A. Lebesgue (1850)**: `x^p - y^2 = 1` has no solutions for odd `p`.
- **Ko Chao (1965)**: `x^2 - y^q = 1` has only `3^2 - 2^3` for `q` odd. Together
  with Lebesgue this closes both exponent-2 cases.
- **Robert Tijdeman (1976)**: the number of solutions is finite, with an
  **effective** bound from Baker's theory of linear forms in logarithms. The
  bound is around `exp(exp(exp(exp(730))))` in early forms — utterly
  unreachable.
- **Cassels (1960)**: the relations `p | y` and `q | x`, which are the structural
  conditions every later attack builds on.
- **Mihăilescu (2000)**: a solution forces the **double Wieferich** condition
  `p^{q-1} = 1 (mod q^2)` and `q^{p-1} = 1 (mod p^2)`. This drove the
  computational searches, which confirmed no second solution for exponents up
  to roughly `10^7`–`10^8`.

The seed's "strong necessary conditions ... of the shape `p^2` divides
`y^{p-1} - 1`" is the Cassels/double-Wieferich tier, stated without attribution.

## The solution being withheld

**Preda Mihăilescu, 2002**, "Primary cyclotomic units and a proof of Catalan's
conjecture", *Journal für die reine und angewandte Mathematik* (Crelle) 572
(2004), 167–195. Announced 2002.

The proof is entirely in cyclotomic fields and uses **no** computation and **no**
appeal to Baker's linear forms in logarithms — which was the surprise, since
every previous route went through effective bounds. The structure:

1. Reduce to `p, q` odd primes, using Lebesgue and Ko Chao.
2. Use Cassels' relations to get the ideal factorisation in `Z[zeta_p]`.
3. The heart: an argument about **primary cyclotomic units** and the
   `Z[G]`-module structure of the `p`-th cyclotomic field's class group, showing
   the minus part cannot accommodate the required relation. Uses Thaine's
   theorem and Stickelberger's theorem.
4. Separate treatment of the case `p = 1 (mod q)`.

Later simplified by Bilu, Metsänkylä and others.

## Why this problem is in the calibration set

It is the **deep machinery** test, and it is the one the harness is most likely
to fail informatively. Unlike the other two, there is no short idea and no
machine-checkable artifact: progress requires actually working in `Z[zeta_p]`,
which means the run must either drive a computer algebra system competently or
reason in prose about class groups — and the second is how a mathematically
confident model produces fluent nonsense.

So this problem measures whether the harness **knows what it does not know**:
whether `symbolic_math` gets used for the cyclotomic arithmetic, whether claims
about class numbers get labelled conditional, and whether the falsifier catches
the arguments that prove too much. A run that ends with "the exponent-2 cases
proved, Cassels' relations re-derived and verified, and a precise statement of
where the cyclotomic obstruction begins" is a **good** run. A run that ends with
a confident proof is almost certainly a failed one.

## De-naming assessment

**Weak.** `x^p - y^q = 1` is instantly recognisable to any model, and "8 and 9"
in the first paragraph makes it unmistakable. De-naming removes the string
"Catalan" from searches and nothing more.

Attribution therefore rests entirely on the **leakage audit** and on the
**ordering** in the trace. The discriminator: re-deriving Cassels' relations
from the ideal factorisation is derivation; stating `p | y` and `q | x` as known
facts before any factorisation appears is recall.

Note also that the seed itself is a strong hint by necessity — it names
cyclotomic fields and the class group as the obstruction, because that is where
the problem genuinely is and a seed that hid it would send the run to grind on
elementary factorisation for four hours. Score accordingly: reaching "the
obstruction is the class group" is worth little here, since the seed says it.
Reaching a *specific* module-theoretic statement about the minus part is worth a
great deal.

## Falsifiable checks for the audit

- `solutions(N)` must return exactly `(3,2,2,3)`. Any other output is a broken
  oracle, almost certainly floating-point.
- The double-Wieferich conditions must be satisfied by `(p,q) = (2,3)`:
  check `2^2 = 4 = 1 (mod 9)`? No — `4 != 1 (mod 9)`. The conditions are stated
  for **odd** primes and `(2,3)` is outside their hypothesis. **This is itself a
  trap worth watching**: a run that "calibrates" its condition checker on
  `(2,3)` and finds it fails may either correctly conclude the hypothesis
  excludes it, or incorrectly conclude the conditions are wrong. Which of those
  happens is a genuine signal about the run's care.
- Watch for these appearing before any derivation produced them: "Mihăilescu",
  "Catalan", "Cassels", "Tijdeman", "Wieferich", "Stickelberger", "Thaine",
  "primary cyclotomic units", or the assertion that the answer is `8, 9` only,
  stated as settled rather than as the conjecture.
