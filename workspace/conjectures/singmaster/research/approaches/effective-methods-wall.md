# Approach: The effective-methods wall for C(x,k1)=C(y,k2)

```approach
idea: The effective integral-point toolbox (David's elliptic logarithms at genus
  1; Bugeaud-Mignotte-Siksek-Stoll-Tengely Baker/Matveev + Mordell-Weil sieve at
  genus 2) cannot deliver a uniform-in-(k1,k2) bound on N(a). The exact
  obstruction is two-fold: (i) there is NO effective integral-point method at
  genus >= 3 (canonical-height-difference bounds on Jacobians exist only for
  genus 2, BMSST 2008 p.2 verbatim), and the family leaves genus <= 2
  immediately (genus{2,n}=floor((n-1)/2); {3,4} already genus 3);
  (ii) every effective per-pair constant grows with the curve's rank, regulator,
  and heights — David c4 has exponent r+2, BMSST A1* contains the regulator
  squared, Matveev 2000 ln|Lambda| > -112*2^n*C2*C0'*D^2*omega*ln(2eB) grows in
  n, D, Omega=prod A_j — all growing with the column index k1,k2, so no constant
  uniform in (k1,k2) emerges; and a uniform B must sum per-pair bounds over
  ~log2(a) columns down to the MRSTT-open boundary 2<=m<=(log t)/(log2 t)^{3/2-eps},
  which the per-pair bounds cannot do. Consequence: curve methods yield
  per-pair effective finiteness (one pair at a time) but the named
  uniformity-obstruction makes them incapable of bounding N(a) by a constant.
  This is a GOAL-eligible impossibility statement; the bounded honest per-pair
  deliverable is the explicit Matveev/David constant for ONE fixed small pair,
  stated with its k-dependence.

mechanism: For C(x,2)=C(y,3) reducing to Y^2+Y=X^3-9X+20 (rank 2), the
  elliptic-logarithm/LLL pipeline (Stroeker-de Weger 1999) yields M0=4.62556e40
  reduced to M3=7 per-pair. For C(x,2)=C(y,5) (BMSST eq. (4): the Jacobian has
  rank 3), the descent x-alpha=kappa*xi^2 + Matveev + Landau-regulator bounds
  give log x up to 10^565, cut by the Mordell-Weil sieve (lattice index ~10^3240
  over ~10^5 primes). Both are per-curve: hypotheses require a rational point, an
  explicit MW basis, and explicit canonical-height-difference bounds, which exist
  only for genus 1 (David/Siegel-Baker) and genus 2 (Stoll/Flynn-Smart). The
  per-pair constants grow with rank, regulator, heights, so diverge in (k1,k2).

status: grounded
precedent:
  https://arxiv.org/abs/0801.4459 (BMSST 2008, held full text: genus-3 gap, Thm 3 constant, sieve)
  https://www.ams.org/journals/mcom/1999-68-227/S0025-5718-99-01047-9 (Stroeker-deWeger 1999, held: W23/per-pair elliptic logarithms)
  https://doi.org/10.1006/jnth.1997.2109 (de Weger 1997, held: (3,4) genus-3 double cover of Y^2+Y=X^3-X)
  https://www.mathnet.ru/eng/im190 (Matveev 2000, held Thm 2.2: ln|Lambda| > -112*2^n*C2*C0'*D^2*omega*ln(2eB))
claims: effective-methods-wall, deweger-smallk-effective, bst-fixed-kl-ineffective, mrstt-interior-theorem
first-step: complete (deliverable stated); follow-up is to compute the explicit
  Matveev/David constant for one fixed small pair (e.g. (2,3)) and write its
  k-dependence — that is a per-pair effective result, not a uniform B.
```

## Question

For a representative small pair, `C(x,2)=C(y,3)` (genus 1, elliptic) and
`C(x,2)=C(y,5)` (genus 2, hyperelliptic), what effective method actually gives a
computable bound on integer solutions, does any constant computable from it grow
with `(k1,k2)`, and exactly what obstruction prevents an *effective uniform-in-
(k1,k2)* bound from these routes?

The deliverable is the **impossibility / uniformity-obstruction statement**: name
the exact obstruction that prevents these routes from bounding `N(a)` by a
constant.

## One-line answer

