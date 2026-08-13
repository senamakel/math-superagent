<!-- source: https://www.cirm-math.fr/RepOrga/2077/Slides/Stoll.pdf | converted from PDF -->

On a problem of Erd ˝os concerning the digits of 2n in base 3
– and Hensel’s lemma

Thomas Stoll

CIRM, 08/11/2019

in memoriam Christian Mauduit

joint work with H. Kaneko (Tsukuba, Japan)

Université de Lorraine / Institut Élie Cartan de Lorraine
 1

Motivation - original problem

Erd ˝os squarefree conjecture

Erd ˝os squarefree conjecture: The central binomial coefﬁcient (
2n
n ) is never
squarefree for n > 4.
 Solved.

Proved :

• by Sark ˝ozy (1985) for all sufﬁciently large n and,

• independently, by Granville and Ramaré (1996) and Velammal (1995) for
all n > 4.

Since 4 | (
2n
n ) for n ̸= 2k it is sufﬁcient to study (
2k +1

2k )
.

2

Erd ˝os squarefree conjecture

Erd ˝os squarefree conjecture: The central binomial coefﬁcient (
2n
n ) is never
squarefree for n > 4.

Solved.

Proved :

• by Sark ˝ozy (1985) for all sufﬁciently large n and,

• independently, by Granville and Ramaré (1996) and Velammal (1995) for
all n > 4.

Since 4 | (
2n
n ) for n ̸= 2k it is sufﬁcient to study (
2k +1

2k )
.
 2

Erd ˝os squarefree conjecture’

Erd ˝os squarefree conjecture’ : The central binomial coefﬁcient (
2n
n ) is
divisible by 4 or 9 for every n > 4 except n = 64 and n = 256.
 Unsolved !

• Goetgheluck (1988): True for n ≤ 2
4.2·10
7 .

• Holdum, Klausen, and Rasmussen (2015) : True for n ≤ 2
10
13 ; the set of
k such that 9 does not divide (
2
k +1

2k ) is of density 0.

3

Erd ˝os squarefree conjecture’

Erd ˝os squarefree conjecture’ : The central binomial coefﬁcient (
2n
n ) is
divisible by 4 or 9 for every n > 4 except n = 64 and n = 256.

Unsolved !

• Goetgheluck (1988): True for n ≤ 2
4.2·10
7 .

• Holdum, Klausen, and Rasmussen (2015) : True for n ≤ 2
10
13 ; the set of
k such that 9 does not divide (
2
k +1

2k ) is of density 0.
 3

⇐=

P. Erd ˝os, Some Unconven-
tional Problems in Number
Theory, Math. Mag. 52 (1979),
pp. 67–70.
 4

Erd ˝os’ approach (to the squarefree conjecture):

• Kummer’s theorem (1852): for p prime,

pm ||
 (2
k +1

2k
 )
 ⇔ m = #carries when adding 2
k + 2
k in base p.
 • 3 does not divide (
2k +1

2k ) ⇔ the ternary expansion of 2
n omits the digits 2.

“ I conjecture that for k > 8, 2
k is not the sum of distinct powers of 3 [...] but
as far as I see there is no method at our disposal to attack this conjecture.”
(Erd ˝os ternary digits conjecture)

5

Erd ˝os’ approach (to the squarefree conjecture):

• Kummer’s theorem (1852): for p prime,

pm ||
 (2
k +1

2k
 )
 ⇔ m = #carries when adding 2
k + 2
k in base p.

• 3 does not divide (
2k +1

2k ) ⇔ the ternary expansion of 2
n omits the digits 2.
 “ I conjecture that for k > 8, 2
k is not the sum of distinct powers of 3 [...] but
as far as I see there is no method at our disposal to attack this conjecture.”
(Erd ˝os ternary digits conjecture)

5

Erd ˝os’ approach (to the squarefree conjecture):

• Kummer’s theorem (1852): for p prime,

pm ||
 (2
k +1

2k
 )
 ⇔ m = #carries when adding 2
k + 2
k in base p.

