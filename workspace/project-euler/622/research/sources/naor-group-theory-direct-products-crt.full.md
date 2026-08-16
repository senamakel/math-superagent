<!-- source: https://web.math.princeton.edu/~naor/homepage%20files/products.pdf | converted from PDF -->

Notes: c⃝ F.P. Greenleaf 2003 - 2008 v43-f05products.tex 12/05

Algebra I: Section 6. The structure of groups.

6.1 Direct products of groups.

We begin with a basic product construction.

6.1.1 Deﬁnition (External Direct Product). Given groups A1, . . . , An we deﬁne their
external direct product to be the Cartesian product set G = A1 × . . . × An equipped with
component-by-component multiplication of n-tuples. If a = (a1, . . . , an), b = (b1, . . . , bn) in the
Cartesian product set G, their product is

(1) a · b = (a1, . . . , an) · (b1, . . . , bn) = (a1b1, . . . , anbn) for all ai, bi ∈ Ai

The identity element is e = (e1, . . . , en) where ei is the identity element in Ai; the inverse of
an element is a
−1 = (a−1
1 , . . . , a−1
n ).

There is a natural isomorphism between Ai and the subgroup

Ai = (e1) × . . . × Ai × . . . (en) ,

the n-tuples whose entries are trivial except for ai. From (1) it is clear that

(a) Each Ai is a subgroup in G.

(b) The bijective map Ji(ai) = (e1, . . . , ai, . . . , en) deﬁnes an isomorphism from
Ai to Ai.
(c) The Ai commute with each other in the sense that xy = yx if x ∈ Ai, y ∈ Aj
and i ̸= j.

(d) Each Ai is a normal subgroup in G.

Note carefully, however, that the subgroup Ai need not commute with itself (the case when
i = j) unless the group Ai happens to be abelian.
The subsets H i = A1 × . . . × Ai−1 × (ei) × Ai+1 × . . . × An ⊆ G are also normal subgroups,
and in a group-theoretic sense the H i are complementary to the Ai. We have the following
properties.

(2)
 (i) H i ∩ Ai = (e)

(ii) G = A1 · A2 · . . . · An (product of subsets in G)

(iii) Each complement H i is a normal subgroup in G

(iv) Ai ∼= G/H i via the bijection fi : ai ↦→ Ji(ai)H i

6.1.2 Exercise. Verify the claims (a) – (d) regarding the subgroups Ai in a direct product
G = A1 × . . . × An. □

6.1.3 Exercise. Verify the relations (2) between the subgroups Ai ∼= Ai and their complemen-
tary subgroups H i. □

6.1.4 Exercise. Verify that the map fi : Ai → G/H i deﬁned in (iii) above is actually a
bijection, and that it is a homomorphism from Ai to the quotient group G/H i. □

The order of entries in an n-tuple makes a diﬀerence; therefore the Cartesian product sets
A1 × A2 and A2 × A1 are not the same thing (unless A1 = A2). For instance, are the direct
product groups Z3 × Z5 and Z5 × Z3 the same? What do elements in these groups look like?

1

However, in dealing with groups we only care whether they are isomorphic. It happens that
Z3 × Z5 ∼= Z5 × Z3 even though these groups are not “identical.”

6.1.5 Exercise. Let A1, A2, . . . be groups. Prove that the following product groups are iso-
morphic.

(a) A1 × A2 ∼= A2 × A1
(b) A1 × (A2 × A3) ∼= (A1 × A2) × A3 ∼= A1 × A2 × A3 (as deﬁned in (1))

(c) If one of the groups is trivial we get

A1 × (e) ∼= A1 (e) × A2 ∼= A2 □

In essence, the operation of forming the direct product of two groups is commutative and
associative, and the trivial group E = (e) acts as an “identity element.” The signiﬁcance of (b)
is that, up to isomorphism, we get the same group if we multiply groups together all at once,
as in (1), or multiply them successively two at a time.

6.1.6 Exercise. In the product group G = A×A the diagonal is the subset ∆ = {(a, a) : a ∈ A}

(a) Show that ∆ is a subgroup of G

(b) Show that ∆ ∼= G.

(c) Find a complete set of coset representatives for the coset space G/∆.

In general ∆ is not a normal subgroup of G × G. Can you see why? In (c) you are looking for a
set X ⊆ G that meets each coset g∆ in a unique point. Such a set is referred to as a transversal
for the space of cosets G/∆. □

6.1.7 Example. Euclidean space Rn equipped with vector addition (+) as a binary operation
is an abelian group. Its elements are deﬁned as n-tuples x = (x1, . . . , xn) of real numbers,
elements of the Cartesian product set R × . . . × R. Comparison of the sum

x + y = (x1 + y1, . . . , xn + yn)

with (1) shows that G = (Rn, +) is precisely the direct product group (R × . . . × R, +) made
up of n copies of the real line (R, +). □

6.1.8 Exercise. The set of integral vectors in Rn

Z
n = {x ∈ Rn : x = (x1, . . . , xn) with xi ∈ Z for all i}

is a group under vector addition (+). Explain why (Z
n, +) ∼= Z × . . . × Z. If {ui} is an R-basis
for Rn and Λ = {a1u1 + . . . + anun : ai ∈ Z} = Zu1 + . . . + Zun

prove that (Λ, +) is an abelian group isomorphic to (Z
n, +). What map ψ : Z
n → Λ eﬀects the
isomorphism? □

There is an important “internal” version of the direct product construction. Given a group
G and subgroups Ai ⊆ G we would like to know when G is isomorphic to the direct product
A1 × . . . × An. From (2) we can read out some obvious necessary conditions,

(3A) (i) Each Ai must be a normal subgroup in G.

(ii) The Ai must generate G in the sense that G is equal to the product set
A1 · · · An = {x1 · · · xn : xi ∈ Ai}
Furthermore it is evident from the deﬁnition of the direct product G = A1 × . . . × An that each
group element g has a unique decomposition as a product g = x1 · · · xn with xi ∈ Ai. That

2

imposes a third condition

(3B) (iii) Each g ∈ G has a unique factorization g = x1 · · · xn such that xi ∈ Ai.

Note that (ii) insures the existence of such a factorization while (iii) insures its uniqueness.
Conditions (i) – (iii) are also suﬃcient, but before we prove that we must work out a few
simple consequences of these hypotheses.

6.1.9 Exercise. Let G be a group and A, B two subgroups. Then the product set

AB = {ab : a ∈ A, b ∈ B}

is a subgroup if either A or B is normal, and the product is a normal subgroup if both A and
B are normal.
Note: Recall the discussion of Section 3.3, especially Exercise 3.3.14. □

6.1.10 Lemma. Let G be a group and A1, . . . , An subgroups that satisfy conditions (i) – (iii)
set forth in (3). Then the “complementary sets”

Hi = ∏

j̸=i Aj = A1 · . . . · Ai−1 · ei · Ai+1 · . . . · An

are normal subgroups that have the following “disjointness” property.

(4) Hi ∩ Ai = (e) for each 1 ≤ i ≤ n

Proof: By 6.1.9 the product AB = {ab : a ∈ A, b ∈ B} of two normal subgroups is again a
normal subgroup, hence Hi is normal, being the product of several normal subgroups. As for
disjointness, any g ∈ Hi ∩ Ai can be decomposed two ways

g = e · . . . · e · ai · e · . . . · e = a1 · . . . · ai−1 · e · ai+1 · . . . · an

These must agree. Unique factorization forces aj = e for all j, so g = e and the intersection is
trivial. □

Note: Except in the special case when there are just two factors, statement (4) is much stronger
than “pairwise disjointness” Ai ∩ Aj = (e) of the subgroups Ai when i ̸= j. An analogous
situation arises in linear algebra when we ask whether a family of vector subspaces V1, . . . , Vr ⊆
V is “linearly independent.” This does not follow from the pairwise disjointness condition
Vi ∩ Vj = (0), unless there are just two subspaces; instead, we must require that each Vi have
trivial intersection with the linear span Hi = ∑
j̸=i Vj of all the other subspaces. As a simple
example, consider three lines V1, V2, V3 (one-dimensional subspaces) in R3. These need not be
linearly independent if they are merely pairwise disjoint in the sense that Vi ∩Vj = (0) for i ̸= j;
they might, for instance, all lie in the xy-plane. But they are linearly independent if each Vi is
essentially disjoint from the 2-dimensional subspace Hi spanned by the other two lines. □

6.1.11 Lemma. Let G be a group and A1, . . . , An subgroups that satisfy conditions (i) and (ii)
of (3A). Then the following statements are equivalent

(iii) unique factorization: Each g ∈ G can be written uniquely as a product
g = x1 · · · xn with xi ∈ Ai.
(iii)
′ disjointness condition: The complementary subgroups Hi = ∏
j̸=i Aj
have the disjointness property Ai ∩ Hi = (e) for each 1 ≤ i ≤ n.

Proof: We’ve already proved (iii) ⇒ (iii)
′ in 6.1.10. To prove (iii)
′ ⇒ (iii), suppose some g
has distinct factorizations g = x1 · · · xn = y1 · · · yn, and let i be the smallest index such that
xi ̸= yi. Then x1 = y1, . . . , xi−1 = yi−1, and cancellation yields

xixi+1 · · · xn = yiyi+1 · · · yn
y−1
i xi = yi+1 · · · yn · x
−1
n · · · x
−1
i+1

3

The right hand product lies in the subgroup Ai+1 · · · An ⊆ Hi, while the left hand product
lies in Ai. We are assuming the intersection Ai ∩ Hi is trivial, so both products reduce to the
identity element e and we get xi = yi, contrary to the deﬁnition of i. Uniqueness of factorization
is proved. □

We are now ready to state the main result. We frame it in terms of the unique factorization
condition (iii), but by 6.1.11 we may replace (iii) with (iii)
′ if we wish.

6.1.12 Theorem (Internal Direct Product). Let G be a group and A1, . . . , An subgroups
such that

(i) Each Ai is a normal subgroup in G

(ii) The product set A1 · · · An is equal to G.

(iii) Each g ∈ G decomposes uniquely as g = a1 · · · an with ai ∈ Ai.

Then G is isomorphic to the direct product group A1 × . . . × An. In particular, elements of Ai
and Aj automatically commute if i ̸= j.

Proof: If i ̸= j we have pairwise disjointness Ai ∩Aj = (e) because Aj ⊆ Hj, and Ai ∩Hj = (e)
by 6.1.11. Using this we can show that Ai and Aj commute when i ̸= j. To see why, let
xi ∈ Ai, yj ∈ Aj and consider the “commutator” z = xiyjx
−1
i y−1
j . Since Aj is normal in G
the element z = (xiyjx
−1
i )y−1
j must lie in Aj; the same argument shows that z also lies in Ai.
Since i ̸= j, we get z = e by unique factorization. But xiyjx
−1
i y−1
j = e implies xiyj = yjxi, as
required.
The unique decomposition property (iii) means precisely that the map p(a1, . . . , an) = a1·. . .·
an from the Cartesian product set A1 × . . . × An to G is a bijection. It is also a homomorphism,
because if a = (a1, . . . , an), b = (b1, . . . , bn) we can make the following rearrangements of
commuting group elements

p(a)p(b) = a1 · · · an · b1 · · · bn
= a1b1 · a2 · · · an · b2 · · · bn
= a1b1 · a2b2 · a3 · · · an · b3 · · · bn
...

= a1b1 · a2b2 · . . . · anbn
= p(ab) (since ab = (a1b1, . . . , anbn))

Thus p is an isomorphism of groups. That ﬁnishes the proof. □

In view of this result, a group satisfying the conditions of Theorem 6.1.12 is often called an
internal direct product of the subgroups A1, . . . , An.
This decomposition theorem, and the notion of direct product, are most often applied when
there are just two factors. Then the decomposability criteria are much simpler, and direct
products structure G ∼= A × B is much easier to recognize.

6.1.13 Corollary. Let G be a group and A, B two subgroups such that

(i) A and B are normal subgroups in G.

(ii) The product set AB is equal to G.

(iii) A ∩ B = (e).

Then G is isomorphic to the direct product A × B under the map p(a, b) = a · b.

Proof: Combine 6.1.11 and 6.1.12 taking n = 2 □

The following examples illustrate the use of these results.

4

6.1.14 Example. The cyclic group G = Z4, with generator a = [1], is an abelian group of
order 4. So is the direct product G
′ = Z2 × Z2, whose elements can be written as

e = (0, 0) a = (1, 0) b = (0, 1) c = (1, 1)

where by abuse of notation we write k for the class [k]. Can these groups be isomorphic – i.e.
is the cyclic group a direct product of smaller subgroups? Answer: No. In G
′ every element
g ̸= e has order order o(g) = 2; in fact, writing (+) for the operation in Z2 × Z2 we have
(a, b) + (a, b) = (2 · a, 2 · b) = (0, 0). In contrast, G has a cyclic generator a such that o(a) = 4.
That’s impossible if G ∼= G
′. □

6.1.15 Example. Let G be the cyclic group (Z6, +). Since the order of any element in G must
divide |G| = 6, the possible orders are o(g) = 1, 2, 3, 6. The element a = [3] has order 2, since
[3] + [3] = [6] = [0], and the group A it generates has order |A| = 2; obviously A ∼= (Z2, +)
because, up to isomorphism, Z2 is the only group of order 2. Similarly, the element b = [2] has
order o(b) = 3, and generates a cyclic subgroup of order |B| = 3. Obviously B ∼= (Z3, +).
Since G is abelian, both A and B are normal subgroups. Furthermore, A ∩ B is a subgroup
of both A and B, and by Lagrange its order must divide both |A| = 2 and |B| = 3; that forces
A ∩ B to be trivial. Finally, the product set A + B is easily seen to be all of G. (We are writing
the group operation as (+) in this example.) By 6.1.13 we conclude that Z6 ∼= Z2 × Z3. This
cyclic group does decompose as the direct product of cyclic subgroups. □

What might account for the diﬀerent outcomes in the last two examples? A complete answer
will emerge eventually when we discuss the Chinese Remainder Theorem (below), but for the
moment it suﬃces to point out that the subgroups A, B in the second example are associated
with diﬀerent prime divisors of |G| = 6. There are no distinct prime divisors when |G| = 4 = 22.

6.1.16 Exercise. Do you think it possible to decompose the cyclic group (Z15, +) as a direct
product of smaller cyclic subgroups? How about the cyclic group (Z9, +)? Explain.
Hint: If G factors, what orders could the factors have? □

6.1.17 Example. Up to isomorphism, describe all groups of order |G| = 4.

Discussion: We procede by looking at the largest possible order o(b) for an element of G. By
Lagrange, the only possibilities are o(b) = 1, 2, 4; since o(b) = 1 ⇔ b = e the maximal order
cannot be 1.

Case 1: o(b) = 4. Then G is cyclic of order 4 and must be isomorphic to (Z4, +).

Case 2: o(b) = 2. Then all elements x ̸= e have order o(x) = 2, so that x
2 = e and x
−1 = x
for each x ∈ G. Pick any a ̸= e and let A = ⟨a⟩; obviously A ∼= Z2. Next pick any element
b /∈ A and let B = ⟨b⟩; obviously B ∼= Z2 too, but B ̸= A. The subgroup A ∩ B lies within
both A and B, and must be trivial; otherwise |A ∩ B| = 2 and A = B = A ∩ B, which has been
excluded by our choice of b.
We claim that the product set AB is equal to G. A sophisticated way to verify this is to
invoke Theorem 3.4.7 which says that |AB| = |A| · |B| / |A ∩ B| = (2 · 2)/1 = 4, and hence that
AB = G.
Finally we observe that G must be abelian. In fact if a, b ∈ G the element ab has e = (ab)
2 =
abab; if we then multiply on the right by b−1 and on the left by a−1 we get a−1b−1 = ba. But
a−1 = a and b−1 = b, so ab = ba as required. It follows that A and B are normal subgroups in
G, and hence by 6.1.14 that G is the internal direct product of these subgroups: G ∼= Z2 × Z2
in Case 2.
Thus, up to isomorphism, the only possibilities for a group of order four are the groups
G ∼= Z4 and G
′ ∼= Z2 × Z2 of Example 6.1.14. □

Here is an example in which previous results are used to exhibit the presence of direct product
structure in a group. It follows the lines of 6.1.17, except for the need to invoke the Cauchy
theorems (Cor. 4.3.3) to establish commutativity of the group.

5

6.1.18 Exercise (Groups of order p
2). Assume G is a ﬁnite group of order |G| = p2 for
some prime p > 1. Prove that G ∼= Zp2 or G ∼= Zp × Zp.
Hint: Use the Cauchy theorems and adapt the ideas developed in 6.1.17. □

6.1.19 Exercise. Prove that |A1 × . . . × Ar| = |A1| · . . . · |Ar| for any direct product of groups.
□

6.1.20 Exercise. Prove that the order o(x) of an element x = (a, b) in the direct product
group A × B is the least common multiple lcm(o(a), o(b)). Is a similar result true for direct
products of several groups?
Hint: Observe that x
m = e ⇔ am = e and bm = e. In any group, gm = e ⇔ m is a multiple of
o(g). □

6.1.21 Exercise. Is Z15 × Z4 a cyclic group – i.e. does it have an element of order 60? Does
Z15 × Z5 have elements of order (i) 75? (ii) 25? (iii) 15? (iv) 3? (v) any other order? □

6.1.22 Exercise. Identify all elements x = (a, b) of order o(x) = 5 in Z15 × Z5. Same for
Z15 × Z4. □

Ultimately we will have a lot to say about the structure of a ﬁnite group G in terms of the
prime divisors of its order n = |G|. There is one important case in which the outcome has a
striking simplicity.

6.1.23 Theorem. Let G be a nontrivial ﬁnite group of prime order |G| = p > 1. Then G is
isomorphic to the cyclic group (Zp, +). Furthermore, every b ̸= e is a cyclic generator.

