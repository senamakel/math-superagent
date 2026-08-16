<!-- source: https://arxiv.org/pdf/2405.06220 | converted from PDF -->

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC
INTEGER OMITTING A DIGIT

JIUZHOU ZHAO AND RUOFAN LI
∗

Abstract. Let α, β be two relatively prime algebraic integers in a number field K
and N be a positive integer. We show that the number of n ∈ {1, 2, . . . , N } such
that the β-adic expansion of αn omits a given digit is less than C1N σ(β), where
σ(β) := log(|N (β)|−1)
log |N (β)| and C1 is a constant depending only on β, if all prime ideal
factors of β are unramified and their norms are integer primes.

1. Introduction

Consider the ternary expansion

(2n)3 := akn . . . a1a0,

where aj ∈ {0, 1, 2}, 0 ≤ j ≤ kn satisfies 2
n = ∑kn
j=0 aj3
j. It is an interesting
phenomenon that (20)3 = 1, (2
2)3 = 11 and (28)3 = 100111 omit the digit 2. No other
value of n such that (2n)3 omits the digit 2 is known. Indeed, Erd˝os [4] proposed the
following conjecture, which is still open.

Conjecture 1.1. The ternary expansion of 2
n can not omit the digit 2 for all n ≥ 9.

This conjecture is related to the persistence problem (see [1, 2]) which concerns
base b expansion of natural numbers. Given an integer b > 1 and a natural number
n = ∑k
j=1 djbk−j with dj ∈ {0, 1, . . . , b − 1}, define the Sloane map Sb : N → N
by Sb(n) := ∏k
j=1 dj. By [2, Proposition 1.1], Sb(n) < n for all n ≥ b. Thus, the
orbit under the Sloane map Sm
b (n), m ≥ 1 always stabilizes after a finite number of
steps, that is, there exists a minimal number lb(n) such that Sj
b (n) = Slb(n)
b (n) for all
j ≥ lb(n). When b = 2, it is trivial to see that lb(n) = 1 for all n, the persistence
problem asks whether a uniform bound of lb(n) exists in general.

Problem 1.2 (Persistence problem). For a given b > 2, is there a positive number
B(b) such that lb(n) ≤ B(b) for all n?

In the case of base b = 3, the only nonzero values assumed by the Sloane map are
powers of 2. Hence, in order to answer the persistence problem for base 3, it suffices
to establish the following weaker form of Conjecture 1.1.

2020 Mathematics Subject Classification. Primary 11A63; Secondary 11R04.
Key words and phrases. Radix representation, digital problems, p-adic interpolation.
∗Corresponding author. 1arXiv:2405.06220v2  [math.NT]  4 Dec 2025
2 JIUZHOU ZHAO AND RUOFAN LI
∗

Conjecture 1.3. There is a positive integer k0 such that for all k ≥ k0, the ternary
expansion of 2
k can not omit the digit 0.

Another problem related to Conjecture 1.1 is determining practical binomial coef-
ficients (see [17, 21]). A positive integer n is called practical if all positive integers
less than n can be written as a sum of distinct divisors of n. Leonetti and Sanna
[17] remarked that, likely, there are only finitely many positive integers n such that(
2n
n ) is not a practical number. They proved that if n is a power of 2 whose ternary
expansion omits the digit 2, then (2n
n ) is not a practical number [17, Proposition 2.1].

Progress towards Conjecture 1.1 has been in the form of upper bounds on

M(N ) := #
{1 ≤ n ≤ N : (2
n)3 omits the digit 2
},

where the symbol # denote cardinality. The best known bound on M(N ) is due to
Narkiewicz [19] who proved that

(1.1) M(N ) ≤ 1.62N σ, where σ := log3 2 ≈ 0.63092.

We refer the reader to [3, 7, 14, 16] for more results related to Narkiewicz’s result.

In this paper, we are going to generalize Narkiewicz’s result (1.1) by describing the
above phenomena in general algebraic number fields. Let K be a number field with
ring of integers OK. Fix an element β ∈ OK with norm |N (β)| > 1.

Definition 1.4. We call (β, {0, 1, . . . , |N (β)|−1}) a canonical number system (CNS)
in OK, if every α ∈ OK can be represented uniquely as

(1.2) α = a0 + a1β + · · · + amβm, aj ∈ {0, 1, . . . , |N (β)| − 1} (j = 0, 1, . . . , m),

which is called the radix expansion of α in base β. For convenience, denote

(1.3) (α)β := am . . . a1a0, and (α)β,j := aj (j = 0, 1, . . . , m).

