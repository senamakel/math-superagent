# Mason–Stothers (polynomial abc) via the Wronskian

```approach
idea: Mason–Stothers theorem (the polynomial abc conjecture, proved by Stothers 1981 and
      Mason 1984): for coprime A, B, C over an algebraically closed char-0 field with
      A + B = C, one has max(deg A, deg B, deg C) ≤ deg rad(ABC) − 1. Apply it to the
      derivative identity A + B = C that defines each common root of f and H_i(f).
mechanism: A common root r of f and H_i(f) is exactly a common zero of the coprime parts,
      and the Wronskian W_i = f·H_i' − H_i·f' vanishes at r; more strongly, gcd(f, H_i f) ≠ 1
      means f and H_i f share a factor, so writing A = f/…, B = −H_i f/…, C = W_i/… over the
      radical gcd makes A + B = C with deg rad(ABC) forced *small* by the shared roots. The
      n−1 conditions (one per i) impose n−1 separate abc inequalities; summing them against
      deg rad(f·H_i f) ≤ (number of distinct roots involved) gives a degree inequality that a
      non-pure-power f can only satisfy if the radical is large — a contradiction unless f is
      a power, or a new bound on how many distinct roots a counterexample can have.
status: refuted
killed-by: refuted on paper. The additive triple Mason-Stothers consumes does not exist: A = f/rad, B = -H_i f/rad give A + B = f(1-H_i)/rad, which is not C = W_i/rad (W_i = f H_i' - H_i f'). The needed identity f(1-H_i) = W_i is false in general (f = x^2-1, i = 1: (x^2-1)(1-2x) != (x^2-1)*2 - (2x)^2). W_i is a bilinear Wronskian with no additive companion, so there is no abc inequality to sum; the char-p separability story is downstream of an additive identity that never materialises. No first-step computation is worth running — the guard-set calibration would only re-confirm f(1-H_i) != W_i.
first-step: Symbolically (sympy, exact) verify the Wronskian/abc bookkeeping on the oracle's
      guard set: for f = (x−1)^n compute each W_i = f·H_i' − H_i·f' and confirm the Mason
      bound deg ≤ deg rad − 1 is *sharpened* to equality by the shared root, while for the
      char-p witness x^{p+1}−x^p locate exactly which term of the inequality fails in char p.
      This is the calibration that says whether the inequality is tight enough to force anything.
```

## What is established vs. what is speculation

- **Established (proved theorem, source to confirm):** the Mason–Stothers theorem, and the
  elementary fact that `deg rad(A B C)` is controlled by the number of distinct roots when
  `A, B` are the coprime parts of `f` and `H_i f` divided by their radical gcd. The
  Wronskian identity `f·H_i' − H_i·f' = f²·(H_i/f)'` is a differential-algebra identity,
  no speculation.
- **Speculation (mine, to be attacked):** that the n−1 inequalities jointly force
  `f = (x−a)^n`. This is the part with no source; Mason–Stothers has, to the run's
  knowledge, *not* been applied to CA.

## Char-`p` break (mandatory)

Mason–Stothers is a char-0 statement: in characteristic `p` the ordinary derivative
kills `x^p`-factors, the gcd/radical bookkeeping collapses, and the witness
`x^{p+1} − x^p` violates the clean inequality — so the argument *must* break at the step
`deg rad(f·H_i f)` controls `deg W_i`, which is where char `p` derivatives vanish. The
Hasse convention (already in `lib.casas_alvero.is_ca_hasse`) is the right object to
stress-test this break against, reusing the run's hasse-vs-ordinary resolution.

## Why it is not a restatement of a closed approach

None of the closed approaches is an *inequality theorem on radicals*. The resultant/
Gröbner routes are about ideals and regular sequences; the apolarity route is about
catalecticant minors; tropical about the fan. Mason–Stothers is a completely different
engine: a sharp degree inequality whose rigidity, when it bites, is exactly the kind of
structural fact GOAL.md point 3 wants (a bound on distinct roots of a counterexample).

## Honest likely output

Most likely a new *restricted class*: CA under the hypothesis that the shared roots
`r_1,…,r_{n−1}` are distinct (or few) — where Mason's bound is strongest — plus a sharp
lower bound on the number of distinct roots of any counterexample. A full proof is not
expected; a sharpened minimal-counterexample constraint is the deliverable.
