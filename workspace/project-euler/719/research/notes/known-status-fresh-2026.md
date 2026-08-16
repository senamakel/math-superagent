# Known-status review — Project Euler 719, T(10^12) = 128088830547982

Question asked of this run: is the result already known, and is the argument
strong enough for what it claims? Do not try to solve the problem; find out
whether the result is published, whether the method is the standard one, and
anything that contradicts the run's conclusion. Be blunt about the second
question.

This is a fresh re-derivation, independent of the four known-status notes the
run already carried (`research/notes/known-status-{report,blunt-review,pe719,
verified}.md`), reached by new web searches in this pass.

## Verdict

**The result is fully known, catalogued, and published, and the numeric answer
is correct. The method is the standard — in fact the canonical — one. Nothing
in the run is new; it is an accurate reproduction of a solved contest problem
by the published technique. The argument is strong for "this is the correct
value of T(10^12)" and worth nothing as novelty, because there is no novelty.**

## 1. Is the result published, and by whom?

Yes — at every level: the problem, the objects, the method, and the answer.

**The problem.** Project Euler 719 "Number Splitting", by **Colin Hughes**,
published 2020-06-06.
- https://projecteuler.net/problem=719 (official statement)
- https://projecteuler.net/problem=719/about

**The objects are a catalogued OEIS pair, and the OEIS record names this
problem as its defining application.**
- **A104113** — the S-numbers themselves: "Numbers which when chopped into one,
  two or more parts, added and squared result in the same number."
  https://oeis.org/A104113. The record **links Project Euler 719 directly**.
  John Drake's b-file has **408 terms, the last exactly 10^12** — i.e. the
  complete set of S-numbers ≤ 10^12 is catalogued.
- **A038206** — the roots m, with `a(n)^2 = A104113(n)` (Tarantini).
  https://oeis.org/A038206. The b-file's 408th term is exactly
  isqrt(10^12) = 10^6 (term 409 = 1005291 > 10^6), so it enumerates every
  S-root ≤ 10^12. Every term ≡ 0 or 1 (mod 9).

**The method is in the public record, not just the answer.** The OEIS records
print **Michael S. Branicky's** 2021 solver recursion `expr(t,d)` verbatim —
the exact recursion `code/solution.py` implements.

**The answer.** The value 128088830547982 appears, as exactly this number, in
independent published answer lists and solvers:
- https://github.com/nayuki/luckytoilet-project-euler-solutions/blob/master/Solutions.md — entry 719 = 128088830547982
- https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/refs/heads/master/Solutions.md — entry 719 = 128088830547982
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py (and /solvers/719.md) — same method, self-tests the four examples and T(10^4)=41333, prints T(10^12)
- https://github.com/gagan405/rs-playground/commit/6a18496... — Rust solver with `assert_eq!(128088830547982, find_sum_s_numbers())`
- https://forums.raspberrypi.com/viewtopic.php?t=286790 — independent solver (Sept 2020) reports T(1e12) = 128,088,830,547,982
- https://euler.haku.dev/playground/719 and https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719 — independent write-ups of the same approach

## 2. Is the method the standard one?

**Yes — essentially *the* standard one, and more: it is the exact technique
printed on the OEIS records and used by every published solver surveyed.** The
three ingredients:

1. **Root reduction** — an S-number is determined by its root m, so test only
   m in [2, isqrt(N)] and sum m². Turns the 10^12 bound into a 10^6 root scan.
   Stated by every surveyed solver (cirosantilli 719.md, IVL, trizen's Julia).
2. **Mod-9 filter** — any split preserves value mod 9, so m ≡ m² (mod 9), i.e.
   m ≡ 0 or 1 (mod 9). An OEIS comment (Andrea Tarantini, 2021-09-27) and in
   every public writeup. Prunes ~7/9 of roots.
3. **Digit-partition recursion** — Branicky's `expr(t,d)`: try each first-block
   length, recurse on the remainder. Precisely `code/solution.py`'s method.

The run's "three distinct implementations" (forward DFS+prune, memoized
digit-DP, meet-in-the-middle) are three flavours of the *same* split-and-sum
predicate by the same bound — not three genuinely different mathematical
routes. The MITM variant is the only one not literally on the OEIS page, and it
solves the same predicate; its role here is as a second computed full-size
route, not as a new method.

## 3. Anything that contradicts the run's conclusions?

**No contradiction of the mathematics.** The number is correct and matches the
published value; I found no source disputing it. Three notes of caution about
*claims framing*, none about the number:

