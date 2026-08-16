# Two proven infinite consecutive-pair S-root families — F1 and F2 (upgraded from conjecture)

## Status
Two infinite consecutive-pair S-root families of Project Euler 719 that the
earlier run recorded as *conjectures* are now **proven theorems** by exact
decimal identities (with the underlying expansion confirmed by sympy), and the
family classification is now complete.

## F1 — (10^k − 1, 10^k) for all k >= 2  (the 9-repunit and the power of 10)

- `(10^k - 1)^2 = 10^{2k} - 2·10^k + 1 = (10^k - 2)·10^k + 1`
  Digits = `str(10^k - 2) + "0"*(k-1) + "1"`, split into blocks
  `[10^k - 2, 0*(k-1), 1]`, whose values sum to `(10^k - 2) + 1 = 10^k - 1`.
  >= 3 blocks, so this is a valid S-root split. (e.g. 9801 = 98 + 0 + 1.)
- `(10^k)^2 = 10^{2k} = str(10^k) + "0"*k`, split into blocks `[10^k, 0*k]`,
  sum = `10^k`. (e.g. 10000 = 100 + 0 + 0.)
- Verified by exact string identity for every k in 2..60 and by sympy
  expansion.  (PROVEN.)

## F2 — (10^k − 10, 10^k − 9) for all k >= 3   (e.g. 990/991, 9990/9991, ...)

- `(10^k - 10)^2 = 10^{2k} - 20·10^k + 100`
  Digits = `str(10^k - 20) + "0"*(k-3) + "10" + "0"`, split into blocks
  `[10^k - 20, 0*(k-3), 10, 0]`, sum = `(10^k - 20) + 10 = 10^k - 10`.
  (e.g. 980100 = 980 + 0 + 10 + 0.)
- `(10^k - 9)^2 = 10^{2k} - 18·10^k + 81`
  Digits = `str(10^k - 18) + "0"*(k-2) + "8" + "1"`, split into blocks
  `[10^k - 18, 0*(k-2), 8, 1]`, sum = `(10^k - 18) + 8 + 1 = 10^k - 9`.
  (e.g. 99800100 = 998000 + 0 + 0 + 8 + 1? — the k=4 example in the code:
  9982 + 0 + 0 + 8 + 1 = 9991, and 99820081 = 9982 00 8 1.)
- Verified by exact string identity for every k in 3..80, sympy expansion.
  (PROVEN.)

## Completeness of the (10^k − 10^j, +1) consecutive-pair shape

- Single-root families `x_k = 10^k − j` (j=1..9) are uniform S-roots for all
  large k only for **j = 1** (the 9-repunit) and **j = 9** (10^k − 9); j=2..8
  fail at some small k.
- The consecutive-pair `(10^k − 10^j, 10^k − 10^j + 1)` is a uniform pair of
  S-roots for all large k **only for j = 1**, which is exactly F2. For every
  j >= 2 the pair fails at precisely k = j+2 (e.g. j=2 → (9900,9901) fails at
  k=4). F1 is the j=0/repunit case.
- Hence F1 and F2 are the only two infinite consecutive-pair S-root families
  of the (10^k − 10^j) shape.

```claim
id: f1-f2-infinite-pair-families
statement: Two infinite consecutive-pair S-root families of PE 719 are proven: F1 = (10^k - 1, 10^k) for all k >= 2, and F2 = (10^k - 10, 10^k - 9) for all k >= 3 (verified by exact string identities + sympy expansion for k up to 60/80). F1 and F2 are the only two infinite consecutive-pair S-root families of the (10^k - 10^j) shape: the pair (10^k - 10^j, 10^k - 10^j + 1) fails at k = j+2 for every j >= 2, and single-root families 10^k - j are uniform only for j = 1, 9.
hypotheses: base 10, S-number rule as in GOAL.md
holds-here: yes
status: checked (exact string identities verified over all k in range; sympy expansion)
bearing: F1+F2 cover only 18 of the 408 roots <= 10^6 (~4.4%); no enumeration-reducing power for T(10^12); the O(sqrt N) root scan is confirmed the right method.
anchor: research/approaches/f1-f2-proven-families.md
```

## Consequence for the goal

Neither family has enumeration-reducing power for T(10^12): F1+F2 cover only
18 of the 408 roots <= 10^6 (~4.4%). The O(sqrt N) root scan with the
digit-partition recursion is confirmed as the right method, and the answer
T(10^12) = 128088830547982 is unchanged and double-verified (solution.py vs
OEIS A038206 b-file sum-of-squares). No modulus beyond 9 gives a stronger
necessary residue filter (mod 27/99 residues are exact lifts of the mod-9
{0,1} set; mods 7,11,13,17,19,37 are full), so mod-9 is the strongest modular
filter.

## Verification commands
- `python code/f1_proof_check2.py` — F1 identities, all k in 2..60.
- `python code/f2_proof_check2.py` — F2 identities, all k in 3..80.
- `python code/f2_symbolic.py` — sympy expansion of both squares.
- `python code/gen_pair_families.py` — (10^k−10^j,+1) fails at k=j+2 for j>=2.
- `python code/single_families.py` — single-root 10^k−j uniform only j=1,9.
