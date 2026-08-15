# Fractional chromatic number as a polynomial-time lower-bound certificate

```approach
idea: Use the fractional chromatic number chi_f — the LP relaxation of colouring,
computable in polynomial time (exactly over Q for small graphs) — as a one-sided
certificate chi(G) >= ceil(chi_f(G)). Since chi of the plane is the sup over
finite unit-distance graphs, chi_f > 4 on any finite UDG proves chi >= 5 with an
LP certificate (a feasible dual / an explicit fractional colouring of weight > 4),
a strictly weaker demand than exhibiting a non-4-colourable graph, and one
verified by linear programming rather than a SAT refutation.
status: adopted
first-step: (tool_builder-ready) Write code/lib/frac_chromatic.py implementing
chi_f exactly over Q for n <= 30 via the independent-set LP (dual form: max
w(V) s.t. w(S) <= 1 for every independent set S, with stable sets enumerated by
a bounded search; or the primal via sympy's exact LP). Calibrate on known values:
chi_f(C5) = 5/2, chi_f(diamond) = 3 (diamond is chordal, hence perfect, hence
chi_f = chi). Then compute chi_f(Moser spindle) and chi_f(Moser+Moser) — the
exact values are new information and must be <= 4 (their chi is 4) — and use
chi_f as the graded objective over the Minkowski-sum/spindle tiers: chi is frozen
at 4 across the whole constructible family, so chi_f's motion in (3,4] is the
only continuous signal of accumulating rigidity. Target invariant: chi_f(R^2)
itself; a constructible chi_f > 4 is a polynomial-checkable LP-dual certificate,
and a proved sup over constructibles of <= 4 bounds what the LP route can buy.
mechanism: chi_f is a different invariant from both the adopted theta SDP and the
refuted circular-chromatic number. Theta is the semidefinite sandwich bound
omega <= theta(Gbar) <= chi; chi_f is the polyhedral bound chi_f <= chi (equality
for perfect graphs), obtained by an LP, not an SDP, so it can be strictly stronger
and is certified by a linear-programming dual rather than an SDP dual. Crucially
it does not share the refutation of the circular-chromatic line: that line died
because chi = ceil(chi_c) makes "chi_c > 4" exactly as hard as the 4-colouring
SAT. chi_f has no such identity — chi_f > 4 is a *polynomial-time-checkable*
one-sided certificate, so it is a genuinely easier and independent route to the
same lower bound. The run has never computed chi_f on any of its graphs; the open
question the mechanism poses is whether any constructible UDG (or any UDG at all)
has chi_f > 4, and if the sup over finite UDGs equals 4 exactly then that
negative fact — a theorem about the fractional chromatic number of the plane — is
itself a durable, citable result that would bound what the LP route can do.
precedent:
  - Definitive LP formulation, both primal (min sum of weights over independent
    sets, covering each vertex to weight >= 1) and dual (max vertex weighting s.t.
    every independent set has weight <= 1); strong duality. Standard; e.g. the
    "Fractional coloring" expository page and Scheinerman–Ullman "Fractional
    Graph Theory".
  - chi_f(G) = max_w w(V)/alpha_w(G) over weightings w (independent-set weighted
    alpha). For vertex-transitive graphs chi_f = |V|/alpha(G). (Scheinerman-Ullman.)
  - Exact computation is **NP-hard**: the independent-set LP has exponentially
    many variables, and separating independent sets is hard; approximating chi_f
    within any constant factor is NP-hard even on bounded-degree graphs (Khot
    2001; Gvozdenovic–Laurent "Approximating the chromatic number..."; Suomela's
    cstheory answer). So "polynomial time exactly over Q" in the candidate is
    FALSE in the worst case — it is only feasible for the run's tiny graphs where
    the independent-set polytope can be enumerated exhaustively. This is a
    correction to the mechanism's stated complexity, not a refutation for the
    graphs that matter (n <= ~26 here).
  - chi_f <= chi always (chi_f is a relaxation); chi(G) = ceil(chi_c(G)) identity
    (why circular died); chi_f has NO such identity so chi_f > 4 is a strictly
    easier one-sided certificate — the candidate's central (correct) claim.
  - The plane value: whether sup over finite UDGs of chi_f exceeds 4 is open; the
    literature's answer-tier on the plane's *fractional* chromatic number is
    censored at this run's network boundary, so it must be COMPUTED, not sourced.
  - claim sat-k-colourability-encoding (the exact oracle); claim
    lovasz-sandwich-theta (the adopted SDP sandwich this LP route is distinct
    from); claim circular-chromatic... (the refuted analogue it does not inherit).
grounded-by: chi-f-is-a-correct-one-sided-relaxation-without-the-ceil-identity
```

## Literature verdict

