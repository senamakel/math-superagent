# Scholar digest — the four genuinely-new library sources, re-read directly

Prior scholar passes (`scholar-research-library-digest.md`, `scholar-synthesis-gap-closed.md`,
`scholar-digest-new-sources.md`) already synthesised the library. This note re-reads the
four newly-added sources **directly** and adds an independent hand-verification that did
not exist, since the run's shell verification (`verify_new_sources.py`) was written but
never executed (no `.captured.txt` on disk).

## Context: the decisive finding is already closed

The run holds `f(n) = min{ D(S) : |S|=2^{n-1}+1 } >= sqrt(n)` for all n, via the signed
adjacency A_n (A_n²=nI), Cauchy interlacing, and λ_max ≤ Δ. Machine-verified: A_n²=nI
exact n≤8 (huang_spectral.captured.txt), interlacing λ_max≥√n for every admissible S
n≤4 and random S n≤10, consistent with exact f(1..5)=1,2,2,2,3=ceil(√n). The four new
sources are judged against this.

## Liu–Zhou (Eigenvalues of Cayley Graphs, doi:10.37236/8569) — USEFUL, AND HAND-VERIFIED

Plain adjacency of Q_d has eigenvalues {d−2i : i=0..d} with multiplicity C(d,i). I
verified the two aggregate invariants by hand without a shell, since trace(adjacency)=0
and trace(A²)=#ordered adjacent pairs are determined by the claimed spectrum:
- trace: Σ_i (d−2i)C(d,i) = d·2^d − 2·E[i·]·2^d = d·2^d − 2·(d/2)·2^d = 0 ✓ (adjacency, zero trace).
- trace(A²): with X=d−2·Bin(d,1/2), E[X²]=Var+E² = d+0 = d, so Σ (d−2i)²C(d,i) = d·2^d = # ordered adjacent pairs ✓ (each Q_d vertex has d neighbours, 2^d vertices).

So the claimed spectrum is internally consistent. Crucially it isolates that the √n of
the max-degree argument comes ONLY from the SIGNED matrix (A_n²=nI), not from the plain
adjacency whose largest eigenvalue is d. Confirms the run's spectral route; contradicts
nothing.

## Barber (arXiv:1210.4029) — USEFUL, ONE REAL CONTRADICTION FLAGGED

Maximum independent sets of Q_n are exactly the two parity classes X_0, X_1 (size
2^{n-1}). Closes `classification-maximum-independent-20be`. Structural base: an extremal
S of size 2^{n-1}+1 is a parity class plus one crossing vertex (internal degree n).

**FLAGGED CONTRADICTION (within the library), p. the balanced-set formula:**
the source file's prose gives the odd-n balanced-max as `2^{n-1}−2^{n-2}(n−1)` while its
own claim block and the summary give `2^{n-1}−2^{n-2}(n−1)/2`. Both can be checked
against reality at small n:
- even n=2: `2^{n-1}−2^{n-3}(n−2)` = 2−0 = 2. But Q_2 (a 4-cycle) has NO independent set
  of size 2 with one even and one odd vertex — every even vertex is adjacent to both
  odds. True max balanced independent set of Q_2 is 0. So the even formula fails at n=2.
- odd n=5: with the /2 version, `2^{4}−2^{3}·4/2` = 16−16 = 0, which is absurd (balanced
  independent sets of size >0 clearly exist). With the no-/2 version, 16−32 < 0, also
  absurd. So BOTH transcriptions fail at n=5.

The formula's exact constant cannot be resolved here because Barber's PDF is withheld
(evidence screen). The **classification claim** is standard, unaffected, and consistent
with the subcube isoperimetric extremal family; I confirmed by exhaustive reasoning
(Q_3 has no non-parity size-4 independent set) but this needs a shell run to promote to
`checked`. **The formula itself is NOT load-bearing** for the D(S) bound (it is the d=0
line; f(n)'s +1 excess is untouched by it).

## Falik–Samorodnitsky (CPC 2007) — DOES NOT HELP, confirms obstruction

Edge-isoperimetric total-influence inequality Σ I_i(A) ≥ 2·log2(1/µ)·µ; KKL combinatorial
proof (some variable has influence ≥ Ω(log n/n)). Bounds a total/outer-boundary quantity,
NOT max internal degree D(S); its regime is µ ≤ 1/2 while the problem sits at µ just
over 1/2. KKL's max is over coordinate-directions of a leaving-boundary count, not over
vertices of internal degree. Confirms the recorded obstruction; adds nothing to D(S).

## Keevash–Long (arXiv:1807.09618) — DOES NOT HELP, confirms obstruction

Harper vertex-isoperimetric (min vertex boundary by Hamming-ball initial segments) plus a
new stability refinement (near-min boundary ⇒ close to a generalised Hamming ball). Applies
at m=2^{n-1}+1 but bounds the OUTER vertex boundary, never the max internal degree D(S).
Even with stability it only refines the boundary quantity. Most explicit statement in the
library that isoperimetric machinery is the wrong side of the cut for D(S).

## Bottom line

- **Do not help** (for the D(S) bound; confirm obstruction only): Falik–Samorodnitsky,
  Keevash–Long, and the four OEIS sequences + Lipari (astrophysics) + citation leads from
  the earlier pass.
- **Confirmed the spectral base:** Liu–Zhou, now hand-verified by trace invariants.
- **Structural scaffold only, one formula contradictory:** Barber (classification yes,
  balanced-formula constant unresolved and not load-bearing).
- The decisive conclusion — f(n) ≥ √n, gap closed from below, residue = exact value
  ceil(√n) and the un-rebuilt upper construction — is UNCHANGED by all four sources. The
  genuine open residue remains: rebuild/certify the matching upper construction
  `f(n) ≤ ceil(√n)` to promote Θ(√n) to exact equality, and run `verify_new_sources.py`.