For b ∈ {0, 1, . . . , |N (β)| − 1}, denote

(1.4) Mb(α, β, N ) := #
{1 ≤ n ≤ N : (αn)β,j ̸= b for all possible j},

For the rest of this article, we assume α is not a root of unity as otherwise αn only
have finitely many different value as n changes. Recall that α, β ∈ OK are relatively
prime if the prime ideal decomposition

(1.5) (β) = p
e1
1 · · · p
eh
h
satisfies that pj ∤ α (i.e. α /∈ pj) for all j = 1, 2, . . . , h. Our first result is an upper
bound of Mb(α, β, N ) (similar to (1.1)).

Theorem 1.5. Suppose (β, {0, 1, . . . , |N (β)| − 1}) is a CNS, β is not divided by
ramified primes and α is relatively prime to β, then

(1.6) Mb(α, β, N ) ≤ C1N σ(β)

holds for any digit b ∈ {1, . . . , |N (β)| − 1}, where σ(β) := log(|N (β)|−1)
log |N (β)| and C1 is a
constant depending only on β.

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC INTEGER OMITTING A DIGIT 3

Taking OK = Z, α = 2 and β = 3, Theorem 1.5 leads to (1.1) up to a constant
multiple.
K´atai and Szab´o [11] determined all the CNS for Gaussian integers. And the
question of determining all CNS in quadratic number fields has been answered by
[9, 10]. However, in extensions of higher degree, there is not necessarily a CNS. We
say OK is monogenic if there exists γ ∈ OK, such that {1, γ, . . . , γd−1} is an integer
basis in OK. It is clear from the definition that if (β, {0, 1, . . . , |N (β)| − 1}) is a CNS
in OK, then OK = Z[β], hence OK must be monogenic. Although OK = Z[β] does
not implies (β, {0, 1, . . . , |N (β)| − 1}) is a CNS in OK in general, we do have the
following criterion to determine whether the ring of integers has a CNS.

Theorem 1.6 (Kov´acs [15]). Let K be a finite extension of Q with ring of integers
OK and [K : Q] = d ≥ 3. There exists a CNS (β, {0, 1, . . . , |N (β)| − 1}) in OK if
and only if OK is monogenic.

However, for number fields with degree at least 3, their rings of integers are unlikely
to be monogenic, see [8, 18, 22] for some recent results on monogeneity of number
fields. In order to study those non-monogenic number fields, we introduce the concept
of β-adic expansion which is a natural generalization of p-adic expansion.

Definition 1.7. Given a number field K and its ring of integers OK. Fix β ∈ OK with
norm |N (β)| > 1 and a set of representatives Dβ of the quotient group OK/βOK. For
every α ∈ OK, the β-adic expansion of α (with respect to Dβ) is the unique sequence
(ai)i∈N ∈ DN
β such that

(1.7) α = lim
i→∞ a0 + · · · + aiβi

with respect to p-adic topology for any prime ideal p in OK dividing β.

For instance, when β = 2 and Dβ = {0, 3}, the 2-adic expansion of 1 respect to
{0, 3} is 1 = 3 + 3 · 21 + 3 · 2
3 + 3 · 2
5 + · · · .

It is not hard to see that the sequence (ai)i∈N is always ultimately periodic.
We note that some other generalizations of p-adic expansion exist in the literature.
K´atai [12] considered number systems in rings of integers, involving sets of represen-
tatives and Peth¨o [13] introduced number systems based on polynomials g(t) ∈ Z[t].
When Dβ is clear, denote

(1.8) (α)β := (ai)i∈N, (α)β,j := aj (j = 0, 1, . . . ).

and for b ∈ Dβ let

(1.9) Mb(α, β, N ) := #{1 ≤ n ≤ N : (αn)β,j ̸= b for all possible j}.

We will see in Section 2 that β-adic expansion is well-defined and closely related
to the radix expansion in base β, so the abuse of notations here should not cause
confusion.

4 JIUZHOU ZHAO AND RUOFAN LI
∗

An upper bound of this Mb(α, β, N ) is also obtained.

Theorem 1.8. Let (β) = pe1
1 · · · p
eh
h satisfy that pi is unramified and N (pi) = qi for
all i, where qi is the integer prime lying below pi. If α is relatively prime to β, then

(1.10) Mb(α, β, N ) ≤ C1N σ(β)

for any digit b ∈ Dβ, where σ(β) := log(|N (β)|−1)
log |N (β)| and C1 is a constant depending only
on β.

As a special case of Theorem 1.8, we obtain the following generalization of Narkiewicz’s
result for coprime rational integers p and q.

