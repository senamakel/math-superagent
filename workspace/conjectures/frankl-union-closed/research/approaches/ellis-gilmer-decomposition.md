# Decomposition of node `ellis-gilmer-conjecture-refuted`

**File:** `code/lean/ellis_gilmer_conjecture_refuted.lean` — compiles, 4 `sorry`s,
all non-gap theorems kernel-clean (only `propext`/`Classical.choice`/`Quot.sound`).

**Node statement:** Gilmer's Conjecture 1 is false. i.i.d. A,B over subsets of
[n], all marginals < 1/2, H(A)>0, would give H(A∪B)+D(A∪B||A) > H(A). Ellis
(arXiv:2211.12401) gives an n=2 counterexample: p(∅)=p({1,2})=x, p({1})=p({2})=1/2−x,
x=0.3, marginal exactly 1/2, Ellis-rewrite quantity ≈ −0.0468; an ε-perturbation
p'({1,2})=x−2ε, p'({1})=p'({2})=1/2+ε−x gives marginals < 1/2, quantity still < 0.

## Proven (kernel-checked, no sorry)

- `mass_1_half`, `mass_2_half`, `boundary_distribution`: both elements have
  marginal exactly 1/2; the distribution at x=3/10 has positive mass, total
  mass 1.
- `ellis_lhs_negative`: the Ellis-rewrite quantity at x=3/10 equals
  `(2/25)·ln(2/3) < 0` (via `lhs_eq_closed`, `log_10_3_sub_log_5`,
  `closed_at_3_10`, `closed_neg`). Independent numeric check: LHS = −0.046797…,
  marginals = 1/2, matches the paper and the closed form (natural-log version
  (2/25)ln(2/3)).

## Gaps (each is a fenced `gap` docstring block in the lean file)

> **Directive 21 correction (STATEMENT BUG).** Two of the four sorry-blocked
> goals were FALSE as stated and could never have been discharged, because both
> mistakenly asked for the **entropy of `p`** (a strictly positive quantity on
> the open simplex) to be negative:
> - `gap_perturbed_strict` demanded `0 < hsum f` **and** `(∑ f i·log(1/f i)) < 0`
>   — but `hsum f` is *defined* as exactly that sum, so it asserted `X > 0 ∧ X < 0`
>   for the same `X`. Unsatisfiable.
> - `gilmer_refuted_boundary` demanded `(∑ f i·log(1/f i)) < 0` on a distribution
>   with all `f i > 0`, sum 1 — Shannon entropy in nats, strictly positive.
>   Unsatisfiable.
>
> What is actually negative is quantity (1), the **difference**
> `Σ_s q_s·log(1/p_s) − Σ_s p_s·log(1/p_s)` that `LHS`/`closed` encode — already
> kernel-checked as `(2/25)·ln(2/3) < 0` at `x = 3/10` via `ellis_lhs_negative`.
> Both goals must be restated around that difference, **not** around `hsum`.
> The restatement is task `restate-false-lean-goals-ellis-gilmer`; do not assign
> a prover to them until it is done. The arithmetic core (8 declarations on only
> propext/Classical.choice/Quot.sound) is untouched.

| id | lemma | status | next |
| --- | --- | --- | --- |
| `ellis-gilmer-conjecture-refuted/gap-union-weights` | iid-union weights q over the 16 bitwise-OR pairs equal closed forms q(∅)=x², q({1})=q({2})=1/4−x², q({1,2})=1/2+x² | open — correctly stated | fin_cases over the `or` table, then ring — purely mechanical |
| `ellis-gilmer-conjecture-refuted/gap-entropy-rewrite` | Ellis's rewrite: H(A∪B)+D(A∪B||A) = Σ_s q_s·log(1/p_s) since log(1/q)+log(q/p)=log(1/p) | open — correctly stated | log_mul + log_div to collapse, then ring |
| `ellis-gilmer-conjecture-refuted/gap-perturbed-strict` | strict-hypothesis counterexample: `∃ ε > 0`, a distribution (Ellis's `p'(∅)=x, p'({1,2})=x−2ε, p'({1})=p'({2})=1/2+ε−x`) with every marginal `< 1/2`, `H > 0`, and the **difference (1)** negative — stated with a **perturbed-LHS** function, not with `hsum` on both sides | **RE-STATEMENT REQUIRED** (directive 21) | continuity of (1) in the distribution + ε/δ from strict negativity at ε=0, instantiate rational ε |
| `ellis-gilmer-conjecture-refuted/gilmer-refuted-boundary` | **RE-STATEMENT REQUIRED** (directive 21): assert `∃ x, 0 < x ∧ x < 1/2`, all marginals of `mass x` equal `1/2`, and `LHS x < 0` — `ellis_lhs_negative` + `boundary_distribution` give this at `x = 3/10`, so it becomes provable now rather than a sorry | **RE-STATEMENT REQUIRED** | fit `ellis_lhs_negative` + `boundary_distribution` at `x = 3/10` together |

The combining theorem's shape is kernel-checked (it elaborates); its leaves are
open. The strict `< 1/2` counterexample is the union of `gap_perturbed_strict`
with the boundary refutation.
