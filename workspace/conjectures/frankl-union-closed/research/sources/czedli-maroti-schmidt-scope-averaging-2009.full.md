<!-- source: https://www.math.u-szeged.hu/~czedli/m/publ.pdf/czedli-maroti-schmidt_on-the-scope-of-averaging-Frankl's-conjecture.pdf | converted from PDF -->

ON THE SCOPE OF AVERAGING FOR FRANKL9S
CONJECTURE

z .65OR –Z.Pˇ/Wg MWY/ .OS M6R .OTWg 6Nˇ P9 T6M .6S S–ﬀMWˇT

Abstract- /et F be a union1closed family of subsets of an m1element set A9
/et n J |F| ≥ x9 Vor b ∈ A let wrb( denote the number of sets in F containing
b minus the number of sets in F not containing b9 Franklbs conjecture from
w’[’g also known as the unionIclosed sets conjectureg states that there exists
an element b ∈ A with wrb( ≥ k9
The present paper deals with the average of the wrb(g computed over all
b ∈ A9 F is said to satisfy the averaged Franklbs property if this average is non1
negative9 6lthough this much stronger property does not hold for all union1
closed familiesg the Irst author [[] veriIed the averaged VranklFs property
whenever n ≥ xm − xm/2 and m ≥ 09
The main result of this paper shows that rw( we cannot replace xm/2 with
the upper integer part of xm/0g and rx( if VranklFs conjecture is true rat least
for m1element base sets( and n ≥ xm −⌊xm/0⌋ then the averaged VranklFs
property holds ri9e9g xm/2 can be replaced with the lower integer part of xm/0(9
The proof combines elementary facts from combinatorics and lattice theory9
The paper is self1containedg and the reader is assumed to be familiar neither
with lattices nor with combinatorics9

’C Introduction and the main theorem

ﬂiven an mqelement tnite set A “ {a1,. .. , am}Ha family jorH in other wordsH
a setx F of subsets of AH iCeC F· P jAxH is called a union-closed family jover
Axif X ∪ Y ∈F whenever X, Y ∈FC We always assume that A is tnite with
ˇ ↦ m 0“ |A| and n 0“ |F| • BC Ut was Peter ;rankl in ’R5R who formulated
the following conjectureH now known as Frankl1s conjecture or the union-closed sets
conjecture0if F is as above then there exists an element of A which is contained
in at least half of the members of FC Un spite of at least three dozen papersH this
conjecture is still openC Eence it will be convenient to use the following terminology0
we say that Frankl1s conjecture holds over m-element base setsH if for any unionq
closed family F of subsets of an mqelement jequivalentlyH at most mqelementx set
A with |F| • BH there exists an element of A which is contained in at least half of
the members of FC
VlearlyH it is suscient to consider only those unionqclosed sets that contain the
empty setC Eence in the sequelH when the size |F| of F will be importantH we will
always assume that ∅∈ FC

Date3 qanuary ]g xkk]g revised3 ˇecember wwg xkk]9
Key words and phrasesU Union1closed setsg VranklFs conjectureg lattice9
This research was partially supported by the NVSR of ﬀungary rOTY6(g grant no9 T kp’p00g
T p]]k’ and Y ﬁkwp]9
 1

2G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

The known achievements on ;ranklgs conjecture belong to two categoriesC The
trst category is constituted by those jin factH the majority ofx results that beq
long to pure combinatoricsH with respect to both the statements and their proofsC
There are several directions and the titles of the listed references speak for themq
selvesH so we mention only a few results relevant to our investigationsC Sohsnjak and
8arkovirc [´] prove that ;ranklgs conjecture holds over elevenqelement base setsH
while Roberts [ˇT] settles the case n “ |F| ↦ MT and n< Mm − ’C Ns an opposite to
Robertsg result on “small familiesPH ﬂao and Yu [’ˇ] verify the conjecture for “very
large familiesPH iCeC for those with

j’x n • B
m − ’B
(ˇ
B
 )[m/3] − ’
B
 (
m
ˇ
 ) − ´
ˇ m zMM.´ .

;or other achievements of combinatorial nature cfCH eCgCH ﬀorton and Sarvate [B’]
and Vaughan [ˇB]C !ne can read more about the problem at [ˇ5] orH of courseH in
;rankl [’B]C
!n the other handH Stanley [ˇ’] and Poonen [BB] establish a nice lattice theoq
retic version of ;ranklgs conjectureC j;or details one can also see [5] or Nbe and
ﬀakano [ˇ]Cx This initiated a series of lattice theoretical papers given by Nbe and
ﬀakano [’]H [B]H [ˇ]H [M]H Eerrmann and 6angsdorf [’M]H and Reinhold [BM] jsome
of which contained results already known in the folklorex4 these are the results
belonging to the second categoryC
EoweverH there were no real links between the combinatorial and the lattice
theoretical approaches before [5]H except of course for the statement of their equivaq
lenceC Un particularH results that look “combinatorialP were proved by combinatorial
methodsH and the lattice theoretical results have not had a signitcant inﬁuence on
combinatoristsC This is very surprisingH for the lattice theoretic approach has at
least one obvious advantage0 while it is fairly discult to visualize a unionqclosed
family withH sayH jm, nx“ j´, ’BxH depicting the Easse diagram of the corresponding
twelve element lattice creates no problem at allC
ProbablyH [5] is the trst case when a purely combinatorial statement is proved
within lattice theoryC SimilarlyH the present paper belongs to neither of the aboveq
mentioned two categoriesC !ur main result is purely combinatorial without menq
tioning latticesC Uts proof is a mixture of lattice theory and combinatoricsC EoweverH
only the rudiments of lattice theory and those of combinatorics are usedC So the
paper is intended to be selfqcontained for most of the readersC

6et F be a unionqclosed family over A and let the notations n “ |F| • BH
m “ |A| “ {a1,. .. , am} be txed throughoutC ;or a ∈ A let

jBx wjax“ |{X ∈F 0 a ∈ X}| − |{X ∈F 0 a/∈ X}| .

Then ;ranklgs conjecture claims the existence of an a ∈ A with wjax • TC With
the notation wjFx“ ’
|A|
 ∑

a∈A wjax

let us say that F satistes the averaged Frankl1s property if

wjFx • T .

Nlthough this property clearly implies that ;ranklgs conjecture holds for the given
FH it belongs to the folklore that many unionqclosed families fail to satisfy the
averaged ;ranklgs propertyC

AVERAGING FOR FRANKL8S CONJECTURE 3

;or a given m “ |A|H the maximum value of n is of course B
mC ;or “largeP
unionqclosed families F including ∅H it is proved in [5] that

jˇx |F| • B
m − B
m/2 “⇒ wjFx • T.

This statement is much stronger than ﬂao and Yugs j’x in two senses0 jˇx covers
many more instances of FH and “;ranklgsP is replaced by “averaged ;ranklgsPC

Lven if B
m/2 is betterH iCeCH largerH than the corresponding expression in j’xH
already [5] observes that Bm/2 is not the optimal valueC The original target of
the present paper was to replace B
m/2 in jˇx with the best possible valueH in the
additional hope that the improved version of jˇx gives more information on the
original ;ranklgs conjecture as wellC UnfortunatelyH this extra hope is not fultlled
yetH for the main theorem below assumes the validity of ;ranklgs conjectureC Ns
usualH the upper respC lower integer part of a real number x will be denoted by ⌈x⌉
respC ⌊x⌋4 for example ⌈ˇB/ˇ⌉ “ ’’C

Main Theorem. Let m • ˇ, and let A be an m-element set.

j’x There exists a union-closed family F over A with ∅∈ F and |F| “ ⌊B
m+1/ˇ⌋ “
⌈B
m+1/ˇ⌉− ’ such that F fails the averaged Frankl1s property.
jBx Assume that Frankl1s conjecture holds over m-element base sets. Then each
union-closed family F over A with ∅∈ F and

jMx n 0“ |F| • ⌈B
m+1/ˇ⌉

satisses the averaged Frankl1s property.

;ranklgs conjecture has been intensively studied and it is almost three decades
oldC Eence it is reasonable to conjecture that jMx in itself implies wjFx • T for
unionqclosed families FC

The rest of the paper is devoted to the proof of this theorem and will run as
followsC ;irst we introduce some integer sequencesH and study their elementary
propertiesC This requires only elementary arguments with inductionC Then we
study orderqideals and jorderqx semiqideals jto be detned laterx of tnite Soolean
latticesC We are interested in how to maximize the sum jequivalentlyH the averagex
of heights of elements of an orderqideal or semiqideal X when |X| is txedC Using the
properties of our integer sequences we will show the expected but nontrivial fact
that this maximum is available via the obvious greedy algorithmC !rderqideals do
not create an invincible problem4 howeverH our treatment for semiqideals needs the
assumption that ;ranklgs conjecture holds over mqelement base setsC This leads to
a new conjectureH formulated at the end of the paperC
!nce the greedy algorithm for semiqideals is proven to be appropriateH the 8ain
Theorem follows immediately from its obvious reformulation for semiqidealsC Nlq
though this reformulation translates the problem to 6attice TheoryH this is an easier
and less elegant translation than the usual one by Stanley [ˇ’] and Poonen [BB]C

BC Some integer sequences

We are going to detne and study three kinds of integer sequences0 ⃗wH ⃗/ and ⃗xC
The ⃗w respC ⃗/ sequences calculate the total height of greedy orderqideals respC greedy
semiqideals jto be detned laterxC The ⃗x sequences are the stepping stone between

4G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

these two kinds of idealsH and the ⃗x sequences are also needed to understand the
inner structure of ⃗/ sequencesC
Un this sectionH m and n will denote arbitrary natural numbersC ﬂiven two
integer sequences ⃗a “ja1,. .., amx and ⃗b “jb1,. .. , bnxH their concatenation will be
denoted by
 ja1,. .. , amx ⊎ jb1,. .. , bnx“ ja1,. .., am,b1,. .. , bnx.

The length of a sequence ⃗a is denoted by lengthj⃗ax4 it is always a positive integer
and we have lengthj⃗ax z lengthj⃗bx “ lengthj⃗a ⊎ ⃗bxC When lengthj⃗ax “ lengthj⃗bx
then ⃗a z ⃗b and ⃗a − ⃗b are understood componentwiseH eCgCH

ja1,. .. , akxz jb1,. .. , bkx“ ja1 z b1,. .., ak z bkx.

The constant sequence jj, j, ... ,jx will be denoted by dj4 we use this notation only
in connection with additionH so there will be no ambiguity what the length of dj isC
;or exampleH ja1,. .. , akxz d’is ja1 z’,. .. , ak z ’xC When there exists a sequence
⃗c with ⃗a ⊎ ⃗c “ ⃗b then we say that ⃗a is a jproperx initial segment of ⃗bC ﬀowH via
inductionH let us detne

⃗w90) “ jTx,⃗w9i+1) “ ⃗w9i) ⊎ jd’z ⃗w9i)x,

