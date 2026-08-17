"""Characterize the block structure of vR (right-special factor value) over k.

vR(k) constant on intervals [lo,hi]. Find these intervals from exact data,
plus track P1, N1, S evolution within each block to test if the state is a
simple linear recurrence over a block (constant vR).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "out", "structure.json")
st = json.load(open(DATA))
ks = sorted(int(k) for k in st)

def get(k):
    d = st[str(k)]
    return dict(Psi=d["Psi"], S=sum(d["values"]), N1=d["N1"],
                P1=d["P1"], vR=int(d["R"]), R=d["R"])

# vR blocks
print("vR block structure (k : vR_value : R-string)")
cur_vR = None
start = None
for k in ks:
    v = get(k)
    if v["vR"] != cur_vR:
        if cur_vR is not None:
            print(f"[{start}-{k-1}]  vR={cur_vR} R={get(start)['R']}")
        cur_vR = v["vR"]; start = k
print(f"[{start}-{ks[-1]}]  vR={cur_vR} R={get(start)['R']}")

print()
print("Block lengths:", )
# recompute
blocks=[]
cur=None;start=None
for k in ks:
    v=get(k)
    if v["vR"]!=cur:
        if cur is not None: blocks.append((start,k-1,cur))
        cur=v["vR"];start=k
blocks.append((start,ks[-1],cur))
print("block (lo,hi,length):", [(lo,hi,hi-lo+1) for lo,hi,_ in blocks])
