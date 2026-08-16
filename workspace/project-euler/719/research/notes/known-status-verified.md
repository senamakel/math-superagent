# Independent known-status verification — Project Euler 719, T(10^12)

Question: is the run's result T(10^12) = 128088830547982 already known and
published, is the method the standard one, and is the argument strong enough?

This is an independent re-check; the run already carried a known-status report
(`research/notes/known-status-report.md`), and this note re-derives the verdict
from fresh searches rather than just quoting it. The conclusion is the same.

## Verdict

**The result is fully known, catalogued, and published, and the run's method is
the standard one. Nothing the run produced is new; it is an accurate
reproduction of a published contest answer.** The numeric answer is correct and
matches the published value. The verification is genuine and multi-route. But
the one-claim, eight-claim-start convergence is exactly what *should* happen
when four of those claims already carry the answer's terms and the exact solver
recursion, so the speed is evidence of reproduction, not discovery.

## 1. Is the result published, and by whom?

- **The problem** is Project Euler 719 "Number Splitting", by Colin Hughes,
  published 6 June 2020. Official statement:
  https://projecteuler.net/problem=719 ; published date via
  https://projecteuler.info/problem=719.
- **The objects are a catalogued OEIS pair.** A104113 is exactly the S-numbers
  ("Numbers which when chopped into one, two or more parts, added and squared
  result in the same number") and its record **explicitly links Project Euler
  719** as the defining problem: https://oeis.org/A104113. The roots are
  A038206, https://oeis.org/A038206, with `a(n) = A038206(n)^2` (Tarantini).
- **The method, not just the answer, is in the public record.** The OEIS
  records print Branicky's exact solver recursion `expr(t,d)` (2021), which is
  precisely what `code/solution.py` implements.
- **The b-files catalogue the ≤ 10^12 list.** A104113's b-file has 408 terms,
  the last exactly 10^12; A038206's b-file's 408th root is exactly
  isqrt(10^12) = 10^6. So the sum the run computed, T(10^12), is the sum of a
  catalogued, complete term list.
- **Independent published/euler solvers** confirm the same value and method:
  - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
    (root scan + mod-9 + recursion; self-tests the four examples and
    T(10^4)=41333; prints T(10^12)).
  - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
    (documents the same three techniques).
  - https://euler.haku.dev/playground/719 and
    https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
    (independent write-ups of the same approach).

## 2. Is the method the standard one?

Yes — essentially **the** standard one, and the run's method is not one of
several accepted approaches but the exact technique on the OEIS records and in
every surveyed solver: (1) root reduction (test only m ≤ isqrt(N), so 10^6
roots instead of 10^12 numbers); (2) mod-9 filter (any split preserves value
mod 9, so m ≡ m² (mod 9), i.e. m ≡ 0 or 1 (mod 9)); (3) the digit-partition
recursion `expr` over the digits of m². The run's "three distinct
implementations" (DFS+prune, DT-memoized digit-DP, meet-in-the-middle) are
three flavours of the *same* split-and-sum predicate, not three genuinely
different mathematical routes; the MITM variant is the only one not literally on
the OEIS page, and it solves the same predicate by the same bound.

## 3. Anything that contradicts the run's conclusions?

- **The numeric answer is correct.** 128088830547982 matches the published
  value (cirosantilli 719.py prints it; the independent b-file sum confirms it).
  No contradiction found.
- **The claim "the general multi-block class has no published closed form"**
  is consistent with the literature surveyed: Kaprekar numbers (A006886), torn
  numbers (A102766/A238237), Iannucci's unitary-divisor formula, Dudeney, and
  Butler–Graham–Stong's mod-(b−1) partition invariance all parametrise the
  **two-block** subcase only; no source gives a closed form for the arbitrary-
  block T(10^12). I found no counter-source.
- **Mod-9 is only a necessary filter.** It must not be mistaken for a solution;
  the run correctly treats it as pruning, and its "verified to drop zero true
  S-roots" is a checked necessary-condition cross-check, sound but not the
  method.

## 4. Is the argument strong enough for what it claims?

For the claim it actually makes — *this is the correct value of T(10^12)* — the
argument is strong. It is genuinely multiple-route: a full brute oracle
reproducing the four worked examples and T(10^4)=41333, the O(√N) recursion
solver, and an independent sum of the OEIS A038206 b-file roots' squares, all
agreeing, and the value independently matches the published answer. The
`t-final-answer` claim is correctly marked "checked".

The one thing the argument is **not** strong enough for is novelty. There is
none; this is a known, catalogued contest answer.

## On speed / the 1-attempt, 8-claim start

Bluntly: a result reached in 1 attempt on 8 established claims is *expected* for
a problem of this size, and is not evidence of a new result. At least four of
the eight claims come directly from the OEIS records that already contain the
answer's terms (both b-files end exactly at the ≤ 10^12 boundary) and the exact
solver recursion (Branicky). The run converged immediately because the method
and the answer were already in the library, not because it discovered anything.
That does not make the computation wrong — every check passes — it makes it a
faithful reproduction. The correct framing is "reproduced a published result
well", not "solved something new".

## Sources (URLs)

- https://projecteuler.net/problem=719 — official problem statement
- https://projecteuler.info/problem=719 — publisher/date (Colin Hughes, 2020-06-06)
- https://oeis.org/A104113 — S-numbers; links PE 719; Branicky `expr` recursion
- https://oeis.org/A038206 — roots m; Branicky `expr`; b-file to 10^6
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
- https://euler.haku.dev/playground/719 — confirms value
- https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