• 3 does not divide (
2k +1

2k ) ⇔ the ternary expansion of 2
n omits the digits 2.

“ I conjecture that for k > 8, 2
k is not the sum of distinct powers of 3 [...] but
as far as I see there is no method at our disposal to attack this conjecture.”
(Erd ˝os ternary digits conjecture)
 5

Examples
 n 2n (2n)3
0 1 1 20 = 30

1 2 2
2 4 11 22 = 31 + 30

3 8 22
4 16 121
5 32 1012
6 64 2101
7 128 11202
8 256 100111 28 = 35 + 32 + 31 + 30

9 512 200222
10 1024 1101221
11 2048 2210212
12 4096 12121201
 Heuristically:

≈ ∑

n
 ( 2
3
 )length of expansion of 2
n in base 3 ≈ ∑

n
 ( 2
3
 )n log 2
log 3 < ∞.

6

Examples
 n 2n (2n)3
0 1 1 20 = 30

1 2 2
2 4 11 22 = 31 + 30

3 8 22
4 16 121
5 32 1012
6 64 2101
7 128 11202
8 256 100111 28 = 35 + 32 + 31 + 30

9 512 200222
10 1024 1101221
11 2048 2210212
12 4096 12121201

Heuristically:

≈ ∑

n
 ( 2
3
 )length of expansion of 2
n in base 3 ≈ ∑

n
 ( 2
3
 )n log 2
log 3 < ∞.
 6

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}.
 Widely open !

. . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞. Widely open !

. . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !

. . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).

7

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}. Widely open !
 . . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞. Widely open !

. . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !

. . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).

7

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}. Widely open !

. . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞.
 Widely open !

. . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !

. . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).

7

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}. Widely open !

. . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞. Widely open !
 . . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !

. . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).

7

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}. Widely open !

. . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞. Widely open !

. . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !

. . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).

7

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}. Widely open !

. . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞. Widely open !

. . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !
 . . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).

7

Conjectures

Erd ˝os ternary digits conjecture:
{n : (2n)3 does not contain any digit “2”} = {0, 2, 8}. Widely open !

. . . - weak form:
#{n : (2
n)3 does not contain any digit “2”} < ∞. Widely open !

. . . - even weaker form:
#{n < x : (2
n)3 does not contain any digit “2”} = o(x log 2/ log 3).
 Widely open !

. . . - ﬂexible form:
#{n < x : (2
n)3 contains at most ψ1(n) digits “2”} ≤ ψ2(x).
 7

Results

• Gupta (1978):

{n < 4374 : (2n)3 does not contain any digit “2”} = {0, 2, 8}.
 • Narkiewicz (1980):

#{n < x : (2
n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Kennedy/Cooper (2001): a, b integers with (a, b) = 1, then

#{n < x : (an)b does not contain any digit ≥ “b/2”} ≤ Cbx log((b+1)/2)/ log b.

• Holdun/Klausen/Rasmussen (2015): improvements of the
multiplicative constants in Narkiewicz (1980) and Kennedy/Cooper
(2001).

8

Results

• Gupta (1978):

{n < 4374 : (2n)3 does not contain any digit “2”} = {0, 2, 8}.

• Narkiewicz (1980):

#{n < x : (2
n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.
 • Kennedy/Cooper (2001): a, b integers with (a, b) = 1, then

#{n < x : (an)b does not contain any digit ≥ “b/2”} ≤ Cbx log((b+1)/2)/ log b.

• Holdun/Klausen/Rasmussen (2015): improvements of the
multiplicative constants in Narkiewicz (1980) and Kennedy/Cooper
(2001).

8

Results

• Gupta (1978):

{n < 4374 : (2n)3 does not contain any digit “2”} = {0, 2, 8}.

• Narkiewicz (1980):

#{n < x : (2
n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Kennedy/Cooper (2001): a, b integers with (a, b) = 1, then

#{n < x : (an)b does not contain any digit ≥ “b/2”} ≤ Cbx log((b+1)/2)/ log b.
 • Holdun/Klausen/Rasmussen (2015): improvements of the
