"""Print longer record-b sequences for d in {2,5,7} up to N=10^7, exact distance via mpmath."""
import mpmath as mp
mp.mp.dps = 50
pi = mp.mpf('3.14159265358979323846264338327950288419716939937510')
for d in [2,5,7]:
    sd = mp.sqrt(d)
    alpha = sd - mp.floor(sd)
    beta = pi - 3
    best = mp.mpf(10)
    recs = []
    N = 10_000_000
    for b in range(0, N+1):
        v = b*alpha - beta
        fr = v - mp.floor(v)
        err = min(fr, 1-fr)
        if err < best - mp.mpf('1e-45'):
            best = err
            recs.append(b)
    print(f"d={d}: {recs}")