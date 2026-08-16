# Refutation: CA in degree 4 over F_5 is false — p=5 is a bad prime for n=4 (Hasse)

## What I attacked
The characteristic-p statement "CA holds in degree 4 over F_5", i.e. the
claim that a monic quartic over F_5 sharing a root with each Hasse derivative
H_1, H_2, H_3 is necessarily a pure power. This is FALSE.

## The counterexample (checked by hand against the encoding)
Over F_5, f(x) = x^4 − x^2 = x^2 (x−1)(x+1), THREE distinct roots {0, 1, 4},
so it is NOT a pure power.

Hasse derivatives over F_5 (H_i(f) = sum_j C(j,i) c_j x^{j−i}):
  H_1 = x(4x^2 + 3)   (from f = x^4 + 0·x^3 − x^2: H_1 = 4x^3 − 2x = 4x^3 + 3x)
  H_2 = x^2 + 4       (C(4,2)=6=1 → x^2, C(2,2)=1 → −1=4)
  H_3 = 4x            (C(4,3)=4 → 4x)

Values on F_5 = {c0=0, c1=1, c2=2, c3=3, c4=4}:
  f   = x^4−x^2   : f(0)=0, f(1)=0, f(2)=2, f(3)=2, f(4)=0  ->  (c0,c0,c2,c2,c0)
  H_1 = 4x^3+3x   : H1(0)=0, H1(1)=2, H1(2)=3, H1(3)=2, H1(4)=3  -> (c0,c2,c3,c2,c3)
  H_2 = x^2+4     : H2(0)=4, H2(1)=0, H2(2)=3, H2(3)=3, H2(4)=0  -> (c4,c0,c3,c3,c0)
  H_3 = 4x        : H3(0)=0, H3(1)=4, H3(2)=3, H3(3)=2, H3(4)=1  -> (c0,c4,c3,c2,c1)

(All arithmetic mod 5, checked: H1(2)=4·8+6=32+6=38=3, H1(3)=4·27+9=108+9=117=2,
H1(4)=4·64+12=256+12=268=3.)

Hypothesis (CA for this f), none vacuous (no H_i is identically zero):
  - shares a root with H_1: X=0 (f(0)=0, H1(0)=0)
  - shares a root with H_2: X=1 (f(1)=0, H2(1)=0), also X=4
  - shares a root with H_3: X=0 (f(0)=0, H3(0)=0)

Conclusion (CA degree 4): f is a pure power of degree 4. Over F_5 the pure
powers (x−a)^4 are exactly the 5 vectors that take value 1 at every nonzero
input and 0 at a (Fermat: t^4 = 1 for t ≠ 0 mod 5):
  a=0:(c0,c1,c1,c1,c1) a=1:(c1,c0,c1,c1,c1) a=2:(c1,c1,c0,c1,c1)
  a=3:(c1,c1,c1,c0,c1) a=4:(c1,c1,c1,c1,c0)
f = (c0,c0,c2,c2,c0) is none of these (it takes value 2, which no pure power
over F_5 ever does).  => counterexample over F_5.

## Engine result
`find_counterexample` on `code/refute/ca_deg4_char5.p` returned **refuted**
(CounterSatisfiable). After adding all 10 pairwise-distinct axioms for
c0..c4, the solver produced a 5-element model whose function tables match my
hand computation of x^4−x^2 and its Hasse derivatives exactly (I verified
every entry above).  The first run without the pairwise-distinct axioms let
the solver collapse the domain (c3=c2, c4=c1) to a 3-element quotient — still
a valid model of those axioms but not literally the F_5 field — so the
distinctness axioms are load-bearing for a faithful encoding.

## What this does and does not establish
- ESTABLISHES (char-p): p=5 is a BAD prime for degree 4 in the Hasse
  formulation.  This is an independent engine confirmation at a prime the
  refute folder had not previously exercised (it held only the p=3 witness for
  n=4), agreeing with the published n=4 list {3,5,7} (Castryck et al. 2012 /
  De Jong-Draisma), the run's `badprimes-n4-minor-criterion-verified` claim
  (lcm_T J_T = 1575 = 3^2·5^2·7 ⇒ 5 | J_T, so the reformulation's J_T
  prediction is faithful at this point), and the ordinary/Hasse scheme runs.
- ESTABLISHES (char-free break test): the two-distinct/three-distinct root
  rungs `R-ca-two-roots`, `R-ca-k-roots` are false outside characteristic 0 —
  this f has three distinct roots, satisfies the hypothesis, and is not a pure
  power.  The centroid argument that proves the char-0 two-roots rung divides
  by n and is char-0-specific; here n=4, p=5 (p < n is not the issue — the
  failure is intrinsic to the false char-p statement, as it must be).
- DOES NOT refute the char-0 rungs `R-ca-deg4` or `R-ca-two-roots`, which are
  stated over Q/C and remain open char-0 conjectures here.  This counterexample
  lives in characteristic 5 and touches neither.

## Honest verdict
`refuted` for "CA holds in degree 4 over F_5"; `not a counterexample` for (and
hence silent on) the char-0 conjectures.  The value is a verified
hand-and-engine-checked char-p witness at a fresh prime that corroborates the
run's bad-prime boundary for n=4 and the faithfulness of the J_T
reformulation at p=5.

```claim
id: deg4-char5-refuted
statement: CA in degree 4 over F_5 is false in the Hasse-derivative
  formulation: f = x^4 − x^2 = x^2(x−1)(x+1) has three distinct roots, shares
  a root with each Hasse derivative H_1=x(4x^2+3), H_2=x^2+4, H_3=4x (none
  identically zero), and is not a pure power.  Hence p=5 is a bad prime for
  n=4, matching the published list {3,5,7} and the run's J_T criterion
  (lcm_T J_T = 1575 = 3^2·5^2·7).  The char-free reading of the k-distinct-
  roots rungs (k<=3) is false in char p.
hypotheses: characteristic 5, degree 4, Hasse-derivative formulation of the
  char-p CA hypothesis
holds-here: this is the negative control the run's hard constraint requires
  for the char-p regime; it does NOT bear on the char-0 rungs R-ca-deg4 or
  R-ca-two-roots, which are stated over Q/C and remain open here.
status: checked (engine-refuted on code/refute/ca_deg4_char5.p; the 5-element
  model's f, H_1, H_2, H_3 tables verified entry-by-entry by hand against
  x^4−x^2 over F_5; agrees with the n=4 bad-prime list {3,5,7} and the run's
  computed claim badprimes-n4-minor-criterion-verified via 5 | 1575)
anchor: code/refute/ca_deg4_char5.p
falsifies: a char-free argument for CA in degree 4, or for the k-distinct-roots
  rungs that never uses characteristic 0 (any such proves a false char-p
  statement).
```

## Relation to the run's commitments
This is not a new degree or a refutation of any char-0 claim: it is a fresh,
independently engine-verified char-p witness at p=5 for n=4.  It strengthens
the evidence that the refuter's TPTP encoding pipeline is faithful (the model
came back exactly equal to the hand computation once the field-distinctness
axioms were added), and it corroborates the reformulation's claim that the
entire char-0 content is carried by J_T ≠ 0, since the prime divisors of the
n=4 lcm J_T = 1575 = {3,5,7} are exactly the degrees-4 bad primes.