multiplicative constants in Narkiewicz (1980) and Kennedy/Cooper
(2001).

8

Results

• Gupta (1978):

{n < 4374 : (2n)3 does not contain any digit “2”} = {0, 2, 8}.

• Narkiewicz (1980):

#{n < x : (2
n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Kennedy/Cooper (2001): a, b integers with (a, b) = 1, then

#{n < x : (an)b does not contain any digit ≥ “b/2”} ≤ Cbx log((b+1)/2)/ log b.

• Holdun/Klausen/Rasmussen (2015): improvements of the
multiplicative constants in Narkiewicz (1980) and Kennedy/Cooper
(2001).
 8

Proof of Narkiewicz (1980)

Narkiewicz (1980):

#{n < x : (2n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.
 • Write 2
n = 3
m0 + 3
m1 + · · · + 3
ms

with 0 = m0 < m1 < · · · < ms.

• Reduce modulo 3
k . Then the RHS takes one of the 2
k −1 values

1 + ε1 · 3 + · · · + εk −1 · 3
k −1, εi ∈ {0, 1}.

• Thus, 2
k −1 possibilities for 2
n (mod 3
k ).

• 2 is primitive root for every power of 3, there are only 2
k −1 residue
classes mod 2 · 3k −1 in which n can lie.

• Count.

9

Proof of Narkiewicz (1980)

Narkiewicz (1980):

#{n < x : (2n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Write 2
n = 3
m0 + 3
m1 + · · · + 3
ms

with 0 = m0 < m1 < · · · < ms.
 • Reduce modulo 3
k . Then the RHS takes one of the 2
k −1 values

1 + ε1 · 3 + · · · + εk −1 · 3
k −1, εi ∈ {0, 1}.

• Thus, 2
k −1 possibilities for 2
n (mod 3
k ).

• 2 is primitive root for every power of 3, there are only 2
k −1 residue
classes mod 2 · 3k −1 in which n can lie.

• Count.

9

Proof of Narkiewicz (1980)

Narkiewicz (1980):

#{n < x : (2n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Write 2
n = 3
m0 + 3
m1 + · · · + 3
ms

with 0 = m0 < m1 < · · · < ms.

• Reduce modulo 3
k . Then the RHS takes one of the 2
k −1 values

1 + ε1 · 3 + · · · + εk −1 · 3
k −1, εi ∈ {0, 1}.
 • Thus, 2
k −1 possibilities for 2
n (mod 3
k ).

• 2 is primitive root for every power of 3, there are only 2
k −1 residue
classes mod 2 · 3k −1 in which n can lie.

• Count.

9

Proof of Narkiewicz (1980)

Narkiewicz (1980):

#{n < x : (2n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Write 2
n = 3
m0 + 3
m1 + · · · + 3
ms

with 0 = m0 < m1 < · · · < ms.

• Reduce modulo 3
k . Then the RHS takes one of the 2
k −1 values

1 + ε1 · 3 + · · · + εk −1 · 3
k −1, εi ∈ {0, 1}.

• Thus, 2
k −1 possibilities for 2
n (mod 3
k ).
 • 2 is primitive root for every power of 3, there are only 2
k −1 residue
classes mod 2 · 3k −1 in which n can lie.

• Count.

9

Proof of Narkiewicz (1980)

Narkiewicz (1980):

#{n < x : (2n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Write 2
n = 3
m0 + 3
m1 + · · · + 3
ms

with 0 = m0 < m1 < · · · < ms.

• Reduce modulo 3
k . Then the RHS takes one of the 2
k −1 values

1 + ε1 · 3 + · · · + εk −1 · 3
k −1, εi ∈ {0, 1}.

• Thus, 2
k −1 possibilities for 2
n (mod 3
k ).

• 2 is primitive root for every power of 3, there are only 2
k −1 residue
classes mod 2 · 3k −1 in which n can lie.
 • Count.

9

Proof of Narkiewicz (1980)

Narkiewicz (1980):

