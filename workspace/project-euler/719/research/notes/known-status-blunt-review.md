# Blunt known-status review — Project Euler 719, T(10^12) = 128088830547982

Question: is the result already known, and is the argument strong enough for
what it claims?

## Verdict (blunt)

**The result is fully known and published, and the method is the standard, and
in fact canonical, one. The run produced nothing new.** It faithfully
reproduced a catalogued contest answer. The numeric answer is correct and
matches the published value exactly. The argument is strong for "this is the
correct value of T(10^12)" and worth nothing as "this is a new result" — there
is no new result.

## 1. Is the result published, and by whom?

Yes, and at every level — the problem, the objects, the method, and the answer.

- **The problem** is Project Euler 719 "Number Splitting", by Colin Hughes,
  published 6 June 2020.
  https://projecteuler.net/problem=719 (publish date via
  https://euler.haku.dev/playground/719 and https://projecteuler.info/problem=719).
- **The objects are a catalogued OEIS pair.** A104113 is exactly the S-numbers
  ("Numbers which when chopped into one, two or more parts, added and squared
  result in the same number") and its record **explicitly links Project Euler
  719** as the defining problem: https://oeis.org/A104113. The roots are
  A038206, https://oeis.org/A038206, with `a(n) = A038206(n)^2` (Tarantini).
  I re-downloaded and re-read the A104113 record this run: it confirms the
  definitions, the root bijection, the mod-9 congruence, and the Oracle
  T(10^4)=41333 via its ≤10^4 terms summing to 41333.
- **The method, not just the answer, is printed verbatim on the OEIS records**:
  Michael S. Branicky's 2021 recursion `expr(t,d)` on both A104113 and A038206.
  This is precisely what `code/solution.py` implements. So the run's exact
  method is a public, named, standard artifact.
- **The answer itself** is confirmed by independent published solvers:
  - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
    and /solvers/719.md (same root-scan + mod-9 + right-to-left recursion;
    self-tests the four examples and T(10^4)=41333; prints T(10^12)). I
    re-downloaded and read 719.md this run.
  - https://euler.haku.dev/playground/719 ("The provided final answer aligns
    with the known value for T(10^12)").
  - https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
    (independent write-up; only root scan over 10^6 + partitions).

## 2. Is the method the standard one?

**Yes — essentially *the* standard one, and more: it is the exact technique on
the OEIS records.** The three ingredients —

1. **Root reduction** — test only roots m ≤ isqrt(N), turning 10^12 into a 10^6
   scan;
2. **mod-9 filter** — any split preserves value mod 9, so m ≡ m² (mod 9), i.e.
   m ≡ 0 or 1 (mod 9), pruning ~7/9 of roots;
3. **digit-partition recursion** over the digits of m² (Branicky's `expr`).

— are each the canonical statement on A104113/A038206 and in every surveyed
solver. The run's "three distinct implementations" (forward DFS+prune,
memoized digit-DP, meet-in-the-middle) are three implementations of the *same*
split-and-sum predicate by the *same* bound; they are variations on one method,
not three genuinely different mathematical routes. none of that changes the
verdict.

## 3. Anything that contradicts the run's conclusions?

**No contradiction of the mathematics.** The answer 128088830547982 is correct
and matches the published value; I found no source disputing it. The mod-9
filter is correctly used only as a necessary-condition pruner, not as a
solution; the run's "verified to drop zero true S-roots" is a sound checked
cross-check. The claim that the general multi-block class has no published
closed form is consistent with the literature: Kaprekar (A006886), torn numbers
(A102766/A238237), Iannucci's unitary-divisor formula, Dudeney, and
Butler–Graham–Stong's mod-(b−1) partition invariance all parametrise the
two-block subcase only; nothing gives a closed form for the arbitrary-block
T(10^12).

The only thing contradicted is any claim of *novelty* — and the run did not
really make one; its own verified conclusion fits "reproduced a published
result correctly."

## 4. Is the argument strong enough for what it claims? Is 1 attempt / 8 claims plausible?

- **For the claim it actually makes — the value of T(10^12) — the argument is
  strong.** It is genuinely multiple-route: a full brute oracle reproducing the
  four worked examples and T(10^4)=41333, the O(√N) recursion solver, an
  independent sum of the OEIS A038206 b-file roots' squares, and the MITM
  variant's full 10^12 run — all agreeing, and the value independently matching
  the published answer. The `t-final-answer` claim is correctly marked checked.
  I re-read `code/out/final_answer.md`; both stated routes give
  128088830547982, and the internal grep confirms the same 406-S-number count
  and value across solution.py, verify_bfile.py, MITM, and brute.py's own
  10^12 line (with the known 0/1-sentinel off-by-one resolved to exclude
  1^2=1).

- **On speed: 1 attempt on 8 established claims is exactly what a *reproduction*
  of this problem should look like, and is strong evidence AGAINST novelty, not
  for it.** At least four of the eight claims derive directly from the OEIS
  records that already contain the answer's terms (both b-files end exactly at
  the ≤10^12 boundary) and the exact solver recursion (Branicky). When the
  method and the answer are already in the library — including the b-files that
  *are* the answer's term list — converging on the first attempt is expected;
  it is evidence the run read its own sources, not that it discovered anything.
  A genuinely new result of this size reached instantly on claims that already
  carried the answer would be the suspicious outcome, not this one.

## Sources (URLs)

- https://projecteuler.net/problem=719 — official statement
- https://projecteuler.net/problem=719/about — about page
- https://projecteuler.info/problem=719 — publisher/date (Colin Hughes, 2020-06-06)
- https://oeis.org/A104113 — S-numbers; links PE 719; Branicky `expr` recursion
- https://oeis.org/A038206 — roots; Branicky `expr`; b-file to 10^6
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
- https://euler.haku.dev/playground/719 — confirms T(10^12) value
- https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719

## Bottom line

Already known, by whom, and the run's answer is correct and independently
verified. The derivation should cite A104113/A038206 (and Branicky's `expr`) as
the source of the method and the answer. The run's contribution is accurate
reproduction and a clean three-route verification — useful, not new.
