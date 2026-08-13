# MRSTT exact theorem statement — Singmaster in the interior

Source: K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen,
"Singmaster's conjecture in the interior of Pascal's triangle",
arXiv:2106.03335v1 (7 Jun 2021), Quart. J. Math. 73 (2022) 1137–1177.

Full text held at `research/sources/mrstt-fulltext.full.md` (123KB).
Summary at `research/summaries/mrstt-fulltext.md`.

## Counting convention (same as the rest of this run)

N(a) counts both mirrors (n,k) and (n,n-k) AND the trivial pair
C(a,1)=C(a,a-1). So N(3003)=8 under this convention, 4 in half-triangle.

## Theorem 1.3 (Interior Theorem) — literal statement

Let 0 < ε < 1. Let n and m be integers with

    exp((log n)^{2/3+ε}) ≤ m ≤ n/2                                    (1.3)

and let t = C(n,m). Then for t sufficiently large depending on ε, the
equation C(n',m') = t has at most TWO solutions (n',m') in the region
(1.3). Consequently, in the symmetric interior

    exp((log n)^{2/3+ε}) ≤ m ≤ n - exp((log n)^{2/3+ε})               (1.4)

the equation has at most FOUR solutions.

### Refinement (Theorem 1.3, second part)

For 0 < ε' < ε/(2/3+ε), in the region

    exp((log n)^{2/3+ε}) ≤ m ≤ n / exp((log n)^{1-ε'})

there is at most ONE solution.

### Sharpness (Remark 1.4)

The bound of two (resp. four) is sharp: the infinite Fibonacci family
C(F_{2j+2}F_{2j+3}, F_{2j}F_{2j+3}) = C(F_{2j+2}F_{2j+3}-1, F_{2j}F_{2j+3}+1)
provides infinitely many t with exactly two solutions in the left-half
interior (hence four in the full interior). These are the solutions to
C(n+1,m+1)=C(n,m+2).

## What this reduces the conjecture to (Remark 1.5)

To prove Singmaster's conjecture (N(t) = O(1)), it now suffices to handle
the **boundary region**:

    2 ≤ m ≤ exp((log n)^{2/3+ε})                                       (1.5)

Equivalently, in terms of t:

    2 ≤ m ≤ (log t) / (log log t)^{3/2 - ε}                            (1.6)

This is the **exact open gap**. The interior is settled; the small-m
regime (where m/log t → 0) is the whole remaining problem.

## Remark 1.11 — no interior value 3

A modification of the proof shows there cannot be exactly THREE solutions
in the interior (1.4). The possible interior multiplicities are 0, 1, 2, 4.

## Effectiveness and uniformity

- **effective: yes** — confirmed from the full text, Remark 1.7, which states
  verbatim: "The implied quantitative bounds in the hypothesis 't is
  sufficiently large depending on ε' are effective; however, we have made no
  attempt whatsoever to optimize them in this paper, and will likely be too
  large to be of use in numerical verification of Singmaster's conjecture in
  their current form." So the threshold is a computable function of ε — not
  non-constructive — but unoptimized and astronomically large. This is the
  effective-versus-usable distinction GOAL.md demands: an effective constant
  nobody can evaluate is a different object from a bound.
- **uniform-in-k: yes (over the interior)** — the theorem covers all m in the
  stated range simultaneously; it does not fix (k1,k2) pairs. This is what
  makes MRSTT genuinely stronger than per-pair Siegel/Faltings: it is uniform
  over all m in the interior.
- **uniform-in-the-boundary: no** — the theorem explicitly does NOT cover
  the boundary (1.5)/(1.6). The method has a hard ceiling there (Prop 1.12).
- **size of the threshold:** no explicit expression is given in the paper;
  Remark 1.7 says the constant was not optimised and "will likely be too large
  to be of use in numerical verification of Singmaster's conjecture in their
  current form." It is an effective-but-unusable bound, not a usable one.

## Method and its limit (Proposition 1.12)

The proof uses non-archimedean equidistribution of fractional parts
{v_p(C(n,m))} over primes p in [P, P + P/log^100 P], with
P ≈ exp((log n)^{2/3+ε/2}). The key estimate requires

    N, M = O(exp(log^{3/2-ε} P))

where N, M are the parameters being compared. Even under the Riemann
Hypothesis this restriction cannot be relaxed; only a randomness heuristic
would push the range to exp(P^c), which would lower the interior boundary
function from exp((log n)^{2/3+ε}) to (log n)^C.

**Implication**: the 2/3 exponent is a genuine barrier for the interior
method. Extending the interior theorem to smaller m requires a fundamentally
different technique — improving constants cannot bridge the gap.

## Theorem 1.8 — falling factorial analogue

For the falling factorial (n)_m = n(n-1)...(n-m+1), at most TWO integer
solutions in exp((log n)^{2/3+ε}) ≤ m < n. Sharp (family
(a^2-a)_{a^2-2a} = (a^2-a-1)_{a^2-2a+1} attains it).

## Table: what is and is not covered

| Region | m range (in n) | Bound | Method | Effective? | Uniform in k? |
|--------|---------------|-------|--------|-----------|---------------|
| Interior (MRSTT Thm 1.3) | exp((log n)^{2/3+ε}) ≤ m ≤ n/2 | ≤2 (≤4 full) | non-archimedean equidistribution | yes (huge) | yes |
| Deep interior (Thm 1.3) | exp((log n)^{2/3+ε}) ≤ m ≤ n/exp((log n)^{1-ε'}) | ≤1 | same | yes (huge) | yes |
| Boundary (open) | 2 ≤ m ≤ exp((log n)^{2/3+ε}) | unknown | — | — | — |
| Fixed (k1,k2) | m=k1, m'=k2 fixed | finite | Siegel/Faltings | no | no |

```claim
id: mrstt-exact-statement
statement: MRSTT Theorem 1.3 (arXiv:2106.03335, QJM 2022): For 0<ε<1 and t
  sufficiently large (effective threshold), C(n,m)=t has at most 2 solutions in
  exp((log n)^{2/3+ε}) ≤ m ≤ n/2 (at most 4 in the full symmetric interior
  exp((log n)^{2/3+ε}) ≤ m ≤ n-exp((log n)^{2/3+ε})), and at most 1 in
  exp((log n)^{2/3+ε}) ≤ m ≤ n/exp((log n)^{1-ε'}). To prove Singmaster it now
  suffices to handle the boundary 2 ≤ m ≤ exp((log n)^{2/3+ε}), equivalently
  2 ≤ m ≤ (log t)/(log log t)^{3/2-ε}. The bound of 2/4 is sharp (infinite
  Fibonacci family attains it). Interior multiplicities cannot be exactly 3
  (Remark 1.11). The method's non-archimedean equidistribution requires
  N,M = O(exp(log^{3/2-ε} P)), cannot be relaxed even under RH, making the
  2/3 exponent a genuine barrier (Prop 1.12).
hypotheses: 0<ε<1; t sufficiently large depending on ε; counting both mirrors
  plus trivial pair (N(3003)=8 convention).
holds-here: yes — this is the current record theorem for the interior.
status: asserted-by-source (full text held; not re-derived here)
bearing: Reduces Singmaster to the boundary (1.5)/(1.6). The entire remaining
  gap is the small-m regime. The constant is effective (yes) and uniform in
  k over the interior (yes), but does not cover the boundary (no).
effective: yes (confirmed from full text Remark 1.7; effective-but-huge, not
  non-constructive)
uniform-in-k: yes (over the interior range; no over the boundary)
anchor: research/approaches/mrstt-exact-statement.md
```
