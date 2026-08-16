import json
import sys
sys.path.insert(0, 'code')
try:
    from lib.supply_fold import s_sos
    from lib.primes import *
except Exception as e:
    print("import err", e)
    raise

data = json.load(open('code/out/nu2_primes_xor_40000.json'))
print("len(data) =", len(data))
print("data[4000] =", data[4000], " data[40000] =", data[40000])
for n in (16385, 16386, 16384, 20000, 31752):
    print(n, "data =", data[n])

# compute nu2(n) directly via canonical oracle: S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}, nu2 = (n-2-S)/2
from lib.primes import first_primes, h_string
def oracle_nu2(n):
    q = first_primes(n+1)
    h = h_string(q)  # h[j] = [r_{j+1} != r_j], length n-1? check
    S = s_sos(n, h)
    nu = (n - 2 - S)//2
    return nu

for n in (53, 64, 4000, 16384, 16385, 16386, 20000, 31752, 40000):
    print("oracle nu2(", n, ") =", oracle_nu2(n), " data =", data[n])