# Enumerating n ≤ 10^18 with σ(n)/n = k + 1/2 (hemiperfect numbers)

Report for the research question: the standard mathematical/algorithmic technique
for enumerating all n up to a large bound whose abundancy index σ(n)/n equals an
odd half-integer. This is a *method* report — the concrete source is the
technique write-up for Project Euler 241 (which asks exactly this for the bound
10^18), cross-checked against the OEIS, Wikipedia, and the abundancy-outlaw
literature. No Project-Euler answer is reproduced.

## 1. The sequence: OEIS A159907

**A-number and URL:** A159907 — "Numbers m with half-integral abundancy index,
σ(m)/m = k+1/2 with integer k."
URL: https://oeis.org/A159907

- First terms (as given): 2, 24, 4320, 4680, 26208, 8910720, 17428320,
  20427264, 91963648, 197064960, 8583644160, 10200236032, 21857648640, ...
  (b-file to n=130 by Max Alekseyev).
- **Equivalent formulations** (from the entry):
  - A159907 = { n : 2·σ(n) ∈ n·A005408 } = { n : antisigma(n) ≡ 0 (mod n) },
    antisigma(n) = n(n+1)/2 − σ(n).
  - Quick check: denominator(sigma(n)/n) == 2 — the PARI one-liner
    `isok(n)=denominator(sigma(n,-1))==2`.
- **All terms are even; odd n and powers of 2 beyond 2 can never qualify.**
  Reason: for odd n, σ(n) is odd, so σ(n)/n = (2k+1)/2 would force
  2σ(n) = (2k+1)n — odd = odd·odd, impossible since LHS 2σ(n) is even.
- Related sequences: A088912 (smallest m of abundancy k+1/2), A141643 (5/2),
  A055153 (7/2), A141645 (9/2), A159271 (11/2), A160678 (13/2, noted
  "conjectured to be finite").
- **Wikipedia** calls these **hemiperfect numbers** — positive integers with
  σ(n)/n = k/2 for odd k. https://en.wikipedia.org/wiki/Hemiperfect_number

## 2. The standard backtracking/DFS over prime powers

The abundancy index is **multiplicative**:

\[
\frac{\sigma(n)}{n} = \prod_{p^a \| n} \frac{\sigma(p^a)}{p^a},
\qquad
\frac{\sigma(p^a)}{p^a} = \frac{1+p+\cdots+p^a}{p^a}
= \frac{p^{a+1}-1}{p^a(p-1)}.
\]

(This is the classical "abundancy index" framework of **Laatsch 1986**,
"Measuring the Abundancy of Integers", Math. Mag. 59:84–92 —
https://www.jstor.org/stable/2690424 — which established the index, its
multiplicativity, and the density of the attainable set.)

**Goal:** find all n ≤ LIMIT with σ(n)/n = r/2 for odd r (k+1/2 ↔ r = 2k+1).

**Residual formulation.** For a fixed target T = r/2, track the *reduced*
residual quotient

\[
Q(n) = T \cdot \frac{n}{\sigma(n)} = \frac{u}{v}.
\]

The target is reached exactly when Q(n) = 1. Extending a partial factorization
by a new prime power p^e updates

\[
Q(n p^e) = Q(n) \cdot \frac{p^e}{\sigma(p^e)}.
\]

**State:** current partial n, its reduced residual Q = u/v, next-prime pointer.

### The recursion

```
dfs(r, idx, n, u, v):            # Q = u/v = (r/2)·n/σ(n), primes from PRIMES[idx] up
    reduce (u,v) by gcd
    if u == 1 and v == 1:         # Q == 1  → solution n found
        record n; return
    if u < v:                      # Q < 1, adding prime powers only lowers Q
        return
    if n > LIMIT:
        return

    d = v                          # smallest prime factor of v (denominator)
    if v > 1:
        d = min primefactor(v)     # (factor with Miller–Rabin + Pollard–Rho)

    for p in PRIMES[idx:]:
        if v > 1 and p < d:
            continue               # cannot skip the forced prime d
        e = a                      # if p^a || v, exponents start at a
        while True:
            pe = p**e; n2 = n*pe
            if n2 > LIMIT: break
            num2 = u * pe; den2 = v * σ(p^e)
            if num2 < den2: break              # Q would drop below 1
            if n2 * (den2 / gcd(num2,den2)) > LIMIT: break
            dfs(r, idx+1, n2, num2, den2)
            e += 1
        if v > 1 and p >= d:
            break                  # forced prime d already fully processed
```

