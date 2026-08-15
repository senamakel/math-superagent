import json
# Verify the full supply composition: ballot e(n)>=0  => w(n) >= (n-2)/2
# (this is exactly leg(b)); combined with nu2>=w/2 gives nu2 >= (n-2)/4 > n^0.525.
# Check against dense nu2 file.
nu2 = {}
for line in open("/workspace/code/out/nu2_dense.txt"):
    parts = line.split()
    if len(parts) == 2:
        nu2[int(parts[0])] = int(parts[1])

# (n-2)/4 > n^0.525 crossing
import math
def n0525(n): return n**0.525
cross = None
for n in range(10, 500):
    if (n-2)/4 > n0525(n):
        cross = n; break
print("first n with (n-2)/4 > n^0.525:", cross)

# verify nu2(n) >= (n-2)/4 on the dense range if ballot held (i.e. nu2>=w/2 and w>=n/2)
# check nu2 >= (n-2)/4 directly on the dense file
viol = [n for n in range(17, 30001) if n in nu2 and nu2[n] < (n-2)/4]
print("nu2(n) >= (n-2)/4 violations over dense n in [17,30000]:", len(viol), "first:", viol[:5])

# min margin ratio
mr = min((nu2[n]/( (n-2)/4 ) for n in range(17,30001) if n in nu2), default=None)
min_n = min((n for n in range(17,30001) if n in nu2 and nu2[n]/( (n-2)/4 )==mr), default=None)
print("min 4*nu2/(n-2) =", mr, "at n=", min_n)
