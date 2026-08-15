# Related equations: the Pillai tier — differences between perfect powers equal to a fixed integer

## Source URLs

- Bennett, M. A., "Pillai's conjecture revisited", J. Number Theory 98 (2003). ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0022314X02000495
- Bennett, M. A., "On Some Exponential Equations of S. S. Pillai", Canad. J. Math. 53 (2001), 897–922. https://doi.org/10.4153/cjm-2001-036-6
- Bennett, M. A., "Differences between Perfect Powers", Canad. Math. Bull. 52 (2009). https://doi.org/10.4153/cmb-2008-034-8
- Scott, R., Styer, R., "The generalized Pillai equation ±ra^x ± sb^y = c", J. Number Theory 118 (2006), 236–265. https://doi.org/10.1016/j.jnt.2005.09.001
- Scott, R., Styer, R., "Handling a large bound for a problem on the generalized Pillai equation ±ra^x ± sb^y = c", arXiv:1112.4547.
- Waldschmidt, M., "Perfect powers: Pillai's works and their developments", arXiv:0908.4031 — survey of the family; retrieved only in summary form, full text screened.

How obtained: server-side `read_sources` on the ScienceDirect and Cambridge pages; quotes below are taken verbatim from those readouts.

## Why this tier is here

problem.md's own Leads list, last row, names exactly this family as missing and
as the one "most likely to transfer": *differences of perfect powers equal to a
fixed constant other than 1, and the general question of gaps between perfect
powers.* This note fills that tier with the primary sources and their exact
statements. It is technique about the *adjacent* family `a^x - b^y = c`; the
run's own target (`x^p - y^q = 1`) sits inside it (`a = x`, `b = y` are fixed
by the problem, `c = 1`). Nothing here supplies the answer to `x^p - y^q = 1`;
the two-exponent-one-exponent problem is not the one-solution question asked.

## The Stroeker–Tijdeman theorem (Pillai's conjecture for (3,2)), as generalised

