# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `_exec_review.py` | _(undescribed)_ |
| `brute.captured.txt` | _(undescribed)_ |
| `brute.recheck.captured.txt` | _(undescribed)_ |
| `c10d4.txt` | _(undescribed)_ |
| `c7d3.txt` | _(undescribed)_ |
| `c8d3.txt` | _(undescribed)_ |
| `c9d3.txt` | _(undescribed)_ |
| `c_seq.txt` | _(undescribed)_ |
| `check_barber_balanced.py` | Brute-force oracle (n=2..5) that computes the true maximum balanced independent set of Q_n and compares against Barber's two transcribed constant versions, settling the transcription contradiction. Must be run by a coder/tool_builder — scholar has no shell. |
| `check_barber_balanced2.py` | Superseded duplicate of the Barber balanced-set oracle; kept only for provenance. |
| `check_clifford_extremal.py` | _(undescribed)_ |
| `check_interlacing.py` | Verifies the linear-algebra technique behind a max-degree lower bound on the cube: signed adjacency with A'^2 = nI, and spectral interlacing forcing a >half principal submatrix to have an eigenvalue >= sqrt(n). |
| `check_nd.py` | _(undescribed)_ |
| `check_oeis_vs_f.py` | Cross-checks that the four OEIS sequences fetched by lookup (A002264, A003056, A053251, A202453) do not equal f(n)=ceil(sqrt(n)) on n=1..20, so earlier scholar term-comparison can be confirmed machine-side. |
| `check_seq.py` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `delsarte_lp.py` | _(undescribed)_ |
| `delsarte_lp_correct.captured.txt` | _(undescribed)_ |
| `delsarte_lp_correct.py` | Correctly-posed Delsarte/Krawtchouk LP minimising average internal degree a_1 over the distance-distribution polytope of H(2,n) at size 2^{n-1}+1. Returns LP value (best lower bound on f(n) from averaging) for n=1..8; exact-rational coefficients fed to HiGHS. Established correct: valid lower bound since a_1(S)=avg-deg(S)<=D(S) for every S and the LP relaxes the feasible set; cross-checked against real-set average degrees. Produced code/out/delsarte_lp_correct.captured.txt.  The Delsarte police is the canonical strongest averaging/eigenfunction bound; values decay to 0 exponentially, confirming the averaging route cannot reach sqrt(n) or log n. |
| `delsarte_lp_finding.md` | The executed result writeup: correctly-posed Delsarte/Krawtchouk LP min average-internal-degree = 1,1,3/4,1/2,5/16,3/16,7/64,1/16 for n=1..8, decaying to 0 exponentially. Confirming quantitatively that no averaging/edge-counting method can reach sqrt(n) or log n; hence the known bounds must come from a non-averaging mechanism producing a maximum directly. Also records that the Clifford 'parity class + one vertex' conjecture is refuted by the exact n=4 witness. |
| `delsarte_lp_verify.captured.txt` | _(undescribed)_ |
| `delsarte_lp_verify.py` | Independent verification of the Delsarte LP finding: exact edge-counting a1(S)=2e(S)/M for the even-weight set + vertex 1, showing the LP value (a valid lower bound on f(n)) decays to 0 and is essentially tight against real sets (LP <= a1 in every n, both -> 0). Run output in code/out/delsarte_lp_verify.captured.txt. |
| `extend_f_exact.captured.txt` | _(undescribed)_ |
| `extend_f_exact.py` | _(undescribed)_ |
| `f-exact-1..5-note.md` | _(undescribed)_ |
| `f-exact-note.md` | _(undescribed)_ |
| `f5_independent.captured.txt` | _(undescribed)_ |
| `f_exact_verify.captured.txt` | _(undescribed)_ |
| `first_step_exact_value.py` | First step of adopted approach: decide via the existing ILP oracle whether { |
| `fmax_driver.captured.txt` | _(undescribed)_ |
| `ground_approaches.captured.txt` | _(undescribed)_ |
| `ground_approaches.py` | Grounded the inventor approaches: (1) Delsarte/Krawtchouk LP for min average internal degree and (2) the Clifford 'parity-plus-one' structural claim. NOTE: the LP in this file is degenerate (missing the sum a_i = M constraint, giving a1=0 everywhere) — superseded by delsarte_lp_correct.py which poses the LP correctly. Run output in code/out/ground_approaches.captured.txt confirms the correct LP is needed (this file gave 0.0, corrected file gives the true values). The parity-plus-one check here is valid: witness is parity-plus-one = False. |
| `huang_spectral.captured.txt` | Captured full output of code/spectral_verify.py: exact A_n^2==n*I+support (n=1..8), spectrum +-sqrt(n) (n=2..10), interlacing lambda_max>=sqrt(n) for random |
| `huang_spectral.confirmation.md` | _(undescribed)_ |
| `huang_spectral_verified.md` | Durable claim blocks for the mechanically verified Huang spectral lower bound f(n) ≥ √n, plus the synthesis claim f(n) = Θ(√n). |
| `indep_research_check.py` | _(undescribed)_ |
| `independent_review_huang.py` | _(undescribed)_ |
| `pattern_extend.captured.txt` | _(undescribed)_ |
| `pattern_extend.py` | _(undescribed)_ |
| `pattern_n8.log` | _(undescribed)_ |
| `pattern_report.md` | Pattern-finder report: f(n)=1,2,2,2,3,3,3 = ceil(sqrt(n)) for n<=7 (exact), the Delsarte LP closed form n/2^{n-1} (verified, decays to 0), and the flatness of extremal sets. Details which regularities are proved versus conjecture, and flags the spurious order-3 recurrence that the 7th term falsified. |
| `research_independent_verify.py` | _(undescribed)_ |
| `run_barber_check.sh` | Wrapper to run the Barber balanced-set oracle with a 540s timeout and captured output. |
| `run_ground.sh` | _(undescribed)_ |
| `run_independent_review.sh` | _(undescribed)_ |
| `run_oeis_check.sh` | _(undescribed)_ |
| `run_review.sh` | _(undescribed)_ |
| `run_verif.sh` | _(undescribed)_ |
| `scholar_verify_chain.py` | Fresh independent duplicate of the spectral verification; NOT RUN in this session (scholar has no execution tool). Kept only to record that the independent check was attempted; the authoritative runs are huang_spectral.captured.txt and verify_interlacing_chain.captured.txt. |
| `scholar_verify_huang.py` | Independent exact machine check (n=1..7) of the three lemmas behind f(n)>=sqrt(n): A_n^2=nI on integer block matrices, spectrum ±sqrt(n), interlacing on random (2^{n-1}+1)-row principal submatrices, edge-support. Queued for coder (no execution tool in scholar). |
| `tmp_run3.py` | _(undescribed)_ |
| `verify_barber_balanced.README.md` | Run instructions for verify_barber_balanced.py (brute force of max balanced independent set of Q_n); leftover to be executed by a runner for n=4,5. |
| `verify_barber_balanced.note.md` | Resolution note (with claim block) of the Barber balanced-independent-set odd-n formula /2 contradiction in the library: hand-check at n=3 proves the 2^{n-1}-2^{n-2}(n-1)/2 form, refuting the prose transcription 2^{n-1}-2^{n-2}(n-1). Not load-bearing for D(S). |
| `verify_barber_balanced.py` | Brute force of the max balanced independent set of Q_n (equal even/odd parity counts, independent) for n=2..4, to resolve which transcription of Barber's odd-n formula (with or without the /2) is correct; the hand-check at n=3 found the /2 form right. |
| `verify_interlacing_chain.captured.txt` | _(undescribed)_ |
| `verify_interlacing_chain.py` | Exact integer verification of the Huang spectral-interlacing chain: builds A_1=[[0,1],[1,0]], A_n=block[[A_{n-1},I],[I,-A_{n-1}]]; checks symmetry, {0,±1} entries, zero diagonal, A_n^2=n*I exactly, support=edges of Q_n (n=1..8); checks λ_max(B)>=√n for S=even-weight+one odd ( |
| `verify_interlacing_summary.md` | _(undescribed)_ |
