# Kane 2004 — "New Bounds on the Number of Representations of t as a Binomial Coefficient" (PRIMARY)

Source: D. Kane, *Integers* 4 (2004), #A07, pp. 1–10, electronic.
PDF fetched from the author's page http://cseweb.ucsd.edu/~dakane/combinations.pdf.
Full text: `research/sources/kane-2004-new-bounds.full.md`. (The 2007
*Integers* 7 #A53 companion is also held: `kane-combinations2.full.md`.)

## What it proves

**Theorem 1.** For t > 1, with N(t) = #{(n,m) : C(n,m) = t},

```
N(t) = O( log t · log log log t / (log log t)^2 ).
```

This improves Abbott–Erdős–Hanson 1974's `O(log t / log log t)` (and their
conditional-on-Cramér `O((log t)^{2/3+eps})`). It is the **first** of Kane's two
improvements; the 2007 paper tightens the denominator to `(log log t)^3`.

## Method — the A/B/C decomposition (origin of the framework MRSTT and Kane 2007 build on)

N(t) = 2A(t) + 2B(t) + 2C(t) + O(1) where, writing solutions as (n,m) with 2m <= n:

- A(t): 2m < n < m^{6/5}  (near-boundary small slopes) — bounded via AEH's
  Theorem 3: A(t) <= (log t)^{3/4}.
- B(t): m^{6/5} < n < m^{log log t / 24 log log log t} (the intermediate region)
  — bounded by a Rolle/interpolation argument: f(z) := the analytic function
  with C(f(z), z) = t satisfies C(n,m)=t iff n is near
  exp((log t + log m!)/m) + (m-1)/2; if k+1 many m_i have integer f(m_i), the
  degree-k interpolating polynomial's k-th divided difference is a nonzero
  integer multiple of M^{-1}, forcing it >= (m_{k+1}-m_1)^{-k(k+1)/2}, while
  analytic estimates give the k-th derivative of f is tiny; hence
  m_{k+1} - m_1 > (log log t)^4, so B(t) <= log t/(log log t)^3.
- C(t): n > m log log t / 24 log log log t (n nearly fixed by m) — bounded
  crudely: the largest m in this range is O(log t · log log log t / (log log t)^2).

Key lemma: Rolle's theorem iteration (Lemma 2.1) + its corollary applied to
f(x) - p(x); Stirling expansion (2.1) for log Γ; derivative bounds of
exp((log t + log Γ(x+1))/x) via Cauchy integral formula.

## Bearing for this run

- Completes the bound-history chain at primary level: Singmaster 1971
  O(log a) (not held, attested) → AEH 1974 O(log a/log log a) → **Kane 2004
  (this paper) O(log a · log₃a/(log₂a)²)** → Kane 2007 O(log a · log₃a/(log₂a)³)
  → MRSTT interior (bounded count for large m).
- Grows with t — not a uniform bound; it is a reproduction target only, with the
  explicit shape now primary-sourced.
- The `2m <= n` half-triangle convention (his (2.2)) is exactly this run's
  counting-convention anchor: N(t) <= 2 × (half-triangle count).
- The interpolation/derivative machinery is the "Archimedean" approach MRSTT
  reference as "work of Kane" (MR 2373115 = the 2007 paper, held).

```claim
id: kane-2004-first-improvement
statement: Kane 2004 (Integers 4 #A07, primary held): N(t) = O(log t ·
  log log log t / (log log t)^2) for t>1, where N(t) counts representations
  t = C(n,m) (both mirrors, via N(t) <= 2 * #{2m<=n}). Proof: A/B/C
  decomposition; A(t) <= (log t)^{3/4} via AEH Thm 3; B(t) <= log t/(log log
  t)^3 via Rolle+integer divided differences (gap (log log t)^4); C(t) <=
  O(log t log log log t/(log log t)^2) via the curve bound n ~ m log log t.
hypotheses: t > 1 integer; Stirling/analytic estimates for large t.
holds-here: yes — it is the 2004 rung of the bounds ladder this run surveys.
status: sourced (primary full text held)
bearing: the historical best-bound chain is now primary at the 2004 rung; the
  bound grows with t (not uniform), so it is a reproduction target, not a
  Singmaster proof.
anchor: research/summaries/kane-2004-new-bounds.md
```