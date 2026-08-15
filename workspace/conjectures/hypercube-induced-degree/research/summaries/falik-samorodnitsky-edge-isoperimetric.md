# Falik–Samorodnitsky, "Edge-isoperimetric inequalities and influences" (CPC 16, 2007)

URL: https://doi.org/10.1017/s0963548306008340 (full text via semanticscholar reader fd95cf9a…)

## What it establishes

1. **Edge-isoperimetric / total-influence inequality:** for A ⊆ {0,1}^n with
   µ = |A|/2^n ≤ 1/2,
       Σ_{i=1}^n I_i(A) ≥ 2·log2(1/µ)·µ,
   where I_i(A) is the influence of coordinate i on the indicator of A (the
   fraction of vertices whose i-th flip leaves/enters A).
2. A combinatorial proof of Kahn–Kalai–Linial: every balanced f has a variable
   with influence ≥ Ω(log n / n).
3. Improved constants; near-optimal functions resemble subcubes; conjectures on
   exact constants.

## Why it is here / relevance

The strongest edge/influence bound on the cube is a **total** (Σ_i I_i, average
over directions) and **outer-boundary** (leaving A) quantity. It does not bound
the max internal degree D(S) of problem.md. Note the subtlety the source note
flags: the influence bound is a *per-coordinate average over vertices* of
S→complement edges, not a per-vertex internal degree; the max degree inside S is
a per-coordinate *internal* influence, a different object. For |S| = 2^{n-1}+1
(µ slightly over 1/2) the stated inequality's regime (µ ≤ 1/2) just fails to hit
the exact edge, though by continuity the log-type total bound is what the method
can yield. KKL's Ω(log n/n) is the "max-from-analysis" engine; the recorded
obstruction is precisely that it bounds coordinate sensitivity, not D(S).

## claim block

```claim
id: falik-samorodnitsky-edge-isoperimetric
statement: For A ⊆ {0,1}^n with µ = |A|/2^n <= 1/2, total influence
  Σ_i I_i(A) >= 2 log2(1/µ)·µ (edge-isoperimetric); KKL follows: some variable
  has influence >= Ω(log n / n) for balanced f.
hypotheses: A subset of cube, µ <= 1/2; I_i influence (boundary fraction).
holds-here: partially — problem.md's |S| = 2^{n-1}+1 has µ just over 1/2, just
  outside the stated regime; the bounded quantity is total/average outer
  boundary, not max internal degree D(S).
status: asserted-by-source (proved in paper, not re-derived here)
bearing: fingerprints the obstruction — influence/total-boundary methods bound
  averages; a D(S) lower bound needs a per-vertex internal max, orthogonal here.
anchor: research/sources/falik-samorodnitsky-edge-isoperimetric-influences.md
```

```claim
id: kkl-balance-influence
statement: Every balanced Boolean f on {0,1}^n has a variable with influence
  >= c·log(n)/n (KKL 1988; combinatorial proof in Falik–Samorodnitsky 2007).
hypotheses: f with E f = 1/2.
holds-here: true as stated; quantity is max per-coordinate *leaving-boundary*
  influence, NOT max internal degree. Transfer to D(S) is unproved and is the
  actual gap.
status: asserted-by-source
bearing: the standard maximum-producing Fourier result on the cube; KKL alone
  cannot give D(S) >= omega(log n) because its max is over directions of a
  boundary count, not over vertices of internal degree.
anchor: research/sources/falik-samorodnitsky-edge-isoperimetric-influences.md
```

**Does not help** for the D(S) bound directly — confirms the averaging/log-n
obstruction. Part of the four "stuck" techniques in problem.md.
