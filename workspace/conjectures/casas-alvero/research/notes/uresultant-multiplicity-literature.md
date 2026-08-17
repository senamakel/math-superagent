# u-resultant multiplicity / tree-count facts: known or new?

Question under review: are these two facts about the Casas-Alvero ideal NEW to
the literature, and does any Samuel-multiplicity / complete-intersection /
tree-count statement appear anywhere?

> (1) On the traceless-slice CA scheme, ring QQ[a_2..a_n] with weight w(a_j)=j,
>     Hasse-resultant ideal I=(R_1..R_{n-1}), R_i=Res_x(f,H_i f), the weighted
>     order ord_0(R_i)=n(n-i) for each i, and the quotient length
>     |Q[a_2..a_n]/I| = n^(n-2) (Cayley's number of labeled trees).
> (2) The CA scheme in the traceless slice has Samuel multiplicity n^(n-2).

Sources checked (held + arXiv): Castryck–Laterveer–Ounaïes 2012 (d=12),
Draisma–de Jong survey 2011, Laterveer–Ounaïes 2012 constraints, Schaub–
Spivakovsky 2023/2024/2025 (JCA), de Frutos Marín 2013 thesis, Lu 2017
(computational AG, regular sequences), Ghosh 2024 finiteness (almost/complete
intersection), Diaz-Toca–Gonzalez-Vega 2006, Chellali 2012/2015, Massri 2018.

## Verdict — fact (1): KNOWN / SOURCED, the half with `ord_0(R_i)=n(n-i)`

De Frutos Marín's doctoral thesis (2013), Ch. 5.4 (held, ~line 8626), states
the order fact explicitly. In the traceless ring Z[a_2..a_{n-1}] with weight
gr(a_k)=k, each Hasse-resultant

    G<i> := Res(P_n, P_n^<i>),   P_n^<i> = (1/i!) P_n^(i) the Hasse derivative,

is a weighted-homogeneous polynomial, and she writes: "cada resultante K<i>
es homogénea de grado n(n−i), puesto que ese es el grado del polinomio
homogéneo pesado G<i> en el anillo Z[a_2..a_{n-1}] cuando precisamente se le
atribuye peso k a cada indeterminada a_k."

- Her `a_k := (−1)^k s_k` are the elementary symmetrics in the roots, with the
  traceless condition `x_1+…+x_n=0` exactly as the run's `a_1=0` slice. Weight
  of `a_k` = k matches `w(a_j)=j`. So this IS the run's fact (1) order.
- The engine is the classical statement (also in the thesis, lines 1614, 1715)
  that `Res(P,Q)` with deg P = n, deg Q = i is weighted-homogeneous of weighted
  degree n·i under weights equal to subscripts. For Hasse derivative i it gives
  ord_0 = n·i... *careful*: for Q = P_n^<i> of (formal) degree n−i the weighted
  degree is n·(n−i). So ord_0(R_i) = n(n−i). Consistent.

**Verdict: `ord_0(R_i) = n(n−i)` is published (de Frutos 2013, §5.4), not new.**
It is the classical weighted-homogeneity of the resultant specialised to the
traceless CA Hasse-resultants. The run's mechanical re-derivation (n=3..6,
Singular vdim + weighted-order product) confirms it; the novelty is only the
run's *explicit weight-(j) framing and the closed-form consequence*, not the
order itself.

## Verdict — fact (2): n^(n-2) quotient length & Samuel multiplicity: NOT in the literature

No held source and no arXiv result (queries "Casas-Alvero AND tree",
"AND Cayley", "AND Samuel", "AND multiplicity", "AND complete intersection")
computes the quotient length, the Samuel multiplicity, or the n^(n-2) =
Cayley tree count of the traceless-slice CA resultant ideal.

