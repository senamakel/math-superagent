# Refutation note: I^1_6b four second-type passages and ECT reduction

**Status: refuted (the inference), not a dynamical counterexample.**

## Claim attacked
The adopted shortcut says that the exact displacement formed from the four second-type Dulac passages reduces to a finite-dimensional ECT-controlled family. Here the objects are the four Dulac maps, their regular transition compositions, the scalar displacement `L_ν`, and an ECT family (a family whose initial Wronskians are nonzero on the working interval).

## Theory and source check
Rousseau–Shan–Zhu 2015, §2.6, Theorem 2.3 (held at `research/sources/rousseau-shan-zhu-2015-second-type-dulac-full.full.md`, lines 147–208) gives, at rational resonances, a compensator term plus a remainder `φ_i`. Its stated control is an asymptotic bound and `C^{l-2}` regularity in generalized monomials; it is not a finite-dimensional ECT representation. The same source's proof at lines 335–355 uses property (I)/(J) and derivation–division for a specially normalized situation, not a general closure theorem for four independently composed passages.

## Executed oracle
The existing naive guard was checked first: `code/out/i6b_four_passage_oracle.captured.txt` reproduces all five worked examples. Existing exact diagnostics also show cancellation of two individually ECT pairs. Those are only logical toys and were not reused as the requested result.

I then ran `code/refute/i6b_transseries_counterexample.py`; the capture is `code/out/i6b_transseries_counterexample.captured.txt`. At the resonant value `a=0`, set

`ω(x,0) = -log x`, `R(x)=exp(-1/x) sin(1/x)`,

and compare the finite compensator truncation `T=x` with the exact symbolic germ `D=x+R`. The program computed exact limits of derivatives `R^(k)(x)` for `k=0,...,4` as `x→0+`, all zero, while checking five exact zeros `x=1/(nπ)`. Thus every tested finite jet agrees with the truncation at the boundary, but the remainder has infinitely many accumulating zeros. This is a counterexample to the logical implication “finite truncation/ECT data controls the exact displacement” under only flatness/asymptotic remainder control.

## Exact missing hypothesis
One must add either:

1. a parameter-uniform quasianalytic/Noetherian transseries class, closed under all four second-type Dulac maps and the regular transitions, with a proved zero-count/zero-transfer theorem; or
2. an explicit uniform remainder theorem proving that the remainder cannot introduce additional zeros (including at resonant parameter strata and where leading coefficients vanish).

Property (I)/(J), finite `C^k` control, and a finite compensator truncation alone do not supply this. The source explicitly has extra nondegeneracy in its worked derivation (for example `\tilde n_2(A_0,0)≠0` at lines 333–346), so that hypothesis cannot silently be promoted to the full four-passage family.

## Refuter's conclusion
**The adopted reduction is refuted as stated.** The witness is symbolic/transseries, not a realized quadratic vector field; therefore it does not refute finite cyclicity of `I^1_6b`. It pinpoints the load-bearing gap: closure plus quasianalytic zero transfer, uniformly over resonances and degeneracy strata.

`complexity_class: polynomial` (fixed symbolic derivative order and five zeros); `oracle_bound: truncation order <=4`.
