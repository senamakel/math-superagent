# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk, from the note store,
or from a session it was not present for: established results with their basis,
approaches that died and why, what the computed numbers look like, what durable
memory relates this problem to, and where two accounts disagree. It is not a
catalogue of files — `research/INDEX.md` is that — and not a narration of what
agents did.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The
file is re-sent on every model call in every role that reads it, so length here
is a bill the whole run pays many times over; a brief past its budget is cut
where it exceeds it on the way into a prompt, with a notice saying so. Link the
file that still holds any detail compressed away — source notes under
`research/summaries/`, untouched full texts under `research/sources/`,
reflections, threads. Durable findings belong in Cognee. A statement nobody can
trace to a source is worth less than no statement.

## Established

What this run may treat as known. Evidence classes: `checked` = computed here in exact integer arithmetic; `sourced` = primary source cited; `reasoned` = derived here from a source; `asserted-by-source` = on the source's word, not yet independently checked here.

- **Phase state (directive).** Phase 1 is closed and the library is CLOSED — no further source acquisition except against a stated gap in `research/REQUESTS.md`. The oracle is PROVEN, including its λ/μ counting path: the count-path negatives C9(1,2) and circulant(99,{1..7}) both pass shape+regularity and fail `is_srg` only on explicit LAMBDA/MU count mismatches (18/18 adjacent/non-adjacent pairs at 9; 1386/8118 at 99), captured in `code/out/oracle-controls.captured.txt`. `sys.path.insert` removed tree-wide; imports are bare `from lib.srg import ...`.
- **Makhnev 1988 Thm 2 conditional, sourced AND controls passed (checked).** The primary Russian full text has been read in the library (open on mathnet.ru paperid=4220): under condition (*) [n3=0], a λ=1 SRG is μ≤3 or (27,10,1,5) (Thm 1), and no srg(99,14,1,2)/(115,18,1,3) satisfies (*) (Thm 2, building an srg(33,12,1,6) contradiction). Admissibility gate passed: BOTH controls rook(3) and bvls_graph() satisfy (*) with n3=0 (exact; μ=2≤3 so Thm1's branch absorbs them) in `code/out/makhnev-1988-condition-captured.txt`. Contrapositively, any putative (99,14,1,2) has n3≥1 — a CONSTRAINT, not a nonexistence proof (the n3≥1 case must still be killed). Both controls have n3=0, so they cannot refute an n3≥1 argument; that line needs a different control. Claim `makhnev1988-condstar-theorems`.
- **n3 finding, checked (directive 12).** All four classical λ=1 SRGs have n3=0: rook(3) T=6, doily srg(15,6,1,3) T=15, GQ(2,4) srg(27,10,1,5) T=45, BvLS T=891; disjoint triangle pairs are joined by 0, 1, or 3 edges — never 2 (rook {3:6}, doily {3:60}, GQ(2,4) {3:720}, BvLS {0:133650,1:240570,3:8910}; `code/out/n3_four_graphs.captured.txt`, claim `n3-zero-four-classical-lambda1-srgs`). The join-2 configuration is absent in the whole μ≤3-or-exception part of the family — a FINDING, not a failed search. There is NO μ=2 in-family positive control (n3≥1 IS witnessed in the μ≥4 members (81,20,1,6),(729,112,1,20), claim `bondarenko-radchenko-lambda1-gk`, but μ≠2 cannot gate a μ=2-specific argument). The kill target is therefore a FINITE SAT/CP-SAT question: does a 2-edge-joined disjoint triangle pair extend at all in a locally-7K2 μ=2 graph? (task `kill-n3-ge1-case`). This is a **sat_solver** job — spawn sat_solver (never once spawned this run), not a tool_builder counting script — and the encoder must find the join-3 and join-1 triangle pairs BvLS contains plus rook(3) outright before any UNSAT is believed.
- **n3 seed extends locally; the CONTRADICTION was a false positive (checked, directive 14).** The 2-edge-joined disjoint triangle pair is LOCALLY CONSISTENT: under the only criterion arc-consistency may soundly conclude (adjacent ≤1 common neighbour, non-adjacent ≤2, deficits satisfiable by the ~91 outside vertices), complete enumeration of the 9 free interior edges of the 8-vertex forced closure (512 assignments) finds 2 satisfying assignments — the seed extends locally (`code/out/n3_seed_consistency_ub.captured.txt`, claim `n3-seed-locally-consistent-radius1`). The earlier CONTRADICTION (`code/out/n3_local_propagation.captured.txt`, now SUPERSEDED) was an over-forcing saturation-branch bug in `code/lib/localprop.py`, not an obstruction. So NO local obstruction at this radius; the next question — at what radius, if any, does the seed stop extending — is paused by directive 16: write solution.md first (task `write-solution-md`), then return via bounded enumeration on one more shell, NOT CP-SAT (task `radius-one-more-shell-enumeration`). Zero-within-patch completions (`n3_seed_consistency.captured.txt`, 0 of 512) is NOT an obstruction — required common neighbours may sit among the other 91 vertices.
- **Makhnev Thm 2's 99-case mechanism re-derived here — n3≥1 at 99 upgraded from sourced to re-derived-here.** The forced-subgraph chain reconstructs the primary-text lemmas exactly: |Γ(A)|=39, 36 points in 12 inner triangles, 60 outside points → 20 outer triangles, 1+12+20=33 triangle-vertices partitioning all 99 points (`code/out/check_makhnev_n3_counts.captured.txt`). The forced Λ₀ = srg(33,12,1,6) is parameter-INFEASIBLE by multiplicity integrality directly — g numerator 2k+(v−1)(λ−μ) = −136 not divisible by √Δ = 7 (`code/out/check_srg33_12_1_6.captured.txt`) — a candidate strictly-simpler self-contained route than the published Thm 1 rejection (μ=6>3, not (27,10,1,5)); written up as note `research/notes/makhnev-99-shorter-proof.md`, claim `makhnev99-shorter-proof-integrality` (infeasibility step checked; lemma chain sourced, not reproved).
- **n3 is NOT arithmetically forced at 99 (checked).** The 62 Reimbayev order-6 counts are each (n,k)-term ± c·n3 (c ∈ {0,1/3,2/3,4/3,1,2,4,5,6,8,10,14}); requiring all nonneg integers admits n3=0 for every family member, residue n3≡0 (mod 3), admissible interval [0,4158] at k=14. Order-6 counting alone does not force n3≥1 at 99, and n3=0 is family-realizable (both controls). `code/out/n3_order6_feasibility.captured.txt`, claim `order6-n3-not-forced`.
- **Five-member family, checked.** Integrality of the eigenvalue multiplicities admits exactly five parameter sets for `srg(v,k,1,2)`: `(9,4),(99,14),(243,22),(6273,112),(494019,994)` — equivalently `k = u²+u+2` with `2u+1 | 63` (a = √(4k−7) = 2u+1 ∈ {3,7,9,21,63}), `u ∈ {1,3,4,10,31}` — the divisor-63 characterization, checked in `code/out/divisor63-characterization.md`. Computed in exact integer arithmetic (`code/out/feasibility-candidates-corrected.md`, claim `integrality-five-members`). **This corrects problem.md**, whose candidate list `9,33,99,243,513,969` was wrong: the five-member list won.
- **33 is excluded by integrality, checked.** `srg(33,8,1,2)` does not exist: `2k−(v−1) = −16` is not divisible by `√(4k−7) = 5`, so the eigenvalue multiplicity is non-integral (claims `srg33-does-not-exist-integrality`, `c2`). It dies on the same arithmetic test that 9, 99, and 243 all pass — so 33 gives no structural precedent against 99.
- **9 and 243 exist, checked.** `srg(9,4,1,2)` is the 3×3 rook's graph (= Paley(9)); `srg(243,22,1,2)` is the Berlekamp–van Lint–Seidel graph from the perfect ternary Golay code (claim `c4`; Brouwer's tables, van Lint 1975). `lib.srg.is_srg` confirmed both exactly — rook(3) True, bvls_graph() True with 2673 edges — recorded in `code/out/oracle-selfcheck.md`. These are the negative controls every nonexistence argument must fail on.
- **Bagchi / Brouwer–Neumaier μ=2 dichotomy does not bite at 99, sourced+reasoned.** The "grid" conclusion needs both `k < 12λ(λ+3)` and `k < (λ+1)(λ+2)`; for λ=1 the second bound is 6, and `k = 14, 22 ≥ 6`, so neither 99 nor 243 is forced to be a grid. BN1988's table marks (99,14,1) open `?` (claims `c6-resolved-no-bite`, `brouwer-neumaier-1988-99-open`).
- **Automorphism constraints, asserted-by-source.** For a putative (99,14,1,2) with G = Aut: |G| divides 2·3³·7·11 (Makhnev–Minakova 2004); if 7‖G‖ then G ≅ Z₇, and if 2‖G‖ then |G| divides 6 (Cesarz–Woldar 2025, computer-free in published form); only primes 2 and 3 can divide |G| (Behbahani–Lam 2011); no G ≅ Z₆, S₃, Z₉, E₉ (Crnković–Maksimović 2020). A nontrivial group, if any, is very small; triviality is open. Full table: `research/notes/automorphism-orders-consolidated.md`, claims `c3`, `automorphism-orders-consolidated`.

