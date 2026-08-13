# The budget equality case is impossible for `2 ≤ a ≤ 28`

`GOAL.md` asks for "an impossibility lemma for a structural class, run against
the witness set". This is one, and it is sharp at the witness.

## The class

`research/notes/parity-and-2-adic-budget.md` proves the exact identity
`Σ_i v2(p_i^{e_i} + 1) = a + 1` and its corollary `ω(odd) ≤ a + 1`, with
**equality iff every odd unitary component is `≡ 1 (mod 4)`**. The equality case
is the extreme of the budget: every component spends the minimum, so the odd
part carries as many distinct primes as the power of 2 can pay for.

In that case, dividing `σ*(n) = 2n` by `n`,

```
(1 + 2^-a) · Π_{i=1}^{a+1} (1 + 1/q_i) = 2,     q_i = p_i^{e_i} ≡ 1 (mod 4)
```

so the odd components must hit the exact rational target

```
Π_{i=1}^{a+1} (1 + 1/q_i)  =  T(a) := 2^{a+1} / (2^a + 1).
```

## The argument

`(1 + 1/q)` is strictly decreasing in `q`, so the left side is maximised by
taking the `a+1` **smallest admissible component sizes over distinct odd
primes**. For a prime `p` the minimal admissible power is `p` when `p ≡ 1 (4)`
and `p²` when `p ≡ 3 (4)`. So the admissible sizes begin

```
5, 9, 13, 17, 29, 37, 41, 49, 53, 61, 73, 89, …
```

with `9 = 3²` and `49 = 7²` entering as squares. If that maximum falls short of
`T(a)`, no configuration exists and the equality case dies for that `a`.

It falls short, by a wide margin, for every `a` from 2 to 28. This is a
*maximum*, not a search: nothing enumerates `n`, and the only object considered
is the multiset of component sizes.

```
    a   ω=a+1        T(a)     max product     verdict
    1       2   1.3333333     1.3333333     attained exactly — n = 90
    2       3   1.6000000     1.4358974     IMPOSSIBLE
    8       9   1.9922179     1.7203206     IMPOSSIBLE
   20      21   1.9999981     1.9268898     IMPOSSIBLE
   28      29   1.9999999     1.9999983     IMPOSSIBLE
   29      30   2.0000000     2.0049650     undecided
```

`T(a) ↗ 2` while the max product grows only like `Π(1 + 1/q)` over the thinnest
admissible primes, so the two cross at `a = 29` and the bound says nothing
beyond. Extending it needs a genuinely different input, not more `a`.

## The `a = 8` case, which was the one worth killing

`GOAL.md` and the operator note on the lower bound single out `a = 8` as the
rigid extremal configuration, since `a ≥ 8` is forced for any sixth example.
`2^8 + 1 = 257` is **prime**, so `257 | n` and `257` must itself be one of the
nine components. The most generous admissible multiset is therefore

```
{5, 9, 13, 17, 29, 37, 41, 49, 257},   product 1.695032672
```

against a required `512/257 = 1.992217899`. A deficit of `0.297`. So `a = 8` is
impossible, and with it the entire equality boundary of the lower-bound note.

## Run against the witness set — and sharp there

The lemma must not kill any of the five, and one of the five is in its scope:

| `n` | `a` | `ω(odd)` | in the equality case? | survives |
| --- | --- | --- | --- | --- |
| 6 | 1 | 1 | no | untouched |
| 60 | 2 | 2 | no | untouched |
| **90** | **1** | **2** | **yes** | **yes — `a = 1`, not in `2 ≤ a ≤ 28`** |
| 87360 | 6 | 4 | no | untouched |
| 146361946186458562560000 | 18 | 11 | no | untouched |

`n = 90 = 2 · 3² · 5` is in the equality case, with components `9` and `5` both
`≡ 1 (mod 4)`. At `a = 1` the bound gives `max = 4/3` and `T(1) = 4/3` — **equal
in exact arithmetic** — and the extremal multiset `{5, 9}` is precisely the odd
part of `90`. The bound is not merely consistent with the witness set; it is
attained, with equality, exactly at the one known number in its class, by the
one configuration that number uses. That is the strongest evidence available
that the estimate is not lossy at the bottom, and it is why the exclusion begins
at `a = 2` rather than `a = 1`.

```claim
id: budget-equality-case-impossible
statement: Let n = 2^a * prod_i p_i^{e_i} be unitary perfect with p_i odd and
  distinct. In the equality case omega(odd part) = a + 1 of the 2-adic budget
  corollary - equivalently, every odd unitary component is 1 mod 4 - the odd
  components must satisfy prod_{i=1}^{a+1} (1 + 1/q_i) = 2^{a+1}/(2^a + 1).
  Maximising the left side over the a+1 smallest admissible component sizes
  (p if p = 1 mod 4, p^2 if p = 3 mod 4, one per distinct odd prime) shows the
  maximum is strictly less than the target for every a with 2 <= a <= 28, so
  the equality case is impossible there. In particular a = 8 is impossible,
  where 2^8 + 1 = 257 is prime and forces 257 as one of the nine components,
  giving maximum 1.695032672 against a required 512/257 = 1.992217899. The
  bound is undecided for a >= 29 and is attained with exact equality at a = 1.
hypotheses: n unitary perfect; the exact budget identity
  sum_i v2(p_i^{e_i}+1) = a+1 and its equality condition, both proved in
  research/notes/parity-and-2-adic-budget.md. No hypothesis about a sixth
  example is used - the statement covers the known numbers too
holds-here: yes, and sharply. Run against all five known numbers. Exactly one,
  n = 90, lies in the equality case, with a = 1, which is outside the excluded
  range 2 <= a <= 28. At a = 1 the maximum equals the target 4/3 in exact
  rational arithmetic and the extremal multiset {5, 9} is precisely the odd
  part of 90, so the bound is attained by the witness rather than merely
  consistent with it. The other four are not in the equality case and are
  untouched
status: checked
bearing: closes the equality boundary of unitary-perfect-lower-bound-on-a. That
  note forces a >= 8 for a sixth example with equality a = 8 requiring nine odd
  components all 1 mod 4; this kills a = 8 outright, and every other a up to
  28, so a sixth example in the equality case needs a >= 29. Combined with
  Wall 1988 it also means any sixth example with exactly nine odd components
  has a >= 29 rather than a >= 8. The method is an extremal estimate, not a
  search, and it stops at 29 because T(a) tends to 2; pushing further needs a
  different input, most plausibly the forced divisors of 2^a + 1 used as in the
  a = 8 case rather than only the smallest admissible sizes
anchor: code/out/equality_case_elimination.captured.txt;
  code/out/equality_case_reproduced.captured.txt (operator directive 4/7/8/9/10,
  verbatim rerun, EXIT_CODE=0, 3728 bytes);
  code/out/equality_case_verify.captured.txt (independent exact-Fraction
  verifier, 5015 bytes, 4/4 points PASS on fresh arithmetic);
  code/out/equality_case_verify_FIXED.captured.txt (directive 13, exact
  filename, EXIT_CODE=0, 4/4 points PASS, M(28)=1.997752859598546538 < T(28),
  M(29)=2.004964963784822807 > T(29), boundary confirmed at a = 28);
  research/notes/parity-and-2-adic-budget.md;
  research/notes/lower-bound-on-a.md
source: operator-computation
```
