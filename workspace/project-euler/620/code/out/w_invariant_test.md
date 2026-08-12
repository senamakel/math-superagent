# W-invariant off-centre meshing model — test result

Program: `code/pattern/w_invariant_test.py`
Output: `code/out/w_invariant_test.txt`
Model source: `research/threads/offcentre-mesh-phase-model.md`

## What was tested

Off-centre dual-mesh phase model. Geometry: S=(0,0), C=(d,0),
R=c/2pi, r=s/2pi, rho_t=t/2pi, a_t=(s+t)/2pi (=|SP|), b_t=(c-t)/2pi (=|CP|),
d in (d_min, d_max), d_min=max(|a_p-b_p|,|a_q-b_q|), d_max=R-r-1 (1cm gap).
Interior angles phi, chi, gamma (at S, C, P; phi+chi+gamma=pi) from atan2 on
the exact tangency point. Invariants:
  W_t  = s*phi_t  + c*chi_t  - t*gamma_t
  W'_t = s*phi_t  - c*chi_t  + t*gamma_t

Condition sets (each condition a congruence to an integer, mod 1):
- A: (s*phi_p+c*chi_p/pi)∈Z, (s*phi_q+c*chi_q/pi)∈Z, (W_p-W_q)/2pi∈Z
- B: (W_p-W_q)/2pi∈Z  (cross-type only)
- C: (p*gamma_p-c*chi_p)/pi∈Z, (q*gamma_q-c*chi_q)/pi∈Z, cross
     (thread suspected this is identically satisfied at all d)
- D: (s*phi_p+c*chi_p/pi)∈Z, (s*phi_q+c*chi_q/pi)∈Z, (W'_p-W'_q)/2pi∈Z

## Method

Fixed-budget per pair: float64 numpy scan of [d_min,d_max] (N=1e7 flagship,
1e6 in G-sums; chunked to limit memory) plus 1e-3 endpoint probes where the
angle derivatives diverge near d_min; each near-integer anchor of any key is
refined by mpmath (40 dps) bisection of `key(d)=nearest_integer` to residue
<1e-24; a d is valid for a set iff the max residue over that set's conditions
is <VERIFY_TOL=1e-9 (mpmath). Guards reject anchors on/outside the open
interval and roots that drift >200*step from their anchor. An independent
coverage cross-check clusters all grid points whose conjoined set-residue is
near-zero and requires each cluster to be matched by a found valid d.

Cost per (c,s,p,q): fixed O(N) float work + O(#roots) mpmath bisections —
independent of the problem bound 500. No answer-space enumeration.

## Results (g(16,5,5,6); oracle = 9)

| set | valid d | note |
| --- | --- | --- |
| A | 0 | no d satisfies Ap & Aq & cross together |
| B | 5 | cross-type roots only |
| C | 0 | **NOT identically satisfied** — residues up to 0.5, contradicts thread suspicion |
| D | 0 | same as A; the crossD variant adds nothing |

B's 5 valid d (norm residue of cross ~1e-29): d =
0.16077354, 0.17476876, 0.20974100, 0.29060980, 0.53311395.
Convergence: B count stable at 5 for N = 1e6, 4e6, 12e6 (same 5 roots, same
5 clusters, coverage OK) — not a resolution artifact.

Since no set gives 9 on the flagship, G(16)/G(20) were not run (only sets
hitting 9 trigger them).

## Verdict

None of condition sets A/B/C/D reproduces the oracle 9/9/205. The W-invariant
model as specified — in any of these four congruence formulations — is not the
counting rule. The cross-type single congruence (B) is the only one that
produces any discrete d's (5), so a completed model would need the additional
pair/completeness constraints to select, from richer data, the 9 — but A, C, D
all return 0, so no simple completion among these variants works either.
Set C's "identically satisfied" hypothesis is falsified.
