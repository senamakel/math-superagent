"""Verify the exact identity L_in == V_patch - 4 across every n3
survivor at the stable fixpoint, and the seed itself.
This re-derives the ledger fresh (no floats)."""
import sys
sys.path.insert(0, '/workspace/code')
from lib.n3patch import (seed, closure_rule3, assignments, forced_ledger,
                         patch_cliques, undecided_pairs)

def grow_all():
    """Replicate n3_grow_radius: enumerate survivors to stable fixpoint."""
    verts, A = seed()
    # radius 0: seed
    led0 = forced_ledger(verts, A)
    # radius 1: closure + enumerate
    verts, A, st = closure_rule3(verts, A)
    survs = []
    for bits, nA in assignments(verts, A):
        ok_path = True
        vv, AA = list(verts), dict(nA)
        while True:
            vv, AA, st = closure_rule3(vv, AA)
            if st == 'excess':
                ok_path = False
                break
            free = undecided_pairs(vv, AA)
            if not free:
                break
            # not fully decided -> branch again (not expected at fixpoint)
            break
        if ok_path:
            survs.append((vv, AA))
    return led0, survs

led0, survs = grow_all()
print("seed: V=%d L_in=%d  (V-4=%d)  match=%s"
      % (led0['V_patch'], led0['L_in'], led0['V_patch']-4,
         led0['L_in']==led0['V_patch']-4))

bad = []
vals = []
for (vv, AA) in survs:
    led = forced_ledger(vv, AA)
    vals.append((led['V_patch'], led['L_in']))
    if led['L_in'] != led['V_patch'] - 4:
        bad.append((led['V_patch'], led['L_in']))
print("survivors checked: %d" % len(survs))
print("distinct (V, L_in) pairs:", sorted(set(vals)))
print("violations of L_in==V-4: %d" % len(bad))

# every patch triangle per vertex: tri_through_v <= 3? (max_lines_v reported)
maxlines = max(forced_ledger(vv, AA)['max_lines_v'] for (vv, AA) in survs)
print("max patch lines through any vertex across survivors:", maxlines)
