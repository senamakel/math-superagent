# Collatz — weakened versions

The goal with its difficulties switched off, rung by rung, weakest first. The
forward loop settles a rung; this file records which difficulties were off when
it did, and what turning the next one back on would take. A rung that failed
stays, with the reason.

```ladder
goal: For every positive integer n, the Collatz orbit n, T(n), T^2(n), ... eventually reaches 1, where T(n)=n/2 if n is even and T(n)=3n+1 if n is odd.
difficulties: all-n, unbounded-orbit, nontrivial-cycle, parity-independence-unproved, mixed-primes, irrationality-measure-of-log3-over-log2
status: open
```

## The difficulties, named as obstructions

- **all-n** — the quantifier ranges over *every* positive integer, not a residue
  class, a growth-bounded family, or a density-one set. Any result controlling
  only typical or almost-every orbit has switched this off and is *not* the
  conjecture; Tao's logarithmic-density-zero exception set is exactly this
  difficulty left on.
- **unbounded-orbit** — sub-claim (a): an orbit may diverge to infinity. The
  conjecture requires this be ruled out for every n, not almost every.
- **nontrivial-cycle** — sub-claim (b): an orbit may enter a cycle other than
  1→4→2→1. The conjecture requires this be ruled out for every n.
- **parity-independence-unproved** — the random-walk heuristic (expected
  multiplicative drift √3/2 < 1) assumes independence of consecutive parities,
  which is unproved. A worst-case argument is required; anything resting on the
  independence assumption has switched this off and settled a statistical
  shadow of the problem.
- **mixed-primes** — the map combines division by 2 (2-adic valuation, dependent
  on the *whole* residue of n mod 2^k as k grows) with multiplication by 3 plus
  an additive constant. No algebraic relation between 2 and 3 ties the two
  operations together, so no closed form for the k-step iterate of an
  *unprescribed* orbit exists.
- **irrationality-measure-of-log3-over-log2** — a cycle with p odd steps and q
  even steps forces 2^q close to 3^p, i.e. a small value of |q log 2 − p log 3|,
  and the *effective* irrationality measure μ of log 3/log 2 is what converts
  that into a lower bound on p, q, and the minimum element. Every cycle-exclusion
  bound is only as strong as the μ it rests on, and pushing μ down is a separate
  hard problem (linear forms in logarithms).

## Rungs, weakest first

```rung
id: R-small-n-direct
statement: For every positive integer n with 1 ≤ n ≤ 2^20, the Collatz orbit of n eventually reaches 1.
off: all-n, unbounded-orbit, nontrivial-cycle, parity-independence-unproved, mixed-primes, irrationality-measure-of-log3-over-log2
stance: open
merge: Settled by an exact, obviously-correct checker run once; the bound 2^20 is chosen so this is minutes of work, not a claim about the frontier. Every difficulty is off by *finiteness* — the check answers divergence and cycles within the range by inspection. Turning all-n back on means pushing the frontier, and the move is structural, not bigger: replace the per-integer check with a coverage/tree argument in the accelerated (Syracuse) form, so the verified bound moves without cost tracking the bound. That is where mixed-primes first re-enters — the tree argument must handle the 2-adic structure of 3n+1.
```

```rung
id: R-prescribed-parity-descent
statement: Let k ≥ 1 and let v ∈ {0,1}^k be a parity vector of weight a (a = number of odd steps), so b = k − a even steps. Writing T^k for the k-fold iterate of the plain map, the composition is affine: T^k(n) = (3^a·n + c_v)/2^b for an explicit non-negative integer c_v determined by v alone. Consequently, if 3^a < 2^b then every n whose first k orbit parities are v satisfies T^k(n) < n whenever n > c_v/(2^b − 3^a); each such residue class therefore has only finitely many members not forced below their start, and those are checked directly. Weakened target: prove the affine identity and the descent inequality, and enumerate the classes at k = 2^5 (or as far as the finite check reaches).
off: all-n, unbounded-orbit, nontrivial-cycle, parity-independence-unproved, mixed-primes, irrationality-measure-of-log3-over-log2
stance: open
merge: The first rung that is *infinite*: an explicit finite list of residue classes mod 2^k, each containing infinitely many n, all settled. Every difficulty is off, but differently from R-small-n-direct — all-n by restricting to the named classes, parity-independence-unproved because the parities are *prescribed* rather than modelled, unbounded-orbit and nontrivial-cycle because monotone descent rules both out inside a class, mixed-primes because the affine identity is exact and 2-adic consistency is respected. Two structural facts the forward loop must establish and not assume: (i) not every v ∈ {0,1}^k occurs — an odd step lands on 3n+1, which is even, so v has no two adjacent 1s, and the achievable v of weight a are counted by C(k−a+1, a), total Fibonacci F(k+2); (ii) the descent condition 3^a < 2^b is a/k < log 2/(log 2 + log 3) ≈ 0.3869, while the achievable weights are pinned at a ≤ ⌈k/2⌉ by consistency, with typical weight density 1/(φ+2) ≈ 0.276 (φ the golden ratio — the mean over the F(k+2) no-adjacent-1s strings). So the missed classes sit in the window [0.3869k, 0.5k] — a thin tail, but non-empty for every k ≥ 2, which is why this rung is genuinely weaker than the goal and not a disguised proof. Turning parity-independence-unproved back on is the whole gap: the classes this rung misses are exactly those, and no argument is known that handles an orbit whose parity weight sits in that window. First move: fix k, enumerate achievable v with 3^a < 2^b, compute c_v for each (a finite induction on v — Lean-provable), get the explicit threshold, and check the finite residue below it.
```

