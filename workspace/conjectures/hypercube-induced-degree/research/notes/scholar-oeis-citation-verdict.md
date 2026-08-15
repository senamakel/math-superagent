# The four OEIS lookups and the four citation graphs — curator verdict, with the one checked claim

This note records the scholar's/curator's judgment on the eight files fetched by
lookup (four OEIS sequences, four citation digests). They were filed with
placeholders ("not read — replace this") and have now been replaced by notes
under `research/summaries/`. The one mechanical claim is stated as a claim block;
the rest are catalogue/citation verdicts (no claims, by the rule that a
catalogue is `status: catalogued` and a citation graph asserts existence, not
content).

## The one claim (checked by term comparison, n=1..5, and corroborated by a program a runner can execute)

```claim
id: oeis-lookups-not-f
statement: None of the four OEIS sequences fetched by lookup — A002264
  (floor(n/3)), A003056 (inverse triangular), A053251 (mock theta psi),
  A202453 (Fibonacci self-fusion, 2-D) — equals the sequence f(n) = min{ D(S) :
  S ⊆ {0,1}^n, |S|=2^{n-1}+1 } on n=1..5.
  Term-by-term against exact f(1..5)=1,2,2,2,3=ceil(sqrt(n)):
  A002264=0,0,1,1,1; A003056=1,1,2,2,2; A053251=1,1,1,2,2; A202453 is 2-D.
hypotheses: n positive; f(n) the max-internal-degree minimum as in problem.md.
holds-here: yes (direct term comparison, all four, n=1..5)
status: checked (terms read from each OEIS entry; cross-check program written at
  code/out/check_oeis_vs_f.py for a runner to execute — not yet run machine-side)
bearing: closes the "is there a catalogue closed form for f(n)" question; the
  sqrt of f(n) is structural (A_n^2=nI), so no inverse-triangular or
  partition-counting closed form is relevant. Prevents re-reading all four.
contradicts: none in recalled memory.
answers: (no open request quoted these sequences)
anchor: research/summaries/oeis_a002264.md etc.; code/out/check_oeis_vs_f.py
```

## Why the sqrt red herring is worth flagging

A003056 is ~sqrt(2n) and so looks like the answer, but that is coincidence:
f(n)'s sqrt growth is produced by the quadratic identity A_n^2 = n·I on the
signed adjacency matrix (spectrum ±sqrt(n)), not by an inverse-triangular
index. Anyone modelling f(n)'s sqrt as ceil of √(cn) via a catalogue is on the
wrong structural track. This is the summary-level warning aimed at other schools
before they chase the same lookup.

## Citation digests — leads, not evidence

- `citations_w1871596124` (Falik–Samorodnitsky root): one new actionable lead —
  **Ambainis et al. 2014, "Tighter Relations between Sensitivity and Other
  Complexity Measures"** — the Boolean-sensitivity side of problem.md's
  "Connections to Boolean function complexity." Transfer to D(S) is unproved.
  Worth a research request; not evidence.
- `citations_w2103749128` (KKL root): confirms Nisan–Szegedy 1994 exists and is
  heavily cited; screen still withholds it, so recalled-not-sourced, unchanged.
- `citations_w2745097389` (Keevash–Long refs): reconfirms the outer-boundary/
  Fourier family already classified as stuck at log n.
- `citations_w2914000451`: cosmic-ray-positron astrophysics (Lipari), mis-
  attributed, unrelated — discard.

None of the eight contradicts durable memory; none adds a theorem on D(S).
The goal's main line remains the spectral chain f(n) >= sqrt(n) already on disk.
