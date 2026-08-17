"""Independent re-verification of the BvLS(243) C3 triangle-graph spectrum.

Cross-checkes the claim from c3_spectrum_exact_verify.captured.txt (00:50) that
    C3( BvLS(243) ) has spectrum  {-3:648, 3:110, 12:132, 30:1}
by a fully independent route: build the graph, build the triangle graph, and
count integer eigenvalues via numpy eigvalsh (exact integers, since the SRG
spectrum is integral and distinct). Also verifies dimension/degree consistency
and the multiplicity sum = nT.
"""
import numpy as np
from collections import Counter
from lib.srg import bvls_graph
from lib.triangles import triangle_graph

adj = bvls_graph()
n = len(adj)
print(f"BvLS vertices: {n}")

C3, tris = triangle_graph(adj)
C3m = np.array(C3, dtype=int)
nT = C3m.shape[0]
print(f"triangle graph vertices (nT): {nT}")

# degree of each C3 vertex = sum over row
deg = C3m.sum(axis=1)
print(f"C3 degree (all rows equal?): {set(deg.tolist())}")

eigs = np.linalg.eigvalsh(C3m.astype(float))
# eigenvalues are known integral here; round and count
must_be_integer = all(abs(e - round(e)) < 1e-6 for e in eigs)
print("all eigenvalues integral (within 1e-6):", must_be_integer)
cnt = Counter(int(round(e)) for e in eigs)
print("C3 spectrum (eigenval: mult), sorted:")
for k in sorted(cnt):
    print(f"   {k}: {cnt[k]}")
print(f"sum of multiplicities = {sum(cnt.values())}  (should equal nT={nT})")

# closed-form prediction for u=4 (BvLS = srg(243,22,1,2), k=22, v=243, u=4)
u = 4; k = u*u+u+2; v = 1+k*k//2
a = 2*u+1
top = 2*k-(v-1)
m_r = ((v-1)-top//a)//2
m_s = ((v-1)+top//a)//2
rt = k//2+u-3
st = k//2-(u+1)-3
nneg = nT-v
d = 3*(k//2-1)
pred = Counter({d:1, rt:m_r, st:m_s, -3:nneg})
print("predicted C3 spectrum (closed form):")
for kk in sorted(pred): print(f"   {kk}: {pred[kk]}")
print("predicted == actual:", pred == cnt)
