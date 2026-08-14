import json
D=json.load(open("out/exact_state_1_120.json"))
MOD=101001001
# print k, N1, P1, R within blocks, detect P1 pattern
alpha=(3-5**0.5)/2
print("k : N1 : P1mod : R : block")
# find blocks of constant vR
vrs=[D[str(k)]['vR'] for k in range(1,121)]
runs=[]; cs=None
for k in range(1,121):
    v=vrs[k-1]
    if v!=cs:
        if cs is not None: runs.append((cs_start,k-1,cs))
        cs=v; cs_start=k
runs.append((cs_start,120,cs))
for (s,e,v) in runs[:40]:
    print(f"  block k={s}..{e} len={e-s+1}: vR={v}")
    # P1 mod within block
    p1=[D[str(k)]['P1']%MOD for k in range(s,e+1)]
    print(f"    P1 mod: {p1}")
    N1=[D[str(k)]['N1'] for k in range(s,e+1)]
    print(f"    N1: {N1}")
