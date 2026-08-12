# Morgenstern, "Smallest entry in a 3×3 magic square of squares" (2007) — [[morgenstern-smallest-entry-8-digit.full]]

Develops a complete enumeration method for 3-square arithmetic progressions L², M_n², H_n² with a **fixed smallest value L** (L²=2M²−H²), and proves a lower bound on the smallest entry of a full MSS.

## What it establishes
- **Recursion structure:** all representations of L² = 2M²−H² with fixed L are generated from finitely many "generators" with L < H < 7L, via the forward recursion (M_{n+g}, H_{n+g}) = (3M_n+2H_n, 3H_n+4M_n). The number of generator sequences for L = ∏p^a is g = ∏(2a+1). Generators come in pairs (with a companion transformation), plus Hg=7L always.
- **Prime-factor reduction:** L and H need only have prime factors that are 8k+1 or 8k+7; an 8k+3 or 8k+5 prime factor of L forces a common factor of all entries (divide out to a smaller solution).
- **Magic-square condition:** the fastest step values satisfy H_i²+H_j² = H_k²+L² (eq. 4), with the step-value-additivity (a,b,a+b); a "termination theorem" shows once certain inequalities hold for g consecutive H_k, all further combinations are impossible — enumeration can stop.

## The bound
> **Claim (abstract):** all 9 entries of a 3×3 magic square of distinct squares must be at least the squares of 8-digit numbers.
Proof route: L=1 is impossible (the first three representations fail the magic condition), so the smallest entry can't be 1²; scanning L (with prime factors only 8k+1, 8k+7) terminates the enumeration for all L up to 7-digit magnitude, forcing the smallest entry L to be ≥ 10⁴ (an 8-digit square, i.e. L itself ~10⁴, L² ~10⁸). The claimed bound is 8-digit entries.

**Status caveat:** the impossible-L termination is proven for the *examined* L; the "all 9 entries are ≥ squares of 8-digit numbers" is the paper's stated PROVEN result from a complete enumeration. Treat the enumeration extent (L up to how far) as the operative content: the method enumerates entirely and terminates for each L that can't work. Not independently reproduced here.

```claim
id: morgenstern-smallest-entry
statement: All nine entries of a 3×3 magic square of distinct squares must be at least the
  squares of 8-digit numbers; in particular the smallest entry is > 10⁴. Uses the complete
  fixed-start enumeration of 3-square APs and a termination theorem.
hypotheses: all nine entries distinct integer squares; primitive up to a common square factor
holds-here: yes
status: asserted (claimed as proven by the paper's exhaustive enumeration; not reproduced here)
bearing: a concrete lower bound on the smallest entry; any solution has all entries ≥ 8-digit
anchor: research/sources/morgenstern-smallest-entry-8-digit.full.md
```

Structural note for this run: the three centre-line APs share the *smallest* value c−(a+b) in the 7-square configuration studied (not the centre), with steps a, b, a+b adding — this "same smallest value, steps (a,b,a+b)" view is a genuinely different parametrisation from the (c,u,v) centre view and is what drives the enumeration.
