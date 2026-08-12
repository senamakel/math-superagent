# Exponent-signature enumeration with prime-assignment search

```approach
idea: Enumerate exponent signatures (multisets of exponents sorted nonincreasing) feasible for n ≤ 10^18, then for each signature determine if any assignment of distinct primes in nondecreasing order achieves a half-integer abundancy
mechanism: Every n = ∏ p_i^{e_i} has an exponent signature E = (e_1 ≥ e_2 ≥ ... ≥ e_r). The product constraint ∏ p_i^{e_i} ≤ 10^18 and the prime ordering (p_1 < p_2 < ... < p_r, with e_i nonincreasing) mean the minimum n for a given signature E is achieved by assigning the smallest primes in order: 2^{e_1}·3^{e_2}·5^{e_3}·... . The number of signatures with this minimum ≤ 10^18 is small — e_1 ≤ 59 and the product constraint limits r and the exponent values. Crucially, for a fixed signature E and a fixed target T = r/2, the function f(p_1,...,p_r) = ∏ σ(p_i^{e_i})/p_i^{e_i} is strictly decreasing in each p_i. This monotonicity means that for a given signature, there is at most a narrow range of prime assignments that can achieve T — and often none at all. The search flips the usual order: first fix HOW MANY of each prime power (the signature), then determine WHICH primes can realize the target. The signature enumeration is a bounded integer partition problem (product of p_min^e ≤ 10^18); the prime assignment is a monotonically constrained search over r-tuples of distinct primes. This is structurally different from the denominator-cancellation DFS which interleaves prime choice and exponent choice, building n multiplicatively from small primes up. Here the global shape is chosen first, and the primes are fit to it second. For small r (≤ 10 or so) and small exponents, the prime-assignment step can be solved by greedy/binary-search along each dimension, exploiting strict monotonicity.
status: grounded
first-step: Generate all exponent signatures E = (e_1 ≥ e_2 ≥ ... ≥ e_r) such that min_n(E) = ∏_{i=1}^r p_i^{e_i} ≤ 10^18 (where p_i is the i-th prime). Count them and verify the count is manageable (expected: a few thousand). Then for the simplest signature (single prime power: r=1), solve σ(p^e)/p^e = (2k+1)/2 for p prime — this is a finite check. For r=2, use the 2-prime shortcut from Alekseyev (complete-the-rectangle / Brahmagupta). For r ≥ 3, implement a monotone search over prime tuples. Validate against the brute oracle.
precedent: [Goto & Shibata, Math. Comp. 73(245) (2004) 475–491](https://www.ams.org/journals/mcom/2004-73-245/S0025-5718-03-01554-0/S0025-5718-03-01554-0.pdf) — Lemma 2.1 monotonicity of the divisor-ratio function (H(p^e)<H(p^f)<H(q^f) for e<f, p<q; H(nm)=H(n)H(m) for coprime factors). Cohen's theorem (only finitely many n with fixed ratio) via that paper. Claim ids: goto-shibata-multiplicative-monotone-method; Alekseyev's 2-prime shortcut (arXiv:2601.17832, Section 3.1). PLACEHOLDER: no direct published instance of the signature-first ordering found.
```

## What the literature says

The reformulation's two load-bearing claims are both **named, published results**, but the
*specific* "enumerate exponent signature first, then fit primes" ordering is **not, as far
as I could find, a distinct named method in the literature** — it is a re-ordering of the
same multiplicative monotone tree-search that Alekseyev and Flammenkamp perform. I say this
plainly rather than refuting it, because nothing shows it is *wrong*; it just reduces to the
standard method rather than being an independent one.

**What is solidly grounded (this is the named part):**

- *Goto–Shibata Lemma 2.1* (Math. Comp. 2004): H(n) = n·τ(n)/σ(n) is multiplicative and
  monotone in the sense H(p^e) < H(p^f) < H(q^f) for e<f and p<q, and H(nm)=H(n)H(m) for
  coprime factors. The abundancy index I(n)=σ(n)/n = 1/H(n)·(n/σ)(n)… is the multiplicative
  sibling; the same monotonicity drives the prime-wheel pruning. This is the fact that makes
  "for a fixed signature, replacing a prime by a larger one strictly decreases each
  σ(p^e)/p^e factor" true — the monotonicity the approach leans on holds here.
- *Cohen's finiteness* (as reported in Goto–Shibata): for any fixed integer c, only
  finitely many n have H(n)=c. This bounds the signature enumeration (only finitely many
  shapes can realise a given target / stay ≤ 10^18).

**Do the hypotheses hold here?** For the monotonicity: yes — σ(p^e)/p^e is strictly
decreasing in p for fixed e (p/(p−1) decreases), and I is multiplicative, so for a fixed
exponent signature the abundancy over prime assignments is strictly decreasing in each
coordinate. For the finiteness: H(n)=c refers to the harmonic mean, a different quantity
than σ(n)/n = k+1/2; the finiteness of fixed *half-integer abundancy* sets below a bound is
a separate (expected-finite, but not the same theorem) statement.

**Has anyone applied this to the problem?** Not as a standalone named approach that I found.
The tightest precedent is the Alekseyev p^k / pq shortcuts (Section 3.1 of arXiv:2601.17832):
for r=1 (a single prime-power cofactor) the search reduces to factoring a'−c' and testing
the prime-power factors — exactly the "r=1 signature" subcase this approach calls first. For
r=2, Alekseyev's complete-the-rectangle (Ap+B)(Aq+B)=B²−AC is the named 2-prime shortcut.
So the small-r signature cases are *already inside* the standard method; the approach is a
re-packaging, not a new theorem.

**What it would buy / cost:** a clean bound on the signature space (a bounded integer
partition problem) that is independent of 10^18, exploiting that the minimum n for a
signature is achieved by the smallest primes. But it carries a real risk the run's own
"state what would make it wrong" highlights: the claim "at most a narrow range of prime
assignments achieve T" is **a conjecture, not a theorem** — nothing in the literature bounds
the number of (p_1,…,p_r) tuples realising a fixed abundancy for a fixed signature, and the
m-dimensional monotone search could be expensive or discover multiple separated solutions.
Without a proof of that range, the method's pruning is heuristic, whereas Alekseyev's wheel
has a proved-completeness theorem (Theorem 3.3). That is the concrete reason the standard
wheel is preferred over this ordering.

Verdict: **not refuted, but not independently grounded** — its named ingredients (Lemma 2.1
monotonicity, Cohen finiteness, the p^k/pq shortcuts) are all real and hold here, yet the
distinct "signature-first" ordering has no direct published precedent I could find, and its
central range-bounding assertion is unproved (heuristic). Record that silence explicitly;
the approach is subsumed by [alekseyev-res-tree.md] and [two-adic-split-odd-search.md].

## Precedent / claim ids
- Goto & Shibata, Math. Comp. 73(245) (2004): Lemma 2.1 monotonicity, Cohen finiteness.
  Claim goto-shibata-multiplicative-monotone-method.
- Alekseyev arXiv:2601.17832 Section 3.1: p^k and pq shortcuts (named complete-the-rectangle /
  Brahmagupta) — these *are* the r=1 and r=2 signature cases.
- No direct published instance of the global signature-first ordering found; state as silence.
