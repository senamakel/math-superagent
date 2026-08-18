# Reduction attack record

## Restatement and theory

For a rational convergent slope `a=p/q`, the mechanical digits are
`d_j=floor(x+(j+1)a)-floor(x+ja)`, and the decimal value is
`v=sum_{j=0}^{k-1} d_j 10^(k-1-j)`.  The proposed primitive evaluates moments
of `floor((p i+q)/r)` with weight `z^i`, `i=0..n-1`; this is the finite-difference
telescoping identity plus the universal-Euclidean monoid.  The attack checks
exactly those index conventions, rather than enumerating the target bound.

The naive direct moment loop is an exponential/oracle-style bounded check only;
`oracle_bound` is `k<=80` (and `n<25` for the moment grid).  The proposed
algorithm itself is logarithmic in the Euclidean recursion and is not replaced
by this oracle.

## Executed artifact

`code/refute/attack_reduction_counterexample.py` was written as the executable
attack.  It was not executable in this tool environment (no shell/program-run
tool was available), so no output is claimed.  This is an honest unverified
artifact, not evidence of a pass or failure.

## Hand attack / smallest boundary cases

The zero-length case must return the identity (`S0=S1=S2=dR=dU=0`), and the
one-term case must use weight `z^0=1`.  The documented `ue0` transformation is
exact: `floor((p i+q)/r)=floor((p(i+1)+(q-p))/r)`, with a constant intercept lift
and corresponding first/second-moment shift.  Thus an unchanged intercept or
weight `z^(i+1)` is the likely failure mode, not the already-tested monoid
composition.

A deliberately shifted decimal exponent is visibly wrong at `k=1`: the unique
one-digit value is changed from `d_0` to `10 d_0`; hence any evaluator using
`10^(k-j)` instead of `10^(k-1-j)` fails immediately whenever the factor is `1`.
This is a counterexample to that *wrong variant*, not to the current documented
formula.

## Verdict

`undecided`: no counterexample to the current reduction was mechanically run in
this environment. Existing artifacts report the correct `ue0` mapping and
small-k indexing checks, but the full proposed reduction is still not present:
`code/out/solution_wiring.captured.txt` records a failure at `k=1` in an earlier
attempt before a boundary correction.  Approximant stability is documented only
through the mechanical construction at small k, not through a completed
full-size evaluator.  A larger run would settle whether the current wiring,
including all intercept aggregation, reproduces `Psi(10^4)` and `Psi(10^6)`;
scaling the bounded oracle alone would settle nothing new.
