# Ruin-theory / Foster–Lyapunov certificate for the surplus process

```approach
idea: Treat the recharge identity's surplus S_k = Σ_{i<k}(j_i+1) − (k−1) as a Cramér–Lundberg insurance surplus process (unit premium, claims j_i+1), and prove the ruin set {b_k = 0} is transient by constructing a stochastic Lyapunov function / exponential supermartingale whose drift condition is exactly the regeneration net-profit condition.
mechanism: The recharge identity b_k = b_1 + S_k (proved, this run) is verbatim the structure of the classical risk model: between regeneration events the surplus decreases by exactly 1 per row (premium outflow), and at event i it jumps up by j_i+1 ≥ 1 (claim). Ruin is b_k ≤ 0, i.e. S_k ≤ −b_1. This is a skip-free upward-jump surplus process. The target is NOT the mean event rate (the record already shows the mean is the wrong target because the jump distribution is heavy-tailed): it is a per-event drift/domination bound, which is precisely what Lundberg's adjustment-coefficient and Foster–Lyapunov criteria are built to do. Concretely, define γ* = sup{ γ : E[e^{γ((j_i+1)−T_i)} | state] ≤ 1 } where T_i is the inter-event time; γ* > 0 (a strict net-profit condition) gives an exponential bound on P(ruin by row n), and a Foster–Lyapunov test function V(state) with V non-increasing in mean except on a finite set, and V = +∞ on the ruin set, certifies transience of {b=0}. The state is the LOCAL pair (edge x, intruder y) plus the surplus — the same (b, x, y) boundary state the step/drain laws already make exact — so the drift can be checked pointwise along the actual deterministic prime sequence, no stationarity or ergodicity needed (which is what killed the subadditive/Kingman route: primes are not stationary). The hypothesis it reduces GC to is: the drift condition γ* > 0 holds for the prime gap source, equivalently Σ(j_i+1) outpaces the inter-event times with a margin that survives the heavy tail.
status: refuted
disposition: (b) parked — refuted, not a route to G-supply; probabilistic-ruin machinery needs a measure the deterministic primes lack, and the drift condition restates the conjecture (Directive 44 item 2).
precedent: >
  The named mathematics is real and standard, but it is a statement about
  PROBABILISTIC ruin, which this problem's object is not.
  - https://onlinelibrary.wiley.com/doi/10.1002/9781118445112.stat04324
    (Lundberg inequality survey: the adjustment coefficient / Cramér–Lundberg
    approximation applies to a risk process with Poisson claims and i.i.d.
    net-profits per period; the exponential bound psi(u) ~ e^{-R·u} requires an
    exponential moment of the claim.)
  - https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/ruin-probabilities-via-local-adjustment-coefficients/19355DD55274981BE27D3B0C235E7EB0
    (Asmussen, local adjustment coefficient; large-deviation / Lundberg-type
    bounds for reserve-dependent premiums.)
  - https://www.sciencedirect.com/science/article/pii/S0167668712000807
    (second-order heavy-tailed ruin asymptotics — the regime when there is NO
    exponential moment and the adjustment coefficient is degenerate.)
  - claims: step-law-theorem-proved, step-law-and-recharge-identity,
    bigjump-cap-characterization-1000, zero-sum-flow-mincut-restatement-refuted,
    anti-gilbreath-construction
  No source applies risk theory to Gilbreath (none exists in the Gilbreath
  literature); the recharge identity as a "surplus process" is this run's own
  vocabulary (equivalently the STEP-LAW/RECHARGE accounting), not a sourced
  application, and it is already a proved theorem here.
  The general-class hope is killed by Eppstein 2011 (anti-gilbreath-construction):
  a 2-then-odds sequence with gaps ≤ f(n) whose right edge escapes to non-1
  infinitely often IS a surplus path that hits ruin infinitely often; so no
  pointwise per-event drift condition holds for the whole 2-then-odds class.
  The primes can only differ by non-concentration, which no drift theorem in
  risk theory supplies.
killed-by: >
  The drift/supermartingale certificate is (i) a statement about probabilistic
  ruin, which this is not — there is no probability measure, no i.i.d. claim
  law, no Poisson arrival, and the jump sizes/times are deterministic functions
  of the fixed prime sequence; (ii) the required "strictly positive per-event
  net profit γ*>0 everywhere" hypothesis is RESTATED, not reduced — it is
  exactly the unproved regeneration content (the conjecture says the recharge
  surplus never falls k−1 behind), carrying no named theorem that supplies it;
  and (iii) at the level where risk theory is non-vacuous (heavy-tailed claims
  with no exponential moment) the adjustment coefficient degenerates (Lundberg
  exponent = 0, subexponential ruin asymptotics), which is precisely the regime
  the run's own data occupies (heavy-tailed surplus: 12 genuine giant jumps
  carry 86.1% of S_1000), so the exponential Lundberg bound the method is built
  to produce cannot exist. Eppstein kills the class-level claim. The honest
  deliverable survives only as the conditional "IF the per-event net-profit
  drift holds on the prime gap source THEN b_k never hits 0", whose hypothesis
  is the conjecture restated in drift language.
buy: >
  A clean vocabulary: the recharge identity IS a skip-free upward-jump surplus
  process with unit premium per row and claims (j_i+1). This reframes (not
  proves) the open question as "the net-profit drift per (2,4)-event stays
  positive on every finite stretch". The Foster–Lyapunov test-function idea
  (V(x,y,s) = s − ψ(y)) is a useful way to ORGANISE the search for a per-event
  drift certificate, and the run should keep it as a tool, but it provides no
  new theorem: every named theorem in this body is about probabilistic ruin and
  cannot be invoked without inventing a law the primes do not follow.
first-step (superseded): From blocks_depth1000.json estimate the empirical per-event net profit (j_i+1)−T_i and test whether the running surplus is monotone-nonnegative on every finite stretch — this is already the recharge identity's S_k ≥ k−2, i.e. the conjecture itself. The drift condition can be tested, but a negative test on any row refutes only that candidate certificate, and a positive test on the 60 computed events proves nothing beyond depth 1000.
side: regeneration (bounds the recharge side of the balance; does not re-derive erosion, which is settled)
named-mathematics: Cramér–Lundberg risk model, Lundberg exponent / adjustment coefficient, Foster–Lyapunov / drift criteria for Markov chains, stochastic domination by a heavy-tailed claim process, reflected random walk.
speculative: The jump times/sizes are driven by the deterministic prime gaps, not i.i.d.; the supermartingale must therefore be verified against the actual sequence rather than a stationary law. The honest deliverable is a conditional reduction — "if the net-profit drift condition holds (stated hypothesis on prime-gap statistics), then b_k never hits 0" — which is exactly the shape of partial result GOAL.md asks for.
falsifier: Eppstein's anti-Gilbreath construction (gaps ≤ f(n) whose right edge escapes infinitely often) is the standing witness that the drift condition FAILS in the general 2-then-odds class; the approach must state precisely what property of the prime gaps (non-concentration / correlation structure) restores γ* > 0, or it is just a restatement.
