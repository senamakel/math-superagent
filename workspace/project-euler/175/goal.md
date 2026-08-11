# Goal

## Objective

Solve Project Euler problem 175 exactly, giving the answer string it requests.

## Exact statement (from /workspace/problem.html, Project Euler 175)

- Define f(0) = 1, and for n >= 1 let f(n) be the number of ways to write n as a sum of
  powers of 2 where no power occurs more than twice.
- Worked example: f(10) = 5, since the five ways to express 10 are
  10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1.
- Claim: for every fraction p/q (p > 0, q > 0) there exists at least one integer n such
  that f(n)/f(n-1) = p/q.
- Worked example: the smallest n for which f(n)/f(n-1) = 13/17 is 241. The binary
  expansion of 241 is 11110001. Reading MSB to LSB there are 4 ones, 3 zeroes, 1 one;
  the string "4,3,1" is the **Shortened Binary Expansion** (SBE) of 241.
- Task: find the Shortened Binary Expansion of the smallest n for which
  f(n)/f(n-1) = 123456789/987654321.
- Output format: comma separated integers, without any whitespaces.

## Symbols

- n: positive integer argument of f (also the index in the ratio f(n)/f(n-1)).
- f(n): count of multisets of powers of 2 (each power of 2 used at most twice) summing to n.
- p, q: numerator and denominator of the target ratio, p > 0, q > 0.
- SBE of an integer m: the list of lengths of maximal runs of equal bits in the binary
  expansion of m, read from the most significant bit to the least significant bit,
  comma-separated, no whitespace.

## Test oracle (every implementation must reproduce these before full-size work)

1. f(0) = 1, f(1) = 1 (definition).
2. f(10) = 5, with exactly the five partitions listed above.
3. The smallest n with f(n)/f(n-1) = 13/17 is n = 241; bin(241) = 11110001; SBE = 4,3,1.

## Completion criteria

- /workspace/solution.py reproduces oracle checks 2 and 3 before running at full size.
- The final answer SBE for p/q = 123456789/987654321, as a comma-separated string with no
  whitespace, obtained by the structural method (tree walk), and confirmed by an
  independent route (independent program / brute force on the largest reachable case).