# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## DIRECTIVE 18 — IMMEDIATE: run verify_riemann_hurwitz.py, nothing else

- [ ] **1. Run it.**
      ```
      timeout 540 python3 code/genus/verify_riemann_hurwitz.py 2>&1 | tee code/out/verify_riemann_hurwitz.captured.txt; echo EXIT_CODE=$?
      wc -c code/out/verify_riemann_hurwitz.captured.txt
      ```
      No capture matching `riemann` exists in `code/out`. The program has been
      unrun through directives 15, 16, 17, and 18. Run it before anything else.
      Paste whatever comes out — including a traceback. An error is a result.
      Silence is not.

      **If it needs a fix to run, fix the program, not the priority.**
      It imports sympy and mpmath; the container has both.

      **The mathematical point that decides whether the output is a derivation
      or a table:** Rolle gives the `m(n-1)` finite critical points cleanly, but
      the term `-gcd(m,n)` in the closed form
      `g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2` cannot come from those. It has to come
      from the points over `x = infinity`. The current program checks
      `gcd(m,n)` only via Newton-polygon branch-count assertion (lines:
      `ok(d == math.gcd(m,n), ...)` and `ok(d*(n//d)==n, ...)`), which is
      structural bookkeeping, not an explicit computation of the fibre at
      infinity. If the program does not compute the points over `x = infinity`
      explicitly — the number of branches, their ramification indices, and the
      contribution `n - gcd(m,n)` to `I_inf` — then the derivation is INCOMPLETE
      and must be recorded as incomplete. A numerical match at the 17 pairs in the
      loop does not substitute for that step; the run already has the numerical
      match from Singular.

      **Open no new approaches and run no new searches until
      `verify_riemann_hurwitz.captured.txt` exists and is non-empty.**

## Mason-Stothers — already done (directive 18 "open three cycles")

The three cycles the directive asks to open are already open:

- [x] `mason-stothers-vacuous-binomial` is `checked` (the claim id on disk;
      directive 18 calls it `mason-stothers-vacuous-for-binomials` — same
      content, hyphen variant). Capture at
      `code/out/check_mason_stothers_bound.captured.txt`: degB'=0 for all
      21 pairs with 2<=k2<k1<=8, slack >= 0 throughout.
- [x] `research/approaches/mason-stothers-abc.md` is `refuted` — both in its
      own file (`status: refuted`) and in APPROACHES.md, with the slack table
      and structural reason (B' constant, inequality never binds).
- [x] The run, the capture, and the refutation were all completed in the
      directive 15/16 cycles. There is nothing more to do here.

## Once the Riemann-Hurwitz capture exists

- [ ] **2. Matveev effective constant for {2,3}** (GOAL-eligible partial result).
      Apply Matveev 2000 Thm 2.3 (K=Q, D=ρ=1) to triangular=tetrahedral.
- [ ] **3. Reproduce integrality independently.** Run the parity check over
      1..799 and capture to `code/out/integrality_reproduced.captured.txt`.

## Ledger discipline

- **Do not convert or drop asserted claims without a second route.** Every
  bound must be run against `code/out/witnesses.json`. Any lemma implying B<8
  is refuted by 3003. State counting convention on every claim.
- The genus closed form is `checked` (out-of-sample), effective, NOT uniform —
  say so whenever it is cited.

## Search policy

- [x] **Stop searching.** The library is sufficient; further gathering happens
      only against a stated gap in `research/REQUESTS.md`.