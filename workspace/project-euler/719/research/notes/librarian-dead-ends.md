# Librarian dead-end log — two leads to avoid re-fetching

These are leads this run triaged and ruled out, kept so a later run does not
spend a fetch on either. Both confirmed the library already holds everything
relevant.

## 1. DOI 10.1155/2018/1096123 resolves to an unrelated paper

`research/summaries/citations_w2811198925.md` was filed as "Citation graph — A
Review of the Self-Adaptive Traffic Signal Control System". This came from a
citation-graph walk of the Javaheri / torn-number DOI and is a **false
positive**: the DOI resolves to a traffic-signal-control paper with nothing to
do with Kaprekar numbers, torn numbers, digit-splitting, or square roots of
digit sums. OpenAlex returned it as a "cited by" of a torn-number DOI because
of a broken/misattributed DOI link, not because of any mathematical connection.

**Do not re-fetch.** Its 21 "cited by" rows are all traffic-signal-control
papers (reinforcement learning, intersection timing). None bears on PE 719.

## 2. No primary literature for the general multi-block split-and-sum class

Confirmed-by-search negative (deep_research + two exa_search queries): the
general PE 719 class — n = m^2 split into >= 2 contiguous blocks summing to m
(OEIS A104113, roots A038206) — has **no published mathematical treatment**.
Searches for the class routinely resolve to one of three *distinct* objects
that do not address it:

- **Kaprekar constants / Kaprekar transformation dynamics** (fixed points of
  the digit-rearrange-and-subtract map): "On Some Formulas for Kaprekar
  Constants", "Fixed Points and Cycles of the Kaprekar Transformation",
  "Four-digit Kaprekar dynamics in odd bases". Different operation (sort and
  subtract), different class.
- **Junction numbers** (Alekseyev–Sloane, arXiv:2112.14365): numbers u with
  >= 2 representations u = v + s(v). Different equation.
- **Sum-of-digits of squares** (Drmota–Rivat; Srichan): analytic bounds on
  s(n^2), the *whole* digit sum, not a block partition summing to the root.

None of these is a source for PE 719. The general class exists in the
literature only as the OEIS records A104113/A038206 with their exact `expr`
digit-partition recursion (`a038206-expr-recursion`). The published two-block
(Kaprekar/torn) and single-block (0,1,81) theories are already in this library.

**Consequence already stored in Cognee:** T(10^12) has no closed-form route;
the method is the O(sqrt N) root scan applying the `expr` recursion to each
m <= isqrt(N).

## 3. SSPDS (A048653) is a different class — not a source for PE 719

Downloaded `research/sources/smarandache-square-partial-digital.full.md`
(Russo 2014, Zenodo 10.5281/zenodo.9036): the Smarandache Square-Partial-Digital
Subsequence, squares whose digit string splits into blocks that are EACH
themselves square numbers. This is adjacent to but distinct from the run's
S-numbers (blocks summing to the root): e.g. 441 = 21^2 = 4|4|1 is SSPDS (blocks
are squares) but NOT an S-number (4+4+1 = 9 != 21). SSPDS does not bear on
T(10^12). Recorded so a later run does not mistake the two.

## 4. S·P numbers ("On S.P numbers", Math. Gazette) are a third, distinct class

The Mathematical Gazette "S.P numbers" thread (Parameśwaran 1997 / "82.1 On
S.P numbers" 1998; Bussmann 2001; Kominers & Kominers 2010) defines S·P
numbers as integers **equal to the product of their digits times the sum of
their digits** — e.g. 144 = 1·4·4·(1+4+4). This is a *different* operation
(digit product × digit sum), not a digit-split into blocks. It is the third
name-collision a PE719 search can hit (after the two-block Kaprekar class and
SSPDS). It does NOT bear on T(10^12). The Kominers paper (improved finiteness
bounds, sharp for base 2) is cited in the frontier; no download is held in the
library, and none is needed for this run.
