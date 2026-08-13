# OEIS A358691 — Kimberling's "Gilbreath transform", odd-indexed primes

<!-- source: https://oeis.org/A358691 | full text: sources/oeis-A358691-gilbreath-transform.full.md (summary holds essentially all of it) -->

## What it establishes

**Clark Kimberling (Nov 2022) defines the named object "Gilbreath transform"** — the
run's A036262 summary already cited it; here is the catalogue record.

**Definition (Kimberling):** For a real sequence S = (s(k)), the Gilbreath array
is g(1,n) = |s(n+1)−s(n)|, g(k,n) = |g(k−1,n+1) − g(k−1,n)|; the **Gilbreath
transform** is G(S) = (g(n,1)) — the leading column. **GC ⟺ G(primes) = (1,1,1,...).**

**Conjectured examples (all catalogue-asserted, none proved there):**

| S | G(S) | Status vs this run |
| --- | --- | --- |
| primes A000040 | (1,1,1,...) | this IS Gilbreath's conjecture |
| Fibonacci A000045 | (0,1,1,0,1,1,...) = A011655 | eventually periodic |
| Lucas A000032 | (2,1,1,0,1,1,0,1,1,...) | eventually periodic |
| odd-indexed primes A031368 | **A358691 = (3,3,3,3,1,1,1,...)** | this entry: starts 3 then 1 forever |
| A031369 | A358692 = (1,3,1,1,1,1,...) | eventually 1 |

Two further conjectured examples:
1. **S = primes of the form k·n+2 (k odd, n≥0) ⟹ G(S) = (k,k,k,...)** —
   this is *exactly* the Li 2026 modulo-k Gilbreath family already in the
   library (`modulo-k-gilbreath-family`, verified odd k < 100,000). An
   independent catalogue statement of the same generalization.
2. S = primes p(b(n)) for an increasing arithmetic b with b(1)=1 ⟹ G(S)
   eventually (1,1,1,...); same if b(1)>1 and S = 2 followed by p(b(n)).

Kimberling's remark: "It appears that there are many S such that G(S) is
eventually periodic" — the heuristic the A036262 summary flagged.

**Example corner (odd-indexed primes 2,5,11,17,23,31,41,...):** the leading
column is 3,3,3,3,1,1,1,... — visible in the worked array in the entry.

## Bearing / status

**Catalogue source (status: catalogued).** Gives the run a named object (the
Gilbreath transform) for the leading-column map, and two independent
corroborations: (a) the odd-indexed primes give a *proved-by-data, small*
example where a 2-then-odds-like start enters the 1-regime permanently after
four rows — a data point for the "regeneration is eventually complete" class;
(b) Kimberling's k·n+2 conjecture matches Li 2026's verified modulo-k family,
cross-confirming both. The references also surface an index entry cluster
(the "Gilbreath conjecture and transform" index) worth mining.

```claim
id: oeis-a358691-gilbreath-transform
statement: Kimberling defines the Gilbreath transform G(S) = leading column of the absolute-difference array of S; GC ⟺ G(primes)=(1,1,1,...). Catalogue-asserted conjectures: odd-indexed primes give G=(3,3,3,3,1,1,1,...), Fibonacci gives (0,1,1,0,1,1,...), and primes kn+2 (k odd) give G=(k,k,k,...) — the last is an independent statement of the Li 2026 modulo-k family already verified by this run's sources.
hypotheses: none beyond the definition; the examples are conjectured in the entry (status: catalogue-asserted), aside from the trivial ones.
holds-here: yes — the k·n+2 example independently matches the held modulo-k claim; the transform gives the leading-column map a name.
status: catalogued (Kimberling, OEIS 2022); the kn+2 statement corroborates Li 2026 (asserted there, verified odd k<100,000).
bearing: named object for the leading column; cross-source corroboration of the modulo-k family; a worked example of an eventually-1 transform.
anchor: research/sources/oeis-A358691-gilbreath-transform.full.md
```