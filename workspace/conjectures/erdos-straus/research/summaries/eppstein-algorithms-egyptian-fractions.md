# Eppstein, "Algorithms for Egyptian Fractions" — index page (ics.uci.edu)

Source: https://www.ics.uci.edu/~eppstein/numth/egypt/intro.html (HTML)
Stored as a summary (the page's whole content is the 2.7 KB intro; no separate `.full.md`).

## What it is

The index page of Eppstein's Egyptian-fraction survey (the Mathematica notebook published as "Ten Algorithms for Egyptian Fractions", Mathematica in Educ. Res. 4(2):5–15, 1995, with later additions: binary remainder improvements, reverse greedy, generalized remainder, small multiple). It states the foundations: every rational has infinitely many Egyptian-fraction representations, but only finitely many with a given number of terms [Ste92]; the representation problem splits into methods (approximation, conflict resolution, binary, continued fraction, reverse greedy, brute force, small numerators). The page links the sections; the section that matters for this run's problem is **Small Numerators** (see `research/summaries/eppstein-small-numerators.md`), which contains the modular-conditions analysis of 4/y and 25 explicit open-class representations.

## Implication

Holds the survey's framing and reference network (Wagon 1991, Stewart 1992). The substantive content is in the small-numerators section, already summarised under its own file. Nothing else here bears on the six open classes directly.

```claim
id: eppstein-algorithms-index
statement: Eppstein's survey index states the Egyptian-fraction foundations (every rational has infinitely many representations, finitely many with a fixed number of terms) and organises the algorithmic methods; the 4/y-specific content is in its "Small Numerators" section.
hypotheses: none.
holds-here: true — context; the fixed-term finiteness is the same fact MathWorld records and it grounds the "parametric family" approach.
status: sourced (Eppstein, ics.uci.edu survey; the finiteness fact is classical, cf. MathWorld).
bearing: indexes the survey; the substantive small-numerators content lives in the companion summary.
anchor: research/summaries/eppstein-algorithms-egyptian-fractions.md
```