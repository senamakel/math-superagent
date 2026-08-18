# Refutation/obstruction: four second-type Dulac contributions and ECT

```claim
id: h16-i6b-four-passage-ect-obstruction
status: checked
```

## Exact target inspected
The proposed route is: after the RR blow-up for the open center graphic I¹₆b, express the full displacement as a sum/composition of four second-type Dulac contributions and infer a finite-dimensional ECT family from passage-wise Chebyshev behavior or from a first slow-divergence integral.

RR 2015 §2.6 explicitly defines second-type maps (from a section ȳ=ȳ₀ to r=r₀ or ρ=ρ₀) and then states that only first-type maps are needed in that paper. Its Theorem 2.3 is consequently not a formula for the four required endpoint germs. The paper's boundary results do not supply the missing full-graphic reduction.

## Checked algebraic obstruction
An ECT pair requires a nonzero 2×2 Wronskian. Exact symbolic computation gives p=(1,x), W(p)=1; q=(-1,-x), W(q)=-1; p+q=(0,0), W(p+q)=0; and f_a=(a,ax), W(f_a)=a², hence rank drops at a=0. This was executed by `code/refute/i6b_ect_symbolic_guard.py`; capture: `code/out/i6b_ect_symbolic_guard.captured.txt`. Existing exact toy probes independently find zero higher Wronskians for iterated-log/transseries surrogates. These are minimal algebraic counterexamples to the inference, not counterexamples to the quadratic vector field or to finite cyclicity.

## Precise missing hypotheses
The implication requires: exact four second-type Dulac expansions; a common parameter-uniform analytic/quasianalytic or Noetherian/transseries class closed under composition; non-cancellation and fixed rank including every vanishing slow-divergence stratum; and verified Wronskian/CT signs plus endpoint little-o conditions. None is established for I¹₆b. A slow-divergence integral is only a leading displacement term. If it vanishes, higher terms and the remainder control the zeros; finite jets or property-J/C^k asymptotics alone do not provide this control. The flat-term probe exp(-1/x)sin(1/x) is invisible to every finite jet but has infinitely many zeros accumulating at 0.

## Verdict
**Refuted:** the bare algebraic inference “four ECT-like passage contributions imply their sum is ECT.” **Undecided:** actual I¹₆b finite cyclicity. No faithful dynamical counterexample was found or claimed.

Search frame: exact symbolic affine pairs and bounded toy coefficient models; witness outside the dynamical model, so no published exhaustive dynamical regime is challenged.

Source: Rousseau–Shan–Zhu 2015, §2.6 and Theorem 2.3 (`research/sources/rousseau-shan-zhu-2015-second-type-dulac-full.full.md`); Huzak 2018 DF₂a precedent; GMV ECT criterion.
