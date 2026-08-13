"""Verify structural claims before the library records them.

Claims checked:
1. The reduction to primes and the even case.
2. Mordell's covering identities (2 mod 3, 3 mod 4, 2 or 3 mod 5, 3/5/6 mod 7,
   5 mod 8) leave only the six classes {1,121,169,289,361,529} mod 840
   previously claimed open -- and that all six are squares mod 840.
3. Proposition 1.6 (Elsholtz-Tao, from Schinzel/Yamamoto): for an odd perfect
   square n, there is NO Type-I and NO Type-II solution to 4/n=1/x+1/y+1/z.
4. The oracle `solves` reproduces the witness set in code/out/witnesses.json.
"""
from fractions import Fraction
import json

def solves(n, x, y, z):
    """Exact rational check 4/n == 1/x+1/y+1/z, all x,y,z positive ints."""
    if not (isinstance(x,int) and isinstance(y,int) and isinstance(z,int)):
        return False
    if x <= 0 or y <= 0 or z <= 0:
        return False
    return Fraction(4,n) == Fraction(1,x) + Fraction(1,y) + Fraction(1,z)

def type_of(n, x, y, z):
    """Return 'I' if n divides exactly one of x,y,z, 'II' if exactly two,
    else None."""
    count = sum(1 for v in (x,y,z) if v % n == 0)
    return {1:'I', 2:'II'}.get(count)

# ---- Claim 4: oracle on witnesses ----
w = json.load(open('code/out/witnesses.json'))
bad = []
nchecked = 0
for res, lst in w['witnesses'].items():
    for entry in lst:
        nchecked += 1
        if not solves(entry['n'], *entry['xyz']):
            bad.append((entry['n'], entry['xyz']))
print(f"Claim4: checked {nchecked} witnesses, solutions correct: {len(bad)==0}")

# ---- Claim 1: even case and prime reduction ----
# Every even n=2m: 4/n = 1/m+1/2m+1/2m
for m in range(1,20):
    n=2*m
    assert solves(n, m, 2*m, 2*m), (n,m)
print("Claim1a: even-n identity  4/(2m)=1/m+1/(2m)+1/(2m) holds for m=1..19")

# ---- Claim 2: which n mod 840 are covered by the five Mordell-ish families ----
# Each identity solves 4/(n) for n in a congruence class. Solve by search: for
# each residue r mod 840 (coprime, since prime n), check whether the standard
# polynomial identities cover r, i.e. whether at least one of:
#   n = 2 mod 3, 3 mod 4, 2or3 mod 5, 3/5/6 mod 7, 5 mod 8
# A residue is UNCOVERED if none of these hold.
covered_cond = lambda r: (r%3==2) or (r%4==3) or (r%5 in (2,3)) or (r%7 in (3,5,6)) or (r%8==5)
uncovered = [r for r in range(840) if covered_cond(r) is False]
uncovered = [r for r in range(840) if r%2==1 and r%5!=0 and r%7!=0 and r%3!=0 and not covered_cond(r)]
print("Claim2: uncovered residues mod 840 (odd, coprime to 3,5,7):")
print(" ", sorted(uncovered))
expected = [1,121,169,289,361,529]
print("  expected open set:", expected)
print("  all six are squares mod 840:",
      all(any(s*s%840==r for s in range(840)) for r in expected))
squares = sorted(set(s*s%840 for s in range(840)))
print("  actually ALL squares mod 840:", squares)
# comment: Mordell identities cover everything except these six among the
# residue classes that matter (odd, coprime to 3,5,7). All six are squares.

# The real statement (Wikipedia): combination covers all n except possibly
# congruent to the six squares mod 840. Note uncovered list from the five
# families alone (allowed to include non-coprime / square cases).
full_uncovered = [r for r in range(840) if not covered_cond(r)]
print("Claim2b: full uncovered set from 5 families (no coprime filter):",
      sorted(full_uncovered))

# ---- Claim 3: vanishing of Type I/II at odd squares ----
# Brute force: for n = odd square <= N, no solution is Type I or Type II.
# We search all x,y,z with 1/x+1/y+1/z = 4/n; bounded by the fact that each
# term >= the 4/n, so denominators <= 4n roughly. Use x<=y<=z WLOG bound:
# z >= n/4*... simplest: x <= 4n, y <= 4n/(4/x - ...). Standard: search
# x in [n/4+1, ...] with 4/n-1/x >0.
import math
def type1_2_at_odd_square(n, limit):
    found = []
    # x,y,z positive, assume x<=y<=z. 1/x>0 requires 4/n-1/x>0 => x>n/4
    for x in range(n//4+1, 4*n+1):
        rem = Fraction(4,n) - Fraction(1,x)
        if rem <= 0: continue
        # now rem = 1/y+1/z, y<=z => 1/y >= rem/2 => y<=2/rem, and 1/y<rem => y>1/rem
        ymax = 2//rem if rem.denominator==1 else int(2/rem)+2
        for y in range(max(x, int(1/rem)+1), ymax+2):
            if y<=0: continue
            zrem = rem - Fraction(1,y)
            if zrem <= 0: continue
            z = zrem.denominator // zrem.numerator
            if zrem.numerator != 1: continue
            if z < y: continue
            if z >= 10**12: continue
            if solves(n,x,y,z):
                found.append((x,y,z,type_of(n,x,y,z)))
    return found

for n in [9,25,49,81,121]:
    sols = type1_2_at_odd_square(n, 4*n)
    # Every solution here is automatically type I or II (prime n), but n not
    # prime. Still, ELT Prop 1.6 says NO type I/II at all. Check none.
    non_neither = [s for s in sols if s[3] in ('I','II')]
    print(f"Claim3: odd square n={n}: solutions found={len(sols)}, "
          f"I/II among them={len(non_neither)}")
