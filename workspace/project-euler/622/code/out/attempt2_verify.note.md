# PE622 attempt2 verification — captured output

Program: `code/pe622/attempt2_verify.py` (self-contained, no imports beyond math.gcd).

Result: reproduced every worked example by **direct out-faro simulation**, confirmed
the `s(n) = ord_{n-1}(2)` reduction on all even decks 2..80, and computed the
answer by exact divisor enumeration of `2^60 - 1`.

```text
PART A: direct simulation — reproduce every stated worked example
s(52) [direct simulation] = 8
s(86) [direct simulation] = 8
even n with s(n)=8 [direct simulation] = [18, 52, 86, 256]
sum of even n with s(n)=8 [direct simulation] = 412
Worked examples reproduced by DIRECT SIMULATION: 8, 8, 412.

PART B: cross-check s(n) == ord_{n-1}(2) on even decks 2..80
All even n in 2..80 match: brute-force out-shuffle order == ord_{n-1}(2).

PART C: answer — enumerate divisors of 2^60 - 1 with ord_m(2)=60
N = 2^60 - 1 = 1152921504606846975
factorisation of N: {3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1, 41: 1, 61: 1, 151: 1, 331: 1, 1321: 1}
prime divisors of 60: [2, 3, 5]
total divisors of N: 4608
count C of m with ord_m(2)=60: 4456
sum S of those m: 3010983666182119516
ANSWER = S + C = 3010983666182123972
independent direct-ord route: C = 4456  S = 3010983666182119516
Two independent routes agree exactly.
FINAL ANSWER = 3010983666182123972
```

```claim
id: pe622-answer-order-sixty-directsim
statement: The sum of all positive even n with s(n) = 60 (Project Euler 622)
  is 3010983666182123972, where s(n) is the number of consecutive perfect
  out-shuffles needed to restore a deck of size n. Derived here by direct
  out-faro simulation (reproducing s(52)=8, s(86)=8, and the sum 412 over
  {18,52,86,256}) and by two independent exact divisor-enumeration routes
  over the 4608 divisors of 2^60-1, which agree.
hypotheses: n even, n >= 2.
holds-here: yes.
status: checked
basis: two independent exact routes (structural 60/prime-divisor test over the
divisors of 2^60-1, and direct multiplicative-order iteration over the same
divisor set) both give C=4456, S=3010983666182119516, ANSWER=3010983666182123972.
The reduction s(n)=ord_{n-1}(2) is confirmed on every even deck 2..80 and the
three stated worked examples (8, 8, 412) are reproduced by direct simulation.
```

The number **3010983666182123972** matches the run's existing answer in GOAL.md
and the independent `iex_gcd_check.py` / `inclusion_exclusion.py` routes, and was
derived here without consulting any published PE622 answer.
