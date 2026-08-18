# Cassaigne, "On extremal properties of the Fibonacci word" (RAIRO-ITA 42 (2008) 701–715)

Source: https://www.numdam.org/article/ITA_2008__42_4_701_0.pdf . DOI 10.1051/ita:2008003.
Full text: `research/sources/cassaigne-extremal-properties-fibonacci-word.full.md`.
Downloaded by librarian (this cycle). This is the first-occurrence/recurrence primary source the
library had been missing: it gives the first-occurrence window bound that justifies brute.py's
"prefix length ≥ const·k" and directive 9's contiguous-window range.

## What it establishes (verbatim statements)

Conventions: A = arbitrary alphabet, B = {a,b}; Fibonacci word f is the fixed point of
phi: a->ab, b->a; lengths |phi^n(a)| = F_{n+2}; golden ratio Phi = (1+sqrt5)/2. Ln(u) = set of
length-n factors; L(u) = all factors.

**First occurrence (Sec 3.2).** R'(n) = inf{ N : Ln(u_0..u_{N-1}) = Ln(u) } — the shortest prefix
length whose factor set of length n equals the full language. Then
rho'*(u) = limsup_{n->inf} R'(n)/n in [1, +inf].
**"R'(n) - n + 1 is the maximal position where a factor of length n occurs for the first time."**

**Theorem 3.1 + comment:** for a Sturmian word of slope alpha = [0; a1,a2,a3,...],
rho*(u) = 2 + limsup [a_n; a_{n-1},...,a_1]. The Fibonacci word has rho*(f) = Phi + 2 (lowest
possible for a Sturmian word).

**Theorem 3.4 (first occurrence, the load-bearing number):** rho'*(f) = Phi + 1 ≈ 2.618
for the Fibonacci word. (Optimality is NOT attained by f: the word u fixed by
a->abaababa, b->aba has rho'*(u) = (29 - 2sqrt10)/9 ≈ 2.519, and this is optimal; but
Phi + 1 ≈ 2.618 is the Fibonacci word's own constant.)

**Theorem 3.3:** for Sturmian u, rho*(u) = ind*(u).

## Bearing on PE1006

The problem's Ψ(k) sums squares over the k+1 distinct length-k factors (subwords). brute.py must
build a prefix long enough to contain every length-k factor at least once. The maximum first
occurrence position is R'(k) - k + 1, and rho'*(f) = Phi+1 means R'(k) ~ (Phi+1)·k ≈ 2.618k at
large k. This is the rigorous justification that the finite Fibonacci words S_n (prefixes of f)
stabilise the length-k factor set once the prefix reaches ~2.618k letters — the "≥ 3k is safe"
heuristic in the run's notes is comfortably above this constant. It also bounds directive 9's
contiguous-window range {F_n - k - 1 .. F_n - 1} of q_n q_n, which must cover all first
occurrences to be a complete factor set.
