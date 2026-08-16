"""Direct verification that the two n=3 residues are/are not genuine integer solutions.
Ground-truth check: for the asserted M2 solution 3^4=2^0+2^4+2^6, verify exactly.
Also verify papers' determinate characterization: 2^i determinate mod M iff v2(M) > i
for the tail length, and loop length = ord of 2 mod the odd part.
"""
def v2(n):
    c=0
    while n%2==0: n//=2; c+=1
    return c

M1=5440; M2=2**7*5*17*257
print("v2(M1)=",v2(M1), " v2(M2)=",v2(M2))
# exact check of the n=3 solution
print("3^4 =",3**4)
print("2^0+2^4+2^6 =",2**0+2**4+2**6)
print("equal in Z:",3**4 == 1+16+64," ; mod M2:", (3**4 % M2)==((1+16+64)%M2))

# Lemma 3.1 hypothesis test for the two moduli, using clean residue math
# Notation 2.3: O'2(M) = ord of 2 mod M' (odd part coprime to 6, i.e. /3^v), 
# O'3(M) = ord of 3 mod M' (part coprime to 6, i.e. /2^u).
# For M1=2^6*5*17: M'=5*17. For M2=2^7*5*17*257: M'=5*17*257.
import math
def ord_mod(a,n):
    if math.gcd(a,n)!=1: return None
    k=1; r=a%n
    while r!=1: r=(r*a)%n; k+=1
    return k
def odd_part_coprime6(M):
    while M%2==0: M//=2
    while M%3==0: M//=3
    return M
for M in [M1,M2]:
    Mp=odd_part_coprime6(M)
    o2=ord_mod(2,Mp); o3=ord_mod(3,Mp)
    print(f"M={M}, M'={Mp}: O'2={o2}, O'3={o3};  "
          f"O'3 divisible by 2^5? {o3 is not None and o3%(2**5)==0}; "
          f"O'2 divisible by 3^4={3**4}? {o2 is not None and o2%(3**4)==0}")