Proof: Let b ̸= e and consider the cyclic subgroup H = {e, b, b2, . . . , bk−1}, with bk = e. By
Lagrange, |H| = k ≥ 2 must divide the order |G| = p of the whole group. Hence k = p and
H = G. □

Direct products and the Chinese Remainder Theorem. The Chinese Remainder The-
orem (CRT) has its roots in number theory but has many uses. One application completely
resolves the issues regarding direct products Zm × Zn mentioned in 6.1.14 - 16. The original
remainder theorem arose in antiquity when attempts were made to solve systems of congruences
involving several diﬀerent moduli ni

x ≡ a1 (mod n1)
... x ∈ Z

x ≡ ar (mod nr)

The notion of congruence is a modern one; the ancient chinese would have viewed this problem
as the search for an integer x with speciﬁed remainders ai after division by ni, i = 1, 2, . . . r.
Such systems do not always have solutions, but solutions do exist if the moduli n1, . . . , nr
are pairwise relatively prime, so that gcd(ni, nj) = 1 if i ̸= j, and then the solution x is unique
up to added multiples of the least common multiple m = lcm(n1, . . . , nr) of the moduli.

6.1.24 Exercise. Here are two systems of congruences

(a) { x ≡ 5 (mod 3)
x ≡ 1 (mod 12) (b) { x ≡ 5 (mod 3)
x ≡ 1 (mod 5)

Taking a “bare hands” approach, verify that the system (a) has no solutions and that the
solutions of (b) are of the form x0 + k · 15 where x0 = 11 and k ∈ Z.
Hint: If m, n > 1 recall our discussion in Chapter 2 where we showed that the greatest common
divisor c = gcd(m, n) is the smallest positive element in the lattice Λ = Zm + Zn. In particular:
(i) there exist integers r, s (which are not hard to ﬁnd by trial and error) such that gcd(m, n) =
rm + sn, and (ii) the elements in Λ are precisely the integer multiples of gcd(m, n). The moduli

6

m = 3, n = 5 are relatively prime in (b), with gcd = 1, but not in (a). □

6.1.25 Exercise. Recall that if a1, . . . , ar > 0 their greatest common divisor gcd(a1, . . . , ar)
is equal to the smallest positive element in the lattice of integer-linear combinations Λ =
Za1 + . . . + Zar. (The proof is the same as when r = 2.) We say that the ai are jointly relatively
prime if this gcd = 1. Prove that

(a) (Pairwise relatively prime) ⇒ (Jointly relatively prime)

(b) Give an example showing that the converse does not hold. □

To keep things simple let’s consider a system involving just two congruences

(5) x ≡ a1 (mod m) x ≡ a2 (mod n)

This remainder problem is completely equivalent to a problem in group theory: the system is
solvable for every choice of a1, a2 on the right if and only if the direct product group Zm × Zn
is cyclic – i.e. if and only Zm × Zn ∼= Zmn.

6.1.26 Theorem (Chinese Remainder Theorem). If m, n > 1 are relatively prime, so
that gcd(m, n) = 1, then Zm × Zn ∼= Zmn as additive groups. Furthermore, the system of
congruences (5) has a solution for every choice of a1, a2 ∈ Z, and if x0 ∈ Z is one solution the
full set of solutions in Z is the congruence class x0 + Zmn.

Proof: To keep track of the three diﬀerent types of congruence classes we write [k]m =
k + Zm, [k]n = k + Zn, [k]mn = k + Zmn to distinguish them. Now observe that any element
[k]mn in Zmn determines well-deﬁned classes [k]m, [k]n in Zm, Zn having the same representative
k. That is, the correspondences

[k]mn ↦→ [k]m and [k]mn ↦→ [k]n

determine well deﬁned maps from Zmn into Zm and Zn respectively. In fact, if k′ is any
other representative of the class [k]mn, that means k′ = k + s · mn for some integer s. But
k′ = k + (sn)m is congruent (mod m) to k and hence [k′]m = [k]m; likewise [k′]n = [k]n.
We now create a map ψ from Zmn to the Cartesian product set Zm × Zn by setting

(6) ψ([k]mn) = ([k]m, [k]n) ∈ Zm × Zn for all [k]mn in Zmn

This map is well-deﬁned independent of how we choose representatives k of elements of Zmn.
It is immediate from the deﬁnition that ψ intertwines the (+) operations in the additive groups
Zmn and Zm × Zn because

ψ([k]mn + [ℓ]mn) = ψ([k + ℓ]mn) = ([k + ℓ]m, [k + ℓ]n)

= ([k]m + [ℓ]m, [k]n + [ℓ]n)

= ([k]m, [k]n) + ([ℓ]m, [ℓ]n) (defn. of (+) in Zm × Zn)
= ψ([k]mn) + ψ([ℓ]mn)

Thus ψ : (Zmn, +) → (Zm, +) × (Zn, +) is a homomorphism of abelian groups.
So far we have not used the hypothesis gcd(m, n) = 1, which is needed to show that ψ is
one-to-one. (It will then be surjective too, because the sets Zmn and Zm × Zn have the same
cardinality mn.) If two points in Zmn have the same image, with ψ([k]mn) = ψ([ℓ]mn), that
means the components in Zm × Zn must match up, so that

(7) { [k]m = [ℓ]m
[k]n = [ℓ]n which means that { k − ℓ is divisible by m
k − ℓ is divisible by n

In general, divisibility m|k and n|k is not enough to insure that an integer k is divisible by mn
(try m = 4, n = 2, k = 8). But if m and n are relatively prime then they have no prime factors
in common and the product must divide k. In our setting this tells us that

mn divides k − ℓ ⇒ k − ℓ ≡ 0 (mod mn) ⇒ k ≡ ℓ (mod mn)

7

□ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □
□ □ □ □ □ □ □ □ □ □ □ □

Figure 6.1 The product group Zm × Zn represented as an m × n array. The
element 1 = (1, 1) and its iterates are shaded. In this portrayal the array is
7 × 12; since gcd(7, 12) = 1 the iterates will cycle once through each point in the
array before returning to position 1.

so that [k]mn = [ℓ]mn, as required to show that ψ is one-to-one. The map ψ is the desired
isomorphism between groups.
To connect all this with the remainder problem, if m, n are relatively prime the element
1 = ([1]m, [1]n) must be a cyclic generator for Zm × Zn because it is the ψ-image of the
generator [1]mn in the cyclic group Zmn. Given a1, a2, consider the element a = ([a1]m, [a2]n)
in the product group. Then some multiple of 1 is equal to a, say a = k · 1. Then

([a1]m, [a2]n) = a = k · 1 = (k · [1]m, k · [1]n) = ([k]m, [k]n)

so that k ≡ a1 (mod m) and k ≡ a2 (mod n), which is the same as saying that x0 = k is
a solution of the congruence (5). If k′ is another solution then k′ · 1 = a = k · 1 so we get
(k′ − k) · 1 = a − a = 0 = ([0]m, [0]n). But 1 has order mn, being the generator of Zmn, so this
happens ⇔ (k′ − k) is a multiple of mn. The full set of solutions is therefore x0 + Z · mn as
claimed. □

The converse of this theorem is not true. For example, gcd(2, 4) > 1 and the direct product
Z4 × Z2 is not isomorphic to Z8: the maximal order of any element x in the product group is
4 because 4 · ([k]4, [ℓ]2) = (4[k]4, 4[ℓ]2) = ([0]4, [0]2). But Z8 has a cyclic generator of order 8.

6.1.27 Exercise. Is Z45 ∼= Z9 × Z5? Is Z45 ∼= Z15 × Z3? Prove or explain why not.
Hint: Compare orders of elements. □

6.1.28 Exercise. In Z7 × Z12 there is some exponent k such that

k · 1 = k · ([1]7, [1]12) is equal to ([3]7, [−4]12)

Find a k that does this. Then ﬁnd a “normalized ” solution lying in the range 0 ≤ k < 7·12 = 84.
□
 The underlying idea of this proof is illustrated in Figure 6.1 where we represent Zm×Zn as an
m×n array of squares. Counting from the bottom left square 0 = (0, 0), the element 1 = (1, 1) is
the dark shaded square and its “powers” 1, 1+ 1 = (2, 2), . . . move diagonally upward until they
hit an edge, at which point they re-enter the array from the opposite edge. If gcd(m, n) = 1 all
squares get hit exactly once until we ﬁnally arrive back at 0 = mn · 1; the pattern then repeats.
This observation tells us how to compute the inverse ψ−1 : Zm ×Zn → Zmn of our isomorphism.
A pair a = ([a1]m, [a2]n) maps back to [k]mn in Zmn ⇔ k is the ﬁrst integer k = 0, 1, 2, . . . such
that k · 1 = a. This k is of course the desired solution of the congruence system (5), so knowing
how to compute ψ−1 is equivalent to being able to solve the remainder problem.

Systematic solution of remainder problems. Start by working backward: if x is a solution to
(5) then there exist k, ℓ ∈ Z such that x = a1 + km = a2 + ℓn, and hence a2 − a1 = km − ℓn.
Conversely, given k, ℓ satisfying the latter identity we could recover x as a1 + km or a2 + ℓn,
which automatically have the same value. So, we procede as follows

8

Step 1. Using the fact that gcd(m, n) = 1, ﬁnd integers r, s such that 1 = rm + sn =
rm− (−sn). (There are fast algorithms for doing this, see Chapter 2; it is easy using
a calculator if m and n are not too large.)

Step 2. Then

(a2 − a1) = (a2 − a1)(rm + sn) = (a2 − a1)r · m − (−1)(a2 − a1)s · n

and we may take k = (a2 − a1)r, ℓ = (−1)(a2 − a1)s.

Step 3. x0 = a1 + (a2 − a1)rm = a2 − (a2 − a1)sn is a basic solution to (5). All
others lie in the set x0 + Zmn.

6.1.29 Exercise. Use the method outlined above to ﬁnd the solutions of the congruence
problem x ≡ 14 (mod 18) x ≡ −2 (mod 25)

Find a particular solution lying in the range 0 ≤ x < 480 = lcm(18, 25). □

The CRT can be generalized in many ways. It can be made to work, with essentially the
same proof, for systems of arbitrary size provided we require that the moduli n1, . . . , nr be
pairwise relatively prime, so that gcd(ni, nj) = 1 if i ̸= j. This is a much stronger condition
than saying gcd(n1, . . . , nr) = 1, which means that no prime p > 1 divides every ni.

6.1.30 Exercise. Using induction on r prove that Zn1n2...nr ∼= Zn1 × . . . × Znr if the ni are
pairwise relatively prime (so gcd(ni, nj) = 1 if i ̸= j). □

6.1.31 Exercise. Give an example of integers n1, n2, n3 > 1 that are jointly relatively prime
(so that gcd(n1, n2, n3) = 1: there is no single prime p such that p|ni for all i) but the ni are
not pairwise relatively prime (so gcd(ni, nj) = 1 and ni, nj have no primes in common if i ̸= j).
□
 In another direction, we observe that Zn comes equipped with both a (+) and a multi-
plication operation (·), making it a commutative ring with identity as in Chapter 2. One can
deﬁne a direct product R1 × R2 of commutative rings very much as we deﬁned direct product
of groups, by imposing the following sum and product operations on the Cartesian product set
R1 × R2 = {(a, b) : a ∈ R1, b ∈ R2}

(r1, r2) + (r′
1, r′
2) = (r1 + r′
1, r2 + r′
2)

(r1, r2) · (r′
1, r′
2) = (r1r′
1, r2r′
2)

It is easy to check that (R1 × R2, +, · ) is a new commutative ring, with identity element
1 = (11, 12) if each Rk has an identity element 1k.
A review of the proof of the Chinese Remainder Theorem reveals that the bijective map
ψ : Zmn → Zm × Zn created there is actually an isomorphism of commutative rings because it
intertwines both the (+) and (·) operations

ψ([k]mn + [ℓ]mn) = ψ([k]mn) + ψ([ℓ]mn) (proved in 6.1.26)

ψ([k]mn · [ℓ]mn) = ψ([kℓ]mn) = ([kℓ]m, [kℓ]n)
= ([k]m, [k]n) · ([ℓ]m, [ℓ]n) (defn. of (·) in Zm × Zn)

= ψ([k]mn) · ψ([ℓ]mn)

Thus Zmn ∼= Zm × Zn as rings, not just as groups. One consequence is a result about groups
of units in Zn that has important consequences in number theory, although we will just view it
as a result about the direct product structure of certain groups of units.

9

6.1.32 Theorem. If m, n > 1 are relatively prime and Um, Un, Umn are the multiplicative
abelian groups of units in Zm, Zm, Zmn then

(8) (Umn, · ) ∼= (Um, · ) × (Un, · )

and in particular the sizes of these groups satisfy the following multiplicative condition

(9) |Umn| = |Um| · |Un| if gcd(m, n) = 1

Note: Before launching into the proof we remark that the set of units in any commutative ring
R with identity 1R ∈ R can be deﬁned just as for Zn

(10) UR = {x ∈ R : ∃ y ∈ R such that x · y = 1R }

The element y in (10) is called the multiplicative inverse of x, and is written y = x
−1. As with
Zn, the units UR form a commutative group (UR, · ) under multiplication. The proof of 6.1.32
rests on two easily veriﬁed properties of groups UR.

6.1.33 Exercise. If ψ : R → R′ is an isomorphism of commutative rings with identity show
that ψ must map units to units, so that ψ(UR) = UR′ . In particular the groups (UR, · ) and
(UR′ , · ) are isomorphic. While you are at it, explain why ψ must map the identity 1R ∈ R to
the identity 1R′ ∈ R′. □

6.1.34 Exercise. If R1, R2 are commutative rings with identities 11 ∈ R1, 12 ∈ R2, prove that
the set of units UR1×R2 in the direct product ring is the Cartesian product of the separate
groups of units

(11) UR1×R2 = UR1 × UR2 = {(x, y) : x ∈ UR1 , y ∈ UR2 } □

Proof (6.1.32): First observe that ψ : Zmn → Zm × Zn maps Umn one-to-one onto the group
of units UZm×Zn, by 6.1.33. By 6.1.43, the group of units in Zm × Zn is equal to Um × Un.
Since ψ is a bijection that intertwines the (·) operations on each side we see that ψ is a
group isomorphism from (Umn, · ) to the direct product group (Um, · ) × (Un, · ). □

Remarks: Even if m and n are relatively prime, the orders |Um|, |Un| of the groups of units
need not have this property. For instance, if p > 1 is a prime then |Up| = p − 1 and there
is no simple connection between p and the prime divisors of p − 1, or between the divisors of
|Up| = p − 1 and |Uq| = q − 1 if p, q are diﬀerent primes. Furthermore the groups Um, Un need
not be cyclic, though they are abelian. Nevertheless we get a direct product decomposition (8).
Theorem 6.1.32 operates in a very diﬀerent environment from that of the Chinese Remainder
Theorem 6.1.26. Its proof is also more subtle in that it rests on the interplay between the (+)
and (·) operations in Z, while the CRT spoke only of (+).

6.1.35 Exercise. If n1, . . . , nr are pairwise relatively prime, with gcd(ni, nj) = 1 for i ̸= j,
give an inductive proof that Un1n2...nr ∼= Un1 × . . . × Unr and |Un1n2...nr | = |Un1 | · . . . · |Unr | .
□

6.1.36 Exercise. Decompose Z630 as a direct product Zn1 × . . . Znr of cyclic groups. Using
2.5.30 we could compute |U630| by tediously comparing the prime divisors of 630 = 2 · 32 · 5 · 7
with those of each 1 ≤ k < 630. However, the formula of 6.1.35 might provide an easier way to
calculate |U630|. Do it.
Hint: Is the group of units (U9, · ) cyclic? (Check orders o(x) of its elements.) □

The Euler Phi-Function φ : N → N is often mentioned in number theory. It has many
equivalent deﬁnitions, but for us it is easiest to take

φ(1) = 1 φ(n) = |Un| = #(multiplicative units in Zn)

10

Theorem 6.1.32 shows that φ(mn) = φ(m)φ(n) if m and n are relatively prime, and it is this
property that makes the φ-function so useful.

6.1.37 Exercise. The multiplicative property of Exercise 6.1.32 is no help in computing the
size of the group of units Upk where p is a prime, since pk does not split into relatively prime
factors. (Think p = 2, k = 7, pk = 128.) However, one can show directly that

Upk = #{1 ≤ j < pk : gcd(j, pk) = 1} = #{1 ≤ j < pk : p does not divide j}

has cardinality |Upk | = pk−1(p − 1). Carry out this computation.
Hint: Every integer 0 ≤ m < pk has a unique “base p” expansion

m = a0 + a1p + a2p2 + . . . + ak−1pk−1

where 0 ≤ aj < p for each j. Some divisiblity questions become easy using base p expansions.
You may want to use the following Exercise. □

6.1.38 Exercise. Prove that gcd(m, pk) ̸= 1 ⇔ m is a multiple of p. □

6.1.39 Exercise. Compute the size |Un| for n = 2 · 32 · 53 · 49 = 110, 250. □

By exploiting the multiplicative property of the φ-function we obtain a group-theoretic proof
of the following important fact from number theory that reﬂects the subtle interplay between
the operations (+) and (·) in the ring Zn.

6.1.40 Theorem. For any integer n ≥ 1 we have

n = ∑

d|n,1≤d≤n φ(d) = ∑

d|n,1≤d≤n |Ud|

Proof: In the cyclic group (Zn, +) every element x has some additive order o
+(x) = smallest
integer k such that k · x = [0]; by Lagrange, this must be a divisor of n. Letting Sd = {x ∈
Zn : o
+(x) = d} we obviously have Zn = ⋃d|n Sd. These sets are disjoint, and they are all
nonempty because, as in Theorem 3.4.7, there is a unique cyclic subgroup Hd of order d in
Zn for each divisor d|n. Its generator lies in Sd so Sd is nonempty, but by uniqueness of the
group Hd we must have ⟨x⟩ = Hd for each x ∈ Sd, so that Sd ⊆ Hd. Under the isomorphism
Hd ∼= (Zd, +) the set Sd corresponds to the cyclic generators in (Zd, +). But in Proposition
3.1.33 we identiﬁed these generators explicitly as the set of units Ud ⊆ Zd. It follows that

n = ∑

d|n |Sd| = ∑

d|n |Ud| = ∑

d|n φ(d)

as claimed. □
6.2 Semidirect products.

We have determined all groups of order 1 ≤ |G| ≤ 5 using the notion of direct product. But
when |G| = 6 we encounter some cases that cannot be understood in terms of cyclic groups
and their direct products. This leads us to a more general product construction, the semidirect
product N ×φ H of two groups. The construction is motivated by the following considerations.
If A and B are subgroups of a group G, the conditions

(12) AB = G and A ∩ B = (e)

imply that every g ∈ G has a unique factorization g = ab. Existence is clear since G = AB,
while uniqueness follows from the condition A ∩ B = (e) because

a1b1 = a2b2 ⇒ (a2)
−1a1 = b2(b1)
−1 is in A ∩ B

⇒ (a2)
−1a1 = e and b2(b1)
−1 = e
⇒ a2 = a1 and b2 = b1

11

This means there is a natural “parametrization” of points in G by pairs (a, b) in the Cartesian
product space A × B, which at the moment is not equipped with a group structure. The
correspondence A × B ≈ G is eﬀected by the bijection p : A × B → G with p(a, b) = a · b
(product of a and b in G). The labels a and b may be thought of as “coordinates” labeling
all points in G, and it is natural to ask what the group operation looks like when described in
terms of these parameters.
If both A and B are normal subgroups then by 6.1.13 G is their internal direct product and
our question has a simple answer. When we identify G ≈ A × B the group operations take the
familiar form (a, b) ∗ (a′, b′) = (aa′, bb′) (a, b)
−1 = (a−1, b−1)

and the identity element is e = (e, e).
If neither subgroup is normal, the description of the group law in terms of these parameters
can be formidable, and we will not attempt to analyze this situation here. There is, however,
a fruitful middle ground: the case in which just one of the subgroups is normal. This leads to
the notion of semidirect product, which encompasses an enormous set of examples that arise in
geometry and higher algebra.
In this setting we relabel the subgroups as N and H with N the normal subgroup. That
way it will be readily apparent in calculations which group elements lie in the normal subgroup.
Points in G correspond to pairs (n, h) in the Cartesian product set N × H. Furthermore, the
product operation in G can be described explicitly in terms of these pairs. Given elements
g1 = n1h1, g2 = n2h2 in G we must rewrite g1g2 = n1h1 · n2h2 as a product n′′h′′ with
n′′ ∈ N, h′′ ∈ H. The problem is, essentially, to move h1 to the other side of n2, keeping track
of the damage if they fail to commute. This is easy. Because N ⊳ G we may multiply and
divide by h1 to get n1h1n2h2 = n1(h1xh−1
1 ) · h1h2 = n′′ · h′′

in which n′′ ∈ N because h1N h−1
1 ⊆ N . Identifying each gi with its corresponding coordinate
pair (ni, hi) in N × H, the group multiplication law takes the form

(n1, h1) · (n2, h2) = (n1(h1n2h−1
1 ) , h1h2)
= (n1φh1 (n2), h1h2)(13)

where φh : N → N is the conjugation operation φh(n) = hnh−1 for any h ∈ H. The normal
subgroup N is invariant under the action of any conjugation αg(n) = gng−1, g ∈ G, and φh
is just the restriction φh = αh|N of the inner automorphism αh to the set N . Obviously
φh ∈ Aut(N ) for each h ∈ H, and we obtain an action H × N → N of H on N such that

φe = id
N φh1h2 = φh1 ◦ φh2 φh−1 = (φh)
−1 (inverse of the operator φh)

which means that the correspondence Φ : H → Aut(N ) given by Φ(h) = φh is a group homo-
morphism. Conversely, as we noted in our previous discussion of group actions (Chapter 4),
every such homomorphism Φ determines an action of H on N by automorphisms. There is a
one-to-one correspondence between actions H ×N → N and homomorphisms Φ : H → Aut(N ).
It is evident from (13) that the original group G can be reconstructed from its subgroups
N, H if we know the action of H on N via conjugation operators φh. In this way G has been
realized as an “internal semidirect product” of N by H – i.e. as the Cartesian product set N ×H
equipped with the multiplication law (13) determined by φh. We summarize these remarks as
follows.

6.2.1 Proposition (Internal Semidirect Product). Let G be a group and N, H two sub-
groups such that

(i) N is normal in G (ii) N H = G (iii) N ∩ H = (e)

12

Each g ∈ G has a unique factorization as g = nh, so there is a natural bijection between G
and the Cartesian product set N × H. The group action H × N → N via conjugation operators
φh(n) = hnh−1 determines the following “product operation” in the Cartesian product set N ×H.

(14) (n, h) · (n′, h′) = (nφh(n′), hh′) for n, n′ ∈ N and h, h′ ∈ H

This operation makes the Cartesian product set into a group, and the product map p(n, h) = nh
is an isomorphism from (N × H, · ) to the original group G.

Proof: We have noted the unique factorization g = nh in the remarks following (12); the
bijection N × H ≈ G is given by the product map p(n, h) = nh. Our other claims follow if we
can just prove that the product map p intertwines group operations in N × H and G:

p((n, h) · (n′, h′)) = p(n, h)p(n′, h′)

From deﬁnition (14) we see that

p(n, h)p(n′, h′) = nhn′h′ = n(hn′h−1)hh′ = nφh(n′)hh′ = p(nφh(n′), hh′) = p((n, h) · (n′, h′))

(last step by deﬁnition (14)) as required. □

All this is expressed by saying that G is the internal semidirect product of the subgroups
N and H, which we indicate by writing G = N ×φ H to distinguish it from the direct product
N × H of Section 6.1. Of course if the action H × N → N is trivial, as when the subgroups H
and N commute (so that φh = id
N for all h ∈ H), then the semidirect product reduces to the
ordinary direct product.

6.2.2 Exercise. In a semidirect product G = N ×φ H with group law (14) it is clear that the
identity element is just the pair e = (e, e). Use this observation to compute the inverse

(15) (n, h)
−1 = (h−1n−1h, h−1) = (φh−1 (n−1), h−1) for all n ∈ N, h ∈ H

of any pair (n, h) ∈ N × H. □

6.2.3 Exercise. In a semidirect product G = N ×φ H with group law (14) the pairs (n, e) and
(e, h) in the product set N × H correspond under p to the group elements n and h. Use (14)
and (15) to verify that

(a) (n, e) · (e, h) = (n, h)

(b) Conjugation of (n, e) by (e, h) under the group law (14) has the same eﬀect
in N ×φ H as conjugating n by h in the original group G – i.e. we have
(e, h)(n, e)(e, h)
−1 = (hnh−1, e) = (φh(n), e).

What happens if we multiply (e, h) · (n, e), reversing the order of the elements in (a)? □

The following observation often simpliﬁes the job of deciding whether a group G is in fact a
semidirect product of two of its subgroups.

6.2.4 Exercise. Let G be a group and N, H subgroups such that (i) N H = G, (ii) N ∩H = (e),
and
 (iii) H normalizes N in the sense that hN h−1 ⊆ N for every h ∈ H.

Prove that N is in fact normal in G, so G is the internal semidirect product N ×φ H. □

External Semidirect Product. We now reverse this bottom-up analysis, in which N and
H lie within a pre-existing group G, to construct a new group N ×φ H, the external direct
product of N by H, given the following ingredients

(16) (i) Two unrelated abstract groups N and H

(ii) A group action H × N → N implemented by automorphisms φh ∈ Aut(N )
for each h.
 13

Of course, specifying the action in (ii) is completely equivalent to specifying some homomor-
phism Φ : H → Aut(N ); just set Φ(h) = φh.

6.2.5 Theorem. Given two abstract groups N, H and a homomorphism Φ : H → Aut(N )
deﬁne a binary operation on the Cartesian product set N × H, exactly as in (14) and (15).

(17) (n, h) · (n′, h′) = (nφh(n′), hh′) for all n, n′ ∈ N, h, h′ ∈ H

where φh = Φ(h) ∈ Aut(N ). Then G is a group, the external semidirect product, which
we denote by N ×φ H. The inversion operation g ↦→ g−1 in this group has the form (15).
The subsets N = {(n, e) : n ∈ N } and H = {(e, h) : h ∈ H} are subgroups in G that are
isomorphic to N and H. They satisfy the conditions N H = G, N ∩ H = (e), and N is normal
in G. Thus G is the internal semidirect product of these subgroups.

Proof: There is some bother involved in checking that the operation (17) is associative because
the action does not arise via multiplications in some pre-existing group, as it did in 6.2.1. We
leave these routine but tedious calculations to the reader.
The identity element is e = (e, e) = (eN , eH ). The inverse operation is

(n, h)
−1 = (φh−1 (n−1), h−1)

In fact, recalling that φe = id
N and that φh−1 = (φh)
−1 because Φ : H → Aut(N ) is a
homomorphism, (17) gives

(n, h) · (φh−1 (n−1), h−1) = (nφh(φ
−1
h (n−1)), hh−1) = (nn−1, e) = (e, e)
(φh−1 (n−1), h−1) · (n, h) = (φh−1 (n−1)φ
−1
h (n), h−1h)

= ( (φ
−1
h (n))
−1φ
−1
h (n), e) = (e, e)

In G the maps n ↦→ (n, e) ∈ N and h ↦→ (e, h) ∈ H are isomorphic embeddings of N and H
in G because they are bijections such that

(n, e) · (n′, e) = (nn′, e) and (e, h) · (e, h′) = (e, hh′)

We get G = N H because (n, e) · (e, h) = (nφe(e), eh) = (n, h), and it is obvious that N ∩ H =
{(e, e)}. Normality of N follows because

(n, h)(n′, e)(n, h)
−1 = (n, e)(e, h)(n′, e)(e, h−1)(n−1, e)

= (n, e)(φh(n′), h)(e, h−1)(n−1, e)
= (n, e)(φh(n′), e)(n−1, e)

= (nφh(n′)n−1, e)

for all n′ ∈ N ; the lefthand component is back in N so that gN g−1 ⊆ N for any g = (n, h) ∈ G.
When we identify N ∼= N and H ∼= H, the action of h ∈ H by conjugation on n ∈ N
matches up with the original action of H × N → N determined by Φ, so the group G we have
constructed is the internal semidirect product N ×φ H of these subgroups. □

The next example is important in geometry.

6.2.6 Example (The Dihedral Groups Dn). These nonabelian groups of order |Dn| = 2n,
deﬁned for n ≥ 2, are the full symmetry groups of regular n-gons. To describe Dn consider a
regular n-gon in the xy-plane, centered at the origin and with one vertex on the positive x-axis,
as shown in Figure 6.2 (where n = 6). Let θ = 2π/n radians, and deﬁne the basic symmetry
operations
 ρθ = (counterclockwise rotation about the origin by θ radians)
σ = (reﬂection across the x-axis)

14

Figure 6.2. The basic symmetry operations on a regular n-gon, shown here for the
regular hexagon (n = 6). The same idea works for all n. In our discussions vertices
are labeled 0, 1, 2, . . . , n − 1 as indicated. The symmetry groups Dn have diﬀerent
properties for even and odd n, and n = 2 is exceptional.

Obviously these elements have orders

(18A) o(σ) = 2 so σ2 = e and σ−1 = σ

o(ρθ) = n with distinct powers ρj
θ for 0 ≤ j < n and ρn
θ = I.

The dihedral group Dn is the subgroup Dn = ⟨ρθ, σ⟩ generated by ρθ and σ in the group
O(2) of orthogonal linear transformations of the plane. Obviously N = ⟨ρθ⟩ is a cyclic subgroup
isomorphic to Zn and H = ⟨σ⟩ is a copy of Z2 embedded in Dn. We will show that Dn is the
semidirect product of these subgroups.
We begin by verifying another relation, which together with the obvious relations (18A)
completely determines Dn.

(18B) σρθσ = σρθσ−1 = ρ−1
θ (Note that ρ−1
θ = ρ−θ = ρn−1
θ and σ−1 = σ)

This last relation tells us how to pass a rotation across a reﬂection when forming products,
since σρθ = ρ−1
θ σ; furthermore, since conjugation by σ is an automorphism we also get

σρk
θ σ = σρk
θ σ−1 = (σρθσ−1)
k = ρ−k
θ = ρn−k
θ for all k ∈ Z

One could check (18B) by tedious matrix computations, but it is easier simply to track the
action of each factor on the standard unit vectors e1 = (1, 0), e2 = (0, 1) in R2, as shown in
Figure 6.3 below. Once we know what the product does to basis vectors we know what it does
to all vectors, and it is not hard to recognize the outcome as a familiar linear operator. (In
(18B) the end result is clockwise rotation by θ radians.)
Using the relations (18) we now show that every element of Dn = ⟨ρθ, σ⟩ can be written
uniquely in the form
 ρk
θ σℓ where 0 ≤ k < n and ℓ = 0 or 1

Since ρn
θ = σ2 = I, the operator ρk
θ depends only on the (mod n) congruence class of k, and
it is convenient to think of this exponent as an element k ∈ Zn; likewise the exponent in σℓ

should be thought of as an element ℓ ∈ Z2. Then the factorization of elements in Dn takes the
form

(19) Any element in the dihedral group Dn can be factored uniquely in the form
ρk
θ σℓ where k ∈ Zn and ℓ ∈ Z2.
 15

Figure 6.3. Action of σρθσ on basis vectors in R2.

To prove this, we show that the set S of elements listed in (19) is already a group. Then, since
Dn = ⟨ρθ, σ⟩ ⊇ S and S is a subgroup containing the generators, the two sets must be equal;
uniqueness of the factorization follows. Clearly I ∈ S, and S · S ⊆ S because

(ρk
θ σℓ)(ρr
θσs) = ρk
θ (σℓρr
θσ−ℓ)σℓ+s

= ρk
θ (σℓρθσ−ℓ)
rσℓ+s (conjugation by σℓ is an automorphism)

= ρk
θ (ρ(−1)ℓ

θ )r σℓ+s (repeated use of (18B))

= ρk+(−1)ℓr
θ σℓ+s ∈ S

Finally S−1 = S, and S is a subgroup, because

(ρk
θ σℓ)
−1 = σ−ℓρ−k
θ
= σℓρ−k
θ σℓσ−ℓ (because σ = σ−1)

= (σℓρθσℓ)
−kσ−ℓ

= (ρ(−1)ℓ

θ )−k σ−ℓ

= ρ−(−1)ℓk
θ σ−ℓ ∈ S

From (19) we see that Dn is a ﬁnite group of operators on the plane, with |Dn| = 2n.
As for uniqueness, the identity ρk
θ σℓ = ρr
θσs implies ρk−r
θ = σs−ℓ. Unless both exponents
are congruent to zero, the transformation on the left has determinant +1 while the one on the
right has determinant −1, which is impossible.
The unique decomposition (19) shows that the subgroups N = ⟨ρθ⟩ and H = ⟨σ⟩ have the
properties (i) N ∩ H = (e), (ii) N H = Dn. Furthermore N is a normal subgroup, a fact that
is apparent once we compute the action of H on N by conjugation:

(20) φσ(ρk
θ ) = σρk
θ σ−1 = (σρθσ−1)
k = ρ−k
θ ∈ N

Thus φσ is the inversion automorphism J : n → n−1. Then conjugation by an arbitrary element
g = ρr
θσs ∈ Dn has the following eﬀect

gρk
θ g−1 = (ρr
θσs)ρk
θ (ρr
θσs)
−1 = ρr
θ(σsρk
θ σ−s)ρ−r
θ = ρr
θ(ρ(−1)sk
θ )ρ−r
θ = ρ(−1)sk
θ

because N is abelian. This proves Dn ∼= Zn ×φ Z2 under the action H × N → N in (20). □

6.2.7 Corollary (Multiplication Law in Dn). If two elements of Dn are written in factored
form (19), the group operations take the form

(a) (ρk
θ σℓ) · (ρr
θσs) = ρk+(−1)ℓr
θ σℓ+s

(b) (ρk
θ σℓ)
−1 = ρ−(−1)ℓk
θ σ−ℓ
 16

for k, r ∈ Zn and ℓ, s ∈ Z2. □

6.2.8 Exercise. In G = Dn the geometric meaning of the elements ρk
θ and the reﬂection σ
is clear, but what about products of the form ρk
θ σ with 0 < k < n? Use the idea shown in
Figure 6.3 to ﬁnd geometric descriptions of the following group elements

(a) ρθσ (b) ρk
θ σ (with k ≡/ 0 (mod n))

Assume n ≥ 3. □

6.2.9 Exercise. In Dn show that the group element

ρk
θ σρ−k
θ (with k ≡/ 0 (mod n))

is the reﬂection σL across the line through the origin that passes through the kth vertex of the
n-gon. (Label vertices 0, 1, 2, . . . , n − 1 counterclockwise starting with the vertex on the positive
x-axis).
Hint: This can be seen via a geometric argument, without resorting to calculations of the sort
shown in Figure 6.3. □

6.2.10 Exercise. Determine the center Z(Dn) = {x ∈ Dn : gxg−1 = x for all g ∈ G} for
n ≥ 3.
Note: The answer will depend on whether n is even or odd. When n = 2 the group is abelian
and the center is all of D2.
Hint: By 3.1.46 an element x = ρiσj is in the center of Dn ⇔ x commutes with the two
generators ρ and σ of Dn. This simpliﬁes calculation of the center. □

6.2.11 Exercise. Determine all conjugacy classes in D6 and in D7.
Note: Recall that N (hence also the outside coset N σ) are unions of whole conjugacy classes,
so you might start by determining the classes that lie in the normal subgroup. □

6.2.12 Exercise. Use Exercise 6.2.11 to determine all normal subgroups in D6 and in D7.
Hint: Recall 5.4.2 and 5.4.6. □

6.2.13 Exercise. For n ≥ 3 determine the conjugacy classes in Dn. Start by discussing the
class Cσ = {gσg−1 : g ∈ Dn}.
Note: The answer is diﬀerent for odd and even n. D2 ∼= Z2 × Z2 is abelian and has trivial
classes. □

6.2.14 Example (Invertible Aﬃne Mappings Aﬀ(V )). The aﬃne mappings on a ﬁnite
dimensional vector space V over ﬁeld of scalars F are the maps of the form

(21) T (v) = A(v) + a where A is a linear map and a ∈ V

It is easily seen that T : V → V is an invertible bijection ⇔ A is an invertible linear map,
with det(A) ̸= 0. It is also clear that the set Aﬀ(V ) of invertible aﬃne maps is a group under
composition of operators since the composite

(22) T ′ ◦ T (v) = A
′(T v) + a′ = A
′(Av + a) + a′ = A
′A(v) + (A
′a + a′)

is again invertible and aﬃne.
Any aﬃne map has the form T = ta ◦ A where A is a linear operator on V and ta : V → V is
the pure translation operator ta(v) = v+a. The components A, a in (21) are uniquly determined,
for if A
′v + a′ = Av + a for all v then we have A
′v − Av = a − a′. Taking v = 0 we get a′ = a,
and then A
′v = Av for all v, so A
′ = A as operators on V . Within G = Aﬀ(V ) we ﬁnd two
natural subgroups

Translations: N = {ta : a ∈ V }. This subgroup is abelian because ta ◦ ta′ = ta+a′
and since a′ ̸= a ⇒ ta′ ̸= ta, the map j : a ↦→ ta is an isomorphism between (V, +)

17

and the subgroup N in (Aﬀ(V ), ◦ ).

Purely Linear Operators: GL(V ) = {A : det(A) ̸= 0} is the set of all invertible
linear operators A : V → V . It is obviously a subgroup in Aﬀ(V ).

We have just remarked that G = N · GL(V ). It is also clear that N ∩ GL(V ) = {I}, where I is
the identity operator on V . [In fact, every linear operator A leaves the origin in V ﬁxed, but a
translation ta does this only when a = 0 and ta = I.] We claim that N is a normal subgroup
in G, and hence we have a semidirect product Aﬀ(V ) = N ×φ GL(V ).
Let T be any element in G. To see that T taT −1 ∈ N for T ∈ Aﬀ(V ) we ﬁrst apply (21) to
compute the inverse of any operator T v = Av + b in G

(23) T −1v = A
−1(v − b) = A
−1(v) − A
−1(b)

(Simply solve w = T v = Av + b for v in terms of w.) Next we compute the eﬀect of conjugation
by T on a translation ta in the special case when T = A is linear and b = 0. We get

(24) AtaA
−1 = tA(a) for all a ∈ V, A ∈ GL(V )

because for every v we have

AtaA
−1(v) = A(A
−1(v) + a) = AA
−1(v) + A(a) = v + A(a) = tA(a)(v)

Thus, conjugating a translation ta by a purely linear operator produces another translation as
expected, but it is also useful to observe that

When we identify (V, +) ∼= N via the bijection j : a ↦→ ta, the action GL(V ) × N →
N by conjugation (which sends ta ↦→ AtaA
−1) gets identiﬁed with the usual action
of the linear operator A on vectors in V (which sends a ↦→ A(a)).

Now let T be any element in G. To see that T N T −1 ⊆ N for all T ∈ G, we write T = tb ◦ A
and compute the eﬀect of conjugation; since t−1
b = t−b, equation (24) implies that

T taT −1 = tb(AtaA
−1)t−b = tbtA(a)t−b = tb+A(a)−b = tA(a)

Compare with (24): throwing in the translation component tb has no eﬀect when T acts by
conjugation on the translation subgroup N . That makes sense: N is abelian and acts trivially
on itself via conjugation. □

We have stated that Dn is the full set of symmetries of the n-gon, without going into the proof.
First you must understand what we mean by “symmetries.” The set M(2) of all bijections
f : R2 → R2 that are distance-preserving

dist(f (x), f (y)) = dist(x, y) where dist(x, y) = √
(x1 − y1)2 + (x2 − y2)2

is easily seen to be a group under composition of mappings. It is called the group of rigid
motions in the plane. With some clever eﬀort (details in Section 1.9) one can show that every
operator in M (2) is actually an invertible aﬃne mapping, as deﬁned in 6.2.14, whose linear
part has a special form.

T v = Av+b where {
b ∈ R2 and A ∈ O(2) = {A ∈ M(2, R) : AA
t = I = A
tA},
the group of 2 × 2 real orthogonal matrices.

Orthogonal matrices arise here because a linear operator A : R2 → R2 preserves distances in
the plane if and only if it corresponds to an orthogonal matrix. Since translation operators
ta : v ↦→ v + a are automatically distance preserving, the subgroup M (2) ⊆ Aﬀ(R2) of distance
preserving mappings of the plane consists precisely of those maps whose linear part lies in
O(2). Thus M (2) is the semidirect product M (2) = R2 ×φ O(2) when we identify the normal

18

subgroup of translation operators N with (R2, +). The action O(2) × R2 → R2 associated with
this product is the usual action of a matrix A on a vector v ∈ R2, namely φA(v) = Av.
A symmetry of the regular n-gon E is any distance preserving map T ∈ M(2) such that
T (E) = E, and we claim that these symmetries are precisely the mappings found in Dn. We
will address this geometric claim later, but for the moment there is an interesting question to
be answered. The n-gon shown in Figure 6.4(a) has some obvious symmetries whose presence
in Dn is not so obvious. When n is even there are two types of lines of reﬂection symmetry
through the origin: (i) lines passing through a vertex, and (ii) lines through the midpoint of
an edge. (When n is odd these are the same.) The reﬂections σ
L across such lines are clearly
symmetries of the n-gon. Where do these occur in Dn?

Figure 6.4. In (a) we show the reﬂection symmetry σL across a line L passing
through the midpoint of an edge of the n-gon. (b) The 2-gon degenerates to a line
segment with two vertices.

6.2.15 Exercise. Assume n ≥ 3 and consider reﬂection σL across a line that extends from
the origin through the center of an edge of the n-gon, as in Figure 6.4(a). Is this one of the
operations in Dn = {ρk
θ σℓ}? Which one?
Note: For lines of the ﬁrst type see Exercise 6.2.9. □

6.2.16 Exercise (The Degenerate case n = 2). When n = 2 the n-gon degenerates into a
line segment, as shown in Figure 6.4(b). This shape has D2 as its full symmetry group; notice
that θ = π.

(a) Identify the geometric meaning of each element e, ρθ, σ, ρθσ.

(b) Verify that D2 is abelian.

(c) The only groups of order 4 are Z4 and Z2 × Z2. Which one is D2? □

We close this section with a few case studies. In the ﬁrst we shall determine all groups of
order |G| = 6, up to isomorphism. We will analyze some more complicated groups at the end
of Section 6.3 after introducing an important new tool, the Sylow Theorems.

6.2.17 Example (Groups of order |G| = 6). By Cauchy’s theorem 4.3.4 there exist cyclic
subgroups H2 and H3 of order 2 and 3. The subgroup H3 is normal because if gH3g−1 ̸= H3
for some element g ∈ G, then the intersection gH3g−1 ∩ H3 would be trivial and the product
set would have cardinality
 |gH3g−1 · H3| = |gH3g−1| · |H3|
|H3 ∩ gH3g−1| = 9

which exceeds the size of G. Contradiction.
Once we know H2 ∼= Z2 and that H3 ∼= Z3 is normal, G must be a semidirect product of Z2
acting on Z3. The possible actions are determined by the homomorphisms Φ : Z2 → (U3, · ) ∼=

19

Aut(Z3, +), which in turn are fully determined by where they send the nontrivial element a ̸= e
in Z2. There are just two possible semidirect products:

Group G
(1): in which Φ(a) = [1]
3 , the identity element in U3. We have Z2 = {e, a}
and the corresponding automorphisms of Z3 are

φ
(1)
e = φ
(1)
a = τ[1] = idZ3

All elements in Z2 go to the identity map so we have the trivial action of Z2 on
Z3. The resulting group is the abelian direct product G
(1) = Z3 × Z2 which, by the
Chinese Remainder Theorem, is isomorphic to the cyclic group Z6.

Group G
(2): in which Φ(a) = [2]
3 = [−1]
3. Then the corresponding automorphisms
of Z3 are
 φ
(2)
e = idZ3
φ
(2)
a = τ[−1]

Now φa is the inversion map J : [ℓ] → [−1][ℓ] = −[ℓ] on the additive group Z3.
The semidirect product in which Z2 acts by inversion of Zn is precisely the dihedral
group Dn, so G
(2) ∼= D3. [ This can be seen by observing that the elements

ρ = ([1]
n , [0]
2) and σ = ([0]
n, [1]
2)

satisfy the identities
 o(ρ) = n o(σ) = 2 σρσ−1 = ρ−1

characteristic of the dihedral groups.] There are no other possibilities for groups of
order 6. In particular, up to isomorphism the only abelian group of order 6 is Z6.

Incidentally, we have indirectly proved that the permutation group S3 is isomorphic to D3
because both are noncommutative and of order 6. □

6.2.18 Exercise. Verify that the multiplication law in G
(2) = Zn ×φ Z2 is given by

([i], [j]) · ([k], [ℓ]) = ([i] + τ j
[−1]([k]) , [j + ℓ])

= ([i + (−1)
jk] , [j + ℓ])

Use this to show that the elements ρ, σ above satisfy the “dihedral identities.” □

6.2.19 Exercise. Can you devise a bijective map ψ : S3 → D3 that eﬀects the isomorphism
mentioned above?
Hint: What subgroups in S3 might play the roles of N = {e, ρθ, ρ2
θ} and H = {e, σ} in D3? □

In the preceding discussion we ended up having to determine all possible homomorphisms

Φ : (Z2, +) → (U3, · ) ∼= Aut(Z3, +)

That was easy because the groups were quite small, and cyclic. More generally, to determine the
possible semidirect products N ×φ H we must determine all homomorphisms Φ : H → Aut(N ).
In attacking this question you should remember that a homomorphism is completely determined
once you know where it sends the generators of H. Another useful constraint is the fact that

• The order of the image group Φ(H) must divide the order of Aut(G).

• The order of the image group Φ(H) must also divide the order of H.

20

The ﬁrst follows because Φ(H) is a subgroup in Aut(N ); the second follows from Lagrange and
the First Isomorphism Theorem because Φ(H) ∼= H/ker(Φ) and

|H| = |ker Φ| · |H/ker Φ| = |ker Φ| · |Φ(H)|

Sometimes these conditions by themselves force Φ to be trivial, with Φ(h) = id
N for all h ∈ H.
In most examples below, both H and N are cyclic, say N ∼= Zn and H ∼= Zm. (When
they are not cyclic, then ﬁnding all homomorphisms Φ : H → Aut(N ), and the corresponding
semidirect products N ×φ H, begins to get really interesting.) We have previously seen that
(Un, · ) ∼= Aut(Zn, +) via the correspondence that takes [r] ∈ Un to the automorphism

τ[r] : [j] → [r][j] = [rj] for all [j] ∈ Zn

Thus for cyclic N ∼= Zn and H ∼= Zm the following tasks are equivalent

• Find all actions by automorphisms H × N → N

• Find all homomorphisms Φ : H → Aut(N )

• Find all homomorphisms Φ : H → Aut(Zn, +)

• Find all homomorphisms Φ : (Zm, +) → (Un, · )

Since Zm = ⟨a⟩ where a = [1]m, any homomorphism such as Φ is completely determined
once we specify the element in Un to which Φ sends the generator a. But not all assignments
Φ(a) = b, b ∈ Un, yield valid homomorphisms Φ; since o(a) = m and m · a = [0], the element b
must also be chosen to have the compatibility property bm = [1] in Un, because

(25) [1] = Φ(e) = Φ(m · a) = Φ(a)
m = bm

(This is another way of saying that the order of the cyclic image group Φ(H) = ⟨b⟩ must be a
divisor of |H| = m.) It is not hard to check that all assignments Φ(a) = b with this property
yield distinct valid homomorphisms Φ : Zm → Un. All possible homomorphisms Φ are now
accounted for. In turn these homomorphisms determine all possible actions H × N → N , and
in determining these actions we are ﬁnding all possible semidirect products G = N ×φ H of
cyclic groups. Note that the trivial homomorphism Φ : H → Aut(N ), with φh = idN for all
h ∈ H, corresponds to the trivial action of H on N , and yields the direct product G = N × H
because (n, h) · (n′, h′) = (nφh(n′), hh′) = (nn′, hh′)

All other actions give noncommutative semidirect products.

6.2.20 Exercise. Let G be a ﬁnite cyclic group and H an arbitrary group. If a is a generator
for G then o(a) = m = |G|. Suppose b ∈ H has the property bm = e. Prove that there is a
unique group homomorphism Φ : G → H such that Φ(aj) = bj for all j. □

Notation in Semidirect Products Zm ×φ Zn. Semidirect products of cyclic groups, such as
the dihedral groups, can be regarded as having the form Zm ×φ Zn. Determining the group law
in the parameters of the Cartesian product space Zm × Zn can be a bit confusing since integers
are combined using the (+) operation within Zm and Zn; multiplied via (·) within the group of
units Um; and also multiplied in forming the actions

τ[r] : [ℓ] → [r][ℓ] = [rℓ] for [r] ∈ Um, [ℓ] ∈ Zm

To avoid future confusion we work through the details below.

6.2.21 Proposition. If Φ : (Zn, +) → (Um, · ) is the homomorphism that sends the generator

21

a = [1]n of Zn to an element b = [r]m in Um that satisﬁes the compatibility condition bm = [1]m,
then the corresponding group operation in the semidirect product Zm ×φ Zn takes the form

(26) ([i]m, [j]n) · ([k]m, [ℓ]n) = ([i + rjk]m , [j + ℓ]n)

Proof: Since Zn is an additive group the jth “power” of the generator a is j · a = a + . . . + a,
and since Φ is a homomorphism from an additive group to a multiplicative group we get

Φ(j · a) = Φ(a + . . . + a)

= Φ(a) ◦ . . . ◦ Φ(a)
= Φ(a)
j = τ j
[r] = τ[r]j = τ[rj]

Hence, (suppressing some subscripts m, n for clarity), we get

([i]m, [j]n) · ([k]m, [ℓ]n) = ([i] + τ j
[r]([k]) , [j] + [ℓ])

= ([i] + [r]
j[k], [j + ℓ]) = ([i + rj k]m , [j + ℓ]n)

as required □

We now turn to various other computed examples.

6.2.22 Example. Determine the group of units (U5, · ) and its isomorphism type. Then ﬁnd all
possible homomorphisms Φ : Z3 → U5. Describe the possible semidirect products G = Z5 ×φZ3.

Discussion: Obviously

Aut(Z5, +) ∼= U5 = {[k] : gcd(k, 5) = 1} = {[1], [2], [3], [4]}

and |U5| = 4. There are two possibilities: U5 ∼= Z4 and U5 ∼= Z2 × Z2. If we calculate the
orders of a few elements in U5 we ﬁnd that o([2]) = 4, so (U5, · ) ∼= (Z4, +).
If Φ : Z3 → U5 is a homomorphism, the size |Φ(Z3)| of the image subgroup in U5 must be a
divisor of both 3 and 4. Since gcd(3, 4) = 1, the range of Φ must be the trivial subgroup {[1]}
in U5, so the only action Z3 × Z5 → Z5 by automorphisms is the trivial action. The direct
product Z5 × Z3 ∼= Z15 is the only possible semidirect product. (Notice that we didn’t need to
know the structure of U5 to see this!) □

6.2.23 Example. Repeat the last example taking N = Z9 and H = Z3.

Discussion: Now Aut(N ) = U9 = {[1], [2], [4], [5], [7], [8]} and |U9| = 6. Up to isomorphism
there are just two groups of order |G| = 6, and since the group of units is abelian we see that
U9 ∼= (Z6, +), without inspecting the orders of any elements in U9. [ In fact, o([2]) = 6 so
a = [2] is a cyclic generator of U9.] However, it is useful to actually write down the orders o(x)
of elements in U9 and the groups ⟨x⟩ they generate, see the Table below.

Table. Orders of
elements in U9 and
the cyclic groups
they generate.
 x o(x) ⟨x⟩

[1] 1 1

[2] 6 1, 2, 4, 8, 16 ≡ 7, 14 ≡ 5

[4] 3 1, 4, 16 ≡ 7

[5] 6 1, 5, 25 ≡ 7, 35 ≡ 8, 40 ≡ 4, 20 ≡ 2

[7] 3 1, 7, 49 ≡ 4

[8] 2 1, 8 ≡ −1

22

With this we can determine the possible homomorphisms Φ : Z3 → U9. Our only ﬂexibility in
deﬁning Φ lies in specifying where Φ sends the generator a = [1] of H = Z3. Since a has order
3, we can only send a to an element b ∈ U9 such that b3 = e, and there are just three such
elements: b = [1], [4], [7]. Each assignment yields an action and a semidirect product structure
on Z9 × Z3

Group G
(1): Φ sends a to [1] ∈ U9. Then Φ([j]3) = Φ(j · a) = [1]
j = [1] for all
j. The action of Z3 on Z9 is trivial and we get the direct product G
(1) ∼= Z9 × Z3
(which, incidentally, is not ∼= Z27. Why?).

Group G
(2): Φ sends a to the element [4] in U9, which corresponds to the auto-
morphism τ[4] : [k] → [4][k] = [4k] for all [j] ∈ Z9. By (26), the group law in the
semidirect product is

([i]9, [j]3 ) · ([k]9 , [ℓ]3) = ([i + 4jk]9 , [j + ℓ]3)

Group G
(2): Φ sends a to the element [7] in U9, which corresponds to the auto-
morphism τ[7] : [k] → [7][k] = [7k] for all [j] ∈ Z9. By (26), the group law in the
semidirect product is

([i]
9, [j]
3 ) · ([k]
9 , [ℓ]
3) = ([i + 7jk]
9 , [j + ℓ]
3)

The preceeding analysis shows that all semidirect products Z9 ×φ Z3 are included in our list
of groups G
(1), . . . , G
(3); it does not, however, insure that the groups we have constructed are
distinct up to isomorphism. Since [7] = [4]
−1 in (U9, · ) there seems to be a strong symmetry
between the multiplication laws in G
(2) and G
(3). In fact, these groups are isomorphic, so there
is only one nonabelian semidirect product of the form Z9 ×φ Z3

6.2.24 Exercise. Verify that the map ψ : Z9 × Z3 → Z9 × Z3 given by

ψ([i], [j]) = ([1], [2j])

is an isomorphism from G
(3) to G
(2).
Note: ψ is obviously a bijection on the Cartesian product space Z9 × Z3 because [2] is a unit
in Z3. □

You might wonder how anyone ever came up with the map ψ that eﬀects this isomorphism.
Here is a clue: The products in G
(2) and G
(3) involve multipliers of the form 4j and 7j. The
equation 4x = 7 in U9 has x = 2 as a solution, and therefore 42j ≡ 7j in Z9 for all j ∈ Z3.

6.2.25 Exercise. Describe all semidirect products Z3 ×φ Z3 by ﬁnding all possible homomo-
prhisms Φ : Z3 → (U3, · ) ∼= Aut(Z3, +). □

6.2.26 Exercise. If p, q > 1 are primes and p ≥ q, prove that the only semidirect products
Zq ×φ Zp are trivial direct products. Produce an example showing that this is not necessarily
true if p < q. □

The next example involves an N that is abelian but not cyclic.

6.2.27 Exercise. Describe all automorphisms of the non-cyclic group N = Z2 × Z2. Then
describe all homomorphisms Φ : Z2 → Aut(N ), and determine all possible semidirect products
N ×φ Z2.
Hint: Aut(N ) ∼= S3, the group of permutations of 3 objects. What 3 objects could possibly
be permuted by a typical automorphism of Z2 × Z2? Which elements σ ∈ S3 satisfy σ2 = e?
What are the corresponding automorphisms of Z2 × Z2? □

6.2.28 Exercise. Make a table showing o(x) for all x ∈ U16.

23

(a) Use this to prove that U16 ∼= Z4 × Z2.

(b) Explain why there are no isomorphisms between the groups Z8, Z4 × Z2, and
Z2 × Z2 × Z2.
(c) Determine all semidirect products Z16 ×φ Z7.

(d) Determine all semidirect products Z16 ×φ Z2.

The next two exercises on product groups will play an important role in a later discussion
(Section 6.3) in which we shall describe all groups of order |G| = 8, a tricky case whose outcome
is quite diﬀerent from that when |G| = 6.

6.2.29 Exercise. If G is a group such that o(x) = 2 for all x ̸= e, so x
2 = e for all x, prove
that G is abelian.
Hint: Recall the discussion of 6.1.17 where we proved that all groups of order |G| = 4 are
abelian. □

6.2.30 Exercise. If G is a ﬁnite group such that o(x) = 2 for all x ̸= e,

(a) Prove that |G| = 2n for some n ∈ N.

(b) Use 6.2.29 to prove that

G ∼= Z2 × . . . × Z2 (n factors) □

Group Extensions. Suppose N ⊳ G is a normal subgroup. Then there is a natural exact
sequence of homomorphisms

(27) e −→ N φ1=id
−−−−−−→ G φ2=π
−−−−−−→ H = G/N −→ e

where π : G → G/N is the quotient map. Here exact means range(φi−1) = ker(φi) at every
step in the sequence, which is certainly true in (27) since id
N is one-to-one, π is surjective, and
ker(π) = N . The middle group G in such a sequence (27) is called an extension of the group
G/N by the group N . In some sense G is a composite of N and H = G/N , but additional
information is needed to know how they are put together. Part of this information is obtained
by noting that there is a natural group action G × N → N , given by g · n = φg(n) = gng−1.
This makes sense because N ⊳ G. For each g ∈ G the operator φg : N → N is actually an
automorphism of N , and it is easily checked that

(28) The map Φ : g ↦→ φg is a homomorphism from G to the group of automor-
phisms Aut(N ), so that φe = id
N and φg1g2 = φg1 ◦ φg2 .

For any g the conjugation operators αg(x) = gxg−1 are inner automorphism of G (recall
Section 3.5). However, the restrictions φg = αg|N are not necessarily inner automorphisms
of N because there might not be any element b ∈ N such that conjugation by b matches the
restricted action of g on N . For instance, if N is abelian all inner automorphisms are trivial;
but the restrictions φg = αg|N can be nontrivial because g lies outside of N .
Sometimes, if we are lucky, the sequence (27) splits: there is a subgroup H ⊆ G that cross-
sections the G/N cosets in the following sense. Then the action (28) is all we need to solve the
problem of reassembling G from its components N and G/N : the semidirect product construc-
tion does the job.

6.2.31 Deﬁnition. Let G be a group and N a normal subgroup, as in (27). A subgroup H is a
cross-section for G/N if each coset in G/N meets the set H in a single point; in particular,
H ∩ N = (e). If such a subgroup exists we say that the sequence (27) splits. Such subgroups
are generally not unique.
 24

The meaning of the cross-section property is shown in
Figure 6.5. The idea is that

Every coset C in G/N has a unique repre-
sentative x (i.e. xN = C) such that x lies
in the cross-section subgroup H.

Existence of such a representative follows because the
coset C meets the set H; uniqueness follows because
there is just one point in C ∩ H. What all this means is
that the quotient map π : G → G/N restricts to H to
give a bijective homomorphism πH : H → G/N , which
implies that H ∼= G/N for any cross-section. In eﬀect,
cross-sections H are copies of the quotient group G/N
embedded back inside G.
Various conditions are equivalent to existence of a
cross-section. We summarize the possibilities in the next
lemma.
 Figure 6.5. A cross-section H meets
each coset in G/N in a single point, so
the quotient map π restricts to an iso-
morphism from H to G/N , as shown.

6.2.32 Lemma. Let G be a group, H a subgroup and N a normal subgroup. Then the following
statements are equivalent

(a) The product set N H is equal to G and N ∩ H = (e)

(b) Each g ∈ G has a unique factorization g = nh with n ∈ N, h ∈ H.

(c) H is a cross-section for G/N cosets

These conditions are satisﬁed precisely when the sequence (27) splits, and then we have H ∼=
G/N .

Remark: Notice that N H = HN by normality of N , because every product nh can be rewritten
as nh = h(h−1nh) = h′n′. Thus each g also has a unique factorization as g = h′n′. To avoid
notational mess later on we restrict attention to factorizations g = nh in which the normal
element lies on the left, even though cosets in G/N have the form gN .

Proof: For (c) ⇒ (a), if H cross-sections cosets we get H ∩ N = (e) by looking at the coset
eN = N . For any x ∈ G the intersection xN ∩ H = (b) consists of a single point such that
xN = bN . In particular there is some n ∈ N such that x = bn ∈ HN = N H. Hence G = N H.
For (a) ⇒ (b), every group element has some decomposition g = nh because G = N H. If
g = nh = n′h′, then n−1n′ = h(h′)
−1 lies in N ∩ H = (e), so that n = n′ and h = h′. The
decomposition is unique.
For (b) ⇒ (c), unique factorization implies that g = nh = h(h−1nh) ∈ hN . Hence gN = hN ,
so every coset in G/N has at least one representative in H. If we could ﬁnd two representatives
h, h′ ∈ H ∩ gN , we would then have

hN = gN = h′N ⇒ h′ = hn for some n ∈ N

⇒ h−1h′ = n ∈ H ∩ N = (e)
⇒ n = e and h′ = h

Therefore each coset meets H in a single point, as required. □

Obviously condition (a) means G is a semidirect product of the form N ×φ H, and we can
reconstruct G once we know how elements h ∈ H act as automorphisms φh = αh|N on the
normal subgroup N . In the next section we will see that among groups of order |G| = 8 there is
one (the group Q8 of unit quaternions ) that is a non-split extension of G/N ∼= Z2 by N ∼= Z4.
For non-split extensions an entirely new theory of group cohomology is needed to deal to see
how the subgroups N and G/N combine to reconstruct G.

25

Here is an example of a non-split extension. Although it involves an inﬁnite group, it illus-
trates the sort of obstructions that can prevent the existence of a subgroup that cross-sections
the N -cosets in G. The quaternion group Q8 to be discussed in Section 6.3 is a ﬁnite group
exhibiting similar behavior.

6.2.33 Example. If we take G = R and N = Z, the
extension e → Z → R → G/N → e does not split,
so G is not a semidirect product of N and H. To see
why, recall that G/N is isomorphic to the circle group
S1 = {z ∈ C : |z| = 1}. In fact (as in 3.3.3), the homo-
morphism φ : (R, +) → (S1, · ) given by the exponential
map φ(t) = e2πit has kernel ker φ = Z, and hence by the
First Isomorphism Theorem 3.1.13 the map φ factors
through the quotient map π : R → R/Z to give an iso-
morphism ˜φ : (R/Z, +) → (S1, · ) as shown in Figure 6.6
at right.
 R φ
−→ (S1, · )
π ↓ ր

R/Z ˜φ

Figure 6.6. The induced map ˜φ is
an isomorphism such that ˜φ ◦ π = φ
(diagram commutes).

Arguing by contradiction, we now show that no subgroup H in R can cross-section the cosets
x + Z in R/Z. Suppose such an H actually exists. Consider any rational value 0 < θ < 1. Then
mθ ∈ Z for some m ∈ N, and hence 1 = φ(mθ) = φ(θ)
m. Since H is a cross-section for R/Z-
cosets, there is some x ∈ H such that x + Z = θ + Z. Therefore x − θ ∈ Z, mx − mθ ∈ Z, and
then φ(mx) = φ(mθ) = 1 because ker φ = Z. But if H is a cross-section we also know that the
restricted homomorphism φ
H : H → S1 is a bijection, and hence an isomorphism of groups.
Since x ∈ H ⇒ mx = x + . . . + x ∈ H, the only way to get φ(mx) = 1 is to have mx = 0
because φ : H → S1 is one-to-one and we already have φ(0) = 1. This in turn implies that
x = 0, which is impossible because it would imply that θ ≡ x ≡ 0 (mod 1) and hence that θ is
an integer contrary to our choice of 0 < θ < 1. Conclusion: no subgroup can cross-section the
cosets in R/Z. □
 26

6.3 The Sylow theorems.

A group is called a p-group if its order is some power ps of a prime p > 1. If G is a non-
trivial ﬁnite group, its order |G| = n will have various prime divisors pi > 1 with multiplicities
ni ≥ 1 such that |G| = ∏r
i=1 pni
i . We now show that the pattern of subgroups in G is keyed
to these prime divisors and their multiplicities. The connection is revealed in the three “Sylow
Theorems” presented below.

6.3.1 Deﬁnition. Let G be a ﬁnite group whose order has n = ∏r
i=1 pni
i as its prime fac-
torization. A subgroup H ⊆ G is a pi-group if its order is some power of pi. It is a Sylow
pi-subgroup if its order is as large as possible, namely |H| = pni
i . For any prime p > 1 we
write Sylp(G) to indicate the collection of all Sylow p-subgroups in G. Unless p is a divisor
of |G| this collection will be empty; if Sylp(G) ̸= ∅, it might contain several distinct Sylow p-
subgroups.

The main point of the Sylow theorems is that Sylp(G) is not empty if p divides |G|, and this
observation is the starting point if we wish to unravel the structure of a given ﬁnite group.

6.3.2 Theorem (The Sylow Theorems). Let G be a group of ﬁnite order n = ∏r
i=1 pni
i .
Then for each prime factor pi we have

(a) G contains a subgroup Spi which has exactly pni
i elements.

(b) If Spi is a ﬁxed Sylow pi-subgroup, any subgroup H whose order is a power
of pi can be conjugated to lie within Spi – i.e. there is some g ∈ G such
that gHg−1 ⊆ Sp . In particular all Sylow pi-subgroups are conjugates of one
another.
(c) The number of distinct Sylow pi-subgroups is equal to 1 + mpi for some m, so
their number is congruent to 1 (mod pi). The number of p-Sylow subgroups
must also be a divisor of |G|.

For each prime divisor p > 1, all the Sylow p-subgroups are isomorphic since they are conjugates
of each other.

Proof: For (a) we start with the abelian case, working by induction on n = |G|. If n = 1 the
theorem is vacuous, true by default. For n = 2 we have G ∼= Z2; p = 2 is the only divisor and G
itself is the Sylow 2-subgoup. So, we may assume n ≥ 2 and p > 1 is one of its prime divisors,
say with pk the largest power dividing n. In Cauchy’s theorem 4.3.5 we showed that G contains a
cyclic subgroup H = ⟨a⟩ of order |H| = p. Since G is abelian, H is normal; the abelian quotient
G
′ = G/H has order less than n, so we may apply the induction hypothesis to it. By Lagrange’s
theorem 3.4.1, if p is not a divisor of |G/H| then p has multiplicity k = 1 and H is the Sylow
p-subgroup we seek. Otherwise, by Lagrange’s theorem we have |G| = |G/H| · |H| = p|G/H|, so
p is a divisor of |G/H| with multiplicity k − 1 ≥ 1. By the induction hypothesis G/H contains
a Sylow p subgroup H, of order pk−1. The pullback H ′ = π−1(H) = {g ∈ G : π(g) ∈ H} under
the quotient homomorphism π : G → G/H must have order |H ′| = pk since |H ′| = |H| · |H|.
Thus H ′ is a Sylow p-subgroup for G, which proves the abelian version of (a).
For general groups G we again use induction on n = |G| to prove (a), and again the cases
n = 1, 2 are trivial (not to mention abelian). So, assume n ≥ 2 and that p > 1 is a prime divisor
whose largest power in n is pk. If G is nonabelian, the decomposition of G into conjugacy classes
is nontrivial. The class equation 4.3.1 says

|G| = |Z(G)| + ∑

x∈S′ |Cx| = |Z(G)| + ∑

x∈S′
 |G|
|ZG(x)|

where S′ is a set of representatives for the nontrivial conjugacy classes Cx in G, and ZG(x) =
{g ∈ G : gx = xg} is the centralizer of x (the stabilizer StabG(x) when we let G act on itself

27

by conjugation). If there is a nontrivial class Cx such that |ZG(x)| is divisible by pk, then pk

is also the largest power of p that can possibly divide |ZG(x)| since ZG(x) is a subgroup in G.
Clearly |ZG(x)| < |G| because Cx is nontrivial, so by the inductive hypothesis this subgroup
already contains a Sylow p-group for G.
If no such x exists, then for every nontrivial class we have

#(elements in the class) = |G|
|ZG(x)| is divisible by p .

because the multiplicity of p in the centralizer is less than that in G. Therefore by the class
equation, the number of elements in the center Z(G) must also be divisible by p and hence
|Z(G)| must include a factor of the form ps for some 1 ≤ s ≤ k. If s = k we simply apply the
abelian result to Z(G) and are done. Otherwise, consider the quotient group G/Z(G)p where
Z(G)p is the Sylow p-subgroup of the center, with |Z(G)p| = ps. (Any subgroup of the center
Z(G) is normal in G, so the quotient is a group.) Induction applies to this quotient, whose
order involves the prime factor pk−s. Therefore the quotient contains a Sylow p-subgroup Sp
of this order. The pullback Sp in G has order pk since we factor out a group of order ps to get
Spi. This Sp is the desired Sylow p-subgroup in G.
To prove (b) and (c) we use the following instructive lemma about actions of p-groups.

6.3.3 Lemma. Let X be a ﬁnite set acted on by p-group G. Let

X G = {x ∈ X : g · x = x, all g ∈ G}

be the set of G-ﬁxed points in X. Then |X G| ≡ |X| (mod p).

Proof: The set X G is obviously G-invariant and so is the diﬀerence set X ∼ X G, which must
then be a union of disjoint nontrivial G-orbits. The cardinality |G|/|StabG(x)| of any such orbit
is a divisor of |G| and so must be a power ps with s ≥ 1. Hence |O| is congruent to 0 (mod p)
for every nontrivial orbit O in X. But then the same must be true for the union X ∼ X G of
these orbits. That means
 |X| = |X ∼ X G| + |X G| ≡ |X G| (mod p)

as claimed. □

For (b) let n = pkm with gcd(m, pk) = 1, ﬁx a Sylow p-group Sp, and let H be a subgroup
whose order is a power of p. Consider the permutation action of H on the coset space G/Sp.
Then |Sp| = pk and |G/Sp| ≡/ 0 (mod p), so by 6.3.3 there is at least one ﬁxed point xSp in X.
But then HxSp = xSp ⇒ x
−1HxSp = Sp ⇒ x
−1Hx ⊆ Sp and we’re done.
For (c) we ﬁx a Sylow p-subgroup Sp and look at the action of Sp by conjugation on the
set X of all Sylow p-groups. The base point Sp is a ﬁxed point in X; we claim that there
are no others, and then (c) follows from our lemma. If there were another ﬁxed point H it
would be normalized by Sp in the sense that gHg−1 = H for g ∈ Sp. Thus Sp is contained in
the normalizer of H: the subgroup N = {g ∈ G : gHg−1 = H}. Hence Sp and H are Sylow
p-subgroups of N , and by (b) there exists some n ∈ N such that Sp = nHn−1. By deﬁnition
of N this makes Sp = H as claimed.
Let Xp be the set of all p-Sylow subgroups and let P be any base point in Xp. By (b) the
action G × Xp → Xp is transitive so |Xp| = |G|/|StabG(P )| and |G| is a multiple of |Xp|, as
claimed. □

In 4.3.5 (Cauchy theorem) we proved that if p is a divisor of n = |G| then there are elements
in G such that o(x) = p. If pk is the largest power dividing n, one can generalize the Sylow
theorems to prove that there exist subgroups of order pr for every 1 ≤ r ≤ k.

Note: In analyzing the structure of groups, special interest attaches to the p-groups, for which
|G| = pk, so it is worth noting that
 28

Figure 6.7. If prime divisor p of |G| has multiplicity 1, the Sylow p-subgroups
S(1)
p , . . . , S(N)
p are “essentially disjoint” as indicated in (a), so their union has cardinality
|Ep| = N (p−1)+1. If p, q are diﬀerent prime divisors, the unions Ep, Eq of the correspond-
ing Sylow subgroups are essentially disjoint, as in (b), even if p and q have multiplicities
greater than 1 (in which case the individual S(i)
p might have nontrivial overlap). Thus
|Ep ∪ Eq| = |Ep| + |Eq| − 1.

A ﬁnite group G is a p-group ⇔ the order of each element is a power of p.

Implication (⇒) is trivial (Lagrange). For the converse (⇐), if some prime q ̸= p appeared
in the prime decomposition of |G|, then by 4.3.5 there would be a cyclic subgroup of order q,
which is impossible. □

By 6.3.2(b), a Sylow p-subgroup is normal in G if and only if there is just one such subgroup.
Sometimes we can determine when this happens by using 6.3.2(c), and in any case a lot can
be learned about the pattern of Sylow subgroups by looking at intersections of conjugates
Sp ∩ gSpg−1 with Lagrange and the Sylow theorems in mind. For instance, suppose p has
multiplicity 1 in the prime factorization of n = |G|. Then the distinct Sylow p-subgroups
S(1)
p , . . . , S(N )
p all have order p and by Lagrange their pairwise intersections are trivial. Hence
their union has cardinality N (p − 1) + 1, which cannot exceed |G|. This and the requirement
that N ≡ 1 (mod p) can put serious constraints on the S(i)
p . The idea is shown in Figure 6.7.
Another useful counting principle concerns the unions Ep = ⋃N
i=1 S(i)
p and Eq = ⋃M
j=1 S(j)
q
of all the p-Sylow and q-Sylow subgroups in G, where p, q are distinct prime divisors of |G|.
The subgroups in Ep, Eq have orders |S(i)
p | = pk and |S(j)
q | = qℓ where k, ℓ ∈ N. Hence
gcd(pk, qℓ) = 1, which implies that S(i)
p ∩ S(j)
q = (e) for all i, j. That forces the “blobs” Ep and
Eq to be essentially disjoint in the sense that Ep ∩ Eq = (e), because any x ∈ Ep ∩ Eq would
lie in the intersection of a p-Sylow and a q-Sylow subgroup. Obviously the union of these blobs
must ﬁt inside G, so that |Ep ∪ Eq| = |Ep| + |Eq| − 1 ≤ |G|, see Figure 6.7. (There must also
be room outside Ep ∪ Eq for Sylow subgroups associated with other prime divisors of n.) These
constraints can also provide useful information about the pattern of Sylow subgroups in G.

6.3.4 Example. Let G be an arbitrary group of order |G| = 28 = 7 · 22. If H7 is a 7-
Sylow subgroup then |H7| = 7 and N = #(7-Sylow subgroups) is equal to 1 because the next
possible value N = 8 would make the union E7 of the Sylow 7-subgroups have cardinality
8(7 − 1) + 1 = 49, which is bigger than the group itself. (Besides, N = 8 can’t work because it
is not a divisor of |G| = 28.) Thus the 7-Sylow subgroup H7 ∼= (Z7, +) is normal in G.
The 2-Sylow subgroups H2 all have order |H2| = 22 = 4. As shown in Section 6.2, all
groups of order 4 are abelian and up to isomorphism the only possibilities are Z4 (cyclic), and
Z2 × Z2. The number of 2-Sylow subgroups can only be N = 1, 3, 5, 7, ...; only 1 and 7 are
divisors of |G| = 28, so #(2-Sylow subgroups) is either 1 or 7. Fix a 2-Sylow subgroup H2.

29

Then H2 ∩ H7 = (e) since gcd(4, 7) = 1; it follows that |H7 · H2| = 28 and G = H7H2. Thus G
is a semidirect product H7 ×φ H2 = Z7 ×φ H2.

Case 1: H2 ∼= Z4. Identifying H2 = (Z4, +), con-
sider the standard generator a = [1]
4 of Z4. We must
determine all homomorphisms Φ : Z4 → (U7, · ) ∼=
Aut(Z7, +). Since U7 = {[1], [2], [3], . . . , [6]} is abelian
and |U7| = 6 it follows from 6.2.17 that U7 ∼= (Z6, +).
We won’t need this speciﬁc information below, but what
we do need is a list of the orders of the elements in U7,
and the groups ⟨x⟩ they generate, so we can decide which
elements b ∈ U7 may be assigned as images Φ(a) of the
generator of H2. The orders are listed in the table at
right. Since 4 · a = [0] in Z4 ⇒ Φ(a)
4 = [1] in U7, the
only possible assignments are Φ(a) = [1] or [6] = [−1],
which correspond to the automorphisms τ[1] (identity
map) and τ[−1] (inversion) on Z7.

Case 1A: Φ(a) = τ[1] = idZ7. This yields the trivial ac-
tion of H2 = Z4 on N = Z7; the corresponding group is
the direct product G
(1) = Z7 × Z4 ∼= Z28.
 x o(x) Subgroup ⟨x⟩

[1] 1 1

[2] 3 1, 2, 4

[3] 6 all

[4] 3 1, 4, 2

[5] 6 all

[6] 2 1, 6 ≡ −1

Data Table for U7.

Case 1B: Φ(a) = τ[−1] = J (the inversion automorphism on Z7). The automorphisms corre-
sponding to the various elements in Z4 = {j · a : 0 ≤ j < 4} are Φ(j · a) = Φ(a)
j = J j, so
that Φ([0]) = I Φ([1]) = J Φ([2]) = J 2 = I Φ([3]) = J 3 = J

In Proposition 6.2.21 we showed that the multiplication law in the resulting semidirect product
G
(2) = H7 ×φ H2 ∼= Z7 ×φ Z4 takes the form

(29) ([i]
7 , [j]
4) · ([k]
7 , [ℓ]
4) = ([i + (−1)
jk]
7 , [j + ℓ]
4)

6.3.5 Exercise. Suppose we specify generators a, u and write H2 and H7 in multiplicative
notation, so that H2 = {e, a, a
2, a3} and H7 = {e, u, u2, . . . , u6}. Prove that the multiplication
law in G
(2) = H7 ×φ H2 takes the form

(ui, aj) ⋆ (uk, aℓ) = (uiΦ(a)
j(uk), aj+ℓ)

= (ui+(−1)j k, aj+ℓ)(30)

for all exponents i, k ∈ Z7 and j, ℓ ∈ Z4.
Note: In multiplicative notation, Φ(a) = φa is the operator that maps uj to u−j for all 0 ≤ j < 7.
Furthermore, Φ(ai) = Φ(a)
i. □

Case 2: H2 = Z2 × Z2. The analysis is complicated by the fact that the acting group is not
cyclic. It will be convenient to write H2 multiplicatively, as H2 = {e, u, v, w} where

u2 = v2 = w2 = e and uv = w, vw = u, wu = v

Obviously H2 is the internal direct product of the two subgroups ⟨u⟩ ∼= ⟨v⟩ ∼= Z2. Consequently
each element g ∈ H2 has a unique factorization in the form g = uivj with i, j ∈ Z2. As
always, a homomorphism Φ : H2 → (U7, · ) is determined by where it sends the generators u, v.
Furthermore K = ker(Φ) can only have cardinality |K| = 1, 2, 4.

Case 2A: |K| = 4 or 1. In the ﬁrst case H2 = K acts trivially on H7 and we have a direct
product G
(3) = Z7 × Z2 × Z2 ∼= Z14 × Z2. The second case |K| = 1 cannot arise because Φ
would then be injective and Φ(H2) would be a subgroup of order 4 in a group U7 of order 6.

30

Case 2B: |K| = 2. Any such Φ must “kill” e and exactly one other element (sending both to
[1] in U7). By relabeling points in H2 we may assume K = {e, u}; then since w = uv we get

Φ(w) = Φ(u)Φ(v) = Φ(v) with Φ(v) ̸= [1] in U7

Since v2 = e the image Φ(v) can only be an element x in U7 such that x
2 = [1], and since
Φ(v) ̸= [1] the only choice is Φ(v) = [6] = [−1]. This corresponds to the inversion automorphism
τ[−1] = J on Z7, so in this case Φ is fully determined:

Φ(e) = Φ(u) = I Φ(v) = Φ(w) = J

Let us label the resulting semidirect product as G
(4).
Writing both H2 = {uivj : i, j ∈ Z2} (unique factorization) and H7 = ⟨a⟩ in multiplicative
form, the multiplication law in G
(4) = H7 ×φ H2 takes the form

(ak, uivj) ⋆ (aℓ, urvs) = (akΦ(uivj)(aℓ), ui+rvj+s)

= (akΦ(u)
iΦ(v)
j (aℓ), ui+rvj+s)(31) = (akΦ(v)
j(aℓ), ui+rvj+s) (since Φ(u) = I)

= (ak+(−1)j ℓ , ui+rvj+s) □

It would seem that we have produced four distinct groups such that |G| = 28, but ap-
pearances sometimes deceive. How do we know there isn’t some “accidental” isomorphism
G
(i) ∼= G
(j) despite the diﬀerences in the way the groups are constructed? The answer is:
Without further investigation, we don’t! Obviously Z28 ̸∼= Z14 × Z2 (why?), and an abelian
group can’t be isomorphic to a nonabelian group, so the only interesting possibility is that
G
(2) ∼= G
(4). To disprove this we might compare various structural properties of the two groups
– e.g. highest orders of elements, the sizes and isomorphism types of the centers, the number
and size of the conjugacy classes, etc – all of which can be computed once the group law on the
Cartesian product set H7 × H2 has been determined.
There also seems to be a “missing” group of order 28, namely the dihedral group D14.
Where does it appear in the list G
(1), . . . , G
(4)?
A look at the way G
(4) was constructed shows that the element u ∈ H2 ⊆ G
(4) acts
trivially on every element of the normal subgroup H7. This action is just conjugation by u,
φu(n) = unu−1 restricted to elements n ∈ H7, which means that u commutes with all n ∈ H7.
Since u also commutes with everyone in the abelian subgroup H2 it follows that u commutes
with all g ∈ G
(4) = H7H2. Thus the cyclic subgroup U = ⟨u⟩ ∼= Z2 is in the center of G
(4).
Obviously U ∩ H7 = (e), so the product set M = U · H7 is a normal subgroup of order 14 in
G
(4), and is isomorphic to Z2 × Z7 ∼= Z14. On the other hand, every element of G
(4) has a
unique factorization g = xy with x ∈ H7, y ∈ H2. From this it follows easily that the element
v ∈ H2 lies outside of M , and since o(v) = 2 the subgroup V = ⟨v⟩ ∼= Z2 has the properties
V ∩ M = (e), M V = G
(4), M ⊳ G
(4). This allows us to recognize G
(4) as a semidirect product
M ×φ V ∼= Z14 ×φ Z2.
In fact, G
(4) is the missing dihedral group. The possible semidirect products Z14 ×φ Z2 cor-
respond to homomorphisms Φ : Z2 → U14 ∼= Aut(Z14, +). But U14 = {[1], [3], [5], [9], [11], [13]}
is abelian and has order 6, hence U14 ∼= Z6; only the elements x = [1] and x = [13] = [−1] in U14
satisfy the compatibility condition x
2 = [1], so the only possible assignments of the generator
v ∈ V ∼= Z2 to elements in U14 are

Φ(v) = τ[1] = idM
Φ(v) = τ[−1] = J (inversion automorphism on M = Z14)

The ﬁrst would make G
(4) an abelian direct product Z14 × Z2, which is impossible; the other
choice clearly yields G
(4) ∼= D14.
 31

Is G
(2) ∼= G
(4)? We have just seen that |Z(G
(4))| ≥ 2. On the other hand an element
g = ukaℓ is in the center of G
(2) ⇔ e = xgx
−1 for all x = uiaj ∈ G
(2). Applying the
multiplicative form of the group law in G
(2) worked out in equation (30), we get

e = (uiaj)(ukaℓ)(a−ju−i)

= ui(ajuka−j)(aℓu−ia−ℓ)aℓ

= uia(−1)j k(a−(−1)ℓi)aℓ

= u(−1)jk+[1−(−1)ℓ]i aℓ

for all i, j. By unique decomposition we must have aℓ = e; hence ℓ ≡ 0 (mod 4) and [1−(−1)
ℓ] =
0. We then get u(−1)j k = e and hence k ≡ 0 (mod 7)

Therefore g = ukaℓ = e is the only central element in G
(2) and G
(2) cannot be isomorphic to
G
(4).

Abelian groups and the Sylow theorems. If G is a ﬁnite abelian group the Sylow theorems
provide an explicit natural direct product decomposition. This is not the ﬁnal answer if we want
to know the detailed structure of ﬁnite abelian groups, but it is a big step in that direction. The
proof uses the observation that in an abelian group all Sylow p-subgroups are automatically
normal subgroups, and hence by Theorem 6.3.1(b) there is just one Sylow p-subgroup for each
prime divisor of the order |G|.

6.3.6 Theorem. Any ﬁnite abelian group is isomorphic to a direct product Sp1 × . . . × Spr
where n = ∏r
i=1 pni
i is the prime decomposition of the order |G| = n and Spi is the unique Sylow
pi-subgroup in Gof order pni
i . This direct product decomposition is canonical: the subgroups Spi
are uniquely determined, as are the primes pi and their exponents ni.

Note: The components Spi need not be cyclic groups. For instance, if p = 2 we might have
S2 = Z2 × Z4 which cannot be isomorphic to the cyclic group Z8 of the same size. Determining
the ﬁne structure of the components Spi would require further eﬀort, leading to the Fundamental
Structure Theorem for ﬁnitely generated abelian groups. The coarse decomposition 6.3.6 is the
ﬁrst step in that direction.

Proof: Let’s write Si for the unique Sylow pi-subgroup. For each index index 1 ≤ i ≤ r the
product set Hi = ∏i
j=1 Sj is a normal subgroup (G is abelian). We now apply Lagrange’s

theorem and the counting principle 3.4.7 to show that its order is |Hi| = ∏i
j=1 pnj
j . Obviously
|H1| = |S1| = pn1
1 . When i = 2, the order of the subgroup H1 ∩ S2 = S1 ∩ S2 must divide both
pn1
1 and pn2
2 , and hence the intersection H1 ∩ S2 is trivial; it follows immediately from 3.4.7 that
H2 = H1S1 has cardinality |H1|·|S2|/|H1 ∩S2| = pn1
1 pn2
2 . At the next stage we have H3 = H2S3
and H2 ∩ S3 is again trivial because these subgroups have diﬀerent prime divisors; applying
3.4.7 we get |H3| = |H2| · |S3| = pn1
1 pn2
2 pn3
3 . Continuing inductively we prove our claim.
This already implies that G is a direct product. In fact, since |G| = |Hr| we see that G
is equal to the product set S1S2 . . . Sr. It remains only to check that if a1a2 . . . ar = e with
ai ∈ Si, then each ai = e. Let q be the smallest index such that a non-trivial decomposition of
the identity occurs. Certainly q > 1 and aq ̸= e, and then a−1
q = a1 . . . aq−1. But on the left
we have an element of Sq and on the right an element of the subgroup Hq−1. These subgroups
have trivial intersection, which is impossible if aq ̸= e. Thus every element in G has a unique
decomposition of the form a1a2 . . . ar, and G is the direct product of its Sylow subgroups. □

Essentially, this result says that to understand the the internal structure of any ﬁnite abelian
group it suﬃces to analyze the abelian p-groups – those with just one prime divisor and order
pk for some k
In order for the Sylow subgroups to be useful indicators of the overall structure for noncom-
mutative G it is necessary to prove that they are pervasive in G. Here’s what that means.

32

6.3.7 Lemma. Let G be a nontrivial ﬁnite group and let S be the subgroup generated by all
the Sylow subgroups in G:
 S = ⟨
 r⋃

i=1
 ⋃ {H : H ∈ Sylpi(G)} ⟩

where the pi > 1 are the prime divisors of |G|. Then S is all of G.

Proof: The result has already been established when G is abelian. We argue by induction on
n = |G|. The result is trivial when n = 2, so we may assume that n > 2 and that the theorem
is true for all groups of order at most n − 1.
If S ̸= G, there exist elements a /∈ S. The cyclic subgroup M = ⟨a⟩ must have order |M | = m
that divides |G| = n, which means that only the pi can appear in the prime factorization of
m. Let p be one of those primes. Any Sylow p-subgroup for M will have order ps for some
s ≤ ni (if p = pi). By Theorem 6.3.1(b), every such subgroup must be contained in one of the
Sylow p-subgroups for G. The product of the Sylow subgroups in M is therefore contained in
S. But by its deﬁnition M is abelian and hence (by 6.3.5) is the product of its Sylow subgroups,
which means we have a ∈ M ⊆ S. That is impossible since we are assuming a lies outside S.
Conclusion: we must actually have G = S, as claimed. □

A Case Study: The Groups of Order 12. The following analysis of all groups of order 12
will draw upon almost everything discussed so far.

6.3.8 Example (Groups of Order 12). Classify all groups with |G| = 12 up to isomorphism.
Identify all semidirect products in this family.

Discussion: There are Sylow subgroups Hp for the prime divisors p = 2, 3, with |H2| = 4 and
|H3| = 3; thus H3 ∼= Z3 while H2 could be either Z4 or Z2 × Z2 (abelian). We obviously have
H2 ∩ H3 = (e) and |H2 · H3| = 4 · 3/|H2 ∩ H3| = 12, so that H2H3 = G. Now let Ep be the
union of all conjugates of Hp. Then E2 ∩ E3 = (e) because all intersections Hp ∩ Hq are trivial
when p ̸= q.
By 6.3.2 we have

#(Sylow 2-subgroups) = 1 (if H2 ⊳ G), or 3

#(Sylow 3-subgroups) = 1 (if H3 ⊳ G), or 4

If H3 is not a normal subgroup the union of its conjugates has cardinality |E3| = 4(3−1)+1 = 9,
since conjugates of H3 intersect only at the identity. In this situation, the other Sylow subgroup
H2 must be normal, otherwise E2 ∪ E3 would contain more than 12 points. (An argument of
this sort cannot be made when H2 is non-normal because conjugates of H2 might overlap in
subgroups of order 2.) The conclusion is

At least one of the subgroups H2, H3 must be normal in G

and hence every G of order 12 can be realized as a semidirect product. We will employ the
Chinese Remainder Theorem 6.1.26 in our analysis of these products.

Case 1: Both H2, H3 normal. Then G is the direct product H2 × H3 and is abelian. The
possible distinct isomorphism types are

Group G
(1) : Z3 × Z4 ∼= Z12
Group G
(2) : Z3 × (Z2 × Z2) ∼= Z6 × Z2

Case 2: Only H3 is normal. Then G is a semidirect product Z3 ×φ Z4 or Z3 ×φ (Z2 × Z2).

Case 2A: If H2 = Z4, let us write both H2 and H3 ∼= Z3 in additive notation. Then G is
determined by some homomorphism

Φ : Z4 → (U3, · ) ∼= Aut(Z3, +)

33

Since |U3| = 2 the only possible assignments for the cyclic generator a = [1]
4 in Z4 are Φ(a) = id
(in which case G is one of the abelian groups already listed), or Φ(a) is the inversion map
J([k]) = −[k], [k] ∈ Z3. Then we we get a new group of order 12.

Group G
(3). This group is the the semidirect product Z3 ×φ Z4 whose multiplication
operation has been described in (26) of proposition 6.2.21:

([i]
3 , [j]
4) ⋆ ([k]
3 , [ℓ]
4) = ([i] + Φ(a)
j ([k]) , [j] + [ℓ])
= ([i + (−1)
jk]
3 , [j + ℓ]
4)(32)

for all [i], [k] ∈ Z3, [j], [ℓ] ∈ Z4.

Note that Φ(e) = Φ(2 · a) = Φ(a)
2 = id and Φ(a), Φ(3 · a) = Φ(a)
3 are both equal to J.

6.3.9 Exercise. In terms of generators and relations, G
(3) is generated by elements x, y which
satisfy the relations x
3 = e y4 = e yx = x
2y

Verify this claim. Which elements in Z3 ×φ Z4 should be identiﬁed with x and y? □

Case 2B: If H2 = Z2 × Z2 let’s write both H2 and H3 in multiplicative form

H2 = {uivj : i, j ∈ Z2} H3 = {e, a, a
2}

as in 6.3.4. Since Aut(H3) ∼= Aut(Z3, +) ∼= (U3, · ) ∼= (Z2, +), any nontrivial homomorphism
Φ : H2 → Aut(H3) will have a kernel ker(Φ) of index 2 in H2. By changing our labeling of
elements in H2 we may assume that Φ is the map

Φ(e) = Φ(u) = I Φ(v) = Φ(uv) = J (Inversion map J : ai → a−i on H3)

The multiplication law for the resulting semidirect product G
(4) = H3 ×φ H2 then takes the
form
 (ak, uivj) ⋆ (aℓ, urvs) = (akΦ(uivj)(aℓ) , ui+rvj+s)

= (akJ j(aℓ) , ui+rvj+s)(33)
 = (ak+(−1)j ℓ , ui+rvj+s)

for all exponents i, j, r, s ∈ Z2 and k, ℓ ∈ Z4. This is a familiar group in disguise.

Group G
(4). Up to isomorphism, this semidirect product Z3 ×φ (Z2 × Z2) is the
dihedral group D6

In fact, the element u ∈ H2 is central in G because Φ(u) = I, and it generates a subgroup
Z = ⟨u⟩ ∼= Z2 such that Z ∩ H3 = (e). Thus N = H3 · Z is a subgroup isomorphic to
Z3 × Z2 ∼= Z6 that is normal in G, with index |G/N | = 2. The element v in H2 generates a
copy of Z2 transverse to N . It is easy to check that the element ρ = au is a cyclic generator for
N and that σ = v, with o(σ) = 2 satisﬁes the dihedral relation σρσ−1 = ρ−1. It follows that
G
(4) ∼= D6 as claimed.

Case 3: Only H2 is normal. If H2 ∼= Z4 then G = H2 ×φ H3 is determined by by some
homomorphism Φ : Z3 ∼= Z3 → (U4, · ) ∼= (Z2, +). Since gcd(2, 3) = 1, Φ must be trivial and we
get nothing new.
If H2 ∼= Z2 × Z2 we again employ multiplicative notation for both H2 and H3, as in Case
2B. Important insight is achieved if we relabel elements of H2 = {uivj : i, j ∈ Z2} as

e, x1 = u, x2 = v, x3 = uv ,

34

Observe that xixi+1 = xi+2 = xi−1 for 1 ≤ i ≤ 3 when subscripts are reckoned (mod 3), and
that xixi = e. (Thus for instance, x1x2 = uv = x3, x2x3 = v · uv = u = x1 etc.) Elements in
Aut(H2) permute the xi leaving e ﬁxed, and all permutations of [1, 3] are accounted for.

6.3.10 Exercise. Prove that every permutation σ of the integers [1, 3] yields an automorphism
τ of Z2 × Z2 = {e, x1, x2, x3} such that

τ (e) = e, τ (xi) = xσ(i) for 1 ≤ i ≤ 3

Verify that the correspondence σ ∈ S3 ↦→ τ ∈ Aut(H2) is bijective and an isomorphism of
groups. □

Thus we obtain a natural identiﬁcation of Aut(H2) with the permutation group S3. A homo-
morphism Φ : Z3 → Aut(H2) ∼= S3 must carry the cyclic generator a ∈ H3 to a permutation
Φ(a) = σ such that σ3 = e. The case σ = e is uninteresting since it yields the trivial action,
so we must assign Φ(a) = (123) or Φ(a) = (132) = (123)
−1. Both choices yield isomorphic
semidirect products since they diﬀer only in the way we label nontrivial elements in H2, so we
may as well take Φ(a) = (123), which corresponds to the automorphism

Φ(a)(e) = e Φ(a)(u) = v, Φ(a)(v) = uv, Φ(a)(uv) = u

of H2. The new group G
(5) = H2 ×φ H3 ∼= (Z2 × Z2) ×φ Z3 has the following multiplication law

(34) (uivj, ak) ⋆ (urvs, aℓ) = (uivj · Φ(a)
k(urvs) , ak+ℓ)

for exponents i, j, r, s ∈ Z2, k, ℓ ∈ Z4.
The role of the permutation (123) in this group law becomes clearer when we label elements
in H2 as e, x1, x2, x3. Then Φ(a)xi = xi+1 and Φ(a)
kxi = xi+k if we reckon subscripts (mod
3), and the multiplication law (35) takes the form

(e, ak) ⋆ (e, aℓ) = (e, ak+ℓ)
(e, ak) ⋆ (xi, aℓ) = (e · Φ(a)
k(xi) , ak+ℓ)

= (xi+k, ak+ℓ)
(xi, ak) ⋆ (e, aℓ) = (xi · Φ(a)
k(e) , ak+ℓ)

= (xi, ak+ℓ)
(xi, ak) ⋆ (xj , aℓ) = (xi · Φ(a)
k(xj ) , ak+ℓ)

= (xixj+k, ak+ℓ)

To evaluate the last type of product we might need to make a 4 × 4 multiplication table for
elements of H2; there is no simple algebraic formula m = m(i, j) for rewriting products xixj in
the form xm with 1 ≤ i, j, m ≤ 3. (The formula xixi+1 = xi+2 only applies when j = i ± 1.)
We have identiﬁed a new group.

Group G
(5): the semidirect product H2 ×φ H3 ∼= (Z2 × Z2) ×φ Z3 with multiplication
law (35) is isomorphic to the group of even permutations A4. It is also the group of
orientation-preserving symmetries of the regular tetrahedron.

A regular tetrahedron centered at the origin T ⊆ R3 is exceptional in that every permutation
of its four vertices corresponds to an orthogonal linear transformation (rigid motion) in R3 that
maps the tetrahedron to itself. It can be shown by convexity arguments that there are no other
rigid-motion symmetries of this solid, so the full symmetry group of the tetrahedron is ∼= S4.
In this picture, the even permutations A4 correspond to the subgroup of orientation-preserving
symmetries, which are all rotations through axes passing through the center of T; the full group
S4 includes some reﬂections across planes passing through the origin. Obviously |A4| = 12.

35

To see why the group described in (35) is isomorphic
to A4, regarded as the symmetry group of the tetrahe-
dron T, consider the tetrahedron shown in Figure 6.8
with vertices labeled 1, 2, 3, 4. Any 2,2-cycle, such as
(12)(34), corresponds to a 180◦ rotation about an axis
passing through the midpoints of opposite edges. We
have previously shown (Chapter 5) that the Klein Vier-
group N = {e} ∪ {all three 2,2-cycles}

is a normal subgroup in S4 isomorphic to Z2 × Z2. For
each axis passing through a vertex and the center of the
opposite face, we get a subgroup of order 3 (one of the
four Sylow subgroups H3) consisting of 0◦, 120◦, and
240◦ rotations about this axis. For example the sub-
group {e, (123), (132)} corresponds to rotations about
the axis passing through vertex 4 and the center of
the opposite face. With these geometric descriptions
in mind, it is not hard to see how to identify elements
in our abstract model (35) with the correct geometric
operations on T. □
 Figure 6.8. A regular tetrahedron
centered at the origin. We show:
rotation A1 by 120
◦ about an axis
through vertex 1, and B13 by 180
◦

about an axis through midpoints of
opposite edges.

6.3.11 Exercise. Explain why the ﬁve groups G
(1), . . . , G
(5) of order 12 are pairwise non-
isomorphic. □

We take up one last example to show that the Sylow theorems do not always yield a deﬁnitive
analysis, and that as the order of G increases we begin to encounter groups that are not
semidirect products – i.e. they arise as extensions e → N → G → G/N → e that do not split.

6.3.12 Example (Groups of order 8). These are all p-groups so the Sylow theorems are
not much help; however by (3.2.5, 3.2.6) we know G has nontrivial center Z = Z(G), which
can only have order 2, 4, 8. If |Z| = 8 the group is abelian and the possibilities are G =
Z8, Z4 × Z2, Z2 × Z2 × Z2, in view of the following result.

6.3.13 Lemma. If G is abelian with |G| = 8 then G is isomorphic to Z8, Z4 × Z2, or
Z2 × Z2 × Z2.

Proof: If the maximum order of an element is o(x) = 8 then G ∼= Z8. If the maximum is 4,
say for x = a, then A = ⟨a⟩ ∼= Z4. Suppose there exists some b /∈ A such that o(b) = 2. Then
B = ⟨b⟩ ∼= Z2 is transverse to A, A ∩ B = (e), AB = G, and since G is abelian it is a direct
product ∼= Z4 × Z2.
Otherwise we have o(b) = 4 for all b /∈ A and B ∼= Z4, but now we must have |A ∩ B| = 2
(because |G| = |A|·|B| = 16 if A∩B = (e)). The only subgroup of Z4 with order 2 is {[0]
4, [2]
4},
whose nontrivial element has order 2. That means a2 and b2 are the only elements of A and B
of order 2, and we must have a2 = b2, a−2 = a2, b−2 = b2, and A ∩ B = {e, a2}. Now look at
the powers of the element ab: we get e, ab, (ab)
2 = a2b2 = a2a−2 = e. Since b /∈ A ⇒ ab /∈ A we
have found an element outside of A with order 2. Contradiction. This case cannot arise. □

If |Z| = 4 then G/Z ∼= Z2. Since G/Z is cyclic and Z is central in G, G must be abelian
(why?). Contradiction. Thus |Z| cannot equal 4.

6.3.14 Exercise. If G is a ﬁnite group and Z a subgroup such that (i) Z is central in G
(zg = gz for all z ∈ Z, g ∈ G), and (ii) G/Z is cyclic, prove that G must be abelian. □

Assuming |Z| = 2, let x be an element of highest order in G. We can only have o(x) = 2
or 4 (G is abelian if o(x) = 8). In the ﬁrst case all elements y ̸= e would have order 2 and

36

G ∼= Z2 × Z2 × Z2 (see Exercises 6.2.29 - 30). Abelian G have already been excluded, so we
must have o(x) = 4 and N = ⟨x⟩ is isomorphic to Z4; the following elementary result shows
that N is also normal in G.

6.3.15 Exercise. Let G be a group and H a subgroup of index |G/H| = 2. Prove that H is
automatically normal in G.
Hint: There are just two cosets, H and xH with x /∈ H. Show that xHx
−1 = H. □

We now have an extension

e −→ N ∼= Z4 −→ G −→ Q = G/N ∼= Z2 −→ e

and the real issue is whether it splits.
If it does there is a subgroup Q = ⟨y⟩ ∼= Z2 transverse to G/N cosets and we have a
semidirect product N ×φ Q. We saw in 1.3.2 that Aut(Z4, +) ∼= (U4, · ) ∼= (Z3, +). The only
possible homomorphisms Φ : Z2 → Aut(N ) must map the nontrivial element y ∈ Q to either

(a) Φ(y) = id
N , in which case G is an abelian direct product Z4 × Z2, a
possibility we have already excluded.
(b) Φ(y) = the inversion map, which takes [k]4 to −[k]4 = [4 − k]4 in Z4.
In this case:

x
4 = e, y2 = e, yxy = yxy−1 = Φ(y)(x) = x
−1

Obviously this G is isomorphic to the the dihedral group D4.

In the non-split case we claim that G is the group of unit quaternions Q8 = {±1, ±i, ±j, ±k}
in which the elements ±1 are central, −i = (−1)i, . . . , −k = (−1)k and

(−1)
2 = 1 i2 = j2 = k2 = ijk = −1

from which we get other familiar relations such as ij = k = −ji, jk = i = −kj, . . .. Given Q8
it is easy to check that its center is Z(Q8) = {1, −1} and that N = ⟨j⟩ = {1, j, −1, −j} is a
cyclic normal subgroup ∼= Z4. But as you can easily check, the only elements g ∈ Q8 such that
g2 = 1 are ±1, which lie in N ; thus the extension Q8 of G/N ∼= Z2 by N ∼= Z4 cannot split.
It remains to check by hand that up to an isomorphism Q8 is the only possibile non-split
extension. Taking an x ∈ G that generates a cyclic normal subgroup N ∼= Z4, let y be any
element lying outside N , so that G = ⟨x, y⟩. Since our extension does not split we cannot have
o(y) = 2, but y2 ≡ e (mod N ) so y2 ∈ {x, x
2, x
3 = x
−1}. The ﬁrst and last possibilities are
excluded: if, say, y2 = x then y3 = xy = yx and G would be abelian. Hence our generators x, y
satisfy o(x) = o(y) = 4 y /∈ N = ⟨x⟩ y2 = x
2

Let us write “−1” for the element x
2 = y2 and “1” for the identity element in G. Then
(−1)
2 = 1 and −1 is central in G (because (−1)x = x
2x = x(−1), and likewise for y). Next
observe that z = xy satisﬁes z2 = −1. To see this, ﬁrst note that xy /∈ N but (xy)
2 ∈ N . If
xyxy = x then yxy = e and x = y2 = x
2, which is impossible; likewise we get xyxy ̸= x
3.
So, we must have (xy)
2 = x
2 – i.e. xyz = xy(xy) = −1. We conclude that G ∼= Q8 when we
identify with 1, i, j, k with 1, x, y, z and −1 = x
2 = y2, −i = x
3, −j = y3, −k = z3. □

To summarize: the only groups of order 8 are Q8, D4, Z8, Z4 × Z2, and Z2 × Z2 × Z2.
Deciding whether an extension e → N → G → G/N → e splits can be diﬃcult. Even if N
and G/N are cyclic, the extension need not split – the group Q8 of quaternion units being one
counterexample.
Keeping in mind that G ∼= Zp for any group of prime order p > 1, we have now identiﬁed
all groups of order |G| ≤ 13 except for those of orders 9 and 10. You might try your hand at
ﬁlling in these gaps.
 37

6.3.16 Exercise. If |G| = 9 prove that

(a) G is abelian

(b) G is isomorphic to Z9 or Z3 × Z3.

Explain why the groups in (b) are not isomorphic. □

6.3.17 Exercise. Determine all groups of order |G| = 10 □

38

6.4 Some types of groups: simple, solvable, nilpotent.

A group is simple if it contains no proper normal subgroups, which is to say it has no proper
quotients G/N ; by this deﬁnition, the trivial group is not simple. In view of Cauchy’s theorem
4.3.5, the only simple ﬁnite abelian groups are (Zp, +) where p > 1 is prime. Noncommutative
examples include the alternating groups An, consisting of all even permutations in the full
permutation group Sn on n objects. The fact that An is simple for n ≥ 5 is of great importance
in Galois’ theory of equations; Sn itself is not simple because it always has An as a proper
normal subgroup.
Complementary to the simple groups we have the solvable and nilpotent groups. For any G,
ﬁnite or not, two descending series of normal subgroups can be deﬁned in terms of commutators
[x, y] = xyx
−1y−1. If A, B are subgroups we deﬁne the associated group [A, B] to be the
subgroup generated by all commutators formed from elements of A and B:

(35) [A, B] = ⟨ xyx
−1y−1 : x ∈ A, y ∈ B ⟩

The commutator subgroup [G, G] obtained by taking A = B = G is of particular importance.
First, it is a normal subgroup, but in fact it is a characteristic subgroup, which means it is
invariant under all α ∈ Aut(G). This follows because the image of a commutator [x, y] under
any automorphism α has the form

(36) α([x, y]) = [α(x), α(y)] for all x, y ∈ G

and again is a commutator. Second, the quotient G/[G, G] is abelian because we are factoring
out all relations associated with noncommutativity of G. In fact, the commutator group is the
smallest normal subgroup such that G/N is abelian.

6.4.1 Exercise. Suppose S is a subset of a group G and let H = ⟨S⟩ be the subgroup it
generates. If φ : G → G is a homomorphism that maps S into itself, prove that φ leaves the
generated subgroup invariant too – i.e. φ(H) ⊆ H.
Hint: Recall that ⟨S⟩ is deﬁned to be the smallest subgroup in G that contains S. It is also
described by “building up from S” as ⟨S⟩ = {a1a2 . . . ar : r < ∞ and ai ∈ S ∪ S−1} – i.e.
⟨S⟩ is the set of all “words” of ﬁnite length whose letters are of the form s or s−1. The latter
viewpoint might be congenial in proving that φ(H) ⊆ H. □

6.4.2 Exercise. If α ∈ Aut(G) and x, y ∈ G, verify the identity (28) and then use it to prove
that the commutator subgroup [G, G] is a characteristic subgroup in G.
Hint: Use the previous exercise. □

6.4.3 Exercise. If G is any group and N any normal subgroup, prove that G/N is abelian if
and only if N ⊇ [G, G]. □

Obviously G is abelian ⇔ [G, G] is trivial.
We now deﬁne the upper/lower derived series to be the descending series of subgroups
shown in Figure 6.9. Both series begin with G followed by D1(G) = D1(G) = [G, G]. In order
to understand these deﬁnitions it would be useful to verify that in the right hand series we have
Dk+ℓ(G) = Dk(Dℓ(G)). This is almost obvious (by induction on k); it is not true for the series
on the left.
The horizontal inclusions shown in Figure 6.9 follow by an easy inductive argument from the
fact that A
′ ⊇ A ⇒ [A
′, B] ⊇ [A, B]. A recursive argument based on Exercises 6.4.1-2 shows
that all subgroups in Figure 6.9 are normal, and in fact are characteristic subgroups in G. For
example, we know that D1(G) = [G, G] is characteristic by 6.4.2. The next derived group D2(G)
is generated by commutators [g, a] such that g ∈ G, a ∈ D1(G); but an automorphism α ∈
Aut(G) maps generators to generators in D2(G) because α([g, a]) = [α(g), α(a)] ∈ [G, D1(G)].
Hence by 6.4.1 the subgroup D2(G) is invariant under α. Similar arguments, which we omit,

39

G G
∪ ∪
D1(G) = [G, G] = D1(G) = [G, G]
∪ ∪
D2(G) = [G, D1(G)] ⊇ D2(G) = [D1(G), D1(G)]
∪ ∪
D3(G) = [G, D2(G)] ⊇ D3(G) = [D2(G), D2(G)]
∪ ∪
... ...
∪ ∪
Dk+1(G) = [G, Dk(G)] ⊇ Dk+1(G) = [Dk(G), Dk(G)]
∪ ∪
... ...
Upper Derived Series Lower Derived Series

Figure 6.9. The two derived series for G.

show that all the subgroups Dk(G) and Dk(G) are invariant under all automorphisms of G.

6.4.4 Exercise. Fill in the details needed to show

(a) A
′ ⊃ A ⇒ [A
′, B] ⊇ [A, B]

(b) The inclusions shown in Figure 6.9 are valid

(c) The Dk(G) are all characteristic subgroups in G.

(d) The Dk(G) are all characteristic subgroups in G.

(e) Dk+ℓ(G) = Dk(Dℓ(G)) for all k, ℓ ≥ 1.

(f) If H ⊆ G then Dk(H) ⊆ Dk(G) and Dk(H) ⊆ Dk(G). □

It is possible that one or both series stabilize after a ﬁnite number of steps, so that

G ⊇ D1(G) ⊇ . . . ⊇ Dk(G) = Dk+1(G) = . . .

or G ⊇ D1(G) ⊇ . . . ⊇ Dk(G) = Dk+1(G) = . . . ,

Clearly, once two successive groups are equal, say Dk(G) = Dk+1(G), then all later subgroups
are the same. Furthermore if G is ﬁnite the subgroups must “stabilize.” When this happens the
repeating stable subgroup need not be trivial; for example the alternating group An (n ≥ 5) has
no proper normal subgroups and is nonabelian, so the lower derived series for the permutation
group is Sn ⊇ An = An = . . ..
For inﬁnite groups these descending series might not stabilize at all, as is true for the free
group F2 on two generators. [One can, with some eﬀort, prove that F2 is residually nilpotent
in the sense that ⋂∞
k=1 Dk(F2) = (e).]
Two important classes of groups are deﬁned by the properties of their derived series.

6.4.5 Deﬁnition. A group G is nilpotent if the upper derived series is eventually trivial,
and G is solvable if the lower derived series becomes trivial in ﬁnitely many steps. Obviously
(nilpotent) ⇒ (solvable), but the converse fails. □

6.4.6 Exercise. The aﬃne group of the line G = Aﬀ(2, R) consists of the operators

T(a,b) : R → R with a > 0, b ∈ R T(a,b)(x) = ax + b

which form a group under composition.
 40

(a) Verify that G is a group and work out formulas for computing (i) T(a,b) ◦
T(a′,b′), and (ii) T −1
(a,b).

(b) Verify that N = {T(1,b) : b ∈ R} is a normal subgroup isomorphic to R
and that G/N ∼= R. Hint: The exponential map identiﬁes (R, +) with the
multiplicative group of numbers a > 0.
(c) Compute the derived group [G, G] and verify that G is solvable.

(d) Show that the center Z(G) is trivial, and that G is not nilpotent.

Note: This group is often referred to as the “ax + b group,” for obvious reasons. □

6.4.7 Exercise. The 3 × 3 Heisenberg group can be described as the set of upper triangular
matrices
 G =
 






 1 x z
0 1 y
0 0 1
 

 : x, y, z ∈ R





We shall label group elements by the symbol strings (x, y, z)

(a) In terms of these parameters compute the form of the product (x, y, z) ∗
(x
′, y′, z′) = . . . of two group elements and the inverse (x, y, z)
−1 = . . ..
(b) Show that Z(G) = {(0, 0, z) : z ∈ R} and identify the commutator subgroup
[G, G].

Then verify that G is nilpotent. □

We now list some basic combinatorial facts about these groups. The ﬁrst is just an exercise in
understanding the deﬁnitions.

6.4.8 Exercise. Show that any homomorphism φ : G → G
′ preserves the various derived
subgroups:

(i) φ(Dk(G)) = Dk(φ(G)) ⊆ Dk(G
′)

(ii) φ(Dk(G)) = Dk(φ(G)) ⊆ Dk(G
′)

for all k = 1, 2, . . ..
Hint: Use Exercise 6.4.1 and induction on the index k. □

It follows almost immediately that all homomorphic images and all subgroups of nilpotent (or
solvable) groups are again nilpotent (or solvable). [For quotients, apply Exercise 6.4.8. For any
subgroup H we have [H, H] ⊆ [G, G], and then inductively we get [H, Dk(H)] ⊆ [G, Dk(G)]
and [H, Dk(H)] ⊆ [G, Dk(G)] for k = 1, 2, . . .. Thus Dr+1(G) = (e) ⇒ Dr+1(H) = (e), and
similarly for the lower derived series.] As a corollary we obtain a basic combinatorial result:

6.4.9 Lemma. If N ⊳ G is a normal subgroup of a group G, giving us the sequence of homo-
morphisms e −→ N id
−→ G π
−→ G/N −→ e ,

then G is solvable if and only if G/N and N are solvable.

Proof: We have just discussed (⇒), and conversely if π : G → G/N is the quotient homomor-
phism, solvability of G/N insures that Dn+1(G/N ) = (e) for some n. Exercise 6.4.8 insures
that π(Dn+1(G)) = Dn+1(G/N ) = (e), and hence Dn+1(G) ⊆ N . Taking k so Dk+1(N ) = (e)
we get Dk+n+2(G) = Dk+1(Dn+1(G)) ⊆ Dk+1(N ) = (e). □

Nilpotent groups do not share this property, see Exercise 6.4.6 where N ∼= R and G/N ∼= R are
nilpotent (abelian) but G is not nilpotent. But for solvable groups there is an even stronger
result which sheds light on how they are put together.

41

6.4.10 Lemma. A group G is solvable if there exist subgroups

G = G0 ⊇ G1 ⊇ . . . ⊇ Gr ⊇ Gr+1 = (e)

such that

(i) Gj+1 is a normal subgroup in Gj for each j,

(ii) each quotient Gj/Gj+1 is solvable.

In particular G is solvable if the quotients are all abelian. Conversely, if G is solvable such
sequences exist and the subgroups can be chosen so each quotient is abelian.

Proof: The previous remarks show that we can work backward up the chain G ⊇ D1(G) ⊇
D2(G) ⊇ . . ., successively verifying solvability of Gr, Gr−1, . . .. Starting from the top, Ex-
ercise 6.4.3 shows that G/D1(G) = G/[G, G] is abelian, but since D2(G) = D1(D1(G)) =
[D1(G), D1(G)] we see that D1(G)/D2(G) is abelian, etc. □

Nilpotent groups, unlike solvable groups, always have nontrivial centers. In fact, if Dr(G) ̸= (e)
and Dr+1(G) = [G, Dr(G)] = (e), we see that Dr(G) is a nontrivial central subgroup in G.
Central subgroups play a prominent role in the nilpotent analog of 6.4.10.

6.4.11 Lemma. A group G is nilpotent if there there is a subgroup N such that (i) N is central
in G, and (ii) G/N is nilpotent.

Proof: All subgroups of the center Z(Gj) are normal in Gj , so G/N is a bona-ﬁde group.
Now observe that Dr+1(G/N ) = (e) for some r and that Dr+1(G/N ) = π(Dr+1(G)) un-
der the quotient map π. Thus Dr+1(G) ⊆ N = ker π, and since N is central in G we get
Dr+2(G) = [G, Dr+1(G)] ⊆ [G, N ] = (e). Thus G is nilpotent. □

For other conditions leading to nilpotence of G see 6.4.13 below.
One useful consequence of 6.4.11 is the fact that nonabelian ﬁnite groups always include
sizeable nilpotent subgroups, namely their Sylow p-subgroups.

6.4.12 Corollary. If |G| = pk for some prime then G is nilpotent.

Proof: If k = 1 then G ∼= Zp, so assume k > 1. Then the center Z(G) is nontrivial and
|G/Z(G)| = pr for some r < k. By induction G/Z(G) is nilpotent, and since Z(G) is central G
must be nilpotent too. □

Nilpotent groups are the next best thing to being abelian; solvable groups also have some
commutative aspects, but the connection is more tenuous. The pervasive role of “centers” in
nilpotent groups is revealed by noting that there is a third canonical series of subgroups in any
group G, the ascending central series Z(G) ⊆ Z (2) ⊆ Z (3) ⊆ . . . deﬁned as follows.

Z (1) = Z(G) (the center of G)
Z (2) = {x ∈ G : xy ≡ yx (mod Z(G)), all y ∈ G}

Z (3) = {x ∈ G : xy ≡ yx (mod Z (2)), all y ∈ G}
...(37) Z (k+1) = {x ∈ G : xy ≡ yx (mod Z (k))}
...

The group Z (2) is often referred to as the second center of G; it is just the pullback to G of
the center in the quotient group G/Z(G). (The center of the quotient need not be trivial.)
Obviously, Z (k) ⊆ Z (k+1) at every step, and if equality holds at the kth step it holds at every
later step. We note without proof the following characterization of nilpotent groups in terms
of the ascending central series.
 42

6.4.13 Theorem. A group G is nilpotent if and only if we have Z (k) = G for some k = 1, 2, . . ..

Nilpotent groups are particularly amenable to study via inductive arguments. Indeed, 6.4.11
and 6.4.13 provide us with two inductive strategies:

1. Run up the ascending central series (e) ⊆ Z(G) ⊆ . . . hoping to prove some
result by examining the abelian group Z(G) and the smaller nilpotent group
G/Z(G).
2. Examine the descending derived series, G ⊇ [G, G] ⊇ . . . hoping to prove
some result by examining the abelian group G/[G, G] and the smaller nilpo-
tent group [G, G]. In this connection it is worth noting that any intermediate
subgroup G ⊇ H ⊇ [G, G] is automatically nilpotent and normal in G, and
G/H is abelian.

6.4.14 Example. The permutation groups S2, S3, S4 are solvable. For n ≥ 5 the alternating
group An = {σ ∈ Sn : sgn(σ) = +1} is simple and is the only proper normal subgroup in Sn.
Hence Sn is not solvable for n ≥ 5.

Discussion: Assume n ≥ 5. In 5.3.5 – 5.3.7 we indicated why An is the only proper normal
subgroup in Sn, and showed that An is simple. The lower commutator series for Sn terminates
prematurely, with
 Sn ⊇ D1(Sn) = [Sn, Sn] = An = D2(Sn) = D3(Sn) = . . .

so Sn is not solvable. In fact, since the signature map sgn : Sn → {±1} is a homomorphism
we get sgn(xyx
−1y−1) = sgn(x)sgn(y)sgn(x)
−1sgn(y)
−1 = 1 for every commutator of elements
in Sn. Thus [Sn, Sn] ⊆ An. But Sn is not abelian, so the the commutator subgroup [Sn, Sn]
is nontrivial and normal in Sn, and hence in An. Thus it is either all of An and D1(Sn) =
[Sn, Sn] = An as shown above. At the next step in the commutator sequence, An is nonabelian
so D2(Sn) = [An, An] is nontrivial, and it is a normal subgroup in An. As such, it must equal
An. From here on the commutator sequence repeats.
For n = 2, 3, 4 we know that S2 ∼= Z2 is abelian, hence solvable. In Example 5.4.1 we
showed that S3/A3 ∼= Z2 and that A3 ∼= Z3, so S3 is solvable by 6.4.10. In 5.4.4 we showed
that S4 contains the abelian Klein Viergroup V4 ∼= Z2 × Z2 as a normal subgroup, and that
S4/A4 ∼= Z2, A4/V4 ∼= Z3. Applying 6.4.10 again we conclude that S4 is solvable. □

One goal of group theory has been to classify the ﬁnite simple groups up to isomorphism.
Nilpotent and solvable groups are generally far from simple, owing to the presence of various
series of normal subgroups. It is easy to see that the only simple solvable groups are abelian,
and they are the cyclic groups (Zp, +) where p > 1 is a prime. Here we can only mention a
remarkable theorem proved in the 1970’s that opened the way for the successful classiﬁcation
of all ﬁnite simple groups in the 1980’s.

6.4.15 Theorem. If G is a ﬁnite group of odd order, then G is solvable. Hence all nonabelian
ﬁnite simple groups have order divisible by 2.

The proof ran some 250 pages and occupied an entire issue of Paciﬁc Journal of Mathematics.
Note that the only abelian simple groups are (Zp, +) for primes p > 1; these have odd order p,
except for p = 2.
The structure of non-simple groups can be quite complicated, even though they are in some
sense assembled by combining simple groups. Nevertheless, certain structural features can be
identiﬁed by recalling that the product set N = N1N2 formed from two normal subgroups is
again a normal subgroup. First notice that if both groups are solvable, so is the product. In fact,
by the Second Isomorphism Theorem for quotients 3.3.14 we have a sequence of homomorphisms

e −→ N1 id
−→ N π
−→ N/N1 ∼= N2/N1 ∩ N2 −→ e

43

and the middle group is solvable if the end groups are (Lemma 6.4.9). Thus a group G always
contains a unique largest solvable normal subgroup R, which is sometimes referred to as the
solvable radical of G. The quotient G/R contains no normal solvable subgroups at all,
although there will certainly be non-normal abelian and solvable subgroups in it, for instance
cyclic subgroups.

6.4.16 Exercise. For any n ≥ 3 determine the center Z(G) of the dihedral group G = Dn.
Hint: The answer will depend on whether n is even or odd. □

6.4.17 Exercise. Compute the commutator subgroup [G, G] for the dihedral group G =
Dn, n ≥ 3. Is Dn nilpotent for any n? Solvable? □

6.4.18 Exercise. In the cases where the center of Dn is nontirival, does the extension

e → Z(Dn) → Dn → Dn/Z(Dn) → e

split – i.e. is Dn a semidirect product with its center as the normal subgroup? □

6.4.19 Exercise. Compute the commutator subgroup [G, G] of the quaternion group G = Q8
of Example 6.3.10. Is Q8 nilpotent? Solvable? □

44
