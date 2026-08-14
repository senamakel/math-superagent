# Shared context

## Established

Nothing yet. The workspace is scaffold-only: all READMEs, role prompts, and empty
template folders (`research/approaches`, `backward`, `threads`; `code/lib`, `code/out`).
`research/CLAIMS.md` reads "No claims recorded yet". No claim id exists. No number
has been computed. `GOAL.md` and `TASKS.md` are unedited placeholders.

The only content this run holds is the statement at `/workspace/problem.md`.

**Problem restated** (PE1006). $S_0="0"$, $S_1="01"$, $S_n=S_{n-1}S_{n-2}$.
A *Fibonacci subword* = a contiguous substring of some $S_n$. For each $k\ge1$ there
are exactly $k+1$ distinct Fibonacci subwords of length $k$. Interpret each as a
decimal number (leading zeros dropped) and let $\Psi(k)$ = sum of their squares.
Oracle values: $\Psi(3)=20302$ (subwords 001,010,100,101 → 1²+10²+100²+101²);
$\Psi(10)\equiv10699667\pmod{101001001}$. Find $\Psi(10^{18})\bmod 101001001$.

These oracle values are the test targets; both are as stated, not yet reproduced by
any program.

## Ruled out

Nothing. No approach has been tried, so no dead end exists yet. Do not let the
inventor treat any line as pre-explored.

## Numbers

Only the statement's given values (Ψ(3)=20302, Ψ(10)≡10699667 mod 101001001). No
computed or independently confirmed terms.

## Recalled

Nothing. `recall_memory`/`recall_scratch` return no prior or related-run notes on
PE1006, Fibonacci subwords, or Ψ. This appears to be a first run on the problem.

## Contradictions

None recorded.

## Gaps

- Definition must be turned into an executable oracle: `code/brute.py` collecting
  distinct length-k substrings over finite $S_n$, reproducing Ψ(3)=20302 and
  Ψ(10)≡10699667 first.
- The governing structure (the family of the $k+1$ distinct length-$k$ Fibonacci
  subwords, and a way to sum their squares without enumerating $10^{18}$ of them)
  is unstated and uninvestigated. Bound $k=10^{18}$ defeats any per-subword method.
- `GOAL.md` and `TASKS.md` need writing.
