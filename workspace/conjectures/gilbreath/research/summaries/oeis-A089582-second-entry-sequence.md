# A089582 — the second-entry sequence of the Gilbreath triangle (the run's core object)

<!-- source: https://oeis.org/A089582 | full text: sources/oeis-A089582-second-entry-sequence.full.md -->

## What it establishes

**A089582 is literally the sequence the whole conjecture is about**: `d_k(2)` for `k > 1` in the iterated prime-difference triangle — i.e. the run's `A_k(1)`, the second entry of row `k`. The OEIS comment states the reduction exactly:

> "This sequence gives d_k(2) for all k>1 and for the conjecture to be true, this sequence must contain only 0's and 2's."

This is the catalogue's independent statement of the run's proved reduction
(`gilbreath-reduces-to-second-in-02`): GC ⟺ A089582 ⊆ {0,2}. It also notes
"Although not necessary to the conjecture's validity, the 0's and 2's are of
roughly equal count" — a statistical observation matching this run's depth-1000
data (59.6% of intruders are 4, block interiors roughly balanced).

- **Sequence as catalogued** (first 105 terms): `2,0,2,2,2,2,2,2,0,0,0,0,0,0,2,2,0,2,2,0,0,2,2,2,0,0,0,2,2,0,2,0,0,0,2,2,0,0,0,0,0,0,2,2,0,2,2,0,2,0,0,2,0,2,2,2,2,0,0,0,0,0,0,2,0,0,2,2,0,0,2,2,0,2,0,0,0,0,0,2,0,2,2,2,2,2,0,0,2,2,0,0,2,2,0,0,0,0,2,2,2,2,0,0,0`
- **Zero counts in first 10^n terms**: 3, 53, 520, 4995, 49737, 500177 (Robert G. Wilson v, 2014) — trends toward 50%, matching "roughly equal".
- **Cross-checked this run**: `code/out/check_A089582_crosscheck.py` recomputes A_k(1) from the primes with the run's exact generator and compares all 105 terms against the catalogue — **zero mismatches**. The oracle is independently confirmed against a catalogue source.
- The OEIS references give the canonical citation chain: Guy A10, Pickover 2009 (p. 410), Ribenboim 1995, Odlyzko 1993.
- Authors: Robert G. Wilson v and R. K. Guy, Nov 2003. Related: A036262 (array), A036277 (position of first term > 2), A213014 (zeros before first term > 1), A000232.

## Bearing / status

**Catalogue source (status: catalogued).** This is the cleanest numerical home of the run's central object: the conjecture's truth is exactly "A089582 ⊆ {0,2}". It independently corroborates (a) the reduction, (b) the run's row data, (c) the ~50/50 zero/two balance. A claim phrased as "A_k(1) ∈ {0,2}" is a claim about this catalogue sequence.

```claim
id: oeis-A089582-second-entry-catalogue
statement: The second-entry sequence A_k(1) (k≥1) of the prime Gilbreath triangle is the OEIS catalogue sequence A089582, and GC ⟺ A089582 ⊆ {0,2}. The run's exact generator reproduces all 105 catalogued terms with zero mismatches.
hypotheses: primes triangle; A_k(1) = second entry of row k.
holds-here: yes — this IS the run's central object; independent catalogue confirmation of the reduction and the data.
status: catalogued + checked (run's generator matches all 105 catalogue terms)
bearing: gives the run's core quantity a catalogue home and an independent data cross-check; the ~50/50 zero/two balance is a statistical observation on this sequence.
anchor: research/sources/oeis-A089582-second-entry-sequence.full.md, code/out/check_A089582_crosscheck.py
```

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

Let d_0(n) = p_n, the n-th prime, for n = 1 and let d_k+1 (n) = | d_k(n) - d_k(n+1) | for k = 0, n = 1. A well known conjecture, usually ascribed to Gilbreath but actually due to Proth in the 19th century, says that d_k(1) = 1 for all k >= 1. This sequence gives d_k(2) for all k >1 and for the conjecture to be true, this sequence must contain only 0's and 2's. Although not necessary to the conjecture's validity, the 0's and 2's are of roughly equal count.

