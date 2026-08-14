"""Study the extension sequence of length-k factors and the RS factor position.

Each length-k factor extends to w0 (value 10v) and/or w1 (value 10v+1).
Interior factors have exactly one extension; the right-special factor has both
(S). The ordered sequence of extensions along lex order is a Sturmian-driven
object. We print it for each k and look for the recursion as k grows:
how does the extension sequence of length k map to length k+1?
"""
import json, os
with open(os.path.join(os.path.dirname(__file__),"..","out","structure.json")) as f:
    structure = json.load(f)
ks = sorted(int(k) for k in structure)

for k in ks:
    d = structure[str(k)]
    ext = d["extensions"]   # in sorted-factors order
    # compress: '0'->0, '1'->1, 'S'->S (RS marker)
    s = "".join(ext)
    # positions of 'S' (should be 1)
    spos = [i for i,e in enumerate(ext) if e=='S']
    n0 = ext.count('0'); n1 = ext.count('1'); nS = ext.count('S')
    # encode as counts
    print(f"k={k:2d} n0={n0} n1={n1} nS={nS} RSpos={spos} ext={s}")
