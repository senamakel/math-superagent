# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method policy for the whole run: how to reason (compute before prose), evidence rules (every number from a run, every theorem cited), housekeeping conventions |
| `README.md` | Overview of the workspace and its entry points (AGENTS.md, prompts/, goal.md, tasks.md, scratchpad.md, memory.md) |
| `aj.py` | Exploratory: decomposes Q(n) = sum over j of (n-j)!*A_j + (n!)^2 via Lehmer coefficients, verifies Q and prints A_j values for n=2..5; fed the A_j-pattern hunt later carried by aj2.py |
| `aj2.py` | Exploratory: computes A_j(n) = sum over i, pi of c_j(pi^i) for n=2..8 (Lehmer route, orbit-walk optimized) and reconstructs Q = n!^2 + sum_j (n-j)!*A_j; faster successor to aj.py for the A_j table |
| `aj3.py` | Computes M_j (Lehmer-coefficient power sums) for n=9,10 to extend the f_n(k)=A_n-B_n(k-1) data for closed-form fitting. |
| `brute.py` | Method-1 oracle: literal double sum Q(n) = sum over pi of sum_{i} rank(pi^i) by walking every power. O((n!)^2), exact; reproduces rank(2,1,3)=3, Q(2)=5, Q(3)=88, Q(6)=133103808. Writes results.json |
| `brute2.py` | Method-2 oracle (independent): Q(n) = sum over pi of (n!/ord(pi)) * sum over tau in <pi> of rank(tau), using periodicity d = ord(pi) = lcm of cycle lengths. Cross-validates brute.py for n=2..7. Writes results2.json |
| `config.toml` | Run configuration: workspace kind, solver flags (exact arithmetic, verify with code, cite sources, forbid exponential), artifact file paths |
| `explore.out.txt` | Saved stdout of explore.py (n=2..7): M_j vectors and N(j,m) matrices exposing the translation-invariant gap function f(k)=N(j,j+k) |
| `explore.py` | Exploratory script for n=2..7: computes M_j = sum over pi,i of a_j(pi^i) (a_j = Lehmer code coefficient) and the pairwise matrix N(j,m) = #{(pi,i): (pi^i)[m] < (pi^i)[j]}, exact integers. Verified M_j == sum_{m>j} N[j][m]. Revealed N depends only on gap m-j (translation-invariant), so M_j is the suffix sum of the gap function f(k) |
| `fdtable.json` | Output of fdtable.py: per-n rows {n, d, phi(n!/d), F(d)} for n=4,5,6 plus totals; the verified F(d)/phi divisor table for the Q(n) structure |
| `fdtable.py` | Verifier for the F(d) route: computes Q(n)=sum over d dividing n! of phi(n!/d)*F(d), cross-checks toolkits/f_table.py against toolkits/f_literal.py for n=4,5,6, asserts known Q values (4808, 597876, 133103808), writes fdtable.json |
| `fi.py` | Exploratory: studies F_i(n)=sum over pi of rank(pi^i) over i=1..n! for n=4,5 — frequencies of distinct F_i values and mean (checks mean equals n!(n!+1)/2) |
| `fi2.py` | Exploratory: groups F_i(n) by g = gcd(i, n!) for n=4,5 to test whether F_i is constant on each gcd class (the independence claim behind F(d)); predecessor of toolkits/f_literal.py's assert |
| `fit.py` | Symbolic/float exploration of alpha_n and beta_n closed forms for the f_n(k)=n!(n-1)![alpha-beta(k-1)] fit in the Q(n) problem. |
| `fit2.py` | Fit alpha_n = A/(n!(n-1)!), beta_n = B/(n!(n-1)!) against candidate basis functions (small rational coefficients, harmonic numbers) using exact M_j data for n=4..10; successor to fit.py for the closed-form hunt. |
| `fit3.py` | Systematic exact search of basis-function linear combinations for alpha_n,beta_n in the Q(n) closed form fit. |
| `fit4.py` | Exact rational-basis search for alpha_n and beta_n closed forms over many candidate basis functions. |
| `fk.py` | Computes the gap function f(k)=N(j,j+k) for n=2..9 and tests the affine structure f(k)=A-Bk and extracts A,B. |
| `gaps.py` | Computes T(j,m)=#{(pi,i): 0<=i<n!, (pi^i)(m)<(pi^i)(j)} for n=2..9 exactly via the period formula T(j,m)=sum_pi (n!/ord(pi)) * #{tau in <pi>: tau(m)<tau(j)} (Fractions), without iterating all n! powers. Verifies translation invariance T(j,j+k) independent of j, and reports f_n(k)=T(1,1+k), its differences, and whether f is exactly arithmetic (A_n=f(1), step B_n). Oracle-checked n=2,3 (in-script literal) and n=4,5 (separate literal). Established the structural lead that f_n is arithmetic in k for all n. |
| `goal.md` | Objective: compute Q(10^6) mod (10^9+7); statement, worked examples (Q(2)=5, Q(3)=88, Q(6)=133103808, Q(10) about 468421536), completion criteria, current status |
| `mean.py` | Exploratory: prints sums of F(d) over proper divisors and total to inspect the pattern inside F(d) for n=4,5,6; inspective, no output file |
| `memory.md` | Working memory: problem restatement, verified Q(n) table (n=2..8) with both methods' timings, established results, failed approaches (none), open questions (the n=10^6 method) |
| `ntau.py` | Exploratory: computes N(tau)=#{(pi,i) with pi^i=tau, i in 1..n!} and tests whether N(tau) depends only on tau's cycle type (n=3,4); also re-derives Q = sum over tau of rank(tau)*N(tau) |
| `perpi.py` | Exploratory: per-permutation analysis for n=5 — orders, cyclic-subgroup rank sums, grouped by cycle type, looking for structure in the intra-subgroup rank sum |
| `problem.html` | The problem statement (source of the run): defines Q(n), rank, pi^i; gives worked examples; asks for Q(10^6) mod (10^9+7) |
| `problem.url` | Source URL for the problem statement: https://projecteuler.net/minimal=903 |
| `psid.py` | Exploratory: verifies Q(n)=sum over d dividing n! of psi(d)*phi(n!/d) for n=5 with psi(d)=F-value for i with gcd(i,n!)=d, and prints psi(d) over all divisors to look for structure |
| `qtable.py` | Exploratory: computes Q(n) via the period/orbit formula for n=2..10 and prints normalization ratios Q/n! and Q/(n!)^2 to look for a closed form; quantifies the runtime wall at n=10 |
| `results.json` | Output of brute.py (method 1, literal): exact Q(n) and Q mod p for n=2..7; n=8 skipped (budget estimate exceeds cap) |
| `results2.json` | Output of brute2.py (method 2, period formula): exact Q(n) and Q mod p for n=2..7 (the n=8 value 24768798220800 lives in memory.md but was never written to this file) |
| `scratchpad.md` | Provisional work: the task, method-1 cost model, method-2 justification, power-semantics check, verified results table |
| `tasks.md` | Task list with checkboxes: recording objective, reading the statement, writing brute.py/brute2.py, verifying n=2..6/7/8, and the (pending) efficient method |