Corollary 1.9. Let p, q be two coprime rational integers and b ∈ {0, 1, . . . , q − 1}.
Then Mb(p, q, N ) ≤ CN log(q−1)/ log(q)

for some constant C that can be effectively computed.

2. β-adic expansion

We begin with reviewing basic facts on algebraic number fields and p-adic topology.
Fix a number field K and let p be a prime ideal of OK, we define the p-adic valuation
and p-adic absolute value on the field K.

Definition 2.1. The p-adic valuation vp on K \ {0} is defined as follows:

(1) For each integer a ∈ OK \ {0}, let vp(a) be the unique non-negative integer
satisfying (a) = p
vp(a)b with p ∤ b.
(2) For x = a/b ∈ K \ {0} with a, b ∈ OK, let vp(x) := vp(a) − vp(b).

Remark 2.2. (i) It is often convenient to set vp(0) = +∞.
(ii) Note that the valuation vp on K \ {0} is well-defined: if a/b = a′/b
′ for nonzero
a, b, a′, and b
′ in OK, then vp(a) − vp(b) = vp(a
′) − vp(b
′).
(iii) One can check that for all x, y ∈ K, vp(xy) = vp(x) + vp(y) and

vp(x + y) ≥ min{vp(x), vp(y)}.

A prime ideal p is called ramified, if the unique integer prime q ∈ p satisfies that
vp(q) > 1. There are only finitely many ramified primes in OK.

Definition 2.3. The p-adic absolute value | · |p on the field K is defined as follows:
fix a constant c ∈ (0, 1), set |α|p = c
vp(α) for α ∈ K \ {0}, and |0|p = 0. The p-adic
topology on K is the topology induced by | · |p.

For any β ∈ K, let β1, . . . , βs be the roots of the minimal polynomial of β, then
the norm of β is N (β) := ( ∏s
i=1 βi)[K:Q(β)]. For an ideal a ⊆ OK, define its norm by
N (a) := #(OK/a). For principal ideals, we have N (βOK) = |N (β)|; see [6, Theorem
76]. In Theorem 1.8, we consider prime ideals pi whose norms are integer primes, this
means they all have inertial degree 1.

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC INTEGER OMITTING A DIGIT 5

Definition 2.4. Let G be an abelian group and H ⊆ G be a subgroup. We say that
a subset S ⊆ G is a set of representatives of the quotient group G/H if the map
S → G/H : x ↦→ x + H is a bijection.

Remark 2.5. A set of representatives is usually not unique. In this article, we only
consider the case that G/H is finite, so there always exists a set of representatives.
In general, if one assumes the axiom of choice, then every quotient group have sets
of representatives.

From now on, let Dβ denotes a set of representatives of OK/βOK, then there is a
natural bijection from Di
β to OK/βiOK.

Lemma 2.6. For any i ≥ 1, the map

Di
β → OK/βiOK

(a0, a1, . . . , ai−1) ↦→ a0 + a1β + · · · + ai−1βi−1 + βiOK

is a bijection.

Proof. When i = 1, the statement holds since Dβ is a set of representatives of
OK/βOK. Assume the statement is valid for i and we are going to prove it for
i + 1. Note that #(Di+1
β ) = |N (β)|i+1 = |N (βi+1)| = #(
OK/βi+1OK), so it suffice to
prove that the map is injective.

Suppose (a0, . . . , ai) and (b0, . . . , bi) have the same image under the map, that is,
∑i
j=0 ajβj + βi+1OK = ∑i
j=0 bjβj + βi+1OK. Then

i−1∑

j=0 (aj − bj)βj + (ai − bi)βi ∈ βi+1OK,

so ∑i−1
j=0(aj − bj)βj ∈ βiOK. By the induction hypothesis, we have (a0, . . . , ai−1) =
(b0, . . . , bi−1). Therefore, we obtain aiβi − biβi ∈ βi+1OK, hence ai − bi ∈ βOK. Since
ai, bi ∈ Dβ, their difference can not lie in βOK unless they are the same. □

For each i ≥ 1, we have two natural maps Di+1
β → Di
β and OK/βi+1OK →
OK/βiOK, and it is easy to check that they commute with the map in Lemma 2.6.
Taking inverse limits, we have a bijection

DN
β ←→ OK,β := lim
← OK/βiOK

(ai)i∈N ←→ a0 + a1β + · · · + aiβi + · · ·

Now OK can be viewed as a subring of OK,β via natural embedding, so for every
α ∈ OK, there is a sequence (ai)i∈N ∈ DN
β such that

