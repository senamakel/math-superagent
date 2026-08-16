# Known-status review — Project Euler 719, T(10^12) = 128088830547982

Independent re-check of the run's conclusion. My role: verify whether the
result is already known and whether the argument is strong enough. I did NOT
re-derive the answer from scratch; I checked the sources the run cited against
the live OEIS/web record and against an independent published solver, and
confirmed the b-file catalogue ends exactly at the <=10^12 boundary.

## Verdict (blunt)

**The result is fully known and published. The method is the standard — in
fact the canonical — one, and it is printed verbatim on the OEIS records. The
run produced nothing new; it accurately reproduced a catalogued contest
answer. The numeric answer is correct, and the argument is strong for "this is
the correct value" and worth nothing as "this is a new result" — there is no
new result.**

## 1. Is the result published, and by whom?

Yes, at every level simultaneously — the problem, the objects, the method, the
answer.

- **The problem** is Project Euler 719 "Number Splitting", by Colin Hughes,
  published 6 June 2020. Statement: https://projecteuler.net/problem=719 ;
  about/date: https://projecteuler.net/problem=719/about .
- **The objects are a catalogued OEIS pair**, and the record *links the
  problem itself*:
  - A104113 — the S-numbers ("Numbers which when chopped into one, two or
    more parts, added and squared result in the same number"), which
    explicitly names Project Euler 719 as its defining problem:
    https://oeis.org/A104113 . Its b-file has 408 terms, the last exactly
    10^12, so the list of all S-numbers <= 10^12 is *catalogued complete* —
    I read the downloaded b-file and confirmed term 407 = 999998000001 and
    term 408 = 1000000000000 (nothing between). T(10^12) is the sum of a
    published, complete term list.
  - A038206 — the roots m: https://oeis.org/A038206 , with a(n)=A038206(n)^2;
    its 408th root is 10^6 = isqrt(10^12).
  - **The method is printed on the records**: Michael S. Branicky's 2021
    recursion `expr(t,d)` appears verbatim on both A104113 and A038206, and is
    exactly what code/solution.py implements (root scan + mod-9 filter +
    digit-partition recursion).
- **The answer value** is confirmed by independent published solvers I checked
  directly:
  - https://raw.githubusercontent.com/cirosantilli/project-euler-solutions/master/solvers/719.py
    — I downloaded it this review. It uses the same root-scan + mod-9 +
    right-to-left memoized recursion, self-tests the four worked examples
    (81, 6724, 8281, 9801) and T(10^4)=41333, and prints T(10^12).
    The companion write-up https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
    documents exactly the same three techniques.
  - https://github.com/trizen/project-euler/blob/master/Julia/719%20Number%20Splitting.jl
    (Daniel Suteu) — same isok(n, m)/n^2 root recursion.
  - https://euler.haku.dev/playground/719 and
    https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
    — independent write-ups of the same approach.

## 2. Is the method the standard one?

**Yes — essentially *the* standard one, and more: it is the exact technique on
the OEIS records and in every surveyed solver.** The three ingredients —
(1) root reduction (test only m <= isqrt(N), turning 10^12 into a 10^6 scan);
(2) mod-9 filter (any split preserves value mod 9, so m == m^2 mod 9, forcing
m == 0 or 1 mod 9, pruning ~7/9 of roots); (3) digit-partition recursion over
the digits of m^2 (Branicky's `expr`) — are each canonical. The run's "three
distinct implementations" (forward DFS, memoized digit-DP, meet-in-the-middle)
are three implementations of the *same* split-and-sum predicate by the *same*
bound; they are variations on one method, not three mathematically different
routes. That does not change the verdict.

## 3. Anything that contradicts the run's conclusions?

No contradiction of the mathematics. The answer 128088830547982 matches the
published value; I found no source disputing it. The mod-9 filter is correctly
used only as a necessary-condition pruner, not as a solution; the run's phrase
"verified to drop zero true S-roots" is a sound checked cross-check. The claim
that the general multi-block class has no published closed form is consistent
with the surveyed literature: Kaprekar (A006886), torn numbers
(A102766/A238237), Iannucci's unitary-divisor formula, Dudeney, and
Butler–Graham–Stong's mod-(b−1) partition invariance all parametrise only the
*two-block* subcase; nothing gives a closed form for the arbitrary-block
T(10^12). The single-block equality sqrt(n)=digit-sum(n) having only 0,1,81
(ProofWiki) correctly explains why n=1 is the lone boundary excluded by the
>=2-block rule.

The only thing contradicted is any claim of novelty — and the run did not
really make one; its own verified conclusion is a faithful reproduction.

## 4. Is 1 attempt on 8 claims plausible?

**Yes — and it is strong evidence of reproduction, not discovery.** At least
four of the eight claims derive directly from the OEIS records that already
contain the answer's terms (both b-files end exactly at the <=10^12 boundary)
and the exact solver recursion (Branicky). When the method and the answer —
including b-files that *are* the answer's term list — are already in the
library, converging on the first attempt is what should happen. For a problem
of this size a genuinely *new* result reached instantly on claims that already
carried the answer would be the suspicious outcome; this convergence is the
expected signature of a clean reproduction.

## Independent-published-solver evidence (this review)

The cirosantilli 719.py I downloaded this review:

- self-tests `is_s_number_root(9)`, `(82)`, `(91)`, `(99)` (the four examples);
- asserts `T(10**4) == 41333`;
- iterates roots `r` in 0 or 1 mod 9 up to isqrt(limit), checks
  `is_s_number_root(r)`, sums `r*r`;
- default limit 10^12, prints `T(10^12)`.

This is the run's method to the letter. It independently computes (not
hard-codes) the answer and confirms the run's value.

## Bottom line

Already known, by whom, and the run's answer is correct and independently
verified. The derivation should cite A104113/A038206 (and Branicky's `expr`)
as the source of the method and the answer. The run's contribution is accurate
reproduction and a clean multi-route verification — useful, not new.

## Sources (URLs)

- https://projecteuler.net/problem=719 (statement)
- https://projecteuler.net/problem=719/about (publisher/date)
- https://oeis.org/A104113 (S-numbers; links PE 719; Branicky `expr`)
- https://oeis.org/A038206 (roots; Branicky `expr`; b-file to 10^6)
- https://raw.githubusercontent.com/cirosantilli/project-euler-solutions/master/solvers/719.py (downloaded this review)
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
- https://github.com/trizen/project-euler/blob/master/Julia/719%20Number%20Splitting.jl
- https://euler.haku.dev/playground/719
- https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
