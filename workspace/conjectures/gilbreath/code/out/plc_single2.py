import time
from lib.fcsr import fcsr_lambda_bits
def popcount(j): return bin(j).count("1")
for N in (80,120,160,200,256):
    h=[popcount(j)&1 for j in range(N)]
    t0=time.time()
    lam,_=fcsr_lambda_bits(h)
    dt=time.time()-t0
    print("N=%3d lambda=%d  time=%.3fs bits=%d" % (N,lam,dt,lam.bit_length()))