Pillai (1931, 1936) conjectured: for fixed coprime `a > b >= 2`, the equation
`a^x - b^y = c` has at most one solution in positive integers `x, y`, provided
`|c|` is larger than a constant `c_0(a, b)` depending only on `a, b`. His proof
(and Herschfeld's for `(3,2)`) used Siegel's sharpening of Thue's theorem and was
ineffective — it could not compute `c_0(a,b)`.

For the special case `(a, b) = (3, 2)` Pillai conjectured `c_0(3, 2) = 13`, from
the three two-solution equations

    3 - 2 = 3^2 - 2^3 = 1
    3 - 2^3 = 3^3 - 2^5 = -5
    3 - 2^4 = 3^5 - 2^8 = -13

**Stroeker and Tijdeman (1982)** proved `c_0(3,2) = 13` using lower bounds for
linear forms in logarithms of algebraic numbers (Baker-type). Scott later gave an
elementary proof via integers in quadratic fields.

**The generalised statement (Bennett, Pillai's conjecture revisited):**

> If `N >= 2` and `c` are positive integers, then the equation
> `|(N+1)^x - N^y| = c` has at most one solution in positive integers `x, y`,
> unless `(N, c) ∈ {(2,1), (2,5), (2,7), (2,13), (2,23), (3,13)}`.
> In the first two cases there are precisely 3 solutions; the last four have
> 2 solutions apiece.

The proof uses the **hypergeometric method of Thue and Siegel** — bounds for
fractional parts of powers of rationals — and explicitly avoids lower bounds for
linear forms in logarithms. The exceptional pairs give the equations

    3 - 2 = 3^2 - 2^3 = 2^2 - 3 = 1           (N,c)=(2,1)
    3^2 - 2^2 = 2^3 - 3 = 2^5 - 3^3 = 5       (N,c)=(2,5)
    3^2 - 2 = 2^4 - 3^2 = 7                   (N,c)=(2,7)
    2^4 - 3 = 2^8 - 3^5 = 13                  (N,c)=(2,13)
    3^3 - 2^2 = 2^5 - 3^2 = 23                (N,c)=(2,23)

Note the first row: `3 - 2 = 3^2 - 2^3 = 1` — the run's own known solution
`3^2 - 2^3 = 1` appears *inside* the exceptional set of the Pillai theorem. This
is the falsifier discipline made visible: `c = 1`, `(N,c)=(2,1)` is precisely an
exception where more than one solution exists, so any lemma claiming a universal
"at most one" over a range that includes `c = 1` here must state `c = 1` as the
exception, exactly as this theorem does.

## Bennett's sharper one-solution results (2001, Canad. J. Math.)

Scott's result (via quadratic-field integer arguments), quoted verbatim from the
readout:

> If `b > 1` and `c` are positive integers and `a` is a positive rational prime,
> then equation (1.1) `a^x - b^y = c` has at most one solution in positive
> integers `x, y` unless either `(a,b,c) = (3,2,1), (2,3,5), (2,3,13)` or
> `(2,5,3)`, or `a > 2, gcd(a,b)=1` and the smallest `t` with `b^t ≡ 1 (mod a)`
> satisfies `t ≡ 1 (mod 2)`. In these situations the equation has at most two
> such solutions.

Bennett's Theorem 1.1 (2001): for nonzero integers `a, b >= 2`, `c`, the
equation `a^x - b^y = c` has **at most two solutions** in positive integers
`x, y`. This sharpens Le (who needed `min{a,b} >= 10^5`, `min{x,y} >= 2`) and
Shorey. Bennett's theorem is essentially sharp: the pair `(a,b,c)=(3,2,1)` gives
the two solutions `(x,y)=(1,1)` and `(2,3)` — again the run's known solution
`3^2 - 2^3 = 1` is exactly the borderline case.

## The inequality form (LeVeque sharpened, Bennett 2008/2009)

"Differences between Perfect Powers" (Canad. Math. Bull. 2009):

> Let `a, b` be positive integers. There is at most one pair of positive integers
> `(x, y)` for which `0 < |a^x - b^y| < (1/4) max{a^{x/2}, b^{y/2}}`.

This sharpens a classic result of LeVeque (1952). The proof uses the
hypergeometric method of Thue–Siegel ("which, to our knowledge, has not been
applied previously in this context"), and can alternatively be obtained from
log-linear-form bounds of Laurent–Mignotte–Nesterenko for large `a, b`.

## What transfers to the run's problem

The mechanism these theorems share with the both-odd-prime case of
`x^p - y^q = 1`:

- **Which it shows is hard**: for `a, b` fixed, `c = 1` sits at the *boundary* of
  every at-most-one theorem — `(3,2,1)` is the prototype exception, and the only
  genuine unresolved one for the coprime pair `(3,2)`. In the run's problem the
  bases `x, y` are not fixed but *the thing to solve for*, so `c = 1` is not a
  small-c exception to be enumerated: it is the case where `a` and `b` are
  themselves unknown, which these fixed-base theorems do not cover.
- **The two genuinely different engines**: (i) linear forms in logarithms
  (Stroeker–Tijdeman route — effective but astronomically large constants; this
  is the source of the "finite but not computable" bound the problem statement
  describes) and (ii) the hypergeometric/Thue–Siegel method (Bennett's route —
  no such constants, but only for fixed small `(a,b)`). The library already
  holds the log-form tier (`tijdeman-linear-forms-survey.md`) and Bennett's
  hypergeometric approach is the technique recorded here. Neither extends
  directly to variable `x, y` (the run's case), which is precisely why the
  open problem stays open.
- **The falsifier check**: `3^2 - 2^3 = 1` is the canonical example in which
  two distinct exponent pairs give the same value `1`, i.e. `c = 1` has more
  than one representation as `a^x - b^y` with `(a,b)=(3,2)`. Any transfer of an
  "at most one representation" result to the run's problem must handle this or
  it is refuted by the known solution.

## Claims

```claim
id: stroeker-tijdeman-c0-3-2-13
statement: >
  For the equation 3^x - 2^y = c with c > 13, there is at most one solution in
  positive integers x, y. Equivalently c_0(3,2) = 13: for |c| > 13 the equation
  3^x - 2^y = c has at most one positive-integer solution. This is Pillai's
  conjecture for (a,b) = (3,2), proved by Stroeker and Tijdeman (1982) via lower
  bounds for linear forms in logarithms; Scott later gave an elementary proof.
hypotheses: c integer with |c| > 13; base pair (3,2), coprime.
holds-here: no — the run's problem fixes c = 1 (|c| = 1 < 13), which lies
strictly inside the excluded small-c region. The theorem says nothing about
c = 1; indeed c = 1 has the two representations (x,y) = (1,1) and (2,3), i.e.
3 - 2 = 3^2 - 2^3 = 1. So this theorem neither proves nor refutes anything
about x^p - y^q = 1; it is the adjacent-family result.
status: sourced (Bennett, "Pillai's conjecture revisited", JNT 2003, verbatim
  quote of the Stroeker–Tijdeman background).
anchor: research/sources/pillai-related-equations-stroeker-tijdeman-bennett.md
bearing: fixes the boundary of the adjacent fixed-base family; shows c = 1 is
  the small-c regime no at-most-one theorem covers when the bases are the unknowns.
```

```claim
id: bennett-at-most-two-solutions-2001
statement: >
  For nonzero integers a, b >= 2 and c, the equation a^x - b^y = c has at most
  two solutions in positive integers x, y. (Bennett, Canad. J. Math. 2001,
  Theorem 1.1; sharpens Le and Shorey, who needed min{a,b} >= 10^5, min{x,y} >= 2.)
  The bound is sharp: (a,b,c) = (3,2,1) admits the two solutions (x,y) = (1,1)
  and (2,3).
hypotheses: a, b >= 2 nonzero integers; c nonzero integer; x, y >= 1.
holds-here: no — fixes a, b as given constants. The run's problem treats x, y
as the unknowns (bases and exponents both), so the at-most-two bound over fixed
a, b does not apply. But the sharpness example (a,b,c)=(3,2,1) is exactly the
known solution's neighborhood, confirming c = 1 for the coprime pair (3,2) is
the delicate two-solution case.
status: sourced (Bennett 2001, verbatim abstract and Proposition 2.1 quotes from
  readout).
anchor: research/sources/pillai-related-equations-stroeker-tijdeman-bennett.md
bearing: the strongest quantitative "how many representations of a fixed value
  as a^x - b^y" type statement in the library for the fixed-base family; the
  mechanism (hypergeometric/Thue–Siegel vs log-forms) is the transferable part.
```

```claim
id: bennett-inequality-at-most-one-2008
statement: >
  Let a, b be positive integers. There is at most one pair of positive integers
  (x, y) for which 0 < |a^x - b^y| < (1/4) max{a^{x/2}, b^{y/2}}. Sharpens
  LeVeque's classic result on near-equalities of perfect powers, by the
  hypergeometric method of Thue–Siegel.
hypotheses: a, b positive integers; x, y positive integers.
holds-here: no — a, b fixed; the inequality form does not cover equality c = 1
  as the run's problem needs it (bases are the unknowns).
status: sourced (Bennett 2008/2009 abstract, verbatim from readout).
anchor: research/sources/pillai-related-equations-stroeker-tijdeman-bennett.md
bearing: shows the run's problem sits at the equality boundary (right-hand side
  limit 1/4 not attained, c = 1 exactly); the two-solution sharpness of the
  (3,2,1) case is the closest neighbouring result.
```

## Relation to the known solution (falsifier)

The known solution `3^2 - 2^3 = 1` is, verbatim, one of the two solutions of
`3^x - 2^y = 1` (the other being `3^1 - 2^1 = 1`). So within the fixed-base
family `(a,b) = (3,2)`, the value `c = 1` has **two** representations — it is
the archetypal exception to every at-most-one statement, by every source above.
The run's problem differs only in that it does not fix `(x, y) = (3, 2)` as
bases: it asks whether *any* coprime pair of bases can represent `1` as
`x^p - y^q`. These sources independently confirm that `c = 1` is precisely the
boundary where small cases cluster, and that the two routes (log-forms,
hypergeometric) both stop exactly there.