- **The "three independent routes" overstates the independence of the b-file
  route.** `verify_bfile.py` sums the squares of the OEIS A038206 b-file roots
  — but those b-file terms *are* the published answer (A104113 links PE 719;
  Drake's b-file is titled "terms 1..408" ending at 10^12). So the b-file route
  is a route that re-reads a catalogue already containing the answer; it is an
  independent *program* but not an independent *source*. What does genuinely
  provide a second computed value is the **MITM solver**, which ran a full
  live 10^12 computation (`attempts/03/code/out/candidates_mitm.txt`:
  count 406, exactly matching; worked examples, T(10^4)=41333, T(10^6),
  T(10^9), T(10^12) all reproduced). So there are two genuinely computed
  full-size values (solution.py on record, candidates_mitm.py live), plus the
  catalogue read.
- **solution.py was not re-run live at full size in the final container.**
  `code/out/live_rerun.captured.txt` records that Python `solution.py 10^12`
  exceeds the 600 s tool budget (10^11 took 106 s, growth superlinear), so the
  full-size value at 10^12 is confirmed there only by the independent b-file
  route; the solver agrees with brute at every reachable size (10^4, 10^6,
  10^9). The recorded full-size value is independently corroborated by the MITM
  live run.
- **"The general multi-block class has no published closed form"** is
  consistent with the literature surveyed (Kaprekar A006886, torn numbers
  A102766/A238237, Iannucci's unitary-divisor formula, Dudeney,
  Butler–Graham–Stong mod-(b−1) invariance all parametrise the two-block
  subcase only; nothing gives a closed form for arbitrary-block T(10^12)). One
  historical note: the run's own GOAL/CONTEXT point out that `verify_bfile.py`
  once printed 128088830547983 / 41334 including sentence sentinel m=1 before
  the `m >= 2` filter was applied; the fixed route prints the correct
  128088830547982 / 41333. That was a real, found, and fixed bug.

## 4. Is the argument strong enough? Is 1 attempt / 8 claims plausible?

- **For the claim it actually makes — the value of T(10^12) — the argument is
  strong.** It is genuinely multi-route: a brute oracle reproducing the four
  worked examples and T(10^4)=41333, the O(√N) recursion solver, and the MITM
  solver's full live 10^12 run (count 406), all agreeing, and the value
  independently matches the published answer. The `t-final-answer` claim is
  correctly marked "checked."

- **On speed: 1 attempt on 8 established claims is exactly what a
  *reproduction* of this problem looks like, and is strong evidence AGAINST
  novelty, not for it.** At least four of the eight claims derive directly from
  the OEIS records that already contain the answer's terms (both b-files end
  exactly at the ≤ 10^12 boundary) and the exact solver recursion (Branicky).
  When the method and the answer are already in the library — including the
  b-files that *are* the answer's term list — converging on the first attempt
  is expected; it is evidence the run read its own sources, not that it
  discovered anything. A genuinely new result of this size reached instantly on
  claims that already carried the answer would be the suspicious outcome, not
  this one.

## Bottom line

**Already known, by Colin Hughes's Project Euler 719, catalogued as OEIS
A104113/A038206, with Branicky's recursion as the standard method, and the
answer 128088830547982 published in multiple independent answer lists. The run
reproduced it correctly with a genuine two-computed-route verification. The
derivation should cite A104113/A038206 (and Branicky's `expr`) as the source
of both method and answer.** Nothing here is new; the contribution is accurate
reproduction and a clean multi-route verification.

## Sources (URLs)

- https://projecteuler.net/problem=719 (official statement) and /about
- https://oeis.org/A104113 — S-numbers; links PE 719; Drake b-file 408 terms to 10^12; Branicky `expr`; Tarantini mod-9
- https://oeis.org/A038206 — roots; Branicky `expr`; b-file 408th term = 10^6 = isqrt(10^12)
- https://github.com/nayuki/luckytoilet-project-euler-solutions/blob/master/Solutions.md — entry 719 = 128088830547982
- https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/refs/heads/master/Solutions.md — entry 719 = 128088830547982
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py and /solvers/719.md — same method
- https://github.com/gagan405/rs-playground/commit/6a18496fa9eaceea018a73b0cd3e91da3892c7fc — Rust assert 128088830547982
- https://forums.raspberrypi.com/viewtopic.php?t=286790 — independent solver reports 128,088,830,547,982
- https://euler.haku.dev/playground/719 ; https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719
- https://github.com/trizen/project-euler/blob/master/Julia/719%20Number%20Splitting.jl
