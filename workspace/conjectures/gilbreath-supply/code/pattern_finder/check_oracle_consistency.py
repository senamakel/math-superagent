import json, sys
sys.path.insert(0, 'code')
from lib.primes import h_string
from lib.supply_fold import s_sos
data = json.load(open('code/out/nu2_primes_xor_40000.json'))

def oracle_nu2(n):
    h = h_string(n)          # length n-1, indices j=0..n-2
    S = s_sos(n, h)
    return (n - 2 - S)//2, S

for n in (53, 64, 4000, 16384, 16385, 16386, 32769, 40000):
    nu, S = oracle_nu2(n)
    print(f"n={n}: oracle nu2={nu}  data={data[n]}  match={nu==data[n]}  S={S}  (n-2)={n-2}")

# check data[32769]
print("data[32769] =", data[32769])