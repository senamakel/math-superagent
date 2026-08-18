# Librarian cycle — Cobham–Semenov standard survey added (top frontier row)

## What was added

- **Bruyère, Hansel, Michaux & Villemaire, "Logic and p-recognizable sets of
  integers", Bull. Belg. Math. Soc. Simon Stevin 1(2) (1994) 191–238, DOI
  10.36045/bbms/1103408547** — the survey that had been the most-cited
  non-held frontier row (cited by 3 of our held sources).
  - Obtained at https://www-verimag.imag.fr/~iosif/LAT/bru.pdf (typed PDF,
    114 KB markdown) after the EMIS copy redirected to a zbmath 403 and the
    projecteuclid entry is paywalled; also indexed at EUDML (232407).
  - Full text: `research/sources/bruyere-hansel-michaux-villemaire-logic-p-recognizable.full.md`
  - Digest replaced with a real summary:
    `research/summaries/bruyere-hansel-michaux-villemaire-logic-p-recognizable.md`
  - Citation graph (251 citations) walked both directions via
    `citation_graph 10.36045/bbms/1103408547`; 50 works filed as leads in
    derived/FRONTIER.md; the bibliography+abstracts at
    `research/summaries/citations_w2163696969.md`.

## Why it matters here

The decisive statement is **Theorem 7.7 (Cobham–Semenov)**, verified in the
full text (lines 1485–1515): if p, q ≥ 2 are multiplicatively independent and
s is both p- and q-recognizable, then s is definable in ⟨N, +⟩ (ultimately
periodic in N). This is the standard citable tier for the run's Cobham
obstruction claim `cobham-bes-frougny-multiplicatively-independent-conversion`
(10 and φ = (1+√5)/2 are multiplicatively independent ⇒ no finite-automaton
conversion between φ- and decimal numerations ⇒ the Zeckendorf digit-DP route
is blocked). The Frougny 2002 paper (linear numeration systems) remains the
exact-form reference for the non-integer-base case; this survey is the primary
integer-base statement both descend from. The universal-Euclidean monoid is
**not** an automaton conversion, so it is untouched by this theorem — the
summary says so explicitly to prevent a future misread.

## State of the library

All four previously open research requests remain closed (`answers:` lines in
the claim notes: `req-close-factor-complexity`,
`req-close-universal-euclidean`). OEIS lookups recorded as misses
(`oeis-psi-miss-recorded.md`, `oeis-misses-cycle3.md`). The frontier's
remaining high rows are paywalled primaries (Morse–Hedlund 1940 Symbolic
Dynamics II; Berstel 1986 Book of L) or already-held duplicates. The next
cycle's scarce budget belongs to the solver's wiring of mech_psi through
ueuclid (directive 10 order), not to more sources.

```claim
id: cobham-bes-frougny-multiplicatively-independent-conversion
statement: Two linear numeration systems (over Pisot bases) are mutually
recognisable / convertible by finite automata only if their bases are
multiplicatively dependent. In particular, since 10 and phi = (1+sqrt5)/2 are
multiplicatively independent, no finite automaton converts between the
Fibonacci (phi-)numeration of positions and the decimal (base-10) digit
weights used to read a length-k window as a decimal number.
hypotheses: bases are Pisot (integer case: p, q >= 2 multiplicatively
independent); standard recognisability in each base.
holds-here: yes — 10 and phi are multiplicatively independent (10^k = phi^m
would force phi rational, impossible); the integer-base case holds a fortiori
for powers of 10 vs powers of phi.
status: sourced
bearing: rules out the finite-automaton Zeckendorf digit-DP route to Psi(k)
(approaches/pe1006-zeckendorf-automatic-digit-dp) at full size; the committed
universal-Euclidean monoid does exact integer arithmetic in one base and is
not affected.
anchor: research/sources/bruyere-hansel-michaux-villemaire-logic-p-recognizable.full.md
(Theorem 7.7, Cobham–Semenov, verified at lines 1485–1515, with the
multiplicative-independence hypothesis);
research/sources/frougny-mult-dep-linear-numeration-2002-irif.full.md
(Theorem 2, Corollary 1, and the independence restriction)
answers: (the automaton-conversion question, negatively — strengthened with a
second, primary-tier anchor)
```