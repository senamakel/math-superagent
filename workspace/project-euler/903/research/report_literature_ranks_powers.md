# Literature search: ranks of permutation powers, Lehmer sums over cyclic subgroups, and the f_n(k) structure

Date: 18 Sep 2025 (run 2). Question: is there literature on
(1) sum of Lehmer/factoradic ranks over the elements of a cyclic subgroup <pi> of S_n
    or over the powers pi^i of a fixed permutation;
(2) the count N(j,m) = #{(pi,i): 0<=i<n!, (pi^i)(m) < (pi^i)(j)}, empirically
    (n<=11) translation-invariant in j and exactly linear in the gap k = m-j;
(3) OEIS entries for A_n = 1,10,184,5052,191232,9851040,650626560,54052427520,
    5514150297600,680309947699200 and Q(n) = 5,88,4808,597876,133103808,47124948960.

## 1. Closest literature: expected descent/inversion statistics of powers of random permutations

**Cambie & Yan, "Descents and inversions in powers of permutations", arXiv:2408.01211** (Aug 2024).
This is the direct hit.  It proves, for uniform pi in S_n, explicit formulas for the
expected number of descents and inversions in the k-th power pi^k.

Theorem 1.1 (descents).  For k in Z^+ and n >= 2k+1,
  (1/n!) sum_{pi in S_n} des(pi^k) = (n-1)/2 - (tau(k)^2 - tau(k) - tau_o(k) + sigma(k)) / (2n),
where tau(k) = #divisors, sigma(k) = sum of divisors, tau_o(k) = tau(k / 2^{nu_2(k)}) = #odd divisors.

Theorem 1.2 (inversions).  For k in Z^+ and n >= 2k+1,
  (1/n!) sum_{pi in S_n} inv(pi^k) = n(n-1)/4 - (tau(k)-1) n/6
                                     - (tau(k)^2 - tau(k) - tau_o(k) + sigma(k)) / 12.
For odd prime k = p these simplify to (n-1)/2 - (p+1)/(2n) and n(n-1)/4 - n/6 - (p+1)/12.
The paper also confirms Archer-Geary's conjecture E[des(pi^2)] = E[des(pi^3)] = (n-1)/2 - 2/n.

WHY THIS IS THE STRUCTURE BEHIND f_n(k):  the proof (Section 2, Lemmas 2.1-2.6 +
Type 1-7 bookkeeping) gives, for a FIXED exponent k and fixed pair i < j with gap
d = j-i, the number of pi with an inversion at (i,j) in pi^k:

  Inv_k(i, i+d) = ( (n-d-1)(tau(k)n - tau(k)^2 - sigma(k))
                   + (n+d-3)(n - tau(k) - tau_o(k)) ) (n-3)! + tau_o(k) (n-2)!
                  + (constant type-1 term, independent of i,j,k),

which is (i) independent of i except through the gap d (translation invariance per
exponent), and (ii) affine in d (the d appears only in the two linear terms).  The
claimed edge counts are inside the proof of Theorem 1.2 ("the total number of ways to
have an inversion at i<j of these types").  Since our f_n(d) = sum over exponents
i=1..n! of the per-exponent counts (each (pi,i) pair counted once), and each
per-exponent count under the n >= 2k+1 hypothesis is translation-invariant and affine
in the gap, the gap-affine form f_n(k) = A_n + (k-1) B_n observed for n <= 11 is
exactly what this machinery predicts.

CAVEAT:  the n >= 2k+1 hypothesis only covers exponents k <= (n-1)/2.  For the large
exponents (k > (n-1)/2) in our sum the CY lemmas are not claimed, and a naive
extension fails:  summing the per-exponent slopes for n=3 gives 32 while the true
B_3 = 1 (hand computation; the high exponents contribute via pi^k = pi^{k mod ord(pi)}
structure, not via the CY formula).  So the linearity of the FULL f_n(k) for n<=11 is
a verified empirical fact whose mechanism is identified (per-exponent gap-affine
counts) but whose large-exponent regime still needs its own proof.  This is the main
open step toward a closed form.

**Archer & Geary, "Descents in powers of permutations", arXiv:2406.09369** (Jun 2024)
is the origin of the questions resolved by Cambie-Yan (Grassmannian permutation counts
for pi^2, pi^3; conjectures on expected descents in pi^2, pi^3).  Confirmed by CY.

## 2. OEIS: clean negative results

All lookups via oeis.org/search?q=...&fmt=text  (the &fmt=json endpoint returned
blocked/empty 4-byte payloads; fmt=text worked):

- 1,10,184,5052,191232,9851040  -> "No results"
- 5,88,4808,597876,133103808     -> "No results"
- 30,290,2464,23130,235080,2728368  (|B_n|/(n-1)! for n=6..11) -> "No results"
- two probe sequences (expected-inv derived values) -> "No results"

So neither A_n, nor Q(n), nor the normalized slope sequence is in the OEIS.  No
closed form, recurrence, or generating function is catalogued for these sequences.

## 3. Adjacent work found (marginal or ruled out)

- **Hultman, "Permutation statistics of products of random permutations", arXiv:1301.0430**:
  framework to compute expected statistics on products of t uniform permutations from
  a union of conjugacy classes, via mean-statistic expansion in irreducible S_n
  characters.  Methodological neighbour (expectation over group-distributed
  permutations) but for products, not powers; nothing about lexicographic rank.
- **Homomesy literature** (Propp-Roby 2011; LaCroix-Roby arXiv:2008.03292; Elder,
  Lafrenière, McNicholas, Striker, Welch arXiv:2206.13409, 122 proved homomesies):
  "statistic average constant over each orbit of a map".  RULED OUT for our
  statistic: the orbit {pi^i} of pi = id has average inv 0 while the orbit of a long
  cycle has positive average, so inv (and hence rank-related Lehmer digits) is not
  homomesic under the power map.
- **"Arithmetic functions and fixed points of powers of permutations"** (Archiv der
  Math. 120 (2023) 565-575, Springer link): the function k -> F(pi^k) (fixed point
  counts) determines the conjugacy class of pi.  Tangential; encodes cycle structure
  rather than rank statistics.
- **Legendre, "The number system of the permutations generated by cyclic shift",
  arXiv:1007.2870**: rank/unrank *within* the orbit of cyclic shifts (a specific
  cyclic subgroup of S_n), not sums over orbits, and not arbitrary powers.  One-line
  mention only.
- **Not found anywhere**: any closed form for rank(pi^i) as a function of i, any sum
  of Lehmer-code ranks over a cyclic subgroup <pi> of S_n, any formula for
  E[rank(pi^i)] over the (pi,i)-uniform distribution.  These remain unstudied in the
  literature; the homogeneous CY average (uniform pi, fixed power) is the closest
  published result.

## 4. Files and status

- research/cambie_yan_html.full.md — full text of arXiv:2408.01211 (theorems above from
  Section 1 and the proof of Theorem 1.2).
- research/archer_geary_descents_powers.full.md — full text of arXiv:2406.09369.
- research/oeis_*.md — the five OEIS "No results" pages.
- research/verify_cambie_yan.py — verification script (CY theorems vs literal
  enumeration for n=3..7; gap-affinity of extend_f.json rows; per-gap pair
  probability affineness).  WRITTEN BUT NOT RUN: this session has no code executor;
  run it to confirm before relying on its outputs.

NOTE / FLAG: one web search surfaced a GitHub "Project Euler 903" solution page.
Per task instructions (no PE solution pages) it was NOT opened and nothing from it
was used; it only confirmed (independently of us) that the problem is PE 903 and
that the published route also reduces Q(n) to pair-inversion expectations.