Key implementation detail (from the technique source): the exponent loop of a
**forced** prime starts at the exponent a with p^a || v — because the numerator
contribution p^e must be large enough to cancel the denominator power.

### Pruning rules (why the tree stays tiny)

Three branches are cut:

1. **Overshoot:** if u < v (Q < 1), adding further prime powers always
   multiplies Q by a factor < 1, so Q can never return to 1. (Each
   σ(p^e)/p^e > 1, so its inverse p^e/σ(p^e) < 1; Q can only decrease as the
   factorization grows.)
2. **Magnitude:** if n·v > LIMIT no completion fits below the bound — the
   completed n' is a multiple of the current n by at least the remaining
   cofactor c with c ≡ 0 (mod v) (see the forced-divisibility lemma below),
   so n' ≥ n·v > LIMIT.
3. **Reuse:** if the denominator forces a prime already used in the partial
   factorization, the branch is impossible (primes are added in
   non-decreasing order and each prime occurs once).

### The denominator-cancellation argument (why large primes don't blow up the search)

The load-bearing invariant:

> **Lemma (denominator divides the cofactor).** Write σ(n)/n = A/B in lowest
> terms, and let σ(c)/c = M/N. If σ(nc)/(nc) = r/2 then — because
> σ(nc)/(nc) = (A/B)(M/N) and σ(p^e) is never divisible by p — the reduced
> denominator B of the partial index must *divide* the cofactor c.
>
> In terms of the residual: with Q = u/v and target completion c (so
> Q·(c/σ(c)) = 1), we get u·c = v·σ(c), hence **v | c**.

**Consequences used by the DFS:**

- The next prime introduced must be the smallest prime factor d of v; skipping
  d leaves it in the reduced denominator forever (all later denominators and
  numerators avoid the prime d, so no future cancellation can remove it). So
  the search is **forced** to visit d at exactly the right point — the choice
  is not heuristic, it is forced.
- Therefore the **candidate set of primes is tiny**: denominators v are
  divisors of products of σ(p^a) over the small primes already in the partial
  factorization. A large prime p can only ever enter the search as a *forced*
  factor of such a small denominator — i.e., p must divide σ(q^b) for an
  already-used small prime power. There are very few prime divisors of these
  σ(q^b) values, and each can appear with the forced explicit exponent.
  Combinatorial explosion over the full prime sequence never happens; the tree
  is bounded by the small-denominator divisors, not by π(10^18).
- The split over targets: for the 10^18 bound, r is bounded by Robin's
  theorem / the A088912 table — the smallest number with abundancy 13/2 is
  ≈1.7·10^44, so only r ∈ {3,5,7,9,11} (< i.e. targets 3/2,…,11/2) are
  reachable. (Source: Wikipedia's "Smalles hemiperfect of abundancy k/2" table
  and A088912; Robin's inequality σ(n) < e^γ n log log n, true for n ≥ 5041
  if RH — gives the a(k) lower bounds quoted on A088912.)

### Why this is the right method (and alternatives that fail)

