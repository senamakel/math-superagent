# G-supply crux settled in the negative: the switch count is genuinely two-point

**Cycle / source:** librarian, 2026, chasing the sole open REQUEST ("G-supply", the
supply-side lower bound ν₂(q_{n-1}) ≥ n^β, β > 0.525, or ν₂ ≥ c·n).

**Status:** settled (negative for the unconditional direction). Recorded so the
next worker does not re-derive the ONE mathematical fact that decides whether
Route B can ever be made unconditional.

## The crux, from REQUESTS.md

> A source showing the mod-4 switch bit is a one-point statistic (then
> GRH/Dirichlet suffices), OR a theorem delivering ν₂ > n^{0.525+δ}
> unconditionally, OR a source showing no positive-linear lower bound is
> provable from current methods.

## Settlement

The switch bit is **NOT a one-point statistic**. It is two-point. Therefore
GRH/Dirichlet (one-point PNT-in-AP) does **not** suffice, and the unconditional
linear bound ν₂ ≥ c·n is **not** derivable from current analytic tools. This is
the third bullet ("no positive-linear lower bound is provable from current
methods"), now established by argument.

### Why two-point is forced — the countermodel

Let `N_switch(x) = #{p_n ≤ x : p_{n+1} ≢ p_n (mod 4)}`. This is exactly ν₂ (the
bit `h[j] = (gap_j//2) mod 2` is 1 iff `gap_j ≡ 2 (mod 4)` iff the consecutive
pair switches parity-of-class).

One-point data from PNT-in-AP:
```
#{p ≤ x : p ≡ 1 mod 4} ≈ #{p ≤ x : p ≡ 3 mod 4} ≈ π(x)/2.
```
These two marginals alone impose **zero** lower bound on N_switch. An ordering
that lists all 1-mod-4 primes followed by all 3-mod-4 primes (which is
*consistent with* the marginals) achieves a single switch — N_switch = 1 is not
ruled out by any one-point theorem. A lower bound on the switch count is a
statement about the **joint** distribution of two consecutive primes, which is
exactly the prime k-tuple / Hardy–Littlewood correlation. In short:
```
class counts (one-point)       do not constrain   consecutive-pair switches (two-point)
```

### LOS-2016: the leading term is CONJECTURAL for r ≥ 2

The library claim `los-2016-consecutive-pair-mod4-bias` carried the phrase
"main term unconditional from PNT-in-AP". That is an **overstatement** and
should be read as corrected here. LOS 2016 (PNAS 113:31 E4446) state their
r-tuple formula
```
π(x; q, a) = li(x)/φ(q)^r (1 + c1(q;a) loglog x/log x + c2(q;a)/log x + O((log x)^{-7/4}))
```
as a **main conjecture** (labeled Conjecture in the paper). For r = 2 the
leading coefficient li(x)/φ(q)^2 is precisely the Hardy–Littlewood k-tuple
prediction; PNT-in-AP supplies only the one-point r = 1 case. The bias/pattern
*structure* (the c1, c2 refinements) is entirely conjectural. So "ν₂ = n/2 to
first order" is expected on the k-tuple conjecture, NOT unconditional.

### The unconditional literature is on the WRONG (non-switch) side

- **Ruzsa 2001, "Consecutive primes modulo 4", Indag. Math. 12(4):489–503**
  (abstract held via Martin et al. 2024 field survey, arXiv:2309.08729, entry
  [231]; full text paywalled — do not re-attempt the DOI): the number of
  consecutive-prime pairs ≤ x **both ≡ 1 (mod 4)** is `≫ x loglog x / log² x`
  (improving Shiu; method of Maier). This is a lower bound on the **equal-
  residue / non-switch** direction — it bounds pairs that do NOT contribute to
  ν₂, i.e. it pushes the switch count DOWN, giving nothing to ν₂. Generalizes
  to any φ(q)/2 reduced classes mod q.
- **Maynard 2015** (small gaps) gives a positive proportion of admissible
  k-tuples realized as **small gaps**, i.e. about gap *sizes*, not about the
  mod-4 residue-switch density. Orthogonal to ν₂.
- **Lau 2024** (arXiv:2409.12819) shows infinitely many realized residue
  patterns via an r-th-moment Maynard–Tao sieve, but the pattern count gives no
  density, and it improves the *lower bound on number of patterns*, not the
  switch density.
- **Ash–Beltis–Gross–Sinnott 2011** (Exp. Math. 20) give a *heuristic* formula
  (inclusion–exclusion / Pólya cutoff) for consecutive-pair residue
  frequencies — confirmation of the k-tuple-level structure, not a theorem.

## Consequence for Route B

Granville's reduction (Theorem 5.5) turns GC into ν₂ > n^β with β > 0.525,
where the demand side α = 0.525 is unconditional (Baker–Harman–Pintz) and the
supply side ν₂ ≥ c·n is the sole open content. This cycle establishes:

- The supply side is **two-point**, hence **conjectural at the leading order**
  (needs Hardy–Littlewood / k-tuple), and
- **no unconditional positive-linear lower bound is provable from PNT-in-AP /
  GRH / Dirichlet alone** — the one-point machinery is structurally blind to
  the switch count (explicit countermodel above).

So Route B cannot be closed unconditionally by analytic number theory at the
current state of the art. The honest form of the deliverable is a **conditional
proof**: "Assuming the Hardy–Littlewood / k-tuple conjecture (or its two-point
mod-4 special case), GC follows via the ν₂ reduction." That is a genuine partial
result — it pins GC to a single, standard, conjectural two-point correlation —
but it must be stated as conditional, never as unconditional.

## What would falsify this settlement

A source delivering N_switch(x) ≥ c·π(x) (or ≥ c·x/log x) with c > 0
unconditionally. None exists in the literature (searches 2026, incl. 2023–25
papers); every unconditional result touches the non-switch side or gap sizes.
The same-class lower bounds (Ruzsa/Shiu/Martin, sub-density `x loglog x/log² x`)
are the classical obstruction and are held in the library.

## Filing

- This note: `research/notes/g-supply-two-point-crux-settled.md`.
- The correction to the LOS overstatement is recorded here; the claim ledger
  row `los-2016-consecutive-pair-mod4-bias` should be read with "the leading
  term requires the (open) k-tuple conjecture, not PNT-in-AP."