α − (a0 + a1β + · · · + aiβi) ∈ βi+1OK

6 JIUZHOU ZHAO AND RUOFAN LI
∗

holds for each i ∈ N, and we have

(2.1) α = lim
i→∞ a0 + · · · + aiβi

with respect to p-adic topology for any prime ideal p in OK dividing β. If there exists
another sequence (bi)i∈N ∈ DN
β such that

α = lim
i→∞ b0 + b1β + · · · + biβi

with respect to p-adic topology for some prime ideal p in OK dividing β, then bi-
jectivity implies (ai)i∈N = (bi)i∈N. Therefore we conclude that β-adic expansion is
well-defined.

Next we investigate the relation between β-adic expansion and the radix expansion
of base β. When Dβ = {0, 1, . . . , |N (β)| − 1} and (β, Dβ) is a CNS, for any α ∈
OK, we have α = a0 + a1β + · · · + amβm for some a0, . . . , am ∈ D. Therefore if
Dβ is a set of representatives, then the β-adic expansion of α with respect to is
(a0, . . . , am, 0, 0, 0, . . .).

Lemma 2.7. Let (β) = pe1
1 · · · p
eh
h . If (β, {0, 1, . . . , |N (β)| − 1}) is a CNS in OK,
then |N (pi)| = qi for all i, where qi is the integer prime that lies below pi.

Proof. Assume |N (pi)| > qi for some i. Then

|N (β)| = ∏

1≤i≤h
 ∣
∣
∣N (pi)
∣
∣
∣ei > ∏

1≤i≤h qei
i ,

hence ∏
1≤i≤h qei
i ∈ {0, 1, . . . , |N (β)|−1}. Since pi | qi for all i, we have β | ∏
1≤i≤h qei
i ,
thus the map
 {0, 1, . . . , |N (β)| − 1} → OK/βOK
x ↦→ x + βOK

is not injective. Note that #Dβ = |N (β)| = #(OK/βOK), so the above map is also
not surjective. Therefore we can choose an element α ∈ OK such that α ̸≡ x (mod β)
for any x ∈ Dβ. However, since (β, {0, 1, . . . , |N (β)| − 1}) is a CNS in OK, we have
α = c0 + c1β + · · · + cmβm for some c0, . . . , cm ∈ Dβ, which implies α ≡ c0 (mod β), a
contradiction. □

Lemma 2.8. Let (β) = pe1
1 · · · p
eh
h and Dβ = {0, 1, . . . , |N (β)| − 1}. If (β, Dβ) is
a CNS in OK, and pj is unramified for all j, then Dβ is a set of representatives of
OK/βOK.

Proof. Note that #(OK/βOK) = N (βOK) = |N (β)| = #Dβ, so we only need to
show x − y /∈ βOK for all distinct x, y ∈ Dβ. Assume that β | x − y for some
distinct x, y ∈ Dβ, then pe1
1 · · · p
eh
h | x − y. Since pj is unramified for all j, this implies
qe1
1 · · · qeh
h | x − y. Hence, combined with Lemma 2.7,

|N (β)| = N (p
e1
1 · · · p
eh
h ) = N (p1)
e1 · · · N (ph)
eh = qe1
1 · · · qeh
h | x − y,

a contradiction. □

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC INTEGER OMITTING A DIGIT 7

Corollary 2.9 (=Theorem 1.5). Take Dβ = {0, 1, . . . , |N (β)| − 1}. If (β, Dβ) is a
CNS, β is not divided by ramified primes and α is relatively prime to β, then (1.10)
holds for any digit b ∈ {1, . . . , |N (β)| − 1}.

Proof. Note that if the radix expansion of αn in base β is

αn = a0 + a1β + · · · + amβm, aj ∈ Dβ (j = 0, 1, . . . , m),

then we may add infinitely many zeroes to obtain its β-adic expansion

(a0, a1, . . . , am, 0, 0, . . .).

Therefore this corollary follows from Theorem 1.8, Lemma 2.7 and Lemma 2.8. □

Remark 2.10. When b = 0, if the length of the radix expansion of αn is long enough,
the we may use a similar inequality as (4.6) and follow the proof of Theorem 1.8 to
deduce the desired bound.

3. p-adic interpolation of the sequence (αn)n∈N

Let (β) = p
e1
1 · · · p
eh
h be the prime ideal decomposition of (β) and α ∈ OK be rela-
tively prime to β. Fix a prime ideal p ∈ {p1, . . . , ph}. In order to analyze the β-adic
expansion of αn, we need to introduce a powerful method called p-adic interpolation.

