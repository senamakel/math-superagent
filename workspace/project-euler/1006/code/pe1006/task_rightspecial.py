"""Examine state quantities vR(k), R(k) as binary strings/fibonacci structure.

The right-special factor R(k) (length k, extends both 0 and 1) is reputedly a
prefix of the infinite Fibonacci word near a special position. Tabulate R(k) as
a string and compare to the infinite Fibonacci word's prefixes / suffixes, and
list vR(k) and N1(k), N0(k) to seek structural recurrences.
"""
import json, os

MOD = 101001001
with open(os.path.join(os.path.dirname(__file__),"..","out","structure.json")) as f:
    structure = json.load(f)

# build infinite Fibonacci word f (fixed point 0->01, 1->0)
a, b = "0", "01"
# iterate to length 500
while len(b) < 600:
    a, b = b, b + a
f = b

ks = sorted(int(k) for k in structure)

print("k : R(k) : vR(k) : N1 : N0 : predParent?")
# The right-special factor of length k is the prefix of the *left*-special structure.
# Check: is R(k) always a prefix of f?  Compare spacing.
prevR = None
for k in ks:
    d = structure[str(k)]
    R = d["R"]  # integer
    # find R as binary string of length k
    # factors contains the string; find which has value and is right-special
    facs = d["factors"]
    rs = None
    for w in facs:
        if (w+'0') in {x for x in d.get("extensions",[]) if False}:
            pass
    # use recorded right-special via checking extension in next length
    nxt = structure.get(str(k+1))
    if nxt:
        nxtk1 = {w for w in nxt["factors"]}
        for w in facs:
            if (w+'0') in nxtk1 and (w+'1') in nxtk1:
                rs = w
                break
    else:
        rs = f"{R}"  # approximate
    print(f"{k:3d} : {rs!r} vR={R:12d} : N1={d['N1']} N0={d.get('N1',0)}")

print()
# Relationship: right-special length k+1 ends with? and is it R(k)+d or d+R(k)?
print("Check whether R(k+1) is an extension of R(k):")
for k in ks:
    nxt = structure.get(str(k+1))
    if not nxt: continue
    cur = structure[str(k)]
    nxtk1 = set(nxt["factors"])
    rs_cur = None
    for w in cur["factors"]:
        if (w+'0') in nxtk1 and (w+'1') in nxtk1:
            rs_cur = w; break
    rs_nxt = None
    k2 = structure.get(str(k+2))
    k2f = set(k2["factors"]) if k2 else set()
    for w in nxt["factors"]:
        if (w+'0') in k2f and (w+'1') in k2f:
            rs_nxt = w; break
    print(f"{k:3d}: R(k)={rs_cur!r:20s} R(k+1)={rs_nxt!r:20s} R(k+1)[0:-1]==R(k)? {rs_nxt[:k]==rs_cur}")
