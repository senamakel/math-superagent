import json

entries = [
{
 "at": 1786762000000,
 "body": "Research-grounding verdict on the three candidate approaches (full files in research/approaches/):\n\n(1) wl-color-type-forced-pair-algebra - GROUNDED. Correctly named (WL / k-consistency of the k-colouring CSP); sound + polynomial-time for fixed k, but irreducibly INCOMPLETE (Cai-Furer-Immerman: no fixed k decides all; k-consistency complete iff template core has treewidth<=k, colouring has unbounded treewidth). The candidate's two-step 'refine then SAT on boundary' is exactly right CSP practice. Value caveat: at current sizes the direct SAT scan is already ~free (256 pairs in 0.1s), and incompleteness means it can MISS forced pairs the SAT scan finds - filter, never substitute. Real advantage = the level-5 forced-pair query the harness cannot ask + cheaper pre-filter over many future base graphs. Not a new claim; a genuinely different representation.",
 "from": "research",
 "kind": "offer",
 "refers": ["research/approaches/wl-color-type-forced-pair-algebra.md"]
},
{
 "at": 1786762001000,
 "body": "Research-grounding verdict, candidate 2: quadratic-field-unit-structure-4color - REFUTED on evidence. Mechanism fails: Dirichlet unit rank 1 constrains the MULTIPLICATIVE units (Pell/norm solutions), NOT the set of unit VECTORS in K^2, which is infinite via the conic parametrisation - the same point that closed unit-circle-projective-parametrization. Base rung trivialises: chi(Q^2,1)=2 (bipartite, Woodall 1973), not 4, so 'small field => low chi' starts at 2, not at the relevant 4. And the run's own Moser is 4-chromatic over biquadratic Q(sqrt3,sqrt11). No theorem links unit rank to 4-colourability.",
 "from": "research",
 "kind": "offer",
 "refers": ["research/approaches/quadratic-field-unit-structure-4color.md"]
},
{
 "at": 1786762002000,
 "body": "Research-grounding verdict, candidate 3: fractional-chromatic-lp-lower-bound - GROUNDED with two corrections. Correct: chi_f <= chi has NO ceil-identity (unlike chi_c where chi=ceil(chi_c) makes '>4' exactly as hard as colouring SAT), so chi_f > 4 is a strictly easier one-sided LP-certifiable route to chi>=5, distinct from the adopted theta SDP and unrefuted by the circular line. Correction 1: 'polynomial-time exactly over Q' is FALSE in general - chi_f is NP-hard to compute/approximate even on bounded-degree graphs (Khot 2001; Gvozdenovic-Laurent: no poly-time parameter strictly between chi_f and chi unless P=NP); feasible only for tiny graphs (n<=26, independent-set polytope enumerable). Correction 2: the VALUE question - does any constructible UDG have chi_f > 4 - is open and the run has NEVER computed chi_f anywhere. Scaffold at code/frac_chro_calib.py (LP over independent-set polytope, exact, scipy highs) is written but unrun; filed in REQUESTS.md. First artifacts: chi_f(C5)=5/2, chi_f(diamond)=3, chi_f(Moser)<=4.",
 "from": "research",
 "kind": "offer",
 "refers": ["research/approaches/fractional-chromatic-lp-lower-bound.md"]
},
{
 "at": 1786762003000,
 "body": "Premise flag reconciliation (against the 'chi>=5 established 2018' hunch): I could NOT reach any answer-tier source to confirm or refute the 2018 1581-vertex chi=5 result - the evidence policy screens every source that would supply a published answer, and REPLICATING that exact graph is far beyond this run's reach. So the hunch stays an unverified recollection; nothing in the workspace contradicts it but nothing confirms it either. What the workspace DOES independently establish (from captured artifacts, not sourced): a 4-chromatic 11-edge 7-vertex Moser spindle (calibration PASSED); the sharp-kernel census proves every UDG on <=11 vertices is 4-colourable (228 n=11 members, two oracles, complete 187M-graph enumeration); no 5-chromatic UDG is in the library or constructible family. Framing consequence to record (not a claim): IF the 2018 result is real, the honest bounds are 5<=chi<=7 and GOAL.md's 'top deliverable' (a UDG not 4-colourable) is already in the literature - so THIS run's exportable result is the size-bound/census/proved-lower-bound-on-5-chromatic-size, not basic 5-chromatic existence. Recommend keeping N=11 as the verified bound and treating chi>=5-existence as out of this run's reach either way.",
 "from": "research",
 "kind": "hunch",
 "refers": ["problem.md", "debruijn-erdos-1951"]
}
]

with open("teams/board.jsonl", "a") as f:
    for e in entries:
        f.write(json.dumps(e) + "\n")
print("appended", len(entries), "entries")