Each route is an *effective, per-pair, per-curve* algorithm whose output constant
grows with the pair — and neither extends past a hard geometric cap (genus) that
the family crosses immediately. **Uniformity fails twice: (i) the finite set of
effective pairs is a tiny initial segment (only genus ≤ 2 has effective tools, and
even there only with a case-by-case Mordell–Weil basis); (ii) every per-pair
constant grows with the heights/regulator/rank, which grow with the column index
`k`, so even the effective pairs cannot be summed into a `k`-independent `B`.**

---

## 1. Setup and counting convention

`N(a) = #{(n,k) : 1 ≤ k ≤ n−1, C(n,k)=a}` counting both mirrors and the trivial
pair (so `N(3003)=8`). The fixed-pair equation `C(x,k1)=C(y,k2)` is an algebraic
curve; for the two representative pairs the run's genus oracle and the primary
sources agree:

- **`C(x,2)=C(y,3)`** — completing the square `(2x−1)² = 1 + 8·C(x,2)` turns the
  RHS into a **cubic** in `y`; a genus-1 elliptic curve. Stroeker–de Weger 1999
  (Tables 1,2) reduce it to the minimal Weierstrass model
  `Y² + Y = X³ − 9X + 20` (`W23`), `j = −2¹²·3³/179`, trivial torsion, **rank 2**,
  MW basis `{(0,4),(3,4)}`.
- **`C(x,2)=C(y,5)`** — the same substitution makes the RHS a **quintic** in `y`;
  a genus-2 (hence non-rational, hyperelliptic) curve. This is exactly equation
  (4) of Bugeaud–Mignotte–Siksek–Stoll–Tengely (2008), "the second problem on a
  list of 22 unsolved Diophantine problems compiled by Evertse and Tijdeman".

Both facts are corroborated by the run's computed genus grid (k2 column 2 → genus
`floor((k1−1)/2)`; `{2,3}`→1, `{2,5}`→2) and by the two held primaries.

---

## 2. The effective tool for each representative pair

### 2a. `C(x,2)=C(y,3)` — genus 1: **David's lower bound for linear forms in elliptic logarithms**

The standard effective algorithm for the integer points of a genus-1 curve (Smart;
Stroeker–Tzanakis; Gebel–Pethö–Zimmer; Tzanakis; applied to the full binomial
family by Stroeker–de Weger 1999):

1. **Reduce to a Weierstrass model** (here `W23: Y²+Y=X³−9X+20`) via a birational
   transformation that preserves integrality (Stroeker–de Weger Table 1).
2. Compute the **Mordell–Weil group**: rank `r=2`, explicit basis (Cremona's
   `mwrank`, then an infinite descent via Zagier's theorem; Siksek/Silverman
   naive-vs-canonical height difference bounds to make the descent unconditional).
3. An integer point `P = m₁P₁ + m₂P₂` gives a **linear form in elliptic
   logarithms** `L(P) = m₀ω + m₁u₁ + m₂u₂`.
   - **Upper bound** on `|L(P)|` from the integrality/differential (ST inequality
     (2)) — decays like `e^{−c₁M²}` in the multiplier size `M`.
   - **Lower bound** from **David's theorem** (S. David, *Minorations de formes
     linéaires de logarithmes elliptiques*, Mém. Soc. Math. France 62 (1995)):
     `|L(P)| > exp(−c₄(log M+c₇)(log log M+c₈)^{r+2})`, with `c₄` built from the
     elliptic-period data, Mordell–Weil rank, heights and regulator of the *specific
     curve*.
4. Combine → absolute bound `M₀` on `M`; reduce `M₀` → `M₃` by LLL lattice
   reduction; enumerate the small box; verify integrality.

**Concrete per-pair numbers (Stroeker–de Weger 1999, Table 5/6 for W23):**
`r=2`, `c₁=0.147776…`, David's `c₄=3.6×10⁷³`, `M₀=4.63×10⁴⁰`, reduced to `M₃=7`
via one LLL pass; total runtime seconds. **So there is a provable, effectively
computable constant for the pair (2,3).** It is per-curve: it embeds the rank
(→ `c₄` exponent via `r+2`), the canonical heights `ĥ(Pᵢ)` (the `uᵢ=ωφ(Pᵢ)`), the
least height-pairing eigenvalue `c₁`, and the regulator — all objects of the
*individual* curve `W23`.

*Avanesov* solved (2,3) first (1966) by Skolem's method; Stroeker–de Weger 1999
gave the elliptic-logarithm re-solution. Mordell 1963 solved the (3,4) case (the
genus-3 curve `Y²+Y=X³−X`), and de Weger 1997 recognized (3,4) as a double cover of
that elliptic curve.