Recall that (K, | · |p) is a valued field and the distance of x, y ∈ K is defined as
|x − y|p. A valued field is said to be complete when every Cauchy sequence has a
limit.

Proposition 3.1 ([20, Chapter 1, (M)]). Every valued field has a completion.

We denote the completion of K with respect to the p-adic absolute value | · |p by
Kp, and denote the extended absolute value again by | · |p. Let

¯B(0, 1) = {x ∈ Kp : |x|p ≤ 1}

denote the closed unit ball of Kp. It is clear that OK ⊂ ¯B(0, 1).

Let (αn)n∈N be a sequence of integers in OK. A p-adic interpolation of the sequence
(αn)n∈N is a continuous function G(x), defined in the unit ball ¯B(0, 1), with G(n) = αn
for all n ∈ N.

Lemma 3.2. If α ∈ OK satisfies that p ∤ α, then there is a rational integer up such
that the sequence (αn)n∈N can be divided into subsequences

(αl(αup)n)n∈N, l = 0, 1, . . . , up − 1,

and for each l, the sequence (αl(αup)
n)n∈N has an analytic p-adic interpolation Gl.

Proof. Define the formal series

log(1 + X) :=
 ∞∑

n=1(−1)
n+1 X n

n

8 JIUZHOU ZHAO AND RUOFAN LI
∗

Recall that for a power series f (X) = ∑∞
n=0 anX n with coefficients in Kp, the radius
of convergence is defined as

(3.1) r = 1/(lim sup
n→+∞ |an|p),

then f (x) converges for every x ∈ Kp with |x|p < r, see [5, Proposition 5.4.1] for
details.
Let an = (−1)n+1/n, we claim that |an|
1/n
p = c
−vp(n)/n → 1 as n → ∞, where c is
the constant fixed in Definition 2.3. To see this, let q be the unique integer prime
lying below p and n = qvq(n)a with q ∤ a, then vq(n) ≤ log n; on the other hand,

(3.2) (n) = (q)vq(n)(a) = (pvp(q)b)
vq(n)(a),

with p ∤ b, thus

(3.3) vp(n) = vp(q)vq(n) ≤ vp(q) log n,

which completes the proof of the claim. Hence, applying (3.1), we can define the
p-adic logarithm of x ∈ B(1, 1) := {x ∈ Kp : |x − 1|p < 1} as

logp(x) = logp(1 + (x − 1)) =
 ∞∑

n=1(−1)
n+1 (x − 1)n

n .

Define the formal series exp(X) := ∑∞
n=0 X n/n!. To calculate the radius of conver-
gence (3.1), let an = 1/(n!). Similar to (3.2) and (3.3), we have

(3.4) vp(n!) = vp(q)vq(n!) < vp(q)n
q − 1 ,

where we use vq(n!) ≤ n/(q − 1) in the last inequality (see [5, Lemma 5.7.4]). Hence,

|1/n!|
1/n
p = c
−vp(n!)/n < c
−vp(q)/(q−1),

this implies that the radius of convergence r ≥ c
vp(q)/(q−1). Therefore, we can define
the p-adic exponential function as

(3.5) expp(x) :=
 ∞∑

n=0
 xn

n! , x ∈ B(0, cvp(q)/(q−1))

Observe that for all x ∈ B(1, c
vp(q)) and N ∈ N,
∣
∣
∣
 N∑

n=1(−1)
n+1 (x − 1)n

n
 ∣
∣
∣p ≤ max
1≤n≤N |x − 1|n
p
|n|p
(3.6)
 = max
1≤n≤N
 (cnvp(x−1)/c
vp(n))

≤ max
1≤n≤N
 (cnvp(x−1)/c
vp(q) log n) ≤ |x − 1|p,

where we use (3.3) in the third step. Hence, for each x ∈ B(1, cvp(q)), we have

(3.7) | logp(x)|p ≤ |x − 1|p.

Thus, by (3.5) and (3.7), logp(x) is in the domain of expp when x ∈ ¯B(1, cvp(q)+1).

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC INTEGER OMITTING A DIGIT 9

Note that OK/p
vp(q)+1 is a finite additive group, the sequence α, α2, . . . , αn, . . .
must satisfy that there exist two integers n, m with 0 ≤ n < m such that

αm + OK/p
vp(q)+1 = αn + OK/p
vp(q)+1,

thus αn(αm−n − 1) ∈ p
vp(q)+1. By the condition p ∤ α, we have αm−n − 1 ∈ p
vp(q)+1.
Therefore, there is an integer up such that |αup − 1|p ≤ c
vp(q)+1.

