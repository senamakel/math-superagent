# Sums of products of binomial coefficients mod 2 — Wu (INTEGERS 22, 2022)

Source: https://math.colgate.edu/~integers/w81/w81.pdf
Full text: [[run-length-transform-binomial-mod2-integers.full]]

## What it establishes

- **Theorem 1 (the submask criterion).** `C(n,k) ≡ 0 (mod 2)` iff `k ∧ (¬n) ≠ 0`;
  equivalently `C(n,k) ≡ 1 (mod 2)` iff `k` is a binary submask of `n`
  (`k ∧ n = k`). This is *the* definitional basis of this problem's fold rows:
  row `d` of `Φ_n` is 1 exactly at positions `n−1−d+o` for `o ⊆ d`, by Lucas.
- **Theorem 2.** `C(n,k)C(m,r) ≡ 0 (mod 2)` iff `(k∧¬n) ∨ (r∧¬m) ≠ 0`.
- **Run length transform (Definition 1).** For a bit sequence, the 1-runs `R`
  are the lengths of maximal runs of consecutive 1s in the **binary expansion**
  of `n`; the run length transform of `{S_n}` is `T_0 = S_0`, and for `n > 0`,
  `T_n = ∏_{i ∈ R} S_i`. (This is a construction on the *binary digits of n*,
  **not** the maximal-consecutive-integer runs inside `M_d` of this problem.)
- **Theorem 4 / Theorem 12.** Recurrences for run length transforms of linear
  recurrence sequences: if `S_{n+1} = d0·S_n + d1·S_{n-1}`, `S_0=1, S_1=c1`, then
  `T_0=1`, `T_{2n}=T_n`, `T_{4n+1}=c1·T_n`, `T_{4n+3}=d0·T_{2n+1}+d1·T_n`.
  The order-(k+1) analogue is Theorem 12. All such transforms are **2-regular**.
- **Theorem 10 (OEIS A106737).** `a(0)=1, a(2n)=a(n), a(4n+1)=2a(n),
  a(4n+3)=2a(2n+1)−a(n)`; the run length transform of the positive integers.

```claim
id: wu-submask-criterion
statement: C(n,k) is odd iff k is a binary submask of n (k & n == k); C(n,k) is even
  iff k & ~n != 0.
hypotheses: n, k nonnegative integers, k <= n; modulus 2
holds-here: yes -- this is exactly the Lucas criterion defining the fold rows M_d
status: proved (Lucas/Wu Thm 1)
bearing: definitional basis of Phi_n; row d is the indicator of {o : o subset d}
anchor: research/sources/run-length-transform-binomial-mod2-integers.full.md
```

## Bearing / what it does NOT settle

Confirms the submask criterion (already imported as the definition of `M_d`) and
provides the 2-regular / run-length-transform vocabulary. **The paper's "run length
transform" is on the binary expansion of an index and is a different object from this
problem's maximal-consecutive-integer runs inside `M_d`** (problem item 5). It does not
describe which symmetric-difference sets `M_d △ M_{d'}` occur — the crux (priority 1)
remains open and unaddressed by this source.
