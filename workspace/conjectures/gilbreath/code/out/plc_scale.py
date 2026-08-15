import time
from lib.fcsr import fcsr_lambda_bits, fcsr_lambda_prefix
def popcount(j): return bin(j).count("1")
h=[popcount(j)&1 for j in range(3000)]
for maxN in (64,128,256,512):
    t0=time.time()
    lam=fcsr_lambda_prefix(h[:maxN])
    dt=time.time()-t0
    print("maxN=%4d lam_prefix time=%.2fs last lambda=%d" % (maxN,dt,lam[-1]))
