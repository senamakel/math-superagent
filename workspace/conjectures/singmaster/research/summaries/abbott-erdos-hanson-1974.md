# Abbott–Erdős–Hanson 1974 — On the number of times an integer occurs as a binomial coefficient

Source: H. L. Abbott, P. Erdős, D. Hanson, Amer. Math. Monthly 81 (1974) 256–261,
primary PDF (renyi.hu) read. [[abbott-erdos-hanson-1974]]

## Theorems (primary-source statements)

- **Theorem 1**: the **average and normal order of N(t) is 2**; more precisely the
  number of `t ≤ x` with `N(t) > 2` is `O(√x)`. (Proof: count pairs, get
  `Σ_{t≤x} N(t) = 2x + 2·2^{1/2}√x + O(x^{1/3}log x)`.)
- **Theorem 2**: for `w(t) < log t/log log t` (w = #distinct prime factors),
  `N(t) < 2 w(t) log t / (log t − w(t) log log t)`.
- **Theorem 3**: `N(t) = O(log t / log log t)` — the first improvement over
  Singmaster. Proof uses **Ingham's theorem** (prime between `x` and `x+x^{5/8}`):
  split the solution set `S={n : C(n,k)=t}` into `n > (log t)^{6/5}` (hence
  `k < log t/log log t`) and the rest; for the rest, the largest `P` prime in
  `(N−K, N]` divides `t` and all `n ≥ P`, so `|S₂| ≤ N−P ≤ P^{5/8} = O((log t)^{3/4})`.
- **Theorem 4**: `G(t) = O(√(log t))` for `t = (n+1)(n+2)…(n+l)` (products of
  consecutive integers), with explicit constant `(2+δ)√(log t/log 2)`.

**Cramér-conditional**: assuming a prime between `x` and `x+(log x)^2`,
`N(t) = O_ε((log t)^{2/3+ε})`.

## Witness data recorded in the paper

- `N(t)=6` for the six `t ≤ 2^48`: 120, 210, 1540, 7140, 11628, 24310.
- The **only** `t ≤ 2^48` with `N(t) ≥ 8` is `t = 3003`, `N(3003)=8`
  (attributed to Singmaster's verification).
- `N(t) ≥ 6` **infinitely often** (Singmaster/Lind).

## Bearing for this run

Primary source for the `O(log t/log log t)` historical step and for the
average/normal-order-2 fact (which books show that "almost all a occur as themselves
+ one mirror"). The `O(√x)` bound on `N(t)>2` counts the size of the set of numbers
with *any* nontrivial repeat, which is the relevant empirical picture: repeats are
rare and bounded in number, matching `B=8`-style thinking — but this is about the
set of t, not the multiplicity of one t, so it does not itself bound N(a) < 8.

```claim
id: aeh-average-normal-order-2
statement: Abbott-Erdos-Hanson 1974 (Thm 1): the average and normal order of N(t) is
  2; explicitly #{t<=x : N(t)>2} = O(sqrt(x)).
hypotheses: none.
holds-here: yes.
status: sourced (primary PDF read; proof reproduced in note)
bearing: numbers with any nontrivial repeat are O(sqrt(x)) of [1,x]; does NOT by
  itself bound the multiplicity of a single value, but frames the empirical picture.
anchor: research/summaries/abbott-erdos-hanson-1974.md
```