## Ruled out

Approaches that failed, and the reason each failed. A known dead end is a
result, and this section is what stops the run paying for one twice.

- **Eigenvalue-only nonexistence routes — integrality, Krein, absolute bound, whole-graph interlacing.** All of these survive on the existing graphs `srg(9,4,1,2)` and `srg(243,22,1,2)`, so an argument built on them alone proves a false statement and is refuted on arrival. Integrality does exclude 33, 513, and 969, but not 99 — it cannot be pushed further.
- **The naive "μ=2 ⇒ grid or k ≥ 48" reading of Bagchi/BN1988.** Dissolves once the second branch `k < (λ+1)(λ+2) = 6` is restored; it "proved" 243 nonexistence, which is how it was known to be wrong. See Established.
- **G-reduce part (c): the reduction does NOT recurse (checked negative).** The vertex-derived outer partial Steiner triple system's collinearity graph is not an srg(*,*,1,2): on bvls_graph() it has λ=1 but μ ∈ {0:330, 1:11880, 2:9900}, non-constant. Parts (a),(b) hold on both controls, but any 99 argument reducing to "the outer design must be its own srg" is refuted on arrival by the 243 control. `code/out/g_reduce_control.captured.txt`.
- **Order-6 counting forces n3≥1 at 99.** False. All 62 order-6 counts admit n3=0 at every family member (residue n3≡0 mod 3, interval [0,4158] at k=14), so the count identities cannot distinguish 99 from the n3=0 controls. `code/out/n3_order6_feasibility.captured.txt`.
- **The hexagon count as a standalone nonexistence route.** Closed, not dead — redirected to n3. The identity n12 = (1/12)nk(k−2)(2k²−21k+53) + n3 is exact, and both existing members attain n3=0 (checked in `code/out/hexagon_identity_verified.captured.txt`), so n3=0 is family-realizable and the C₆ count alone cannot distinguish 99. What remains live is forcing n3 itself, per Makhnev Thm 2.
- **Local obstruction for the n3 seed at the 8-vertex forced-closure radius.** False — an engine soundness bug (over-forcing saturation branch in `code/lib/localprop.py`), not a graph property. The sound capture finds 2 satisfying assignments (`code/out/n3_seed_consistency_ub.captured.txt`; note `research/notes/kill-n3-ge1-local-consistency.md`). The stale CONTRADICTION capture is annotated SUPERSEDED.

## Numbers

Computed terms, the range over which the oracle and the method agree, the size
of the object at the bound in the statement.

- Oracle self-check (`code/out/oracle-selfcheck.md`): rook(3) → srg(9,4,1,2) True; bvls_graph() → srg(243,22,1,2) True, 2673 edges; 14-regular circulant on 99 → rejected with "off-diagonal common-neighbour mismatch on 9504 entries".

## Recalled

What durable memory holds about this problem or problems of its shape, marked as
recalled rather than as this run's own finding, with hypotheses checked against
this problem before being relied on.

## Contradictions

Where sources disagree, where a source contradicts recalled memory, or where a
computation contradicts a conjecture. The most valuable rows here: record them
rather than silently picking a side.

## Gaps

What the run still needs and has not found. State a gap precisely enough to be a
research request rather than a mood.
