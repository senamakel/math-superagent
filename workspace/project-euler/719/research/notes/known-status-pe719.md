# Known-status review: PE 719, T(10^12) = 128088830547982

Question: is the run's result already published, is the method the standard one,
and is the argument as strong as the run claims?

## 1. The result is published — it is the official answer to Project Euler 719

- **Problem page:** https://projecteuler.net/problem=719 — Colin Hughes,
  2020-06-06, "Number Splitting"; the run reproduces the problem statement
  exactly and computes the requested T(10^12).
- **Answer lists (exact match 128088830547982):**
  - https://github.com/nayuki/luckytoilet-project-euler-solutions/blob/master/Solutions.md
    — entry 719 = 128088830547982 (mirror of luckytoilet's canonical answer list).
  - https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/refs/heads/master/Solutions.md
    — entry 719 = 128088830547982.
  - https://forums.raspberrypi.com/viewtopic.php?t=286790 — independent solver
    (Sept 2020) reports T(1e12) = 128,088,830,547,982, describing PE 719 as
    "not one of the project's most mind bending problems" (solved by recursion).
- **The full answer set is itself catalogue material:**
  - https://oeis.org/A104113 — the S-numbers (0, 1, 81, 100, 1296, 2025, 3025,
    6724, 8281, 9801, 10000, …). John Drake's b-file has **408 terms ending
    exactly at 1000000000000 = 10^12**, i.e. the whole answer set is published.
    The record links Project Euler 719 directly.
  - https://oeis.org/A038206 — the roots m; b-file's first 408 terms end at
    1000000 = isqrt(10^12), term 409 = 1005291.

Result: correct and **already known**. Nothing in the answer is new; the run is
a faithful reproduction of a solved contest problem.

## 2. The method is the standard one

- Root reduction: only test m in [2, isqrt(N)], summing m^2 for roots whose
  digit string of m^2 splits into 2+ blocks summing to m. This is the approach
  of every published solver found (cirosantilli 719.py, trizen's Julia,
  ivl-projecteuler.com, the Raspberry Pi forum post).
- The digit-partition recursion is exactly the OEIS program:
  - https://oeis.org/A104113, PROG by **Michael S. Branicky** (2021-09-27):
    `def expr(t, d): if t<0: return False; if t==int(d): return True;
    return any(expr(t-int(d[:i]), d[i:]) for i in range(1, len(d)))` —
    precisely what code/solution.py implements, and the OEIS A104113/A038206
    records also print ok(m) = expr(m, str(m^2)).
  - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py
    — same recursion plus the mod-9 pruning.
- The mod-9 necessary filter (m ≡ 0 or 1 (mod 9)) is standard: it is an OEIS
  comment (Andrea Tarantini, 2021-09-27: "Every term is congruent to 0 or 1
  modulo 9") and is used in every public writeup found.

The run's structural claim that "the two-block Kaprekar/torn-number subcase is
a proper subset and the general multi-block class has no published closed form
— hence the direct recursion" is consistent with the sources: A104113 has no
formula beyond a(n) = A038206(n)^2 (also OEIS, Tarantini) and no closed form;
the two-block class is OEIS A102766/A006886, a documented proper subset.

## 3. What contradicts or weakens the run's claims

- **"Three independent routes" overstates the independence of one route.**
  code/verify_bfile.py reads the OEIS A038206 b-file and sums the squares of
  its roots — but those b-file terms *are* the published answer (A104113 links
  PE 719; Drake's b-file is titled "terms 1..408", ending at 10^12). So the
  b-file route is not a route independent of the known answer: it is a route
  that re-reads a catalogue that already contains the answer.
  Mitigating: the coverage claim (408 roots ≤ 10^6, term 409 = 1005291) is
  verified from the downloaded file (research/sources/oeis_a038206_b.full.md,
  lines 410-411), and — decisively — the MITM solver **computed** T(10^12) by
  its own code at full size in this container (attempts/03/code/out/commands.log:
  exit 0, count 406 S-numbers, "mismatches total: 0" against brute on all roots
  in [2,5000], "filter violations: 0"). So there are two genuinely computed
  full-size values (solution.py in an earlier run of record, candidates_mitm.py
  in this one), plus the catalogue read.
- The run's live re-run note honestly states solution.py exceeded the 600 s
  budget at full size and was not re-run live in the final container; the
  recorded full-size value is corroborated as above.
- Small overcount history (verify_bfile.py initially printed 128088830547983 /
  41334 including sentinel m=1) was found and fixed; the fixed route prints
  128088830547982 / 41333. This is a real (fixed) bug, worth recording.

## 4. Plausibility of 1 attempt on 8 claims

Unsurprising for this problem. The run's own claim ledger shows it rested on
`a038206-expr-recursion` (the exact Branicky recursion is in the OEIS record),
`a038206-bfile-cover` and `a104113-bfile-cover` (catalogue b-files **whose
terms are the answer**), plus the oracle and mod-9 claims. When the claims set
already contains the standard recursion and the full term list, arriving at the
catalogued answer in one attempt is expected, is not evidence of error, and
does not make the result new. Arriving fast on a known answer is exactly what
reproduction looks like.

## Sources

- https://projecteuler.net/problem=719 (and /about)
- https://github.com/nayuki/luckytoilet-project-euler-solutions/blob/master/Solutions.md
- https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/refs/heads/master/Solutions.md
- https://forums.raspberrypi.com/viewtopic.php?t=286790
- https://oeis.org/A104113 ; https://oeis.org/A038206 ; https://oeis.org/A102766
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/719.py (and /solvers/719.md)
- https://github.com/trizen/project-euler/blob/master/Julia/719%20Number%20Splitting.jl
- https://www.ivl-projecteuler.com/overview-of-problems/5-difficulty/problem-719