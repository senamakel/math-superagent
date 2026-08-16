"""Compare my direct oracle with the library s_sos on the prime h, per guard."""
import sympy
from lib.supply_fold import s_sos, s_direct, h_from_r

ps = list(sympy.primerange(1, 10**9))
N = 4000
q = ps[:N+1]
r = [x % 4 for x in q]
h = h_from_r(r)
print("h[:20] =", h[:20])

import sys
sys.path.insert(0, 'code')
from pattern_finder.oracle_exact import nu2 as my_nu2, T as my_T

for n in [53, 64, 100, 1000, 4000]:
    Ss, ones_s = s_sos(n, h)
    Sd, ones_d = s_direct(n, h)
    my = my_nu2(n, h)
    print(f"n={n}: s_sos ones={ones_s}  s_direct={ones_d}  my_direct={my}")

# my h differs? compare my h vs library h
print("my h vs lib h equal:", all((((q[j+1]-q[j])//2)%2)==h[j] for j in range(20)))
