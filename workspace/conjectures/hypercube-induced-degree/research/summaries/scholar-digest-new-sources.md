# Scholar digest — the three new library sources, cross-checked against recalled memory

Scholar's independent reading of the three sources the librarian added, against
what the run already holds (exact f(1..5)=1,2,2,2,3 = ceil(sqrt(n)); the spectral
re-derivation f(n) >= sqrt(n); the obstruction that isoperimetric/influence
methods bound only average/outer-boundary quantities).

## Liu–Zhou (Eigenvalues of Cayley Graphs, doi:10.37236/8569) — USEFUL, confirms
Plain adjacency spectrum of Q_d: eigenvalues d−2i, mult C(d,i), largest = d.
This is the one genuinely useful distinction it adds: it isolates that the
sqrt(n) cannot come from the plain adjacency (whose largest eigenvalue is d),
only from the SIGNED matrix A_n (A_n²=nI, ±sqrt(n)). Recalled memory already
asserted the signed-matrix proof; this source backs the "base spectrum" against
which the sign construction is consistent, and rules out the reading that the
plain spectrum already gives sqrt. Confirms, does not contradict.

## Barber (arXiv:1210.4029) — USEFUL for extremal structure, one edge-case catch
Max independent sets of Q_n are exactly the two parity classes (each 2^{n-1});
every other independent set is smaller. Consequence the run already used:
S of size 2^{n-1}+1 is a parity class plus one crossing vertex (internal degree n).
The balanced-independent-set formula, as transcribed, is WRONG at its small-n
edge (n=2 gives 2 = 2^{n-1}, contradicting "strictly smaller for n>1"; the true
max balanced independent set of Q_2 is 0). General statement holds from n=3;
only the small-n constant needs source confirmation. Flagged, not silently trusted.

## Ellis (CPC 2011) — DOES NOT HELP, confirms obstruction only
Edge-isoperimetric extremal sets are subcubes, with a quantitative stability
bound. This is again an OUTER/boundary quantity; it does not bound the maximum
internal degree D(S). It constrains the A-side extremal structure (subcube/
parity-layer) and cross-checks Barber–Erde, but adds nothing to the max-degree
question. Same verdict as all the isoperimetric/influence sources.

## Cross-source consistency
No source contradicts the run's durable findings. All three agree with the
parity-class + one-vertex picture and with the spectral closure of the sqrt
lower bound. The contradiction that dominates this run is not source-vs-source
but source-vs-framing: `problem.md` states the gap is open "thirty years",
while the run's spectral re-derivation closes f(n) >= sqrt(n) from below. The
new sources do not reopen that or change the residue (exact f(n) for non-square
n, the un-citeable upper construction).

## Verification status
Claims from all three sources remain `status: asserted-by-source` — the scholar
role has no shell, so `code/verify_new_sources.py` (Liu-Zhou spectrum d=2..7,
Barber parity brute force n=2..4, Ellis subcube-extremality spot-check) is
written but NOT run. A runner (coder/tool_builder/sat_solver) must execute
`timeout 540 python3 code/verify_new_sources.py | tee code/out/verify_new_sources.captured.txt`
before any of the three is promoted to checked. Until then they are taken on
the source's word, as CLAIMS.md already records them.
