#!/usr/bin/env python3
"""Test the surviving c=1 pairwise-distinct conjecture away from real data.

PE185 instances look like: a random secret s (len L), R random guesses, each
guess's c_i = its ACTUAL number of matches against s.  Question: among guesses
with c_i == 1, are their single match positions pairwise distinct?
For a random guess, P(match at a given position) = 1/10.  Built by definition
this is NOT forced.  We measure how often the real data's coincidental-looking
property (all 6 distinct) arises by chance in this generation model.
"""
import random
random.seed(12345)

def trial(L, R, secret):
    guesses = ["".join(random.choice("0123456789") for _ in range(L))
               for _ in range(R)]
    # count matches for each guess
    matchpos = []
    for g in guesses:
        pos = [p for p in range(L) if g[p] == secret[p]]
        matchpos.append(pos)
    # among guesses with exactly 1 match, positions
    ones = [pos[0] for pos in matchpos if len(pos) == 1]
    distinct = len(ones) == len(set(ones))
    return len(ones), distinct

L, R = 16, 22
# Expected ~2^16... no: matches per random guess ~ Binomial(L, 1/10); P(1 match)
# = L*(1/10)*(0.9)^(L-1) = 16*0.1*0.9^15 = 1.6*0.2059 = 0.329. So ~7 guesses
# per 22 have c=1 on average.
random_secret = "".join(random.choice("0123456789") for _ in range(L))

N = 200000
both_have2 = 0   # distinct(real-ish many ones) with >=6 ones
ones_ge6_distinct = 0
ones_exactly6_all_distinct = 0
for _ in range(N):
    k, distinct = trial(L, R, random_secret)
    if k >= 6 and distinct:
        ones_ge6_distinct += 1
    if k == 6 and distinct:
        ones_exactly6_all_distinct += 1
print("trials:", N)
print("frac with >=6 c=1 guesses all pairwise-distinct:",
      ones_ge6_distinct / N)
print("frac with exactly-6 c=1 guesses all pairwise-distinct:",
      ones_exactly6_all_distinct / N)
