# Executed: n5_m3_joinirreducible_check.py (mechanical confirmation of claim n5-m3-joinirreducible-filters)

(Stored here because the memory server was unavailable when this run tried to
file the same text; the workspace copy is the durable record.)

- Ran: `python3 code/out/n5_m3_joinirreducible_check.py`
- Capture: `code/out/n5_m3_joinirreducible.captured.txt` (exit 0, three-line header)
- Oracle: self-contained exact lattice computation (covering relations,
  transitive principal filters, join-irreducibles); no floats.
- Range: N5 in both standard labellings + the M3 diamond, |L| = 5 each.

Output (verbatim):

```
PENTAGON layout A: chain 0<a<b<1 and 0<c<b, a∥c
== N5 (layout A): |L|=5, join-irreducibles & filter sizes ==
   a: |[a)|=3  <= 5/2=2.5? False
   c: |[c)|=3  <= 5/2=2.5? False
   1: |[1)|=1  <= 5/2=2.5? True
   Frankl lattice form satisfied: True
PENTAGON layout B: 0<a<c<1, 0<b<c<1, a∥b
== N5 (layout B): |L|=5, join-irreducibles & filter sizes ==
   a: |[a)|=3  <= 5/2=2.5? False
   b: |[b)|=3  <= 5/2=2.5? False
   1: |[1)|=1  <= 5/2=2.5? True
   Frankl lattice form satisfied: True
DIAMOND M3: 0 < a,b,c < 1
== M3: |L|=5, join-irreducibles & filter sizes ==
   a: |[a)|=2  <= 5/2=2.5? True
   b: |[b)|=2  <= 5/2=2.5? True
   c: |[c)|=2  <= 5/2=2.5? True
   Frankl lattice form satisfied: True
```

What it settles: the pentagon N5 — in BOTH standard labellings — has
join-irreducibles {a,c,1}/{a,b,1} with principal-filter sizes {3,3,1}; the
only join-irreducible with |[j)| ≤ 5/2 is the top 1̂ (filter size 1,
vacuously abundant; nothing to lift). The element c with |[c)|=2 is
join-reducible (c = a∨b), NOT join-irreducible. The M3 diamond atoms each
have |[a)|=2 ≤ 5/2, confirming the M3 half of the kernel. Claim
`n5-m3-joinirreducible-filters` is thereby mechanically confirmed (its status
and anchor updated in research/approaches-grounding-notes.md, and the approach
note research/approaches/forbidden-sublattice-lifting.md cites the capture).
The inventor's forbidden-sublattice-lifting kernel claim — N5 has a
join-irreducible b with |↑b|=2 — is false as stated; the M3 half stands, so a
restarted lift program would have to begin from M3, not N5.