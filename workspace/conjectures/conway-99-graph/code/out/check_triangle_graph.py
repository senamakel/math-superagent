"""Verify the triangle-graph thread's structural claim on both control graphs.

Thread triangle-graph next-step: build C3(Gamma) for rook(3)=srg(9,4,1,2) and
BvLS=srg(243,22,1,2) through code/lib, confirm the degree prediction d=3(k/2-1),
confirm the NOT-strongly-regular structural claim (shared by 99 and 243, so a
constraint not a rule-out), and compare the computed spectrum (numerical) with
the Phillips eq 4.3 prediction.

Exact conclusions (integer arithmetic):
  - number of triangles = nk/6  (rook 6, bvls 891)
  - C3 degree = d on every vertex (rook 3 -> K_{3,3} = srg(6,3,0,3); bvls 30)
  - C3 is / is not strongly regular, decided exactly by common-neighbour counts
  - trace and trace-of-square of the C3 adjacency match the predicted spectrum

Numerical conclusion (numpy float spectrum, labelled as such):
  - eigenvalue multiplicities of C3(BvLS) match {30:1, 12:132, 3:110, -3:648}
"""
import numpy as np
from lib.srg import rook, bvls_graph, is_srg
from lib.triangles import triangle_graph, c3_spectrum_prediction

# ---- rook(3) : C3 should be K_{3,3} = srg(6,3,0,3) ----
R = rook(3)
C3r, tris_r = triangle_graph(R)
print("=== srg(9,4,1,2) rook(3) ===")
print("triangles:", len(tris_r), "(expect nk/6 =", 9*4//6, ")")
deg = C3r.sum(axis=1)
print("C3 degree (all):", set(deg.tolist()), "(expect {3})")
print("edges:", int(C3r.sum()//2), "(expect 6*3/2 = 9 = K_3,3)")
print("C3 is srg(6,3,0,3):", is_srg(C3r, 6, 3, 0, 3))
# (The eq-4.3 prediction needs nT >= v; for rook nT-v = 6-9 < 0, because rook's
#  C3 IS strongly regular and is the degenerate Thm-4.5 case. Prediction only
#  below for BvLS.)

# ---- BvLS : C3 should be 30-regular, NOT strongly regular ----
B = bvls_graph()
C3b, tris_b = triangle_graph(B)
print()
print("=== srg(243,22,1,2) BvLS ===")
print("triangles:", len(tris_b), "(expect nk/6 =", 243*22//6, ")")
deg = C3b.sum(axis=1)
print("C3 degree all-equal:", bool(np.all(deg == deg[0])), "value", int(deg[0]),
      "(expect 30 = 3(11-1))")
print("edges:", int(C3b.sum()//2), "(expect", 891*30//2, ")")

# exact strong-regularity decision
srg_ok, srg_detail = is_srg(C3b, 891, 30, 0, 0)  # lam,mu unknown -> not srg unless stated
# C3 cannot be srg(891,30,lambda,mu) for any lambda,mu if common-neighbour counts non-constant:
A2 = C3b @ C3b
I = np.eye(891, dtype=np.int64)
off = ~I.astype(bool)
adj = C3b.astype(bool)
adjcnt = A2[adj & off]
nadjcnt = A2[(~adj) & off]
adj_same = len(set(adjcnt.tolist()))
nadj_same = len(set(nadjcnt.tolist()))
print("adjacent common-neighbour distinct values:", adj_same,
      "(>1 => NOT strongly regular)")
print("non-adjacent common-neighbour distinct values:", nadj_same,
      "(>1 => NOT strongly regular)")

# trace / sum-of-squares invariants vs prediction
pred_spec, d, nT = c3_spectrum_prediction(243, 22, 4, -5, 132, 110)  # r=4(s mult132),s=-5(mult110)
tracesum = sum(e*m for e, m in pred_spec)
sqsum = sum(e*e*m for e, m in pred_spec)
print("predicted nT", nT, "d", d, "trace-sum", tracesum, "sq-sum", sqsum)
print("computed trace:", int(np.trace(C3b)), " Fprediction", tracesum)
print("computed sum-sq (2*edges):", int((C3b@C3b).trace()), " prediction", sqsum)

# numerical spectrum multiplicity check (labelled numerical)
eig = np.linalg.eigvalsh(C3b.astype(float))
rounded = np.round(eig)
from collections import Counter
cnt = Counter(int(x) for x in rounded)
print("numerical eigenvalue multiset (rounded):", dict(sorted(cnt.items())))
print("predicted multiset:", dict(sorted({e: m for e, m in pred_spec}.items())))
