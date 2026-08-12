# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `CLAIMS.md` | Derived: every claim block in the notes, one row each, with whether its hypotheses hold here and what evidence stands behind it. Rewritten on every research write; do not edit. |
| `FRONTIER.md` | Derived: leads harvested from the citations inside every downloaded document (ranked by how many library sources cite each; struck-through = already in library). A row is a lead, not a recommendation; nothing here is judged. Rewritten on each download; do not edit by hand. |
| `L1.0/oeis_a001006.md` | Motzkin numbers A001006 lookup note (g.f., D-finite recurrence, closed form). Establishes D(N) is NOT Motzkin (diverges at n=2). Kills the Motzkin closed-form candidate for D(N). |
| `L1.0/oeis_a005207.md` | Fibonacci-family lookup note ((F(2n-1)+F(n+1))/2 sequ; diverges from D(N) at n=2). Rules out a Fibonacci closed form for D(N). |
| `L1.0/oeis_a007902.md` | A007902 (pebbling configurations) = the run's 2D amoeba sequence D_2D(N), matched on every term (D_2D(N)=A007902(N+1)). Names the 2D analogue: no closed form, only asymptotics (~2.32^n) and a memoized G(k,m) recurrence. Not the 3D D(N). Claim d2d-equals-a007902. |
| `L1.0/oeis_a055999.md` | OEIS A055999 (a(n)=n(n+7)/2 quadratic) lookup note. Hit: the PE763 max-level column Q_2(N)=R(N,N-2)/3^(N-5) equals A055999(N-5)=(N-5)(N+2)/2 exactly for N=6..14, confirming the Q_2 closed form from a catalogued sequence. Source https://oeis.org/A055999. |
| `L1.0/oeis_a074171.md` | OEIS A074171 (a(1)=1,a(2)=3 then n(n+7)/2, 'essentially A055999') lookup note. Matched only as a sibling of A055999, which gives the run's Q_2(N)=(N-5)(N+2)/2 max-level-column closed form on N=6..14. Source https://oeis.org/A074171. |
| `L1.0/oeis_a086246.md` | Motzkin-variant lookup note ((1+x-sqrt(1-2x-3x^2))/2 sequ). Not D(N); a ruled-out closed-form family candidate. |
| `L1.0/oeis_a134227.md` | OEIS A134227 ((n-1)(n+6)/2 + [n=1], 'essentially A055999', row sums of A134226) lookup note. Sibling of A055999/A074171 in the n(n+7)/2 family; the run's Q_2(N)=(N-5)(N+2)/2 identification uses A055999. Source https://oeis.org/A134227. |
| `L1.0/oeis_a168049.md` | _(undescribed)_ |
| `L1.0/oeis_direct.md` | _(undescribed)_ |
| `L1.0/oeis_partial.md` | _(undescribed)_ |
| `L1.1/oeis_a186085.md` | _(undescribed)_ |
| `L1.1/oeis_a383891.md` | _(undescribed)_ |
| `L1.1/oeis_a392317.md` | _(undescribed)_ |
| `L2.0/L1.0.md` | _(undescribed)_ |
| `L2.0/cgmo_opening_dijkstra.md` | _(undescribed)_ |
| `L2.0/pebbling_amz.md` | _(undescribed)_ |
| `L2.0/pebbling_ejc_survey.md` | Complete structural digest of the EJC chessboard-pebbling survey (Eriksson, EJC 2 (1995) #R7) — the pivotal source: n-dim weight, voidance bijection (Prop 20), polyominoids + Catalan, 2D crossing subtlety & GFs, n>=3 folded-polyominoid four-way bijection (Thm 9), minimal-unavoidable structure, Fig.3 table. Verified against the full text research/L0.0/pebbling_ejc_survey.full.md incl. Fig.3 (col n=2 = Catalan, row k=2 = n(3n-1)/2) re-checked by hand. |
| `L2.0/pebbling_eriksson_eljc.md` | _(undescribed)_ |
| `L2.0/pebbling_knessl_pdf.md` | _(undescribed)_ |
| `THREADS.md` | Derived: every direction of attack under research/threads/, what each rests on, and why the dead ones died. Rewritten on every research write; do not edit. |
| `amoeba2d_pebbling_a007902.md` | _(undescribed)_ |
| `amoeba_seq_oeis.md` | _(undescribed)_ |
| `inventor_confirm_checklist.md` | _(undescribed)_ |
| `inventor_proposal_collapse.md` | _(undescribed)_ |
| `oeis_lookup_2d_3d.md` | _(undescribed)_ |
| `pebbling_structure_3d_ladder.md` | The sourced structural characterization ladder: 2D reachable positions = polyominoids via voidance sets (Eriksson Props 7,8,20), 2D crossing subtlety (Thm 10, GF growth 4.112), and for n>=3: positions = voidance sets = folded polyominoids, no cell played twice (Thm 9, Prop 24), plus the G(k,m) recurrence, contour formula and asymptotics for A007902. Names the correct counting object for 3D D(N) (folded 3-labelled polyominoids). Carries the two structural claim blocks. |
| `scholar_report.md` | Verification pass report over the research library: re-checked each primary-source digest against its full text (CGMO lemmas/theorem, Zhen-Knessl recurrence/contour/asymptotics, Eriksson Thm 9/Prop 24/Fig.3 which was verified by hand), fixed the stale 'placeholder' index rows, and confirmed no contradiction with MEMORY.md values. Records what remains lacking: a 3D recurrence/DP reaching N=10000. |