⃗x9i) “ d’z ⃗w9i) ji “T, ’, B .. .x, and

⃗/91) “ x0, ⃗/9i+1) “ ⃗x9i) ⊎ ⃗/9i), which means that

⃗/9j) “ ⃗x9j−1) ⊎ ⃗x9j−2) ⊎ {{{ ⊎ ⃗x91) ⊎ ⃗x90) jj “’, B, ˇ,. ..x.

;or exampleH
 ⃗w94) “j
 ⃗w93)
︷ ︸︸ ︷
T, ’, ’, B
︸ ︷︷ ︸
⃗w92)
 , ’, B, B, ˇ
︸ ︷︷ ︸
d’z ⃗w92)
,
 d’z ⃗w93)
︷ ︸︸ ︷
’, B, B, ˇ, B, ˇ, ˇ, Mx and

⃗/94) “j ’, B, B, ˇ, B, ˇ, ˇ, M
︸ ︷︷ ︸
⃗x93)
 , ’, B, B, ˇ
︸ ︷︷ ︸
⃗x92)
 , ’, B
︸︷︷︸
⃗x91)
 , ’︸︷︷︸
⃗x90) x .

ﬀotice that lengthj⃗w9i)x “ lengthj⃗x9i)x“B
i jT ↦ ix while lengthj⃗/9i)x“ B
i − ’
j’ ↦ ixC The trst member of a sequence is always indexed by ’C The ith member
of ⃗w9n) willH of courseH be denoted by ⃗w9n)
i H and similar notations apply for ⃗/9n)

and ⃗x9n)C ;or convenienceH let ⃗w9∞) respC ⃗x9∞) denote the insnite sequence whose
initial segment of length B
k is ⃗w9k) respC ⃗x9k) for each k ∈ N “ {’, B,. ..}C
;or T ↦ k ↦ nH the subsequences of the form

segmj⃗a, B
k,ix0“jai2k+1,ai2k+2,. .. , a9i+1)2kx,i “T, ’,. .., B
n−k − ’

are called B
k-segments of ⃗a “ja1,. .. , a2nxC Vonsecutive Bkqsegments will play an
important role in the forthcoming considerationsC 6et

segmj⃗a, B
k,ix,. .. , segmj⃗a, B
k,i z ℓ − ’x and

segmj⃗a, B
k,jx,. .. , segmj⃗a, B
k,j z ℓ − ’x

be two families of ℓ consecutive B
kqsegmentsH and consider two subsets X and Y
of the corresponding index setsH iCeCH let X ·{t 0 iB
k z’ ↦ t ↦ ji z ℓxBk} and
Y ·{t 0 jB
k z’ ↦ t ↦ jj z ℓxBk}C We say that X and Y are equally positioned in

AVERAGING FOR FRANKL8S CONJECTURE 5

these families of B
k-segments if X → Y H x ↦→ x zjj − ixBk is a bijectionC That isH
“equally positionedP has the natural meaningC
ﬂiven a sequence ⃗a “ja1,. .. , aℓx4 the sum of t consecutive members of ⃗a beginq
ning at the ith position will be denoted by

yj⃗a, i, tx“ ai z ai+1 z {{ { z ai+t−1 .

This notation assumes that ’ ↦ iHT ↦ t and i z t − ’ ↦ ℓC ﬀotice that yj⃗a, i, Tx“T
by conventionC The forthcoming lemmas will be formulated only for ⃗w9n)H but other
than 6emma B they will be obviously valid and used for ⃗x9n) as wellC Ns usualH
N0 “ N ∪{T} denotes the set of nonnegative integersC

Lemma 1. Let i ∈ N and j ∈ N0 with i z j − ’ ↦ B
n. Then yj⃗w9n), ’,jx ↦
yj⃗w9n),i,jx.

Proof. We can assume that i> ’C We use induction on jC Since ⃗w9n)
1 is the only
occurrence of T in ⃗w9n)H the statement is evident for j ↦ ’C So we assume that
j> ’ and the lemma holds for ’,. .. , j − ’C ;or brevityH let x “ yj⃗w9n), ’,jx and
y “ yj⃗w9n),i,jxC
Uf i ↦ j jpictorially0 if x and y overlapx then

x “ yj⃗w9n), ’,i − ’x z yj⃗w9n),i,j − i z ’x and

y “ yj⃗w9n),i,j − i z’x z yj⃗w9n),j z’,i − ’x ,j´x

and x ↦ y follows from the induction hypothesisC
Eence we can assume that i>jC The pictorial illustration below jeven if it does
not reﬁect the full generalityx will be useful for what comes next0

⃗w9n) “j ⃗w9k)
︷ ︸︸ ︷
⌊,. .. , ⌊,
 d’z ⃗w9k)