#{n < x : (2n)3 does not contain any digit “2”} ≤ 1.62 x log 2/ log 3.

• Write 2
n = 3
m0 + 3
m1 + · · · + 3
ms

with 0 = m0 < m1 < · · · < ms.

• Reduce modulo 3
k . Then the RHS takes one of the 2
k −1 values

1 + ε1 · 3 + · · · + εk −1 · 3
k −1, εi ∈ {0, 1}.

• Thus, 2
k −1 possibilities for 2
n (mod 3
k ).

• 2 is primitive root for every power of 3, there are only 2
k −1 residue
classes mod 2 · 3k −1 in which n can lie.

• Count.
 9

Linear forms in logarithms

• Stewart (1980): Let a, b be multiplicatively independent. Then there
exists C = C(a, b) such that for all n ≥ n0,

(# digits ̸= α of (n)a ) + (# digits ̸= β of (n)b) ≥ log log n
log log log n + C .
 Apply for (a = 2, n → 2n, α = 0, and b = 3, β = 0):

(# digits = 1 of (2n)3 ) + (# digits = 2 of (2n)3 ) ≥ c log n
log log n , n ≥ n0.

The number of non-zero digits in (2
n)3 is unbounded.

No information on the individual count of the 1’s and 2’s.

10

Linear forms in logarithms

• Stewart (1980): Let a, b be multiplicatively independent. Then there
exists C = C(a, b) such that for all n ≥ n0,

(# digits ̸= α of (n)a ) + (# digits ̸= β of (n)b) ≥ log log n
log log log n + C .

Apply for (a = 2, n → 2n, α = 0, and b = 3, β = 0):

(# digits = 1 of (2n)3 ) + (# digits = 2 of (2n)3 ) ≥ c log n
log log n , n ≥ n0.

The number of non-zero digits in (2
n)3 is unbounded.
 No information on the individual count of the 1’s and 2’s.

10

Linear forms in logarithms

• Stewart (1980): Let a, b be multiplicatively independent. Then there
exists C = C(a, b) such that for all n ≥ n0,

(# digits ̸= α of (n)a ) + (# digits ̸= β of (n)b) ≥ log log n
log log log n + C .

Apply for (a = 2, n → 2n, α = 0, and b = 3, β = 0):

(# digits = 1 of (2n)3 ) + (# digits = 2 of (2n)3 ) ≥ c log n
log log n , n ≥ n0.

The number of non-zero digits in (2
n)3 is unbounded.

No information on the individual count of the 1’s and 2’s.
 10

Average results

Let dn,m be the number of digits “2” within the ﬁrst m digits a0, a1, . . . am−1 of
2n in base 3,

2
n = a0 + a1 · 3 + · · · + am−1 · 3m−1 + · · · + aN · 3
N , N ≈ n · log 2
log 3

• lim
n→∞ dn,N
N = 1
3 or lim
n→∞ dn,mn
mn = 1
3 ,

for some suitable mn → ∞, mn monotone, would prove Erd ˝os ternary
digits conjecture (weak form).
 • Dupuy et Weirich (2016):

lim
m→∞ lim
N→∞ 1
N
 N∑

n=1
 dn,m
m = 1
3 .

• Yu (2018+):
 lim
N→∞ 1
N
 N∑

n=1
 dn,mn
mn = 1
3 .

11

Average results

Let dn,m be the number of digits “2” within the ﬁrst m digits a0, a1, . . . am−1 of
2n in base 3,

2
n = a0 + a1 · 3 + · · · + am−1 · 3m−1 + · · · + aN · 3
N , N ≈ n · log 2
log 3

• lim
n→∞ dn,N
N = 1
3 or lim
n→∞ dn,mn
mn = 1
3 ,

for some suitable mn → ∞, mn monotone, would prove Erd ˝os ternary
digits conjecture (weak form).

• Dupuy et Weirich (2016):

lim
m→∞ lim
N→∞ 1
N
 N∑

n=1
 dn,m
m = 1
3 .
 • Yu (2018+):
 lim
N→∞ 1
N
 N∑

n=1
 dn,mn
mn = 1
3 .

11

Average results

Let dn,m be the number of digits “2” within the ﬁrst m digits a0, a1, . . . am−1 of
2n in base 3,

2
n = a0 + a1 · 3 + · · · + am−1 · 3m−1 + · · · + aN · 3
N , N ≈ n · log 2
log 3

• lim
n→∞ dn,N
N = 1
3 or lim
n→∞ dn,mn
mn = 1
3 ,

for some suitable mn → ∞, mn monotone, would prove Erd ˝os ternary
digits conjecture (weak form).

• Dupuy et Weirich (2016):

lim
m→∞ lim
N→∞ 1
N
 N∑

n=1
 dn,m
m = 1
3 .

• Yu (2018+):
 lim
N→∞ 1
N
 N∑

n=1
 dn,mn
mn = 1
3 .
 11

Variations

• Lagarias (2009): For all λ > 0 and x ≥ x0(λ),

#{n < x : (⌊λ2
n⌋)3 does not contain any digit “2”} ≤ 25 x 0.9725.
 There are uncountably many λ such that there are inﬁnitely many such
(exceptional) n’s.

dimH {λ > 0 : #{n : (⌊λ2
n⌋)3 does not contain any digit “2”} = ∞} = log 2
log 3 .

(Work by Abram, Lagarias (2014), Abram, Lagarias, Bolshakov (2017)
etc.)

• Burrell/Yu (2019+):

#{n < x : n contains only digits “0”, “1” in bases 3, 4 and 5} ≤ Cεx ε

(Uses an improvement of Yu on Furstenberg’s slicing problem.)

12

Variations

• Lagarias (2009): For all λ > 0 and x ≥ x0(λ),

#{n < x : (⌊λ2
n⌋)3 does not contain any digit “2”} ≤ 25 x 0.9725.