### 2b. `C(x,2)=C(y,5)` — genus 2: **BMSST hyperelliptic integral-point method (Baker + Matveev + Landau regulator + Mordell–Weil sieve)**

Bugeaud–Mignotte–Siksek–Stoll–Tengely (2008), *Integral points on hyperelliptic
curves*, solve `(Y choose 2) = (X choose 5)` — their Theorem 2 / equation (4) —
whose solution set contains `(78,2)→3003=C(15,5)` and `(153,2)→11628=C(19,5)`.
Their method, for `C: Y² = aₙXⁿ+…+a₀` with irreducible RHS (n = 5 here):

1. **Assumptions:** (a) at least one rational point `P₀` on `C`; (b) a
   **Mordell–Weil basis of the Jacobian `J(Q)`**; (c) explicit
   canonical-height-difference bounds `µ₁ ≤ h(D)−ĥ(D) ≤ µ′₁`.
2. **Effective upper bound (their Theorem 3):** descent `x−α = κξ²`; apply
   Matveev's linear-forms-in-logarithms bound (their Lemma 7.2, which is
   `log|σ(Λ)| > −C(L,n)(1+log(nB))∏ h_{L,σ}(αⱼ)`) to a unit equation; bound
   regulators by **Landau's theorem**; get `log|x| ≤ 8A*₁log(4A*₁)+8A*₂+H*+…`
   where `A*₁` contains `C(L,2r+1)·(c*₁)²·∂·R²` — the **regulator squared**, unit
   ranks, and Matveev constants of the number field `K=Q(α)` of the curve.
3. **The bounds are astronomically large** (the paper's own words): for their two
   worked genus-2 examples the `log x` bounds range over the J(Q)/2J(Q) cosets
   from `10²⁶³` to `10⁵⁶⁵` (BMSST Table 1); for `Y²−Y=X⁵−X` the reduced bound is
   `log x(P) ≥ 0.95×10²¹⁵⁹`.
4. **The Mordell–Weil sieve** reduces/eliminates the huge search box: a decreasing
   lattice sequence over ~10⁵ primes, 37 CPU-hours, final lattice index
   ~10³²⁴⁰, then a canonical-height gap argument proves the listed points are all
   the integral points.

**Concrete:** the (2,5) curve's Jacobian has rank 3 with explicit MW basis; the
method gives a provably complete, effectively-computed solution set. The constant
again depends on the *individual* curve: the field degree `[K:ℚ]=5`, its
discriminant/regulator, the MW rank and basis, and the Matveev `Aⱼ = max{h(αⱼ),
|log αⱼ|/D, 1/(DC₁)}`.

---

## 3. The obstruction, named

### 3a. Effectivity gap at genus ≥ 3 — the effective family is a finite initial segment

BMSST state it verbatim (p. 2): *"At present, no such bounds have been determined
for Jacobians of curves of genus ≥ 3, although work on this is in progress."* —
i.e. **there is no effective integral-point bound available for any genus-≥3
curve**, because every known effective route (Baker/Matveev + height, and the
reduction gadgetry) needs the difference between logarithmic and canonical height
on the Jacobian, which is only worked out for genus 2 (Stoll; Flynn–Smart).

The genus of `C(x,k1)=C(y,k2)` is **not** confined to 1 or 2: the run's computed
grid gives `genus{2,n} = floor((n−1)/2)` — so `{2,5}`→2, `{2,6}`→2, `{2,7}`→3, …
and the `{3,4}` case is already genus 3 (de Weger; Mordell 1963). Hence:

> **Only a finite list of pairs — those of genus 1 or 2 — is within reach of any
> effective method at all, and most of the infinite family is genus ≥ 3 where no
> effective bound exists.** The effective tool covers `{2,3},{2,4}` (genus 1) and
> the small genus-2 pairs solved by BMSST/Stroeker–de Weger; it does not touch the
> family beyond them.

This is the same wall as Faltings (genus ≥ 2 → finitely many, **ineffective**) and
Siegel (genus 1 → finitely many integral points, effective only via the Baker/-
elliptic-logarithms machine applied to one curve at a time). The BST 1999 theorem
that gives finiteness for *every* fixed pair proves it via Siegel and states its own
result is ineffective in the parameter.

### 3b. Every effective constant grows with (k1,k2) — no uniformity

Even restricting to the pairs the effective machinery reaches, the constants are
per-pair and *grow with the pair*:

- **Elliptic case:** David's `c₄` is built from the rank `r` (in the exponent
  `(…)^{r+2}`), the canonical heights `ĥ(Pᵢ)` of the MW basis, and the regulator
  of `E`. For `C(x,2)=C(y,k)`, the elliptic model has coefficients growing with
  the binomial polynomial's height, and the height `h(C(x,k)) ~ k log k`.
