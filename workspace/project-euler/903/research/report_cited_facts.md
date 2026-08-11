# Cited mathematical facts: permutations in one-line notation

Question: facts (with URLs) on (1) Lehmer/factorial rank, (2) k-th root counts in
terms of cycle structure, (3) identities for sums of ranks, (4) order/exponent of
S_n and bijectivity of the power map. Note: task is a contest-style computation;
per instructions NO Project Euler 903 source was used or cited. One search
accidentally surfaced a 903-solution page; it was disregarded.

---

## (1) Lehmer code / factorial number system → lexicographic rank

**Precise statement.** For a permutation σ = (σ_1,…,σ_n) of {1,…,n} in one-line
notation, define the Lehmer digits
    c_i(σ) = #{ j : i < j ≤ n, σ_j < σ_i },   (right inversion count at i)
so 0 ≤ c_i ≤ n−i. Then the 0-based lexicographic position (the number of
permutations of {1,…,n} strictly before σ in lexicographic order) is
    rank0(σ) = Σ_{i=1}^{n} c_i(σ) · (n−i)!,
and the 1-based rank is rank0(σ)+1. The map σ ↦ (c_1,…,c_n) is a bijection from
S_n onto the Cartesian product {0..n−1}×…×{0}, so rank0 bijects S_n onto
{0,…,n!−1}. Equivalently (c_1,…,c_n) is the factoradic representation of rank0.

Sources:
- https://handwiki.org/wiki/Inversion_(discrete_mathematics)  — explicitly gives
  rank(σ) = Σ_i r(i)·(n−i)! where r(i)=#{k>i: σ(k)<σ(i)}, 0≤r(i)≤n−i.
- https://en.wikipedia.org/wiki/Lehmer_code  — defines L(σ)_i=#{j>i: σ_j<σ_i},
  each L_i∈{0,…,n−i}, rank read as mixed-radix (base-1,…,base-(n−1)).
- https://en.wikipedia.org/wiki/Factorial_number_system  — factoradic digits give
  the lexicographic position (0-based); mixed-base place value (i−1)! for the
  i-th digit from the right. (Downloaded to research/factorial_number_system_wiki.md)
- https://bonetblai.github.io/reports/AAAI08-ws10-ranking.pdf  — Knuth's
  factorial/inversion-table ranking formula r(π)=Σ d_i (n−1−i)!.
- https://faabian.github.io/algebraic-combinatorics/blueprint/sect0026.html —
  Lehmer code, lex↔code order isomorphism (an algebraic-combinatorics lecturer
  note).

Check on the oracle: rank(2,1,3) = 3. c_1=#{j>1: σ_j<2}=1 (only σ_2=1<2), c_2=0,
c_3=0 → rank0 = 1·2! = 2, 1-based = 3. ✓ (verified here by hand and by
research/verify_facts.py in memory.)

---

## (2) Number of k-th roots of a permutation (cycle structure)

**Existence (Wilf/Knopfmacher–Warlimont).** Let σ have cycle type a, i.e. a_ℓ
cycles of length ℓ. σ is an m-th power (τ^m=σ for some τ) if and only if, for
every ℓ, a_ℓ is divisible by ⟨(ℓ,m)⟩ := ∏_{p|ℓ} p^{ν_p(m)} (the part of m supported
on the primes of ℓ). [Wilf, Generatingfunctionology Thm 4.8.2; restated as
Theorem 3 of Leaños–Moreno–Rivera-Martínez.] Note: when m is a prime p this
reduces to: cycles of length multiple of p must come in batches of p.

**Exact count.** [Leaños, Moreno, Rivera-Martínez, arXiv:1005.1531, Theorem 1.]
Let m be fixed positive, σ an n-permutation of type a=(a_1,…,a_n). For each ℓ with
a_ℓ≠0 define
    G_m(ℓ,a) = { g ∈ N : g ≤ a_ℓ, gcd(gℓ,m)=g },
with associate vector g=(g_1,…,g_k)=elements of G_m in increasing order, and
    E_m(ℓ,a) = { ε=(ε_1,…,ε_k) ∈ N_0^k : g_1ε_1+…+g_kε_k = a_ℓ }.
Then the number of m-th roots of σ is
    r^{(m)}(a) = ∏_{ℓ≥1, a_ℓ≠0}  a_ℓ! · Σ_{ε∈E_m(ℓ,a_ℓ)} ∏_{i=1}^{k}
                       ℓ^{(g_i−1)ε_i} / ( g_i^{ε_i} ε_i! ).
(The generator-form: Theorem 2 states the coefficient of a! times ∏ t_ℓ^{a_ℓ}
in exp( Σ_ℓ Σ_{g∈G_m(ℓ)} (ℓ^{g−1}/g) t_ℓ^g ) equals the count.)

