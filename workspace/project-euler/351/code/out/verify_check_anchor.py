#!/usr/bin/env python3
"""Exact arithmetic verification of the PE 351 check anchor and the recalled typo chain.

Verifies, with exact integers only:
  1. H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8) with Phi(10^8)=3039635516365908 (OEIS A064018 a(8)).
  2. H(10^8) = 6*A063985(10^8) with A063985(10^8)=1960364533634092.
  3. The magnitude anchor: Phi(10^8)/10^16 vs 3/pi^2; H(10^8)/10^16 vs 3(1-6/pi^2).
  4. What Phi(10^8) the recalled typo 11762189901804552 would require, and the
     difference from the catalogue value.
"""
import math

N = 10**8
PHI = 3039635516365908          # OEIS A064018 a(8)
A = 1960364533634092            # OEIS A063985(10^8)

tri = N * (N + 1) // 2
H = 6 * (tri - PHI)
H_alt = 6 * A
H_form = 3 * N * N + 3 * N - 6 * PHI

print("check 1: 6*(T(10^8) - Phi(10^8))        =", H)
print("check 2: 3*10^8*(10^8+1) - 6*Phi(10^8)  =", H_form)
print("check 3: 6*A063985(10^8)                 =", H_alt)
print("agreement 1==2==3:", H == H_form == H_alt == 11762187201804552)

print()
print("magnitude: Phi/1e16 = %.8f  (3/pi^2 = %.8f)" % (PHI / 1e16, 3 / math.pi**2))
print("magnitude: H/1e16   = %.8f  (3-18/pi^2 = %.8f)" % (H / 1e16, 3 - 18 / math.pi**2))

print()
typo = 11762189901804552
print("recalled typo H =", typo)
print("typo - correct  =", typo - H)
phi_required = (30000000300000000 - typo) / 6
print("Phi the typo would require =", phi_required)
print("difference from catalogue Phi =", PHI - phi_required)
print("(exact integer check: 6*450000 =", 6 * 450000, ")")

# The stale-typo chain from durable memory: "would require Phi(10^8)=3039635496..."
print()
print("implied Phi(10^8) for typo = 3039635066365908 exactly;",
      "starts 3039635066..., the recalled '3039635496...' is itself imprecise")
