"""Round-16 pattern-finder re-check.

Two purposes:
1) Independently reproduce the full family-count catalogue for srg(v,k,1,2),
   k=u^2+u+2, a=2u+1|63, u in {1,3,4,10,31}, and re-run the sequence tools'
   logic over every catalogue sequence (no low-order linear recurrence, no
   OEIS law -- all are u^3/u^4 quartics governed by the a|63 index set).
2) Re-verify the ONE genuinely new object since round 15 -- the clean
   (super-simple) 2-(22,4,2) design -- as an independent counting check, and
   extract its block-intersection histogram (a finite structural fact, not a
   sequence) plus confirm super-simplicity.

Exact integer arithmetic only.
"""
from math import isqrt

u_list = [1, 3, 4, 10, 31]

def fam(u):
    k = u*u + u + 2
    v = 1 + k*k // 2
    return k, v

def seq_check(values, name):
    # First differences over the 5-term feasible-family sample
    diffs = [values[i+1]-values[i] for i in range(len(values)-1)]
    dd = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
    print(f"{name:>14}: values={values}")
    print(f"{'':>14}  d1={diffs}")
    print(f"{'':>14}  d2={dd}  (d2 nonzero/nonconstant => not low-degree poly)")

names = ["u","k","v","a","triangles","pentagons","hexagon_base","outer_blocks",
         "distance2","coclique","n3cap","m_r","m_s"]
catal = {nm: [] for nm in names}
for u in u_list:
    k, v = fam(u)
    a = 2*u+1
    T = v*k//6
    p5 = v*k*(k-2)*(k-4)//5
    hx = v*k*(k-2)*(2*k*k-21*k+53)//12
    ob = k*(k-2)*(k-4)//12
    d2 = k*(k-2)//2
    coc = (u*k+2)//2
    n3cap = k*(k-2)*(k*k+2)//8
    m_r = u*(u*u+u+2)*(u*u+2*u+3)//(2*(2*u+1))
    m_s = (u+1)*(u*u+2)*(u*u+u+2)//(2*(2*u+1))
    for nm, val in [("u",u),("k",k),("v",v),("a",a),("triangles",T),
                    ("pentagons",p5),("hexagon_base",hx),("outer_blocks",ob),
                    ("distance2",d2),("coclique",coc),("n3cap",n3cap),
                    ("m_r",m_r),("m_s",m_s)]:
        catal[nm].append(val)

print("=== family catalogue ===")
for nm in ["triangles","pentagons","hexagon_base","outer_blocks","distance2",
           "coclique","n3cap","m_r","m_s"]:
    seq_check(catal[nm], nm)

# known reference values from the prior rounds (cross-check exact equality)
assert catal["triangles"] == [6,231,891,117096,81842481]
assert catal["pentagons"] == [0,33264,384912,1669320576,96451036488576]
assert catal["coclique"] == [3,22,45,561,15408]
assert catal["n3cap"] == [18,4158,26730,19320840,121781611728]
assert catal["v"] == [9,99,243,6273,494019]
print("reference cross-checks: ALL PASS (catalogue unchanged)")

print()
print("=== clean super-simple 2-(22,4,2) design re-verify ===")
lines = [l.split() for l in open("code/out/coclique_lift_clean_design.txt")
         if l.strip()]
blocks = [tuple(sorted(map(int, l))) for l in lines]
Bs = set(blocks)
print("blocks:", len(blocks), " distinct:", len(Bs))
assert len(blocks) == len(Bs) == 77
for b in blocks:
    assert len(b) == 4 and all(0 <= x <= 21 for x in b)

from collections import Counter
deg = Counter()
pairc = Counter()
tripc = Counter()
pairshare = Counter()
for b in blocks:
    for x in b:
        deg[x] += 1
    for i in range(4):
        for j in range(i+1,4):
            pairc[tuple(sorted((b[i],b[j])))] += 1
    for i in range(4):
        for j in range(i+1,4):
            for m in range(j+1,4):
                tripc[tuple(sorted((b[i],b[j],b[m])))] += 1
for i in range(len(blocks)):
    for j in range(i+1,len(blocks)):
        inter = len(set(blocks[i]) & set(blocks[j]))
        pairshare[inter] += 1
print("degree hist (all at 14):", dict(sorted(deg.items())))
assert all(d==14 for d in deg.values())
print("pair coverage (all at 2):", sorted(set(pairc.values())))
assert all(c==2 for c in pairc.values())
print("triple-overlap max:", max(tripc.values()), "(super-simple iff <=1)")
print("block-pair intersection histogram (0/1/2):", dict(sorted(pairshare.items())))
print("RE-VERIFY: super-simple 2-(22,4,2) PASS =",
      max(tripc.values()) <= 1 and all(c==2 for c in pairc.values()) and len(Bs)==77)
