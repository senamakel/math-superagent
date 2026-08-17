# polynomial-method-nullstellensatz — polynomial/Combinatorial Nullstellensatz encoding

## Verdict: refuted — the encoding is prior art (DeFranco's iff-Boolean-polynomial) that already stops short, and the Boolean-function literature says an efficient algebraic-witness route is not there

```approach
idea: Polynomial-method / Combinatorial Nullstellensatz representation. A
  function f : {0,1}^n → R supported on F. Union-closure is the *vanishing
  constraint*: f vanishes off F, and F is OR-closed. Construct a specific
  intended-vanishing polynomial H(x) = ∏_{construction over missing unions}
  (something) that must vanish because each factor is supported where a union is
  missing; then Alon's Combinatorial Nullstellensatz / the coefficient trick
  forces a monomial coefficient of H to be nonzero, contradicting the
  all-δ(i)<m/2 hypothesis. Distinct from the closed Fourier/Walsh line: that
  line uses the multiplicative character / influence spectral structure; this
  one uses *divisibility-by-vanishing and the degree/coefficient theorem of the
  Nullstellensatz* (Alon–Tarsi, polynomial method), a different engine that has
  never been aimed at the abundance ≥ 1/2 question.
mechanism: The core Nullstellensatz fact: an n-variable polynomial of degree
  < Σ of the grid's (d_i) that vanishes on a grid point forces — via the sign of
  a top-degree coefficient — a structural statement. Here the grid is {0,1}^n,
  so the relevant object is the multilinear polynomial that is the unique
  function agreeing with any set-map; given the abundance profile (the
  per-element marginals), build the low-degree polynomial whose support and
  degree are constrained by OR-closure, and ask what coefficient the
  "no abundant element" hypothesis forces. The mechanism is a *degree /
  coefficient* contradiction, not a moment or entropy one: a counterexample is
  a support set where every coordinate's difference operator (∂_i f = f|_{x_i=1}
  − f|_{x_i=0}, whose sum over sets is exactly 2δ(i) − m) is negative — i.e. all
  n first-differences negative — and Nullstellensatz-type forcing on a degree
  bound derived from lcm-closure could contradict that. Marked speculative; the
  honest checkable content is whether Olon's-combinatorial-Nullstellensatz type
  forcing (degree-2 multilinear constraints satisfied by every union-closed
  indicator) yields a usable coefficient bound.
status: refuted
killed-by: defranco-boolean-polynomial-encoding — the "encode the family + the
  closure premises + the no-abundant-element conclusion as polynomial vanishings
  and ask whether the system is unsatisfiable" move is EXACTLY the point of
  DeFranco (arXiv:2606.26191, "On Boolean polynomials and the Union-Closed
  Conjecture", 2026): he constructs a Boolean polynomial ICC_{m,n}(X) (in the
  equivalent Intersection-Closed form) such that UCC holds for (m,n) iff
  ICC_{m,n}(X) is the zero Boolean polynomial — an exact iff-encoding, i.e. the
  UNSAT/small-n certificate IS this construction, and DeFranco does NOT prove
  the conjecture. So the reformulation is not new, and it does not by itself
  deliver the abundance bound; the first-step's "if the quadratic Nullstellensatz
  system is already UNSAT on n≤5 that is an exact small-n certificate worth
  escalating" is precisely DeFranco's world and is where the literature stops.
  A SECOND, independent caution: Chen–De–Li–Nadimpalli–Servedio ("Testing
  Intersecting and Union-Closed Families", ITCS 2024, doi:10.4230/lipics.itcs.2024.33)
  prove union-closedness on {0,1}^n is information-theoretically hard to test —
  n^Ω(log(1/ε)) queries for non-adaptive two-sided ε-testers — so there is no
  short degree/coefficient witness that decides union-closure cheaply either;
  the exact small-n system is tractable only because n is tiny, not because the
  algebra is cheap at scale.
precedent: defranco-boolean-polynomials-ucc (https://doi.org/10.48550/arxiv.2606.26191,
  the iff-Boolean-polynomial encoding of UCC ⟺ zero polynomial);
  chen-de-li-nadimpalli-servedio-testing-uc (ITCS 2024,
  doi:10.4230/lipics.itcs.2024.33, hardness of testing union-closedness);
  lozin-zamaraev-horn (Lozin–Zamaraev, JCTA 2023, doi:10.1016/j.jcta.2023.105818,
  Boolean/Horn-function class: they settle the submodular and double-Horn
  Boolean classes — the *other* Boolean-functional line, already filed under
  the grounded boolean-fourier-influence approach);
  alon-combinatorial-nullstellensatz (Alon, CPC 8 (1999) 7–29,
  doi:10.1017/S0963548398003411).
first-step: (refuted as a route to UC — the encoding is prior art. The residual
  legitimate use is an exact small-n certificate: via DeFranco's ICC_{m,n},
  verify on n ≤ 5 that the system is UNSAT (certifying UC on that range) — but
  that is running DeFranco's machine, not a new line, and the signed small-n
  certificates are already the verified ranges (Bosnjak–Marković |∪F|≤11; the
  ITCS hardness says nothing at n≤5 because there it is cheap).)
```

