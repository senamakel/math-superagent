# Leavens & Vermeulen 1992 — 3x+1 search programs

<!-- src: G. T. Leavens, M. Vermeulen, "3x+1 search programs", Computers & Math. with Appl. 24(11) (1992) 79–99, DOI 10.1016/0898-1221(92)90034-F. Full text: research/sources/leavens-vermeulen-1992-3x1-search-programs.full.md (Iowa State Univ. Digital Repository PDF, TR 92-01). -->

## What the source establishes

This is the algorithmic companion to the 1992-era verification searches: it
studies the accelerated map T(n) = (3n+1)/2 if n odd, n/2 if n even, and the
map H(n) = 3n+1 if n odd, n/2 if n even, and reports exhaustive distributed
searches of max_{m<n} max_j T^(j)(m) (maximum excursion) and related
quantities.

- Defines the stopping time σ(n) = least k with T^(k)(n) < n and total
  stopping time; records the peak-seeking statistics and their record
  holders.
- Reports searches up to 5.6×10^13 (56 trillion) for peaks of the excursion
  statistic, using the Argus distributed programming system and a C-based
  distributed search, with optimization techniques (bit-level even/odd
  compression, composite polynomials à la Bentley).
- Algorithmic lemmas on computing T iterates efficiently (e.g. Lemma 5-type
  inequalities bounding max values; the make-odd/bit-counting procedures).

The paper is computational/algorithmic: it does not prove the conjecture but
establishes verified ranges and record-holder statistics that later
verification work (Oliveira e Silva 1999; Barina 2021/2025) superseded.

## Claims

```claim
id: leavens-vermeulen-1992-search
statement: Exhaustive 3x+1 searches for maximum-excursion record holders were performed up to 5.6×10^13 using distributed computing (Argus and C), with stopping-time σ(n) and excursion t(n) statistics and algorithmic optimizations for iterating T and H. (Leavens–Vermeulen, Comput. Math. Appl. 24(11) (1992) 79–99.)
hypotheses: accelerated map T and map H as defined; search range 5.6×10^13
holds-here: yes — the verified-range lineage (this 1992 bound → Oliveira e Silva 3×2^53 → Barina 2^71) documents how the finite-verification frontier grew
evidence: proved in source (full text held; full source text in research/sources/leavens-vermeulen-1992-3x1-search-programs.full.md)
status: verified-numerically
falsifies: a reproducible search showing a record-holder below 5.6×10^13 not captured by the tables, or an error in the stated search bound
```

```claim
id: leavens-vermeulen-1992-methods
statement: The paper's algorithmic techniques — bit-level parity compression, composite-polynomial evaluation, distributed search in Argus and C — are the direct ancestors of the later 3^k-sieve methods used in Barina 2021/2025 verification. (Leavens–Vermeulen 1992.)
hypotheses: none beyond the source
holds-here: yes — lineage of the computational method this run's oracle arm should reproduce
evidence: asserted by this source and corroborated by Barina's method section
status: asserted-by-source
falsifies: an authoritative history showing the sieve methods arose independently
```
