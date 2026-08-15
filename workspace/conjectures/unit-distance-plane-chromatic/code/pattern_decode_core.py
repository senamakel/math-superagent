#!/usr/bin/env python3
"""Decode the dominant 7-vertex 11-edge core form and test whether it is
isomorphic to the Moser spindle. Also check, over the n=11 four-chromatic
kernel members, how many have a 7-vertex 4-critical core isomorphic to Moser.

This tests the structural conjecture: 'op every 7-vertex 11-edge 4-critical
core of a kernel member is the Moser spindle.'

Moser spindle edge set (7 vertices, 11 edges, chi=4) from problem.md / unitfield:
vertices 0..6, edges: two rhombi sharing O.
Standard labelled form (the diamond-based spindle):
  triangle1: edges (0,1),(0,2),(1,2)
  ...
We instead build Moser via the known 7-vertex 11-edge graph and do
isomorphism check by brute permutation (7! = 5040).
"""
import itertools, json, glob, sys
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable

# --- the dominant 7-core from analyze_cores_small: 21 bits, lower-triple order ---
bits = (0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0)
# order i<j, i over 0..6. Build adj matrix.
n=7
idx=0
adj=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if idx < len(bits):
            adj[i][j]=adj[j][i]=bits[idx]
        idx+=1
core_edges=[(i,j) for i in range(n) for j in range(i+1,n) if adj[i][j]]
print("dominant 7-core edges:", core_edges, "count", len(core_edges))

# canonical Moser spindle: use the 7-vertex Moser from problem (labelled 0..6)
# Build from the two-rhombus description in CONTEXT: O=0, P1=1, P2=2, Q=3,
# P1'=4, P2'=5, Q'=6. Edges (all unit):
moser = {(0,1),(0,2),(1,2),(0,3),(0,4),(1,4),(2,5),(1,5),
         (3,4),(3,6),(4,6)}
# Wait - need the 11-edge set. Verify edges by the rhombus structure:
# Rhombus 1: O,P1,P2,Q --> unit edges OP1,OP2,P1P2,P1Q,P2Q? Let's define properly.
# Known Moser: two rhombi sharing O. Rhombus A: O,(1,0),(1/2,sqrt3/2),(3/2,sqrt3/2)
#   edges: O-P1, O-P2, P1-P2, P1-Q, P2-Q  (5 edges, minus OP1? no)
# We rely on the calibrated 11-edge set from brute_calibration.
moser_edges = set()
ms = eval(open("/workspace/code/out/brute_calibration.txt").read())
# brute_calibration print format unknown; hardcode from CONTEXT: 7 vertices 11 edges.
# From unitfield moser_spindle_points the edges are all pairs with |x-y|^2=1;
# the standard 11 are:
moser_edges = {(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),
               (1,4),(1,5),(2,4),(2,5),
               (3,4),(3,6),(4,6)}
# that's 13, wrong. Let me just build Moser with proper edges from unitfield.

from lib import unitfield as uf
pts = uf.moser_spindle_points()
edges_m = uf.unit_graph(pts)
print("Moser from unitfield:", edges_m)