There are uncountably many λ such that there are inﬁnitely many such
(exceptional) n’s.
 dimH {λ > 0 : #{n : (⌊λ2
n⌋)3 does not contain any digit “2”} = ∞} = log 2
log 3 .

(Work by Abram, Lagarias (2014), Abram, Lagarias, Bolshakov (2017)
etc.)

• Burrell/Yu (2019+):

#{n < x : n contains only digits “0”, “1” in bases 3, 4 and 5} ≤ Cεx ε

(Uses an improvement of Yu on Furstenberg’s slicing problem.)

12

Variations

• Lagarias (2009): For all λ > 0 and x ≥ x0(λ),

#{n < x : (⌊λ2
n⌋)3 does not contain any digit “2”} ≤ 25 x 0.9725.

There are uncountably many λ such that there are inﬁnitely many such
(exceptional) n’s.

dimH {λ > 0 : #{n : (⌊λ2
n⌋)3 does not contain any digit “2”} = ∞} = log 2
log 3 .

(Work by Abram, Lagarias (2014), Abram, Lagarias, Bolshakov (2017)
etc.)
 • Burrell/Yu (2019+):

#{n < x : n contains only digits “0”, “1” in bases 3, 4 and 5} ≤ Cεx ε

(Uses an improvement of Yu on Furstenberg’s slicing problem.)

12

Variations

• Lagarias (2009): For all λ > 0 and x ≥ x0(λ),

#{n < x : (⌊λ2
n⌋)3 does not contain any digit “2”} ≤ 25 x 0.9725.

There are uncountably many λ such that there are inﬁnitely many such
(exceptional) n’s.

dimH {λ > 0 : #{n : (⌊λ2
n⌋)3 does not contain any digit “2”} = ∞} = log 2
log 3 .

(Work by Abram, Lagarias (2014), Abram, Lagarias, Bolshakov (2017)
etc.)

• Burrell/Yu (2019+):

#{n < x : n contains only digits “0”, “1” in bases 3, 4 and 5} ≤ Cεx ε

(Uses an improvement of Yu on Furstenberg’s slicing problem.)
 12

Patterns

Soient p, q multiplicatively independent positive integers.