```rung
id: R-no-cycle-bounded-length
statement: There is no non-trivial Collatz cycle of length at most L = 1000, where a cycle is a finite orbit n → T(n) → ... → n with n ≠ 1 and length the number of steps to return.
off: all-n, unbounded-orbit, parity-independence-unproved, mixed-primes
stance: open
merge: nontrivial-cycle is ON but bounded, so the question is finite and exact: for each shape (p, q) with p + q ≤ 1000 and p/q ≈ log2/log3, the cycle condition is a linear equation whose solution must be a positive integer with the right parities — check all shapes. all-n is off because only cycles are asked about (divergent orbits are irrelevant here), unbounded-orbit off for the same reason. Turning the bound off — letting L grow past the exhaustive range — is where irrationality-measure-of-log3-over-log2 bites, and that is the next rung. First move: derive the exact cycle equation 2^q·n = 3^p·n + c for the shape, note it forces n = c/(2^q − 3^p), and observe that shapes with 2^q − 3^p ≤ 0 need separate handling; the whole thing is a finite table a program can emit and Lean can `decide` over.
```

```rung
id: R-no-cycle-via-diophantine
statement: Every non-trivial Collatz cycle with a odd steps and b even steps satisfies the exact relation n·(2^b − 3^a) = c(a,b) with c a positive explicit integer determined by the step pattern, hence 2^b > 3^a, i.e. b·log 2 > a·log 3 — so a cycle forces log 3/log 2 to be well approximated by the rational b/a. Combined with an effective irrationality measure μ for log 3/log 2 — i.e. |log 3/log 2 − p/q| > c₀/q^μ for all integers p, q ≥ 1 — this forces a lower bound on the cycle's minimum element as an explicit function of a, b, μ. Weakened target: state and prove that lower bound for the current best effective μ (value and constant c₀ to be taken from the literature, not guessed — request filed), and compute which cycle shapes it excludes.
off: all-n, unbounded-orbit, parity-independence-unproved
stance: open
merge: mixed-primes and irrationality-measure-of-log3-over-log2 are ON: the cycle is reduced to a near-integer relation between powers of 2 and 3, and the whole exclusion rests on μ. Note the index pairing carefully — the cycle gives log 3/log 2 ≈ b/a with a the odd-step count, so the approximating fraction's numerator is the *even*-step count; getting this backwards turns a lower bound into an upper one. Fully settled, this rung *is* sub-claim (b) — no non-trivial cycle, any length, any minimum element — one of the two halves of the goal. The obstruction that bites is irrationality-measure-of-log3-over-log2: the exclusion bound grows as a power of the minimum element set by μ, and a smaller μ excludes more; μ is not this run's to improve (that is a separate problem in linear forms in logarithms), so the rung's honest ceiling is set by the best published μ. First move: obtain the current best effective μ and its constant (request `current-best-effective-f5d1`), then derive the minimum-element lower bound as an explicit inequality in a, b, μ, c₀, and check it against the frontier the verification rung gives.
```

```rung
id: R-no-divergence-restricted-growth
statement: No Collatz orbit diverges to infinity under a growth restriction on the running maximum — concretely: if the running maximum of the orbit of n is at most n·C for a constant C, then the orbit does not diverge; equivalently, any divergent orbit must have unbounded-to-infinity relative maximum.
off: all-n, nontrivial-cycle, mixed-primes
stance: open
merge: unbounded-orbit is ON but restricted, and parity-independence-unproved is ON — the restriction is a *substitute* for the unproved independence, controlling the worst case by hypothesis instead of by argument. The form of the statement matters: a bounded-relative-maximum orbit has a parity sequence whose 3n+1-frequency is pinned near log2/log3, and pinning it strictly below that forces descent — which is exactly what makes the rung tractable and exactly what makes it weaker. Turning off the growth restriction is the full divergent-orbit sub-claim, open and with no known lever. First move: state the frequency condition precisely (density of odd steps along the first k steps), prove that density < log2/log3 implies eventual descent, and check what the bounded-maximum hypothesis forces the density to be. This is the rung where the ladder is most likely to stall, and if it does the finding is: the growth restriction is not merely convenient but *equivalent* to what independence would give.
```

```rung
id: R-full-conjecture
statement: For every positive integer n, the Collatz orbit of n eventually reaches 1.
off:
stance: open
merge: Every difficulty on. This is the goal, on the ladder only so the climb is visible; a rung that is the goal with nothing off is not a weakened target and no attempt should be booked against it. It closes only if R-prescribed-parity-descent covers all classes (it does not — the critical-weight classes are missed), R-no-cycle-via-diophantine excludes every cycle, and R-no-divergence-restricted-growth loses its restriction — three things no known argument does.
```

## What the ladder says about the problem

The two rungs with real mathematical content — R-prescribed-parity-descent and
R-no-cycle-via-diophantine — are on different axes, and the gap between them is
the shape of the open problem. The descent rung handles *prescribed* parity
sequences and misses exactly the critical-weight classes; the Diophantine rung
handles *cyclic* orbits, whose parity sequence is periodic and therefore
prescribable after the fact, which is why cycles are the tractable half. What
neither touches is an orbit whose parity sequence is neither prescribed nor
eventually periodic — and that is sub-claim (a) in one sentence.
