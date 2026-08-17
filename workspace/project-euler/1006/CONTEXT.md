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
  $\Psi(10^{18})\bmod101001001$. These oracle values are **not yet recomputed
  in-container** — reproducing them is the first gate.
- **Modulus arithmetic** (computed by inspection, trivial): $M=101001001$ is
  odd and $\not\equiv0\bmod5$, so $\gcd(10,M)=1$ and $10$ is invertible mod
  $M$; directive 2 additionally asserts $M$ prime (asserted, unverified).
- **Workspace state** (surveyed this cycle): ledgers `tasks`, `attempts`,
  `goals`, `claims`, `threads`, `approaches` all hold 0 entries; `code/`,
  `code/lib/`, `code/out/`, `research/approaches`, `research/threads`,
  `research/backward` contain only template README/INDEX files; `GOAL.md`,
  `derived/TASKS.md`, `derived/CLAIMS.md` are unwritten templates. Cognee is
  empty for PE1006/Fibonacci-subword queries (recall_memory and recall_scratch
  both returned nothing).

## Asserted but unverified — the steering directives

`config/directives.jsonl` (see also `config/.directives-cursor`) carries two
steer directives that pre-empt the derivation. Both claim to have been
"verified outside the container" against a brute oracle. **No in-workspace
evidence exists: no code, no output, no claim ids.** The directives themselves
say "reproduce it here before building on it." Treat both as hypotheses until
reproduced in-container.

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

## Ruled out

- Nothing yet. No attempt has been made in this workspace; nothing has failed
  here. The one thing already ruled out *by policy*: searching for a published
  PE1006 answer or forum solution invalidates the run.

## Numbers

- Expected oracle: $\Psi(3)=20302$; $\Psi(10)\equiv10699667\pmod{101001001}$
  (statement values, to be reproduced by `code/brute.py` first).
- No computed numbers exist in-container yet.

## Recalled

- Cognee: nothing on PE1006, Fibonacci subwords, $\Psi$, or the modulus.
  (recall_memory/recall_scratch/relate_memory ran empty this cycle.) The two
  directives are steer input, not memory.

## Contradictions

- None on record. Note the standing risk: directive 2 contradicts nothing
  stated, but it is the only substantive route in the workspace and carries no
  in-container verification — a one-source claim, which is a contradiction in
  evidence quality if anything gets built on it before reproduction.

## Gaps

- **In-container reproduction of the oracle: none.** `code/brute.py` does not
  exist; $\Psi(3)$ and $\Psi(10)\bmod M$ must be computed by a naive program
  and matched to the statement before any derived method is trusted (step 1 of
  the run plan).
- **Directive 2's method is unverified in-container.** Suggested gate from the
  directive itself: check the mechanical-word/floor-sum implementation against
  a brute oracle on $k=1..150$ and against $\Psi(10)\equiv10699667$, then run
  at $k=10^{18}$ with $F(n)>k$. Until that check runs, everything about the
  route is hearsay from `config/directives.jsonl`.
- **Primality of $101001001$ is asserted, not shown.** Only invertibility of
  $10$ (proved by $\gcd$) is needed for $x=10^{-1}\bmod M$, but if any step
  cites primeness, verify it.
- `GOAL.md` still holds the template sentence; the precise restatement with
  every symbol defined belongs there and does not exist yet.