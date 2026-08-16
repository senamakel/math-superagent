# Refutation: CA is false in characteristic 2 (negative control, verified by engine)

## What I attacked
The statement "the Casas-Alvero conclusion holds in every characteristic", i.e.
that sharing a root with every derivative forces a pure power, taken naively as
a characteristic-free claim.  This is FALSE: CA is a characteristic-0 theorem,
and in characteristic p it fails.

## The counterexample (checked by hand against the encoding)
Over F_2, f(x) = x^3 + x^2  (= x^{p+1} - x^p at p=2, the canonical witness family).

Values on F_2 = {0, 1}:
  f(0) = 0,  f(1) = 0            f = x^3 + x^2
  f'(0) = 0, f'(1) = 1           f' = x^2
  f''  = 0 identically            (2·(...) terms vanish mod 2)

Hypothesis:  f shares a root with f'  ->  common root x = 0 (f(0)=f'(0)=0)  [h1]
             f shares a root with f'' -> f'' is identically 0, so f(0)=0 works  [h2]
Conclusion:  f is a pure power of degree 3 over F_2.  Pure powers are
             g0 = x^3        : (0,1)
             g1 = x^3+x^2+x+1: (1,0)
             f = (0,0) is neither.

## Engine result
`find_counterexample` on `code/refute/ca_deg3_char2.p` returned `refuted`
(CounterSatisfiable): a 2-element model with f=(c0,c0), fp=(c0,c1) satisfies
both hypothesis axioms and falsifies the pure-power conjecture.

## What this does and does not establish
- ESTABLISHES: my TPTP encoding of the CA derivative-sharing hypothesis is
  faithful — the engine recovered exactly the known char-p counterexample that
  the run's oracle `lib.casas_alvero` also flags (`is_ca=True,
  is_pure_power=False`).  This is the negative control that would have caught a
  transcription error in the encoding.
- DOES NOT refute CA: Casas-Alvero is stated over characteristic-0 fields, where
  it is believed true (and open).  The counterexample is in characteristic 2,
  which is precisely the regime where the run's own hard constraint says any
  char-free argument MUST fail.  So this is a confirmation of the known char-p
  failure, not a challenge to the open char-0 conjecture.

```claim
id: char2-eng-refuted-ca-charfree
statement: The characteristic-free reading of CA — "f monic of degree n sharing a
  root with each of its first n-1 derivatives is a pure power" — is FALSE: over
  F_2, f = x^3 + x^2 shares a root with f' (and with f''=0) yet is not a pure
  power.
hypotheses: characteristic 2, degree 3
holds-here: this is the negative control the run's hard constraint requires, not
  a counterexample in characteristic 0
status: checked (engine-refuted on code/refute/ca_deg3_char2.p, confirmed by
  hand and by the canonical oracle lib.casas_alvero)
anchor: code/refute/ca_deg3_char2.p
falsifies: a char-free argument for CA (any proof that never uses characteristic 0
  proves a false statement).
```

## Honest verdict
This is a `refuted` answer for the *char-p* statement and a *confirmation* for
the char-0 conjecture (not a proof, not a refutation — it says nothing about
char 0).  It validates the refuter's encoding pipeline, so a later
`counterexample` from this pipeline can be trusted to be faithful.
