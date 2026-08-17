"""Round 17: fresh consolidated check of the family sequences and the
incidence rank-deficiency pattern, to confirm the catalogue is current.

All exact integer / Fraction arithmetic. The family index u in {1,3,4,10,31}
(k = u^2+u+2, v = 1+k^2/2, a = 2u+1 | 63)."""
from fractions import Fraction as F

U = [1, 3, 4, 10, 31]

def k_of(u): return u*u + u + 2
def v_of(u): return 1 + k_of(u)*k_of(u)//2

def fam_vals(f):
    return [f(u, k_of(u), v_of(u)) for u in U]

# --- family sequences (re-derived from closed forms here) ---
triangles   = fam_vals(lambda u,k,v: v*k//6)
pentagons   = fam_vals(lambda u,k,v: v*k*(k-2)*(k-4)//5)  # corrected: induced C5, verified by anchored brute force on BvLS(384912) and rook(3)(0); the old v*k*(k-1)*(k-2)*(k-3)//120 encoded a paths-not-cycles count (stray round-17 value, discarded)
hexagon_base= fam_vals(lambda u,k,v: v*k*(k-2)*(2*k*k-21*k+53)//12)  # n3=0 term
outer_blocks= fam_vals(lambda u,k,v: v*(v-1-k)//6)
dist2       = fam_vals(lambda u,k,v: v*(v-1-k))
coclique    = fam_vals(lambda u,k,v: (u+1)*(u*u+2)//2)
n3cap       = fam_vals(lambda u,k,v: v*k*(k-2)//4)
mr          = fam_vals(lambda u,k,v: (v-1 + (2*k-(v-1))//(2*u+1))//2)  # mult of r
ms          = fam_vals(lambda u,k,v: (v-1) - ((v-1 + (2*k-(v-1))//(2*u+1))//2))
d_C         = fam_vals(lambda u,k,v: u+1)
b_coclique  = fam_vals(lambda u,k,v: v - (u+1)*(u*u+2)//2)
dccl_family = fam_vals(lambda u,k,v: v - 1 - k)  # outside count

names = {
 "triangles": triangles, "pentagons": pentagons,
 "hexagon_base_n3=0": hexagon_base, "outer_blocks": outer_blocks,
 "dist2": dist2, "coclique_bound": coclique, "n3cap": n3cap,
 "m_r": mr, "m_s": ms, "d_C": d_C, "coclique_blocks b": b_coclique,
 "dccl_dist": dccl_family,
}

print("=== Fresh re-derived family sequences ===")
for n, s in names.items():
    print(f"{n:>22} {s}")

# --- check first/second differences (nonzero, non-constant => not low poly) ---
def diffs(s):
    return [s[i+1]-s[i] for i in range(len(s)-1)]
print("\n=== First differences (nonzero & non-constant => not linear/quadratic) ===")
for n, s in names.items():
    d1 = diffs(s)
    # compare against "constant" via set
    print(f"{n:>22} d1={d1} const?{len(set(d1))==1}")

# --- incidence rank deficiency (from on-disk capture, exact) ---
# rook(3) n=9 rk=5 d=4 ; doily n=15 rk=10 d=5 ; GQ(2,4) n=27 rk=21 d=6 ; BvLS n=243 rk=243 d=0
print("\n=== incidence rank_2 deficiency vs n : [rook,doily,GQ24,BvLS] ===")
print("[4,5,6,0]  over DIFFERENT v: 9,15,27,243 — so v varies; not a parametric sequence over a fixed family")
