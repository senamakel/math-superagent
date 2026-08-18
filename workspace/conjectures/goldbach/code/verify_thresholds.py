#!/usr/bin/env python3
"""Verify decimal conversions of exp(exp(...)) Chen thresholds cited in ROOT.md.

ROOT.md claims:
  exp(exp 36)   ~= 10^(4.7e14)   (Yamada 2015)
  exp(exp 32.7) ~= 10^(7.7e13)   (Bordignon-Johnston-Starichkova)

Check: log10(exp(exp c)) = exp(c) / ln(10).
"""
import math

def conv(c):
    e_c = math.exp(c)
    log10 = e_c / math.log(10.0)
    return e_c, log10

for c, claimed in [(36.0, 4.7e14), (32.7, 7.7e13), (34.6, None)]:
    e_c, log10 = conv(c)
    print(f"exp(exp {c})  ->  e^{e_c:.4e}  =  10^({log10:.4e})"
          + (f"   [ROOT claims 10^({claimed:.2e})]" if claimed else ""))

# sanity: what c would give the claimed decimal exponents?
for claimed in [4.7e14, 7.7e13]:
    # log10(exp(exp c)) = claimed  =>  exp(c) = claimed * ln 10  =>  c = ln(claimed * ln 10)
    c = math.log(claimed * math.log(10.0))
    print(f"claimed 10^({claimed:.1e}) would come from exp(exp {c:.2f})")

# Yamada's constant 0.007 check: 0.007 * UN * N / log^2 N
# BJS Corollary 4: N > exp(exp 32.7), square-free P2
# BJS Theorem 5: all even N >= 4, sum of prime + product of at most e^29.3 primes
print(f"e^29.3 = {math.exp(29.3):.4e}")

# minimal Goldbach partition records from OeS page
# 3325581707333960528 = 9781 + P19 ; 2795935116574469638 = 9629 + P19
print("S(9781) = 3325581707333960528 = 9781 + P19 (largest least-prime record <= 4e18)")
