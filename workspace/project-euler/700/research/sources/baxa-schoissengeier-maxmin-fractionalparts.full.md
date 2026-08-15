<!-- source: https://bibliotekanauki.pl/articles/1391571.pdf | converted from PDF -->

ACTA ARITHMETICA
LXVIII.3 (1994)

Minimum and maximum order of magnitude
of the discrepancy of (nα)

by

C. Baxa and J. Schoissengeier (Wien)

Dedicated to Prof. Wolfgang Schmidt
on the occasion of his sixtieth birthday

It is a classical result of P. Bohl [5], W. Sierpiński [21, 22] and H. Weyl
[25, 26] that the sequence (nα)n≥1 is uniformly distributed modulo 1 if and
only if α is irrational. The discrepancies

D∗
N (α) = sup
0≤x≤1
 ∣
∣
∣
 N∑

n=1 c[0,x)({nα}) − N x∣
∣
∣

and
 DN (α) = sup
0≤x<y≤1
 ∣
∣
∣
 N∑

n=1 c[x,y)({nα}) − N (y − x)∣
∣
∣

measure the deviation of this sequence from an ideal distribution. (Here
N ∈ N, cM is the characteristic function of the set M and {x} = x − [x]
denotes the fractional part of x.) The speed of convergence in the limit
relations
 lim
N →∞ 1
N D∗
N (α) = 0 and lim
N →∞ 1
N DN (α) = 0

is used as a measure for the quality of distribution and was studied by many
authors. Initially the problem was tackled by H. Behnke [3, 4], A. Ostrowski
[14], G. H. Hardy and J. E. Littlewood [10], and E. Hecke [11]. More re-
cently, it was taken up by H. Niederreiter [13], J. Lesca [12], V. T. S´os [23,
24], Y. Dupain [7, 8], Y. Dupain and V. T. S´os [9], L. Ramshaw [15] and
J. Schoißengeier [17, 18, 20].

Research was supported by the Austrian Science Foundation (FWF) under grant
P8703–PHY.
 [281]

282 C. Baxa and J. Schoißengeier

In [17] it was proved that lim inf N →∞ D∗
N (α) = 1 for all irrational α. To
determine the maximum order of D∗
N (α), the quantities

ω+
N (α) = sup
0≤x≤1
 ( N∑

n=1 c[0,x)({nα}) − N x)

and
 ω−
N (α) = sup
0≤x≤1
 (
N x −
 N∑

n=1 c[0,x)({nα}))

were introduced by J. Schoißengeier [20] who determined

max
1≤N <qm+1 ω+
N (α) and max
1≤N <qm+1 ω−
N (α)

up to an absolute error in terms of the continued fraction expansion of α.
Utilizing D∗
N (α) = max(ω+
N (α), ω−
N (α)) one arrives at the maximum order
of D∗
N (α).
It is the purpose of this paper to prove analogous results for the minimum
and maximum order of DN (α). We calculate max1≤N <qm+1 DN (α) in terms
of the continued fraction expansion of α up to an absolute error (where
qm denotes the denominator of the mth convergent of α). Using this we
describe the maximum order of the sequence (DN (α))N ≥1 and calculate
lim supN →∞ DN (α)/ log N for all α for which DN (α) = O(log N ) is satisﬁed.
Finally, we determine the minimum order of (DN (α))N ≥1 which turns out
to be closely connected to the Lagrange spectrum.

1. The maximum order. We will use the following notations: α will
always denote an irrational real number with regular continued fraction
expansion α = [a0, a1, a2, . . .] (a0 ∈ Z and a1, a2, . . . ∈ N) and convergents
(pm/qm)m≥0. For all i, j ≥ 0 let

sij = qmin(i,j)(qmax(i,j)α − pmax(i,j))

and
 εi = 1
2 (1 − (−1)
ai+1) ∏

0≤j≤i
j≡i (mod 2)
 (−1)
aj+1 .

We are now prepared to state our ﬁrst main result.

Theorem 1.1. For m ≥ 0 let Nm = 1
2 ∑m
i=0(ai+1 + (−1)mεi)qi. Then as
m → ∞,

4 max
1≤N <qm+1 DN (α) =
 m∑

