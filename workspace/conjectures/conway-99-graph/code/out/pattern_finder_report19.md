# Pattern-finder report — round 19: independent re-confirmation; first-ever tool run over the C3 spectrum family

## What I did

I could not store to the note store (memory server health check failed), so this
report is written to disk and is the durable record.

Before forwarding the rounds 1-18 "catalogue exhausted" verdict by inheritance, I
re-derived the state independently:

1. Confirmed the oracle: `lib.srg.is_srg(rook(3), 9,4,1,2)` = True,
   `is_srg(bvls_graph(), 243,22,1,2)` = True (exact common-neighbour counts).
2. Confirmed no on-disk data is newer than `pattern_finder_report18.md`
   (mtime sort); the mined surface is unchanged since the last look.
3. Ran the **C3 triangle-graph spectrum family** through the exact sequence tools
   for the first time — the one tabulation earlier rounds (1-18) never sequenced.
   (The script `c3_spectrum_sequences.py` header explicitly says "prior
   pattern-finder rounds never tabulated" this family.)

## The C3 spectrum family, run through the tools for the first time

Phillips eq 4.3: C3(Gamma) spectrum = d^1, (k/2+r-3)^m_r, (k/2+s-3)^m_s, (-3)^(nT-v),
with d=3(k/2-1). Over the feasible index set u in {1,3,4,10,31}:

- rt = (u-1)(u+4)/2   : [0, 7, 12, 63, 525]
- st = (u-3)(u+2)/2   : [-3, 0, 3, 42, 462]
- -3 mult nT-v        : [-3, 132, 648, 110823, 81348462]

`analyze_sequence` over these (exact):
- rt: not low-degree polynomial (diff levels 1-3 never constant); no linear recurrence found.
- st: all terms divisible by 3, residues mod 3 period 1; not low-degree polynomial.
- -3 mult: all terms divisible by 3, residues mod 3 period 1; not low-degree polynomial.

sympy closed forms (exact): rt and st are **degree-2 polynomials in u**, with
rt - st = 2u + 1 = a (the a=2u+1|63 driver of the whole family). The -3
multiplicity nT-v = v(k-6)/6 is the same a|63-governed high-degree count already
in the catalogue.

## Why this adds nothing that separates 99 from its controls

The C3 spectrum family is **parameter-determined**: values are the closed-form
polynomials in u, not an independent structural invariant. Critically the
C3-not-strongly-regular fact is **shared** by 99 (u=3) and 243 (u=4): both fail
Phillips Thm 4.2's `s == -k/2 or k == 6` criterion (thread-triangle-graph, closed).
So the C3 spectra re-confirm — rather than extend — the standing conclusion: every
parameter-determined count on disk is a|63-governed and none separates 99 from
9 and 243.

## First-falsifying term

None. These are closed forms verified on the fixed feasible index set, not
fitted patterns with an extrapolating term to break. The only 99-specific
structural values remain **coclique bound 22** and **forced n3 ≥ 3** (Makhnev
conditional) — neither a sequence the tools can extend.

## Verdict

The sequence line is genuinely exhausted (now rounds 1-19). No on-disk artifact
holds a new sequence-bearing result since round 16; the C3 family first run this
round confirms rather than adds. NOTHING FURTHER is available from the sequence
tools; the next structural steps are construction/search (the 99-vertex lift of
the super-simple 2-(22,4,2) design; the k=14 local triangle geometry).

## Files
- `code/out/c3_spectrum_sequences.py` — the family source (pre-existing).
- `code/out/pattern_finder_report19.md` — this report.
