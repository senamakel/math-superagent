# MathWorld, "Egyptian Fraction" (Wolfram) — encyclopedic reference

Source: https://mathworld.wolfram.com/EgyptianFraction.html (Eric W. Weisstein, Wolfram MathWorld)
Full text: `research/sources/mathworld-egyptian-fraction.full.md`

## What it establishes (encyclopedic context)

The standard background tier for the whole subject: Egyptian fractions as sums of (usually distinct) unit fractions; Rhind papyrus 2/n table (~1650 BC); Fibonacci/Sylvester greedy algorithm; every rational has Egyptian-fraction representations with arbitrarily many terms, but only finitely many with a fixed number of terms; `1/a = 1/(a+1) + 1/(a(a+1))` splitting identity; Martin 1999 dense Egyptian fractions; each x/y with y odd has an odd-denominator representation (Breusch 1954; Guy 1994); Vose 1985 `t = O(sqrt(log y))` term bound; no known algorithm to minimise terms or largest denominator.

**Erdős–Straus exactly as stated (eq. 12):** `4/n = 1/a+1/b+1/c` "always can be solved" — the conjecture, referenced to the separate MathWorld Erdős–Straus page. Sierpiński's `5/n` analog (1956) also noted.

References worth noting: Eppstein "Ten Algorithms for Egyptian Fractions" 1995; Guy §D11 "Egyptian Fractions" in Unsolved Problems in Number Theory 2nd ed. pp. 158–166; Klee–Wagon pp. 175–177, 206–208; Breusch 1954 (odd-denominator case, the AMM "special case" of problem 4512 — relevant to 3/n odd-denominator expansions).

## Implication for this run

Context tier, not machinery. Confirms the conjecture's statement and the standard reference network (Guy D11, Eppstein, Breusch). Nothing here changes the six-class analysis; the useful adjacent results are (i) the `1/a = 1/(a+1)+1/(a(a+1))` splitting identity (the base of every Egyptian-fraction identity family, including the n≡2 mod 3 family), and (ii) the fact that *fixed-term* representations are finite for each n — the reason identities (parametric families) rather than per-n algorithms are the right instrument for a class-settling. Do not cite MathWorld for any of the six-class claims — it points to the Erdős–Straus page for those; the library's primary sources (Elsholtz–Tao, Salez, Schinzel) carry the actual statements.

```claim
id: mathworld-egyptian-context
statement: MathWorld's Egyptian Fraction page records the standard background (greedy/Fibonacci–Sylvester algorithm; every rational has arbitrarily many Egyptian-fraction expansions but finitely many with a fixed number of terms; 1/a = 1/(a+1) + 1/(a(a+1)) splitting identity; odd-denominator representations exist for y odd per Breusch 1954) and states the Erdős–Straus conjecture (4/n = 1/a+1/b+1/c) as eq. 12, with the Sierpiński 5/n analog.
hypotheses: none beyond the reference being encyclopedic.
holds-here: true — context tier; the fixed-term finiteness justifies seeking parametric families rather than per-n algorithms.
status: sourced (MathWorld entry; the underlying facts are classical and cross-present in Eppstein and Elsholtz–Tao).
bearing: fixes terminology and reference network; not a source for any six-class claim.
anchor: research/sources/mathworld-egyptian-fraction.full.md
```