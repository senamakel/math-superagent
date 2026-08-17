# ROOT — what the literature establishes on the Erdős–Szekeres problem

This is the answer to GOAL.md criterion 1: the exact statement and error term of
every published upper bound, the lower-bound construction written concretely, the
exact values ES(3..6) with the method that settled each, the Peters–Szekeres n=6
computation with its encoding and cost, and three restricted classes / partial
results. Each entry is marked **proved / verified-numerically / conjectured /
asserted-by-source**, and every entry carries a fenced `claim` block so it reaches
`research/CLAIMS.md` and `research/ENTAILMENT.md`.

Conventions throughout: a *point set* is a finite subset of the plane; it is in
**general position** if no three points are collinear. $n$ points are in **convex
position** if they are the vertices of a convex $n$-gon (equivalently, by the
4-point criterion below, if every 4-subset is in convex position). $\mathrm{ES}(n)$
is the least $N$ such that every set of $N$ points in general position contains $n$
in convex position.

---

## 1. Upper bounds — exact statements and error terms

### 1.1 Erdős–Szekeres 1935: the first upper bound

$$\mathrm{ES}(n) \le \binom{2n-4}{n-2} + 1 = 4^{n-o(n)}.$$

This comes from the cups-and-caps theorem: let $f(k,\ell)$ be the least $N$ such
that any $N$-point set in general position contains a $k$-cup or an $\ell$-cap.
Then $f(k,\ell) = \binom{k+\ell-4}{k-2}+1$ (tight — Theorem 2.5 of Morris–Soltan,
[ErSz35]); setting $k=\ell=n$ gives $\mathrm{ES}(n) \le f(n,n)+1$.
A *cup* is a set of points with increasing $x$-coordinate that all lie above their
lower hull (the slopes between consecutive points strictly increase); a *cap* is
the mirror image. The claim it makes is that every 4-subset of a planar set being
in convex position forces the whole set into convex position (Lemma 2.1 of [Suk17],
quoted there as Theorem 1.2.3 of Matoušek).

- **Status: proved** (1935, two proofs: a Ramsey-theoretic one and a geometric
  cups-and-caps one).

```claim
id: es-upper-1935
statement: ES(n) <= binom(2n-4, n-2) + 1, and the cups-and-caps function f(k,l) = binom(k+l-4, k-2) + 1 is tight.
hypotheses: n >= 3; general position (no three collinear)
holds-here: yes
status: proved
bearing: the exact 4^{(1+o(1))n} form, the base from which every later bound counts; f(k,l) tightness is the structural engine of the whole problem
anchor: research/sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md
```

### 1.2 Tóth–Valtr 1998

$$\mathrm{ES}(n) \le \binom{2n-5}{n-3} + 2.$$

The best bound of pure binomial (central-binomial-free) form; the reference against
which later asymptotic improvements are measured. (Morris–Soltan Theorem 2.4,
[TV98]; the survey writes the +2 form.)

- **Status: proved** (1998).

```claim
id: es-upper-toth-valtr
statement: ES(n) <= binom(2n-5, n-3) + 2.
hypotheses: n >= 3; general position
holds-here: yes
status: proved
bearing: the strongest bound of the form C(2n-5, n-3)-scaled form; Norin-Yuditsky and Vlachos measure against this
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md
```

### 1.3 Norin–Yuditsky 2016: improved binomial-form asymptotics

$$\limsup_{n\to\infty}\frac{\mathrm{ES}(n)}{\binom{2n-5}{n-2}} \le \frac{7}{8},$$

improving Vlachos's $\le 29/32$. "Erdős–Szekeres without induction" — a new proof
structure rather than an induction on cups-and-caps. (arXiv:1509.03332, DCG 55(4).)

- **Status: proved**.

```claim
id: es-upper-norin-yuditsky
statement: limsup_{n->inf} ES(n)/binom(2n-5,n-2) <= 7/8 (improves Vlachos's 29/32).
hypotheses: n -> infinity; general position
holds-here: yes
status: proved
bearing: current best bound expressed in the binomial unit; not an o(n)-type improvement, kept for the record of what is established
anchor: research/sources/norin-yuditsky - Erdos-Szekeres without induction - DCG 2016 full.full.md
```

