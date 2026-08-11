# Goal

## Objective

Solve Project Euler problem 175 exactly, giving the answer string it requests: the
Shortened Binary Expansion (SBE) of the smallest n for which f(n)/f(n-1) = 123456789/987654321,
formatted as comma-separated integers with no whitespace.

## Exact statement (from /workspace/problem.html, Project Euler 175)

Verbatim text of all mathematics in the statement (LaTeX rendered to plain text):

1. Definition: *"Define f(0) = 1 and f(n) to be the number of ways to write n as a sum of
   powers of 2 where no power occurs more than twice."*
   (The case n >= 1 is implicit: f(0) is set separately.)
2. Worked example: *"For example, f(10) = 5 since there are five different ways to express 10:
   10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1."*
3. Claim: *"It can be shown that for every fraction p / q (p > 0, q > 0) there exists at
   least one integer n such that f(n)/f(n-1) = p/q."* (Quoted as an assertion of the
   statement; neither proven nor used as an oracle in Phase 1.)
4. Worked example: *"For instance, the smallest n for which f(n)/f(n-1) = 13/17 is 241.
   The binary expansion of 241 is 11110001. Reading this binary number from the most
   significant bit to the least significant bit there are 4 one's, 3 zeroes and 1 one.
   We shall call the string 4,3,1 the Shortened Binary Expansion of 241."*
5. Task: *"Find the Shortened Binary Expansion of the smallest n for which
   f(n)/f(n-1) = 123456789/987654321."*
6. Output format: *"Give your answer as comma separated integers, without any whitespaces."*

The HTML contains no other examples; items 2 and 4 are the only concrete instances given.

Interpretation notes (Phase 1, no solving):
- "Powers of 2" include 2^0 = 1 (the examples use 1's), i.e. the set {1, 2, 4, 8, ...}.
- "No power occurs more than twice" means each distinct power of 2 may be used 0, 1, or 2
  times; the summands form a multiset of powers of 2, each with multiplicity at most 2.
- f(n)/f(n-1) is defined for positive integers n only (f(0) = 1 gives the n = 1 case);
  "the smallest n" ranges over n >= 1.

## Symbols

- n: positive integer argument of f; also the index in the ratio f(n)/f(n-1), so n >= 1.
- f(n): the number of multisets of powers of 2 (each distinct power of 2 occurring at most
  twice) whose elements sum to n; f(0) = 1 by definition.
- p, q: numerator and denominator of the target ratio, both positive (p > 0, q > 0);
  p/q is a positive rational and the ratio of two consecutive f-values.
- SBE of an integer m >= 1: the list of lengths of maximal runs of equal bits in the binary
  expansion of m, read from the most significant bit to the least significant bit,
  comma-separated, no whitespace. Example: m = 241, bin(241) = 11110001, runs = [1111, 000,
  1], SBE = "4,3,1".

## Test oracle (every implementation must reproduce these before full-size work)

1. f(0) = 1 (definition; f(1) = 1 follows from the single multiset {1}).
2. f(10) = 5, with exactly the five representations given in the statement:
   8+2, 8+1+1, 4+4+2, 4+2+2+1+1, 4+4+1+1.
3. The smallest n for which f(n)/f(n-1) = 13/17 is n = 241; bin(241) = 11110001;
   reading MSB to LSB there are 4 ones, 3 zeroes, 1 one; SBE(241) = "4,3,1".

## Completion criteria

- /workspace/solution.py reproduces oracle checks 2 and 3 before running at full size.
- The final answer SBE for p/q = 123456789/987654321, as a comma-separated string with no
  whitespace, obtained by the structural method (tree walk), and confirmed by an
  independent route (independent program / brute force on the largest reachable case).