# Kane 2007 — Improved bounds on representing t as a binomial coefficient

Source: D. M. Kane, Integers 7 (2007) #A53, full text read from
http://cseweb.ucsd.edu/~dakane/combinations2.pdf [[kane-combinations2]]

## Result

`N(t) = O((log t)(log₃t)/(log₂t)³)` — the current **unconditional record** for the
total number of solutions to `C(n,m)=t`. (Improved Kane 2004's
`O((log t)(log₃t)/(log₂t)²)` by a factor `log₂t`.)

## Method (Section 2)

Restrict to `n>2m` (mirror symmetry; at most one solution with `n=2m`). Define `f`
implicitly by `C(f(m),m)=t`, extended smoothly via the Γ-function (`f(z)` is analytic).
Then bound the number of integer lattice points `(m,f(m))` on the graph. Kane needs
derivatives of `f` that are **small but nonzero** (eq (4)):
`0 < |f^{(k)}(x)/k!| < 2x^{α−k} e^{2α}(log x)^k`, and the Rolle/interpolation Lemma 1:
if `f−g` (g the interpolating polynomial) has `k+1` integer points then
`|f^{(k)}(y)/k!| = |A/B(m₁,…,m_{k+1})|` for integer `A` and `B` the LCM of the
interpolation denominators.

**The new ingredient (Prop 2)**: `log B(m₁,…,m_k) = O(S·max(1, log(k² log S/S)))`
when the `m_i` span an interval of length `S`. Proved by counting primes dividing
`(m_i−m_j)`, splitting at `S/k` and `S²/k²log S`, using the PNT (Chebyshev `ψ`).

## Section 8 — the dead end (IMPORTANT for this run)

Kane states his technique **cannot be improved much further**:

- Randomized construction of `m_i` gives `log B = Ω(k²(1+log(S/k²)))` for `S>k²`,
  else `Ω(S)`.
- Therefore the inverse density of solutions is at best `O(log₂t)`; and since there
  are `Θ((log t)/(log₂t)²)` values of `m` in the relevant range, **this method alone
  cannot exclude as many as `O((log t)/(log₂t)³)` solutions** — exactly the size of
  the bound it proves.

So Kane's bound is not just unoptimized; the approach is **structurally incapable**
of reaching a uniform / `O(1)` constant. This is a stronger, citable statement of why
the log-ratio methods in the record are not the path to Singmaster.

## Bearing

Confirms the record and, more valuably, documents a proven ceiling on the
Archimedean/convexity method. Any attempt to "sharpen Kane" to a constant is refuted
by Section 8's own lower bound on `log B`. Combined with MRSTT's non-Archimedean
method and its own exp(log^{3/2−ε}P) barrier, this frames the boundary-region gap as
the place a different idea is needed.

```claim
id: kane-method-ceiling
statement: Kane 2007 (Integers 7 #A53 §8) proves his own lattice-point method cannot
  give better than inverse density O(log_2 t): a randomized construction gives
  log B = Ω(k^2(1+log(S/k^2))) (S>k^2) or Ω(S), so one cannot exclude as many as
  O((log t)/(log_2 t)^3) solutions by this technique. The record
  N(t)=O((log t)(log_3 t)/(log_2 t)^3) is thus not just unoptimized but structurally
  limited.
hypotheses: none beyond the setup (n>2m; f analytic extension; k,S as in the proof).
holds-here: yes — bounds the whole Archimedean/convexity approach, this run's record.
status: asserted (author's own analysis of his method's limits)
bearing: shuts the door on 'sharpen Kane to a constant'; names why uniform needs a
  different method.
anchor: research/summaries/kane-combinations2.md
```
