# Shared context

The context curator owns this file; this is the current state of what the run knows.

## Established

**Problem restated (PE1006).** `S_0="0"`, `S_1="01"`, `S_n=S_{n-1}S_{n-2}`. A _Fibonacci
subword_ is a contiguous substring of some finite `S_n`. For each `k` there are exactly
`k+1` distinct length-`k` subwords; interpret each as a decimal (leading zeros dropped)
and let `Psi(k)` be the sum of their squares. Oracle: `Psi(3)=20302`
(`001,010,100,101` → `1²+10²+100²+101²`); `Psi(10)≡10699667 (mod 101001001)`. Target:
`Psi(10^18) mod 101001001`.

**Governing theory (librarian, sourced — see `research/notes/governing-theory-sturmian.md`)**
The `S_n` converge to the infinite Fibonacci word `F` = fixed point of `0→01, 1→0`,
a **Sturmian word of slope `α = 1/φ² = (3−√5)/2`**.
- **Morse–Hedlund** (hal-01827511, Theorem 1 + balanced): an aperiodic word has
  `p(k) ≥ k+1`; a balanced word has `p(k) ≤ k+1`; `F` is balanced and aperiodic, so
  `p(k) = k+1` — exactly the problem's stated FACT (k+1 subwords). Claim
  `PE1006-kplus1-FACT`.
- The set of length-`k` factors of `F` equals the set of length-`k` Fibonacci subwords of
  the finite `S_n` (each `S_n` is a prefix of `F`; any factor occurs inside a finite
  `S_n`). Factor set depends only on slope (Prop 7, hal-01829144) — so computing from the
  infinite word is legitimate.
- **Classification (request `precise-sourced-statement-c1ec` answered):** the `k+1`
  length-`k` factors are exactly the **balanced binary words of length `k`**, each with
  `⌊kα⌋` or `⌈kα⌉` ones (Morse–Hedlund balanced-blocks fact, quoted in Poirier–Steiner
  hal-03869990; claim `PE1006-balanced-factors-floornalpha`). Verified on `k=3`.
- **Enumeration theorem (Perrin–Restivo hal-00828351, Theorem 2):** consecutive length-`k`
  factors in lex order satisfy `u = r·ab·s, v = r·ba·s` or `u = r·a, v = r·b`; gives a
  linear "next factor" generator for the `k+1` factors (claim `PR-consecutive-factors-lex`).

These are the structural ingredients for a method whose cost does NOT grow with `k`:
`k=10^18` defeats any per-subword enumeration, so `Psi(k)` must come from a recurrence /
closed form built on the balanced-word structure, evaluated with fast exponentiation.

## Ruled out

Nothing yet — no method has been implemented. Per-subword enumeration at `k=10^18` is
recognised as infeasible (the wrong method).

## Numbers

Only the statement's given values (Ψ(3)=20302, Ψ(10)≡10699667 mod 101001001); not yet
reproduced by any program. `k=10^18` is the target.

## Recalled

Durable memory holds the governing-theory identification (see "Governing theory" above),
stored by the librarian.

## Contradictions

None recorded.

## Gaps

- `code/brute.py` must reproduce Ψ(3)=20302 and Ψ(10)≡10699667 first (tool_builder).
- `code/solution.py` must compute Ψ(10^18) mod 101001001 with exact arithmetic, agreeing
  with brute.py wherever reachable, via a poly(log) / closed-form method (the recurrence
  from the balanced-word / consecutive-factor structure).
- The precise recurrence/closed form for the sum of squares of the `k+1` balanced-word
  values is still to be derived (inventor / derivation).