• Lagarias conjecture (2009): Any given ﬁnite pattern P = a1a2 · · · ak of
consecutive q-ary digits occurs in (pn)q, for all sufﬁciently large
n > n0(P).
 • Furstenberg conjecture (1970): same statement for (pn)pq instead of
(pn)q.

Weak Erd ˝os conjecture is the case p = 2, q = 3, P = 2 in Lagarias’
conjecture.

Questions:

• Can we avoid a ﬁxed pattern P in the q-ary digital expansions of
p, p2, p3, . . . ?

• If not, how long must we wait to “see” P ?

• What about repeated patterns PP · · · P?

13

Patterns

Soient p, q multiplicatively independent positive integers.

• Lagarias conjecture (2009): Any given ﬁnite pattern P = a1a2 · · · ak of
consecutive q-ary digits occurs in (pn)q, for all sufﬁciently large
n > n0(P).

• Furstenberg conjecture (1970): same statement for (pn)pq instead of
(pn)q.
 Weak Erd ˝os conjecture is the case p = 2, q = 3, P = 2 in Lagarias’
conjecture.

Questions:

• Can we avoid a ﬁxed pattern P in the q-ary digital expansions of
p, p2, p3, . . . ?

• If not, how long must we wait to “see” P ?

• What about repeated patterns PP · · · P?

13

Patterns

Soient p, q multiplicatively independent positive integers.

• Lagarias conjecture (2009): Any given ﬁnite pattern P = a1a2 · · · ak of
consecutive q-ary digits occurs in (pn)q, for all sufﬁciently large
n > n0(P).

• Furstenberg conjecture (1970): same statement for (pn)pq instead of
(pn)q.

Weak Erd ˝os conjecture is the case p = 2, q = 3, P = 2 in Lagarias’
conjecture.
 Questions:

• Can we avoid a ﬁxed pattern P in the q-ary digital expansions of
p, p2, p3, . . . ?

• If not, how long must we wait to “see” P ?

• What about repeated patterns PP · · · P?

13

Patterns

Soient p, q multiplicatively independent positive integers.

• Lagarias conjecture (2009): Any given ﬁnite pattern P = a1a2 · · · ak of
consecutive q-ary digits occurs in (pn)q, for all sufﬁciently large
n > n0(P).

• Furstenberg conjecture (1970): same statement for (pn)pq instead of
(pn)q.

Weak Erd ˝os conjecture is the case p = 2, q = 3, P = 2 in Lagarias’
conjecture.

Questions:

• Can we avoid a ﬁxed pattern P in the q-ary digital expansions of
p, p2, p3, . . . ?

• If not, how long must we wait to “see” P ?

• What about repeated patterns PP · · · P?
 13

Main result - Patterns in exponential functions

Theorem (Kaneko, S. (2018))
Let p ≥ 2 be a prime, m not a power of p, and

P = a1a2 · · · ak

be any ﬁnite pattern of consecutive p-ary digits. Then:

(1) There exist c1, c2 > 0 only depending on p, m and P such that

#{n < x : (mn)p contains ≥ c1 log n occurrences of P} ≥ c2x.

(2) There exists c3 = c3(p, m) and n < c3pkL such that (mn)p contains
L consecutive occurrences of P.

(3) There exists c = c(P) > 0 such that

lim sup
n→∞ # patterns P in (mn)p
log n ≥ c
log p > 0.
 14

Hensel’s lemma - basic statement

Basic statement:
Let f (X ) ∈ Zp[X ]. Suppose that u ∈ Zp is such that

f (u) ≡ 0 (mod p), and f ′(u) ̸≡ 0 (mod p).

Then there exists an unique ξ ∈ Zp such that

f (ξ) = 0, and ξ ≡ u (mod p).
 Basic statement (II):
Let f (X ) ∈ Zp[X ] \ Zp. Suppose that u ∈ Zp is such that

vp(f (u)) > 2vp(f ′(u)).

Then there exists a unique ξ ∈ Zp such that

