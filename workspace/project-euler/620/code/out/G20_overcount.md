# The winning model reproduces G(16) but overcounts G(20) by 8

Computed by the operator from this workspace's own model, re-implemented in
plain Python from the docstring of `code/pattern/fast_g.py` — the monotone
crossing form, no mpmath, no grid:

```
f(d) = Q_p(d) - Q_q(d),  monotone on (DL, DU)
g    = #{ m in Z : f(DL) < m < f(DU) }
Q_t(d) = (c-t)*B_t + (s+t)*G_t,  B_t = atan2(y,x)/2pi,  G_t = atan2(y,x-d)/2pi
|OP| = R - rho_t,  |SP| = r + rho_t
DL = max_t |a_t - b_t|,  DU = min(min_t (a_t + b_t), R - r - 1)
```

## Result

```
g(16,5,5,6) =   9    oracle   9   AGREE
G(16)       =   9    oracle   9   AGREE
G(20)       = 213    oracle 205   DISAGREE  (+8)
```

## Why this matters more than the two agreements

`g(16,5,5,6)` and `G(16)` are **the same single tuple** — G(16) has exactly one
term. Matching both was one data point, not two. G(20) sums 22 tuples and is the
first real test of the counting rule, and the model fails it.

The sign convention established in `tangency_enum_claim.md` is *not* what is
wrong: it is what makes the one tuple come out right, and the other seven sign
variants give 6, 7 or 10. What is wrong is the **counting rule** — which `d` in
the valid interval correspond to physically distinct, admissible arrangements.
Overcounting by 8 across 22 tuples means roughly one spurious arrangement every
three tuples.

## Where the 8 are likely to be

Candidates, in the order worth testing:

1. **The degenerate endpoint.** `d = d_min = 1/(2pi)` is where the two p-planets
   coincide; the run identified and excluded it in its first model
   (`oracle-model-broken.md`) and the crossing count may be re-admitting it via
   an endpoint `m` at `f(DL)`.
2. **Planet overlap that is not the stated overlap.** The statement permits
   planets to overlap one another, but `S` and `C` must stay at least 1cm apart
   at their closest point — `DU = R - r - 1` encodes that. It does not encode a
   planet leaving the annulus or two same-size planets landing on top of each
   other, which are different degeneracies.
3. **p = q collisions.** The sum requires `p < q`, but within a tuple the two
   `p`-planets and two `q`-planets can coincide pairwise at particular `d`.
4. **Endpoint strictness.** `#{m : f(DL) < m < f(DU)}` is strict at both ends;
   whether a crossing exactly at an endpoint is admissible is a modelling choice
   the oracle can settle.

## The check to run

Do not re-derive the sign convention — it is settled. Instead, for the tuples
where the model is wrong, print the offending `d` values and look at the
geometry: which arrangement is being counted that should not be. Then fix the
admissibility test, not the residue.

```claim
id: g20_overcount_by_eight
statement: The monotone-crossing counting rule of code/pattern/fast_g.py with
  sign variant (sigma=-1, eta=-1, theta=-1) gives G(16)=9 (correct) and
  G(20)=213 against the stated 205, an overcount of 8 across the 22 tuples of
  G(20). g(16,5,5,6)=9 is reproduced. The sign convention is therefore correct
  and the admissibility rule for which crossings are physical is not.
hypotheses: f(d)=Q_p-Q_q monotone on (DL,DU); g counts integers strictly
  between f(DL) and f(DU); DL, DU and Q_t as in fast_g.py.
holds-here: yes — computed from this workspace's own model against both stated
  check values
status: checked
bearing: kills any G(500) computed from the present counting rule; the next
  step is to find which crossings are spurious, not to re-derive the residue
anchor: code/out/G20_overcount.md; code/pattern/fast_g.py
source: operator-computation
```