︷ ︸︸ ︷
⌊,. .. , ⌊,
 d’z ⃗w9k)
︷ ︸︸ ︷
⌊,. .. , ⌊,. .. , du z ⃗w9k)
︷ ︸︸ ︷
⌊,. .., ⌊, dv z ⃗w9k)
︷ ︸︸ ︷
⌊,. .., ⌊, dw z ⃗w9k)
︷ ︸︸ ︷
⌊,. .., ⌊,. ..x

⃗w9n) “j ⌊,. .. , ⌊, ⌊,. .. , ⌊, ⌊
︸ ︷︷ ︸
z
 ,. .. , ⌊,. .., ⌊,. .., ⌊, ⌊,. .., ⌊, ⌊
︸ ︷︷ ︸
y
 ,. .., ⌊,. ..x .

Vonsider the unique k ∈ N0 such that B
k ↦ j< B
k+1C The assumption that x and
y do not overlap implies that k ↦ n − ’C
;irstlyH we assume that k< n − ’C Then we can choose three consecutive B
kq
segmentsH say segmj⃗w9n), B
k,qxH segmj⃗w9n), B
k,q z ’x and segmj⃗w9n), B
k,q z BxH such
that the summands of y belong to this family B of consecutive B
kqsegmentsC j8ore
precisely but less pictoriallyH such that qB
k z’ ↦ i and i z j − ’ ↦ jq z ˇxBkCx
Vonsider also the family A of the Bkqsegments segmj⃗w9n), B
k, TxH segmj⃗w9n), B
k, ’x
and segmj⃗w9n), B
k, BxH that isH the trst three B
kqsegmentsC 6et z be the sum of j
consecutive members in the trst three B
kqsegments such that the summands of z in
A and the summands of y in B are equally positionedC j8ore formallyH i “ qB
k z r
and z “ yj⃗w9n),r,jxCx !bserve that A consists of ⃗w9k)H d’z ⃗w9k)H d’z ⃗w9k) while B
consists of du z ⃗w9k)Hdv z ⃗w9k)Hdw z ⃗w9k) for appropriate positive integers u, v, wC
ﬀowH T <uH’ ↦ v and ’ ↦ wH whence the elements of the trst three Bkq
segments are less than or equal to the corresponding elements of segmj⃗w9n), B
k,qxH
segmj⃗w9n), B
k,q z ’xH and segmj⃗w9n), B
k,q z BxC Eence z ↦ yH for z and y are equally
positionedC ;urtherH x ↦ z follows from the previously considered “overlappingP
caseH and we conclude x ↦ yC

6G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

SecondlyH we assume that k “ n − ’C Then ⃗w9n) consists of two Bkqsegments onlyC
Since x and y do not overlapH we obtain that j “B
k and i “B
k z ’C Using ⃗w9n) “
⃗w9k) ⊎ jd’z ⃗w9k)xH we conclude that x “ yj⃗w9k), ’, B
kx <yjd’z ⃗w9k), ’, B
kx“ yC ⊴

Oetne the inverse of a sequence ⃗a “ja1,a2,. .. , akxas

invja1,a2,. .. , akx“ jak,ak−1,. .. , a1x.

The proofH a trivial inductionH of the following lemma is left to the readerC

Lemma 2. ⃗w9n) z invj⃗w9n)x“ dn.

ﬀow we formulate a statement on the sum of the last j members of ⃗w9n)C

Lemma 3. If j ↦ B
n and ’ ↦ i< B
n − j then yj⃗w9n),i,jx ↦ yj⃗w9n), B
n − j z’,jx.

Proof. Vonsider the sequence dn − ⃗w9n)C This sequence is the inverse of ⃗w9n)H so the
sum of the last j members becomes the sum of the trst j membersC Eence the
assertion follows from 6emma ’C ⊴

Lemma 4. Let i, j < B
n and desne

u 0“
 {i z j, if i z j ↦ B
n

B
n, if i z j> B
n and v 0“ i z j − u.

Then yj⃗w9n), ’,ixz yj⃗w9n), ’,jx ↦ yj⃗w9n), ’,uxz yj⃗w9n), ’,vx.

Proof. Uf i z j ↦ B
n then v “ T gives yj⃗w9n), ’,vx “ TH and the assertion is a trivial
consequence of 6emma ’C Eence we can assume that i z j> B
nC 6et us compute4
the application of 6emma ˇ will be denoted by ∞H and we will use that j − v “B
n − i
and jthereforex j> v0

yj⃗w9n), ’,ixz yj⃗w9n), ’,jx“ yj⃗w9n), ’,ixz yj⃗w9n), ’,vxz yj⃗w9n),v z’,j − vx

↦
∞yj⃗w9n), ’,ixz yj⃗w9n), ’,vxz yj⃗w9n),i z’, B
n − ix“

yj⃗w9n), ’, B
nxz yj⃗w9n), ’,vx“ yj⃗w9n), ’,uxz yj⃗w9n), ’,vx . ⊴

Lemma 5. If ’ ↦ i< B
n then ⃗/9n)
i ↦ ⃗x9n)
i .

Proof. Nn easy induction on nCUf i ↦ B
n−1 then ⃗/9n)
i “ ⃗x9n)
i by detnitionC !therq
wise ⃗/9n)
i “ ⃗/9n−1)
i−2n−1 ↦ ⃗x9n−1)
i−2n−1 < jd’z ⃗x9n−1)xi−2n−1 “ ⃗x9n)
i C ⊴

Lemma 6. If T ↦ j< B
n−1 and T ↦ i ↦ B
n−1 then yj⃗/9n), B
n−1 z’,jx ↦
yj⃗/9n),i,jx.

Proof. ;or brevityH let x “ yj⃗/9n), B
n−1 z’,jx and y “ yj⃗/9n),i,jxC
;irst assume that i z j − ’ ↦ B
n−1C This means that the summands of y lie
entirely in ⃗x9n−1)4 howeverH the following illustration is only a particular case jfor
y and z may overlapx0

⃗/9n) “j ⃗x9n−1)
︷ ︸︸ ︷
⌊,. .. , ⌊
︸ ︷︷ ︸
z
 ,. .. , ⌊,. .., ⌊
︸ ︷︷ ︸
y
 ,. .. , ⌊,
 ⃗/9n−1)
︷ ︸︸ ︷
⌊,. .., ⌊
︸ ︷︷ ︸
x
 , ⌊, ⌊, ⌊, ⌊,. .., ⌊ x

;or z “ yj⃗/9n), ’,jx“ yj⃗x9n−1), ’,jx we obtain x ↦ z from 6emma ´C Then
z ↦ yj⃗x9n−1),i,jx“ y by 6emma ’H whence x ↦ yC

AVERAGING FOR FRANKL8S CONJECTURE 7

ﬀow we assume that B
n−1 <i z j − ’H which means that x and y overlapC
6et z “ yj⃗/9n), B
n−1 z’,i z j − B
n−1 − ’xH the “intersection of x and yPH u “
yj⃗/9n),i z j, B
n−1 z’ − ixH v “ yj⃗/9n),i, B
n−1 z’ − ixH andH furtherH let w “
yj⃗/9n),i z j − B
n−1, B
n−1 z’ − ixC Then x “ z z u and y “ z z vH cfC the illustration
below jnotice that w and v may overlapxC

⃗/9n) “j ⃗x9n−1)
︷ ︸︸ ︷
⌊, ⌊,. .., ⌊, ⌊,. . ., ⌊
︸ ︷︷ ︸
w
 ,. .. , ⌊,. .., ⌊
︸ ︷︷ ︸
v
 ,
 ⃗/9n−1)
︷ ︸︸ ︷
⌊, ⌊,. .., ⌊
︸ ︷︷ ︸
z
 , ⌊,. .., ⌊
︸ ︷︷ ︸
u
 ,. .., ⌊,. .., ⌊x

