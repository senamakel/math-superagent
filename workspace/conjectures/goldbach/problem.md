# Goldbach's Conjecture (binary/strong form)

## Statement

> Every even integer $n > 2$ can be written as the sum of two primes:
> $$n = p + q, \qquad p, q \text{ prime}.$$

Posed by Christian Goldbach in a 1742 letter to Euler (Euler restated the
version above; Goldbach's own letter used a now-abandoned convention treating 1
as prime). It is **open** — nobody has proved it and nobody has produced a
counterexample, and it has resisted since 1742, so the working assumption for
this run is that a full proof is out of reach, and the deliverable is a
genuine partial result stated exactly, not a claim of the conjecture.

## What the statement does and does not say

- $n > 2$ and even. $n = 2$ has no representation ($1$ is not prime) and is
  excluded by hypothesis, not a counterexample.
- $p, q$ need not be distinct: $4 = 2 + 2$ is a valid representation.
- This is the **binary** (strong) Goldbach conjecture. Do not conflate it with
  the **ternary** (weak) Goldbach conjecture — every odd integer $> 5$ is a
  sum of three primes — which **was** proved unconditionally by Helfgott
  (2013, building on Vinogradov 1937 and a long chain of effective/computational
  work). The ternary result is a genuinely different, resolved theorem; use it
  only as a technique source, never cite it as resolving the binary case, and
  never let a run report "Goldbach is proved" on the strength of it.
- The conjecture is a statement about *every* even $n$, not almost every one.
  Results bounding the density of exceptions (below) are evidence and real
  mathematics, but are not a proof, exactly analogous to the Collatz workspace's
  distinction between "almost all orbits" and "every orbit" — the same failure
  mode applies here and must be avoided in this run's own reporting.

## Why it is hard, stated as the obstruction to beat

Primality is a multiplicative condition; $p + q = n$ is an additive one. The
conjecture asks that this additive equation have a solution in a
multiplicatively-defined set for *every* $n$, with no algebraic identity known
to bridge the two structures. The two families of tools that come closest each
stop short for a structural reason, not for lack of effort:

- **Sieve methods** (used to get Chen's theorem, below) can show $n = p + q_1 q_2$
  or $n = p + q$ (i.e. $q$ has at most two prime factors), but cannot sharpen
  "at most two prime factors" down to "prime" — this is the **parity problem**
  in sieve theory, a proven structural limitation of sieve methods themselves,
  not a gap waiting on a cleverer sieve. Any approach through sieves alone
  needs to either evade or genuinely break the parity problem, which no known
  technique does.
- **The circle method** (Hardy–Littlewood) predicts the count of
  representations $r(n)$ via the singular series and gets a full unconditional
  proof for the *ternary* problem (three summands smooth out the minor-arc
  error), but for the *binary* problem the minor-arc error terms are not
  currently controllable for all $n$ with known technology — only for almost
  all $n$ (density results, below).

That is the single sentence to keep in view: an approach that produces "at
most two prime factors" instead of "prime," or "almost every $n$" instead of
"every $n$," has produced real mathematics but has not touched the conjecture
itself — report it as exactly that, not as narrowing the open case.

## Where the literature is known to have got to

**These are leads to verify, not established facts.** Every one must be
checked against a primary source before anything is built on it, and any that
cannot be found must be recorded as unfound rather than assumed. Names, years,
and constants here are starting queries and may be wrong.

- Computational verification: exhaustive search has confirmed the conjecture
  for all even $n$ up to some large bound (recalled as being in the range of
  $4 \times 10^{18}$, attributed to Oliveira e Silva, Herzog, and Pardi, or a
  successor). Find the current record, the method (almost certainly a sieve
  plus incremental checking), and whether it has been extended since.
- Chen's theorem (Chen Jingrun, 1966/1973): every sufficiently large even $n$
  is $p + q$ where $q$ is either prime or a semiprime (product of two primes).
  Find the exact "sufficiently large" threshold if made explicit, and the
  proof technique (weighted sieve).
- Montgomery–Vaughan (1975): the number of even $n \le N$ that are *not* a sum
  of two primes is $O(N^{1-\delta})$ for some explicit $\delta > 0$. Find the
  stated $\delta$ and whether it has since been improved.
- Vinogradov (1937) / Helfgott (2013): the ternary conjecture, unconditionally,
  for all odd $n > 5$. Find Helfgott's exact statement, what remained to make
  it fully unconditional after Vinogradov (explicit minor-arc and
  major-arc bounds, and the finite computational check below the effective
  threshold), and whether any known reduction connects the ternary result back
  to a partial binary statement.
- The Hardy–Littlewood conjecture (their Conjecture A / the "Goldbach–Hardy–
  Littlewood asymptotic"): a precise predicted count
  $r(n) \sim 2C_2 \prod_{p \mid n,\, p > 2} \frac{p-1}{p-2} \cdot \frac{n}{(\log n)^2}$.
  Find the exact statement of $C_2$ (the twin-prime constant) and what, if
  anything, is proved about it versus purely conjectured.
- Conditional results under the Generalized Riemann Hypothesis: find whether
  GRH is known to sharpen the exceptional-set bound, shrink the effective
  threshold in Chen-type or circle-method results, or yield anything closer to
  the full binary statement conditionally.
- Linnik's work and later "almost Goldbach" results on the exceptional set,
  and any post-2013 (post-Helfgott) papers revisiting the binary problem —
  search recent literature explicitly rather than assuming nothing has moved.

## What counts as a result here

In descending order of value, and every one of these is a real contribution:

1. A proof for a natural restricted class of even $n$ (e.g. within a residue
   class, or under an extra multiplicative constraint), with hypotheses stated
   exactly.
2. A genuine sharpening of a known bound: a better $\delta$ in the
   Montgomery–Vaughan exceptional-set exponent, a lower computational
   verification bound pushed past the literature's record, or a tighter
   effective threshold in a Chen-type theorem.
3. A precise conditional result: statement $S$ (e.g. under GRH, or under a
   named quantitative hypothesis) implies a strictly stronger partial result
   than what is unconditionally known, with $S$ stated exactly.
4. A structural or reduction result: a clean necessary condition on a
   hypothetical minimal counterexample, or a reduction of the binary problem
   to a cleaner stated problem.
5. A counterexample. Astronomically unlikely given the verified range, and the
   bar for reporting one is a machine-checked, independently reproducible
   primality certificate for every candidate factorization attempt at the
   claimed $n$.
6. A formalisation in Lean 4 of the statement, and of whichever lemmas are
   proved along the way (e.g. a formal statement of Chen's theorem, cited as
   an axiom under `Cited` per this repository's Lean-library rule, not typed
   as `formalised`), with no `sorry` in anything this run actually proves.

Reporting the conjecture as proved, or reporting a density/almost-all/
sufficiently-large-$n$ result as resolving it, is the one outright failure
available on this run.