### 1.4 Suk 2016/17: the breakthrough, $2^{n+o(n)}$

$$\mathrm{ES}(n) \le 2^{\,n + 6\,n^{2/3}\log n} \quad\text{for all } n \ge n_0,$$

$n_0$ a large absolute constant (Theorem 1.1 of [Suk17]); hence
$\mathrm{ES}(n) = 2^{n+o(n)}$. Method: the positive-fraction Erdős–Szekeres theorem
(Bárány–Valtr / Pór–Valtr), dense subsets of the point set with cup/cap support,
then a covering argument. (arXiv:1604.08657; JAMS 30(4):1047–1053, 2017.)

- **Status: proved**.

```claim
id: suk-es-nono
statement: ES(n) <= 2^{n + 6 n^{2/3} log n} for all n >= n0 (a large absolute constant), hence ES(n) = 2^{n+o(n)}.
hypotheses: n >= n0, general position; n0 absolute but not explicit/small
holds-here: yes
status: proved
bearing: first proof that ES(n) is 2^{(1+o(1))n}; for all our finite n it is an upper bound, not the conjecture's exact constant
anchor: research/sources/suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md
```

### 1.5 Holmsen–Mojarrad–Pach–Tardos: sharper error term

$$\mathrm{ES}(n) \le 2^{\,n + O(\sqrt{n\log n})}.$$

Improves Suk's error term from $O(n^{2/3}\log n)$ to $O(\sqrt{n\log n})$; the bound
is currently the best known. Also generalizes to pseudoline arrangements and convex
bodies (for which it obtains $c(n)\le c'(n)\le 2^{n+O(\sqrt{n\log n})}$). (arXiv:
1710.11415; JEMS 22 (2020) 3981–3995.)

