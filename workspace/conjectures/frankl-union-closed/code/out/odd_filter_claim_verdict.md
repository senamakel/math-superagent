# Finding — min max-density over non-Boolean union-closed families

Extremal-counting claim tested by exact algebra + oracle enumeration:

> Among **non-Boolean** union-closed families F ⊆ 2^[n], the minimum of
> `max_x density_x` is `2^{n-1}/(2^n-1)`, and is attained **uniquely** by the
> odd filter `F = 2^[n] \ {∅}`.

**Verdict: the VALUE is correct; the UNIQUENESS is FALSE.**

The minimizers are **n+1** distinct non-Boolean union-closed families, not one:

1. the **odd filter** `2^[n] \ {∅}`, and
2. for each `x ∈ [n]`, the family **`2^[n] \ {{x}}`** — the power set minus the
   singleton `{x}`.

Every one has `m = 2^n - 1` and max density `2^{n-1}/(2^n-1)`.

## Step-by-step verdict

| Step | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | max ≥ 1/2 (Frankl); non-Boolean ⟹ strict > 1/2 | **PASS** | rests on the separately-verified half-density lemma: max density exactly 1/2 ⟹ Boolean subalgebra (max=half forces Boolean). So non-Boolean ⟹ max strictly > 1/2. |
| 2 | for |F|=m, max c_x ≥ ceil(m/2) | **PASS** | integer counts; most-frequent element is in ≥ m/2 sets; odd m=2q+1 can't have c=q+0.5 ⟹ c≥q+1. |
| 3 | odd m: density ≥ (q+1)/(2q+1)=(m+1)/(2m), decreasing in m; largest odd m=2^n−1 | **PASS** | sympy: d/dm[(m+1)/(2m)] = −1/(2m²)<0; and (m+1)/(2m) at m=2^n−1 equals 2^{n-1}/(2^n−1) (difference = 0). |
| 4 | uniqueness of odd filter as the size-2^n−1 UC family | **FAIL** | power-set-minus-singleton families are also UC and attain the same bound. Oracle n=2,3,4: minimizer count 3,4,5 = n+1. |
| 5 | even m non-Boolean: max ≥ m/2+1, density ≥ 1/2+1/m, never beats odd value | **PASS** | sympy: (1/2+1/m) − (1/2 + 1/(2(2^n−1))) ≥ 0 for even m ≤ 2^n; gap positive. So even families never beat the odd-filter value. |

## Exact structural facts (general n)

For `F_x = 2^[n] \ {{x}}`:

- `c_x = 2^{n-1} − 1` (the removed singleton's element), every other `c_y = 2^{n-1}`
- `max density = 2^{n-1}/(2^n−1)`, identical to the odd filter's value.
- It is union-closed: the only set that would force a union to be `{x}` is
  `{x}` itself, which is absent; any union of two proper subsets can't equal the
  singleton `{x}`.
- It is non-Boolean: it is not closed under symmetric difference (it lacks the
  singleton `{x}`).

The general characterisation of union-closed families of size `2^n−1` (oracle,
n=2..8): exactly remove `∅` or a singleton. Removing any non-singleton,
non-empty T breaks closure (two proper subsets can union to T).

## Assumptions & ceiling

- Oracle enumeration of all union-closed families is exhaustive only for
  n ≤ 4 (2^(2^n) subfamilies; 65536 at n=4). At those n the minimizer count
  is exactly n+1.
- The closed-form structural facts (union-closure, density of the
  singleton-removal families) are proved for general n by exact arithmetic and
  verified by direct oracle for n = 2..8.
- The value `2^{n-1}/(2^n−1)` being the *minimum* over ALL non-Boolean UC
  families for general n depends on step 1's Frankl bound holding at that n.
  For n ≤ 11 that's fine (UC verified); for larger n the *value* claim needs
  the Frankl bound, but the *counterexample to uniqueness* (n+1 minimizers) is
  unconditional for every n ≥ 2.

## Files
- `code/out/odd_filter_min_maxdensity_verify.py` — symbolic step checks + oracle minimizer enumeration.
- `code/out/odd_filter_minimizers_char.py` — labels the actual minimizers (odd filter + the n singleton removals).
- `code/out/odd_filter_minimizers_general.py` — closed-form structural proof for general n, verified n=2..8.