What the literature DOES have (and stops short of the run's fact):

1. **Complete-intersection / regular-sequence status** — the closest touching
   point, but it never computes the multiplicity:
   - Schaub–Spivakovsky (JCA 2025, arXiv:2312.08742; and 2023 bad-primes):
     CA in degree n ⟺ ht(R_1,…,R_{n−1}) = n−1 in K[a_1..a_{n−1}] (the
     "independent"/regular-sequence reformulation). Since the number of
     generators equals the height in a CM ring, in a degree where CA holds the
     R_i form a regular sequence, so the quotient is a 0-dim complete
     intersection. They prove only the partial R_i ∉ (…R_j..) for
     i ∈ {d−3,d−2,d−1}; the full regular-sequence ↔ CA is equivalent to the
     conjecture (unproved in general).
   - Lu 2017 (arXiv:1707.04754): proves a set of derivative parameterizations
     form regular sequences "easily" and uses this to compute *dimensions* of
     the varieties involved — an affine/dimension statement, no multiplicity
     and no length.
   - Ghosh finiteness (arXiv:2402.18717): the arithmetic CA scheme X_n and the
     intermediate X_n[j] have K-points forming an *almost* complete
     intersection; raising "when do they form a complete intersection"
     (Question 6.4). Still no Samuel multiplicity, no length, no tree count.

2. **The order product** — de Frutos states ord_0 = n(n−i) (fact 1) but NEVER
   takes the product ∏ n(n−i)/n! nor calls it a multiplicity or a tree count.

3. **Bezout/index interpretation** — the established run's own captures
   (code/out/uresultant_n4/n5/n6*.captured.txt) verify
   |Q[a_2..a_n]/I_n| = n^(n-2) for n=3,4,5,6 via TWO independent exact routes
   (Singular vdim AND the Samuel identity prod ord_0/prod w = prod n(n−i)/n!),
   and identify prod n(n−i)/n! = n^(n−1)(n−1)!/n! = n^(n−2). This is the run's
   own *identification with Cayley's labeled-tree count*.

**Verdict: the quotient-length/Samuel-multiplicity = n^(n−2) and its reading
as Cayley's tree count are NOT found in the literature — new-and-unpublished
as stated.** The underlying identity is classical (Valabrega–Valla 1978:
multiplicity of a complete intersection = product of initial orders, with
equality iff the associated graded is CM; the u-resultant/Lazard multiplicity);
what is new is (a) computing B = ∏ ord_0(R_i) for the CA slice and verifying
it equals the length, and (b) the identification B = n^(n−2) = #labeled trees.

## Caveat — fact (2) is NOT unconditionally equivalent to CA

`|Q[a_2..a_n]/I_n| = n^(n-2)` holds only in a degree where (R_1..R_{n−1}) is a
regular sequence of height n−1 (0-dim complete intersection), i.e. where CA
holds — and by Valabrega–Valla the Samuel identity (multiplicity = product of
orders) is strictly stronger than regularity. So fact (2) is a *certificate* in
verified degrees, not a route to an open degree. It holds in degrees 3..6
(computed); whether the pattern continues is open and tied to the
complete-intersection question.

## Does a Samuel / complete-intersection / tree-count statement appear ANYWHERE for the CA ideal?

- Valabrega–Valla identity: stated generically in the run's own note
  research/notes/uresultant-multiplicity-certificate-novelty.md and applied to
  CA only computationally. It is classical (Valabrega–Valla 1978; Rossi–Valla).
- Complete intersection: yes as a *question*/reformulation (Schaub–Spivakovsky
  height; Ghosh Q6.4), never as a computed multiplicity.
- Tree count n^(n−2): NO source links CA to Cayley's number of labeled trees.
  This is the run's new observation, verified computationally at n=3..6.

## Sources

- De Frutos Marín, *El problema de Casas-Alvero* (Ph.D. thesis 2013, held
  research/sources/defrutosmarin2013_thesis.full.md): §5.4 ~line 8626 =
  ord_0(R_i)=n(n−i); lines 1614, 1715 = classical resultant weighted degree.
- Schaub–Spivakovsky, JCA 17(2) 2025 (held): ht(R_1..R_{d−1})=d−1 ⟺ CA;
  partial R_i ∉ (…). arXiv:2312.08742; also 2307.05997 (bad primes).
- Lu, arXiv:1707.04754 (held): regular sequences, dimension of varieties.
- Ghosh, arXiv:2402.18717 (held): almost/complete intersection, Q6.4.
- Valabrega–Valla, *Form rings and regular sequences*, Nagoya 1978 (not held;
  classical): multiplicity = product of initial orders iff gr CM.
- Castryck–Laterveer–Ounaïes 2012 (held) d=12: the weighted-projective variety
  V_k(d,0) = (Res_x(F,F_H^(j))|j=2..d−1) with weights (d−2,…,1) — the same
  traceless-slice ideal — but only proves emptiness/CA-ness, never an order or
  multiplicity.
- Run captures: code/out/uresultant_n4.captured.txt (len 16, Samuel identity),
  uresultant_n5_multmap.captured.txt (vdim 125), uresultant_n6.captured.txt
  (vdim 1296), each ALL CHECKS PASSED, exact over QQ via Singular vdim + product
  of orders.

## Bottom line

- (1) `ord_0(R_i)=n(n−i)`: **KNOWN** — de Frutos Marín 2013, §5.4. The run
  re-confirms it mechanically; not new.
- (2) quotient length / Samuel multiplicity = n^(n−2) = Cayley's tree count:
  **NEW / NOT FOUND** in the held sources or on the arXiv. Depends (as a
  theorem) on the ideal being a complete intersection (= CA in that degree),
  which is why no source computes it unconditionally; and the Cayley-tree
  reading appears nowhere.

```claim
id: uresultant-order-n-n-i-sourced
statement: In the traceless-slice CA ring QQ[a_2..a_n] with weight w(a_j)=j, each
      Hasse-resultant R_i = Res_x(f, H_i f) is weighted-homogeneous of order
      ord_0(R_i) = n(n-i) at the origin.
hypotheses: f = x^n + sum_{j=2}^n a_j x^{n-j}, H_i the i-th Hasse derivative,
      Hasse resultants, char 0.
holds-here: yes
status: proved
bearing: fact (1) is NOT a new contribution — it is published in de Frutos
      Marín's thesis 2013 §5.4 (and follows from the classical resultant
      weighted-degree formula Res(P,Q) weighted deg = n·(n−i)); the run
      re-confirms it mechanically at n=3..6.
anchor: research/sources/defrutosmarin2013_thesis.full.md (~line 8626)
answers: uresultant-order-literature-novelty
```

```claim
id: uresultant-multiplicity-trees-new
statement: The quotient length |QQ[a_2..a_n]/(R_1..R_{n-1})| and Samuel
      multiplicity of the traceless-slice CA ideal equal n^(n-2), Cayley's
      number of labeled trees on n vertices.
hypotheses: same ring/setup as uresultant-order-n-n-i-sourced; additionally the
      ideal (R_1..R_{n-1}) is a regular sequence of height n-1 (an 0-dim
      complete intersection) — which holds iff CA holds in degree n.
holds-here: yes (verified computationally n=3,4,5,6)
status: checked
bearing: the n^(n-2) identification with labeled trees is NEW/unpublished —
      not in de Frutos, Schaub-Spivakovsky, Castryck et al, Lu, Ghosh, or any
      arXiv result; it depends on the complete-intersection status = CA, so it
      is a certificate in verified degrees, not an unconditional theorem.
anchor: research/notes/uresultant-multiplicity-certificate-novelty.md,
      code/out/uresultant_n4.captured.txt, uresultant_n5_multmap.captured.txt,
      uresultant_n6.captured.txt
follows-from: uresultant-order-n-n-i-sourced,
      samuel-multiplicity-product-of-orders (Valabrega-Valla)
answers: uresultant-multiplicity-literature-novelty
```