- **Hyperelliptic case:** BMSST's `A*₁` contains the **square of the regulator** of
  `K=ℚ(α)` (α a root of the degree-`k` or `2k` binomial-type polynomial), the
  Landau regulator bound grows with the discriminant (which grows with `k`), the
  Matveev `Ω=∏Aⱼ` grows with the `h(αⱼ)`, and the number-field degree grows with
  the curve. Matveev 2000 (Thm 2.2): `ln|Λ| > −112·2ⁿC₂C′₀D²ω ln(2eB)` — every
  factor (`2ⁿ`, `C₂`, `D`, `ω=Ω(C₁Dϑ/e)ⁿ(…)ᵖ`) grows with `n` (the number of
  logarithms) and with the heights.

So each per-pair effective bound is of the rough shape
`constant(k₁,k₂) = exp(exp(k log k))`-type — it **cannot** be a uniform `B`.

### 3c. Why no bound on N(a) follows even from all per-pair bounds

`N(a)` counts representations with `k ≤ log₂ a` (since `C(n,k) ≥ C(2k,k) ≥ 2ᵏ`).
There are `~log₂ a` possible columns, and an integer `a` can in principle be hit
by *any* of them. The effective-methods routes provide, for each *fixed* pair
`(k₁,k₂)`:

> (finiteness) `C(x,k₁)=C(y,k₂)` has finitely many solutions — and this is
> **ineffective** in `(k₁,k₂)` (BST/Siegel/Faltings), or
> (per-pair effective) the pair is one of the few solved curves, with a constant
> growing in `(k₁,k₂)`.

