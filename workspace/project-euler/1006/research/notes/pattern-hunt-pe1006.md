# PE1006 pattern-hunt findings (provisional, not yet proof)

Status: computed this run; survives an attack. Not yet asserted as proven.

## 1. Lmin(k): minimal prefix length containing all k+1 length-k factors

For the infinite Fibonacci word (S_0 = 0, S_1 = 01, S_n = S_{n-1}S_{n-2}).

CONJECTURE (verified exactly k = 1..2583, 0 mismatches, all Fibonacci
boundary checks k = F_m-1, F_m, F_m+1 pass, agrees with OEIS A344953 note
terms positions 1..61):

    Lmin(k) = k + NextFib(k) - 1,
    NextFib(k) = the least Fibonacci number (1, 2, 3, 5, 8, ...) strictly > k.
    Equivalently for F_m <= k < F_{m+1}:  Lmin(k) = k + F_{m+1} - 1.

REFUTED naive guess: Lmin(k) = floor(k phi^2). Fails at k = 2 (Lmin = 4,
floor = 5); 992 failures in k <= 1000.

Values: Lmin(1)=2, ..., Lmin(33)=66, Lmin(34)=88, Lmin(54)=108, Lmin(55)=143,
Lmin(88)=176, Lmin(89)=232, Lmin(143)=286, Lmin(144)=376, Lmin(232)=464,
Lmin(233)=609, Lmin(376)=752, Lmin(377)=986, Lmin(610)=1596, Lmin(987)=2583,
Lmin(1597)=4180, Lmin(2583)=5166.

Consequence for validation: a brute oracle using word length >= 3k is always
safe (3k >= k + NextFib(k) for every k), and the earlier observation that
2k is not always enough (k=15 needs 35 = k + 21 - 1) is exactly the block
formula k + NextFib(k) - 1 with NextFib(15) = 21.

## 2. Exact Psi(k), residues, OEIS

- gen_sequences.py computed exact Psi(1..25) (matching brute.py), residues
  Psi(k) mod 101001001 for k = 1..400, Lmin via a *different* implementation.
  All count checks (k+1 factors), stability probes (74, 0 failures) pass.
  Psi(10) mod M = 10699667 reproduces the problem-statement oracle.
- OEIS: exact Psi(1..10) NOT found; residues Psi(1..5) mod M NOT found.
  No catalogued closed form; structure must come from the problem itself.
- Residue sequence: no constant-coefficient linear recurrence of order <= 12,
  no low-degree polynomial fit over the first 60 terms (exact tool verdicts).
  Looks noise-like; expect regularity only before reduction mod M.

## 3. Why Lmin matters

The brute oracle's "how long a prefix is enough" question is answered in
closed form by Lmin(k) = k + NextFib(k) - 1. At a Fibonacci boundary
k = F_m - 1 the required prefix is exactly 2k; mid-block it grows to ~phi^2 k.
This bound is load-bearing for extending the brute oracle to larger k, and
confirms the mechanical-word construction (directive 2) only needs
F(n) > k to place all k+1 factors.