Note: root counts do NOT appear in the Q(n) reduction — recorded here because the
question asked, and because the same G_m(ℓ) sets are exactly the grouping structure
that governs which powers share an exponent.

Sources:
- https://arxiv.org/pdf/1005.1531  (downloaded: research/leanos_mth_roots_of_permutations.full.md)
- https://doi.org/10.37236/1620  (Pouyanne, EGF + asymptotics: p_n(m) ~ π_m / n^{1−φ(m)/m})
- https://www.sciencedirect.com/science/article/pii/0012365X9490152X  (Chernoff,
  p^l-th roots: count by cycle types with j_k≡0 mod s for k≡0 mod d)
- https://doi.org/10.48550/arxiv.1907.00548  (Glebsky–Licón–Rivera, even/odd k-th roots)
- https://doi.org/10.48550/arxiv.1005.1531 also credits Pavlov 1980 (x^k=a in S_n)
  with the first explicit count.

---

## (3) Identity for the sum of ranks

Since rank0 bijects S_n onto {0,…,n!−1} (fact #1), each value occurs exactly once
among the n! permutations. Hence
    Σ_{σ∈S_n} rank(σ) (1-based) = 1+2+…+n! = n!(n!+1)/2,
    and the average 1-based rank is (n!+1)/2.
This is an immediate corollary of the bijection; it is asserted explicitly in
https://bonetblai.github.io/reports/AAAI08-ws10-ranking.pdf (average rank
(n!−1)/2 for 0-based) — searched several angles; no stronger "sum over a conjugacy
class" identity with a closed form was found in the standard references. The Q(n)
sum is over cyclic subgroups / powers of one π, NOT over whole classes, so this
identity does not by itself solve it — noted as a finding.

Sources:
- https://bonetblai.github.io/reports/AAAI08-ws10-ranking.pdf
- (the fact is a two-line corollary of the Lehmer bijection, which is cited above)

---

## (4) Order / exponent of S_n and bijectivity of the power map

**Exponent of S_n.** The exponent of S_n — the lcm of the orders of all its
elements, equivalently the smallest L with π^L = id for all π — is
    L(n) = lcm(1,2,…,n).
The order of an individual π equals the lcm of its cycle lengths, each of which is
≤ n, and a permutation realizes L(n) as its order; so the lcm over elements equals
lcm(1..n). The maximal element order is Landau's function g(n)=max over partitions
of lcm(parts), with log g(n) ~ sqrt(n log n) (Landau 1902).

**Power map bijectivity.** In any finite group G, the map g ↦ g^k is a bijection
of G if and only if gcd(k,|G|)=1. For G=S_n, |G|=n!, so π↦π^k is a permutation of
S_n iff gcd(k,n!)=1, i.e. iff k shares no prime factor ≤ n. (This is the same as
gcd(k, lcm(1..n))=1.)

**Cycle-level power fact.** For an m-cycle σ, σ^k splits into gcd(k,m) cycles of
length m/gcd(k,m); hence σ^k is still an m-cycle iff gcd(k,m)=1, and more generally
the cyclic subgroup ⟨σ⟩ consists exactly of the ord(σ) distinct powers (this is
the structural fact behind the Q(n) reduction "powers repeat with period ord(π)").

Sources:
- https://groupprops.subwiki.org/wiki/Kth_power_map_is_bijective_iff_k_is_relatively_prime_to_the_order
- https://math.stackexchange.com/questions/878625/when-is-a-power-of-an-m-cycle-also-an-m-cycle
  (σ^k splits into gcd(k,m) cycles of length m/gcd(k,m))
- https://en.wikipedia.org/wiki/Landau_function  and https://oeis.org/A000793
  (Landau's function = max order in S_n; exponent = lcm(1..n))
- https://people.tamu.edu/~yvorobets/MATH433-2010B/Lect2-02web.pdf (order, powers,
  exponent lcm(1..n))
- https://www.combinatorics.org/ojs/index.php/eljc/article/view/v27i1p6
  (Bamberg–Glasby–Harper–Praeger, permutations with order coprime to m — the
  distribution version of the same coprimality condition)

---

## Relevant previous work and gaps

- The run's earlier report (research/report_rank_powers.md) had already derived
  the reduction Q(n) = Σ_{H cyclic} φ(|H|) (n!/|H|) Σ_{τ∈H} rank(τ) and verified
  Q(2)=5, Q(3)=88 by hand. This note supplies the cited facts behind it.
- Of the four requested facts, only #3 has no non-trivial identity: there is no
  known closed form for Σ_{τ∈H} rank(τ) over a cyclic subgroup, which is the part
  that must be attacked to reach n=10^6 without enumeration.
