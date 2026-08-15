import subprocess, os, sys
os.chdir("/workspace/code/scholar")

# Fix the module path so lib.* imports work
import importlib.util, pathlib
p = "/workspace/code/lib/rightdiag.py"
spec = importlib.util.spec_from_file_location("rightdiag", p)
rd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rd)
cycle_and_nu2 = rd.cycle_and_nu2

from math import comb

def build_2thenodds(word, n_terms):
    p = len(word)
    gaps = [2 if word[j % p] == 0 else 4 for j in range(n_terms)]
    q = [2, 3]
    for g in gaps:
        q.append(q[-1] + g)
    return q

def delta_diag(q):
    D = [q[0]]
    diags = [list(D)]
    for n in range(1, len(q)):
        nd = [0]*(n+1)
        nd[0] = q[n]
        for k in range(1, n+1):
            nd[k] = abs(nd[k-1] - D[k-1])
        D = nd
        diags.append(list(D))
    return diags

def nu2_for(word, n):
    # n gaps => q has n+2 entries indexed 0..n+1
    q = build_2thenodds(word, n)
    diags = delta_diag(q)
    diag = diags[-1]
    tau, nu2 = cycle_and_nu2(diag)
    return tau, nu2

print("=== Independent re-check of contradiction ===")
print("Word: h periodic.  If 'any periodic -> nu2=O_p(1)' were right,")
print("every row below would be bounded independent of n.\n")

n_vals = [200, 1000, 3000, 6000]
tests = [
    ("P=2 (power of 2, alt)", [0,1]),
    ("P=2 (power of 2, tail1)", [1,0]),
    ("P=3 (odd factor, tail1)", [0,0,1]),
    ("P=4 (power of 2)", [0,0,0,1]),
    ("P=5 (odd factor, tail1)", [0,0,0,0,1]),
    ("P=7 (odd factor, tail1)", [0,0,0,0,0,0,1]),
]
for name, word in tests:
    row = []
    for n in n_vals:
        _, nu2 = nu2_for(word, n)
        row.append(nu2)
    trend = "linear" if row[-1] > 2*row[0] else ("bounded" if row[-1] <= 4 else "?")
    print("%-28s nu2(n)=%s   -> %s" % (name, row, trend))

print()
print("Interpretation: power-of-2 periods stay bounded (collapse OK);")
print("odd-factor periods grow linearly -> 'periodic of ANY p gives nu2=O_p(1)' is FALSE.")