Since u and w are “equally positionedPH 6emma ´ gives u ↦ wC Then 6emma ˇ
applied to ⃗x9n−1) yields w ↦ vC ;inallyH u ↦ v implies x “ z z u ↦ z z v “ yC ⊴

Lemma 7. If T ↦ i< B
n−1 and T ↦ j ↦ B
n−1 then

yj⃗/9n−1), ’,ixz yj⃗x9n−1), ’,jx ↦ yj⃗/9n), ’,i z jx.

Proof. Since ⃗/9n) “ ⃗x9n−1) ⊎ ⃗/9n−1)H we can compute0

yj⃗/9n−1), ’,ixz yj⃗x9n−1), ’,jx“ yj⃗/9n), B
n−1 z’,ixz yj⃗/9n), ’,jx ↦
∞

yj⃗/9n),j z’,ixz yj⃗/9n), ’,jx“ yj⃗/9n), ’,i z jx ,

where ∞ stands for an application of 6emma [C ⊴

;or a sequence ⃗aH let Ej⃗a,i,.. . ,jx denote

Ej⃗a,i,.. ., jx“ yj⃗a, i, j − i z’x
j − i z’ “ ai z ai+1 z {{ { z aj
j − i z’ ,

the average of the elements in the segment jai,ai+1,. .., ajxC Remember that ⃗x9∞)

was introduced for convenience right before the detnition of segments4 of course
⃗x9∞) could be replaced by ⃗x9n) in the following lemmaC

Lemma 8. Let B ↦ n ∈ N.

j’x For k “’, B,. .., ⌊B
n/ˇ⌋, Ej⃗/9n), ’,. .., kx“ Ej⃗x9∞), ’,. .., kx ↦ n/B.
jBx Ej⃗/9n), ’,. .., ⌊B
n/ˇ⌋ z’x “ Ej⃗x9∞), ’,. .., ⌊B
n/ˇ⌋ z’x >n/B.
jˇx For ⌊B
n/ˇ⌋ <k ↦ B
n − ’, Ej⃗/9n), ’,. .., kx >n/B.

ﬀotice that the equations in Parts j’x and jBx are clear by detnitionsC Nlthough
Part jˇx implies Part jBxH we will prove only Parts j’x and jBxC Part jˇx will not
be provedH for it will not be used in the sequel and its proof is similar to but
considerably lengthier than the proofs of Parts j’x and jBxC

Proof. Oetne

Sn “ {k ∈ N 0 Ej⃗x9∞), ’,. .., tx ↦ n/B for t “’, B,. .., k}.

!ne can easily see that proving that ⌊B
n/ˇ⌋ is the largest member of Sn is equivalent
to proving Parts j’x and jBx for nC We prove this via induction on nC The case
n “ B is evidentC ﬀow suppose that n • ˇ and that Parts j’x and jBx hold for n − ’C

8G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

The trst few members of ⃗x9∞) are depicted below for n “´0

⃗x9n−1)
︷ ︸︸ ︷
⃗x9n−3)
︷ ︸︸ ︷
’, B, B, ˇ,
 d’z ⃗x9n−3)
︷ ︸︸ ︷
B, ˇ, ˇ, M
︸ ︷︷ ︸
⃗x9n−2)
 , B, ˇ, ˇ, M, ˇ, M, M, ´
︸ ︷︷ ︸
d’z ⃗x9n−2)
 ,
 d’z ⃗x9n−1)
︷ ︸︸ ︷
B, ˇ, ˇ, M, ˇ, M, M, ´, ˇ, M, M, ´, M, ´, ´, [,. ..

Since B
n−3 ↦⌊B
n−1/ˇ⌋H the induction hypothesis gives

j[x Ej⃗x9∞), ’,. .., kx ↦ jn − ’x/B for ’ ↦ k ↦ B
n−3.

Eence {’, B,. .., B
n−3}· SnC Ut follows from 6emma B that

j5x Ej⃗x9∞), ’,. .., B
n−3x“ jn − ’x/B.

Rewriting j[x from the trst B
n−3qsegment to the second oneH which is d’z ⃗x9n−3)H
we obtain

Ej⃗x9∞), B
n−3 z’,. .., B
n−3 z kx ↦ jn z’x/B for ’ ↦ k ↦ B
n−3.

This implies {’, B,. .., B
n−2}· SnC ﬀowH j5x for the second Bn−3qsegment gives
Ej⃗x9∞), B
n−3 z’,. .. , B
n−3 zB
n−3x“ jn z’x/BH which combined with j5x yields

j]x Ej⃗x9∞), ’,. .., B
n−2x“ n/B.

The shift from the trst Bn−2qsegment to the second oneH d’z ⃗x9n−2)H changes j]x
into Ej⃗x9∞), B
n−2 z’,. .. , B
n−1x“ ’ z n/B“ jn zBx/BH which together with j]x
gives Ej⃗x9∞), ’,. .., B
n−1x“ jn z’x/BC Eence B
n−1 /∈ SnH and we conclude that
the largest member of Sn is Bn−2 z k for some T ↦ k< B
n−2C Ut follows from
j]x that k is the largest number in {T, ’,. .., B
n−2 − ’} such that Ej⃗x9∞), B
n−2 z
’,. .., B
n−2 z kx ↦ n/BC ﬀow going from the second B
n−2qsegment d’z ⃗x9n−2) to the
trst Bn−2qsegment ⃗x9n−2)H we see that k is the largest number in {T, ’,. .., B
n−2−’}
such that Ej⃗x9∞), ’,. .., kx ↦ n/B−’“ jn−Bx/BC Eence k is the largest member of
Sn−2H whence the induction hypothesis gives k “ ⌊B
n−2/ˇ⌋C ThereforeH the largest
member of Sn is B
n−2 z ⌊B
n−2/ˇ⌋ “ ⌊B
n−2 zB
n−2/ˇ⌋ “ ⌊B
n/ˇ⌋C ⊴

ˇC Semi3ideals and a Theorem equivalent to the Main Theorem

Sy a lattice jL4 ↦x we mean a partially ordered set such that for any x, y ∈ L
the supremum and intmum of {x, y} exist4 they are denoted by x ∨ y and x ∧ yH
respectivelyC We deal only with snite lattices4 they necessarily have a unique least
element T and a unique largest element ’C ;or a ↦ b ∈ L the subset {x ∈ L 0 a ↦
x ↦ b} is denoted by [a, b] and it is called an interval of LC When a “T or b “’
then a particular notation applies0 ↑a “[a, ’] and ↓b “[T,b]C The covering relation
∼ is detned via a ∼ b im a ↦ b and |[a, b]| “ BC Uf T ∼ a then a is called an atom of
the latticeC
6et Bm denote the Soolean lattice of size B
mC Lach x ∈ Bm has a unique com-
plement x′ satisfying x ∨ x′ “ ’ and x ∧ x′ “ TC ﬀotice that Bm is isomorphic to the
power set lattice over an mqelement set4 the singleton setsH the complements of subq
setsH the empty set and the whole set corresponding to the atomsH the complements
of elementsH T and ’ of BmH respectivelyC The height hjxx of an element x ∈ Bm is
the length of any maximal chain in ↓xC Un the powerset modelH the height is just
the number of elements of the given subsetC Uf X is a subset of BmH then the total

AVERAGING FOR FRANKL8S CONJECTURE 9

height hjXxof X is detned to be the sum ∑

a∈X hjaxC Uf X is a nonempty subset
X of BmH then its average height is detned to be and denoted by

hjXx“ hjXx/|X| .

N nonempty subset X of Bm is called an order-ideal if for any x ∈ XH ↓x · XCUf
a nonempty set X is the union of certain intervals [ai,bi] such that the ai are jnot
necessarily distinctx atomsH then X is said to be a semi-ideal of BmC
The goal of the next section is to show that whenever the size |X| of an orderq
ideal is txedH then a straightforward greedy algorithm produces an orderqideal with
maximum total heightC We also prove the analogous statement for semiqideals4
howeverH we could not avoid assuming ;ranklgs conjecture in that caseC The imporq
tance of semiqideals is revealed by the following theorem and the lemma following
itC

