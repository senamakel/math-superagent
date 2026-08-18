# First-occurrence window bound for the Fibonacci word (Cassaigne 2008)

```claim
id: fibonacci-first-occurrence-window-bound
status: recorded
hypotheses: f is the infinite Fibonacci word (fixed point of a->ab, b->a; the S_n
             limit of PE1006); Ln(w) = set of length-n factors; R'(n) = inf{N :
             Ln(f_0..f_{N-1}) = Ln(f)} = shortest prefix whose length-n factor
             set is complete.
statement: For the Fibonacci word f, the first-occurrence quotient
             rho'*(f) = limsup_{n->inf} R'(n)/n = Phi + 1 ~= 2.618,
           where Phi = (1+sqrt5)/2 (golden ratio), by Cassaigne, "On extremal
           properties of the Fibonacci word", RAIRO-ITA 42 (2008) 701-715,
           Sec. 3.2 / Theorem 3.4 context. Moreover R'(n) - n + 1 is the
           maximal first-occurrence position of a length-n factor, so a prefix
           of length ~ (Phi+1)·k contains every length-k factor.
evidence: asserted (sourced) — Cassaigne §3.2 "First occurrence" (lines 429-463) and §5 summary table: ρ′*(f)=Φ+1 stated in the running text; Theorem 3.4 itself is about the *other* Sturmian word u (slope (5−√10)/5) with ρ′*(u)=(29−2√10)/9≈2.519 < Φ+1≈2.618, and that is the optimal value across all non-eventually-periodic words. The Φ+1 for f is the paper's contrast value, not its Theorem 3.4 — do not cite Thm 3.4 for ρ′*(f).
bearing: justifies brute.py's "prefix length >= 3k is safe": 3 > Φ+1 ~= 2.618,
         and the documented worst cases (k=15 needs 35; k=30 needs 63) sit at
         35/15=2.33 and 63/30=2.1, both below 2.618. It also bounds directive 9's
         contiguous-window range {F_n - k - 1 .. F_n - 1} of q_n q_n, which must
         cover all first occurrences to be a complete factor set.
answers: (a source-level anchor for the prefix-length heuristic and the
         contiguous-window completeness; not an open request)
note: research/summaries/cassaigne-extremal-properties-fibonacci-word.md
source: https://www.numdam.org/article/ITA_2008__42_4_701_0.pdf
```

## Context

The library had the Sturmian factor-complexity machinery (p(k)=k+1, the k+1 distinct
length-k factors) and the mechanical/floor-sum construction, but no primary source
for how LONG a prefix (which S_n) is needed before the length-k factor set is complete.
That length is what brute.py's ">= 3k" heuristic and directive 9's contiguous-window
range depend on. Cassaigne's Sec. 3.2 supplies exactly it: the maximal first-occurrence
position of a length-k factor is <= (Phi+1)·k asymptotically = 2.618k.

This is distinct from the recurrence quotient rho*(f) = Phi+2 (Theorem 3.1), which is
about how quickly every block of length R(n) contains every length-n factor — not what
the prefix argument needs. The first-occurrence quotient rho'* is the relevant one.
