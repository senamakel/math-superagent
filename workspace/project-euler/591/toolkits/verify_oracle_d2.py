"""Cross-check the PE591 d=2 n=1e13 oracle with exact/mpmath arithmetic.

Oracle: I_2(BQA_2(pi,1e13)) = -6188084046055, i.e. a=-6188084046055 with b=4375636191520.
Check: is a+b*sqrt(2) close to pi? And is |a| == round(b*sqrt(2)) (about 3.14) or what?
Also verify |a| = round(b*sqrt(2) - pi ... ) relations exactly.
"""
import mpmath as mp
mp.mp.dps = 60
pi = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923')
b = 4375636191520
a = -6188084046055
val = a + b*mp.sqrt(2)
print("a + b*sqrt2 - pi =", mp.nstr(val - pi, 40))
print("b*sqrt2          =", mp.nstr(b*mp.sqrt(2), 40))
print("|a|              =", -a)
print("round(b*sqrt2)   =", mp.nint(b*mp.sqrt(2)))
print("a vs round(pi - b*sqrt2) =", a, "expected", mp.nint(pi - b*mp.sqrt(2)))
print("dist to nearest int of b*sqrt2-pi:", mp.nstr(mp.fabs((b*mp.sqrt(2)-pi) - mp.nint(b*mp.sqrt(2)-pi)), 30))
# check that b is a convergent denominator of some irrational: semiconvergent of sqrt(2)? sqrt2 CF [1;2]
# sqrt(2) convergent denominators: 1,3,7,17,41,99,239,577,1393,3363,8119,19601,47321,114243,275807,665857,1607521,3880899,9369319,22619537,54608393,131836323,318281039,768398401,1855077841,4478554083,10812186007,26102926097
from fractions import Fraction
def cf_denoms_sqrt2(N):
    qm2,qm1 = 0,1
    out=[]
    for _ in range(100):
        q = 2*qm1 + qm2
        if q > N: break
        out.append(q)
        qm2,qm1 = qm1,q
    return out
print("sqrt2 convergent denominators up to 5e12:", cf_denoms_sqrt2(5*10**12))
print("b in sqrt2 conv denoms:", b in cf_denoms_sqrt2(5*10**12))
# semiconvergent denoms of sqrt2
denoms=set(cf_denoms_sqrt2(5*10**12))
print("b a semiconvergent (q_k + m q_{k-1})?", any(b == d + m*e for d in denoms for m in range(3) for e in denoms))