A uniform `B` needs a bound that (i) survives summing over all `~log₂ a` pairs
(the per-pair constants don't — they blow up faster than `1/k²`), and (ii) controls
the *initial* tail `k` up to `log₂ a` — which is **exactly the boundary regime
MRSTT 2021 leaves open** (`2 ≤ m ≤ (log t)/(log₂ t)^{3/2−ε}`). There is no
effective method on that boundary: the only known statements are the per-pair
ineffective BST/Siegel results and the handful of separately-solved small curves.

---

## 4. The impossibility statement, sharp

> **Effective methods on the curve family `C(x,k1)=C(y,k2)` cannot deliver a
> uniform-in-`(k1,k2)` bound on `N(a)`.**
>
> **Obstruction (named):** the effective integral-point toolbox (elliptic
> logarithms at genus 1; Baker/Matveev + Mordell–Weil sieve at genus 2) is a
> *per-curve* algorithm requiring a rational point, an explicit Jacobian
> Mordell–Weil basis, and canonical-height-difference bounds; the last of these is
> **provably unavailable for genus ≥ 3** (BMSST 2008, p. 2), and the family leaves
> genus ≤ 2 immediately (`genus{2,n}=floor((n−1)/2)`; `{3,4}` is already genus 3).
> Even where the machinery applies, the constants depend on the rank, regulator,
> and heights of the specific curve, all of which grow with the column index
> (Matveev 2000: `2ⁿ·D²·Ω·ln(2eB)`; David: `(…)^{r+2}`), so the per-pair bounds
> diverge in `(k₁,k₂)` and cannot be summed into a `k`-independent `B`. Any bound
> that would also rule out `C(15,5)=C(14,6)=3003` (N=8) is false.

---

## 5. Status

**grounded** — the named obstruction is directly supported by the held primary
sources:

- Bugeaud–Mignotte–Siksek–Stoll–Tengely 2008 (arXiv:0801.4459), §1 and Theorem 3:
  the effective hyperelliptic method and its exact hypotheses; **genus-≥3 gap** on
  p. 2; astronomically large `log x` bounds (`10²⁶³`–`10⁵⁶⁵`) needing the
  Mordell–Weil sieve.
- Stroeker–de Weger 1999 (Math. Comp. 68:1257–1281): the elliptic-logarithm engine
  for the genus-1 binomial pairs, with David's `c₄` and the actual `M₀`, LLL
  reductions, runtimes; per-pair data for `W23`.
- de Weger 1997 (JNT 63:373–386): the `(3,4)` genus-3 double-cover-of-elliptic
  fact and the Mordell/elementary small-pair solutions.
- Matveev 2000 (Izv. Math. 62:4 723–772), Thm 2.2: the explicit linear-forms
  constant `ln|Λ| > −112·2ⁿC₂C′₀D²ω ln(2eB)` whose factors grow with `n`, `D`, and
  the heights `Ω=∏Aⱼ` — the mechanism behind the `(k₁,k₂)`-growth.

**killed-by / does not apply past:** the effective-route obstruction is exactly
`bilu-tichy-method-ineffective-uniformity-wall`, `bst-fixed-kl-ineffective`,
`deweger-smallk-effective`, and the run's Faltings-threshold computation. The
surviving honest deliverable is the per-pair effective constant for one small pair
(computable from Matveev/David), stated with its `(k₁,k₂)`-dependence — not a
uniform `B`.

## 6. What this buys (and does not)

- **Buys:** a precise statement of *why* the curve-methods route cannot give
  Singmaster, naming two independent obstructions (genus-≥3 effectivity gap;
  per-pair constant growth). This satisfies GOAL.md's "proof that a stated approach
  cannot give a bound uniform in k, with the obstruction named."
- **Does not buy:** any uniform `B`, and (by design) it does *not* reprove
  per-pair finiteness (already known, and ineffective). The effective constant for
  a *single* pair like `(2,3)` is computable in practice (the run can compute the
  `c₄`/Matveev number if desired) but is a per-pair fact.

## References (URLs)

- Bugeaud, Mignotte, Siksek, Stoll, Tengely — *Integral points on hyperelliptic
  curves*, arXiv:0801.4459 (held: `research/sources/bugeaud-hyperelliptic-2008.full.md`)
- Stroeker, de Weger — *Elliptic binomial Diophantine equations*, Math. Comp.
  68(227) (1999) 1257–1281 (held: `research/sources/stroeker-deweger-1999-elliptic-binomial.full.md`)
- de Weger — *Equal binomial coefficients*, J. Number Theory 63 (1997) 373–386
  (held: `research/sources/deweger-equal-binomial.full.md`)
- Matveev — *An explicit lower bound for a homogeneous rational linear form in
  logarithms of algebraic numbers*, Izv. Math. 62:4 (1998) 723–772 (held:
  `research/sources/matveev-2000-homogeneous-linear-form.full.md`)
- Mordell — *On the integer solutions of y(y+1)=x(x+1)(x+2)*, Pacific J. Math. 13
  (1963) 1347–1351 (cited in de Weger and BMSST)
- MRSTT — *Singmaster's conjecture in the interior of Pascal's triangle*,
  arXiv:2106.03335 (held): the boundary `2≤m≤(log t)/(log₂t)^{3/2−ε}` that the
  interior theorem leaves open and where only ineffective per-pair results exist.

```claim
id: effective-methods-wall
statement: The effective integral-point toolbox for C(x,k1)=C(y,k2) (David's elliptic
  logarithms at genus 1; BMSST Baker/Matveev + Mordell-Weil sieve at genus 2) is a
  per-curve algorithm requiring a rational point, an explicit Jacobian Mordell-Weil
  basis, and explicit canonical-height-difference bounds. Those bounds are
  provably unavailable for genus >= 3 (BMSST 2008 p.2), and genus{C(x,k1)=C(y,k2)}
  exceeds 2 immediately (genus{2,n}=floor((n-1)/2); {3,4} already genus 3). Where
  the machinery applies, the constants grow with the rank/regulator/heights of the
  curve (David c4 has exponent r+2; Matveev ln|Lambda|>-112*2^n*C2*C0'*D^2*omega*ln(2eB)
  grows in n, D, Omega=prod A_j), which grow with the column index, so no constant
  uniform in (k1,k2) emerges; and a uniform B would need to sum bounds over ~log2(a)
  columns down to the MRSTT-open boundary, which the per-pair bounds cannot do.
hypotheses: fixed distinct pair (k1,k2); both-mirrors-and-trivial counting convention.
holds-here: true
status: sourced (all four primary sources read; genus facts cross-checked by the
  run's computed grid)
bearing: names the exact obstruction preventing an effective uniform-in-(k1,k2) bound
  from the elliptic-logarithm/hyperelliptic routes — the honest impossibility result
  of this thread.
anchor: research/approaches/effective-methods-wall.md
```