## What the literature establishes

**The reformulation is prior art.** DeFranco (arXiv:2606.26191, June 2026) exactly constructs, for m subsets of an n-universe, a Boolean polynomial ICC_{m,n}(X) in the Intersection-Closed form such that the Union-Closed Conjecture is true for (m,n) **if and only if** ICC_{m,n}(X) is the zero Boolean polynomial. This is literally the mechanism proposed here — encode the family, encode the connection-closure premises and the no-abundant/rare-element conclusion as polynomial constraints, and test identically-vanishing. The candidate's distinguishing claim ("this engine has never been aimed at the abundance ≥ 1/2 question") is **false**: DeFranco aims exactly the Boolean-polynomial iff-encoding at it. What DeFranco does NOT do is prove the conjecture — he stops at the equivalence, which is the same wall every restatement hits.

**A second, independent caution.** Chen–De–Li–Nadimpalli–Servedio (ITCS 2024, doi:10.4230/lipics.itcs.2024.33) study *testing* whether a Boolean function is union-closed/intersecting and prove the union-closedness property on {0,1}^n is information-theoretically hard: n^Ω(log(1/ε)) queries for non-adaptive two-sided ε-testers (against monotonicity, which is easy). This is a strong reason not to expect a low-degree/coef-less algebraic witness that decides union-closure cheaply at scale — confirming the candidate's own "first step on n ≤ 5 by exact solving" is tractable only because the grid is tiny.

**The one legitimate surviving fragment.** The first-step's observation that "if the quadratic vanishings system is UNSAT on n ≤ 5 that is an exact, non-entropy, non-moment certificate of UC on small n" is real but is DeFranco's construction, and it reproduces only the already-machine-verified small ranges (the |∪F| ≤ 11 case, Bosnjak–Marković, is the standard small-n certificate). It gives no new bound. The Fourier/Walsh influence line (Lozin–Zamaraev's Horn/submodular Boolean classes, filed under boolean-fourier-influence) is the *other* Boolean-functional route and is already the grounded one; this polynomial/Nullstellensatz candidate is the same Boolean-function family restated through vanishing constraints, and it brings no theorem the literature already has.

## What it would have bought / why it cannot

A small-n exact certificate was the promise; but it is prior art (DeFranco) and does not climb toward 1/2. The degree/coefficient Nullstellensatz forcing on an "all first-differences negative" hypothesis was always the speculative hinge, and no source supports it; the ITCS hardness result independently cautions there is no cheap algebraic decision procedure for union-closedness at scale. Refuted on evidence (the encoding exists and stops short; hardness), not on absence.

## Negative controls

2^[n] makes the system "every δ(i) = m/2" i.e. every first-difference 0, so the all-negative hypothesis fails — the system should be trivially satisfiable-by-the-hypothesis-failing. A non-union-closed family makes one quadratic identity f(A)f(B)f(A∪B)ᶜ=0 fail. Finiteness via n ≤ 5. These hold under DeFranco's encoding too (his iff is exact).
