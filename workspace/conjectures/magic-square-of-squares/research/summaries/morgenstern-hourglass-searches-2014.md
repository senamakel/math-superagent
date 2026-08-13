# Morgenstern, "Three new searches for a magic hourglass", June 2014

[[morgenstern-hourglass-searches-2014]]
Source: http://www.multimagie.com/English/Morgenstern25.htm

## What it establishes
Three fresh computational searches for a **magic hourglass**, all reporting **no solutions found**, and — importantly for the Buell-bound caveat — the third is a *pair*-based search strictly wider than Buell's *triple*-based one.

**Search 1 (all central values, partial):** `[(m²+n²)(r²+s²)]² ± 4[mn(m²−n²)(r²+s²)² ± rs(r²−s²)(m²+n²)²]` both squares, all `m,n,r,s < 9000` with `gcd(m,n)=gcd(r,s)=1`. Central values up to ~`8.1×10⁷`, partial search of central values up to almost `(2·9000²)² ≈ 2.6×10¹⁶` (possible square length up to 33 digits). Took several weeks.

**Search 2 (opposite extreme to Buell):** same formulas but `(m²+n²)(r²+s²) < 5×10¹²` with `m,n` coprime and `r,s` coprime — i.e. `m²+n²` sharing **no factor** with `r²+s²`. ~10 hours on 4 i7 cores.

**Search 3 (wider than Buell):** `(m²+n²)² ± 4[mn(m²−n²) ± rs(r²−s²)]` both squares, with `(m²+n²) = (r²+s²) < 5×10¹²`, `m,n` and `r,s` allowed common factors. Buell used **triples** `m²+n² = r²+s² = u²+v²` (which restricts scaling); here **pairs** `m²+n² = r²+s² = (u²+v²)t` allow non-square `t`, so this search tests **more** possibilities than Buell's and acts as an independent verification that **Buell's search correctly found no solutions**. No solutions found. ~10 hours on 4 cores.

## Implications for this run
- Strengthens the "no full-MSS `25×10²⁴` centre bound" caveat already in `buell-search-for-magic-hourglass-1999.md`: not only is that Buell's *hourglass*-only, *coprime* bound, but Morgenstern's pair reformulation (strictly wider than the triple form) also finds nothing in the same range. The absent solution is robust to the scaling relaxation.
- Consistent with CONTEXT.md's note that the hourglass (Φ/gaussian) structure is where the searches concentrate, and that buell's triple-based restriction was the only thing preventing a wider statement; this page shows the wider statement also has no hit up to the same scale.
- Adds no new theorem; it is a search-range fact (several weeks + ~hours of CPU).

```claim
id: morgenstern-2014-hourglass-no-solutions
statement: Three searches for the magic hourglass found no solutions: (1) all m,n,r,s<9000 (central values up to 8.1e7, partial central values up to ~2.6e16, gcd(m,n)=gcd(r,s)=1); (2) (m²+n²)(r²+s²)<5e12, m²+n² coprime to r²+s²; (3) (m²+n²)=(r²+s²)<5e12 allowing common factors, a pair-based search strictly wider than Buell's triple-based search, which independently confirms Buell found no solution.
hypotheses: the three formula families; hourglass configuration; gcd conditions as stated
holds-here: yes (upper-bound/sieve context)
status: asserted (reported on Morgenstern's page; not re-run here)
bearing: corroborates no-hourglass to the searched scale, including under the relaxed (pair) form; reinforces that the 25e24 figure is an hourglass, not full-MSS, bound
anchor: research/sources/morgenstern-hourglass-searches-2014.full.md
```
