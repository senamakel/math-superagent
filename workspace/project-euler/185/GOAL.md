# Goal

## Problem (Project Euler 185 — Number Mind)

We are given `N` guesses `g_1, ..., g_N`, each a digit-string of length `L`, and
for each guess a required count `c_i` (a non-negative integer). A *match* at
position `j` for guess `i` means `s[j] == g_i[j]`, where `s` is the (unknown)
secret digit-string of length `L`. The secret must satisfy, for every `i`:

    #{ j in 0..L-1 : s[j] == g_i[j] } == c_i

i.e. for each guess the number of correctly placed digits equals exactly `c_i`
(digits that match in value but are in the wrong position do NOT count).

The statement asserts the secret is unique in each given instance.

## Worked example (the test oracle)

Length `L = 5`, guesses and required counts:

| guess  | c_i |
|--------|-----|
| 90342  |  2  |
| 70794  |  0  |
| 39458  |  2  |
| 34109  |  1  |
| 51545  |  2  |
| 12531  |  1  |

Claimed secret: **39542**. Quick manual check of guess `90342` against `39542`:
positions 4 and 5 (`4`,`2`) match → 2 correct. ✓

Completeness check against this example: the secret `39542` must be the UNIQUE
string of length 5 satisfying all six counts (verified by brute force over all
10^5 = 100000 candidate strings).

## Main task

`L = 16`, `N = 22` guesses given below (guess ; c_i). Find the unique 16-digit
secret sequence.

5616185650518293 ;2
3847439647293047 ;1
5855462940810587 ;3
9742855507068353 ;3
4296849643607543 ;3
3174248439465858 ;1
4513559094146117 ;2
7890971548908067 ;3
8157356344118483 ;1
2615250744386899 ;2
8690095851526254 ;3
6375711915077050 ;1
6913859173121360 ;1
6442889055042768 ;2
2321386104303845 ;0
2326509471271448 ;2
5251583379644322 ;2
1748270476758276 ;3
4895722652190306 ;1
3041631117224635 ;3
1841236454324589 ;3
2659862637316867 ;2

## Completion criteria

1. A brute-force program `/workspace/brute.py` that reproduces the `L=5`
   example: it finds `39542` and confirms it is the unique answer among all
   `10^5` strings.
2. An efficient solver `/workspace/solution.py` (recursive constraint search
   with pruning) that agrees with brute.py on `L=5` and produces the `L=16`
   secret.
3. A second, independent route (`/workspace/solution2.py` via scipy MILP) that
   reproduces the `L=5` answer and yields the SAME `L=16` secret.
4. Final answer reported with the verification commands and their output.