i=0 ai+1 − ∑

0≤i≤m
 ∑

0≤j≤m
j≡i (mod 2)
 εiεj|sij| + O(1)

Discrepancy of (nα) 283

and
 max
1≤N <qm+1 DN (α) = { DNm(α) + O(1) if Nm < qm+1,
DNm−1(α) + O(1) otherwise.
The implicit constants are absolute.

P r o o f. We introduce

Sm = 1
4
 m∑

i=0 ai+1 − 1
4
 ∑

0≤i≤m
 ∑

0≤j≤m
j≡i (mod 2)
 εiεj|sij|

as a convenient shorthand notation.
Employing c[0,{x−y})({x}) − {x − y} = {y} − {x} for all x, y ∈ R we have
for 0 ≤ k, l ≤ N < qm+1,

(∗) ∆N (k, l)

:=
 N∑

n=1 c[0,{kα})({nα}) − N {kα} −
 N∑

n=1 c[0,{lα})({nα}) + N {lα}

=
 N∑

n=1({(n − k)α} − {nα}) −
 N∑

n=1
({(n − l)α} − {nα})

=
 k−1∑

n=1{−nα} +
 N −k∑

n=1 {nα} −
 l−1∑

n=1{−nα} −
 N −l∑

n=1{nα}

= k − 1 −
 k−1∑

n=1
{nα} − (l − 1) +
 l−1∑

n=1
{nα} +
 N −k∑

n=1 {nα} −
 N −l∑

n=1{nα}

=
 l−1∑

n=1({nα}−1/2)+
N −k∑

n=1 ({nα}−1/2)−
k−1∑

n=1({nα}−1/2)−
N −l∑

n=1({nα}−1/2)

≤ 2 max
1≤M <qm+1
 M∑

n=1 B1(nα) − 2 min
1≤M <qm+1
 M∑

n=1 B1(nα) = Sm + O(1).

Here B1(x) = {x}−1/2 denotes the ﬁrst Bernoulli polynomial. The last step
made use of Corollary 2 in §2 of [19]. Using DN (α) = 1+max1≤k,l≤N ∆N (k, l)
we get max1≤N <qm+1 DN (α) ≤ Sm + c with an absolute constant c > 0. To
obtain equality we set

k := 1 + 1
2
 ∑

0≤i≤m
i≡0 (mod 2)
 (ai+1 + (−1)mεi)qi,

l := 1 + 1
2
 ∑

0≤i≤m
i≡1 (mod 2)
 (ai+1 + (−1)mεi)qi

284 C. Baxa and J. Schoißengeier

and ̂Nm := k +l − 1 = Nm +1. Obviously l − 1 = ̂Nm − k and k − 1 = ̂Nm − l.
According to Corollary 2 in §2 of [19] we have equality in (∗). Had we proved
̂Nm < qm+1 we would have completed the proof of the theorem. It is of no
importance that ̂Nm = Nm + 1 as DN +1(α) = DN (α) + O(1) with an
absolute implied constant. A trivial estimation yields

Nm ≤ 1
2
 m∑

i=0 2ai+1qi = qm+1 + qm − 1.

If am+1 ≥ 3 we even have

Nm < (qm + qm−1) + 1
2 (am+1 + 1)qm ≤ qm+1.

Thus, Nm ≥ qm+1 only if am+1 ≤ 2. But in this case we may safely change
to Nm−1 < qm + qm−1 ≤ qm+1 as Sm = Sm−1 + O(am+1) with an absolute
implied constant.
We conclude the proof with a remark: Obviously Nm ≥ qm if am+1 ≥ 2.
If am+1 = am = 1 it is possible that am+1 + (−1)mεm = am + (−1)
m−1εm−1
= 0 but by the deﬁnition of the εi it is impossible to have also am−1 +
(−1)
m−2εm−2 = 0. Therefore Nm ≥ qm−2.

R e m a r k. Using Corollary 1 in §2 of [19] the Bernoulli polynomials
can be replaced by Dedekind sums in the above estimate. This indicates a
close connection between discrepancies and Dedekind sums which was ﬁrst
pointed out and explored by U. Dieter (oral communication).

Corollary 1.2. Let α be an irrational number. For N ∈ N we deﬁne
m ∈ N by the property qm ≤ N < qm+1. Then

lim sup
N →∞ DN (α) ∕ ( m∑

i=0 ai+1 − ∑

0≤i≤m
 ∑

0≤j≤m
j≡i (mod 2)
 εiεj|sij|
) = 1
4 .

P r o o f. This can be proved along the same lines as Corollary 1 in §2
of [20].

R e m a r k. Another proof of Theorem 1.1 which uses a completely dif-
ferent method is to be found in [1]. It yields more precise information on
where the maximum is attained at the cost of a much longer proof.

2. The maximum order for numbers of bounded density. By
a well known theorem of W. M. Schmidt [16] for every α an inﬁnity of
positive integers N such that DN (α) ≥ (66 log 4)−1 log N exist. On the other
hand, it was ﬁrst observed by H. Behnke [4] that DN (α) = O(log N ) if and
only if α = [a0, a1, a2, . . .] is of bounded density (i.e. ∑m
i=0 ai+1 = O(m) as

Discrepancy of (nα) 285

m → ∞). For these numbers we are now able to compute the inﬁmum of all
possible implied constants in the estimate DN (α) = O(log N ).

Theorem 2.1. Let α be a number of bounded density. Then

ν(α) := lim sup
N →∞
 DN (α)
log N

= 1
4 lim sup
m→∞ 1
log qm
 ( m∑

i=0 ai+1 − ∑

0≤i≤m
 ∑

0≤j≤m
j≡i (mod 2)
 εiεj|sij|)
.

P r o o f. This may be proved as Theorem 1 in §3 of [20].

Theorem 2.1 implies a property of the function ν which was ﬁrst shown
by L. Ramshaw [15]:

Corollary 2.2. Let α, β be two numbers of bounded density. Assume
that there exists a matrix (a b
c d) ∈ GL2(Z) such that β = (aα + b)/(cα + d).
Then ν(β) = ν(α).

P r o o f. This follows immediately from Theorem 2.1 and various parts
of the proof of Theorem 2 in §3 of [20].

R e m a r k. The analogous map ν∗(α) = lim supN →∞ D∗
N (α)/ log N is
studied in [1, 2]. The image of ν∗ has the property ν∗(B) = [ν∗(
√2), ∞).
(Here B denotes the set of all numbers of bounded density.) In the present
case we are able to prove [ν(
√2), ∞) ⊆ ν(B) but ν((1 + √5)/2) < ν(
√2).

In the case of quadratic irrationalities there is a formula which does not
contain any limit processes:

Theorem 2.3. Let α = [0, a1, . . . , ae] where 2 | e and set

ηt = ∏

0≤σ<e
σ≡t (mod 2)

(−1)aσ+1 for t ∈ {0, 1}.

Then

ν(α) = 1
4 log(qe + αqe−1)
 (e−1∑

i=0 ai+1

+
 1∑

t=0(2t − 1) qe−1
2ηt − qe − pe−1 N ( ∑

0≤i<e
i≡t (mod 2)
 εi(qiα − pi)
)

+
 1∑

t=0(2t − 1) ∑

0≤i<e
i≡t (mod 2)
 ∑

0≤j<e
j≡t (mod 2)
 εiεjqipj sgn (i − j)
)
,

where N denotes the norm of the quadratic ﬁeld Q(α).

286 C. Baxa and J. Schoißengeier

P r o o f. Here the same applies as to Theorem 1 of §4 in [20].

N o t e. In view of Corollary 2.2 the assumption on the shape of the con-
tinued fraction expansion of α does not exclude any quadratic irrationalities.
Note also that the period e is not assumed to be of minimal length.
We ﬁnish the section with two special cases of Theorem 2.3.

Corollary 2.4. Let α = [0, a, b] with a, b ∈ N. Then

ν(α) = 1
4 log(1 + b/α)
 (
a+b− 1
2 · 1 − (−1)
a

ab + 2(1 − (−1)a) − 1
2 · 1 − (−1)
b

ab + 2(1 − (−1)b)
 )
.

Corollary 2.5. Let α = [0, a] with a ∈ N. Then

ν(α) = a
4 log(1/α)
 (
1 − 1
2 · 1 − (−1)a

a2 + 4
 )
.

R e m a r k. Corollary 2.5 was ﬁrst proved by L. Ramshaw [15].

3. The maximum order for special Hurwitz continued fractions

Theorem 3.1. Let t ∈ N and αt = coth(1/t) = [t, 3t, 5t, . . .]. Then as
m → ∞,
max
1≤N <qm+1 DN (αt) = 1
4 tm
2 + tm + 1
16t ((−1)
t − 1) log m + O(1).

P r o o f. The proof runs analogously to that of Theorem 1 in §5 of [20].

Theorem 3.2. Let t ∈ N. Then

lim sup
N →∞ DN
 ( coth 1
t
 )( log log N
log N
 )2 = t
4 ,(1)
 lim sup
N →∞ DN ( t√e)( log log N
log N
 )2 = t
4 ,(2)
 lim sup
N →∞ DN ( 2t+1√e2)
( log log N
log N
 )2 = 2t + 1
4 .(3)
 P r o o f. Using the well known continued fraction expansions of the num-
bers coth(1/t), t√e and 2t+1√e2 we proceed according to the following
scheme. First we calculate estimates
m∑

i=0 ai+1 ∼ C1(t)m
2 and
 m∑

i=1 log ai ∼ C2(t)m log m

as m → ∞. Since
m∑

i=1 log ai ≤ log qm ≤
 m∑

i=1 log(ai + 1) =
 m∑

i=1 log ai + O(m)

Discrepancy of (nα) 287

we have
 log qm ∼ C2(t)m log m.

For each N ∈ N we deﬁne m ∈ N via the relation qm ≤ N < qm+1. Since
log qm+1 ∼ log qm as m → ∞ we infer log N ∼ C2(t)m log m as N → ∞.
This yields log log N ∼ log m and log N ∼ C2(t)m log m ∼ C2(t)m log log N
as N → ∞. Putting all together we ﬁnd

Sm ∼
 m∑

i=0 ai+1 ∼ C1(t)m2 ∼ C1(t)
C2(t)2
 ( log N
log log N
 )2,

where we made use of
∑

0≤i≤m
 ∑

0≤j≤m
j≡i (mod 2)
 εiεj|sij| = O(m).

The result now follows from Corollary 1.2.

4. The minimum order. We continue by introducing a few more no-
tations. Let qm ≤ N < qm+1. There is a unique expansion N = ∑m
j=0 bjqj
where 0 ≤ bj ≤ aj+1 for all j, b0 < a1 and bj = aj+1 ⇒ bj−1 = 0 for j ≥ 1.
For j ≥ −1 we deﬁne Aj = ∑m
µ=0 bµsµj. Let iN be the smallest integer j ≥ 0
such that bj ̸= 0. Set

s := min{j | 2 ∤ j, 1 ≤ j ≤ m, Aj > 0, Aj+2 > 0 ⇒ bj+1 < aj+2}

and

t := min{j | 2 ∤ j, 1 ≤ j ≤ m, Aj−1 < 0 < Aj+1,
Aj+2 > 0 ⇒ bj+1 < aj+2 − 1},

where min ∅ := ∞. Finally, we deﬁne

u := { 0 if 2 | iN and (b0 < a1 − 1 or A1 < 0),
min{s, t} otherwise.

Theorem 4.1.

ω+
N (α) = ∑

u≤j≤m
j≡0 (mod 2)
 bj(1 − Aj) + ∑

u≤j≤m
Aj+1<0<Aj−1
j≡0 (mod 2)
 Aj − ∑

u≤j≤m
Aj−1≤0<Aj+1
j≡0 (mod 2)
 Aj(1)
 − ∑

u≤j≤m
Aj <0
j≡0 (mod 2)
 aj+1Aj + (δu,0 − 1)Au,

ω−
N (α) = ω+
N (α) + A0 −
 m∑

j=0 bj((−1)
j − Aj)(2)

288 C. Baxa and J. Schoißengeier

and

(3) DN (α) = 2ω+
N (α) + A0 −
 m∑

j=0 bj((−1)
j − Aj).

P r o o f. Though not explicitly stated, (1) and (2) are contained in The-
orem 1 of §8 in [17]. (Note the slightly diﬀerent deﬁnition of the Aj.) (3)
follows immediately from DN (α) = ω+
N (α) + ω−
N (α).

Lemma 4.2. Let qm ≤ N < qm+1. Then

ω+
N (α) = max
1≤k≤N(σ−1(k) − N {kα}) ≥ qm|qmα − pm|

and ω−
N (α) = 1 + max
1≤k≤N(N {kα} − σ−1(k)) ≥ qm|qmα − pm|,

where σ : {1, . . . , N } → {1, . . . , N } is the unique permutation which satisﬁes
{ασ(i)} < {ασ(i + 1)} for 1 ≤ i < N .

P r o o f. There is a k0 (1 ≤ k0 ≤ N ) such that σ−1(k0) = N . We have

σ−1(k0) − N {k0α} = N |1 + [k0α] − k0α| ≥ qm|qmα − pm|

as |qα − p| ≥ |qmα − pm| > |qm+1α − pm+1| for all (q, p) ̸= (qm+1, pm+1)
with 0 ≤ q < qm+1. The second assumption is proved analogously.

Theorem 4.3. If α is an irrational number , then

lim inf
N →∞ DN (α) = 1 + lim inf
m→∞ qm|qmα − pm|.

P r o o f. As in the proof of Corollary 1 in §9 of [17] we compute Dbqm(α)
(where 1 ≤ b ≤ am+1) using Theorem 4.1 and arrive at

Dbqm(α) = b − (b − 2)bqm|qmα − pm| − b|qmα − pm|.

Putting b = 1 leads to

lim inf
N →∞ DN (α) ≤ 1 + lim inf
m→∞ qm|qmα − pm|.

To prove the reverse inequality let ε > 0 and N such that D∗
N (α) =
max(ω+
N (α), ω−
N (α)) > 1 − ε. (The existence of such an N is guaranteed
by Corollary 2 in §9 of [17].) If (without loss of generality) ω+
N (α) > 1 − ε
then DN (α) = ω+
N (α) + ω−
N (α) > 1 + qm|qmα − pm| − ε by Lemma 4.2.

R e m a r k. As proved in the above theorem, DN (α) behaves like D∗
N (α)
if the sequence (aj)j≥1 of partial quotients is unbounded, otherwise it is
closely related to the Lagrange spectrum. As this set has been studied
thoroughly there is an abundance of information available on the set S :=
{lim inf N →∞ DN (α) | α ∈ R\Q} (see [6]). We restrict ourselves to state just
a few of the known facts:
 Discrepancy of (nα) 289

S is a closed subset of the interval [1, 1 + 1/√5] with min S = 1 and
max S = 1 + 1/√5. Its subset S ∩ (1 + 1/3, 1 + 1/√5] consists of the numbers
1 + m/√9m2 − 4 where m is a positive integer such that

m
2 + m
2
1 + m2
2 = 3mm1m2
for some positive integers m1 ≤ m and m2 ≤ m. The three largest numbers
of S are 1 + 1/√5, 1 + 1/√8 and 1 + 5/√221. Let

µ0 = 253589820 + 283748√462
491993569 = 4.527829 . . .

Then [1, 1+1/µ0] ⊆ S and there is no interval I such that [1, 1+1/µ0] ⫋ I ⊆
S. On the other hand, there are gaps in S such as J = (1+1/√13, 1+1/√12),
i.e. J ∩ S = ∅ but 1 + 1/√12 ∈ S and 1 + 1/√13 ∈ S.

References

[1] C. B a x a, Die maximale Gr¨oßenordnung der Diskrepanz der Folge (nα)n≥1, Disser-
tation, Universit¨at Wien, 1993.
[2] —, On the discrepancy of the sequence (nα), to appear.
[3] H. B e h n k e, ¨Uber die Verteilung von Irrationalit¨aten mod 1, Abh. Math. Sem. Univ.
Hamburg 1 (1922), 252–267.
[4] —, Zur Theorie der diophantischen Approximationen I , ibid. 3 (1924), 261–318.
[5] P. B o h l, ¨Uber ein in der Theorie der s¨akularen St¨orungen vorkommendes Problem,
J. Reine Angew. Math. 135 (1909), 189–283.
[6] T. W. C u s i c k and M. E. F l a h i v e, The Markoﬀ and Lagrange Spectra, Math.
Surveys Monographs 30, Amer. Math. Soc., Providence, Rhode Island, 1989.
[7] Y. D u p a i n, R´epartition et discr´epance, Th`ese, Universit´e de Bordeaux I, 1978.

[8] —, Discr´epance de la suite ({n 1+
√
5
2 }), Ann. Inst. Fourier (Grenoble) 29 (1979),
81–106.
[9] Y. D u p a i n and V. T. S ´o s, On the discrepancy of (nα) sequences, in: Topics in
Classical Number Theory, Vol. 1, Colloq. Math. Soc. J´anos Bolyai 34, G. Hal´asz
(ed.), North-Holland, Amsterdam, 1984, 355–387.
[10] G. H. H a r d y and J. E. L i t t l e w o o d, Some problems of Diophantine Approxi-
mation: The lattice points of a right-angled triangle II , Abh. Math. Sem. Univ.
Hamburg 1 (1922), 212–249.
[11] E. H e c k e, ¨Uber analytische Funktionen und die Verteilung von Zahlen mod. Eins,
ibid. 54–76.
[12] J. L e s c a, Sur la r´epartition modulo 1 de la suite nα, Acta Arith. 20 (1972), 345–352.
[13] H. N i e d e r r e i t e r, Application of diophantine approximation to numerical integra-
tion, in: Diophantine Approximation and Its Applications, C. F. Osgood (ed.),
Academic Press, New York, 1973, 129–199.
[14] A. O s t r o w s k i, Bemerkungen zur Theorie der Diophantischen Approximationen,
Abh. Math. Sem. Univ. Hamburg 1 (1922), 77–98.
[15] L. R a m s h a w, On the discrepancy of the sequence formed by the multiples of an
irrational number , J. Number Theory 13 (1981), 138–175.
[16] W. M. S c h m i d t, Irregularities of distribution VII , Acta Arith. 21 (1972), 45–50.
[17] J. S c h o i ß e n g e i e r, On the discrepancy of (nα), ibid. 44 (1984), 241–279.

290 C. Baxa and J. Schoißengeier

[18] J. S c h o i ß e n g e i e r, On the discrepancy of (nα) II , J. Number Theory 24 (1986),
54–64.
[19] —, Absch¨atzungen f¨ur ∑

n≤N B1(nα), Monatsh. Math. 102 (1986), 59–77.
[20] —, The discrepancy of (nα)n≥1, Math. Ann. 296 (1993), 529–545.
[21] W. S i e r p i ń s k i, Sur la valeur asymptotique d’une certaine somme, Bull. Int. Acad.
Polon. Sci. (Cracovie) A (1910), 9–11.
[22] —, On the asymptotic value of a certain sum, Rozprawy Akademii Umiejętności
w Krakowie, Wydział mat. przyrod. 50 (1910), 1–10 (in Polish).
[23] V. T. S ´o s, On the theory of diophantine approximation II (inhomogeneous prob-
lems), Acta Math. Acad. Sci. Hungar. 9 (1958), 229–241.
[24] —, On strong irregularities of the distribution of {nα} sequences, in: Studies in Pure
Mathematics, P. Erd˝os (ed.), Birkh¨auser, Boston, 1983, 685–700.
[25] H. W e y l, ¨Uber die Gibbs’sche Erscheinung und verwandte Konvergenzph¨anomene,
Rend. Circ. Mat. Palermo 30 (1910), 377–407.
[26] —, ¨Uber die Gleichverteilung von Zahlen mod. Eins, Math. Ann. 77 (1916), 313–352.

INSTITUT F ¨UR MATHEMATIK

UNIVERSIT ¨AT WIEN

STRUDLHOFGASSE 4

A-1090 WIEN, AUSTRIA

E-mail: BAXA@PAP.UNIVIE.AC.AT
 Received on 17.12.1993 (2547)
