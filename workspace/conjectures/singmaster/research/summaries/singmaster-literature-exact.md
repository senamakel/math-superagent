# Singmaster's conjecture — exact statements of the known bounds and families

Question: What exactly do the literature's bounds and the interior theorem say —
hypotheses, constants, ranges — and what is left open?
This note has the full sourced statements; each is marked with its source URL and
evidence class (sourced = quoted from the primary source, a downloaded full text).

Counting convention (fixed by this run, used throughout):
`N(a)` = number of integer pairs `(n,k)` with `1 ≤ k ≤ n-1` and `C(n,k) = a`,
**counting both mirror occurrences** `(n,k)` and `(n,n-k)` and including the
trivial pair `C(a,1) = C(a,a-1)`. Under this convention `N(3003) = 8`.
(If one counts only `k ≤ n/2` and drops the trivial pair, `N(3003) = 3` "nontrivial"
interior points; the same convention must be stated before every claim.)

---

## (1) Singmaster 1971 — O(log a)

Source: D. Singmaster, "How often does an integer occur as a binomial coefficient?",
Amer. Math. Monthly 78 (1971) 385–386. doi:10.2307/2316907.
(Full text captured via Fermat's Library reproduction.)

Statement (Proposition in [Sin1]):
> N(a) = O(log a).

The precise mechanism: for a solution `C(n,k) = a` with `1 ≤ k`, from
`C(2k,k) ≥ 2^k` one gets `k ≤ log2(a)`, i.e. `k ≤ (log a)/(log 2) + O(1)`; and for each
fixed `k`, `n ↦ C(n,k)` is strictly increasing so `n` is unique. Hence the number of
solutions is at most the number of possible `k`, which is `O(log a)`.
The Fermat's Library reproduction records the sharper constant form
`N(a) ≤ 2 + 2 log2 a`.

Conjecture (same paper): "N(a) = O(1)" — the boundedness conjecture. Singmaster also
reports that Erdős, in correspondence, suggested "N(a) = O(log log a)" might be
above the truth (i.e. the true order might be slower).

Evidence class: sourced (statement and mechanism quoted from primary text /
  reproduction).

## (2) Abbott–Erdős–Hanson 1974 — O(log a / log log a)

Source: H. L. Abbott, P. Erdős, D. Hanson, "On the number of times an integer occurs
as a binomial coefficient", Amer. Math. Monthly 81 (1974) 256–261.
doi:10.2307/2319526. (Cited by de Weger 1997 and MRSTT 2021; the number
`O(log a / log log a)` is the form they proved.)

Exact form as quoted by MRSTT (Theorem-history) and by de Weger:
> N(a) = O(log a / log log a)   [AEH 1974]

de Weger's paper states it equivalently as `N(a) = O(log a · log log a)` — note this
is the same statement under a different convention about where the logarithm's base
constant goes; the MRSTT quote gives the "official" asymptotic `O(log a / log₂a)`.
de Weger also records the secondary AEH result: the **average and normal order of
N(a) is 2** (that is, almost all `a` occur only as the value itself and its trivial
row entry), consistent with N(a)=2 for typical a.

Evidence class: sourced (form quoted in two independent downloaded primary sources,
  MRSTT §1 and de Weger §1).

## (3) Kane 2004, 2007 — current record

Sources:
- D. M. Kane, "New bounds on the number of representations of T as a binomial
  coefficient", Integers 4 (2004) #A07. [Kane 2004] → N(t) = O((log t)(log₃t)/(log₂t)²)
- D. M. Kane, "Improved bounds on the number of ways of expressing t as a binomial
  coefficient", Integers 7 (2007) #A53. [Kane 2007]
  (full text downloaded from http://cseweb.ucsd.edu/~dakane/combinations2.pdf)

**Current unconditional record (Kane 2007, Theorem = Abstract):**
> N(t) = O( (log t)(log log log t) / (log log t)³ ).

This is the best-known unconditional bound on the **total** number of solutions, and
remains the record (confirmed by Wikipedia 2025, MRSTT 2021 §1, and the multinomial-
simplex paper arXiv:2107.09107). No unconditional improvement has appeared since 2007.

Conditional (AEH 1974, noted by MRSTT): assuming Cramér's conjecture on prime gaps,
> N(t) = O_ε( (log t)^{2/3+ε} )  for every ε > 0.

Mechanism: restrict to `n > 2m` (mirror symmetry + the single n=2m case); for the
implicit function `f(m) = n` solving `C(n,m)=t`, Kane proves small-but-nonzero
derivative bounds and, via a Rolle/interpolation lemma, shows the graph has few
integer lattice points. The improvement over [Kane 2004] is a sharper bound on the
lcm `B(m₁,…,m_k)` of interpolation denominators (Kane 2007 Prop. 2:
`log B = O(S max(1, log(k²log S/S)))`).

Evidence class: sourced (Kane 2007 full text read; record status independently
  confirmed by Wikipedia, MRSTT, arXiv:2107.09107).

## (4) Matomäki–Radziwiłł–Shao–Tao–Teräväinen 2021 — interior of Pascal's triangle

Source: K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, "Singmaster's
conjecture in the interior of Pascal's triangle", arXiv:2106.03335 (7 Jun 2021);
published Quart. J. Math. (Oxford).
Full text downloaded and read.

**Theorem 1.3 (Singmaster's conjecture in the interior).**
Let `0 < ε < 1`, and assume `t` is sufficiently large depending on `ε`. Then there
are at most **two** solutions `(n,m)` to `C(n,m) = t` in the left-half region
> exp( (log n)^{2/3+ε} ) ≤ m ≤ n/2.

By the symmetry `C(n,m)=C(n,n-m)`, at most **four** solutions in the symmetric
interior region
> exp( (log n)^{2/3+ε} ) ≤ m ≤ n − exp( (log n)^{2/3+ε} ).

**Moreover**, in the (smaller) region
> exp( (log n)^{2/3+ε} ) ≤ m ≤ n / exp( (log n)^{1−ε′} )
there is at most **one** solution, whenever `0 < ε′ < ε/(2/3+ε)` and `t` sufficiently
large depending on both ε and ε′.

**What is covered / the constant:** the constant is "two in each half, four total"
(note: this counts `m,n` with `1≤m<n`, the left half being `m ≤ n/2`; under this
run's convention each of those has a mirror, so the "four total" is already counting
both halves). The "sufficiently large depending on ε" threshold is **effective** but
deliberately not optimized (Remark 1.7: "likely to be too large to be of use in
numerical verification in current form"). The bound of two/four is **sharp**: the
infinite Fibonacci family (see §5) attains it.

**What is left open — the boundary rows / small k (Remark 1.5):**
Theorem 1.3 no longer says anything below `m = exp((log n)^{2/3+ε})`. By Remark 1.5,
all remaining work for Conjecture 1.1 concentrates, without loss of generality, in
the boundary region
> 2 ≤ m ≤ exp( (log n)^{2/3+ε} ),
or equivalently (via (1.7) `n/m ≍ exp((log t)/m)`), in
> 2 ≤ m ≤ (log t) / (log₂t)^{3/2−ε} .

This is precisely the `m/log t → 0` regime where `n` grows extremely rapidly with
`m`; MRSTT state this is "the main obstruction to making further progress."
**Effectiveness of the boundary: none.** The only handle on `2 ≤ m ≤ w(n)` for slowly
growing `w` is via Beukers–Shorey–Tijdeman/Siegel (finite-in-number but completely
**ineffective** — no bound on w computable). Also, the total-bound implication for the
boundary is: MRSTT's interior four bound + a boundary bound would settle the
conjecture, but there is currently **no** unconditional good bound on the boundary
region.

**Cramér-conditional comment (MRSTT):** even under the Riemann hypothesis the
equidistribution scale `P` in their Proposition 1.12 cannot be relaxed past
`N,M ≪ exp(log^{3/2−ε} P)`; a heuristic improvement would push the interior range
from `exp(log^{2/3+ε} n)` down to `(log n)^C`.

**Falling-factorial analogue (Theorem 1.8):** at most two integer solutions to
`(n)_m = t` in `exp((log n)^{2/3+ε}) ≤ m < n`, sharp.

Evidence class: sourced (full text read; exact theorem quoted).

## (5) The infinite family with N(a) ≥ 6 — Fibonacci identity

Sources:
- D. Singmaster, "Repeated binomial coefficients and Fibonacci numbers", Fibonacci
  Quarterly 13(4) (1975) 295–298 (full text read).
- Same identity noted independently by D. A. Lind (1968); also stated in MRSTT
  Remark 1.4 and de Weger §1.

Singmaster solves the equation
> C(n+1, k+1) = C(n, k+2).

Writing `m = n+1`, `j = k+2`, this reduces to a Pell-type equation
`u² − 5v² = −4` (with `u = 5j−1`). The Fibonacci/Lucas solution:

**Family (Singmaster 1975, eq. (6), MRSTT Remark 1.4 notation):**
For each `j ≥ 1`, with `F_j` the Fibonacci numbers `(F_0=0, F_1=1, F_{n+1}=F_n+F_{n-1})`,
>
> n = F_{2j+2} · F_{2j+3} − 1,
> m = F_{2j}   · F_{2j+3} − 1
>
> satisfies  C(n+1, m+1) = C(n, m+2).

The resulting common value `a` occurs **at least six times** (in the standard both-
halves, including trivial-pair count):
1. `C(n+1, m+1)` and its mirror `C(n+1, (n+1)-(m+1))`,
2. `C(n, m+2)` and its mirror `C(n, n-(m+2))`,
3. the trivial pair `C(a,1) = C(a,a-1)`.

Singmaster gives the first few `(n, k)` (his `n`, `k` with `n+1 = F_{2j+2}F_{2j+3}`,
`k = F_{2j}F_{2j+3}`): `(14,4)`, `(103,38)`, `(713,271)`, `(4894,1868)`, ... and the
`j=1` value is exactly
> C(15,5) = C(14,6) = 3003.

(The `j=2` value is `C(104,39) = C(103,40) = 61218182743304701891431482520`, i.e.
≈ 6.12×10²⁸, which does **not** recur anywhere else — verified. This is the ninth
known `a` with `N(a) ≥ 6`, per arXiv:2107.09107.)

The seven small nontrivial repetitions computed by Singmaster (up to 2⁴⁸), reproduced
by this run's oracle in witnesses.json: 120, 210, 1540, 7140, 11628, 24310, 3003.

Evidence class: sourced (primary full texts; values cross-checked: 3003 occurrences
  and the seven N≥6 witnesses are reproduced in witnesses.json; the j=2 value is
  stated in Singmaster and in arXiv:2107.09107).

## (6) de Weger (1997) and effective (Baker-method) small-k curves

Source: B. M. M. de Weger, "Equal binomial coefficients: some elementary
considerations", J. Number Theory 63 (1997) 373–386. doi: (Math Comp/NT972109).
Full text read.

Main content: for fixed `(k,l)` (say `k<l`) the equation `C(n,k) = C(m,l)` is an
algebraic curve; de Weger fully solves several small-`(k,l)` cases with **elementary /
algebraic-number-theory (Mordell) methods**, and the Baker-method cases are solved by
other groups:

- **(k,l) = (3,4)**: a curve of **genus 3** (so Faltings already gives finitely many
  rational points), but it is a **double cover of the elliptic curve**
  `Y² + Y = X³ − X` (Mordell 1963). de Weger's Theorem 1: the only integer solutions
  `(n,m)` to `C(n,3)=C(m,4)` are the trivial ones: `(n,m) ∈ {0,1,2}×{0,1,2,3}`,
  `(3,4),(3,−1),(7,7),(7,−4)`. (So no nontrivial equality `C(n,3)=C(m,4)` exists.)
  Theorem 3: a 2-power-denominator partial result on rational solutions.
- **(k,l) = (2,3)** (Avanesov, Skolem's method): completely solved.
- **(k,l) = (2,4)** (de Weger 1996 [Quart. J. Math. Oxford 47 (1996) 221–231] and
  independently Pintér 1995): solved via the **Gelfond–Baker method** (linear forms in
  logarithms), effective.
- **de Weger's Conjecture A** (his main conjecture): "The equation `C(n,k)=C(m,l)`
  has **no nontrivial solutions but those given above**" — i.e. the six one-off
  identities listed and the infinite Fibonacci family. This would imply `N(a) ≤ 8`
  for all `a ≥ 2`, and `N(a) ≤ 6` for all `a` except `a = 3003` (where `N=8`). This
  conjecture is exactly the route that would settle Singmaster; MRSTT Remark 1.4
  records that de Weger's conjecture implies Singmaster's (for sufficiently large t,
  all-but-finitely many interior binomial coefficients are distinct).

**Elliptic binomial Diophantine equations (Stroeker–de Weger 1999,**
Math. Comp. 68(227):1257–1281, doi:10.1090/S0025-5718-99-01047-9): an effective
(elliptic-logarithm / Baker-type) **algorithm** for determining all integer points on
genus-1 curves. This is the computational engine used to settle the `(m,m′)=(2,6),
(2,8), (3,6), (4,6), (4,8)` cases credited in MRSTT Remark 1.4 to [26].

**Status of fixed-(k,l) curves (MRSTT Remark 1.4/1.5):** for **fixed** `2 ≤ m < m′`,
the number of solutions to `C(n,m) = C(n′,m′)` is **finite**, proved via
Beukers–Shorey–Tijdeman (Siegel's theorem on integral points), and for
`(m,m′)=(2,3)` [Avanesov], `(2,4)` [de Weger, Pintér], `(2,5)` [Bugeaud–Mignotte–
Siksek–Stoll–Tengely], `(3,4)` [de Weger/Mordell], and `(2,6),(2,8),(3,6),(4,6),
(4,8)` [Stroeker–de Weger], plus `n ≤ 10⁶` or `t ≤ 10⁶⁰` [Blokhuis–Brouwer–de
Weger 2017]. The `(2,5)` case (Bugeaud et al. 2008) is on a **hyperelliptic** curve
and is solved with the Mordell–Weil sieve.

**Key caveat for a uniformity argument (this is the structural wall):** the
Beukers–Shorey–Tijdeman / Siegel finiteness for each fixed pair is **ineffective** in
`(m,m′)` — it gives "finitely many" with no bound computable in the parameters, and
hence cannot yield a bound **uniform in `k`**. This is exactly the "finiteness is not
a bound" trap in GOAL.md. Only the *fixed-k* effective cases (Avanesov, de Weger,
Stroeker–de Weger, Bugeaud et al.) give real constants, and each is for one specific
pair.

Evidence class: sourced (de Weger full text read; secondary credit lines in MRSTT
  full text; Bugeaud et al. and Stroeker–de Weger DOIs from search + MRSTT remarks).

---

## Summary of the current front line for the GOAL

- **Best unconditional total bound:** Kane 2007, `O((log t)(log₃t)/(log₂t)³)` — not
  effective-constant-optimized, and the constant is not computed in any source.
- **Best interior bound:** MRSTT 2021, ≤ 4 total (≤ 2 per half) for
  `exp((log n)^{2/3+ε}) ≤ m ≤ n − exp((log n)^{2/3+ε})`, effective-but-huge threshold.
- **The boundary (small-k / outer rows) is the whole remaining obstruction**, and
  every tool there (Beukers–Shorey–Tijdeman, Siegel, Faltings) is either ineffective
  in k or requires a separately-encoded genus-threshold reduction.
- **The infinite N≥6 family** (Fibonacci Pell solutions of `C(n+1,k+1)=C(n,k+2)`,
  with `n+1=F_{2j+2}F_{2j+3}`, `k=F_{2j}F_{2j+3}`) is what forces `N ≥ 6` infinitely
  often and keeps `3003` as the witness with `N=8`.
- **Genus fact relevant to the Faltings threshold** (de Weger): `C(n,3)=C(m,4)` is
  genus 3 yet still a double cover of an elliptic curve; so for the small pairs the
  effective computation is via elliptic/Baker methods, and the genus threshold where
  Faltings "takes over" is not by itself a uniform bound.
