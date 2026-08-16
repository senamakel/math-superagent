# Kleitman & Pachter 1998, "Finding Convex Sets Among Points in the Plane", DCG 19(3):405–410

Source: https://doi.org/10.1007/PL00009358 (Springer landing page; the full-text PDF was not
extractable this run — the held copy is the abstract + the proof-method excerpt recovered in an
earlier read_sources triage, cross-checked against the Morris–Soltan survey and Mojarrad–Vlachos).
Full text: [[kleitman-pachter-Finding-convex-sets-among-points-in-the-plane-1998.full]]

## What it establishes

- **Theorem.** $g(n) \le \binom{2n-4}{n-2} + 7 - 2n$, i.e. $ES(n) \le \binom{2n-4}{n-2} - 2n + 7$.
  This removes a full $2n-7$ from the Chung–Graham bound $\binom{2n-4}{n-2}$, the second improvement
  of 1998.
- The bound resolves to $g(n) \le \binom{2n-4}{n-2} + 7 - 2n$; for example at $n=5$:
  $\binom{6}{3}+7-10 = 20-3 = 17$ (far above the true $ES(5)=9$; it is an asymptotic-form bound).
- Acknowledges Tóth & Valtr contributed the lower-bound construction.

## The method (from the recovered proof excerpt)

Extends the Erdős–Szekeres cups/caps induction to *vertical configurations* (configurations whose
leftmost two hull points are vertical). Defines $f(n,m)$ = least points forcing an $n$-cap or
$m$-cup (exactly $\binom{n+m-4}{n-2}+1$), and $f_V(n,m)$ for vertical configurations. It proves
recurrences
$$f_V(n,m) \le f(n,m-1) + f_V(n-1,m) - 2, \qquad
  f_V(n,m) \le f(n-1,m) + f_V(n,m-1) - 2,$$
solved to the closed form
$$f_V(n,m) \le \binom{n+m-4}{n-2} + 7 - m - n.$$
Setting $m=n$ and passing to a vertical configuration yields $g(n) \le \binom{2n-4}{n-2}+7-2n$.
The engine is the **defective-point** observation: the two leftmost hull points $a,b$ can be
neither (a-defective/) left endpoints of $(n-1)$-caps nor (b-defective/) left endpoints of
$(m-1)$-cups, because extending would make a cup/cap. This "reorient to vertical + defective
extreme points" idea sharpens Chung–Graham's graph method by one unit per defect.

*Provenance note:* the exact bound is confirmed by the primary Springer abstract (held); the
method detail above is from the recovered proof text of the same paper (read_sources triage) and
corroborated by the Morris–Soltan survey digest in this library, which reports the same
$\binom{2n-4}{n-2}+7-2n$ and the defective-point technique.

## Why it matters for this run

Together with Chung–Graham, it completes the 1998 chain
$1935\binom{+1} \rightarrow \text{Chung–Graham } \binom{2n-4}{n-2} \rightarrow$
{text}-> {text}-> $\text{Kleitman–Pachter } \binom{2n-4}{n-2}+7-2n \rightarrow$
{text}-> {text}-> $\text{Tóth–Valtr } \binom{2n-5}{n-2}+2$. The defective-point / vertical-
reorientation move is itself a structural device worth keeping for the run's exact-argument goal:
it shows how a *geometric normalisation* (rotating so two extreme points are vertical) plus a
*cup/cap endpoint-defect* analysis can shave polynomial terms off a binomial — a different lever
from pure counting.

```claim
id: kp98-kleitman-pachter-bound
statement: ES(n) -> g(n) <= C(2n-4, n-2) + 7 - 2n.
hypotheses: n >= 4 (bound in binom form; far above the true value for fixed small n)
holds-here: yes
status: proved
bearing: completes the 1998 split of the 1935 binomial bound; vertical-configuration + defective
        extreme-point method. Superseded as a bound by Toth-Valtr but historically structural.
anchor: research/sources/kleitman-pachter-Finding-convex-sets-among-points-in-the-plane-1998.full.md
```
