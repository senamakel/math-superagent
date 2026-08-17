"""Analyze the lex-ordered chain of length-k factors.

Perrin-Restivo: consecutive factors u (lex-order) and v differ by u=r·ab·s,
v=r·ba·s, so their decimal values differ by +/-9*10^m for some exponent m.
We extract, for each k, the sorted factor values, the consecutive differences
(must be +/-9*10^m), and the sequence of these 'moves'. We then look for
structure in the move sequence across k.
"""
import json, os

with open(os.path.join(os.path.dirname(__file__),"..","out","structure.json")) as f:
    structure = json.load(f)

ks = sorted(int(k) for k in structure)
print("k : move sequence (m, sign) between consecutive factors (lex order)")
from collections import defaultdict
all_moves = {}
for k in ks:
    facs = structure[str(k)]["factors"]  # already sorted
    vals = [int(w) for w in facs]
    # verify differences are +/-9*10^m
    moves = []
    ok = True
    for j in range(len(vals) - 1):
        d = vals[j+1] - vals[j]
        # must be +/-9*10^m
        found = False
        if d != 0:
            if d % 9 == 0 and (d // 9) % 10 in (1,) and abs(d//9) % 2 == 1:
                pass
        # check = +/-9*10^m
        ad = abs(d)
        if ad % 9 == 0:
            m = ad // 9
            # m should be 10^e
            t = m
            e = 0
            while t > 0 and t % 10 == 0:
                t //= 10
                e += 1
            if t == 1:
                found = True
                moves.append((e, 1 if d > 0 else -1))
            else:
                ok = False
        else:
            ok = False
    all_moves[k] = moves
    print(f"k={k:3d}: ok={ok} moves={moves[:30]}{'...' if len(moves)>30 else ''}")

# Look at how many moves are + vs -, and positions of swaps (m)
print()
print("Distribution of move exponents m:")
for k in [6,7,8,9,10]:
    moves = all_moves[k]
    print(f"  k={k}: max m = {max(m[0] for m in moves)}, moves={moves}")
