# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method policy for the whole run: how to reason (compute before prose), evidence rules (every number from a run, every theorem cited), housekeeping conventions |
| `README.md` | Overview of the workspace and its entry points (AGENTS.md, prompts/, goal.md, tasks.md, scratchpad.md, memory.md) |
| `aj.py` | _(undescribed)_ |
| `aj2.py` | _(undescribed)_ |
| `brute.py` | Method-1 oracle: literal double sum Q(n) = Σ_π Σ_i rank(π^i) by walking every power. O((n!)²), exact; reproduces rank(2,1,3)=3, Q(2)=5, Q(3)=88, Q(6)=133103808. Writes results.json. |
| `brute2.py` | Method-2 oracle (independent): Q(n) = Σ_π (n!/ord(π)) · Σ_{τ∈⟨π⟩} rank(τ), using periodicity d = ord(π) = lcm of cycle lengths. Cross-validates brute.py for n=2..7. Writes results2.json. |
| `config.toml` | Run configuration: workspace kind, solver flags (exact arithmetic, verify with code, cite sources, forbid exponential), artifact file paths |
| `explore.out.txt` | _(undescribed)_ |
| `explore.py` | Exploratory script for n=2..7: computes M_j = sum_pi sum_{i=0}^{n!-1} a_j(pi^i) (a_j = Lehmer code coefficient) and the pairwise matrix N(j,m) = #{(pi,i): 0<=i<n!, (pi^i)[m] < (pi^i)[j]}, exact integers. Verified M_j == sum_{m>j} N[j][m]. Revealed N depends only on gap m-j (translation-invariant), so M_j is the suffix sum of the gap function f(k). |
| `fdtable.json` | _(undescribed)_ |
| `fdtable.py` | _(undescribed)_ |
| `fi.py` | _(undescribed)_ |
| `fi2.py` | _(undescribed)_ |
| `goal.md` | Objective: compute Q(10^6) mod (10^9+7); statement, worked examples (Q(2)=5, Q(3)=88, Q(6)=133103808, Q(10)≡468421536), completion criteria, current status |
| `mean.py` | _(undescribed)_ |
| `memory.md` | Working memory: problem restatement, verified Q(n) table (n=2..8) with both methods' timings, established results, failed approaches (none), open questions (the n=10^6 method) |
| `ntau.py` | _(undescribed)_ |
| `perpi.py` | _(undescribed)_ |
| `problem.html` | The problem statement (source of the run): defines Q(n), rank, π^i; gives worked examples; asks for Q(10^6) mod (10^9+7) |
| `problem.url` | Source URL for the problem statement: https://projecteuler.net/minimal=903 |
| `psid.py` | Exploratory: verifies Q(n)=sum_{d |
| `qtable.py` | _(undescribed)_ |
| `results.json` | Output of brute.py (method 1, literal): exact Q(n) and Q mod p for n=2..7; n=8 skipped (budget estimate exceeds cap) |
| `results2.json` | Output of brute2.py (method 2, period formula): exact Q(n) and Q mod p for n=2..8 |
| `scratchpad.md` | Provisional work: the task, method-1 cost model, method-2 justification, power-semantics check, verified results table |
| `tasks.md` | Task list with checkboxes: recording objective, reading the statement, writing brute.py/brute2.py, verifying n=2..6/7/8, and the (pending) efficient method |
