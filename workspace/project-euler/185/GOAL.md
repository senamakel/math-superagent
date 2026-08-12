# Goal

Solve Project Euler 185 (Number Mind).

**Statement.** A secret sequence of N digits is hidden. We are given M guesses,
each a string of N digits together with an integer c = number of positions in
which the guess agrees with the secret (exactly those positions; wrong-place
digits convey nothing).

Find the unique secret sequence that is consistent with every guess.

**Symbols.**
- N: length of the secret sequence.
- M: number of guesses.
- guesses[i]: the i-th guess string, length N.
- counts[i]: c for guess i, i.e. |{ j : guesses[i][j] == secret[j] }|.

**Test oracle (worked example in statement).**
N=5, M=6:
  90342 ;2
  70794 ;0
  39458 ;2
  34109 ;1
  51545 ;2
  12531 ;1
The stated answer is `39542`. brute.py must return this.

**Full-size instance.** N=16, M=22 guesses given in the statement. Find the
unique 16-digit secret.

**Completion criteria.**
1. brute.py (naive enumeration of all 10^N candidates) reproduces 39542 on the
   N=5 example.
2. solution.py reproduces 39542 on the N=5 example (agreement with brute.py).
3. solution.py finds the unique 16-digit secret in reasonable time using a
   structural method (not full enumeration), and that answer is verified by a
   second independent route.
