"""Verify the arithmetic claims in Spencer's carry-packet obstruction (Zenodo 20355936).

Checks each arithmetic fact the paper states, plus that n=0,2,8 all remain digit-2-free
consistently (the falsification oracle is satisfied — failure is a missing induction, not
a wrong witness). Oracle: digit_free(m) exactly.
"""
from code.erdos.oracle import digit_free

def tern(n):
    if n == 0:
        return "0"
    d = []
    while n:
        d.append(str(n % 3))
        n //= 3
    return "".join(reversed(d))

def check(label, got):
    print(f"{label}: {got}")

# length-3 local carry law (Lemma 6.1): 4*[u]_3 must be digit-{0,1}-clean
from itertools import product
clean3 = []
for tup in product([0,1,2], repeat=3):
    u = tup
    val = u[0]*9 + u[1]*3 + u[2]
    q = 4*val
    if digit_free(q):
        clean3.append("".join(map(str,u)))
expected3 = ["000","001","010","021","100","101","210"]
print("Lemma 6.1 clean 3-digit words:", sorted(clean3))
print("matches paper list:", sorted(clean3)==sorted(expected3))

# key arithmetic
print("2101_3 =", 2*27+1*9+0*3+1, "= 64  -> 4*64 =", 4*64, "tern", tern(4*64))
print("100111_3 =", 256, "; 100111_3*4 =", 256*4, "tern", tern(256*4))
print("101_3 = 10 = 2*5 -> 4*10 =", 40, "tern", tern(40))
print("21_3 = 7 -> 4*7 =", 28, "tern", tern(28))
print("10101_3 =", 1+9+81, "-> 4x =", 4*(1+9+81), "tern", tern(4*(1+9+81)))

# 64(1+3^s) dyadically pure only at s=1?
import math
def core(n):
    n2, n3 = n, n
    v2 = (n & -n).bit_length()-1
    while n3 % 3 == 0:
        n3 //= 3
    return n // (2**v2) // (1 if False else 3**0)  # fix below

def core23(n):
    v2 = 0; t=n
    while t%2==0: t//=2; v2+=1
    v3 = 0; t=n
    while t%3==0: t//=3; v3+=1
    return n // (2**v2 * 3**v3)

for s in range(1, 12):
    print(f"1+3^{s} = {1+3**s}, core23 = {core23(1+3**s)}, is_pow2 = {((1+3**s)&((1+3**s)-1))==0}")

# witnesses
print("\nWitnesses (falsification oracle):")
for n in [0,2,8]:
    v = 2**n
    print(f"  digit_free(2^{n}={v}) = {digit_free(v)}, ternary {tern(v)}")

# check that 4^n in A holds iff at each quadrupling the next-power check is clean
print("\n4^e in A for e=0..8:")
for e in range(9):
    print(f"  4^{e} = {4**e} = {tern(4**e)}  inA={digit_free(4**e)}")