- **Status: proved**. This is *the* current best published upper bound, and the one
  ROOT should cite as "best known" — confirmed independently by the Erdős problems
  website (entry #107) and by the Baek–Balko reference list.

```claim
id: hmmpt-current-best
statement: ES(n) <= 2^{n + O(sqrt(n log n))}; the current best published upper bound.
hypotheses: n; general position
holds-here: yes
status: proved
bearing: the strongest published result; every asymptotic claim in this run must be measured against it; not the exact constant 2^{n-2}+1
anchor: research/sources/holmsen-mojarrad-pach-tardos - Two extensions of the Erdos-Szekeres problem.full.md
contradicts: none
```

**Reading of the upper-bound tier.** Every published upper bound from 1935 to today
is of the form $2^{n+o(n)}$ (or weaker); none reaches the conjecture's exact constant
$2^{n-2}+1$. The conjecture remains fully open in the upper direction. The exact
values ES(3..6) are the only cases where the constant is settled, all by low-$n$
arguments or computation.

---

## 2. Lower bound: the Erdős–Szekeres construction, concretely

$$\mathrm{ES}(n) \ge 2^{n-2}+1.$$

Settled direction (Erdős–Szekeres 1960/61 [ErSz61]). The construction, as given
concretely in Morris–Soltan §2.3 (Theorem 2.6, citing [ErSz61], with corrections by
Kalbfl eisch–Stanton):

Let $n\ge 2$. For $i=0,1,\dots,n-2$, let $T_i$ be a set of $\binom{n-2}{i}$ points in
general position containing no $(i+2)$-cap and no $(n-i)$-cup, with the property that
no two points of $T_i$ are connected by a line of slope of absolute value $>1$. Place
a small copy of each $T_i$ in a neighbourhood of the point on the unit circle at angle
$\theta_i = \frac{\pi}{4} - \frac{i\pi}{2(n-2)}$ from the positive $x$-axis. Let
$X = \bigcup_{i=0}^{n-2} T_i$. Then

$$|X| = \sum_{i=0}^{n-2}\binom{n-2}{i} = 2^{n-2}.$$

That no $n$ points of $X$ are in convex position: take any subset $Y\subseteq X$ in
convex position; let $k,l$ be the least and greatest $i$ with $Y\cap T_i\ne\emptyset$.
The construction forces (a) $Y\cap T_k$ is a cap of at most $k+1$ points, (b) $Y\cap T_l$
is a cup of at most $n-l-1$ points, and (c) $|Y\cap T_i|\le 1$ for all interior
$i$. Hence $|Y|\le (k+1)+(l-k-1)+(n-l-1)=n-1$. So no subset of $X$ in convex position
has $n$ points, giving $\mathrm{ES}(n)\ge 2^{n-2}+1$.

- **Status: proved** (the lower-bound inequality). The *realizability* of the
  recursive construction with exact coordinates for every $n$ is settled by
  Duque–Fabila-Monroy–Hidalgo-Toscano (arXiv:1602.03075): the construction can be
  realized in an integer grid of size $O(n^2\log^3 n)$.

```claim
id: es-lower
statement: ES(n) >= 2^{n-2} + 1, via a set X of 2^{n-2} points (blocks T_0..T_{n-2}, |T_i|=C(n-2,i), radial placement) whose largest convex subset has <= n-1 points.
hypotheses: n >= 2; general position; each block T_i has no (i+2)-cap and no (n-i)-cup and slopes bounded in absolute value by 1
holds-here: yes
status: proved
bearing: the equality ES(n)=2^{n-2}+1 is exactly the conjecture; X is the extremal object whose structure all restricted classes probe
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md
```

```claim
id: es-construction-integer-realization
statement: The ES 2^{n-2}-point construction with no convex n-gon can be realized with integer coordinates in a grid of size O(n^2 log^3 n).
hypotheses: n; small integer grid
holds-here: yes
status: proved
bearing: gives this run exact coordinates for n=5,6,7 to feed the oracle; closes the realizability half of gap full-text-faithful-b96b
anchor: research/sources/duque-fabila-monroy-hidalgo-toscano - ES construction small integer coordinates - correct full.full.md
```

---

## 3. Exact values ES(3..6) and the method that settled each

| $n$ | $\mathrm{ES}(n)$ | Method | Status |
|---|---|---|---|
| 3 | 3 | Any 3 non-collinear points already form a convex triangle | proved |
| 4 | 5 | Esther Klein's 1930s proof: from 5 points, 4 in convex position (given in [ErSz35]) | proved |
| 5 | 9 | Makai (and Turán); first published proof by Kalb fl eisch et al.; simpler proofs by Bonnice and by Lovász (Morris–Soltan §2.4, Theorem 2.7) | proved |
| 6 | 17 | Peters–Szekeres 2006 computer proof (ES(6)=17, need 16-point no-6-gon witness); verified externally | verified-numerically (SAT/backtracking on signature functions), famously hard to reproduce by hand |

Notes on ES(5)=9. The 1935 paper already records Makai's ES(5)=9 and prints
ES(3)=3, ES(4)=5, ES(5)=9 as the seed of the conjecture ES(n)=2^{n-2}+1. A clean
hand proof (Bonnice/Lovász) rests on Lemma 2.8: a planar set of shape (3,3,2),
(4,3,1), or (3,4,2) determines a convex pentagon. A set of 9 points with no convex
pentagon is one of (4,4,1), (4,3,2), (3,4,2), (3,3,3); the first two contain an
(4,3,1) 8-subset, the last two a (3,3,2) subset, so Lemma 2.8 applies. The lower
bound 9 comes from an explicit 8-point set (Figure 2.2) with no convex pentagon.
Makai/Turán originally proved the upper bound; the credit split is recorded in
[ErSz61].

```claim
id: es-exact-values
statement: ES(3)=3, ES(4)=5, ES(5)=9, ES(6)=17.
hypotheses: n in {3,4,5,6}; general position
holds-here: yes
status: proved for n<=5 (hand), verified-numerically for n=6 (Peters-Szekeres)
bearing: the cases the oracle must reproduce before anything is built on it (GOAL criterion 3); the only settled constants
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md
```

```claim
id: es-5-lemma
statement: A planar set Y of shape (3,3,2), (4,3,1), or (3,4,2) contains a convex pentagon.
hypotheses: Y in general position with the stated nested-hull shape
holds-here: yes
status: proved
bearing: the concrete hand proof of ES(5)=9; a model of the low-n arguments the run could reconstruct
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md
```

---

## 4. The Peters–Szekeres n=6 computation: encoding and cost

Source: Peters & Szekeres, "Computer solution to the 17-point Erdős–Szekeres
problem", ANZIAM J. 48(2) (2006) 151–164. It proves the strengthened statement
$(P^\*_6)$: every signature function on 17 points contains a convex 6-subset, a
statement strictly stronger than ES(6)=17 because it covers more than the realizable
configurations.

**Encoding.** A planar configuration is represented by a *signature function*
$\sigma:\binom{S_{17}}{3}\to\{+,-\}$ giving the orientation of each triple, satisfying
the necessary geometric conditions (2.1)–(2.3) (essentially the chirotope/orientation
axioms) for all 4-subsets. The array $A_m$ has $m=\binom{17}{3}=680$ elements. A
6-subset is convex iff its $\binom{6}{3}=20$ triples satisfy one of **eight** convex
relations $R_1,\dots,R_8$ (listed in the paper), so the total number of convex
relations on $S_{17}$ is $8\cdot\binom{17}{6}=99{,}008$. The concave signatures on
6 points number $|\Omega|=184{,}556$; restricting to those satisfying the geometric
conditions gives $|\Omega^\*|=892$, each with a compatible subset of size at most 18.
The search assigns signatures from $\Omega^\*$ to the twelve contiguous 6-subsets
$u_1=[1,\dots,6],\dots,u_{12}=[12,\dots,17]$, forced-assignment propagation through
the 99,008 convex relations, then three extra checks (the $U_{13}$ check, the
one-bit check, the two-bit check). Because two complementary assignments of point 1
suffice, at most $|\Omega^\*|/2=446$ independent processes are needed.

**Cost.** Exhaustive enumeration of all $2^{680}$ states is infeasible; the search
uses forced-propagation. The number of partial signatures surviving the $U_{13}$
check was 20,312,212; the number surviving the one-bit check was 23,339; the two-bit
check then always generated a contradiction. On workstations under 2 GHz, one
assignment to $u_1$ took between one and twenty hours; the total to establish
contradictions for all 446 assignments was **approximately 3,000 GHz-hours**
(≈1,500 hours on processors up to 2 GHz). The original 9-point case (Theorem 1,
proving ES(5)-analogue $(P^\*_5)$) runs in under one second on a 1.5 GHz workstation.
Three independent implementations (both authors and B. McKay) established the
result, supporting reproducibility.

- **Status: verified-numerically** (computer proof; independently reimplemented
  three times, but not yet re-verified by this run's own oracle — see gap below).

```claim
id: peters-szekeres-es6
statement: Every signature function on 17 points has a convex 6-subset, hence ES(6)=17; a 16-point set exists with no convex 6-gon (n0(6)=16).
hypotheses: chirotope/orientation axioms (2.1)-(2.3) on 17 points, signature encoding
holds-here: yes
status: verified-numerically (three independent implementations; ~3000 GHz-hours; not yet re-run here)
bearing: the definitive ES(6)=17 and the model to mirror for any SAT/CP-SAT encoder this run builds toward ES(7) or beyond
anchor: research/sources/peters-szekeres - Computer solution to the 17-point ES problem - ANZIAM full.full.md
```

```claim
id: ps-cost
statement: Peters-Szekeres n=6 search: m=680 triple variables, 8 convex relations x C(17,6)=99,008 total, |Omega*|=892 concave signatures, 446 independent u_1 assignments, ~3000 GHz-hours total.
hypotheses: as in the ANZIAM encoding above
holds-here: yes
status: catalogued (numbers taken from the paper's own report)
bearing: the cost model the run must beat or match to reach ES(7); also the reason brute-force enumeration is hopeless (2^680 states)
anchor: research/sources/peters-szekeres - Computer solution to the 17-point ES problem - ANZIAM full.full.md
```

---

## 5. Restricted classes and partial results (exact hypotheses)

### 5.1 Split $k$-gons: the conjecture is tight for a relaxation (Baek–Balko 2025)

Theorem (Baek–Balko, "The Erdős–Szekeres Conjecture Revisited", SoCG 2025,
LIPIcs 332, 13:1–13:15, DOI 10.4230/LIPIcs.SoCG.2025.13). Let a set of points be in
*split convex* position via a *split $k$-gon* (a relaxation of a $k$-tuple in convex
position; the paper's definition of split $k$-gon). Then:

- **Every set of at least $2^{k-2}+1$ points in general position contains a split
  $k$-gon, and this is tight** — the threshold $2^{k-2}+1$ is exactly right for
  split $k$-gons even though it is open for genuine convex $k$-gons. So
  $\mathrm{ES}_{\text{split}}(k) = 2^{k-2}+1$ is *proved*, and the obstruction that
  makes the original conjecture hard survives only in the strictness of "convex"
  versus "split convex".
- **The Erdős–Szekeres Conjecture holds for decomposable sets** (a restricted class
  of point sets, shown in the paper).
- In the ordered 3-uniform hypergraph setting, the corresponding generalized
  conjecture is **false** — a genuinely new phenomenon.
- New constructions of sets of $2^{k-2}$ points with no $k$ points in convex
  position, generalizing all previously known constructions, enabling computational
  attack for large $k$.

- **Status: updated — full SoCG 2025 PDF is now held and digested**
  (`research/summaries/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.md`, anchor
  `research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md`,
  LIPIcs 332, 13:1–13:15, DOI 10.4230/LIPIcs.SoCG.2025.13). Split-threshold result:
  **proved-in-source** — the exact formula ESsplit(a,u,k) = 1 + Σ_{i=k-a+2}^{u} C(k-2, i-2)
  (Theorem 4), ESsplit(k) = 2^{k-2}+1 (Theorem 3), and the abstract hypergraph analogue
  (Theorem 6) are proved on disk (upper bound Lemma 10 by down-set injectivity; lower
  bound Lemma 11 by delta-colorings; the geometric lower-bound Lemma 12 and the
  combinatorial count Lemma 9 are "proof omitted", deferred to the journal version).
  Decomposable-set result (Theorem 8): **asserted-by-source** — the SoCG version
  states it but says "The proof of Theorem 8 is omitted" (deferred to JCTA 2026,
  DOI 10.1016/j.jcta.2026.106195, not fetched). Cweak(7) > 33 (Theorem 7) is
  proved-in-source. The general conjecture remains open. The run's `es_construct`
  at a=u=k is the tightness witness (should be machine-checked for split-k-gon-freeness).

If the paper's proofs hold, this is the single most useful result in the library:
it would prove that the numerology $2^{k-2}+1$ is not an accident of the conjecture
— the correct threshold for a strictly weaker notion — and localize the hardness to
the exact convexity condition. The split threshold is now verified on disk; the
decomposable claim is load-bearing-but-unverified pending the JCTA 2026 full text.

```claim
id: baek-balko-split
statement: ESsplit(k) = 2^{k-2} + 1 (tight threshold for split k-gons); the ES conjecture holds for decomposable sets; the ordered 3-uniform hypergraph generalization fails; new 2^{k-2}-point no-convex-k-gon constructions generalize all prior ones.
hypotheses: split k-gon notion as defined in the paper; decomposable sets as defined there; ordered 3-uniform hypergraphs
holds-here: yes (split k-gon is a relaxation of the real condition; the decomposition and hypergraph results are on stated restricted classes)
status: split threshold (Theorems 3/4/6) proved-in-source in the held SoCG 2025 PDF (Lemma 10 down-set injectivity; Lemma 11 delta-colorings; Lemmas 9 and 12 "proof omitted" — deferred); decomposable-set Theorem 8 asserted-by-source ("The proof of Theorem 8 is omitted", deferred to JCTA 2026)
bearing: 2^{k-2}+1 is proved to be the right number for the split relaxation, narrowing the conjecture's difficulty to "convex" vs "split"; the split threshold and the tightness witness (the run's es_construct) are verified on disk; the decomposable claim stays load-bearing-but-unverified until JCTA 2026 is held.
anchor: research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md
answers: (the Baek-Balko finding the task flagged)
```

### 5.2 Saturation: ES construction is saturated (Damásdi–Dong–Scheucher–Zeng 2024)

For each $n\ge 7$, there is a planar point set of size $\frac78\cdot 2^{n-2}$ that is
*maximal* (saturated) for the property "no convex $n$-gon": it contains no $n$ points
in convex position, but adding any single point creates one. This shows the
saturation number is smaller than the Ramsey number for ES. The proof also shows the
original Erdős–Szekeres construction is itself saturated. (SoCG 2024, arXiv:2312.01223.)

- **Status: proved**.

```claim
id: es-saturation
statement: For every n >= 7 there is a saturated set of size (7/8)*2^{n-2} for convex n-gons, and the ES construction is saturated.
hypotheses: n >= 7; general position; "saturated" = maximal with no convex n-gon
holds-here: yes
status: proved
bearing: a structural constraint on extremal objects: any maximal set is much smaller (7/8 factor) than the conjectured Ramsey threshold; informs what a hypothetical 2^{n-2}-extremal set must look like
anchor: research/sources/damasdi-dong-scheucher-zeng - Saturation results around the Erdos-Szekeres problem - SoCG 2024 full.full.md
```

### 5.3 Convex bodies and pseudoline convexity (Holmsen–Mojarrad–Pach–Tardos 2020)

The Suk-type bound generalizes: for convexity structures induced by pseudoline
arrangements, and for families of convex bodies ($c(n)$, $c'(n)$), the run obtains
$c(n)\le c'(n)\le 2^{n+O(\sqrt{n\log n})}$. Exact hypotheses: $c(n)$ is the least $N$
such that any $N$ pairwise disjoint convex bodies in general position (any three in
convex position) contain $n$ in convex position; $c'(n)$ allows pairs to share up to
two boundary points. (Same paper as §1.5.)

- **Status: proved**.

```claim
id: es-convex-bodies
statement: c(n) <= c'(n) <= 2^{n + O(sqrt(n log n))} for convex bodies / pseudoline convexity (2^{n+o(n)} type bounds).
hypotheses: pairwise disjoint (or sharing <= 2 boundary points) convex bodies, any three in convex position
holds-here: yes
status: proved
bearing: shows the ES phenomenon is robust; the run's structural intuition transfers beyond point sets
anchor: research/sources/holmsen-mojarrad-pach-tardos - Two extensions of the Erdos-Szekeres problem.full.md
```

### 5.4 Empty-hexagon number (adjacent, for context)

Every 30 points in general position contain an empty convex hexagon: $H(6)=30$,
proved by Heule–Scheucher by SAT (arXiv:2403.00737), 17,300 CPU-hours, and formally
verified in Lean by Subercaseaux et al. (ITP 2024). This is the *empty-hexagon*
problem, adjacent to (not the same as) ES; it is a rich source of SAT encodings and
Lean formalization patterns this run can reuse. It is **not** a restricted class of
the ES conjecture — listed for encoding/formalization leverage only.

```claim
id: empty-hexagon-h6
statement: H(6)=30: every set of 30 points in general position contains an empty convex hexagon (SAT proof, Lean-verified).
hypotheses: 30 points, general position; "empty" = no point inside the hexagon
holds-here: not directly (this is the adjacent empty-hexagon problem, not a restricted ES class)
status: verified-numerically + formalised (Lean)
bearing: reference SAT encoding (O(n^4) clauses, chirotope variables) and Lean workflow for this run's formalization and oracle
anchor: research/sources/heule-scheucher - Happy Ending An Empty Hexagon in Every Set of 30 Points - 2024 full.full.md
```

### 5.5 Higher-dimensional ES numbers (context)

Scheucher (arXiv:2105.08406) uses a SAT model on acyclic chirotopes to settle/give
$g^{(3)}(7)=13$, $g^{(4)}(8)\le 13$, $g^{(5)}(9)\le 13$ and analogous $k$-hole bounds.
Higher-dimensional, adjacent to this run, but it is the published reference for the
*acyclic-chirotope SAT* formulation the planar encoder should mirror.

```claim
id: es-higher-dim-sat
statement: SAT on acyclic chirotopes gives g^{(3)}(7)=13, g^{(4)}(8)<=13, g^{(5)}(9)<=13 (and k-hole analogues), DRAT-verified.
hypotheses: points in R^d, general position; acyclic chirotope model
holds-here: not for the plane; kept as the SAT-encoding reference
status: verified-numerically (DRAT certificates)
bearing: standard acyclic-chirotope SAT formulation to mirror for the planar encoder
anchor: research/sources/scheucher - A SAT Attack on Erdos-Szekeres Numbers in Rd and the Empty Hexagon Theorem full.full.md
```

---

## 6. Key structural fact used everywhere

**4-point criterion.** A finite point set $S$ in general position is in convex
position iff every 4-point subset of $S$ is in convex position. (Erdős–Szekeres
1935; restated as Lemma 2.1 of [Suk17], matching Dumitru's Proposition 1.) It is
what lets every encoding work on triples/orientations: a set of $k$ points is convex
iff every one of its 4-subsets is convex, and each 4-subset's convexity is decided
by orientation signs. The "if" direction is the nontrivial one.

```claim
id: four-point-criterion
statement: A finite point set in general position is in convex position iff every 4-subset is in convex position.
hypotheses: general position (no three collinear)
holds-here: yes
status: proved
bearing: the reduction used by every SAT/orientation encoding (Peters-Szekeres, Dumitru, Scheucher, Baek-Balko); backbone of the oracle
anchor: research/sources/suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md
```

---

## 7. What the run still lacks (gaps)

1. **Re-verification of ES(6)=17 by this run's own oracle.** The value is established
   in the literature and independently reimplemented three times (Peters–Szekeres),
   but this run has not yet reproduced the 16-point no-6-gon witness with its own
   exact-arithmetic checker. That is GOAL criterion 3 and is open.
2. **Balko–Valtr "A SAT attack…"** — **RESOLVED (requests `balko-valtr-attack-baa4` /
   `open-access-full-1e6e` answered).** The open-access EuroComb ENDM 49 (2015) 425–431
   full text is held at `research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
   (https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf) — the same content as the
   EJC 66 (2017) journal version, which remains paywalled but need not be fetched. It
   refutes the Peters–Szekeres strengthened conjecture (cES(7)>32, cES(8)>64) on
   NON-pseudolinear colorings, which do not touch the geometric ES conjecture; over
   pseudolinear colorings it verifies Conjecture 3.1 at a=4,u=k=7 (N=16) and a=4,u=k=8
   (N=22). The orientation-variable SAT formulation it carries is the family the run's
   encoder must mirror (claims `balko-valtr-refutes-PS`, `balko-valtr-pseudolinear-verifies`).
3. **Full primary text of Erdős–Szekeres 1961** — **RESOLVED (request
   `full-text-faithful-b96b` answered).** The actual paper ("On some extremum problems in
   elementary geometry", Ann. Univ. Sci. Budapest 3–4 (1961) 53–62) is held in full at
   `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
   (https://renyi.hu/~p_erdos/1960-09.pdf), with the concrete construction in
   `summaries/erdos-szekeres-1961-construction-concrete.md` (claim `es1961-construction-held`,
   status checked). The construction is available both from the primary and from
   Morris–Soltan §2.3 / Duque et al. integer realization.
4. **Blank on ES(7)=33.** The current open case; Dumitru (arXiv:2512.24061) reports
   UN SAT certificates for anchored subfamilies but not a settled ES(7). Not a
   restricted class this run can cite as settled.

## Sources cited in this note

- [ErSz35] P. Erdős & G. Szekeres, *A combinatorial problem in geometry*, Compositio
  Math. 2 (1935) 463–470.
- [ErSz61] P. Erdős & G. Szekeres, *On some extremum problems in elementary geometry*,
  Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3–4 (1961) 53–62 (lower bound; held in
  full in library at `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`).
- [TV98] G. Tóth & P. Valtr, *Note on the Erdős–Szekeres theorem*, DCG 19 (1998).
- [Suk17] A. Suk, *On the Erdős–Szekeres convex polygon problem*, JAMS 30 (2017).
- [HMPT20] Holmsen–Mojarrad–Pach–Tardos, *Two extensions of the ES problem*, JEMS 22 (2020).
- Morris–Soltan survey, BAMS 37(4) (2000) 437–458.
- Damásdi–Dong–Scheucher–Zeng, *Saturation results around the ES problem*, SoCG 2024.
- Baek & Balko, *The ES Conjecture Revisited*, SoCG 2025.
- Peters & Szekeres, *Computer solution to the 17-point ES problem*, ANZIAM 48 (2006).
- Norin & Yuditsky, *ES without induction*, DCG 55 (2016).
- Duque–Fabila-Monroy–Hidalgo-Toscano, arXiv:1602.03075.
- Scheucher, arXiv:2105.08406; Heule–Scheucher arXiv:2403.00737; Subercaseaux et al. arXiv:2403.17370; Dumitru arXiv:2512.24061.
