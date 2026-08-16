# Thread — the near-cubic structure and the 4/7 degree spine

Question: Can the Carr/Markström minimal-counterexample structure be pushed to a
falsifiable degree-distribution impossibility?

The value of this thread: the two strongest *2-power-specific* theorems
(Sudakov–Verstraëte, Liu–Montgomery) both run on average degree ≫ 3 and so
cannot reach the conjecture. The only machinery that lives at δ ≥ 3 is the
degree/independence structure of a minimal counterexample (proved in
Markström, elaborated by Carr) plus the near-miss constructions (Markström
24-vertex, Bensmail arbitrary-size). This thread asks whether that structure
is *rigid enough* to exclude a counterexample on degree counts alone.

```thread
question: Does a minimal counterexample exist, necessarily with ≥4/7 of vertices of degree 3 and all deg-≥4 vertices pairwise non-adjacent, or does that structure force a power-of-2 cycle?
status: open
rests-on: ce-deg-structure, ce-predominantly-cubic, ce-principality-carr, bensmail-q-power, markstrom-24-vertex-near-misses
blocked-by: no quantitative rigidity theorem linking degree counts to cycle presence is established
next: (a) tighten Carr's 4/7 toward an absolute minimum degree-3 fraction that forces a 2-power cycle; (b) test with the oracle whether any small graph meeting (independent deg-≥4 set, all others degree 3, no C4/C8/C16) exists at all in the verified range — UNSAT there is a real structural theorem; (c) study whether the Bensmail 4-only/8-only graphs realize the extremal 4/7 bound.
```

## Why this is the live frontier

The obstruction (problem.md + `ghlu-ma-interval-results`, `sv-sparse-without-2power`,
`lm-large-avgdeg-forces-2power`) says the run must produce a cycle at a
*prescribed* sparse length, which interval/congruence machinery cannot do at
δ ≥ 3. The only structural handle at δ ≥ 3 is the minimal-counterexample degree
picture. If a minimal counterexample exists at all, it is *nearly cubic* and
its non-cubic vertices form an independent set — that is a strong global
constraint a discharging/tilting argument could exploit: push degree-3
fraction up toward 1, and at 1 (cubic) the problem is still open but the
near-misses (Bensmail) say the answer is not "bounded 2-power lengths".

## Falsifiers (what would kill this thread)

- Any verified small graph meeting the full degree structure with no C4/C8/C16
  (none is known; Balaji's 32-vertex bound is consistent with "none exists").
- A proof that some graph satisfying the degree structure avoids all 2-powers
  at arbitrary size (would be a counterexample — extremely unlikely).
- Showing the 4/7 bound is loose and the true behaviour is different.

## Next concrete step

Run the oracle/SAT on the question: does a graph with δ ≥ 3, n ≥ 32, degree-≥4
vertices forming an independent set, all other vertices degree 3, and no C4/C8/
C16 exist? This is the exact "preliminary" structural class. UNSAT would rule
out a whole family of potential counterexamples and is a genuine structural
result; SAT on some n would be the first candidate counterexample shape ever
found. This is a satisfiability question for sat_solver, and it is the finite
test the degree-structure thesis throws off.