Theorem 1. Let m • ˇ.

j’x There exists a semi-ideal X of Bm such that hjXx >m/B and |X| “
⌈B
m/ˇ⌉.
jBx Assume that Frankl1s conjecture holds over m-element base sets. Then for
each semi-ideal X of Bm, |X|↦ ⌊B
m/ˇ⌋ implies hjXx ↦ m/B.

Sy a proper subalgebra of jBm, ∨, Tx we mean a ∨qclosed subset Y of Bm such
that T ∈ Y ̸“ BmC The importance of the above theorem is due to

Lemma 9. Let m ∈ N.

j’x For X · Bm, X is a semi-ideal ic Bm \ X is a proper subalgebra of
jBm, ∨, Tx.
jBx The Main Theorem and Theorem 1 are equivalent statements.
jˇx Assume that Frankl1s conjecture holds over m-element base sets. Then for
each semi-ideal X of Bm other than Bm \{T}, |X ∩↑a|↦ |X|/B for some
atom a ∈ Bm.

Proof. 6et X be a semiqidealH and let u, v ∈ Y “ Bm \ XC Sy way of contradictionH
suppose u ∨ v/∈ Y C Then [p, u ∨ v] · X for some atom p ∈ BmC ;rom p ↦ u ∨ v we
conclude p ↦ u or p ↦ vHsayH p ↦ uH whence u ∈ [p, u ∨ v] · X contradicts u ∈ Y C
This shows that Y is a subalgebra of jBm, ∨, TxC Ut is properH for X ̸“ ∅C
ﬀow let Y “ Bm \ X be a proper subalgebra of jBm, ∨, TxC Then X ̸“ ∅C 6et
u ∈ XH we have to tnd an atom p ∈ Bm with [p, u] ∩ Y “ ∅C 6et y denote the
join of the set Y ∩↓uC Since y ∈ Y H we have y< u and therefore there is an atom
p ∈↓u \↓yH which does the jobC This proves Part j’xC
ﬀowH keeping formula jBx and the powerset model of Bm in mindH for a proper
subalgebra F of jBm, ∨, TxH we let

