# Elsholtz & Tao — "Counting the number of solutions to the Erdős–Straus equation on unit fractions"

Christian Elsholtz and Terence Tao, J. Aust. Math. Soc. 94 (2013) 50–105;
arXiv:1107.1010 (v6, 2 Aug 2015), 55 pp.
Sources: `research/sources/elsholtz-tao-counting.full.md` (the paper itself, PDF
converted, 115 KB — downloaded from terrytao.files.wordpress.com/2011/07/
egyptian-count13.pdf) and `research/sources/pomerance-erdos-straus.full.md`
(ar5iv HTML rendering of arXiv:1107.1010, 170 KB — a second complete copy of the
same paper, named by an earlier run; do not download again).

## What the paper establishes

**Setting.** `f(n)` = number of solutions of `4/n = 1/x+1/y+1/z`, `x,y,z > 0`.
It suffices to consider prime `n = p` (prime reduction). Elsholtz–Tao classify
solutions by how many of `x,y,z` are divisible by `n`: for prime `n`,
**Type I** = exactly one of `x,y,z` divisible by `n`; **Type II** = exactly two
are. `f(p) = 3 f_I(p) + 3 f_II(p)`.

**Main counting result.** As `N → ∞`,
```
N log²N ≪ Σ_{p ≤ N} f(p) ≪ N log²N log log N ,
```
so a typical prime has a small number of solutions; in particular
`f(p) = O(log³p · log log p)` for primes of density arbitrarily close to 1.
The Erdős problems database (also in library) states the cleaner form
`Σ_{p≤N} f(p) = N (log N)^{2+o(1)}`, and the paper also gives
`f(p) ≪ p^{3/5+o(1)}` for all primes.

**Proposition 1.6 (Vanishing — *the* obstruction behind the six open classes).**
> For an odd perfect square `n`, there are no Type-I and no Type-II solutions to
> `4/n = 1/x + 1/y + 1/z`; i.e. `f_I(n) = f_II(n) = 0`.

(Title and content confirmed from source §1: the abstract's statement list in
`research/sources/pomerance-erdos-straus.full.md` lists "Proposition 1.6
(Vanishing)" with the square condition; the claim is asserted in the paper and
re-stated in this run's `code/verify_library_claims.py` claim block
`vanishing-type12-odd-squares` with status *asserted — not re-proved here*.)

This is why the classical machinery stops exactly at the square residue classes:
every classical parametric solution of `4/n` for `n ≡ r (mod m)` (in particular
those giving Type I or Type II for prime `n`) is ruled out when `n` is an odd
perfect square — and the six residual classes mod 840 are all perfect square
residues (`1, 121, 169, 289, 361, 529 = 1², 11², 13², 17², 19², 23²`). Salez's
Schinzel-theorem (Prop 2) is the polynomial-family form of the same fact.

**Solvable congruences (Prop 1.9).** Every primitive residue class
`n ≡ r (mod 840)` is "solvable by polynomials" unless `r` is a perfect square;
the perfect-square primitive classes cannot be solved by polynomials. (Form: the
class `n ≡ −c` or `n ≡ −1/c (mod 4ab)` with `(a,b)=1`, `c | a+b` odd, is
polynomially solvable — this is the system of modular identities in §2/§11,
recovering Mordell's identities as the case `a = b = 1` (gives `n ≡ 3 mod 4`).)

**Structural characterisations used in the count.** Props 2.2 and 2.6 give,
respectively, "Description of Type I solutions" and "Description of Type II
solutions" (with the companion Lemmas 2.8, 2.11 and Lemma 11.2 "Generation of
Type II solutions"). The precise parameter formulas are in the paper (§2); the
section heading list in the ar5iv copy gives the exact proposition titles.
These parametrisations are exactly what the symbolic ansatz search should test
shapes against — any ansatz that specialises to Type I/II at squares is
impossible by Prop 1.6. (This run has not transcribed the parameter formulas from
memory; read §2 of the full text for the exact shapes.)

```claim
id: prime-reduction
statement: It suffices to prove the Erdős–Straus conjecture for prime n: f(nm) ≥ f(n), so a composite counterexample would have a smaller prime-factor counterexample.
hypotheses: none.
holds-here: true.
status: asserted (paper §1, also Wikipedia; this run's brute oracle verified the scale-down identity 4/(nm) = 1/(mx)+1/(my)+1/(mz) for small m).
bearing: all ansatz work may restrict to n prime; n = 840k + r with k making n composite is irrelevant (covered via factors r_k).
anchor: research/summaries/elsholtz-tao-counting.md
```

```claim
id: type-definition
statement: For odd prime p, every solution to 4/p=1/x+1/y+1/z is Type I (p divides exactly one of x,y,z) or Type II (p divides exactly two), and f(p)=3 f_I(p)+3 f_II(p).
hypotheses: p odd prime.
holds-here: true.
status: asserted (paper §1); classical (Rosati/Salez Prop 1 is the A,B,C,D form of the same dichotomy).
bearing: every candidate family is either of Type I, Type II, or — for the ways that matter — must be neither, which Prop 1.6 forbids at squares.
anchor: research/summaries/elsholtz-tao-counting.md
```

```claim
id: vanishing-type12-odd-squares
statement: For any odd perfect square n, f_I(n)=f_II(n)=0: there is no Type-I and no Type-II solution to 4/n=1/x+1/y+1/z.
hypotheses: n an odd perfect square.
holds-here: true — this is exactly why the six square residue classes mod 840 resist the standard identity families.
status: asserted (paper Prop 1.6, with proof in §1/§2 via the parametrisations); this run quotes it from the source but has not re-proved it.
bearing: any symbolic family covering n ≡ 1 (mod 840) must, on squares in that class (e.g. n = (840k+1) with n = m²), produce a non-Type-I/II solution or fail at those n — the core obstruction.
anchor: research/summaries/elsholtz-tao-counting.md
```