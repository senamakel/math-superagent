# R-random-pointwise: the small-n "failure" is real, but the rung is closed

Attacked the committed rung **R-random-pointwise**
(`research/weakened/supply.md`): "For h uniform on the domain of Φ_n,
wt(Φ_n h) ≥ n/4 with probability 1 − exp(−Ω(n))."

## The two facts, and the apparent tension

1. **Small-n counterexample (verified here, n=5).** For h uniform on the
   domain of Φ_5 (d ∈ [2,4]:

       t2 = h2⊕h4,  t3 = h1⊕h2⊕h3⊕h4,  t4 = h0⊕h4,
       wt = t2+t3+t4.

   The model h = all-zeros (engine-confirmed on
   `code/refute/random_pointwise_n5.p`, SZS CounterSatisfiable) gives wt = 0
   < 5/4, and more generally P(wt < n/4) is a *constant* at small n — the run's
   own `research/notes/refute_random_pointwise_small_n.md` records 1/4 at
   n=4, >1/8 at n=5. This confirms the run's documented small-n behaviour is
   real (this exact model is a member of the failing set; its measure 1/2^n
   is allowed by the probabilistic statement).

2. **The proved exact binomial law closes the asymptotic form.** Claim
   `fair-model-exact-binomial` (status: **proved**) says Φ_n is an (n−2)×n
   matrix, rank n−2, surjective onto F₂^{n−2} with every fiber of size 4.
   Hence for uniform h, **Mh is uniform on the full cube F₂^{n−2}** — i.e. its
   n−2 coordinates are iid fair bits — so wt(Φ_n h) ~ Binomial(n−2, 1/2)
   exactly (verified exhaustively n=2..9).

   For X ~ Binomial(n−2, 1/2), the threshold n/4 sits a gap δ = (n−2)/2 − n/4
   = (n−4)/4 = Θ(n) below the mean (n−2)/2. Chernoff gives
   P(wt < n/4) ≤ exp(−Ω(n)). **So the asymptotic form of R-random-pointwise is
   a theorem, obtained from the surjectivity/fiber fact alone.**

## The ladder's caveat is a miscue, not an obstruction

The rung's merge note warns: "concentration does not follow from uniform on a
rank-(n−2) subspace alone — a rank-2 subspace span{e_1,(0,1,…,1)} has E[wt]=n/2
but only half its vectors of weight ≥ n/4 — so the argument must use Φ_n-specific
structure (Lucas), not the bare rank."

That counterexample is a map **F₂² → F₂ⁿ** (a rank-2 *image* subspace, nullity
n−2): its image is a thin 2-dim subspace of the cube, weight not binomial. But
Φ_n is the **opposite** direction: **F₂ⁿ → F₂^{n−2}**, surjective, nullity 2. For
any surjective linear map down to the cube (equal-size fibers), Mh is uniform on
the *whole* cube → coordinates iid → binomial → concentration. The direction of
the map is the whole difference, and Φ_n is on the good side of it. Neither Lucas
nor any additional submask structure is needed; the rank claim is sufficient.

## Verdict

- R-random-pointwise **is closed** by the run's own proved claims
  (`fair-model-exact-binomial` → `uniform-random-h-supply-whp`, which already
  states the Chernoff corollary for every fixed c < 1/2, covering c = 1/4).
  The ladder's "open" marker is stale.
- The small-n constant failure is genuine but irrelevant: it is the boundary
  deviation of a binomial, which decays exponentially, not a disproof.

```claim
id: r-random-pointwise-closed-by-exact-binomial
statement: R-random-pointwise — wt(Phi_n h) >= n/4 with probability 1 -
  exp(-Omega(n)) for h uniform on the domain — is a theorem, from the proved
  exact-binomial law (claim fair-model-exact-binomial, rank Phi_n = n-2,
  surjective onto F2^{n-2}, every fiber size 4): Mh is uniform on the whole
  cube F2^{n-2} so wt ~ Binomial(n-2, 1/2) and Chernoff gives P(wt < n/4) <=
  exp(-Omega(n)) since n/4 is a Theta(n) gap below the mean (n-2)/2. The
  rung's merge-caveat (a rank-2-image subspace has only half its vectors >
  n/4) concerns a map F2^2 -> F2^n, the opposite direction from Phi_n's
  surjective F2^n -> F2^{n-2}, so it does not obstruct this fold. Small-n
  constant failure (P(wt<n/4) ~ 1/4 at n=4, model h=0 wt=0 at n=5, engine-
  confirmed) is the boundary deviation of a binomial and decays, not a
  disproof.
hypotheses: floored convention d in [2,n-1]; rank Phi_n = n-2 (proved claim
  fold-rank-n-minus-2-binomial-proved, n=2..40 + exhaustive n=2..9); h uniform
  on F2^n; standard Chernoff.
holds-here: yes — the exact binomial is established for the actual fold.
status: proved (Chernoff on the proved exact binomial; small-n model is a
  confirming check that the run's caveat is harmless)
bearing: closes the open rung R-random-pointwise without new work; the ladder
  should merge it. The fetch of a fresh concentration argument "must use
  Lucas, not bare rank" is unnecessary: surjectivity in the (n-2)-image
  direction is already enough.
anchor: code/refute/random_pointwise_n5.p (engine model h=0, wt=0);
  claim fair-model-exact-binomial; research/notes/fold_rank_and_binomial_proved.md
```

## Engine-confirmed small-n models (both checked against the statement)

- **n=4** (`code/refute/random_pointwise_n4.p`, SZS CounterSatisfiable): the
  model h = (0,0,0,0) has t2 = h1⊕h3 = 0, t3 = h0⊕h1⊕h2⊕h3 = 0, wt = 0 < 1 =
  n/4. So P(wt < n/4) at n=4 is at least 1/16 > 0; the run's note says the
  exact value is 1/4 (P(h1=h3 and h0=h2) = 4/16). Consistent.
- **n=5** (`code/refute/random_pointwise_n5.p`, SZS CounterSatisfiable): the
  model h = (0,0,0,0,0) has t2=0,t3=0,t4=0, wt = 0 < 5/4 = 1.25. The run's
  note says P(wt=0) = 4/32 = 1/8 and P(wt≤1) is a constant > 0. Consistent.

Both models merely exhibit the binomial's lower tail at tiny n; neither
falsifies the asymptotic statement (which is a theorem, per above).

## Negative control included (rule: a capture must not read as a pass)

The small-n model is not vacuous: it *does* falsify the absolute statement
"every h has wt(Φ_n h) ≥ n/4" (the engine returned CounterSatisfiable on the
forced-witness encoding), exactly as the run's own note predicts. That is the
control that confirms the concentration statement is the honest asymptotic one
and that the probabilistic form — not the all-h form — is what the exact
binomial proves. The two together (model found + binomial law) mean: the rung's
only content is the asymptotic form, and that form is already proved.
