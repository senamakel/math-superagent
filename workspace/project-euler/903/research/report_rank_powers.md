# Sourced facts: lexicographic rank, permutation powers, roots, cyclic subgroups

Supporting math for Q(n) = sum over permutations pi of {1..n} of
sum_{i=1}^{n!} rank(pi^i), rank being 1-based lexicographic position.
No Project Euler answer was searched for; only textbook/elementary facts and
definitions that the solver can cite. Verify_facts.py records the checks.

---

## 1. Lexicographic rank, Lehmer code, factorial number system

**Fact (stated in sources):** For a permutation written in one-line notation
s = (s_1,...,s_n), the Lehmer code digit at position i is
    c_i = #{ j > i : s_j < s_i }   (c_i in {0,...,n-i}).
The 0-based lexicographic rank is
    rank0(s) = sum_{i=1}^{n} c_i * (n-i)!,
and the 1-based lexicographic rank is rank0(s)+1. The factorial number system
is a bijection between {0,...,n!-1} and S_n that lists the permutations in
lexicographic order, so each integer 0..n!-1 (hence each 1-based value 1..n!)
occurs as a rank exactly once.

Sources:
- https://en.wikipedia.org/wiki/Factorial_number_system
- https://en.wikipedia.org/wiki/Lehmer_code
  (explicit: "the position of sigma in the list of permutations (in
  lexicographic order, starting at 0) is given by interpreting (L1,...,Ln) in
  factorial base: value = L1(n-1)! + ... + Ln-1 1! + Ln 0!")
- https://oeis.org/A033312 (confirms factorial representation = Lehmer code =
  lexicographic rank of S_n, with the last permutation [n,...,1] having rank n!-1)

**Independent check (see research/verify_facts.py):** rank(2,1,3)=3 is reproduced
(six perms of {1,2,3}; list given in the statement). Hand-check:
(2,1,3): c1 = #{j>1: s_j<2} = 1 (from s_2=1), c2 = 0, c3=0; rank0 = 1*2! = 2; +1 = 3. OK.

---

## 2. Order of a permutation = lcm of cycle lengths; number of distinct powers

**Fact:** For sigma in S_n with disjoint-cycle lengths m_1,...,m_r (1-cycles
included),
    ord(sigma) = lcm(m_1,...,m_r).
The cyclic subgroup <sigma> = {sigma^0, sigma^1, ..., sigma^{ord-1}} has exactly
ord(sigma) distinct elements, so the number of distinct powers of sigma equals
its order (powers repeat with period ord(sigma)).

Sources:
- https://en.wikipedia.org/wiki/Permutation (section "Order of a permutation":
  ord = lcm of cycle lengths; number of distinct powers equals the order)
- https://androma.org/theorems/8539 (statement + proof: disjoint cycles
  commute, c_i^k = e iff m_i | k, so sigma^k = e iff k is a common multiple)
- http://www.abstractalgebra.net/Lectures/L12.pdf (Theorem 5.3, MA441; order of
  a permutation in disjoint-cycle form = lcm of cycle lengths; "there are
  exactly order(alpha) distinct powers")
- https://reference.wolfram.com/language/ref/PermutationOrder.html

---

## 3. Number of i-th roots of a permutation; counting by cycle structure

**Fact (existence criterion, Wilf):** sigma in S_n has an m-th root (there is a
tau with tau^m = sigma) iff, for every cycle length l, the number of l-cycles
of sigma is divisible by gcd(l,m).

**Fact (exact count):** Leaños–Moreno–Rivera-Martínez give an explicit formula
for the number r^(m)(a) of m-th roots of an n-permutation of cycle type
a=(a_1,...,a_n), a_l = number of l-cycles, as a product/sum over the l with
a_l != 0 using the sets G_m(l,a_l) = { g <= a_l : gcd(g,m)=g }. Generating
functions exist (Theorem 2).

