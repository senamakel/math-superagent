#!/usr/bin/env python3
"""Independent numeric confirmation of V_hexagon = 2 + 2*sqrt(21)/3.
route A: stewbasic n=6 formula (mpmath)
route B: closed-form surd 2 + 2*sqrt(21)/3
Both at 50 dps; diff checked to < 1e-40; explicit 8-dp string match."""
import mpmath as mp
mp.mp.dps = 50

theta = mp.pi/6
K, n = 2, 6
inner = 2*mp.sin(K*theta)/((K+n)*mp.tan(theta)) - mp.cos(K*theta)
alpha = mp.mpf(1)/2*(K*theta + mp.acos(inner))
VA = 1/mp.cos(alpha)

VB = mp.mpf(2) + 2*mp.sqrt(21)/3

print("route A (stewbasic, mpmath):", mp.nstr(VA, 30))
print("route B (2 + 2sqrt21/3)    :", mp.nstr(VB, 30))
print("abs diff                   :", mp.nstr(abs(VA-VB), 12))
print("diff < 1e-40 ?             :", bool(abs(VA-VB) < mp.mpf('1e-40')))

sA = mp.nstr(VA, 9)   # 9 significant digits -> 8 dp since value ~5.055
ans = "5.05505046"
print("route A rounded 8 dp       :", sA)
print("matches run answer 5.05505046 ? :", sA == ans)

# closed form squared check: (2+2s/3)^2 = 40/3+8s/3
s = mp.sqrt(21)
print("hand: (2+2s/3)^2 =", mp.nstr((VB)**2, 20), " expected 40/3+8s/3 =", mp.nstr(mp.mpf(40)/3+8*s/3, 20))