f (ξ) = 0, and vp(ξ − u) > vp(f ′(u)).

15

Hensel’s lemma - basic statement

Basic statement:
Let f (X ) ∈ Zp[X ]. Suppose that u ∈ Zp is such that

f (u) ≡ 0 (mod p), and f ′(u) ̸≡ 0 (mod p).

Then there exists an unique ξ ∈ Zp such that

f (ξ) = 0, and ξ ≡ u (mod p).

Basic statement (II):
Let f (X ) ∈ Zp[X ] \ Zp. Suppose that u ∈ Zp is such that

vp(f (u)) > 2vp(f ′(u)).

Then there exists a unique ξ ∈ Zp such that

f (ξ) = 0, and vp(ξ − u) > vp(f ′(u)).
 15

Hensel’s lemma - differentiable functions

Let f : Zp → Zp be a function and u ∈ Zp. f is differentiable modulo ps at u if
there exists ∂sf (u) ∈ Qp such that for any u′ ∈ Zp and all n > N,

f (u + pnu′) ≡ f (u) + pnu′∂sf (u) (mod pn+s).
 Let f : Zp → Zp and u ∈ Zp. Assume that vp(f (u)) ≥ n and that for all x ∈ Zp
with x ≡ u (mod pn−j ) that f is differentiable modulo ps at x with order N and
that vp(∂sf (x)) = j,

with j + N < n and j < s. Then there exists an ξ ∈ Zp satisfying

f (ξ) = 0, and ξ ≡ u (mod pn−j ).

• Generalises Axelsson/Khrennikov (2016): 1-Lipschitz functions,
namely f : Zp → Zp which satisfy |f (x) − f (y )|p ≤ |x − y |p for any
x, y ∈ Zp.

16

Hensel’s lemma - differentiable functions

Let f : Zp → Zp be a function and u ∈ Zp. f is differentiable modulo ps at u if
there exists ∂sf (u) ∈ Qp such that for any u′ ∈ Zp and all n > N,

f (u + pnu′) ≡ f (u) + pnu′∂sf (u) (mod pn+s).

Let f : Zp → Zp and u ∈ Zp. Assume that vp(f (u)) ≥ n and that for all x ∈ Zp
with x ≡ u (mod pn−j ) that f is differentiable modulo ps at x with order N and
that vp(∂sf (x)) = j,

with j + N < n and j < s. Then there exists an ξ ∈ Zp satisfying

f (ξ) = 0, and ξ ≡ u (mod pn−j ).
 • Generalises Axelsson/Khrennikov (2016): 1-Lipschitz functions,
namely f : Zp → Zp which satisfy |f (x) − f (y )|p ≤ |x − y |p for any
x, y ∈ Zp.

16

Hensel’s lemma - differentiable functions

Let f : Zp → Zp be a function and u ∈ Zp. f is differentiable modulo ps at u if
there exists ∂sf (u) ∈ Qp such that for any u′ ∈ Zp and all n > N,

f (u + pnu′) ≡ f (u) + pnu′∂sf (u) (mod pn+s).

Let f : Zp → Zp and u ∈ Zp. Assume that vp(f (u)) ≥ n and that for all x ∈ Zp
with x ≡ u (mod pn−j ) that f is differentiable modulo ps at x with order N and
that vp(∂sf (x)) = j,

with j + N < n and j < s. Then there exists an ξ ∈ Zp satisfying

f (ξ) = 0, and ξ ≡ u (mod pn−j ).

• Generalises Axelsson/Khrennikov (2016): 1-Lipschitz functions,
namely f : Zp → Zp which satisfy |f (x) − f (y )|p ≤ |x − y |p for any
x, y ∈ Zp.
 16

van der Put series

For a positive integer m, write

m = m0 + m1p + · · · + mk pk ,

where k = ⌊log m/ log p⌋. For x ∈ Zp set

χ(m; x) =
 


1 if |x − m|p ≤ p−1−k ,

0 otherwise.

Let f : Zp → Zp be any continuous function. Then there exists a unique
sequence B(f ; m) (m = 0, 1, . . .) such that