By (3.7), for |x|p ≤ 1,

(3.8) |x logp(αup)|p = |x|p| logp(αup)|p ≤ 1 · |αup − 1|p ≤ c
vp(q)+1.

Combined with (3.5), we obtain that expp(x logp(αup)) is well-defined on the closed
ball ¯B(0, 1). This expression will serve as the definition of (αup)
x, x ∈ ¯B(0, 1).

Now take Gl(x) = αl(αup)
x, x ∈ ¯B(0, 1), for l ∈ {0, 1, . . . , up − 1}, which is the
analytic p-adic interpolation that we want. □

Corollary 3.3. Let (β) = pe1
1 · · · p
eh
h and α ∈ OK be relatively prime to β. Let upi
(i = 1, 2, . . . , h) be as in Lemma 3.2 and u = ∏h
i=1 upi. Then Gl(x) := αl(αu)
x

is an analytic pi-adic interpolation of (αl(αu)n)n∈N for all i = 1, 2, . . . , h and l =
0, 1, . . . , u − 1.

Proof. Let qi be the unique integer prime lying below pi for i = 1, 2, . . . , h. By the
definition of upi, we have

αupi + OK/p
vpi (qi)+1
i = 1 + OK/p
vpi (qi)+1
i .

Hence, for all i ∈ {1, 2, . . . , h}, αu + OK/p
vpi (qi)+1
i = 1 + OK/p
vpi (qi)+1
i , that is,

(3.9) |αu − 1|pi ≤ c
vpi (qi)+1.

Therefore, exppi(x logpi(αu)) is well-defined for |x|pi ≤ 1 (the discussion is similar to
the one in the proof of Lemma 3.2), and this expression will serve as the definition of
(αu)x, |x|pi ≤ 1. □

Remark 3.4. One can think of Gl(x) = αl(αu)
x as a formal function, which is well-
defined on the closed ball ¯B(0, 1) in Kp for all p ∈ {p1, . . . , ph}.

4. Proof of Theorem 1.8

We begin with a simple lemma.

Lemma 4.1. Let Gl(x) = αl(αu)x and {p1, . . . , ph} be as in Corollary 3.3. Then
there exist integers n0, m0 such that

(4.1) |Gl(x) − Gl(y)|p ≥ c
n0|x − y|p,

for all x, y with |x − y|p ≤ c
m0 and p ∈ {p1, . . . , ph}.

10 JIUZHOU ZHAO AND RUOFAN LI
∗

Proof. Fix a p ∈ {p1, . . . , ph}, we claim that there exist integers np, mp > 0 such that
for every pair of distinct x, y ∈ ¯B(0, 1),

(4.2) if |x − y|p ≤ c
mp, then |Gl(x) − Gl(y)|p ≥ c
np|x − y|p.

Assume that for every n, there is a pair of distinct points xn, yn satisfying

(4.3) |xn − yn|p ≤ 1
n, |Gl(xn) − Gl(yn)|p < 1
n|xn − yn|p.

Since ¯B(0, 1) is compact (similar to [5, Corollary 4.2.7]), (xn)n≥1 has a convergent
subsequence (xnj )j≥1, we assume that xnj → x0. We must have ynj → x0 as well.
Suppose that Gl(z) = ∑∞
n=0 cnzn since Gl is analytic, then

Gl(xnj ) − Gl(ynj )
xnj − ynj =
 ∑∞
n=0 cn(x
n
nj − yn
nj )

xnj − ynj
(4.4)
 =
 ∞∑

n=0 cn(x
n−1
nj + xn−2
nj ynj + · · · + yn−1
nj ) →
 ∞∑

n=0 cnnx
n−1
0 = G
′
l(x0),

as j → +∞. But, by (4.3), ∣
∣
∣Gl(xn) − Gl(yn)
xn − yn
 ∣
∣
∣p < 1
n,

combined with (4.4), we have G
′
l(x0) = 0. However, this is impossible, one can check
that:
 G
′
l(x) = αl( ∞∑

n=0
 (x logp(αu)
)n

n!
 )′

= αl ∞∑

n=1
 ( logp(αu)
)nxn−1

(n − 1)!

= (αl logp(αu))
(αu)x ̸= 0,(4.5)

for all x ∈ ¯B(0, 1). This completes the proof of the claim.

Let m0 = max {mp : p ∈ {p1, . . . , ph}
} and n0 = max {
np : p ∈ {p1, . . . , ph}
}. This
completes the proof of the lemma. □