wjF x“ ’
m { ∑

a is an atom of Bm
 wjax

where
 wjax“|F ∩↑a |−|F ∩↓a
′ | “B {|F ∩↑a |−|F ∩↑a |−|F ∩↓a
′ |

“B {|F ∩↑a |−|F |.

10 G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

Eence wjF x • Tim

T ↦ ∑

a atomjB {|F ∩↑a |−|F |x“B(− ∑

a atom |F |/Bz ∑

a atom |F ∩↑a |)

“B
(
−m|F |/Bz ∑

ja, bx0 a ↦ b ∈ F, a atom ’
)

“B
(
−m|F |/Bz ∑

b ∈ F
 ∑

a ↦ b, a atom ’
)

“B
(
−m|F |/Bz ∑

b ∈ F hjbx) “B
(
−m|F |/Bz hjF x(
.

Oividing by B|F | we obtain that wjF x • Tim hjF x • m/BC ﬀow let X “ Bm \ F H
a semiqideal by Part j’xC Since hjBmx“ m/BH hjF x • m/Bim hjXx ↦ m/BH
completing the proof of Part jBxC
;inallyH the straightforward deduction of Part jˇx from the above arguments is
left to the readerC ⊴

MC Greedy order3ideals and greedy semi3ideals

ﬂiven an integer k ∈{’,. .., B
m}H we are looking for a kqelement orderqideal X of
the Soolean lattice Bm with maximal total height hjXxC Ut is natural to construct
X in a greedy way by induction on kC;or k ↦ ˇH every kqelement orderqideal has
the same total heightC Suppose we know how to construct a jk − ’xqelement orderq
ideal Y of maximal total heightC Then we let X “ Y ∪{x} such that x/∈ Y H X
is an orderqideal and hjxx is as large as possibleC ﬀow we have roughly described
our greedy algorithmC The goal of this section is to show that it maximizes the
total heightH indeedC ;irst of allH a more exact description of the greedy algorithm
is necessaryC
6et a1,a2,. .. , am be a txed enumeration of the atoms of BmC Nssociated with
this enumeration we detne a greedy enumeration of Bm via induction as followsC
j;or x, y ∈ BmH x ▹ y will denote that x precedes y in the greedy enumerationCx
;or m ↦ ’H let ▹ coincide with the strict lattice order jwhich is a linear orderH
iCeCH a chainH in this casexC ﬀow assume that m> ’C VlearlyH a1 ∨{ { { ∨ am−1
is a
′
mH the complement of amC The isomorphism theorem of intervals yields that
a1 ∨ am,. .. , am−1 ∨ am is an enumeration of atoms of ↑amH which is a Soolean
latticeC 6et ▹2 denote the greedy enumeration of ↑am associated with the menq
tioned enumeration of its atomsC 6et ▹1 denote the greedy enumeration of ↓a
′
m
associated with the enumeration a1, {{ { ,am−1 of its atomsC ;inallyH let ▹ be the
“concatenationP of ▹1 and ▹2 in the following sense0 for x, y ∈ BmH x ▹ y im
x, y ∈↓a
′
m with x ▹1 yHor x, y ∈↑am with x ▹2 yHor x ∈↓a
′
m and y ∈↑amC The
leftqhand lattice in ;igure ’ shows the greedy enumeration of B3 associated with
the “from left to rightP enumeration jiCeCH a1 “ c2H a2 “ c3H a3 “ c5x of its atomsC
jThe greedy enumeration is detned by the indexing0 ci ▹ cj im i<jCx ﬀowH by a
greedy order-ideal of Bm we mean a nonempty subset of the form {x ∈ Bm 0 x ⊴ b}
where ▹ is a greedy enumeration of BmH x ⊴ b means x ▹ b or x “ bH and b ∈ BmC
Un other wordsH the greedy orderqideals are the nonempty initial segments of greedy
enumerationsC The smallest greedy orderqideal is {T} jtake b “ Tx while the largest
is Bm jtake b “ ’xC The trst part of the following lemma justites our terminologyC

AVERAGING FOR FRANKL8S CONJECTURE 11

3e
2e
 9e 13`e

10e 11e
 15e
14e

12e

5e

4e
 8e

1c

2c 3c 5c
7c
6c
4c
 8c
 6e 7e

1e

Figure 1

Lemma 10. Let X be a greedy order-ideal of Bm. Then X is an order-ideal of
Bm, and its total height is

hjXx“ yj⃗w9m), ’, |X|x , whence hjXx“ Ej⃗w9m), ’,. .., |X|x .

The trivial induction proving this lemma is left to the readerC ﬀowH let a1H a2H
.. .H am still be a txed enumeration of the atoms of BmC;or j “’,. .. , m we detne
the interval Ij “[aj,a
′
1 ∧ {{{ ∧ a
′
j−1] .

Un particularH I1 “[a1, ’] ↑“ Bm−1H Im “[am,a
′
1 ∧ {{{ ∧ a
′
m−1]“ [am,am] ↑“ B0H
and in generalH Ij ↑“ Bm−j C Un the rightqhand lattice in ;igure ’H if we start with
the a1 “ e1H a2 “ e9H a3 “ e13H a4 “ e15 enumeration jiCeCH from left to right
enumerationx of atomsH we have I1 “[e1,e8]H I2 “[e9,e12]H I3 “[e13,e14] and
I4 “ {e15}C ﬀotice that {I1,. .. , Im} is a partition of Bm \{T}C
The sequence I1,I2,. .. , Im is called a standard interval sequence of Bm4 there
are mI such sequencesH for there are mI enumerations of the atomsC ﬀowH by a
greedy semi-ideal of Bm we mean a nonempty subset X of the form

jRx X “ I1 ∪ {{{ ∪ Ik−1 ∪ U

where U is a greedy orderqideal of IkC jEence U ̸“ ∅ but U “ Ik is permittedCx The
unique k ∈{’,. .. , m} in jRx is said to be the rank of the greedy semi-ideal XH and
it will be denoted by rankjXxC

Lemma 11. Let X · Bm be a greedy semi-ideal of Bm. Then it is indeed a
semi-ideal, and its total height is

hjXx“ yj⃗/9m), ’, |X|x, whence hjXx“ Ej⃗/9m), ’,. .., |X|x .

Ut follows from 6emmas ’T and ’’ that for each n ↦ B
m respC k< B
mH Bm includes
a greedy orderqideal respC greedy semiqideal of size n respC k4 this observation will
be relevant in the following proofsC
The following lemma is presented not only for its own interest4 it will be used in
the next sectionC

Lemma 12. Let X and Y be order-ideals of Bm such that |X| “ |Y | and Y is
greedy. Then hjXx ↦ hjY x, i.e., hjXx ↦ hjY x.

Proof. We prove the lemma via induction on mC We can assume that m • BC 6et
X be an orderqideal of BmC Ut susces to construct a greedy orderqideal U such that
|U | “ |X| and hjXx ↦ hjU xC We can jand often willx change X during the proof so

12 G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

that hjXx does not decrease and |X| remains the sameC ﬀowH for later referenceH
we formulate four facts4 they are evident consequences of detnitionsC UfH for someH Y is a greedy orderqideal of B

k and Z is an orderqideal of Bk then
j;act ’x |Y |• B
k−1 implies that Y contains a coatom of Bk4
j;act Bx |Y |↦ B
k−1 implies Y ·↓c for some coatom c of Bk4
j;act ˇx if Z contains a coatom d
′ ∈ Bk and Z ∩↑d is a greedy orderqideal of ↑d
then Z is a greedy orderqideal of Bk jhere d “ d
′′ is an atomx4
j;act Mx ’ ↦ j ↦|Y | implies that Bk has a jqelement greedy orderqideal which
is a subset of Y C
ﬀowH if there is an atom a ∈ Bm \ X then X is an orderqideal in ↓a
′H a Soolean
lattice with m − ’ atomsH whence the induction hypothesis yields an appropriate U
in ↓a
′H which is a greedy orderqideal in Bm as wellC Eence we can assume that X
contains all the atoms of BmC
6et a ∈ Bm be an atomC Since Bm is a disjoint union of ↑a and ↓a
′H X is the
disjoint union of G
′ 0“ X ∩↓a
′ and G 0“ X ∩↑aC j;igure BH where G
′ “ G
′
2 ∪↓pH
depicts a particular but important caseCx Sy the isomorphism theorem of intervalsH

1

0
 b a

p
 a’ b’
B   :m
 2 G
G’

Figure 2

I 0 ↓a
′ →↑a, x ↦→ x ∨ a and B 0 ↑a →↓a
′,x ↦→ x ∧ a
′

are reciprocal isomorphismsC We know ’ ↦|G| from the latest assumptionC The
injectivity of B and the fact that Bjxx ↦ x ∈ X gives Bjxx ∈ G
′ for any x ∈ G
show that |G|↦ |G
′|C
We can assume that G
′ respC G is a greedy orderqideal of ↓a
′ respC ↑a such that
BjGx · G
′C jThen G ∪ G
′ is necessarily an orderqidealH so it is still denoted by
XCx UndeedH if this is not the case thenH instead of G and G
′H we could use H and
H ′ obtained as followsC ;irst the induction hypothesis allows us to replace G
′ by a
greedy orderqideal H ′ of ↓a
′ with |G
′| “ |H ′| and hjG
′x ↦ hjH ′xC VlearlyH IjH ′xis
a greedy orderqideal of ↑aH and ;act M gives a greedy orderqideal H of ↑a such that
|H| “ |G| and H · IjH ′xC Since hjGx ↦ hjHx by the induction hypothesisH H and
H ′ do the jobC
There are three casesC ;irst we assume that B
m−2 ↦|G| or B
m−1 ↦|X|CWe
have B
m−1 ↦|X| in both casesH for |G|↦ |G
′|C Sy ;act ’H there is an atom q ∈ Bm

AVERAGING FOR FRANKL8S CONJECTURE 13

such that ↓q′ · XC Sy the induction hypothesisH there exists a subset Y with
|Y | “ |X ∩↑q| and hjY x • hjX ∩↑qx such that either Y is empty or it is a greedy
orderqideal of ↑qC We can let U “ Y ∪↓q′H which does the job by ;act ˇC
The case when |G
′|↦ B
m−2 is even simplerC UndeedH G
′ ·↓p for some coatom
p of ↓a
′ by ;act BC 6et q “ IjpxH which is a coatom of BmC VlearlyH X ·↓qC
Npplying the induction hypothesis to ↓q we obtain a greedy orderqideal U in ↓q
with hjXx ↦ hjU x and |X| “ |U |H and U does the job in BmH tooC
So we are left with the case depicted in ;igure B4 namelyH let |G| < B
m−2 < |G
′|
and |X| < B
m−1C Sy ;act ’ we can choose an atom b ∈↓a
′ such that its complement
p taken in ↓a
′ belongs to G
′C ﬀotice that p “ a
′ ∧ b
′ “ Bjb
′xC We can assume that
G · [a, b
′]H for otherwise G can be replaced by a |G|qelement greedy orderqideal of
[a, b
′]C 6et G
′
2 “ G
′ ∩ [b, a′]H i “ |G
′
2|H j “ |G|H andH to prepare an application of
6emma M for n “ m − BH let u 0“ i z j and v 0“ TC Since |X| < B
m−1H u< B
m−2C
Vhoose a uqelement greedy orderqideal H ′
2 in [b, a′]C ThenH by ;act ˇH U 0“ H ′
2 ∪↓p
is a greedy orderqideal of ↓a
′H whence U is a greedy orderqideal of BmC ;inallyH
6emmas M and ’T yield hjXx“ hj↓pxz hjG
′
2xz hjGx“ hj↓pxz yj⃗x9m−2), ’,ixz
yj⃗x9m−2), ’,jx ↦ hj↓pxz yj⃗x9m−2), ’,uxz yj⃗x9m−2), ’, Tx “ hj↓pxz hjH ′
2xzT “
hjU xC ⊴

Lemma 13. Assume that Frankl1s conjecture holds over m-element base sets. Then
hjXx ↦ Ej⃗/9m), ’,. .., |X|x for each semi-ideal X of Bm.

Proof. We prove the lemma via induction on mC 6et X be a semiqideal of BmC
Nccording to 6emma ’’H it susces to tnd a greedy semiqideal Y of Bm such that
|X| “ |Y | and hjXx ↦ hjY xC Part jˇx of 6emma R allows us to tx an enumeration
a1,. .. , am of the atoms in Bm such that with the notations

X0 “ X ∩↓a
′
m,X1 “jX ∩↑amx \{am},X2 “ X ∩{am}

we have |X1| z |X2|↦ |X0|C ﬀote that X “ X0 ∪ X1 ∪ X2 and Xi ∩ Xj “ ∅ for
T ↦ i<j ↦ BC
VlearlyH X0 is a semiqideal of ↓a
′
m ↑“ Bm−1C To see that X1 is a semiqideal of
↑am ↑“ Bm−1H let x ∈ X1C Then there is an atom p ∈ Bm with [p, x] · XCUf p ̸“ am
then p ∨ am is an atom of ↑am and [p ∨ am,x] · X1CUf p “ am then for each atom
q of ↑amH[q, x] · X1C Therefore X1 is indeed a semiqideal of ↑amC
ﬀow let I1,. .. , Im−1 be the standard interval sequence of ↓a
′
m determined by the
enumeration a1,. .. , am−1 of its atomsC SimilarlyH let J1,. .. , Jm−1 be the standard
interval sequence of ↑am determined by the enumeration a1 ∨ am,. .. , am−1 ∨ am of
its atomsC ﬀotice that the mappings

Ij 0 Ij → Jj,x ↦→ x ∨ am and Bj 0 Jj → Ij,x ↦→ x ∧ a
′
m

are reciprocal lattice isomorphisms for each j ∈{’,. .., m − ’}C Un factH they are
the restrictions of the reciprocal isomorphisms

I 0 ↓a
′
m →↑am,x ↦→ x ∨ am and B 0 ↑am →↓a
′
m,x ↦→ x ∧ a
′
m .

ﬀow let Y0 “ I1 ∪ {{{ ∪ Ik−1 ∪ U

be a greedy semiqideal of ↓a
′
m jof rank kx such that |Y0| “ |X0|C Eere U denotes a
greedy orderqideal of IkC Since |X1|↦ |X0|H we can choose a greedy semiqideal Y1

14 G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

of ↑am such that |Y1| “ |X1| and BjY1x · Y0 jcfC ;act M from the previous proofxC
6et ℓ be the rank of Y1C Then ℓ ↦ k and Y1 is of the form

Y1 “ J1 ∪ {{{ ∪ Jℓ−1 ∪ V,

where V is a greedy orderqideal of JℓC The induction hypothesis gives hjX0x ↦ hjY0x
and hjX1x ↦ hjY1xH whence hjXx ↦ hjY0 ∪ Y1 ∪ X2xC ﬀotice that

K1 “ I1 ∪ J1,K2 “ I2 ∪ J2,. . . , Km−1 “ Im−1 ∪ Jm−1,Km “ {am}

is the standard interval sequence of Bm associated with the enumeration a1,. .. , am
of its atomsC

;irst we consider the case when k “ ℓ4 the situation for k “ ℓ “ ˇ is outlined
in ;igure ˇC Since U is a jgreedyx orderqideal of IkH V is an orderqideal of Jk and

B   :m
 m

1
 1

0
 a

ma’
 a
2a
3a
 1I
2I V

U
 1J

2J

Figure 3

BkjV x · U H we conclude that U ∪ V is an orderqideal of Kk “ Ik ∪ JkC 6et W be
a greedy orderqideal of Kk such that |W | “ |U | z |V | “ |U ∪ V |C We know from
6emma ’B that hjU ∪ V x ↦ hjW xC VlearlyH

Z 0“ jI1 ∪ J1x ∪{ { {∪ jIk−1 ∪ Jk−1x ∪ W “ K1 ∪ {{{ ∪ Kk−1 ∪ W

is a greedy semiqideal of BmH and we have hjY0 ∪ Y1x ↦ hjZxC Uf X2 “ ∅H iCeC
am /∈ XH then |X| “ |Z| and hjXx“ hjX0xz hjX1x ↦ hjY0xz hjY1x ↦ hjZxH as
requestedC Un case of am ∈ X we need an easy further step0 let Z + be a greedy
semiqideal of Bm such that Z · Z + and |Z +| “ |Z| z ’C Then

hjXx“ hjX0xz hjX1xz hjamx ↦ hjY xz’ ↦ hjZxz’ ↦ hjZ ′x

together with |X| “ |Z +| settles the case k “ ℓC

The general case is when rankjY0x“ k • ℓ “ rankjY1xC This will be settled by
an induction on k − ℓC;or k − ℓ “ T the job has already been doneC ﬀow assume
that k − ℓ> T4 the situation for jk, ℓx“ jM, Bx is outlined in ;igure MC We are going
to detne a pair jT0,T1x of greedy semiqideals with the same properties as those
assumed for jY0,Y1x such that rankjT0x − rankjT1x <k − ℓC

AVERAGING FOR FRANKL8S CONJECTURE 15

B   :m
 m

1
 0
 a

ma’
 3a
4a 2a 1a

1I

3I 2I V

U
 1J

3J 2J

4J

4I
 Figure 4

Ns an intermediate step we detne a greedy semiqideal R0 of ↓a
′
m and a greedy
semiqideal R1 of ↑amC 6et i “ |U | and j “ |V |C Un order to harmonize with the
notations of 6emma MH detne u “ i z j if i z j ↦ B
m−ℓ−1 “ |Jℓ| and let u “ |Jℓ|
otherwiseC 6et v “ i z j − uC ﬀow let R1 “ J1 ∪ {{{ ∪ Jℓ−1 ∪ V + where V + is a
uqelement greedy orderqideal of JℓC 6et U − be a vqelement subset of Ik such that
U − is a greedy orderqideal of Ik when v> TC Then R0 “ I1 ∪ {{{ ∪ Ik−1 ∪ U −C
;inallyH if V + “ Jℓ and U − ̸“ ∅ then let T0 “ R0 \ U −H and add v “ |U −|
many new elements to R1 to obtain the greedy semiqideal T1 of ↑amC jThese new
elements will of course go into Jℓ+1Cx Un the other case when V + ≺ Jℓ or U − “ ∅H
we simply let jT0,T1x“ jR0,R1xC
VlearlyH we have |Y0 ∪ Y1| “ |T0 ∪ T1| and rankjY0x − rankjY1x > rankjT0x −
rankjT1xC So we are left with the duty of showing hjY0xz hjY1x ↦ hjT0xz hjT1xC
Ut follows from 6emmas M and ’T that

hIkjU xz hJℓ jV x ↦ hIkjU −xz hJℓ jV +x .

ThereforeH measuring the total height in Bm rather than in Ik and JℓH we conclude

hjU xz |U | z hjV xz B|V |↦ hjU −xz |U −| z hjV +xz B|V +|,

which implies hjU xz hjV x ↦ hjU −xz hjV +xH for |U −| z |V +| “ |U | z |V | and
|V |↦ |V +|C Therefore hjY0xz hjY1x ↦ hjR0xz hjR1xC ;inallyH hjR0xz hjR1x ↦
hjT0xz hjT1x is evidentC ⊴

´C The end of the proof and two conjectures

ﬀow Theorem ’ follows from 6emmas ]H ’’ and ’ˇC ;inallyH 6emma R guarantees
that Theorem ’ implies the 8ain TheoremC

We conclude the paper with two conjecturesC Nlthough they are formulated
in terms of lattice theoryH which goes well with the present paperH they will be
translated to pure combinatorial language afterwardsC

⌊ ;or each semiqideal X of BmH hjXx ↦ Ej⃗/9m), ’,. .., |X|xC

16 G TABOR CZ TEDLI, MIKL TOS MAR TOTI, AND E. TAM TAS SCHMIDT

⌊ There is a function fjmx such that fjmx/B
m/2 tends to ∞ and hjXx ↦ m/B
for every semiqideal X · Bm with |X|↦ fjmxC

Nccording to 6emma ’ˇ and Theorem ’H a positive solution of ;ranklgs conjecture
would solve both problems in the asrmativeC EoweverH these conjectures might be
easier jto prove or refutex than ;ranklgs oneC
The ideas of 6emma R lead easily to the following combinatorial interpretation
of the trst conjectureC ﬂiven ’ ↦ k ↦ B
|A|H we want to tnd a unionqclosed family
FH ∅∈ F · P jAxH such that wjFx be minimalC The conjecture asserts that we
can obtain such an F by the obvious greedy algorithm in B|A| − k stepsH starting
from F0 “ P jAx and deleting just one member of Fi−1 in the ith stepC ﬀote that
Sohsnjak and 8arkovirc [´] settle the trst conjecture for m ↦ ’’C
N positive solution of the second conjecture would simply say that even if we
cannot leave the assumption “;ranklgs conjecture holds over mqelement setsP out
of the 8ain TheoremH the averaged ;ranklgs property holds for unionqclosed sets
which are “essentiallyP larger than those treated in [5] jand mentioned in the Unq
troductionCx
 References

[w] Tetsuya 6be3 Excess of a latticeg zraphs and –ombinatorics 18 rxkkx(g 0’v–pkx9
[x] Tetsuya 6be3 Strong semimodular lattices and Franklbs conjectureg 6lgebra Universalis 44
rxkkk(g 0[’–0]x9
[0] Tetsuya 6be and 5umpei Nakano3 VranklFs conjecture is true for modular latticesg zraphs
and –ombinatorics 14 rw’’](g 0kv–0ww9
[p] Tetsuya 6be and 5umpei Nakano3 Lower semimodular types of lattices: Franklbs conjecture
holds for lower quasiIsemimodular latticesg zraphs and –ombinatorics 16 rxkkk(g no9 wg w–wﬁ9
[v] W9 5oHsnjak and P9 Markovi.c3 The ,,Ielement case of Franklbs conjectureg Plectron9 q9 –ombin9
15 rxkk](g no9 wg Research Paper ]]g w[ pp9
[ﬁ] P9 5rown and T9 P9 Vaughan3 Conegurations with subset restrictionsg q9 –ombin9 Math9
–ombin9 –omput9 48 rxkkp(g w’[–xwv9
[[] z9 –z.edli3 On averaging VranklFs conjecture for large union1closed setsg qournal of –ombina1
torial Theory 1 Series 6g to appear9
[]] Y9 ˇohmen3 A new perspective on the unionIclosed sets conjectureg 6rs9 –ombin9 58 rxkkw(g
w]0–w]v9
[’] ˇ9 ˇuLus and 59 Sands3 An inequality for sizes of prime elters of enite distributive latticesg
ˇiscrete Math9 201 rw’’’(g ]’–’’9
[wk] M9 Pl1Zahar3 A graphItheoretic version of the unionIclosed sets conjectureg q9 zraph Theory
26 rw’’[(g wvv–wﬁ09
[ww] /9 V9 Vitina and q1–9 Renaud3 On unionIclosed sets and Conwaybs sequenceg 5ull9 6ustral9
Math9 Soc9 47 rw’’0(g 0xw–00x9
[wx] P9 Vrankl3 Extremal set systemsU Handbook of combinatoricsg Vol. 1, 2g wx’0–w0x’g Plsevierg
6msterdamg w’’v9
[w0] Weidong zao and ﬀongquan Yu3 Note on the unionIclosed sets conjectureg 6rs –ombin9 49
rw’’](g x]k–x]]9
[wp] –9 ﬀerrmann and R9 /angsdorf3 Franklbs conjecture for lower semimodular latticesg
http377www9mathematik9tu1darmstadt9de3]k]k7∼herrmann7recherche7
[wv] R9 T9 qohnson and T9 P9 Vaughan3 On unionIclosed familiesU Ig q9 –ombin9 Th9 Ser9 6 84
rw’’](g xpx–xp’9
[wﬁ] z9 /o Varo3 UnionIclosed sets conjecture: improved boundsg q9 –ombin9 Math9 –ombin9
–omput9 16 rw’’p(g ’[–wkx9
[w[] z9 /o Varo3 A note on the unionIclosed sets conjectureg q9 6ustral Math9 Soc9 Ser9 6 57
rw’’p(g x0k–x0ﬁ9
[w]] P9 Markovi.c3 An attempt at Franklbs conjectureg Publ9 Wnst9 Math9 r5eograd( rN9S9( 81(95)
rxkk[(g x’–p09
 AVERAGING FOR FRANKL8S CONJECTURE 17

[w’] R9 Morris3 FCIfamilies and improved bounds for Franklbs conjectureg Puropean q9 –ombin9
27 rxkkﬁ(g xﬁ’–x]x9
[xk] T9 Nishimura and S9 Takahashi3 Around Franklbs conjectureg Sci9 Rep9 Yokohama Nat9 Univ9
Sect9 Math9 Phys9 –hem9 43 rw’’ﬁ(g wv–x09
[xw] R9 M9 Norton and ˇ9 z9 Sarvate3 A note of the unionIclosed sets conjectureg q9 6ustral9
Math9 Soc9 Ser9 6 55 rw’’0( pww–pw09
[xx] 59 Poonen3 UnionIclosed familiesg q9 –ombinatorial Theory 6 59 rw’’x(g xv0–xﬁ]9
[x0] ˇ9 Reimer3 An average set size theoremg –ombin9 Probab9 and –omput9 12 rxkk0(g ]’–’09
[xp] q9 Reinhold3 Franklbs conjecture is true for lower semimodular latticesg zraphs and –ombi1
natorics 16 rxkkk(g wwv–wwﬁ9
[xv] q1–9 Renaud3 Is the unionIclosed sets conjecture the best possible?g q9 6ustral Math9 Soc9
Ser9 6 51 rw’’w(g x[ﬁ–x]09
[xﬁ] q1–9 Renaud3 A second approximation to the boundary function on unionIclosed collectionsg
6rs9 –ombin9 41 rw’’v(g w[[1w]]9
[x[] q1–9 Renaud and ˇ9 z9 Sarvate3 On the unionIclosed sets conjectureg 6rs –ombin9 27 rw’]’(g
wp’–wv09
[x]] q1–9 Renaud and ˇ9 z9 Sarvate3 Improved bounds for the unionIclosed sets conjectureg 6rs
–ombin9 29 rw’’k(g w]w–w]v9
[x’] W9 Rival red(3 Graphs and Orderg N6TO 6dvanced Sci9 Wnst9 Ser9 –3 Math9 and Phys9 Sciences
147g ˇ9 Reidel Publ9 –o9 ˇordrecht–5oston rw’]v(g p9 vxv9
[0k] W9 Robertsg Tech9 Rep9 No9 x7’xg School Math9 Stat9g –urtin Univ9 Tech9g Perthg w’’x9
[0w] R9 P9 Stanley3 Enumerative CombinatoricsN VolU IUg 5elmontg –63 Wadsworth and
5rooks7–ooleg w’]ﬁ9
[0x] T9 P9 Vaughan3 Families implying the Frankl conjectureg Puropean q9 –ombin9 23 rxkkx(g
]vw–]ﬁk9
[00] T9 P9 Vaughan3 A note on the unionIclosed sets conjectureg q9 –ombin9 Math9 –ombin9
–omput9 45 rxkk0(g ’v–wk]9
[0p] T9 P9 Vaughan3 TreeIsets in a unionIclosed familyg q9 –ombin9 Math9 –ombin9 –omput9 49
rxkkp(g [0–]p9
[0v] P9 Winkler3 UnionIclosed sets conjectureg 6ustral9 Math9 Soc9 zaz9 ,R rw’][(g p9 ’’9
[0ﬁ] P9 W.ojcik3 Density of unionIclosed familiesg ˇiscrete Math9 105 rw’’x(g xv’–xﬁ[9
[0[] http377www9math9uiuc9edu7 west7openp7unionclos9html

University of Szeged˝ Bolyai Institute˝ Szeged˝ Aradi vgertanguk tere 1˝ HUNGARY
6720
EImail address3 czedli@math.u-szeged.hu
URL3 http://www.math.u-szeged.hu/∼czedli/

University of Szeged˝ Bolyai Institute˝ Szeged˝ Aradi vgertanguk tere 1˝ HUNGARY
6720
EImail address3 mmaroti@math.u-szeged.hu
URL3 http://www.math.u-szeged.hu/∼mmaroti/

Mathematical Institute of the Budapest University of Technology and Economics˝
M˝uegyetem rkp- 3˝ H31521 Budapest˝ Hungary
EImail addressg P9 T9 Schmidt3 schmidt@math.bme.hu
URL3 http://www.math.bme.hu/∼schmidt/