f (x) =
 ∞∑

m=0 B(f ; m)χ(m; x)

for any x ∈ Zp, the van der Put series of f . (van der Put 1968)
 17

Generalized van der Put series

Let Φ : N → N be a strictly increasing function. For x ∈ Zp write

x =
 ∞∑

j=0
 Φ(j)∑

i=Φ(−1+j)+1 xi pi .

Put τ (m) = min {h ∈ N ∣
∣
∣ m < p1+Φ(h) }

and, for any x ∈ Zp,

χ(m; x) :=
 



1 if |x − m|p ≤ p−1−Φ(τ (m)),

0 otherwise.

For any continuous function f : Zp → Zp there exists a unique sequence
B(m) = B(f ; m) (m = 0, 1, . . .) such that

f (x) =
 ∞∑

m=0 B(f ; m)χ(m; x)

for any x ∈ Zp, the generalized van der Put series of f . Put

b(m) = b(f ; m) := p−τ (m)B(f ; m) ∈ Zp.
 18

Hensel’s lemma - continuous functions

Theorem (Kaneko, S. (2019))

Let Φ : N → N be strictly increasing, f ∈ F (Φ) continuous, u < p1+Φ(n0)

and f (u) ≡ 0 (mod p1+h+n0 ).

Suppose that there exists (S(n))n≥n0 with

S(n) ⊂ (0, pΦ(n+1)−Φ(n)) , #S(n) = p − 1,

such that for any nonnegative integers n, m with

n ≥ n0, m < p1+Φ(n), m ≡ u (mod p1+Φ(n0)),

we have
{ b (
m + ip1+Φ(n)) mod ph+1 ∣
∣
∣ i ∈ S(n)} = {
ph, 2ph, . . . , (p − 1)ph+1} .

Then there exists ξ ∈ Zp such that

f (ξ) = 0, ξ ≡ u (mod p1+Φ(n0)).
 19

Main result - Patterns in exponential functions

Theorem (Kaneko, S. (2018))
Let p ≥ 2 be a prime, m not a power of p, and

P = a1a2 · · · ak

be any ﬁnite pattern of consecutive p-ary digits. Then:

(1) There exist c1, c2 > 0 only depending on p, m and P such that

#{n < x : (mn)p contains ≥ c1 log n occurrences of P} ≥ c2x.

(2) There exists c3 = c3(p, m) and n < c3pkL such that (mn)p contains
L consecutive occurrences of P.

(3) There exists c = c(P) > 0 such that

lim sup
n→∞ # patterns P in (mn)p
log n ≥ c
log p > 0.
 20

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1
 • Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
• For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
• Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
• Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
• Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !

21

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1

• Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
 • For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
• Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
• Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
• Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !

21

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1

• Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
• For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
 • Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
• Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
• Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !

21

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1

• Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
• For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
• Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
 • Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
• Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !

21

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1

• Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
• For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
• Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
• Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
 • Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !

21

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1

• Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
• For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
• Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
• Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
• Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !

21

Key moments in the proof

• Let P = a1a2 · · · ak and bp,L be the integer whose p-ary expansion is

PP · · · P︸ ︷︷ ︸
L 00 · · · 0︸ ︷︷ ︸
c 1, L
′ = kL + c + 1

• Put g : Zp → Zp with
 g(u) = (mp−1)u = (1 + ape)u

with a ∤ p, and set f (u) = g(u) − bp,L.
• For e ≥ 2 or p ≥ 3, g(u) is differentiable modulo pe+1 at any u ∈ Zp with
order 0 and ∂e+1g(u) = ape.
• Generalized Hensel gives ξ ∈ Zp such that g(ξ) = bp,L.
• Let N ≡ ξ (mod pL
′ ) with pL′ ≤ N < 2pL
′ .
• Since u, u′ ∈ Zp with vp(u − u′) ≥ N implies vp(g(u) − g(u′)) ≥ N + 1,

m(p−1)N = g(N) ≡ g(ξ) = bq,L (mod pL
′ ).
 Thank you !
 21