Fix a digit b ∈ Dβ, for a word (aj)k−1
j=0 ∈ (Dβ \ {b})k, denote
[
(aj)
k−1
j=0 ](l) := {
0 ≤ n ≤ |N (β)|
k − 1 : (αl(αu)
n)
β,j = aj for j = 0, . . . , k − 1},

where u is as in Corollary 3.3, l = 0, 1, . . . , u − 1 and the definition of (·)β,j is as in
(1.8). By the definition of Mb(
α, β, u|N (β)|
k) (see (1.9)), we have

Mb(α, β, u|N (β)|
k) ≤#
{1 ≤ n ≤ u|N (β)|
k : (αn)β,j ̸= b for j = 0, . . . , k − 1}

≤
 u∑

l=1
 ∑

(ai)
k−1
i=0 ∈(
Dβ \{b}
)k #
[
(aj)
k−1
j=0 ](l).(4.6)

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC INTEGER OMITTING A DIGIT11

We are now going to estimate #
[
(aj)
k−1
j=0 ](l). Let qj be the unique integer prime
lying below pj for j = 1, 2, . . . , h. By the condition N (pj) = qj, we have

(4.7) |N (β)| =
 h∏

j=1 N (pj)ej =
 h∏

j=1 qej
j .

Consider the partition

(4.8) [
(aj)k−1
j=0 ](l) =
 |N (β)|m0 −1⋃

i=0
 [
(aj)k−1
j=0 ](l)
i

where [(aj)
k−1
j=0 ](l)
i := {
0 ≤ n ≤ |N (β)|
k − 1 : n ∈ [(aj)
k−1
j=0 ](l)

and n ≡ i (mod |N (β)|m0)}
,

and m0 is defined as in Lemma 4.1. Suppose that n, m are in [(aj)
k−1
j=0 ](l)
i , then

αl(αu)
n + βkOK =
 k−1∑

i=0 aiβi + βkOK = αl(αu)
m + βkOK,

that is, βk | (αl(αu)
n − αl(αu)m). Recall that (β) = p
e1
1 · · · p
eh
h , we have

(4.9) ∣
∣
∣αl(αu)
n − αl(αu)
m∣
∣
∣pj ≤ c
kej ,

for all j ∈ {0, 1, . . . , h}. Moreover, n, m ∈ [(aj)
k−1
j=0 ](l)
i also implies that

n ≡ m (mod |N (β)|
m0),

that is, |N (β)|m0 | n − m. Combined this with (4.7), we have

|n − m|pj ≤ c
m0,

for all j ∈ {0, 1, . . . , h}. Hence, by Lemma 4.1 and (4.1), we have

|n − m|pj ≤ c
−n0ckej ,

for all j ∈ {0, 1, . . . , h}. This implies that ∏h
j=1 p
kej −n0
j |(n − m). Recall the condition
that pj is unramified for all j, this implies that

h∏

j=1 qkej −n0
j | (n − m),

where qi is the integer prime that lies in pi. Hence, the distance

|n − m| ≥
 h∏

j=1 qkej −n0
j ,

12 JIUZHOU ZHAO AND RUOFAN LI
∗

which holds for each pair of distinct n, m ∈ [
(aj)k−1
j=0 ](l)
i . Therefore,

(4.10) #
[
(aj)k−1
j=0 ](l)
i ≤ |N (β)|
k/
( h∏

j=1 qkej −n0
j ).

On the other hand, by (4.7),

(4.11) |N (β)|k =
 h∏

j=1 qkej
j .

Applying (4.11) to (4.10), we have

(4.12) #
[
(aj)
k−1
j=0 ](l)
i ≤ ̃C0,

where ̃C0 := ( ∏h
j=1 qj)n0. Applying (4.12), (4.8) to (4.6), we obtain

(4.13) Mb(
α, β, u|N (β)|
k) ≤ C0 · ∣
∣N (β)
∣
∣kσ(β)

where σ(β) := log(|N (β)|−1)
log |N (β)| and C0 := u|N (β)|
m0 ̃C0. For an integer N ∈ N, there is an
integer k ∈ N such that |N (β)|
k−1 ≤ N ≤ |N (β)|
k; then, by (4.13), we have

Mb(α, β, N ) ≤ Mb(α, β, u|N (β)|
k) ≤ C1N σ(β),

where C1 := C0|N (β)|
σ(β). This completes the proof.

Acknowledgements

We thank Wladyslaw Narkiewicz for pointing out errors in the previous version of
this article. We thank the referee for helpful suggestions. This work was supported
in part by NSFC No. 12471085, Science and Technology Commission of Shanghai
Municipality (STCSM) No. 22DZ2229014, NSFC No. 12401006, and Guangdong
Basic and Applied Basic Research Foundation No. 2023A1515110272.

