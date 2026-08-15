import numpy as np

# Verify the k-critical edge-bound specializations claimed in the four notes.

# Dirac 1957: |E| >= (1/2)((k-1)n + k - 3); k=5 -> 2n+1
for k in (4,5,6):
    coeff = (k-1)/2.0
    print(f"Dirac k={k}: |E| >= {coeff}*n + {(k-3)/2.0}")

# KY 2014: F(k,n) = ((k+1)(k-2)n - k(k-3))/(2(k-1)); k=5 -> (9n-5)/4
for k in (4,5,6):
    num_n = (k+1)*(k-2)
    const = -k*(k-3)
    den = 2*(k-1)
    print(f"KY k={k}: |E| >= ({num_n}n {const:+})/{den} = {num_n/den:.4f}n {const/den:+.4f}")
k=5
print("KY k=5 coefficient edges/vertex =", (k+1)*(k-2)/(2*(k-1)), " -> (9n-5)/4 ?",
      ((6*3*np.arange(1,8,1.0) - 5*2)/8 - (9*np.arange(1,8,1.0)-5)/4) == 0)

# Krivelevich 1997: edge/n ratio = (k-1)/2 + (k-3)/(2(k^2-2k-1))
for k in (4,5,6):
    r = (k-1)/2.0 + (k-3)/(2.0*(k*k-2*k-1))
    print(f"Krivelevich k={k}: edge/n ratio = {r:.5f}  (avg degree {2*r:.5f})")

# Gallai 1963: (k-1)/2 + (k-3)/(2(k^2-3))
for k in (4,5,6):
    r = (k-1)/2.0 + (k-3)/(2.0*(k*k-3))
    print(f"Gallai k={k}: edge/n ratio = {r:.5f}")

# The refutation arithmetic: does KY meet the unit-distance ceiling u_2(n)<=C n^(4/3) force a contradiction?
print("\n--- size-bound clash, C=1 ---")
for n in range(6, 14):
    need = (9*n-5)/4.0          # KY lower bound on edges of a 5-critical graph on n vertices
    cap = n**(4.0/3.0)          # SST ceiling at C=1
    verdict = "CONTRADICTION" if need > cap else "ok"
    print(f"n={n:2d}: need>={need:7.3f}  cap<={cap:7.3f}  {verdict}")
