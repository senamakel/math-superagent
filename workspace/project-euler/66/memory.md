# Working memory

## Problem

Project Euler Problem 66 (source: https://projecteuler.net/minimal=66).

Consider the quadratic Diophantine (Pell) equation $x^2 - D y^2 = 1$ with
positive integers $x, y$ and parameter $D$. For square $D$ there are no
solutions in positive integers (stated as an assumption in the problem). For
non-square $D$, infinitely many positive solutions exist; the "minimal
solution in $x$" is the solution with smallest $x$ (the fundamental solution).

Question: find the value of $D \le 1000$ (non-square) whose minimal solution
in $x$ has the largest $x$.

## Established results

Extraction step only — no computation performed yet (per task instruction).

Test oracle facts extracted from the statement (any solution must reproduce):
- $D = 13$: minimal solution $(x, y) = (649, 180)$, i.e. $649^2 - 13\cdot 180^2 = 1$.
- $D = 2$: $(x, y) = (3, 2)$;  $D = 3$: $(2, 1)$;  $D = 5$: $(9, 4)$;
  $D = 6$: $(5, 2)$;  $D = 7$: $(8, 3)$.
- For $D \le 7$, the largest minimal $x$ occurs at $D = 5$ (stated in problem).

## Failed approaches

(none yet)

## Open questions

- None for this extraction step. Next step (not part of this task): derive the
  Pell/continued-fraction method, implement `solution.py`, verify against the
  oracle facts, and compute the answer for $D \le 1000$ with a second,
  independent verification route.

## Phase 2 — Mathematical context for Euler 66

**Provenance tag (applies to every item below):** theory recalled from
mathematical training (classical number theory: Lagrange's periodicity theorem;
Pell–Euler theory of $x^2 - Dy^2 = 1$; chakravala of Bhaskara II; Dirichlet's
unit theorem specialized to real quadratic fields). **No web verification
available in this run** — web search disabled, no source consulted, no URL
cited. `recall_research` returned no prior local notes. Small-case hand checks
(§2.6 and scratchpad.md) validate the statements on examples; they are not
proofs. No code was written and no answer computed in this phase.

### Phase 2.1 — Objects: Pell equation, $\mathbb{Z}[\sqrt{D}]$, norm, units, fundamental solution

*Provenance: theory recalled from mathematical training; no web verification available in this run.*

- **Equation:** $x^2 - D y^2 = 1$ with $D$ a fixed positive **non-square**
  integer; solutions sought in positive integers $(x, y)$. For non-square $D$
  infinitely many positive solutions exist (classical; a construction is
  forced by §2.3).
- **Ring:** $\mathbb{Z}[\sqrt{D}] = \{a + b\sqrt{D} : a, b \in \mathbb{Z}\}$,
  embedded in $\mathbb{R}$ via the positive root; multiplication
  $(a+b\sqrt{D})(c+d\sqrt{D}) = (ac + Dbd) + (ad + bc)\sqrt{D}$.
- **Norm:** $N(a + b\sqrt{D}) = a^2 - D b^2 = (a+b\sqrt{D})(a-b\sqrt{D})$,
  multiplicative: $N(\alpha\beta) = N(\alpha)N(\beta)$ (direct expansion).
  Hence $x^2 - D y^2 = 1 \iff N(x + y\sqrt{D}) = 1$, and $x + y\sqrt{D}$ is a
  unit of the ring (inverse $x - y\sqrt{D}$). Units of norm $+1$
  $\leftrightarrow$ integer solutions of the Pell equation.
- **Fundamental solution $(x_1, y_1)$:** the positive-integer solution with
  least $x$. "Equivalently least $y$": both maps $x \mapsto \sqrt{(x^2-1)/D}$
  ($x \ge 1$) and $y \mapsto \sqrt{1 + Dy^2}$ are strictly increasing on
  positive arguments, so minimal positive $x$ and minimal positive $y$ select
  the same pair.
- **Group structure (classical Pell theorem; special case of Dirichlet's unit
  theorem, the unit rank of $\mathbb{Q}(\sqrt{D})$ is 1):** all positive
  solutions are $(x_n, y_n)$ with $x_n + y_n\sqrt{D} = (x_1 + y_1\sqrt{D})^n$,
  $n \ge 1$; explicitly
  $x_n = \frac{(x_1+y_1\sqrt{D})^n + (x_1-y_1\sqrt{D})^n}{2}$,
  $y_n = \frac{(x_1+y_1\sqrt{D})^n - (x_1-y_1\sqrt{D})^n}{2\sqrt{D}}$,
  both integers by binomial expansion ($\sqrt{D}$-powers cancel in $x_n$; the
  $y_n$ numerator is $2\sqrt{D}$ times an integer). $x_n, y_n$ strictly
  increase with $n$. The full solution set is $\pm(x_1 + y_1\sqrt{D})^n$,
  $n \in \mathbb{Z}$. So the minimal-$x$ solution **generates** all solutions;
  Euler 66 needs only $(x_1, y_1)$.
  *Nuance (medium-high confidence):* if $D \equiv 1 \pmod 4$ the full ring of
  integers of $\mathbb{Q}(\sqrt{D})$ is $\mathbb{Z}[(1+\sqrt{D})/2] \supsetneq
  \mathbb{Z}[\sqrt{D}]$ and contains extra units; the theorem above is stated
  for integer solutions $(x,y)$ of $x^2 - Dy^2 = 1$, i.e. for units of
  $\mathbb{Z}[\sqrt{D}]$ itself, which is the classical Pell statement.

### Phase 2.2 — Lagrange's theorem on the continued fraction of $\sqrt{D}$

*Provenance: theory recalled from mathematical training; no web verification available in this run.*

**Statement (Lagrange, 1770; classical):** for positive non-square integer
$D$,
$$\sqrt{D} = [a_0; \overline{a_1, a_2, \ldots, a_{L-1}, 2a_0}],$$
with $a_0 = \lfloor \sqrt{D} \rfloor$, period length $L \ge 1$, and all
$a_k \ge 1$ for $k \ge 1$. Equivalently: the simple continued fraction of
$\sqrt{D}$ is periodic from the first term $a_1$ onward, and the last digit of
each period block is exactly $2a_0$. The block is palindromic:
$a_{L-j} = a_j$ for $1 \le j \le L-1$. (General Lagrange theorem: the CF of a
quadratic irrational is eventually periodic, and a periodic CF is a quadratic
irrational — Euler; the special form $[a_0; \overline{a_1,\ldots,a_{L-1},2a_0}]$
for $\sqrt{D}$ specifically is the classical corollary.)
Note: $\sqrt{D}$ itself is **not** purely periodic (its conjugate $-\sqrt{D}
< -1$ fails the Galois criterion $-1 < \xi' < 0$); the period starts at $a_1$,
not at $a_0$.

Hand checks (§2.6): $D=2$: $[1;\bar{2}]$, $L=1$; $D=3$: $[1;\overline{1,2}]$,
$L=2$; $D=5$: $[2;\bar{4}]$, $L=1$; $D=7$: $[2;\overline{1,1,1,4}]$, $L=4$;
$D=13$: $[3;\overline{1,1,1,1,6}]$, $L=5$. All palindromic blocks ✓.
The theorem statement itself is standard and I am fully confident of it.

### Phase 2.3 — Convergents and the fundamental solution

*Provenance: theory recalled from mathematical training; no web verification available in this run.*

**Definitions** (for any CF $(a_n)$):
$p_{-2}=0,\ p_{-1}=1,\ q_{-2}=1,\ q_{-1}=0$;
$p_n = a_n p_{n-1} + p_{n-2},\quad q_n = a_n q_{n-1} + q_{n-2}$ for $n \ge 0$;
$p_n/q_n = [a_0; a_1, \ldots, a_n]$ in lowest terms, $q_n \ge 1$.

**Standard identities** (induction):
(i) $p_n q_{n-1} - p_{n-1} q_n = (-1)^{n-1}$ for $n \ge 1$.
(ii) With the complete quotients $(m_k + \sqrt{D})/d_k$ of §2.4:
$p_n^2 - D q_n^2 = (-1)^{n+1} d_{n+1}$ (spot-checked on $D=7$, $n = 0..3$).
In particular $d_{n+1} = 1$ exactly when $L \mid (n+1)$ (standard fact, U4),
so at period boundaries:
$$p_{kL-1}^2 - D\,q_{kL-1}^2 = (-1)^{kL}, \qquad k \ge 1.$$
(iii) Every positive solution of $x^2 - Dy^2 = 1$ is a convergent:
$x/y = p_n/q_n$ for some $n$ (classical, Hardy–Wright level). Hence the
least-$x$ solution is the **first convergent with norm $+1$**.

**Fundamental-solution theorem:** let $L$ be the period length of $\sqrt{D}$.
$$(x_1, y_1) = \begin{cases}
(p_{L-1},\ q_{L-1}), & L \text{ even},\\
(p_{2L-1},\ q_{2L-1}), & L \text{ odd},
\end{cases}$$
since $p_{kL-1}^2 - D q_{kL-1}^2 = (-1)^{kL}$ first equals $+1$ at $k=1$
($L$ even) or $k=2$ ($L$ odd); by (ii)–(iii) no earlier convergent can have
norm $+1$ (norm $+1$ forces $d_{n+1} = 1$ and sign $+$). If $L$ is odd,
$(p_{L-1}, q_{L-1})$ is the least solution of $x^2 - Dy^2 = -1$, and
$(p_{2L-1}, q_{2L-1})$ equals $(p_{L-1}^2 + Dq_{L-1}^2,\ 2p_{L-1}q_{L-1})$.

**Algorithmic equivalent (what a program should do):** iterate convergents —
equivalently run §2.4 and accumulate $p_n, q_n$ — until $p_n^2 - D q_n^2 = +1$
first occurs; that convergent is $(x_1, y_1)$. Termination guaranteed within
$n \le 2L - 1$, i.e. within two periods.

Hand checks against the Phase-1 oracles (§2.6): $D=2$, $L=1$ odd → $(p_1,q_1)
= (3,2)$ ✓; $D=3$, $L=2$ even → $(p_1,q_1) = (2,1)$ ✓; $D=5$, $L=1$ odd →
$(p_1,q_1) = (9,4)$ ✓; $D=7$, $L=4$ even → $(p_3,q_3) = (8,3)$ ✓;
$D=13$, $L=5$ odd → $(p_4,q_4) = (18,5)$ with $18^2 - 13\cdot 25 = -1$, and
$(p_9,q_9) = (649,180)$ ✓.

### Phase 2.4 — Exact-integer continued-fraction iteration for $\sqrt{D}$

*Provenance: theory recalled from mathematical training; no web verification available in this run.*

Standard purely-integer (Euclidean-style) iteration, equivalent to the
complete-quotient recurrence of §2.3(ii):
$$m_0 = 0,\quad d_0 = 1,\quad a_0 = \lfloor \sqrt{D} \rfloor;$$
for $k \ge 1$:
$$m_k = d_{k-1} a_{k-1} - m_{k-1},$$
$$d_k = (D - m_k^2) / d_{k-1} \qquad \text{(exact division; all quantities integers by theory)},$$
$$a_k = \lfloor (a_0 + m_k) / d_k \rfloor.$$
Facts (standard): $d_k \ge 1$ (never zero), $|m_k| \le a_0$, all quantities
integers; the state $(m_k, d_k)$ is purely periodic of period $L$ for
$k \ge 1$; the period ends at the first $k \ge 1$ with $(m_k, d_k) = (a_0, 1)$,
equivalently with $a_k = 2a_0$, and $L$ is that $k$ ($d_k = 1$ iff $L \mid k$).

Hand checks: $D=2$: steps $(m,d,a) = (1,1,2)$ → $L=1$; $D=3$: $(1,2,1)$,
$(1,1,2)$ → $L=2$; $D=5$: $(2,1,4)$ → $L=1$; $D=7$: $(2,3,1),(1,2,1),(1,3,1),
(2,1,4)$ → $L=4$; $D=13$: $(3,4,1),(1,3,1),(2,3,1),(1,4,1),(3,1,6)$ → $L=5$.
Every division in these traces was exact.

Complexity note (qualitative only; no quantitative bounds asserted): per $D$
the loop runs $L$ iterations plus at most one more period; each step is
$O(1)$ big-integer operations; $p_n, q_n$ grow exponentially in $n$, so exact
multi-length arithmetic is needed for the final values (no magnitude claims
made here; see U5).

### Phase 2.5 — Chakravala (cyclic) method of Bhaskara II

*Provenance: theory recalled from mathematical training; no web verification available in this run.*

Independent classical algorithm for the fundamental solution **without
continued fractions** (Bhāskara II, 12th century; documented in the
*Bījagaṇita* tradition; modern reconstruction in the historical-mathematics
literature).

**Invariant:** maintain $(a, b, k)$ with $a^2 - D b^2 = k$.
- **Start:** $(a, b, k) = (a_0, 1,\ a_0^2 - D)$ with $a_0 = \lfloor \sqrt{D}
  \rfloor$ (then $a_0^2 - D \cdot 1^2 = k$ ✓; $k < 0$).
- **Choice of $m$:** choose integer $m$ with $k \mid (a + bm)$ — equivalently
  $m \equiv -a b^{-1} \pmod k$ when $\gcd(b,k)=1$ — minimizing
  $|m^2 - D|$ among admissible $m$ (conventionally $m \ge 0$; ties broken
  arbitrarily). **See U1:** the naive *signed* minimizer can collapse to the
  trivial solution.
- **Updates:**
  $$a' = \frac{a m + D b}{|k|},\qquad b' = \frac{a + b m}{|k|},\qquad k' = \frac{m^2 - D}{k}.$$
  Equivalently $a' + b'\sqrt{D} = (a + b\sqrt{D})(m + \sqrt{D})/|k|$ up to
  sign. **Exact-divisibility claims:** both numerators are divisible by $k$
  (standard; provable from $k \mid (a+bm)$ together with $a^2 \equiv D b^2
  \pmod k$ using $\gcd(b,k) = 1$, which the process maintains — see U2).
- **Invariant preservation:** by multiplicativity of the norm
  $N(a'+b'\sqrt{D}) = k(m^2-D)/k^2 = (m^2-D)/k = k'$, so
  $a'^2 - D b'^2 = k'$ (also a direct algebraic identity).
- **Termination:** iterate until $|k| = 1$. If $k = 1$, then
  $a^2 - Db^2 = 1$; the classical theorem asserts $(a,b)$ is the fundamental
  solution (termination and minimality are theorems of the modern
  reconstruction; not re-derived here — U3). If $k = -1$, take one final step
  $$(a, b) \leftarrow (a^2 + D b^2,\ 2ab),$$
  which is $(a + b\sqrt{D})^2$ in $\mathbb{Z}[\sqrt{D}]$; then
  $(a^2 + Db^2)^2 - D(2ab)^2 = (a^2 - Db^2)^2 = 1$.
- **Relation to §2.3:** if $L$ is odd the chain passes through the norm $-1$
  solution and the final squaring step mirrors the CF "odd $L$" formula; if
  $L$ is even the chain hits norm $+1$ directly (stated as theory, not
  verified in general here).

Hand checks (full traces in scratchpad.md): with the $m \ge 0$,
minimal-$|m^2-D|$ rule the method yields exactly the Phase-1 oracle values
$(x_1,y_1) = (3,2),(2,1),(9,4),(5,2),(8,3)$ for $D = 2,3,5,6,7$ and
$(649,180)$ for $D = 13$ (the latter via the $k=-1$ final squaring step);
and for the classical example $D = 67$ the chain
$(8,1,-3) \to (41,5,6) \to (90,11,-7) \to (221,27,-2) \to (1899,232,-7) \to
(3577,437,6) \to (9053,1106,-3) \to (48842,5967,1)$
reproduces the classical result $48842^2 - 67 \cdot 5967^2 = 1$ (recalled
value, used only as a consistency check of the algorithm, not as project
evidence). Traces validate the rules; they are not a proof of termination or
minimality.

### Phase 2.6 — What was / was not done in this phase

- Done: theory above recalled, cross-checked by hand arithmetic on small cases
  (oracles $D = 2,3,5,6,7,13$ and the classical $D=67$ chain); provenance and
  uncertainty flags recorded.
- Not done: no code written; no answers computed; no web access attempted
  (search disabled); no external sources existed or were cited.

### Phase 2.7 — Uncertainty flags

- **U1 (chakravala $m$-selection; MEDIUM-HIGH confidence after hand-checks):**
  the classical "minimize $|m^2 - D|$" statement needs a canonical-range /
  nonnegativity convention. I found that the *signed* minimizer can collapse
  to the trivial solution: $D=7$, start $(2,1,-3)$, admissible class
  $m \equiv 1 \pmod 3$: signed minimizer $m = -2$ gives $(a',b',k') = (1,0,1)$;
  analogously $D=67$ first step $m = -8$ collapses. The nonnegative-minimizer
  rule reproduces the classical chains. This is the least certain from memory;
  for Phase 3: use the CF route (§2.4) as the primary implementation and
  chakravala as the independent second route (with $m \ge 0$ rule and the
  $k=-1$ final step).
- **U2 (chakravala exact divisibility):** integrality of $(am + Db)/k$ given
  $k \mid (a+bm)$ is asserted by the method; my clean proof sketch needs
  $\gcd(b,k) = 1$ (maintained by the process). Standard-but-not-re-derived.
- **U3 (chakravala termination & minimality):** asserted as a theorem of the
  modern literature (the "rationale of the chakravala" analyses); not
  re-derived in this run. All hand traces (D = 2,3,5,6,7,13,67) support it on
  examples.
- **U4 (CF facts):** "every solution of $x^2 - Dy^2 = 1$ is a convergent of
  $\sqrt{D}$" and "$d_k = 1$ iff $L \mid k$" are standard textbook facts;
  high confidence, spot-checked on $D = 2,3,5,7,13$, not re-proved here.
- **U5 (complexity):** statements intentionally qualitative; no quantitative
  bound on $L$ or $x_1$ for $D \le 1000$ is asserted and no numeric values
  were computed in this phase (per task instruction).

## Phase 4 + 5 — Established results, execution, and verification

**Provenance:** computed results from two independent exact-integer programs
(`solution.py`, `verify_chakravala.py`); both verified against the Phase-1
statement oracles before their full runs. Theory provenance as flagged in
Phase 2 (no web verification available this run).

### Results (ESTABLISHED by computation, two independent routes)

- Minimal solutions of $x^2 - Dy^2 = 1$ for every non-square $D \le 1000$:
  `results_cf.tsv` (969 rows). Every row satisfies $x^2 - Dy^2 = 1$ exactly
  (asserted in both programs).
- **Answer: $D = 661$** (unique argmax; no ties) with
  $x = 16421658242965910275055840472270471049$ (38 digits),
  $y = 638728478116949861246791167518480580$.
- All statement oracles reproduced: D = 13 → (649, 180); D = 2,3,5,6,7 →
  (3,2),(2,1),(9,4),(5,2),(8,3); argmax over D ≤ 7 is D = 5, x = 9.

### Route 1 — continued fractions (`solution.py`)

Exact-integer CF iteration (m_k, d_k, a_k recurrences + convergent recurrences
p_k, q_k), stop at first $p_k^2 - Dq_k^2 = 1$. Rests on Lagrange periodicity
and the fundamental-solution theorem (convergent at L−1 if L even, 2L−1 if L
odd). Structural cross-check inside the script: for all 969 D, the reached
index n satisfies n = L−1 or n = 2L−1 with the independently measured period
length L — confirming minimality (fundamental solution) for every D.
Runtime 0.012 s.

### Route 2 — Chakravala (cyclic) method (`verify_chakravala.py`)

No continued fractions. Invariant $a^2 - Db^2 = k$; m ≡ −a·b⁻¹ (mod |k|),
m ≥ 0 minimizing |m² − D|; updates a′ = |(am+Db)/k|, b′ = |(a+bm)/k|,
k′ = (m²−D)/k; stop at |k| = 1; if k = −1 square the unit
(a,b) → (a²+Db², 2ab). Exact agreement with Route 1 on **all 969** D, same
winner D = 661. Oracle checks D=2,7,13 PASS before the comparison.
Runtime 0.011–0.021 s, exit 0.

### Minimality spot-check (brute force, small instances only, as a check)

For D ∈ {2,3,5,6,7,13}: no y in 1..y_found−1 makes 1 + D·y² a square;
PASS for all six. Not a solution method.

### Failed approaches / notes

- The naive *signed* chakravala m-minimizer collapses to the trivial solution
  (D=7, D=67 tests in Phase 2 scratch); the nonnegative minimizer with the
  two-candidate check (m₀, m₀+|k|) works. First agent runs failed on an
  infrastructure path-validation error (absolute paths rejected), not on
  content; retried with relative paths.

### Files

`solution.py` (primary), `verify_chakravala.py` (second route),
`results_cf.tsv` (table), `solution.md` (derivation + answer + verification),
`goal.md` (statement + oracles + completion criteria), `memory.md`,
`tasks.md`, `scratchpad.md` (hand traces). No external sources were used or
cited (web search disabled this run).