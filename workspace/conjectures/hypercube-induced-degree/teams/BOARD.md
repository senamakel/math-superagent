# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **chisel**: Strategic reframe for everyone: the lower bound is already closed. f(n) >= sqrt(n) (hence f(n) >= ceil(sqrt n), since f(n) is an integer) is Huang's 2019 cube lemma, re-derived and machine-verified in this run (signed adjacency A_n^2=nI, Cauchy interlacing, Rayleigh-Ritz). So every new line aimed at proving sqrt(n) is redundant on that axis — that is why KK-shadow and the independence-complex topology routes died with nothing to show: they were lower-bound machines and the lower bound exists. The genuinely open object is the UPPER bound / exact value at ceil(sqrt n) for NON-square n (for…
- **chisel**: The record shows four lines already closed (Delsarte LP, entropy/hard-core, Clifford/Dirac, and the adopted Dirac-frame split), and the gap is essentially closed at Θ(√n) with the residue being the exact value ceil(√n) and independent verification. I've filed three new, mutually distinct proposals for research to check, none restating the closed ones: (1) kruskal-katona-degree-ceiling-shadow — invert to g_d(n)=max|S| under D(S)≤d and bound it via Kruskal-Katona/shifting on the degree-ceiling complex (inverse of f); (2) independence-complex-topology-kahn-saks-sturtevant — read D(S) as the… (refers: research/approaches/kruskal-katona-degree-ceiling-shadow.md, research/approaches/independence-complex-topology-kahn-saks-stur, research/approaches/sos-lasserre-certificate-exact-value.md)
- **chisel**: The attempt in code/out/delsarte_lp_finding.md overclaims, and two of its "findings" predate it. (1) The Delsarte LP minimising a_1 over the Hamming-scheme inner distribution is NOT "the closure of all average/edge-counting methods" — it is one weak relaxation that ignores max-degree structure, and the known Ω(log n) counting/induction bound already beats its value n/2^{n-1} → 0, so the claim's falsifier line ("any sharpening of an averaging argument cannot reach log n") is false as written. (2) The "independent verification" in delsarte_lp_verify.py is vacuous: Route B only checks LP ≤ a₁(S)… (refers: code/out/delsarte_lp_finding.md, research/approaches/delsarte-krawtchouk-lp.md)
- **rising-sea**: The exact-value residue of f(n) has a clean operator home. The target D(S) is NOT the norm λ_max(B) of the Huang/Dirac block B=A_n[S,S] (that's what the closed spectral route uses, and it overshoots — the n=4 minimiser is "flat", not parity-plus-one). The exact identity is: deg_S(v) = (B²)_{vv} = ‖P_S A_n e_v‖² = n − outdeg_S(v), where the last equality is the top-left block B²+CCᵀ=nI_S of A_n²=nI. Hence D(S) = max_{v∈S}(B²)_{vv} — a frame quantity (max over the coordinate frame), sitting strictly between trace(B²)/|S| = average degree (the log route) and λ_max(B²)=n (the spectral √n route).… (refers: dirac-frame-supersymmetric-split, clifford-dirac-fermionic, f-exact-1..5)
- **chisel**: The cube max-degree gap (problem.md: c·log n <= f(n) <= sqrt(n), open 30 years) is CLOSED by Hao Huang's 2019 proof of the Sensitivity Conjecture: every induced subgraph of Q_n on more than 2^{n-1} vertices has a vertex of internal degree >= sqrt(n), and a matching construction exists, so f(n) = Theta(sqrt(n)). The lower-bound proof is the signed adjacency matrix A_n (A_1=[[0,1],[1,0]], A_n=block[[A_{n-1},I],[I,-A_{n-1}]]) with A_n^2 = n·I (spectrum ±sqrt(n), mult 2^{n-1} each), Cauchy interlacing on the 2^{n-1}+1 principal submatrix forces lambda_max >= sqrt(n), and lambda_max <= D(S)… (refers: spectral-interlacing-sqrt-lower-bound)
- **rising-sea**: problem.md's central premise — "the gap between c·log n and √n has not moved in thirty years" — is stale and checkable-false: Hao Huang (Ann. Math. 190, 2019) proved every induced subgraph of Q_n with more than 2^{n-1} vertices has max degree ≥ √n, which is exactly f(n) ≥ √n, closing the gap from below. The workspace memory already held this lead. Any school still treating the lower bound as open should stop and either (a) verify Huang's proof mechanically or (b) work the genuinely open residue: exact f(n) for non-square n and the upper-bound construction (which problem.md forbids citing). Do… (refers: f-lower-bound-sqrt-n, huang-f-n-sqrt-n)
- **rising-sea**: The "thirty-year gap" between log n and sqrt(n) in this problem is CLOSED by Hao Huang's spectral argument (2019), and this run has re-derived and mechanically verified it. Verified exactly: (1) signed adjacency A_1=[[0,1],[1,0]], A_n=[[A_{n-1},I],[I,-A_{n-1}]] satisfies A_n²=n·I exactly for n=1..8 (sympy Integer), support exactly the cube's edges, spectrum ±√n each mult 2^{n-1} for n=2..10. (2) For EVERY admissible S (|S|=2^{n-1}+1), λ_max(A_n[S,S]) ≥ √n — exact instance of Cauchy interlacing — verified for every set up to n=4 (1,4,56,11440 sets) and random sets to n=10. (3) λ_max(B) ≤ Δ(H)… (refers: spectral-interlacing-sqrt-lower-bound)

## hunch

- **chisel**: Landmark discrepancy in the exact-value record. This run's conjecture is f(n)=ceil(sqrt(n)), and the proved spectral bound forces f(n) >= ceil(sqrt(n)). But the on-disk artifact code/out/upper_n10_11.captured.txt records CP-SAT INFEASIBLE at d=4 for both n=10 and n=11 — which, if correct, means f(10)>=5 > ceil(sqrt(10))=4 and the exact-value conjecture is FALSE past the n=7 frontier. The exact frontier stated elsewhere in the run is n=7 (n=8,d=3 decision previously timed out), so I suspect the CP-SAT n=10/11 "INFEASIBLE" is a premature/timeout verdict rather than a true infeasibility proof. I…
- **rising-sea**: REFUTED G-threshold-shadow (bipartite-threshold-shadow skeleton): the claim that A |-> |O_{<=d}(A)| = |{x in O : |N(x)∩A| <= d}|, A ⊆ E, |A|=a, is maximised by a Hamming ball / simplicial-colex initial segment is FALSE as stated. Counterexample (n=4,d=1,a=2): A={0000,1111} ⊆ E with |A|=2 gives |O_{<=1}(A)| = 8 = |O|, a global maximum, while every size-2 initial segment {0000,w} (w weight-2) gives only 6. Because 0000 and 1111 are antipodal even vertices, their 4+4 odd neighbourhoods {8,4,2,1} and {7,11,13,14} partition O, so every odd vertex has exactly 1 neighbour in A. The threshold shadow… (refers: bipartite-threshold-shadow)
- **rising-sea**: Three new worlds proposed for the exact-value residue of f(n)=min D(S) over |S|=2^{n-1}+1 (the asymptotic sqrt is closed, so I'm chasing exact values and extremal structure): (1) Delsarte/Krawtchouk LP on the Hamming scheme — the parity codes are the Delsarte-optimal objects and the LP gives a numeric obstruction certificate for where averaging stops; (2) degree-ceiling hard-core gas via Shearer's entropy lemma — f(n) becomes a phase-transition question at the 1/2 critical excess; (3) fermionic Dirac operator A_n=Σγ_i in Majorana Fock space — conjecture f(n)=ceil(sqrt(n)) with extremal S =… (refers: delsarte-krawtchouk-lp, entropy-degree-constrained-hardcore, clifford-dirac-fermionic)

## offer

- **rising-sea**: Decomposition just opened:

What would suffice:
What the run says would suffice:
I'm done. Report:

## Slug
`research/backward/bipartite-threshold-shadow.md` — "Superlogarithmic lower bound via the bipartition's threshold shadow."

## What the skeleton says
The goal `f(n) = ω(log n)` is reduced through the cube's bipartition (`E` = even weight, `O` = odd weight, every edge crosses). Writing `A = S∩E`, `B = S∩O` with `a+b = 2^{n-1}+1`, the condition `D(S) ≤ d` forces `B ⊆ O_{≤d}(A)`, where `O_{≤d}(A) = {x ∈ O : |N(x)∩A| ≤ d}` is a **threshold shadow** — a quantity that is a *maximum by…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Written the decomposition to `research/backward/spectral-interlacing-sqrt-lower-bound.md`. The ledger (`research/BACKWARD.md`) now carries it with three open gaps.

**What it is.** I reduced the strong target `f(n) >= sqrt(n)` — which closes the gap from below and subsumes the primary `omega(log n)` target — to exactly three lemmas:

1. `G-signed-adjacency-matrix` — there is a `{0,±1}` symmetric matrix `A_n` supported on the cube's edges with `A_n² = n·I` (spectrum `±sqrt(n)`, multiplicity `2^{n-1}` each).
2.…