The **technical claim in the mechanism is correct and distinguishes this from
both closed lines.** chi_f is the LP relaxation chi_f <= chi; it is NOT related
to chi by an identity like chi = ceil(chi_c), so deciding "chi_f > k" is strictly
easier than deciding "chi not k-colourable" — there is no ceil-identity that
would make the threshold exactly as hard as the colouring SAT. So chi_f > 4 is a
genuinely one-sided, LP-certifiable route to chi >= 5 that is independent of the
circle-chromatic line (which died on the ceil identity) and can beat the theta
SDP (which can sit at 4 while chi_f crosses). The candidate's contrast against
the two closed relaxations is accurate.

**Two corrections, neither fatal to the idea but both load-bearing.**

1. **"Polynomial time exactly over Q" is wrong in general.** Chi_f is NP-hard to
compute and to approximate even on bounded-degree graphs (Khot 2001; the
Gvozdenovic–Laurent theorem even shows no polynomial-time computable parameter
can lie strictly between chi_f and chi unless P=NP). It is *feasible here* only
because the run's graphs are tiny (n ≤ 26) and the independent-set polytope can
be enumerated exhaustively. The mechanism should say "exact but exponential in
the worst case, cheap for the run's sizes," not "polynomial-time." This is a
complexity misstatement, not a refutation of the value for the graphs that
matter.

2. **The value question is a computation, and the run has never done it.** The
CEntral open question — does any constructible UDG (or any UDG at all) have
chi_f > 4 under the plane's unit distance? — is not settled by any source I can
retrieve (the plane's fractional-chromatic answer tier is censored at this run's
network boundary, per REQUESTS.md). The run's record contains no chi_f value for
any of its graphs. So the honest state is: the *method* is grounded and correct;
whether it *fires* on the constructible family is completely open and demands a
computation, exactly as the first-step says.

## Decision — grounded, with the two corrections recorded

The method is **correctly stated as a one-sided relaxation** and is genuinely
distinct from both adopted/refuted lines (theta SDP was adopted; circular died on
the ceil identity; chi_f shares neither defect). It does not re-propose a closed
approach. The two caveats are: (i) the complexity is exact-but-exponential in the
worst case, cheap only because the run's graphs are tiny (independent-set polytope
enumerable), and (ii) its *value* — whether chi_f ever exceeds 4 on a constructible
UDG — is a genuine open computation the run has never performed. That second
question is precisely the run's own style of result either way: a constructible
chi_f > 4 is a certified chi >= 5 (LP dual certificate), and the negative answer
(a theorem that every constructible/small UDG has chi_f <= 4, or stronger) bounds
what the LP route can ever buy. First concrete artifacts the approach should
produce, in order: chi_f(C5) = 5/2, chi_f(diamond) = 3, chi_f(Moser) (should be
<= 4 since chi(Moser)=4), chi_f(Moser+Moser). A scaffold for exactly this
computation is on disk at `code/frac_chro_calib.py` but has not been run.

**Killed-by:** (none — not refuted; both objections are corrections to the
mechanism's complexity claim and to its computational burden, not counterexamples
to the method.)

## Convergence decision — adopted (refined)

Adopted over the WL filter and the (already refuted) quadratic-field line. The
research verdict's two corrections are accepted into the adopted form: (i) the
complexity claim is "exact but exponential in the worst case, cheap only because
the run's graphs are tiny (n <= 26, independent-set polytope enumerable)", not
"polynomial time"; (ii) the value question is a computation the run has never
performed, not a fact.

The refinement that turns a certificate-afterthought into a line of attack:
**chi_f is a graded objective on the construction family while chi is frozen at
4.** Every graph the run can currently build is 4-colourable, so the integer
invariant gives zero search signal — it is stuck at 4 across the whole family.
chi_f sits in [omega, chi] (C5: 5/2 < 3 = chi; diamond/chordal: 3 = chi), and for
the run's 4-chromatic non-perfect graphs its exact value — strictly below 4 or
not — is the new information to compute. Maximising chi_f over the
Minkowski-sum/spindle tiers is therefore the first objective that grades
"closeness to 5-colourability", and it is exact over Q at the run's sizes. The
target invariant is chi_f(R^2) itself: a constructible chi_f > 4 is a
polynomial-checkable LP-dual certificate of chi >= 5, and — since chi_f <= chi
but chi = 5 does not force chi_f > 4 — it is a strictly stronger statement about
the fractional chromatic number of the plane than a bare lower bound on chi;
while a proved sup over the constructible family of <= 4 is a durable bound on
what the LP route can ever buy. Either outcome is a result.

Interplay with the premise flag (chi >= 5 possibly settled in 2018): chi_f > 4
remains open and is NOT implied by a 5-chromatic graph, so the route's value does
not collapse if the flag is confirmed; it reframes the frontier as chi_f(R^2) and
the size/economy of a lower-bound certificate.
