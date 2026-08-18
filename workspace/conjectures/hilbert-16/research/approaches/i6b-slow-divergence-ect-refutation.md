# ECT attack: four second-type Dulac maps and vanishing slow divergence

```approach
slug: i6b-slow-divergence-ect-refutation
status: unresolved-obstruction
complexity_class: polynomial
oracle_bound: symbolic two-function failure modes (not the dynamical family)
```

## Refutation result

The adopted implication is false as a matter of logic:

> each of four passage contributions has Chebyshev/ECT behavior
> ⇒ their summed displacement is a finite-dimensional ECT family.

The exact oracle `code/refute/i6b_ect_failure_modes.py` was executed and its
capture is `code/out/i6b_ect_failure_modes.captured.txt`. It checks
`W(1,x)=1` and `W(-1,-x)=-1`, while the summed family is `(0,0)` and has zero
Wronskian. It also checks the parameter family `(a,a x)`, whose Wronskian is
`a^2`; on the vanishing stratum `a=0` the rank collapses exactly. This is an
exact symbolic counterexample to the inference, not a dynamical
counterexample to H^3_14 or I^1_6b.

The pre-existing four-passage iterated-log toy independently gives
`W3=0` (`code/out/i6b_second_type_toy.captured.txt`), but is deliberately not
the RR transition system. It reinforces, rather than repairs, the logical
failure.

## Why this hits the actual open graphic

RR 2015 explicitly distinguishes second-type maps and says its proof only
needs first-type maps (`research/sources/rousseau-shan-zhu-2015-second-type-dulac-full.full.md`, §2.6). The held audit therefore has no source-backed formula for the
four H^3_14/I^1_6b endpoint germs, no common remainder class, and no
parameter-uniform Wronskian statement. The known boundary calculation does
not supply these missing hypotheses for the full displacement.

The vanishing slow-divergence locus is load-bearing: even if a generic
stratum yielded a finite ECT family, its Wronskian can vanish when the leading
slow-divergence coefficient vanishes. At that locus one must either (a)
stratify and replace the basis by higher-order terms, proving finite type on
every stratum, or (b) work in a larger quasianalytic/transseries module with a
rank/zero theorem stable under specialization. Neither result is currently
in the artifacts or sources.

## Verdict and precise unresolved lemma

**Undecided, not refuted dynamically.** The proposed ECT shortcut is refuted;
finite cyclicity of the actual open graphic remains undecided. The missing
lemma is:

*For the exact RR blow-up of the chosen graphic, derive all four second-type
Dulac maps, identify a parameter-uniform analytic/quasianalytic function
module containing their sum, and prove a zero bound on every slow-divergence
stratum, including the identically-zero stratum.*

A generic Wronskian computation cannot establish this: the oracle shows that
specialization can reduce rank. The existing source-backed first-type formulas
cannot be transferred to the second-type endpoints. This also satisfies the
smooth test warning: formal power/log expansions without a controlled
remainder class do not yield a zero theorem.

## What would falsify this obstruction

A faithful RR-coordinate derivation showing that the four maps share a fixed
ECT basis whose Wronskians remain nonzero after every vanishing-stratum
specialization would defeat the present objection. Conversely, an exact
second-type specialization with two proportional leading terms and an
uncontrolled next-order remainder would turn this unresolved obstruction into
a genuine failure of the finite-ECT route.
