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

## Current direction

Directive 6 (steer), as sharpened by directive 7: stop proposing approaches; **execute** the adopted root-difference-coloring approach. The first step is already *written* (`code/rootdiff/verify_rootdiff_identity.py`) and must now be **run as-is** (do not rewrite; use the rootdiff copy, not the stale `code/refute/verify_rootdiff_identity.py` draft), captured to `code/out/rootdiff_identity.captured.txt` — that capture does not yet exist. The script reports on both identities (A) H_i(f)(x) = e_{n−i}(x−β_1,…,x−β_n) and (B) R_i = ∏_β H_i(f)(β), over QQ (n=4,5,6) and over F_p (n=p+1, p=2,3,5), plus the char-p break table for x^{p+1}−x^p; its docstring states the failure criterion verbatim, and the verdict must be reported against that criterion rather than restated. Char-p break test (`rdc-charp-break`) runs immediately after. **Nothing else starts until that capture exists.** The inventor's last call (245 s, ~18k output tokens) ran under this freeze: any approach it proposed is out of scope and deferred, not adopted. The refuter has been redirected from settled `ca_deg4_char3.p` to an adversarial reading of the rootdiff script. See TASKS.md: rdc-identity-first-step → rdc-charp-break → mason-stothers-decision.

## Established

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it.

- **CA is open; the smallest open degree is 20, not 30** (sourced). Castryck–Laterveer–Ounaïes 2012 settle d=12 and call d=20 "the next open case"; Schaub–Spivakovsky 2024 repeats n=20; Wikipedia (held) agrees. This corrects `problem.md`'s "30". → `research/ROOT.md` (Verification bound), `research/notes/casas-alvero-status.md` (`smallest-open-degree`).
- **A complete proof has been claimed but is unverified** (sourced). Ghosh, arXiv:2501.09272 (v1 16 Jan 2025; v2 21 Mar 2026 "Major revisions") claims CA for all d≥3 in char 0, via Koszul homology + a downward induction with a ℂ-only Brouwer-degree step. It is a preprint: not peer-reviewed, not independently validated, not withdrawn; the refereed 2024–25 sources still treat CA as open. → `research/notes/casas-alvero-status.md` (`ca-status-2025`, `ghosh-v2-version-record`), `research/summaries/ghosh2025_proof_html.md`.
- **Minimal-counterexample constraints** (Laterveer–Ounaïes, arXiv:1204.0450; sourced). A non-trivial CA polynomial of degree N has ≥5 distinct roots (so N≥6), ≥4 in its open Gauss–Lucas hull; ≤4 distinct roots ⇒ CA; a root of multiplicity ≥N−2 ⇒ pure power; the shared-root set {α_1,…,α_{N−1}} cannot have size 2. → `research/summaries/laterveer_ounaies_constraints_2012.md`.
- **Verification bound** (sourced). Degree ≤7 by Gröbner over ℚ (Diaz-Toca–Gonzalez-Vega 2006), 8 (same authors); d=12 settled by Castryck et al 2012 via scenario reduction + reduction-mod-p + Gröbner in char p (~3 weeks, ~90 GB RAM per scenario, 5 scenarios); d=20 judged "utopic" for that method. → `research/ROOT.md`, `research/notes/casas-alvero-status.md` (`computational-boundary`).
- **CA is false in characteristic p** (sourced, and confirmed by the oracle). x^{p+1}−x^p over 𝔽_p is a CA polynomial that is not a pure power. The canonical oracle reports is_ca=True / is_pure_power=False for p=2,3,5,7 — the negative control that proves the checker measures the right thing. → `research/notes/casas-alvero-status.md` (`charp-false`, `charp-witnesses`), `code/out/oracle_guard.captured.txt`.
- **The canonical oracle** (computed & checked). `code/lib/casas_alvero.py`: `is_ca` / `is_pure_power` / `is_counterexample`, exact over ℚ or 𝔽_p via sympy; char-p zero derivatives handled (gcd(f,0)=f). All guards pass: (x−1)^n n=1..8 over ℚ; random deg-5 fails; char-p witnesses are counterexamples; x^n over 𝔽_p is a pure power. → `code/lib/INDEX.md`, `code/out/oracle_guard.captured.txt`.

## Ruled out

Approaches that failed, and the reason each failed. A known dead end is a
result, and this section is what stops the run paying for one twice.

## Numbers

Computed terms, the range over which the oracle and the method agree, the size
of the object at the bound in the statement.

- **SNF minors criterion: feasible at n=4, infeasible at n=5 (measured).** n=4: 19×15 matrices, all 64 tuples, milliseconds (lcm J_T = 1575 → {3,5,7}). n=5: 195×120 matrices, 5^4=625 tuples; a single SNF did not finish within a 90 s cap (`code/out/commands.log`, final command). Route abandoned for n=5 in favour of rank over F_p (`lib.badprimes.rank_mod_p`, `rank_{F_p}(M_T) < 120`). → `research/threads/computational-boundary.md`, task `badprimes-n5-rank-mod-p`.

## Recalled

What durable memory holds about this problem or problems of its shape, marked as
recalled rather than as this run's own finding, with hypotheses checked against
this problem before being relied on.

## Contradictions

Where sources disagree, where a source contradicts recalled memory, or where a
computation contradicts a conjecture. The most valuable rows here: record them
rather than silently picking a side.

- **Bad-prime capture contradicted the published lists and the run's own oracle — ordinary vs Hasse derivatives — RESOLVED.** `code/out/badprimes_sn.captured.txt` now ends ALL CHECKS PASSED: the S_n route under the **Hasse** formulation gives n=3 → {2} and n=4 → {3,5,7}, matching the published lists exactly (all 17 primes p<60, plus bounded F_p enumeration via `is_ca_hasse`). The published lists use **Hasse** derivatives (Castryck 2012 Def 1, `research/sources/castryck2012_degree12_html.full.md:129`; Schaub–Spivakovsky 2023, lines 50-53): p=2 is *good* for n=4 (H_2(x^4+x^2)=1) but *bad* for n=3. The ordinary-derivative convention (sympy `.diff`, `is_ca`) degenerates for p<n (i! = 0, derivatives vanish identically, hypothesis vacuous) and wrongly marks p=2 bad for n=4. The two conventions agree in char 0 (agreement guard 64/64) and for p≥n. The charp-witness-xpp1-xp clause "f(X^p) without constant term works since all derivatives vanish" is ordinary-only and does not survive Hasse (checked, two routes). → `code/lib/casas_alvero.py` (`is_ca` vs `is_ca_hasse`), `research/threads/hasse-vs-ordinary.md`, `research/notes/ordinary-vs-hasse-badprimes.md`, `code/out/ordinary-vs-hasse-charp-witness.md`.

- **Open-degree comparison resolved.** The inverted comparison in `scenario/verify_open_degrees.py` (it flagged `pub != cov` as a mismatch) is fixed; `scenario/verify_open_degrees_check.py` asserts the old comparison falsely flags n=16, 20, 28. Downstream conclusions were re-derived in `research/patterns/open_degree_complement_and_sequences.md`, leaving two genuine discrepancies: n=98 (covered by 2p^k, yet listed open) and n=96 (open via p=2 bad for degree 6, yet omitted from the published list). The `smallest-open-degree = 20` claim was unaffected throughout (sourced, not from the script).

## Gaps

What the run still needs and has not found. State a gap precisely enough to be a
research request rather than a mood.
