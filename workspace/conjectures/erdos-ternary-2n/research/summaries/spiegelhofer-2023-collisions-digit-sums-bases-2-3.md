# Spiegelhofer 2021/2023 — Collisions of digit sums in bases 2 and 3

**Source:** Lukas Spiegelhofer, "Collisions of digit sums in bases 2 and 3",
arXiv:2105.11173 (2021), published Israel J. Math 258 (2023) 475–502.
Full text: `research/sources/spiegelhofer-2023-collisions-pdf.full.md`.

## What it establishes

**Theorem 1.1 (main).** There are infinitely many nonnegative integers `n` with
`s_2(n) = s_3(n)` — a *collision* of the binary and ternary sum-of-digits
functions. More precisely, for every `δ > 0`,
`#{ n < N : s_2(n) = s_3(n) } ≫ N^{log 3 / log 4 − δ}` where `log 3/log 4 ≈ 0.792`.

This settles a folklore conjecture (posed via Deshouillers–Habsieger–Landreau–
Laishram). `s_q(n)` is the minimal number of powers of `q` needed to represent
`n` (i.e. the base-`q` digit sum).

**Separating the values is the difficulty.** `s_2(n)` and `s_3(n)` concentrate
around `(1/2)log_2 N` and `log_3 N` respectively with variance `~ log N`; the gap
between these means is `(1/log 3 − 1/log 4) log N ≈ 0.18889 log N`, which is many
standard deviations, so one expects very few collisions — only `≪ N^δ` for some
`δ < 1`. The result cannot be far from the truth.

**Connection to Erdős's ternary conjecture (a strengthening route).** The paper
records that the binary/ternary digit sums satisfy
`ν_2(binom(2n,n)) = s_2(n)` and `ν_3(binom(2n,n)) = s_3(n) − s_3(2n)/2`.
A strengthened version of Erdős's (proved) squarefree-conjecture would follow
from `s_3(2^k) − s_3(2^{k+1})/2 ≥ 2` for `k ≥ 9`, and **this in turn would follow
if `2^k` has at least two ternary digits equal to `2` for `k ≥ 9`** — because
then at least two carries appear in the ternary addition `2^k + 2^k`. (Note: 
this is a *consequence* pointed to in the introduction, and the Erdős conjecture
[no digit 2 after n>8] is strictly stronger than "at least two 2-digits".)

**Senge–Straus (finiteness of jointly small digit sums).** For coprime `p,q ≥ 2`
and any `c > 0`, only finitely many `n` have `s_p(n) ≤ c` and `s_q(n) ≤ c`.

```claim
id: SPIEGELHOFER-COLLISIONS-INFINITE
statement: (Spiegelhofer, arXiv:2105.11173, Israel J. Math 258 (2023) 475-502,
  Theorem 1.1) There are infinitely many nonnegative integers n with
  s_2(n) = s_3(n); more precisely for every delta > 0,
  #{n<N : s_2(n)=s_3(n)} >> N^(log3/log4 - delta), log3/log4 ~ 0.792.
hypotheses: s_q(n) is the base-q digit sum (= minimal number of powers of q).
holds-here: yes -- s_2 and s_3 describe the base-2/base-3 digit-sum interface
  that the run's carry-transducer route works on; the collision count is the
  distribution of equal digit sums, a sibling to the digits of 2^n problem.
status: asserted-by-source (primary text held verbatim).
bearing: the identity nu_2(binom(2n,n)) = s_2(n) and nu_3(binom(2n,n)) =
  s_3(n) - s_3(2n)/2, and the remark that 2^k having >= 2 ternary 2s for k>=9
  (two carries in the ternary sum 2^k+2^k) would yield a strengthened Erdos
  squarefree bound. Does NOT settle Erdos's ternary conjecture; the "digit 2
  avoids" statement is stronger than two carries.
anchor: research/summaries/spiegelhofer-2023-collisions-digit-sums-bases-2-3.md
```

## Implications for this run

The paper's `ν_2, ν_3` identities are the exact analytic backbone of the
Kummer-carry reformulation in this run's BLUEPRINT
(`KUMMER-CARRY-REFORMULATION`). The "two carries in `2^k+2^k`" remark is a
direct statement that *counting carries in the ternary doubling* is the natural
mechanism for the Erdős bound — precisely the direction the symbolic-invariant /
carry-transducer route pursues. It does **not** settle the Erdős conjecture; it
only records the strengthening-as-consequence relationship.

Status: sourced (primary). The `ν_2`/`ν_3` identities and Senge–Straus theorem
are proved in the paper; the exact connection to Erdős's conjecture is an
introductory remark.
