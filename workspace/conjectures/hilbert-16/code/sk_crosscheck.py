from fractions import Fraction

def S(k):
    # transcribed S_k = 4^{k-1}(k - 13/6) + (2k-1)/3
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

def claim03(k):
    # [3]'s claimed H(2k-1) = 4(2^k - 2)(2^{k+1} - 5)  [superscripts restored]
    return 4*(2**k - 2)*(2**(k+1) - 5)

print("k   S_k (order)      [3] formula       S_k > [3]?")
cross = None
for k in range(1, 60):
    sk = S(k); c3 = claim03(k)
    gt = sk > c3
    if gt and cross is None:
        cross = k
    if k < 12 or (k>=30 and k<=40):
        print(f"{k:2d}  {float(sk):.3e}  {float(c3):.3e}  {gt}")
print("first k with S_k > [3]-formula:", cross)
print("paper states the contradiction holds for k >= 35")
