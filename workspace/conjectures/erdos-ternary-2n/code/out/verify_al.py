#!/usr/bin/env python3
"""Verify automaton construction against the paper's worked examples.
Run from /workspace/code/out so al_automaton is importable in the same dir."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from al_automaton import algo_A, algo_B, perron_eigenvalue

print("=== Algorithm A state counts vs paper ===")
for M, expect in [(7,4),(19,8),(43,None)]:
    ids, edges, rev = algo_A(M)
    tag = "" if expect is None or len(ids)==expect else "MISMATCH"
    print(f"C(1,{M}): states={len(ids)} (paper {expect}) {tag}")

print("\n=== Algorithm B label product ===")
ids, edges = algo_B([7,19])
print(f"C(1,7,19): states={len(ids)} (paper: 6)",
      "OK" if len(ids)==6 else "MISMATCH")

print("\n=== dim_H check vs Table 5.2 (single even powers) ===")
paper = {4:0.438018, 16:0.255960, 64:0.278002, 256:0.287416,
         1024:0.215201, 4096:0.244002, 16384:0.267112}
for M, expd in sorted(paper.items()):
    ids, edges = algo_A(M)
    b = perron_eigenvalue(len(ids), edges)
    d = math.log(b,3)
    ok = "OK" if abs(d-expd)<1e-3 else f"DIFF {expd-d:+.4f}"
    print(f"C(1,{M}): states={len(ids):4d} dim={d:.6f} paper={expd:.6f} {ok}")
