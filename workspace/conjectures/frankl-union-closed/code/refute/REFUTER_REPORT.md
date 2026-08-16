# Refuter report — which statement I attacked and what came back

## Statement attacked

`G-coupling-half`, the single open gap of the `uc-via-entropy-coupling`
skeleton (`research/backward/uc-via-entropy-coupling.md`). I attacked its
**equivalence clause**:

> "Equivalently: the finite-dimensional C-coupling optimization of Yu
> arXiv:2212.00658 has optimal constant exactly 1/2."

I picked this over `R-uc-with-three-set` because: (a) the three-set rung is
genuinely open UC, already exhaustively verified by the run's canonical oracle
for n≤4 and by the literature for n≤11 — a small model search cannot break it,
and the run's own prior TPTP "refutation" of it was already rejected as a
slot-collapse encoding bug; (b) the finite-D "constant exactly 1/2" clause is a
concrete, checkable claim that contradicts in-library published numbers.

## Answer: refuted (exact algebra), for the clause — and only the clause

In Yu's framework the certificate for "an element has density ≥ t" is
`Γ̂(t) > 1` (Corollary 1), so the constant is `t̂_max = sup{t∈(0,1/2): Γ̂(t)>1}`.
"Optimal constant exactly 1/2" requires `Γ̂(1/2) > 1`.

Exact value at the collapsed α=0 extremal (t=1/2, a=(3−√5)/2, β=a):

```
P_pq = (1−β)Q_{a,a} + β Q_{a,1}
w₁ = 1−β/2 (p=a),  w₂ = β/2 (p=1, h=0)
E h(p) = w₁ h(a)
E_indep = w₁² h(2a−a²) = w₁² h(1−a) = w₁² h(a)     [2a−a²=1−a]
Γ̂(1/2) = w₁²h(a)/(w₁h(a)) = w₁ = 1−a/2 = (1+√5)/4 = φ/2 ≈ 0.809017 < 1
```

`Γ̂(1/2) = φ/2 < 1`, so the finite-D relaxation certifies nothing at density
1/2. Its certified constant is `t̂_max ≈ 0.38234` (Yu/Cambie, in-library),
matching the run's own 60-digit exact captures (`commands.log` line 2376:
`0.500000 0.80901699 alpha*=0.0000`; `yugamma_highprec.py` diff=0.0). Since
`Γ̂` is non-increasing in t (proved by set-inclusion), the whole finite-D class
is capped strictly below 1. **The clause "optimal constant exactly 1/2" is
false.**

## What this does NOT refute (important, else the run misreads it)

The **primary coupling inequality** of `G-coupling-half` — that some coupling
in the *full* conditionally-iid class reaches `H(A∨B) > H(A)` at density 1/2 —
remains **open**. Yu's finite-D relaxation is a *strict lower bound* on the
full class (a restricted two-atom family), so a finite-D optimum of 0.38234
does not rule out a full-class coupling reaching 1/2. In their own records,
Liu's conditionally-iid class already beats Yu's 0.38234 up to ≈0.38271.

Consequence for the run: the gap's proposed `next` step — "implement Yu's
finite-D optimization and push the constant toward c = 1/2" — is a **known dead
end** (proved capped at φ/2 < 1 at t=1/2). But the skeleton is NOT thereby
killed: the open question remains in the larger coupling class, which this
refutation does not touch.

## Why I did not use find_counterexample here

The attacked claim is a real-parameter optimization over entropy (transcendental
`sup`/`inf` over a continuum of couplings). It cannot be faithfully stated as a
finite first-order structure whose negation a model finder could witness.
`find_counterexample` is not applicable; the refutation is by exact algebra,
sourced to in-library primary texts (Yu arXiv:2212.00658, Cor 1 / Theorem 1,
and the run's own exact captures).

## For R-uc-with-three-set (the other candidate, not attacked)

The run already closed this path correctly: the TPTP `finding=refuted` on
`uc_with_three_set.p` was an encoding artifact (slots collapsed; genuine |F|=3
not 6), and the decoded family is union-closed with an abundant element. The
canonical oracle exhaustively verified n≤4 (all families with a 3-set have an
abundant element), consistent with the literature's n≤11. No small counterexample
exists; the rung stays open as genuine UC. I did not re-encode it because the
run has already established, with the exact oracle, that no counterexample is
reachable at the sizes this tool can search.

## Evidence class

- **Proved (exact algebra):** Γ̂(1/2) = φ/2 = (1+√5)/4 ≈ 0.809017 < 1.
- **Sourced:** t̂_max ≈ 0.38234 (Yu/Cambie; in-library records).
- **Corroborated:** run's 60-digit exact captures; Γ̂ non-increasing in t.
