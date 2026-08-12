# Goal

Solve Project Euler problem 346: find the sum of all strong repunits below 10^12.

## Completion criteria

- [x] Statement restated and symbols defined (in solution.md).
- [x] Brute program (code/pe346/brute.py) reproduces worked examples:
      8 strong repunits below 50, sum 15864 below 1000.
- [x] Governing theory recorded: strong repunit = repunit of length>=3 in some
      base>1 (plus 1); sorted list = OEIS A053696 with 1 prepended.
- [x] Efficient method O(sqrt(N)*log N) derived and implemented (solution.py).
- [x] Verified by independent route (verify.py) agreeing on all checkpoints and
      on the final value.
- [x] Final answer: sum below 10^12 = **336108797689259276**.
