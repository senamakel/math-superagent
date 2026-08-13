# Elsholtz & Planitzer, "The number of solutions of the Erdős-Straus equation and sums of k unit fractions"

Source: https://arxiv.org/html/1805.02945 (arXiv:1805.02945), published as
C. Elsholtz and S. Planitzer, Proc. Roy. Soc. Edinburgh Sect. A 150 (2020)
1401–1427, DOI 10.1017/prm.2018.137.
Full text: `research/sources/elsholtz-planitzer-erdos-straus-counting.html.full.md`
(arXiv HTML).

## What it establishes (sourced, primary)

**Theorem 1**: for fixed m, the number of solutions of `m/n = 1/a₁+1/a₂+1/a₃`
(a_i positive integers) is at most `O_ε(n^{3/5+ε})`. This improves
Browning–Elsholtz (2011) and extends Elsholtz–Tao (2013, m=4, n prime) to all
fixed m.

**Corollary (algorithm)**: all solutions of m/n as a sum of three unit
fractions can be found in expected time `O_ε(n^ε (n³/m²)^{1/5})` — a
sub-polynomial-in-n search, i.e. the counting-parametrisation analogue of this
run's "search the ansatz, not the integers" principle, with the parameter
space reduced by divisor-function factors.

**Theorem 4 (lower bound)**: for fixed m and every reduced residue class
e mod f there are infinitely many primes p ≡ e (mod f) with

```
f_3(m,p) ≥ exp( ( (5 log 2)/(12 lcm(m,f)) + o(1) ) · log p / log log p ).
```

For m = 4, f = 1 this is `f_3(4,p) ≥ (log p)^{(5 log 2)/12 + o(1)}` along a
sequence of primes (exponent ≈ 0.2888). The Bloom–Elsholtz survey's "almost all
n have f(n) ≥ (log n)^{log 6 + o(1)}" is a related but different statement
(all n, not primes). I have NOT derived the survey's log 6 constant from
Theorem 4 — do not connect the two without reading the full text.

**Section 4 (structure most relevant to the run)**: "Patterns and relative
greatest common divisors" — the parametrisation of 3-term solutions of m/n via
relative gcd bookkeeping. This is the modern replacement for the classical
Type I/II story: solutions of m/n = 1/a₁+1/a₂+1/a₃ inherit a rigid divisibility
pattern from the gcds of the denominators, and the pattern determines which of
the two Mordell/Bloom–Elsholtz congruence families the prime denominator lands
in. Theorem 1's proof (Section 5, "Sums of three unit fractions", Lemma A)
runs through exactly this pattern analysis.

## Relation to the library

- This is the **[ElPl20]** paper erdosproblems #242 and the Bloom–Elsholtz
  survey cite for the counting results; it was the run's cited-but-not-stored
  gap until this download.
- Its upper bound `n^{3/5+ε}` is the tightest known for general m; the
  specialised m=4, n-prime case is Elsholtz–Tao (on disk) with the sharper
  `N (log N)^{2+o(1)}` average.
- Its Section 4 gcd-pattern parametrisation is the same object as
  Elsholtz–Tao Prop 2.1/2.5 (Type I/II) and Bloom–Elsholtz Theorem 1
  (two congruence families) — three independent modern statements of "3-term
  solutions have only two rigid shapes", all on disk now.

```claim
id: elpl20-three-term-upper-bound
statement: For fixed m, the number of positive-integer solutions of m/n = 1/a₁+1/a₂+1/a₃ is O_ε(n^{3/5+ε}); all such solutions can be found in expected time O_ε(n^ε (n³/m²)^{1/5}).
hypotheses: m fixed ≥ 1, ε > 0; a_i positive integers.
holds-here: true — with m=4 this bounds the number of 3-term representations of 4/n for arbitrary n (generalising Elsholtz–Tao's prime case); it quantifies how sparse the solution set is, hence how rigid any covering family must be.
status: sourced (Elsholtz–Planitzer 1805.02945, Theorem 1 + corollary, full text on disk).
bearing: the sparsity of 3-term solutions is why covering identities are highly constrained; supports the "two rigid shapes" picture for the ansatz search.
anchor: research/sources/elsholtz-planitzer-erdos-straus-counting.html.full.md
```

```claim
id: elpl20-many-solutions-residue-classes
statement: For fixed m and every reduced residue class e mod f with gcd(e,f)=1, there are infinitely many primes p ≡ e (mod f) with f_3(m,p) ≥ exp( ((5 log 2)/(12·lcm(m,f)) + o(1)) · log p / log log p ). In particular the open classes mod 840 each contain infinitely many primes with many solutions.
hypotheses: m, e, f fixed; e mod f reduced.
holds-here: true for each of the six open classes (take e = r, f = 840 with the appropriate m = 4): each contains infinitely many primes with at least exp((5 log 2)/(12·840) + o(1)) · log p/log log p) solutions — so the obstruction is covering, not scarcity of solutions.
status: sourced (Elsholtz–Planitzer 1805.02945, Theorem 4; the Bloom–Elsholtz survey's log 6 form is the same mechanism with m=4,f=1).
bearing: falsifies any claim that "the open classes have few solutions"; the six classes have plentiful per-p solutions, and only uniform covering families are missing.
anchor: research/sources/elsholtz-planitzer-erdos-straus-counting.html.full.md
```

## Consequence for this run

Nothing in this paper constructs a covering family for n ≡ 1 (mod 840) — like
all the counting literature it bounds solutions, it does not produce them.
Its value is (a) the algorithmic corollary — a sub-polynomial search for 3-term
solutions of m/n that the run's oracle could use to generate witnesses faster
than the current bounded sweep; and (b) the rigorous "many solutions in every
residue class" statement, which is the correct falsifier for any argument that
claims the open classes are sparse.