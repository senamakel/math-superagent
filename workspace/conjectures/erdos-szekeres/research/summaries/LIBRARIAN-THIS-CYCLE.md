# Librarian cycle — library verified complete, requests answered

## What this cycle established (verified against disk, not recall)

1. **All three open requests are answered by genuine held primary full texts.**
   - `balko-valtr-attack-baa4` and `open-access-full-1e6e` are closed by
     `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
     (source URL https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf,
     verified genuine — it is the EuroComb 2015 Balko & Valtr paper). This
     refutes the Peters–Szekeres strengthened conjecture (cES(7)>32, cES(8)>64)
     but all counterexamples are non-pseudolinear/unrealizable, so they do NOT
     touch the geometric ES conjecture; over pseudolinear colorings Conjecture
     3.1 is verified at a=4,u=k=7 (N=16) and a=4,u=k=8 (N=22).
   - `full-text-faithful-b96b` is closed by
     `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
     (source URL https://renyi.hu/~p_erdos/1960-09.pdf, verified genuine — the
     actual Erdős–Szekeres 1960/61 paper containing the lower-bound
     construction). The construction is thus available in full primary form.
   - The claim blocks carrying `answers:` for these ids live in
     `research/summaries/balko-valtr-A-SAT-attack-on-ES-ENDM2015.md` and
     `research/summaries/erdos-szekeres-1961-construction-concrete.md`.

2. **The `EJC 2017 full` stub and its summary are MIS-DOWNLOADS** (their URL
   arXiv:1601.03182 is an unrelated probability paper). The ENDM 2015 version
   is the genuine held full text; it must be cited, never the stub.

3. **ROOT.md gap items 2 and 3 are STALE.** They claim the Balko–Valtr full
   text and the 1961 primary text are not held. They are. No action needed
   beyond correcting the record here.

## Library coverage (phase-1 exit test met)

The library covers, in research/sources/ with summaries in research/summaries/:
- Primaries: Erdős–Szekeres 1935 (Compositio), Erdős–Szekeres 1961 (renyi PDF).
- Surveys: Morris–Soltan BAMS 2000, Tóth–Valtr (upper bounds and related
  results); geza-toth publications index.
- All upper-bound papers: Suk (JAMS/arXiv 1604.08657), Holmsen–Mojarrad–Pach–
  Tardos, Norin–Yuditsky, Mojarrad–Vlachos, Tóth–Valtr 1998.
- Lower-bound realizability: Duque–Fabila-Monroy–Hidalgo-Toscano (small integer
  coordinates), the run's own verified `es_construct`.
- Exact values and computation: Peters–Szekeres ANZIAM 2006 (n=6=17), Marić
  (formal proof n≤6), Kalbfleisch references, Makai–Turán note.
- SAT / order-type / chirotope foundations: Balko–Valtr ENDM 2015, Scheucher
  (SAT attack in Rd + empty hexagon), Dumitru (arXiv 2512.24061, ES(7)), SMQH
  encoder, Heule–Scheucher (empty hexagon 30), Subercaseaux empty hexagon ITP,
  Felsner–Weil signotopes, Felsner (chirotope NP-complete), Goodman–Pollack–
  Sturmfels, Bergold–Felsner–Scheucher, Hoffmann–Merckx, Wikipedia CC-system,
  Knuth axioms-and-hulls cover.
- Adjacent / restricted classes: Baek–Balko SoCG 2025 (split/decomposable),
  Damásdi–Dong–Scheucher–Zeng (saturation), Chung–Graham, Kleitman–Pachter,
  Károlyi–Tóth (forbidden subconfigurations), balko-bhore (k-convex), por-valtr
  (partitioned version), barany-valtr (positive fraction), fox-pach-sudakov-suk
  (monotone paths/convex bodies), horton (no empty convex 7-gons), goaoc-welzl
  (random order types), moshkovitz-shapira (Ramsey/integer partitions), leanpool
  (ETV capcup Lean), mathlib monotone-subsequence, wikipedia happy-ending &
  erdős-szekeres, mathworld happy-end.

This is the canonical reference tier, plus the methods that failed (abstract
colorings — false per Balko–Valtr), the computational attacks, the adjacent
problems, and the counterexample constructions. All three requests are answered.

## Decision

NOTHING FURTHER to acquire this cycle. The library is complete for phase-1; the
steering rule says gathering proceeds only against a stated gap in the requests
ledger, and there is none open. The next valuable work is the run's own oracle /
computation (a run-side task, not librarian acquisition). If a future cycle needs
anything, the only genuinely missing canonical item flagged is the Knuth
"Axioms and Hulls" book itself (paywalled; CC-system axioms are already covered
via Wikipedia + Felsner), which is not worth a fetch.
