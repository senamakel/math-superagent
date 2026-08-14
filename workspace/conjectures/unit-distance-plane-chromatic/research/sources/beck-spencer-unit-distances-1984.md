# Unit distances — Beck and Spencer 1984

**Source:** doi:10.1016/0097-3165(84)90047-5 (JCT Series A 37:3 (1984) 231–238)
**Authors:** József Beck, Joel Spencer
**Full text:** not on disk; read via read_sources.

## What this establishes

One of the two 1984 primary upper bounds on the maximum number of unit
distances among n points in the plane:

- **Result:** the number of unit distances determined by n points in the plane
  is at most O(n log* n), where log* is the iterated logarithm.
- **Method:** incidence/partitioning arguments over the geometric structure of
  the point set (the Szemerédi–Tóth style incidence machinery), pre-dating and
  complementing the sharper Szemerédi–Trotter-style algebraic bounds.
- This is a *weaker* bound than the O(n^{4/3}) of Spencer–Szemerédi–Trotter
  (1984, in Bollobás, Graph Theory and Combinatorics, pp. 293–303). Both are
  primary sources; together they form the "density cannot be bought" backbone
  of the problem statement's construction argument.

## Why it matters here

The library's `ud-bound-spencer` claim rests on the SST 1984 chapter. This
sibling 1984 paper is an independent primary anchor for the same counting line:
two different 1984 arguments bound unit-distance density, and the stronger one
(O(n^{4/3})) is the constant in the problem's density argument. A claim about
"the O(n^{4/3}) bound dates to 1984 and is published" is now backed by two 1984
primary sources, one of which (this one) is a journal paper reachable through
read_sources.

```claim
id: beck-spencer-1984-unit-distance-bound
statement: The number of unit distances among n points in the plane is at most O(n log* n) (Beck–Spencer 1984, JCTA 37:3). This predates/coincides with the stronger O(n^{4/3}) Spencer–Szemerédi–Trotter bound of the same year; together they anchor the density constraint on unit-distance graphs.
hypotheses: Points in R^2; Euclidean unit distance; n finite.
holds-here: true — supplies a primary, journal-published anchor for the density line that the problem statement's construction argument uses (density cannot be bought; rigidity must be the source).
status: sourced (paper abstract + read_sources summary)
bearing: Gives the counting/density constraint on unit-distance graphs a second, independent primary source; the 4/3 power is the one the run's constructions must respect.
anchor: research/sources/beck-spencer-unit-distances-1984.md
```

## Note on download

Full text blocked at network layer; statement from read_sources summary and the
Józsa–Szemerédi lineage it cites. Status: **sourced via read_sources; full text
not on disk.**