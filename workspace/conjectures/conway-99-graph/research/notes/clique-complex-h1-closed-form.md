# Claim: dim H1(Cl(G)) = 2T − v + 1 = vk/3 − v + 1 — PROVEN for every connected λ=1 SRG

**Status:** proven (derived here from the definition), verified numerically on the controls.
**Gate verdict:** still **refuted-on-arrival** as a 99/243 separator.

## Proof (not a conjecture)

For a connected SRG G with v vertices, E edges, T triangles, the clique complex
Cl(G) has H1(Cl(G);Q) = dim(cycle space) − rk(delta_2) = (E − v + 1) − rk(delta_2),
where delta_2 : C_2 → C_1 sends each triangle to its 3-edge boundary chain.

**Key step — λ=1 forces rk(delta_2) = T.** The definition of λ=1 is that every
edge lies in *exactly one* triangle. If two triangles shared the edge {a,b},
then a and b would have (at least) two common neighbours, giving λ(a,b) ≥ 2,
contradicting λ=1. Hence all triangles are **edge-disjoint**. The boundary of a
triangle {a,b,c} is the edge-chain ab + bc + ca, and edge-disjoint triangles have
pairwise-disjoint edge-support: their boundary vectors are linearly independent
over any field (coefficients ±1). Therefore rk(delta_2) = T exactly — *not* a
2-data-point accident but forced by the parameter λ=1.

Therefore, for every connected λ=1 SRG:

    dim H1(Cl(G)) = (E − v + 1) − T  =  vk/2 − v + 1 − vk/6  =  vk/3 − v + 1  =  2T − v + 1.

## Verification (computed here)

- rook(3) = srg(9,4,1,2): E=18, T=6, H1 = 18−9+1−6 = 4 = 2·6−9+1. ✓
- bvls = srg(243,22,1,2): E=2673, T=891, H1 = 2673−243+1−891 = 1540 = 2·891−243+1. ✓

Confirmed two independent ways: exact rational Gaussian elimination over
Fractions (`pf_h1_closed_form.py`) and sparse mod-p elimination at p=1009, 65537
(`research_clique_complex_chi.py`). Edge-disjointness histogram: {1: 18} (rook),
{1: 2673} (bvls) — every edge in exactly one triangle, rank=T, rho=1.

## Family sequence (exact form)

Over the feasible u ∈ {1,3,4,10,31} (k = u²+u+2, v = 1+k²/2):

    H1 = vk/3 − v + 1 : [4, 364, 1540, 227920, 163190944]
    at 99 (u=3): 364.

OEIS: **no match** (recorded miss — do not search again).
`analyze_sequence`: not a low-degree polynomial (divisor-63 signature); all terms
≡ 0 (mod 4); mod-2 period 1.

## Gate verdict (directive 39, FIRST): still refuted-on-arrival

H1 is **nonzero on both controls** (4, 1540) — so Cioaba–Mim's H1=0 criterion,
whatever else it says, cannot separate 99 from 243: both fail any H1=0 test
identically, and the predicted 364 at 99 is also nonzero. The closed form is
now a *proven* parameter-determined invariant (it holds for ANY λ=1 SRG), which
is exactly why it has **no separating power** — it is atomic in (v,k) and both
controls realize the same formula. The homology line is closed as route
twelve's gate: **refuted on arrival, no obstruction, no separation**, and now
with the mechanism (edge-disjointness from λ=1) stated and proved rather than
left as a 2-point conjecture.

## What would falsify

Nothing within the λ=1 family: the formula is a theorem. It would only fail for
a *disconnected* or non-λ=1 graph, which is not the problem class. (The earlier
scratch framing "rho=1 is a 2-point conjecture" is **retracted** — that was
before the edge-disjointness step; the independence is forced by λ=1.)

## Files
- `code/out/homology_controls.py` (gate source)
- `code/out/research_clique_complex_chi.py` (Euler char + mod-p double check)
- `code/out/pf_h1_closed_form.py` (rank + closed-form exact verification)
- `code/out/pattern_finder_report33.md` (round report)
- this note
