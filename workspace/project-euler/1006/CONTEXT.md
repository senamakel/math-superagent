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

- **Problem statement** (sourced: `problem.md`, official PE minimal page,
  https://projecteuler.net/minimal=1006 — nothing here derives from it yet).
  $S_0=0$, $S_1=01$, $S_n=S_{n-1}S_{n-2}$ for $n\ge2$. A *Fibonacci subword* is
  a contiguous substring of some $S_n$. For each $k$ there are exactly $k+1$
  distinct subwords of length $k$; read as decimal numbers ignoring leading
  zeros, $\Psi(k)$ = sum of their squares. **Worked oracle values from the
  statement:** length-3 subwords are $001,010,100,101$, so
  $\Psi(3)=1^2+10^2+100^2+101^2=20302$; given $S_2=010$, $S_3=01001$,
  $S_4=01001010$; given $\Psi(10)\equiv10699667\pmod{101001001}$; target
  $\Psi(10^{18})\bmod101001001$. All oracle values are **recomputed
  in-container** by `code/brute.py` (verified in `GOAL.md`: Ψ(3)=20302,
  Ψ(10)≡10699667, factor count k+1 for k=1..20).
- **Modulus arithmetic** (computed by inspection, trivial): $M=101001001$ is
  odd and $\not\equiv0\bmod5$, so $\gcd(10,M)=1$ and $10$ is invertible mod
  $M$; directive 2 additionally asserts $M$ prime (asserted, unverified).
- **Workspace state** (surveyed this cycle): the plan on disk is
  `GOAL.md` (precise restatement + verified oracle), `code/brute.py`
  (oracle, verified), `code/mech/mech_psi.py` (mechanical construction,
  == brute k≤400), `research/threads/mechanical-word-floor-sum.md`
  (primary route, carries the directive-4 spec verbatim), and the ledgers;
  `code/solution.py` holds the four phases with Phase 3 marked out of domain.
  Cognee is empty for PE1006/Fibonacci-subword queries (recall_memory and
  recall_scratch both returned nothing).

## Asserted but unverified — the steering directives

`config/directives.jsonl` (see also `config/.directives-cursor`) carries the
steer directives that pre-empt the derivation. Each claimed verification
outside the container without in-workspace evidence at arrival; treat each as a
hypothesis until reproduced in-container. The mechanical-word core of
directives 1-2 is now in-container verified (`mech_psi` == brute k≤400);
directive 6's new anchors are not yet (task `directive-6-anchors`).

1. **Pair-correlation route**, valid at $k=F_n-1$ (directive 1): the $k+1$
   factors are rotations of the standard word $q_n$ truncated to $k$ letters;
   writing $\Psi(k)=\sum_{j,jp} C(j,jp)\,10^{2k-2-j-jp}$, one has
   $C(j,jp)=A(jp-j)$, the cyclic autocorrelation of $q_n$, with closed form
   $A(d)=\max(0,m-t)+\max(0,m-(N-t))$, $N=F_n$, $m=\#\text{ones in }q_n$,
   $t=(dm)\bmod N$. The inner sum over $j$ is geometric, so $\Psi$ becomes one
   lag-sum with geometric weights, and the remaining object
   $\sum_d (ad\bmod N)\,x^d\bmod M$ is evaluable by a Euclidean/Ostrowski
   recursion in $O(\log N)$.
2. **Mechanical-word route for all $k$** (directive 2 — stronger; read it
   before choosing, and it subsumes 1): with rational slope
   $a=F(n-1)/F(n)$ for any $F(n)\gg k$, cut the unit circle at the $k+1$ points
   $\mathrm{frac}(-ma)$, $m=0..k$, take each arc midpoint $x$, and set
   $\mathrm{digit}_j(x)=\lfloor x+(j+1)a\rfloor-\lfloor x+ja\rfloor$. With
   $v(x)=\sum_j \mathrm{digit}_j\,10^{k-1-j}$, telescoping gives
   $v(x)=\lfloor x+ka\rfloor-10^{k-1}\lfloor x\rfloor+
   9\sum_{j=1}^{k-1}10^{k-1-j}\lfloor x+ja\rfloor$; $\Psi(k)$ is the second
   moment of this geometrically weighted floor sum over the $k+1$ reps. The
   primitive is the **universal Euclidean algorithm** (monoid generalisation of
   AtCoder `floor_sum`, aka Chtholly's algorithm) carrying the tuple
   $(\text{count},\sum x^j,\sum x^j\lfloor\cdot\rfloor,\sum x^j\lfloor\cdot\rfloor^2)$
   mod $M$ with $x=10^{-1}\bmod M$ — $O(\log)$ per evaluation. Directive 2
   reports checks at $k=3,5,8,10,13,17,21,26,34,40,55$; both directives were
   checked at $n=3..12$ (dir. 1).
3. **Directive 3 (steer) — Phase 3 is out of scope.** The identity
   $C(j,jp)=A(jp-j)$ of directive 1 holds ONLY at $k=F_n-1$
   ($k=1,2,4,7,12,20,33,54,88,143,\dots$); the Phase-3 failures in
   `code/out/solution_checks.md` at $k=3,200,10^4$ tested outside that domain
   and are expected, so the identity is NOT to be weakened or rewritten — just
   re-tested at $k=F_n-1$. The primary route does not use Phase 3: Phase 2 (the
   telescoped $v$ of directive 2) already passes against brute at $k=1..150$
   and is load-bearing. The remaining work is the universal-Euclidean second
   moment.
4. **Directive 4 (steer) — build the universal-Euclidean O(log) monoid NOW.**
   Toeplitz defects and extension-recurrence residues are off the critical
   path. Spec: lattice path of $y=(p t+q)/r$, $t=1..n$ (R step per unit $t$,
   U step per unit $\lfloor y\rfloor$), split by the Euclidean recursion as in
   AtCoder `floor_sum`, O(log) merges; node carries $dR,dU,w=z^{dR}$, $S_0=\sum
   z^t$, $S_1=\sum z^t\lfloor y\rfloor$, $S_2=\sum z^t\lfloor y\rfloor^2$ mod
   $M$; composition $S_0=l.S_0+l.w\,r.S_0$; $S_1=l.S_1+l.w(r.S_1+l.dU\,r.S_0)$;
   $S_2=l.S_2+l.w(r.S_2+2\,l.dU\,r.S_1+l.dU^2 r.S_0)$; identity zeros, $w=1$.
   The $dU$ shifts carry floor values across segment boundaries — the one place
   the primitive goes wrong. **Acceptance tests in order, none skipped:** (1)
   $S_0$ vs direct loop, random $(p,q,r,n,z)$; (2) $S_1$ vs plain floor_sum at
   $z=1$ and vs direct loop at $z\ne1$; (3) $S_2$ vs direct loop; (4) the
   directive-2 telescoped $v$ through the primitive vs `code/mech/mech_psi.py`
   at $k=1..150$ and vs $\Psi(10)\equiv10699667$; (5) match the VALID
   general-$k$ direct values at $k=1000,10000$ exactly and in negligible time —
   the old Phase-4 anchors are refuted (see Contradictions) and are not the
   gate. Only after (5) run $k=10^{18}$ with a Fibonacci approximant
   $F(n)>10^{18}$, and confirm stability across two different approximants.
5. **Directive 5 (steer) — sequencing on G4.** Write and RUN the evaluator
   (`code/lib/ueuclid.py`) in Python FIRST; formalise it in Lean only after it
   reproduces the anchors. Acceptance tests 1–3 (S0/S1/S2 vs direct loops) post
   numbers this cycle, then 4 and 5; only a checked `.lean` file closes the
   attempt. A formal statement of a primitive whose arithmetic was never
   executed can be internally perfect and still evaluate to the wrong residue,
   so the executable gate precedes Lean.
6. **Directive 8 (steer, this cycle) — primitive sound; run 1–3, then the
   reduction.** `code/lib/ueuclid.py` is CORRECT and O(log), verified outside
   the container on a copy (30 random trials p,q,r≤1e6, n≤3000, random z:
   ueuclid == ueuclid_direct == plain loop on S0/S1/S2, dR=n,
   dU=floor((p·n+q)/r), zero failures; scaling ueuclid(514229,3,1346269,10^18,
   inv10) = 0.3 ms, dU=381966011250351898 = 10^18/φ² to the digit). This is
   ASSERTED steering, not an in-workspace claim. Run tests 1–3 to record the
   numbers on our own record (code/out/ueuclid_acceptance.txt) but do NOT spend
   a cycle debugging a primitive without one. Then move to the reduction
   (supersedes directive 7's "not the Psi evaluation this cycle"): wire mech_psi
   formulation (B) through the monoid, check Psi(k) k=1..150 and Psi(10)=
   10699667, then anchors 34432237/20938836, then k=10^18 with two Fibonacci
   approximants confirmed to agree. THE HAZARD the reduction must pin first:
   S1/S2 are indexed with the segment's first R step at weight z^0, so an
   off-by-one in which power of 10 the j-th digit carries passes every monoid
   test but gives a wrong answer — pin it against mech_psi at SMALL k before
   trusting any large k.
6. **Directive 6 (steer) — anchors corrected.** 16242174 / 77578256 are
   invalid (confirmed: they came from the Phase-3 collapse) and are DISCARDED
   as acceptance criteria. New anchors, recomputed outside the container by the
   independent route (every distinct length-$k$ window of the Fibonacci word
   read as a decimal, prefix length $k+\mathrm{NextFib}(k)-1$ with NextFib the
   least Fibonacci STRICTLY greater than $k$, squares summed mod $M$,
   de-duplicated by residues under two moduli with the distinct count asserted
   to equal $k+1$): $\Psi(10^4)\equiv34432237$ (count $10001$),
   $\Psi(10^6)\equiv20938836$ (count $1000001$). That route reproduces
   $\Psi(3)=20302$ and $\Psi(10)=10699667$ and agrees with a bound-free brute
   oracle over $k=1..120$. Acceptance order for the evaluator: $k=1..150$, then
   $10699667$, then $34432237$, then $20938836$, then $10^{18}$. Strictness
   trap: with a NON-strict NextFib the prefix is one Fibonacci short whenever
   $k$ is itself Fibonacci — $k=3$ then yields $10101$ with only 3 of the 4
   factors. Checked this cycle: `code/lib/fibword.py` `next_fib` is STRICT
   (`bisect_right`), so the trap is not live.
7. **Directive 7 (steer, this cycle) — stop re-verifying settled ground; write
   `code/lib/ueuclid.py` NOW.** The task has been top for three cycles while
   cycles went to source curation, reading, and re-running `brute.py` (already
   validated, tells us nothing new). This cycle's whole deliverable is the file
   + acceptance tests 1–3 pass/fail counts to `code/out` — not Ψ(10^18), not
   Lean, not more sources. If the Euclidean recursion is the hard part, land
   the O(n) DIRECT version of the same monoid FIRST under the same interface
   and prove the composition rule correct against a loop; then the recursion is
   a drop-in replacement with a test that already exists to catch it. Minimum
   file content: node (dR,dU,w,S0,S1,S2) ints mod M; compose per directive 4;
   identity zeros with w=1; `ueuclid(p,q,r,n,z)` via Euclidean split, O(log);
   run against a direct loop for ≥20 random (p,q,r,n,z) with n in the low
   thousands; post pass/fail to code/out.
8. **Directive 9 (steer, this cycle) — the contiguous-window prefix route
   avoids the O(k)-intercept obstruction; check its three claims against
   mech_psi first.** The joint-monoid double-sum of `psi-to-ueuclid-reduction.md`
   fights an O(k) distinct-intercept term (one intercept per l). Directive 9
   replaces it: (1) the $k+1$ DISTINCT length-$k$ factors = exactly the $k+1$
   CONTIGUOUS windows at positions $r=F_n-k-1..F_n-1$ of the doubled standard
   word $q_n q_n$, as sets (k=3: windows of $0100101001$ are $010,100,001,010,
   101$, last four distinct, $20302$), so $\Psi(k)=\sum v_r^2$ over that range —
   no multiplicity, no de-dup, no O(k)-intercept l-sum; (2) $\Psi(k)$ = (full
   cyclic sum over all $F_n$ windows) − (sum over the FIRST $F_n-k-1$ windows);
   (3) the full cyclic sum $=\sum_{j,jp}A(jp-j)10^{2k-2-j-jp}$, $A$ the cyclic
   autocorrelation of $q_n$, for ANY $k<F_n$ — directive 1's identity was never
   restricted to $k=F_n-1$ as a statement about the CYCLIC sum, only about that
   sum equalling $\Psi$, which claim 2 corrects. Claim 3's lag-sum
   $\sum_d(ad\bmod N)x^d$ is the universal-Euclidean/Ostrowski recursion — the
   primitive of directive 4 serves it. The one new object is the partial sum of
   $v_r^2$ over the prefix window range via $v_{r+1}=10v_r-y_r10^k+y_{r+k}$,
   state $(v,\sum v^2,\sum v,1)$ as a constant-size transfer matrix over the
   pair $(y_r,y_{r+k})$, collapsed by Fibonacci-block renormalisation (~87
   blocks at $10^{18}$). ALL THREE claims are ASSERTED (steer), not
   established — check each against `code/mech/mech_psi.py` BEFORE building on
   it (see thread `directive9-contiguous-window-prefix`). Acceptance unchanged:
   k=1..150, $\Psi(10)=10699667$, anchors 34432237/20938836, then $k=10^{18}$
   stable across two approximants.

10. **Directive 10 (steer, this cycle) — no lean_scribe/lean_prover until the
    anchors are reproduced; the Python-before-Lean ordering is now BINDING.**
    Three consecutive cycles spent themselves in the Lean arm at this exact
    junction (103 of the last events lean_scribe, probes like a bare
    `#check Fib`, no file written, neither anchor reproduced). Directive 5 had
    already ordered Python before Lean and the Lean task was marked
    blocked-by the primitive, but the roles were still being spawned — so
    directive 10 makes it a **hard gate: no lean_scribe or lean_prover run is
    to be spawned until `code/out` holds a captured file showing
    $\Psi(10^4)=34432237$ and $\Psi(10^6)=20938836$ recomputed inside the
    container.** The Lean work is NOT cancelled (the attempt still closes with
    a checked `.lean` file); it is deferred behind two numbers. What takes the
    cycle instead, in order: (1) wire formulation (B) of
    `code/mech/mech_psi.py` through `code/lib/ueuclid.py` (built, verified on current code per directive 11 — in-container record pending the module `__main__` run);
    (2) reproduce $\Psi(k)$ k=1..150 and $\Psi(10)=10699667$ through
    that wiring; (3) reproduce the two anchors and capture them to
    `code/out`; (4) run $k=10^{18}$ under two Fibonacci approximants and check
    they agree. Directive 9 removed the O(k)-intercept obstruction (the $k+1$
    distinct factors are the contiguous windows at $r=F_n-k-1..F_n-1$, so no
    dedup and no multi-intercept sum); its three claims **stand — the refuter
    posted no counterexample to any of them** — and are to be checked against
    `mech_psi` as part of step (1).

## Ruled out

- **Published-answer search** — ruled out by policy; searching for a PE1006
  answer or forum solution invalidates the run.
- **Phase 3 (Toeplitz collapse) as a general-k method** — refuted: valid only
  at $k=F_n-1$ (`phase4-anchors-invalid`, deviation ≤1 per cell at general k,
  exact scan k=1..400).
- **Substitution transfer-matrix and pair-correlation-boundary approaches** —
  refuted in `research/approaches/` (image lengths k+c vs k+m+1; boundary
  term closes to the same floor-sum primitive).

## Numbers

- Oracle reproduced by `code/brute.py`: $\Psi(3)=20302$; $\Psi(10)\equiv10699667\pmod{101001001}$; factor count exactly k+1 for k=1..20. Captured in `code/out/brute_oracle_results.md` and `GOAL.md`.
- Mechanical construction `code/mech/mech_psi.py`: agrees with brute exactly k=1..50, with recorded exact values k=1..25, and with recorded residues k=1..400 (mod M); formulation (A)==(B); slope-insensitive. Captured in `code/out/mech_psi.captured.txt`.
- Universal-Euclidean monoid `code/lib/ueuclid.py` (13.9 KB on disk) is **verified in-container**: the earlier "65 FAILURES" claim (`ueuclid-incontainer-fails-s1s2`) was a FALSE ALARM (0/30 run used a 0-indexed oracle/docstring against the module's 1-indexed recursion; index-convention mismatch, not a compose bug). The module passes its own `__main__` — capture `code/out/ueuclid_main.captured.txt`: acceptance 1-3 30/30, floor_sum 30/30, deterministic 6/6, ue0 30/30, large-n dU=381966011250351898 == (514229·10^18+3)//1346269 in 0.29 ms. Convention is 1-INDEXED (t=1..n, weight z^(t-1)); 0-indexed wrapper `ue0(p,q-p,...)`. See `research/notes/refuter-ueuclid-s1s2-false-alarm.md` (claim `ueuclid-s1s2-false-alarm-refuted`). The verified compose formulas (claim `monoid-composition-formulas-verified`) hold. Remaining risk is reduction indexing (which power of 10 the j-th digit of telescoped v carries), to pin against mech_psi at small k.
- Known invalid: Psi(10^4)=16242174 and Psi(10^6)=77578256 (computed by the out-of-domain collapse — see Contradictions). **Directive-6 anchors, asserted from outside the container (pending in-container verification): Psi(10^4)=34432237, Psi(10^6)=20938836** (independent window/residue route, counts 10001/1000001). Valid direct-method values at k=1000, 10000 are not yet computed.

## Recalled

- Cognee: nothing on PE1006, Fibonacci subwords, $\Psi$, or the modulus.
  (recall_memory/recall_scratch/relate_memory ran empty this cycle.) The
  steering directives are steer input, not memory.

## Contradictions

- ~~The universal-Euclidean monoid fails its own acceptance tests in-container~~ — **RESOLVED, false alarm.** The `ueuclid-incontainer-fails-s1s2` claim ("65 failures, compose dU boundary-shift bug") was a 0-indexed-vs-1-indexed convention mismatch in the hand-check and the then-stale oracle/docstring, NOT a bug in the O(log) recursion. Module on disk passes `__main__` 30/30/30/30 + 6/6 (claim `ueuclid-s1s2-false-alarm-refuted`, `refuter-ueuclid-s1s2-false-alarm.md`). It does NOT block acceptance 4, the anchors, or Psi(10^18). The real remaining hazard is reduction indexing, not the primitive.
- **Phase-4 anchors 16242174 / 77578256 are invalid acceptance criteria** —
  the directive-2 record conflicted with the run's own exact checks. Both
  numbers were computed by `Psi_collapse`, which uses the Toeplitz identity
  $C(j,jp)=A(jp-j)$ that solution.py Phase 3 proves holds only at
  $k=F_n-1$ ($k=1,2,4,7,12,20,33,54,88,143,232,376,\dots$); neither $10^4$
  nor $10^6$ is of that form. Refuted claim `phase4-anchors-invalid`
  (research/notes/phase4-anchors-invalid.md): k=200 collapse 64554455 vs
  direct 83031232. Directive 6 confirms the invalidity and supplies the
  replacement anchors: **Psi(10^4)=34432237 and Psi(10^6)=20938836** (mod M),
  recomputed outside the container by the independent window/residue route.
  Verify them in-container (task `directive-6-anchors`) before they gate the
  O(log) run.

## Gaps

- **Directive-6 anchors are asserted, not yet verified in-container.**
  ​Psi(10^4)=34432237 and ​Psi(10^6)=20938836 must be reproduced inside the
  container before they gate the O(log) monoid: k=10^4 via the O(k²) valid
  direct method (`code/out/verify/check_phase4_anchors.py` now compares
  against 34432237), k=10^6 via the window/residue route
  (prefix length k+NextFib(k)-1, NextFib strictly greater than k, distinct
  count asserted k+1). Task `directive-6-anchors`.
- **The universal-Euclidean monoid is sound in-container** (`code/lib/ueuclid.py`, claim `ueuclid-s1s2-false-alarm-refuted`); the old "fix the dU cross terms" instruction is dead. The open gap is the **reduction wiring**: formulate the telescoped `v` (formulation B of `code/mech/mech_psi.py`) as a segment of the monoid and reproduce Psi(k) k=1..150 + Psi(10)=10699667 through `ueuclid`, PINNING the z^0/10-power reduction indexing against mech_psi at small k first (this indexing is untested and is the genuine remaining hazard). Then reproduce the two anchors 34432237/20938836 as the monoid's own output (currently verified only by the independent window/residue route), then k=10^18 stable across two Fibonacci approximants. Task `implement-solution`.
- **Primality of $101001001$ is asserted, not shown.** Only invertibility of
  $10$ (proved by $\gcd$) is needed for $x=10^{-1}\bmod M$, but if any step
  cites primeness, verify it.