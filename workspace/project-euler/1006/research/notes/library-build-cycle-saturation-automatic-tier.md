# Library build cycle — automatic-sequences tier attempted, saturation reached

## What this cycle added

- **Dekking & Keane, "On the conjugacy class of the Fibonacci dynamical system"**
  (arXiv:1608.04487, TCS 668 (2017) 59-69) — `research/sources/dekking-keane-conjugacy-fibonacci-dynamical-system.full.md`.
  Full text from the arXiv abstract page. Mathematical content is topological
  conjugacy of substitution dynamical systems in the Fibonacci class — *indirect*
  bearing on PE1006 (it studies rotation/conjugacy structure of the Fibonacci
  system, the family directive 9's cyclic-sum route treats). Kept because it is a
  peer-reviewed, obtainable primary treatment of the Fibonacci dynamical system's
  rotation/conjugacy family; not load-bearing for the arithmetic.

## What this cycle tried and failed to obtain (recorded so nobody re-burns budget)

1. **Allouche & Mendès France, "Automata and Automatic Sequences"** (chapter in
   *Beyond Quasicrystals*, 1995). Two copies downloaded —
   `allouche-mendesfrance-automata-automatic-sequences.full.md` and
   `...-oeis.full.md` — **BOTH converted to unusable mojibake**: the scanned PDF
   uses a non-embedded custom font encoding that the HTML/PDF→Markdown converter
   cannot re-map (garbled `\u0000-\uFFFF` control characters). **Neither is a
   usable source; do not cite either for a claim.** The digest/summary files carry
   the same garbage. This is a conversion failure, not a missing paper; if a
   text-layer PDF of this chapter is ever needed, it must come from a different
   rip.
2. **Allouche, "Sur la complexité des suites infinies"** (Bull. Belg. Math. Soc.
   Simon Stevin 1 (1994) 133-143) — Project Euclid DOI page returned only the
   paywalled metadata/shopping cart (11 pages, $25 single article). Not obtainable
   free. This is the readable automatic-sequences/complexity catalogue that would
   back the top frontier row (Allouche–Shallit book, cited by 5 of our sources);
   its content is otherwise covered by the held Berstel 2007 survey, Lothaire C2,
   and the Coven–Hedlund papers (1973 of which is on disk).
3. **Morse & Hedlund, "Symbolic Dynamics II: Sturmian Trajectories"** (Amer. J.
   Math. 62 (1940) 1-42) — JSTOR/AMS-paywalled, no free scan. The run already
   holds the actual theorems (Coven–Hedlund 1973 "Sequences with minimal block
   growth" on disk; Lothaire C2 states the Morse–Hedlund minimal-complexity /
   Sturmian-p(n)=n+1 theorem). Honest gap, not a lead.
4. **Coven, "Sequences with Minimal Block Growth II"** (Math. Syst. Theory 8(4)
   376-382, 1975 — single-author continuation; frontier row cites it as 1974 from
   a citing source's year). Springer-paywalled, no free scan. Part I (Coven–Hedlund
   1973) is on disk.
5. **Berstel, "Fibonacci Words — A Survey"** (The Book of L, 1986) — persistent
   known gap (bibliographic record only on disk; full text unobtainable from
   univ-mlv host or lanfanshu mirror). Still not blocking: Sturmian/Fibonacci
   definitions and factor-complexity are covered by Lothaire C2, Perrin–Restivo,
   and the Berstel 2007 survey (all full text on disk).
6. **Chuan & Ho, "Locating factors of the infinite Fibonacci word"** (TCS 349
   (2005) 429-442) — the direct position-theorem source; ScienceDirect-paywalled.
   Its content is held via the Sivasankar–Rama position theorem (full text on
   disk) whose Theorem 7 is the same locating statement. Non-blocking.
7. **de Luca, "A division property of the Fibonacci word"** (IPL 54 (1995)
   307-312) — the run's own sources cite it 1760+ times (frontier top). No free
   PDF (ScienceDirect paywall, Univ. Naples IRIS has no file attached). Recorded
   as an honest gap; not load-bearing for the solver's arithmetic.

## State of the frontier

The top frontier rows are all *paywalled classics* (Allouche–Shallit book,
Morse–Hedlund 1940, Berstel survey, de Luca division property). Their *content*
is held via freely obtainable full-text equivalents already on disk. The two
obtainable-new-source angles left (automatic-sequences chapter, complexity
survey) both failed at the download/conversion stage this cycle. **The library
has reached saturation on the load-bearing tiers** (Sturmian/mechanical-word,
factor complexity, standard words/PER, three-distance/three-gap, universal
Euclidean floor-sum, automatic/Fibonacci-automatic). Further growth would be
redundant retellings of material already anchored. Recommend: hold on new
sources; the run's bottleneck is now the solver's wiring (mech_psi formulation B
through ueuclid, anchors, 10^18), not missing references.

## OEIS

The computed Ψ(k) exact values (k=1..25 in `code/out/psi_exact.txt`) and the
mod-M residues are already recorded as uncatalogued misses (OEIS misses notes on
disk). No closed form obtainable by lookup — consistent with the sequence growing
~10^(2k). This remains recorded so nobody re-searches.
