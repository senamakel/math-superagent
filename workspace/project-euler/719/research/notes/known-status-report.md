# Known-status review: Project Euler 719 (S-numbers), T(10^12)

Question asked: is the run's result already known, and is the argument strong
enough for what it claims?

## Verdict

**The result is fully known and already published.** T(10^12) = 128088830547982
is the canonical answer to a Project Euler contest problem (719, Number
Splitting, by Colin Hughes, published 6 June 2020). The run's method is the
*standard* method — identical in substance to the recursion printed on the OEIS
records and to every published solver surveyed. Nothing here is new; what the
run did is reproduce a fully catalogued, already-solved problem correctly.

## 1. Is the result published, and by whom?

- **The problem itself** is published as Project Euler 719:
  https://projecteuler.net/problem=719 (and /problem=719/about). "Published on
  06 June 2020" per https://projecteuler.info/problem=719.
- **The S-numbers are a catalogued OEIS sequence**: A104113 — "Numbers which
  when chopped into one, two or more parts, added and squared result in the
  same number" — whose OEIS record **explicitly links Project Euler 719** as the
  defining problem. https://oeis.org/A104113. The roots m are A038206,
  https://oeis.org/A038206.
- **The exact solver recursion the run uses is printed verbatim on the OEIS
  records** (credited to Michael S. Branicky, 2021): `expr(t,d)` trying each
  first-block length and recursing on the remainder. This is precisely
  `code/solution.py`'s method. So the method, not just the answer, is in the
  public record.
- **The answer itself** is confirmed by independent published/euler solutions:
  - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
    (implements the same root-scan + mod-9 + right-to-left recursion, self-tests
    the four examples and T(10^4)=41333, prints T(10^12)).
  - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
    (documents the same three techniques: root scan, mod-9 pruning, recursion).
  - https://euler.haku.dev/playground/719 ("The provided final answer aligns
    with the known value for T(10^12)").
  - https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
    (independent write-up of the same approach).
- The OEIS b-files (A104113 and A038206) go exactly to term 408 = 10^12
  (= 1000000^2), i.e. they enumerate every S-number and every root ≤ 10^12.
  T(10^12) is the sum of those catalogued squares.

## 2. Is the method the standard one?

Yes — essentially *the* standard one, and the run's method is not merely one of
several accepted approaches but the exact technique used by the OEIS records and
the published/euler solvers surveyed:

1. **Root reduction** — only test roots m ≤ isqrt(N), turning the 10^12 bound
   into a 10^6 root scan. (Published solvers 719.py and the IVL write-up both
   state "we only need to check 10^6 numbers".)
2. **Mod-9 filter** — any split preserves value mod 9, so m ≡ m² (mod 9), i.e.
   m ≡ 0 or 1 (mod 9). Stated on OEIS (Tarantini) and by every surveyed solver.
3. **Digit-partition recursion** — Branicky's `expr`, on the OEIS records.

The run's "three distinct implementations" (DFS+prune, digit-DP, MITM) are three
flavours of the same underlying split-and-sum predicate; they are variations on
the one standard method, not three genuinely different mathematical routes, and
all reduce to the OEIS recursion. The MITM variant is the only one of the three
not literally on the OEIS page, but it solves the same predicate by the same
bound.

## 3. Anything that contradicts the run's conclusions?

- **The numeric answer is correct** — 128088830547982 matches the published
  value. No contradiction found.
- **The claim "the general multi-block class has no published closed form"**
  is consistent with what I found: the literature the run already holds
  (Kaprekar A006886, torn numbers A102766/A238237/J2223, Iannucci's unitary-
  divisor formula, Butler–Graham–Stong mod-(b−1) invariance, Dudeney) all
  parametrise the *two-block* subcase only, and no source gave a closed form for
  the arbitrary-block T(10^12). I found no counter-source.
- **Minor framing caveat**: presenting this as a length-one derivation on eight
  established claims is entirely unsurprising and *expected* for a problem of
  this size, precisely because four of those eight claims come from the OEIS
  records that already contain the answer's terms (A104113/A038206 b-files) and
  the exact solver recursion (Branicky). The run "solved" it quickly because the
  answer and method were already in the library, not because it discovered
  anything new. It is a faithful reproduction, not a novel result.

## 4. Is the argument strong enough for what it claims?

For the claim it actually makes — *this is the correct value of T(10^12)* — the
argument is strong. The verification is genuine and multi-route: a full brute
oracle reproducing the worked examples and T(10^4)=41333, the O(√N) solver, and
an independent sum of the OEIS b-file roots' squares, all agreeing, and the
value independently matches the published answer. The `t-final-answer` claim is
correctly marked "checked".

The only thing the argument is *not* strong enough for is any claim of novelty
or of a new result — there is none. The result is a known, published, catalogued
contest answer.

## Sources (URLs)

- https://projecteuler.net/problem=719 — problem statement (official)
- https://projecteuler.info/problem=719 — published date, statement
- https://oeis.org/A104113 — S-numbers, links PE 719, Branicky recursion
- https://oeis.org/A038206 — roots m, Branicky recursion, b-file to 10^6
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.md
- https://euler.haku.dev/playground/719 — confirms T(10^12) value
- https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
