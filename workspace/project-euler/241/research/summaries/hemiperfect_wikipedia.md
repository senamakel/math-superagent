# Hemiperfect numbers — definition and the abundance-value bound (Wikipedia)

Source: https://en.wikipedia.org/wiki/Hemiperfect_number — `[[hemiperfect_wikipedia.full]]`

## What it establishes

- **Definition.** n is **hemiperfect** when σ(n)/n = k/2 for an **odd** integer k. This is exactly the PE 241 condition p(n) = k + 1/2 (put 2k+1 for k). PE 241 asks the sum of all hemiperfect n ≤ 10^18.
- **Worked example.** 24: σ(24) = 1+2+3+4+6+8+12+24 = 60 = (5/2)·24, so abundancy 5/2, matching brute.py.
- **First terms** (A159907): 2, 24, 4320, 4680, 26208, 8910720, 17428320, 20427264, 91963648, 197064960, ...
  These reproduce brute.py's oracle set {2,24,4320,4680,26208} (checked by the run).
- **Smallest number of abundancy k/2** (A088912), k odd: k=3→2; k=5→24; k=7→4320; k=9→8 910 720; k=11→17 116 004 505 600 (~1.7e13); k=13→170 974 031 122 008 628 ... (~1.7e44, 45 digits). No number of abundancy 19/2 is known; best bounds for 15/2, 17/2 by M. Marcus.

## What it lets this run do

Because the smallest hemiperfect of abundancy 13/2 is already ~1.7e44 > 10^18, **no n ≤ 10^18 can have abundancy ≥ 13/2**. So for the given bound only abundancies 3/2, 5/2, 7/2, 9/2, 11/2 (k_odd = 3,5,7,9,11, i.e. PE k = 1..5) are reachable. That cuts the DFS governing-objective 2σ(n)=(2k+1)n to five k values. (FH: the k=13 threshold uses the concrete a(6) value, not RH.)

## Does not settle

Does not list ALL hemiperfect n ≤ 10^18 nor their sum (that is the computation). No statement on finitely many vs. infinitely many hemiperfects.

```claim
id: hemi-abundance-bound
statement: No positive integer n <= 10^18 has half-integer abundancy k/2 with k >= 13, because the smallest such number a(6) ~ 1.7e44 exceeds 10^18; hence only abundancies 3/2..11/2 are reachable.
hypotheses: a(6) is the true smallest number of abundancy 13/2 (given by A088912 as an explicit 45-digit integer, and independently bounded by Robin's theorem > 5e16)
holds-here: yes
status: sourced (explicit value in A088912) and consistent with Robin lower bound
bearing: bounds the DFS over 2*sigma(n)=(2k+1)n to k=1..5 for the n<=10^18 bound
anchor: research/sources/hemiperfect_wikipedia.full.md
answers: theory-numbers-with-88d5
```
