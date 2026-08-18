# Durable note (pending memory server recovery) — approach selection, round 1

This content was destined for Cognee (`remember_memory`); the memory server
was unreachable, so it lives here until it can be stored. Do not treat this
as established — it is a record of a decision and of hand-checked arithmetic.

## Decision

- **ADOPTED**: `lte-divisibility-obstruction` — per-shape divisibility
  obstruction $(2^L-3^m) \mid S$.
- **NARROWED**: `parity-rationality-conjugacy` — the conjugacy survives as a
  tool (the parity vector *is* the gap-pattern data $(L,m,\text{gaps})$);
  the three-distance divergence bridge closed for lack of any lemma linking
  Collatz valuations to an irrational rotation.
- **REFUTED**: `backward-transducer-covering` — the stabilization hypothesis
  is unsupported and contradicted by the published $k$-dependent growth; a
  countable union of regular languages need not be regular, so the finite
  language-inclusion reduction fails without it.

## Why the adopted one won

Divisibility is logically prior to any size bound. The earlier refuted
approach (`diophantine-collision-refuted`) died conflating $K$ with $x_{\min}$
and using the irrationality measure in the wrong direction; the adopted line
never touches either.

## Hand-verified arithmetic (this session, by hand — not machine-checked)

The Böhm–Sontacchi formula $x = S(L,m,\text{gaps})/(2^L-3^m)$, accelerated
map $T_0=x/2$, $T_1=(3x+1)/2$, checked against four real cycles on $\mathbb Z$:

| cycle | $L$ | $m$ | gaps | $S$ | $2^L-3^m$ | $x$ |
|---|---|---|---|---|---|---|
| $1\to2\to1$ | 2 | 1 | (2) | 1 | 1 | 1 ✓ |
| $-1\to-1$ | 1 | 1 | (1) | 1 | $-1$ | $-1$ ✓ |
| $-5\to-7\to-10\to-5$ | 3 | 2 | (1,2) | $3\cdot1+2=5$ | $-1$ | $-5$ ✓ |
| $-17\to\dots\to-17$ | 11 | 7 | (1,1,1,2,1,1,4) | 2363 | $-139$ | $-17$ ✓ |

Complete hand-UNSAT for shape $(L,m)=(5,2)$: $D=23$, $S=3+2^{v_1}\in\{5,7,11,19\}$
for $v_1\in\{1,2,3,4\}$ — none divisible by 23, all 4 patterns enumerated,
so **no cycle of shape $(5,2)$ exists**. This is the shape of the target
theorem, at trivial size.

Blind spot: shapes with $|2^L-3^m|=1$ (the trivial cycle's $(2,1)$) impose no
divisibility constraint at all.

## The complexity fact that forces the SAT route

At $m=92$, $L\approx 146$: pattern count $\binom{145}{91}\approx 10^{40}$.
Enumeration is prohibited; the per-prime residue encoding is the only route.

## Load-bearing lemma (state in Lean FIRST)

For $p$ prime with $e = v_p(2^L-3^m)$, the map
$\text{gaps} \mapsto S \bmod p^e$ factors through
$(V_1,\dots,V_{m-1}) \bmod \operatorname{ord}_{p^e}(2)$, where $V_j$ are the
partial sums of the gap vector. This is the completeness lemma that turns a
CP-SAT UNSAT into a theorem.

## Open asks to research

1. Is the order/discrete-log route to $v_p(2^L-3^m)$ for unrelated exponents
   standard in the literature?
2. Brox 2000's divisibility-equation framing — exact statement (nearest
   proved precedent).
3. Is the completeness lemma above in the literature, or genuinely ours?

## Status of the oracle

`code/cycles/shape_oracle.py` written and described; **not executed** — no
execution tool reached this session (confirmed by a subagent too). Whoever
can run programs should run it and post the output.