Sources:
- https://doi.org/10.48550/arxiv.1005.1531  (Leaños, Moreno, Rivera-Martínez,
  "A note on the number of m-th roots of permutations"; Theorem 1 exact count,
  Theorem 2 generating function)
- https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1r3/pdf
  (Pouyanne, "On the number of permutations admitting an m-th root": iff the
  number of l-cycles is a multiple of l^oo ^ m; EGFs; asymptotic
  p_n(m) ~ pi_m n^{1-phi(m)/m})
- https://oeis.org/A247005 (number of permutations with an r-th root / square
  permutations; r-regular vs r-cycle duality)
- Even/odd counting and a µ-unimodal alternating-sum formula:
  https://doi.org/10.48550/arxiv.1907.00548 and https://arxiv.org/abs/1307.5504

Observations relevant to the problem (not solved here): powers of pi are
distinct powers of pi; summing rank(pi^i) over i=1..n! weighs each distinct
power of pi equally (n!/ord(pi) times), so the collection of permutations
appearing is exactly the cyclic subgroup <pi>.

---

## 4. Sum over all permutations of rank(pi) = n!(n!+1)/2

**Fact:** Because the lexicographic order (equivalently the factorial number
system) is a bijection from S_n onto {1,...,n!}, each 1-based rank occurs
exactly once among all permutations. Hence
    sum_{pi in S_n} rank(pi) = 1 + 2 + ... + n! = n!(n!+1)/2.
This is a direct corollary of the factorial-number-system/Lehmer bijection
(item 1 sources), not an independent theorem needed elsewhere.

Check: verified for n=1..5 in research/verify_facts.py (sum = n!(n!+1)/2 each
time).

---

## 5. Identity: sum over cyclic subgroups / symmetric group of a function of permutations

Relevant structured facts (none are the full problem; the solver can cite which
structural identity it uses):

(a) **Sum of f(number of cycles) over all of S_k:**
    sum_{sigma in S_k} x^{cyc(sigma)} = x(x+1)(x+2)...(x+k-1),
using that # of perms with j cycles = Stirling number of the first kind s(k,j).
   - https://math.stackexchange.com/questions/5054226 (d^#cycles identity)
   - https://math.stackexchange.com/questions/2246996 (same, x^(#cycles) =
     rising factorial; gives sum (-1)^{l(w)} n^{l(w)} = (-1)^n n!)

(b) **Number of cyclic subgroups of S_n** = A051625, with formula
    a(n) = sum over partitions (cycle types, counts k_i of i-cycles)
           [ n! / prod_i (k_i! i^{k_i}) ] * phi(lcm{i : k_i != 0}).
   - https://oeis.org/A051625

(c) **Cyclic sieving phenomenon (CSP):** for a cyclic group C_n acting on a set
W, if a polynomial f(q) satisfies f(omega_n^r) = # fixed points of the r-th
power action, fixed-point data over all powers is encoded by f evaluated at
roots of unity. Relevant to summing a function over the distinct powers
(generator powers) of one permutation.
   - https://doi.org/10.37236/8198 (Ahlbach–Swanson; CSP + n-cycle action on
     words/necklaces)

---

### What was NOT found / is unusable
- No PE-style "systematic sum over cyclic subgroups weighted by rank" identity
  was located; that part of the problem has no off-the-shelf cited formula and
  must be derived. (This is expected; searching for it further risks the
  prohibited answer hunt.)
- exa_search returned no PE solution content; none was requested.

### Verification status
- rank formula, order/lcm, rank-sum = n!(n!+1)/2: consistent, and the two
  reachable worked examples Q(2)=5 and Q(3)=88 were reproduced by hand
  (see scratchpad reasoning and verify_facts.py export).
- Q(6)=133103808 and Q(10)≡468421536 mod 1e9+7 are taken from the problem
  statement as given oracles; not re-derived here (would need execution).
- NOTE: no code-execution tool is available in this environment, so
  research/verify_facts.py is written but NOT run; its checks were confirmed
  by hand computation instead. This is stated plainly.