The paper cited below by A. M. Odlyzko reports on a computation that verified this conjecture for k = p(10^13) ~ 3 * 10^11. It also discusses the evidence and the heuristics about this conjecture. It is very likely that similar conjectures are also valid for many other integer sequences.

Number of zeros in the first 10^n terms: 3, 53, 520, 4995, 49737, 500177, ... - [Robert G. Wilson v][11], Sep 29 2014

REFERENCES

R. K. Guy, Unsolved Problems in Number Theory, 2nd Ed., Springer-Verlag, NY, Berlin, 1994, A10.

Clifford A. Pickover, The Math Book, From Pythagoras to the 57th Dimension, 250 Milestones in the History of Mathematics, Sterling Publ., NY, 2009, page 410.

P. Ribenboim, The new book of prime number records, 3rd edition, Springer-Verlag, New York, NY, pp. xxiv+541, ISBN 0-387-94457-5. 1995. MR 96k:11112

LINKS

[Table of n, a(n) for n=1..105.][12]

Chris Caldwell, [The Prime Glossary, Goldbach's conjecture][13].

Andrew M. Odlyzko, [Iterated Absolute Values of Differences of Consecutive Primes][14], Math. Comp. 61 (1993), 373-380.

N. J. A. Sloane, [My favorite integer sequences][15], in Sequences and their Applications (Proceedings of SETA '98).

Eric Weisstein's World of Mathematics, [Gilbreath's Conjecture.][16]

EXAMPLE

See the triangle in [A036262][17].

MAPLE

[A089582][18]:= proc(n)

[A036262][17] (n, 2) ;

end proc:

seq( [A089582][18] (n), n=1..80) ; # [R. J. Mathar][19], May 10 2023

MATHEMATICA

mx = 105; lst = {}; t = Array[ Prime, mx+2]; Do[t = Abs@ Differences@ t; AppendTo[lst, t[[2]]], {n, mx}]; lst

CROSSREFS

See [A036262][17] for an abbreviated table of absolute differences.

Sequence in context: [A044945][20] [A238005][21] [A296509][22] * [A044946][23] [A044947][24] [A044948][25]

Adjacent sequences: [A089579][26] [A089580][27] [A089581][28] * [A089583][29] [A089584][30] [A089585][31]

KEYWORD

easy, nonn

AUTHOR

[Robert G. Wilson v][11] and [R. K. Guy][32], Nov 08 2003

STATUS

approved

[Lookup][3] [Welcome][33] [Wiki][34] [Register][35] [Music][36] [Plot 2][37] [Demos][38] [Index][39] [WebCam][40] [Contribute][41] [Format][42] [Style Sheet][43] [Transforms][44] [Superseeker][45] [Recents][46]

[The OEIS Community][47]

Maintained by [The OEIS Foundation Inc.][48]

Last modified August 13 04:40 EDT 2026. Contains 398270 sequences.

[License Agreements, Terms of Use, Privacy Policy][49]


## Links

[1]: /login?redirect=%2fA089582
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A089582/list
[5]: /A089582/graph
[6]: /search?q=A089582+-id:A089582
[7]: /A089582/listen
[8]: /history?seq=A089582
[9]: /search?q=id:A089582&fmt=text
[10]: /A089582/internal
[11]: /wiki/User:Robert_G._Wilson_v
[12]: /A089582/b089582.txt
[13]: https://t5k.org/glossary/page.php?sort=GilbreathsConjecture
[14]: https://doi.org/10.1090/S0025-5718-1993-1182247-7
[15]: http://neilsloane.com/doc/sg.txt

*[excerpt ends; 689 characters not shown — see `research/sources/oeis-A089582-second-entry-sequence.full.md`]*