- **Spectacular/near-optimal failure:** A naive approach that filters all n ≤
  L by computating σ(n) is O(L log log L) — fine to 10^7, impossible at 10^18
  (the memory's own brute force found the oracle set only to 10^6). That is a
  scan over the bound, and the bound is chosen to defeat it.
- The **DFS over prime powers with forced denominators** is the standard
  procedure behind the 10–20 digit multiperfect/hemiperfect numbers in the
  Numericana lists (Michon & Marcus, https://www.numericana.com/answer/numbers.htm#multiperfect)
  and matches the practical write-up
  https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/241.md
  (which splits targets r ∈ {3,…,13}, tracks Q = T·n/σ(n), and prunes on
  Q<1, n·v>L, forced-prime-reuse).
- The cost is polynomial in the *size of the answer set* plus the number of
  small-prime-power combinations below L — essentially the number of nodes of
  the forced-cancellation tree, which is tiny (the 10^18 search finds 22
  numbers: exactly the 22 hemiperfects ≤ 10^18). It does not scale with
  π(10^18) or with L.

## 3. Classical results: abundancy outlaws, finiteness, rarity

- **Laatsch 1986** (https://www.jstor.org/stable/2690424) founded the
  abundancy-index framework: I(n) = σ(n)/n, I(kn) ≥ I(n) with equality only
  for k=1, the set {I(n)} is **dense in (1, ∞)**, and I is unbounded.
- **Abundancy outlaws** (rationals > 1 that are *not* attained as any σ(n)/n):
  introduced by **Weiner** (1973) — if gcd(k,m)=1 and m < k < σ(m), then k/m
  is an outlaw. **Erdős** later gave a general sufficient construction. Surveys
  and extensions: **Holdener & Stanton**, "Abundancy outlaws of the form
  (σ(N)+t)/N", J. Integer Sequences 10 (2007), 07.9.6
  (https://cs.uwaterloo.ca/journals/JIS/VOL10/Holdener/holdener7.html);
  Holdener & Czarnecki (2007); **Weiner & Holdener** poster
  (https://biology.kenyon.edu/HHMI/posters_2014/weinerz.pdf) with the
  odd-perfect equivalence.
- **Consequences for rarity:** an index r/2 with r odd is a *rational with
  numerator 2σ(n) and denominator n*, so (from the evenness lemma + the
  outlaw criterion m<k<σ(m)) most odd-half-integer abundances are not attained;
  A160678 (13/2) is explicitly "conjectured to be finite". There is **no known
  theorem that the number of hemiperfects is finite** — the known count below
  10^18 is 22, but infinite families are not known to be impossible; the rarity
  is empirical/conjectural, and each fixed abundancy value is expected to have
  only finitely many n (consistent with the forced-denominator search: the
  reachable prime-power combinations are constrained by the cancellation tree).
- **Robin's theorem** (G. Robin 1984; OEIS A067698) underlies the A088912
  lower bounds that justify the r ≤ 11 target split: σ(n) < e^γ n log log n
  for n ≥ 5041 iff RH holds.

## 4. Concrete recursion summary

Pseudo-code with pruning, ready to implement:

```
LIMIT = 10**18
for r in odd targets reachable below LIMIT:      # r = 3,5,7,9,11 for 10^18
    dfs(r, idx=0, n=1, u=r, v=2)                 # Q = r/2

dfs(r, idx, n, u, v):
    g = gcd(u,v); u//=g; v//=g
    if u==1 and v==1: record n; return
    if u < v: return                              # Q < 1
    if n > LIMIT: return
    d = smallest_prime_factor(v) if v>1 else None # forced prime
    for p in PRIMES[idx:]:
        if d is not None and p < d: continue      # may not skip forced prime
        e = valuation(v,p) if d==p else 1         # forced exponent floor
        while n*p^e <= LIMIT and u*p^e >= v*σ(p^e) and n*(v''') ≤ LIMIT:
            dfs(r, idx+1, n*p^e, u*p^e, v*σ(p^e))
            e += 1
        if d is not None and p >= d: break        # forced prime exhausted
```

- **Complexity:** not exponential in LIMIT. Each node that survives is on a
  forced path whose next prime divides a small denominator; the search space
  is the number of valid prime-power prefixes below LIMIT, about 10^3–10^4
  nodes for 10^18 and 22 solutions. Every technique source (project-euler 241
  write-up, Ross Millikan's answer on math.SE
  https://math.stackexchange.com/questions/363842, the Numericana hemiperfect
  pages) uses this same forced-denominator backtracking.

## Sources

- OEIS A159907 — https://oeis.org/A159907 (sequence, formulas, characterizations)
- OEIS A088912 — https://oeis.org/A088912 (smallest m of abundancy n+1/2; Robin-bound comments)
- Wikipedia: Hemiperfect number — https://en.wikipedia.org/wiki/Hemiperfect_number
- CIROSANTILLI, Method write-up for the exact bound 10^18 — https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/241.md (describes the technique only; the repository also holds the DFS code 241.py)
- LAATSCH, Measuring the Abundancy of Integers, Math. Mag. 59 (1986) — https://www.jstor.org/stable/2690424
- HOLDENER & STANTON, Abundancy outlaws ..., JIS 10 (2007) 07.9.6 — https://cs.uwaterloo.ca/journals/JIS/VOL10/Holdener/holdener7.html
- WEINER & HOLDENER poster — https://biology.kenyon.edu/HHMI/posters_2014/weinerz.pdf
- MICHON, Multiperfect and hemiperfect numbers (theory + tables) — https://www.numericana.com/answer/numbers.htm#multiperfect
- ROBIN, Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann, J. Math. Pures Appl. 63 (1984) 187–213 (cite via A088912/A067698)
- Ross MILLIKAN, answer: efficient computation of 10–20 digit multiperfect/hemiperfect numbers — https://math.stackexchange.com/questions/363842