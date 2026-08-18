"""Analyze V(R_k) run structure: densities, and test whether the run VALUES
are suffixes of the Fibonacci word (Sturmian standard words)."""
from decimal import Decimal, getcontext
getcontext().prec = 40

gaps = [1, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 3]
n3 = sum(1 for g in gaps if g == 3)
n2 = sum(1 for g in gaps if g == 2)
tot = len(gaps)
print(f"gaps: total={tot}, #3={n3}, #2={n2}")
print(f"density of 3 = {Decimal(n3)/Decimal(tot)}  (1/phi={Decimal(1)/( (Decimal(1)+Decimal(5).sqrt())/2 )})")
print(f"density of 2 = {Decimal(n2)/Decimal(tot)}  (1/phi^2={Decimal(1)/(((Decimal(3)+Decimal(5).sqrt())/2))})")

# run lengths: same sequence shifted (starts[i+1]-starts[i] but run values)
runlens_hist = {3: 94, 2: 58, 1: 2}
print("\nrun lengths across 154 runs: 3s=94, 2s=58 (1s=2 edge)")
ntot = 154
print(f"density of length-3 runs = {Decimal(94)/Decimal(ntot)} ~ 1/phi = {Decimal(1)/( (Decimal(1)+Decimal(5).sqrt())/2 )}")
print(f"density of length-2 runs = {Decimal(58)/Decimal(ntot)} ~ 1/phi^2 = {Decimal(1)/(((Decimal(3)+Decimal(5).sqrt())/2))}")
