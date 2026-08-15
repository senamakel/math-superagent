# Scholar final pass — library fully digested, one contradiction settled

This pass re-read the reference library against the goal (f(n) = min{ D(S) :
S⊆{0,1}^n, |S|=2^{n-1}+1 }, max internal degree), the tasks, and durable
recalled memory. Every source in `research/sources/` and `research/summaries/`
was already digested by prior scholar passes (`scholar-library-read-in-full.md`,
`scholar-research-library-digest.md`, `scholar-synthesis-gap-closed.md`,
`scholar-digest-new-sources[-v2].md`, `scholar-oeis-citation-verdict.md`,
`scholar-barber-formula-verdict.md`, `scholar-new-library-pass.md`). Nothing in
the new material was left unread. What this pass adds is a settlement and a
coverage confirmation.

## Decisive state (unchanged, confirmed on re-read)

f(n) ≥ √n for all n, proved on the run's own derivation (signed adjacency
A_n, A_n²=nI, Cauchy interlacing of the (2^{n-1}+1)-principal submatrix,
λ_max ≤ Δ). Hence f(n)=Θ(√n), the c·log n vs √n gap is closed from below,
f(n)=ω(log n). Consistent with exact f(1..5)=1,2,2,2,3=ceil(√n).
Caveat: literal f(n)≤√n is false for n=2,5 (integer rounding); correct
statement is Θ(√n), attainment ceil(√n). Open residue: the upper construction
f(n)≤ceil(√n) is not rebuilt on disk (Huang withheld), so exact equality is
not yet certified. All anchors in durable memory.

## Contradiction settled (this pass)

The two Barber balanced-independent-set formula claims disagreed. This pass
confirmed `barber-balanced-formula-transcription-broken` is right: both
transcriptions are broken. Decisive: Q_5 contains {00000,11111}, non-adjacent
and of opposite parity, so a balanced independent set of size 2 always exists,
but at n=5 odd v1=16−32=−16 and odd v2=16−16=0, both absurd; the even form
also collapses (n=6→0, n=8→−64). Neither linear-in-n form is the true constant.
Not load-bearing for f(n) (d=0 line). The classification claim (max independent
sets of Q_n are exactly the parity classes, size 2^{n-1}) is sound and
unaffected.

## Source verdicts (why nothing needs re-reading)

- Do not help for D(S), confirm the obstruction only: Falik–Samorodnitsky,
  Keevash–Long×2, Ellis×2, Harper×2, KKL, Beckner, Friedgut,
  Beltrán–Ivanisvili–Madrid, Durcik–Ivanisvili–Roos, Barber–Erde — all bound
  average/outer-boundary quantities, never the max internal degree.
- Maximum-producing but wrong end: Kruskal–Katona, induced-subgraphs-hypercubes.
- Discard: citation graph w2914000451 (cosmic-ray positrons, mis-attributed).
- All seven OEIS lookups negative — f's √n is A_n²=nI, not a catalogue index.
- Screen-withheld, recalled-not-sourced: Huang 2019, Nisan–Szegedy 1994.
- Actionable lead (not evidence): Ambainis et al. LICS 2014 sensitivity relations.

## Gaps (unchanged)

Rebuild/certify the upper construction f(n)≤ceil(√n) to promote Θ(√n) to exact
equality; then the whole f(n)=ceil(√n) statement is certified. Until then the
certified statement is √n ≤ f(n) + exact f(1..5).

## Claim block

```claim
id: barber-balanced-formula-transcription-broken-confirmed
statement: Neither library transcription of Barber's balanced-independent-set
  constant for Q_n is correct. At n=5 a balanced independent set of size 2
  exists (e.g. {00000,11111}), yet odd v1=2^4−2^3·4=−16 and
  odd v2=2^4−(2^3·4)/2=0; both fail. The even form 2^{n-1}−2^{n-3}(n−2) also
  collapses (n=6→0, n=8→−64). All three linear-in-n forms are broken
  transcriptions; none should be cited.
hypotheses: Q_n balanced = equal even/odd parity counts, independent,
  no inter-parity edges.
holds-here: yes.
status: checked (hand oracle at n=5; cross-consistent with n=3 hit at v2 and the
  n=2 even-form failure). Exact general constant not established here.
bearing: the balanced-set constant is not load-bearing for f(n) (d=0 line,
  untouched by the +1 excess); do not cite either transcription.
contradicts: barber-balanced-formula-odd-half (the over-broad claim asserting the
  /2 form for all odd n≥3); and both rows of
  balanced-independent-set-max-smaller-than-parity carry a broken transcription.
anchors: research/summaries/scholar-barber-formula-verdict.md,
  research/sources/barber-balanced-independent-cube-2012.md,
  code/out/check_barber_balanced.py (oracle, n=5 to run)
```
