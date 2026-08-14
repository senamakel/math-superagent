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
is a bill the whole run pays many times over. Link the file that still holds
any detail compressed away. Durable findings belong in Cognee. A statement
nobody can trace to a source is worth less than no statement.

## Established

- **Problem definition (sourced: `problem.md`, downloaded from
  projecteuler.net/minimal=156).** Natural numbers written consecutively in
  base 10 from 0; `f(n,d)` = total occurrences of digit `d` in 0..n inclusive.
  Solve `f(n,d)=n` for each `d∈{1..9}`; `s(d)` = sum of all solutions for that
  `d`; the note says an `n` satisfying several `d` counts once per `d`. Answer:
  `Σ s(d)` for d=1..9.
- **Oracle targets (given in the statement; none executed this run — this is
  the gate for `code/brute.py`).** `f(n,1)` n=0..12 = 0,1,1,1,1,1,1,1,1,1,2,4,5;
  the value 3 never occurs; first solutions of `f(n,1)=n` are 0, 1, 199981;
  `s(1)=22786974071`.

## Asserted but unverified (this cycle's recall — durable memory, not this
run's own finding, and no source on disk yet)

- **Sticker/exactly-number theory governs this exact problem.** Cognee recall
  returns a paper whose central object `fd(x,b)` is "total occurrences of
  digit d among 1..x in base b" and whose sequences are OEIS A226238 (the
  `fd(x)=x` solutions in base 10) and A364972 (bases where `fd(0,b)` has no
  solution). Its **Prop 9.1**: for base b>d, all `fd(x,b)=x` solutions satisfy
  `x ≤ d·b^b`, so in base 10 `x ≤ d·10^10` — a provable finite search bound
  that directly defeats the "can't enumerate to the answer" objection. It also
  notes `f_b(b^b)=b^b` (so x=b^b is always a solution) and `fd(d·b^b)=d·b^b+1`.
  **Hypotheses to check before relying on it:** paper's `fd` counts from 1 or
  0 (f(0,d)=0 here; a 1-based count could differ by the leading digit of 0 —
  none, so counts agree); paper's "sticker" definition matches overlapping
  equal-length blocks. The recall chunks contain no title/authors/URL — treat
  paper identity as a gap; a research request should reproduce Prop 9.1's
  statement and proof sketch from an identifiable source.
- **Closed-form digit counting (recalled as "classical O(#digits) method";
  GeeksforGeeks "Occurrences of 2 as a Digit in 0 to n" carries the
  place-value recurrence, check value f(22,2)=6).** Verified derivation still
  to be written in `solution.md` and checked against brute.py.

## Ruled out

- Nothing attempted yet this run. Standing prohibition: enumerating n up to
  the answer (answer ~10^10) is the wrong method; the O(#digits) closed form
  for `f(n,d)` plus the `d·10^10` bound is the intended route.

## Numbers

None computed. Targets to hit: f(11,1)=4, f(12,1)=5, first solutions 0, 1,
199981, s(1)=22786974071, then Σs(d) — final answer still open.

## Recalled

Cognee `recall_memory` (queried this cycle: "PE156 digit counting",
"A226238 ... 22786974071", "sticker numbers", "occurrences of 2 as a digit in
0 to n") returns: the sticker-paper chunk above (same pages 15–18 every query)
and to the count-digit-2 query a GeeksforGeeks metadata blob. `relate_memory`
links nodes `project_euler_156`, `f(n,d)` ("counts occurrences of digit d
among numbers 0..n"), the GeeksforGeeks article, and "closed-form digit
counting" (O(#digits) method). `search_claims` ledger is empty; `search_documents`
returns nothing (no indexed notes or outputs). Nothing from a *previous run's*
conclusions was recalled — the durable material appears to be imported
literature knowledge, not prior-run results.

## Contradictions

None so far — nothing computed and no prior-run claims to disagree with. Note
for later: the paper's bound `x ≤ d·10^10` (~9×10^10 for d=9) is an upper
bound on solutions, not on the numbers that must be *checked*; the method must
still evaluate f(n,d) without visiting that whole range.

## Gaps

- `code/brute.py` (naive per-n counting) does not exist yet; it must reproduce
  the oracle (n=0..12 table, 199981, and f(22,2)=6 once extended to d=2)
  before any efficient method is trusted. This is the immediate next step.
- No `solution.md`, no `code/solution.py`, no second independent route.
- Paper identity (title/authors/URL) is missing from the recall chunks — worth
  a research request, since Prop 9.1's bound is the theory the efficient
  search rests on.

## Pointers

Problem statement: `problem.md`. Research layout rules: `research/README.md`.
Code/output conventions: `code/INDEX.md`, `code/out/README.md`. Claim blocks
reach `research/CLAIMS.md` only via notes under `research/` or `code/out/`.