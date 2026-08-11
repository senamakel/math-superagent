import math

pi = math.pi

# Verify |I_d| = round(sqrt(d)*b_d) for my computed data (n=10^4)
print("Check |I_d| == round(sqrt(d)*b):")
data = {
2:(1981,1403),3:(16822,9714),5:(576,259),6:(9398,3838),7:(18279,6910),
8:(13463,4761),10:(26073,8246),11:(15187,4580),12:(16822,4857),13:(25809,7159),
14:(6773,1811),15:(11488,2967),17:(40226,9757),18:(13463,3174),19:(703,162),
20:(40179,8985),21:(5693,1243),22:(25963,5536),23:(11339,2365),24:(9398,1919),
92:(64,7),83:(1081,119),57:(4942,655),61:(8182,1048),37:(5593,920),
}
allok=True
for d,(a,b) in data.items():
    r = round(math.sqrt(d)*b)
    ok = (abs(a)==r)
    if not ok: allok=False
    print(f"  d={d:3d} |I|={abs(a):6d}  b={b:5d}  sqrt(d)*b round={r:6d}  match={ok}")
print("ALL MATCH:", allok)

# Verify problem's d=2 big oracle: I=-6188084046055, b=4375636191520
b=4375636191520; a=-6188084046055
sd2=math.sqrt(2)
print("\nBig oracle d=2: round(sqrt2*b) =", round(sd2*b), " vs |I| =", abs(a))
print("b*sqrt2 =", b*sd2, " a+b*sqrt2-pi =", a+b*sd2-pi)

# Check the exact value claim: compute b*sqrt2 precisely
from decimal import Decimal, getcontext
getcontext().prec=40
bsq = Decimal(b)*Decimal(2).sqrt()
print("b*sqrt2 (dec) =", bsq)
print("difference from -a+... :", bsq - Decimal(abs(a)))
