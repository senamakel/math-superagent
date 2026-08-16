# PROBLEM — scored search over the union-closed coupling constant

Transcription of the mathematical object is in
`research/notes/yu-optimization-verbatim.md` (Yu, *Dimension-Free Bounds for the
Union-Closed Sets Conjecture*, Entropy 2023). Encoding here matches that source.

## The object

Binary entropy, binary log:

    h(x) = −x·log₂x − (1−x)·log₂(1−x),   h(0) = h(1) = 0.

The **ρ = 1** coupling potential:

    φ(1,p,q) = median{ max{p,q}, 1/2, p+q }        (multiset median)

The **two-atom symmetric coupling** P_pq over (p,q) ∈ [0,1]²:

    P_pq = (1−β)·Q_{a1,a2} + β·Q_{b1,b2},
    Q_{x,y} = (1/2)·δ_{(x,y)} + (1/2)·δ_{(y,x)},
    a = (a1+a2)/2,  b = (b1+b2)/2,
    β = (t−a)/(b−a),   constraint set  0 ≤ a ≤ t < b ≤ 1,  β ∈ (0,1],  E h(p) > 0.

The objective (eq. after (4)):

    g(P_pq, α) = (1−α)·E_{(p,q)∼P_p^{⊗2}} h(p+q−pq)
               + α ·E_{(p,q)∼P_pq} h(φ(1,p,q))

where P_p is the marginal of P_pq and P_p^{⊗2} is the independent product
coupling of two copies of that marginal.

The dimension-free lower bound (Prop 1, eq (5)):

    Γ̂(t) = sup_{α∈[0,1]}  inf_{symmetric P_pq : E h(p) > 0}  g(P_pq, α) / E h(p).

## The theorem we are scoring

**Corollary 1:** if Γ̂(t) > 1 for some t ∈ (0, 1/2), then every (finite,
nonempty, OR-closed) union-closed family has some element present in **≥ t·|F|**
sets. So a *certified density* is a t with Γ̂(t) ≥ 1, and the search's job is to
push t as high as possible.

## The search problem

The candidate proposes **α** (plus hyperparameters for the inner minimisation,
e.g. the two-atom grid resolution or tolerance); the scorer then **minimises
`g(P_pq,α)/E h(p)` over the two-atom P class internally** at each t. The
certified density is

    score = max{  t ∈ (a, min(b, 1/2)]  :  inf_{P_pq} g(P_pq,α)/E h(p) ≥ 1  }      (or 0 if none).

The searcher proposes candidates; **the scorer (`score.py`) independently
performs the inner inf and verifies every constraint** and returns the
certified density with its rigorous Gammâ interval. The searcher must NOT write
or modify the scorer.

## One-α caveat (read before searching)

Within the scorer, **α is fixed by the candidate, but P is not**: the scorer
must take the infimum over the two-atom P class itself. For a single candidate
coupling P, the ratio `g(P_pq,α)/E h(p)` is an **upper bound** on the true
infimum `inf_P g(P_pq,α)/E h(p)`, never a lower bound — a single point can only
overestimate a minimum. So a candidate that supplies a non-minimising P reports
an inflated ratio, and its SCORE **certifies nothing**. A genuine certified
density for α requires `inf_P g(P,α)/Eh ≥ 1`: the scorer must minimise `g/Eh`
over P internally, the candidate proposes only α (plus inner-search
hyperparameters), and maximising over candidates is then the sup over α.

## Known ceiling (recorded from the run)

- **Γ̂(t) is non-increasing in t** (proved). So the plateau is reached at the
  largest t satisfying Γ̂(t) ≥ 1, and larger t certifies nothing extra.
- **t̂_max := sup{ t ∈ (0,1/2) : Γ̂(t) > 1 } ≈ 0.382345533366702** (Cambie 2022,
  computed to 0.382345533366702 ≤ t̂_max ≤ 0.382345533366703, attained at
  α ≈ 0.03560698136437784).
- Yu's published certified witness is t = 0.38234 with Γ̂(t) ≥ 1.00000889 at
  α = 0.035, a1 = a2 = 0.3300622, b1 = a, b2 = 1 (β = 0.1560676).
- **Do not trust a candidate scoring above ≈0.3823455 inside this two-atom
  class** — it would falsify the proved monotonicity and must be re-checked
  before it is believed. An honest score above the ceiling requires a richer
  coupling class than the two-atom one this scorer encodes; that is a different,
  still-open question, not what this scorer measures.

## Scorer contract (`score.py`)

Run: `python score.py <candidate_module.py> [N] [REF_T]`

- **Module-path contract**: the candidate is a python module (the harness
  invokes exactly `python3 score.py candidates/<id>.py` — ONE argument, the
  candidate path). The candidate proposes **α only, plus inner-search
  hyperparameters** (e.g. grid resolution, tolerance) — it must NOT supply the
  coupling atoms (a1,a2,b1,b2), because those are the inf variable the scorer
  minimises over internally. The scorer imports the module and reads α (and any
  hyperparameters) from module-level scalars or a `params()`/`make()`/
  `candidate()`/`get_params()`/`solve()` callable. Trailing `[N] [REF_T]` are
  optional with the same defaults. **A candidate that fixes the coupling atoms
  supplies the inf variable and certifies nothing — the scorer must reject it.**
  The old five-positional-float form is not what the harness calls and was the
  reason every early candidate was discarded.
- Verifies every constraint with **rigorous interval arithmetic** (mpmath.iv,
  directed rounding), never floats-to-conclusions.
- Prints `SCORE: c` (the largest certified t) followed by the certified Gammâ
  interval, the certified lower endpoint of Γ̂, and the binding constraint.
- Prints `INVALID: <constraint, violating value>` if a constraint fails.
- Grid scan: 20000 (configurable) t-points in `(a, min(b,1/2)]`, β = (t−a)/(b−a).
- A candidate's certified density is reported via the **lower endpoint** of the
  Γ̂ interval (lo ≥ 1 required), never a midpoint.
- Runtime < 10 s per candidate; memory bounded well under 8 GiB.
- The **verified frontier** is the known ceiling 0.3823455; the scoring map tells
  the search where candidates plateau and which constraint binds.
