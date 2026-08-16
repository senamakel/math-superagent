# de Frutos Marín 2015 "Un problema sobre números combinatorios" — independent corroboration of the run's bad-prime lists

Source record: http://singacom.uva.es/JTN2015/contribuciones/ordinarias/frutos.pdf (Jornadas de Teoría de Números / JTN 2015 contribution, Universidad de Valladolid), Rosa de Frutos Marín. **The PDF is network-blocked from this environment** (the uva.es host is unreachable, same as uvadoc.uva.es). The abstract was obtained via search and is quoted below; the full text is NOT held.

## What the abstract establishes (quoted content)

> La conjetura ha sido probada para grados del tipo n = h·q, donde q es la potencia de un número primo p y h = 1,2. Para cada uno de los h = 3,4,5,6,7, se ha podido dar un listado finito L(h) de valores de p (llamados ineficaces) tales que si p no está en el listado correspondiente a dicho h, entonces se ha podido probar la conjetura para n = h·q, siendo q cualquier potencia de p. Esta circunstancia justifica el calificativo ineficaz para los primos que no están en los correspondientes listados. En concreto, **L(3) está formado solo por el primo 2; L(4), por los tres primos 3, 5, 7; L(5), por los nueve primos 2, 3, 7, 11, 131, 193, 599, 3541, 8009**, mientras que L(6) consiste en 53 primos ineficaces concretos, y L(7) de 661, estos últimos calculados utilizando computación. Para n = 12 también se ha probado utilizando computación.

## Why this is a load-bearing corroboration

The abstract's lists **match exactly** the run's own independently-verified computations:

- **L(4) = {3, 5, 7}** — matches `badprimes-n4-minor-criterion-verified` (SNF lcm J_T = 1575 = 3²·5²·7 → {3,5,7}, two independent exact routes).
- **L(5) = {2, 3, 7, 11, 131, 193, 599, 3541, 8009}** — matches `badprimes-n5-minor-criterion-verified` (rank-over-F_p of the 195×120 matrices M_T, 625 tuples × 170 primes) and `badprimes-n5-semantic-smallprimes` (exhaustive oracle enumeration on {2,3,5,7,11,13}).
- **L(3) = {2}** — matches the Hasse-formulation reproduction (n=3 → {2}).
- **L(6) = 53 primes, L(7) = 661 primes** — the run has NOT computed these; they are a recorded target for a future computational cycle (the n=6/n=7 minors criterion is infeasible, but a dedicated binomial/other-criterion computation for these degrees might reproduce or refine them).
- **"n = 12 también se ha probado utilizando computación"** — corroborates the degree-12 settlement (Castryck et al. 2012), from an independent (thesis-lineage) source.

The "ineficaces" (inefficient) primes are exactly the **bad primes** of the run's terminology — the primes p for which the CA_{n,p} reduction does not go through for degree n. So this source independently confirms the run's bad-prime framework from the arithmetic/combinatorial side (de Frutos Marín's thesis lineage: the discriminant/scheme formulation).

## Status

- Evidence class: **sourced-abstract** (the abstract was obtained and quoted; the full PDF is network-blocked). The list-matching is a verification against the run's own exact computations — but the source itself is not held in full text, so treat it as corroboration from an abstract, not as a held primary text.
- Not downloaded: singacom.uva.es and uvadoc.uva.es are unreachable from this environment (network layer, not 404). Do not retry the fetch in this run.
- Cross-links: `research/sources/defrutosmarin2013_arithmetic-casas-alvero.full.md` (the thesis record), `research/notes/badprimes-criterion-n4-n20.md`, `research/notes/badprimes-criterion-n5.md`, claims `badprimes-n4-minor-criterion-verified`, `badprimes-n5-minor-criterion-verified`, `badprimes-n5-semantic-smallprimes`.

```claim
id: badprimes-lists-corroborated-by-defrutosmarin2015
statement: de Frutos Marín (JTN2015 contribution "Un problema sobre números
  combinatorios", Valladolid) independently lists the bad ("ineficaces")
  primes for degrees n = h·q: L(3)={2}, L(4)={3,5,7},
  L(5)={2,3,7,11,131,193,599,3541,8009}, L(6)=53 primes, L(7)=661 primes
  (the latter two computed), and states n=12 verified computationally.
  The L(3), L(4), L(5) lists match EXACTLY the run's independently verified
  bad-prime lists (claims badprimes-n4-minor-criterion-verified,
  badprimes-n5-minor-criterion-verified, badprimes-n5-semantic-smallprimes,
  and the n=3 Hasse reproduction {2}). This is independent corroboration of
  the run's bad-prime framework from the thesis/arithmetic lineage.
hypotheses: char 0; degree n = h·q with q a prime power; p not in L(h)
holds-here: yes — the matching lists are against the run's own exact
  computations (SNF/rank over F_p, oracle enumeration)
status: asserted-by-source-abstract (full PDF network-blocked; abstract
  quoted in this note)
anchor: research/notes/defrutosmarin2015-combinatorios-corroborates-badprimes.md
falsifies: a full text of the 2015 note whose lists differ from those quoted
  here (in which case re-check which source is right), or a run of the n=6/n=7
  criteria reproducing different lists
```

## Cross-source discrepancy: L(7) count (366 vs 661)

The de Frutos Marín 2015 abstract says **L(7) = 661 primes**, but the held
primary source **Castryck et al. 2012 (Theorem 4)** says degree d=7 has
**366 bad primes**, listed in the accompanying file `badprimes7.txt`, smallest
non-bad prime (apart from p=7) is 127, largest bad prime is the 133-digit
number at line 158 of the held source. The L(6)=53 count agrees between the
two sources.

**Resolution status: UNRESOLVED.** The two sources may be counting different
objects (de Frutos Marín's L(7) may be a different notion than Castryck's
bad-prime list — e.g. "ineficaces" primes for the h=7 reduction could be a
superset, or a different computational convention), or one may be an error.
The full text of the 2015 note is not held (uva.es unreachable), so the
convention difference cannot be checked here. The run should NOT cite "661"
for the d=7 bad-prime count; the held primary source says 366. If a future
cycle obtains the 2015 note's full text, resolve this. This is recorded as a
contradiction-type finding, not silently resolved.