Declaration of interests

There are no relevant financial or non-financial competing interests to report.

References

[1] G. Bonuccelli, L. Colucci, and E. de Faria. On the Erd¨os-Sloane and shifted Sloane persistence
problems. J. Integer Seq., 23(10):Art. 20.10.7, 30, 2020. 1
[2] E. de Faria and C. Tresser. On Sloane’s persistence problem. Exp. Math., 23(4):363–382, 2014.
1
[3] T. Dupuy and D. E. Weirich. Bits of 3n in binary, Wieferich primes and a conjecture of Erd¨os.
J. Number Theory, 158:268–280, 2016. 2
[4] P. Erd˝os. Some unconventional problems in number theory. Number 61, pages 73–82. 1979.
Luminy Conference on Arithmetic. 1
[5] F. Q. Gouvˆea. p-adic numbers. Universitext. Springer, Cham, third edition, [2020] ©2020. 8,
10

ON β-ADIC EXPANSIONS OF POWERS OF AN ALGEBRAIC INTEGER OMITTING A DIGIT13

[6] E. Hecke. Lectures on the theory of algebraic numbers, volume 77 of Graduate Texts in Math-
ematics. Springer-Verlag, New York-Berlin, 1981. Translated from the German by George U.
Brauer, Jay R. Goldman and R. Kotzen. 4
[7] S. T. Holdum, F. R. Klausen, and P. M. Reichstein Rasmussen. Powers in prime bases and a
problem on central binomial coefficients. Integers, 15:Paper No. A43, 13, 2015. 2
[8] B. Jhorar, and S. K. Khanduja. On the index theorem of Ore. Manuscripta Math., 153(1-2):299–
313, 2017. 3
[9] I. K´atai and B. Kov´acs. Kanonische Zahlensysteme in der Theorie der quadratischen algebrais-
chen Zahlen. Acta Sci. Math. (Szeged), 42(1-2):99–107, 1980. 3
[10] I. K´atai and B. Kov´acs. Canonical number systems in imaginary quadratic fields. Acta Math.
Acad. Sci. Hungar., 37(1-3):159–164, 1981. 3
[11] I. K´atai and J. Szab´o. Canonical number systems for complex integers. Acta Sci. Math. (Szeged),
37(3-4):255–260, 1975. 3
[12] I. K´atai. Construction of number systems in algebraic number fields. Ann. Univ. Sci. Budapest.
Sect. Comput., 18(3-4):103–107, 1999. 3
[13] A. Peth¨o. On a polynomial transformation and its application to the construction of a public
key cryptosystem. Computational number theory (Debrecen), 31–43, 1989. 3
[14] R. E. Kennedy and C. Cooper. A generalization of a result by Narkiewicz concerning large
digits of powers. Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat., 11:36–40, 2000. 2
[15] B. Kov´acs. Canonical number systems in algebraic number fields. Acta Math. Acad. Sci. Hun-
gar., 37(4):405–407, 1981. 3
[16] J. C. Lagarias. Ternary expansions of powers of 2. J. Lond. Math. Soc. (2), 79(3):562–588, 2009.
2
[17] P. Leonetti and C. Sanna. Practical numbers among the binomial coefficients. J. Number Theory,
207:145–155, 2020. 2
[18] R. Li. On number fields towers defined by iteration of polynomials. Arch. Math. (Basel),
119(4):371–379, 2022. 3
[19] W. Narkiewicz. A note on a paper of H. Gupta concerning powers of two and three: “Powers of
2 and sums of distinct powers of 3” [Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. No.
602-633 (1978), 151–158 (1979); MR 81g:10016]. Univ. Beograd. Publ. Elektrotehn. Fak. Ser.
Mat. Fiz., (678-715):173–174, 1980. 2
[20] P. Ribenboim. The theory of classical valuations. Springer Monographs in Mathematics.
Springer-Verlag, New York, 1999. 7
[21] C. Sanna. Practical central binomial coefficients. Quaest. Math., 44(9):1141–1144, 2021. 2
[22] H. Smith. The monogeneity of radical extensions. Acta Arith., 198(3):313–327, 2021. 3

School of Mathematical Sciences, Key Laboratory of MEA(Ministry of Educa-
tion) & Shanghai Key Laboratory of PMMP, East China Normal University, Shang-
hai, 200241, China

Email address: zhao9zone@gmail.com

Department of Mathematics, Jinan University, Guangzhou, 510632, China

Email address: liruofan@jnu.edu.cn
