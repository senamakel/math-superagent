# Refutation: CA in degree 4 over F_3 is false — p=3 is a bad prime for n=4 (Hasse)

## What I attacked
The characteristic-p statement "CA holds in degree 4 over F_3", and the
characteristic-free reading of the run's `R-ca-two-roots` rung ("at most two
distinct roots forces a pure power"). Both are FALSE over F_3, and the same
polynomial witnesses both.

## The counterexample (checked by hand against the encoding)
Over F_3, f(x) = x^4 + x = x(x+1)^3  —  TWO distinct roots {0, 2 (= -1 mod 3)},
so it is NOT a pure power.

Hasse derivatives over F_3 (H_i(f) = sum_j C(j,i) c_j x^{j-i}):
  H_1 = x^3 + 1,   H_2 = 0 (identically: 6, 3, 3 vanish mod 3),   H_3 = x.

Values on F_3 = {0,1,2}:
  f  = x^4+x     : f(0)=0, f(1)=2, f(2)=0     ->  (c0, c2, c0)
  H1 = x^3+1     : H1(0)=1, H1(1)=2, H1(2)=0  ->  (c1, c2, c0)
  H2 = 0         : (c0, c0, c0)
  H3 = x         : (c0, c1, c2)

Hypothesis (CA for this f):
  - shares a root with H_1: X=2 (f(2)=0, H1(2)=0)  [hyp1]
  - shares a root with H_2: H2 is identically 0, so any root of f works, e.g. X=0  [hyp2]
  - shares a root with H_3: X=0 (f(0)=0, H3(0)=0)  [hyp3]

Conclusion (CA degree 4): f is a pure power of degree 4.  Over F_3 the pure
powers (x-a)^4 are:
  (x-0)^4 = x^4      : (c0, c1, c1)
  (x-1)^4            : (c1, c0, c1)
  (x-2)^4            : (c1, c1, c0)
f = (c0, c2, c0) is none of these (its value at c1 is 2, never 0 or 1).
=> counterexample.

## Engine result
`find_counterexample` on `code/refute/ca_deg4_char3.p` returned **refuted**
(CounterSatisfiable): the 3-element model with f=(c0,c2,c0), h1=(c1,c2,c0),
h2=(c0,c0,c0), h3=identity satisfies all three hypothesis axioms and
falsifies the pure-power conclusion.  I checked the model's tables against my
hand computation of x^4+x and its Hasse derivatives over F_3 — they agree
exactly.

## What this does and does not establish
- ESTABLISHES (char-p): p=3 is a BAD prime for degree 4 in the Hasse
  formulation, matching the published small-degree list {3,5,7} for n=4
  (Castryck et al. 2012 / de Jong-Draisma) and this run's own computed claim
  `badprimes-n4-minor-criterion-verified`.  It is a faithful, hand-verified
  confirmation of the run's established boundary at a NEW degree-4 witness.
- ESTABLISHES (char-free reading of R-ca-two-roots): the statement "a monic
  f sharing a root with every derivative and having at most 2 distinct roots
  is a pure power" is FALSE in char p — f = x^4+x = x(x+1)^3 over F_3 has
  exactly two distinct roots, satisfies the hypothesis, and is not a pure
  power.  This is exactly the kind of char-p falsification the run's hard
  constraint demands of every candidate argument.
- DOES NOT refute the char-0 rungs: `R-ca-deg4` and `R-ca-two-roots` are
  stated over Q / C (characteristic 0), where the centroid argument for the
  two-roots case is sound (see below) and where the literature already proves
  CA for ≤4 distinct roots (Laterveer-Ounaïes).  This counterexample lives in
  characteristic 3 and touches neither.

## Where the char-0 argument for R-ca-two-roots breaks in char p (located)
The run's proposed proof: f = (x-α)^m (x-β)^(n-m), take f^(n-1), which is
LINEAR with root equal to the centroid (mα + (n-m)β)/n; CA forces this
centroid to be a root of f, so it lies in {α,β}, forcing α=β.

This is correct in characteristic 0, where (n-1)! is invertible and f^(n-1)
is genuinely linear.  It breaks in char p exactly where f^(n-1) becomes
IDENTICALLY ZERO.  For the witness above, n=4 and p=3: f''' = 24x ≡ 0 mod 3
(and (n-1)! = 6 ≡ 0 mod 3), so "f^(n-1) is linear with root = centroid" is
meaningless over F_3 — there is no centroid to force into {α,β}.  The witness
x^p(x-1) (here x^4+x at p=3) is precisely the family on which the centroid
step dies.

## Honest verdict
`refuted` for the char-p statements; `not a counterexample` for (and hence
silent on) the char-0 conjectures R-ca-deg4 and R-ca-two-roots.  The result
is a faithful confirmation of the known bad-prime boundary at degree 4, with
an explicit witness that also, in one stroke, locates the char-p break of the
run's two-roots centroid argument.

```claim
id: deg4-char3-refuted
statement: CA in degree 4 over F_3 is false in the Hasse formulation: f =
  x^4 + x = x(x+1)^3 over F_3 has two distinct roots, shares a root with each
  Hasse derivative H_1=x^3+1, H_2=0, H_3=x, and is not a pure power.  Hence
  p=3 is a bad prime for n=4 (matching {3,5,7}), and the char-free reading of
  the two-distinct-roots rung ("2 roots sharing every derivative forces a
  pure power") is false in char p.
hypotheses: characteristic 3, degree 4, Hasse-derivative formulation of the
  char-p CA hypothesis
holds-here: this is the negative control the run's hard constraint requires
  for the char-p regime; it does NOT bear on the char-0 rungs R-ca-deg4 or
  R-ca-two-roots, which are stated over Q/C and remain open conjectures here.
status: checked (engine-refuted on code/refute/ca_deg4_char3.p; model tables
  verified by hand against x^4+x and its Hasse derivatives; agrees with the
  published n=4 bad-prime list {3,5,7} and the run's computed claim
  badprimes-n4-minor-criterion-verified)
anchor: code/refute/ca_deg4_char3.p
falsifies: a char-free argument for CA in degree 4, or for the two-roots rung,
  that never uses characteristic 0 (any such proves a false char-p statement).
```

## Relation to the two-roots rung (R-ca-two-roots)
In char 0 the two-roots rung is true (centroid argument sound; literature
proves CA for ≤4 distinct roots).  In char p it is false, and this note gives
the explicit witness x^4+x over F_3 (n=4, p=3) plus the precise step that
breaks: f^(n-1) = f''' vanishes identically because (n-1)! = 6 ≡ 0 mod 3.
This is the char-p test the rung's own "merge" step (allow a third root) will
have to keep from being silently reused.
