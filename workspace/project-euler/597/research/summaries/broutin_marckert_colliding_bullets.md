# Broutin & Marckert, "The combinatorics of the colliding bullets problem" — summary

<!-- source: https://arxiv.org/pdf/1709.00789 | Nicolas Broutin, Jean-François Marckert. arXiv:1709.00789 -->

Full text at `research/sources/broutin_marckert_colliding_bullets.full.md` (91k chars).

## What the source establishes

Finite "colliding bullets" problem: n bullets fired at integer times from a
fixed gun, bullet i has iid speed V_i ~ U[0,1]. When two bullets meet they
**mutually annihilate** (unlike PE597, where the rear bumper is removed and the
front continues). Speeds are ordered by starting time, not starting position.

Main result: the distribution of the number S_n of surviving bullets is given
by a simple recurrence:
q_1(1)=1, q_1(0)=0, q_0(0)=1, and for N≥2, 0≤k≤N:
  q_N(k) = (1/N)·q_{N−1}(k−1) + (1 − 1/N)·q_{N−2}(k).
Equivalent Markov chain with memory 2: X_0=0, X_n = B_{1/n}(1+X_{n−1}) where
B_{1/n} ~ Bernoulli(1/n) — and an elegant bijection/recurrence is given. The
survivor count ~ c·log n (CLT), c computed.

The invariance is striking: the same q_N distribution holds across many
variants (accelerated bullets, different spacing schemes), because only the
*order of the speeds* matters, not their magnitudes.

## Why it is in the library (adjacent problem, useful as a contrast)

The survey report explicitly noted the "bullet process family is the adjacent
one, but its collision rule is annihilation, so it is not the right model for
this rear-removal rule." This is that adjacent paper, now on disk so the claim
"its rule is annihilation / only speed-order matters" is checkable against the
primary source rather than the run's memory. It is a **contrast**: PE597's
collision rule (rear removed, front continues, transparency of bumped boats)
is structurally different, and its parity depends on speed **magnitudes**, not
just order (a run-verified refutation). This paper's methods (recurrence on an
ordering statistic, memory-2 Markov structure) are the closest published
template to what an exact n-scaling solution for PE597 would look like — but
the rules differ, so no transfer of the result itself.

## Consistency with the run's record

Consistent with `research/torpids_exact_combinatorics_report.md`: both agree
ballistic-annihilation/bullet is NOT the right model (different removal rule,
order-alone dependence vs. magnitude dependence). No contradiction of the run's
verified refutations.