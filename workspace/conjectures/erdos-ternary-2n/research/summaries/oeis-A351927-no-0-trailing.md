<!-- source: https://oeis.org/A351927 | converted from HTML -->

A351927 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A351927 - OEIS] [3]

A351927

Smallest positive integer k such that 2^k has no '0' in the last n digits of its ternary expansion.

2

1, 2, 4, 10, 15, 15, 15, 15, 15, 15, 50, 50, 101, 101, 101, 101, 143, 143, 143, 143, 143, 143, 143, 143, 143, 1916, 1916, 1916, 1916, 1916, 1916, 82286, 1134022, 1639828, 3483159, 3483159, 3483159, 3917963, 3917963, 3917963, 4729774, 4729774, 9827775, 9827775, 43622201, 43622201, 43622201

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,2

COMMENTS

The powers of two are required to have at least n ternary digits, i.e., 2^k >= 3^(n-1).

Sloane (1973) conjectured that every power 2^n with n > 15 has a '0' somewhere in its ternary expansion (see [A102483][11] and [A346497][12]).

LINKS

[Table of n, a(n) for n=1..47.][13]

Robert I. Saye, [On two conjectures concerning the ternary digits of powers of two][14], arXiv:2202.13256 [math.NT], 2022.

MATHEMATICA

smallest[n_] := Module[{k}, k = Max[1, Ceiling[(n - 1) Log[2, 3]]]; While[MemberQ[Take[IntegerDigits[2^k, 3], -n], 0], ++k]; k]; Table[smallest[n], {n, 1, 20}]

PROG

(PARI) a(n) = my(k=1); while(!vecmin(Vec(Vecrev(digits(2^k, 3)), n)), k++); k; \\ [Michel Marcus][15], Feb 26 2022

(Python)

from sympy.ntheory.digits import digits

def a(n, startk=1):

k = max(startk, len(bin(3**(n-1))[2:]))

pow2 = 2**k

while 0 in digits(pow2, 3)[-n:]:

k += 1

pow2 *= 2

return k

an = 0

for n in range(1, 32):

an = a(n, an)

print(an, end=", ") # [Michael S. Branicky][16], Mar 10 2022

(Python)

from itertools import count

def [A351927][17] (n):

kmax, m = 3**n, (3**(n-1)).bit_length()

k2 = pow(2, m, kmax)

for k in count(m):

a = k2

if 3*a >= kmax:

while a > 0:

a, b = divmod(a, 3)

if b == 0:

break

else:

return k

k2 = 2*k2 % kmax # [Chai Wah Wu][18], Mar 19 2022

CROSSREFS

Cf. [A004642][19], [A117970][20], [A102483][11], [A346497][12], [A351928][21].

Sequence in context: [A056392][22] [A080149][23] [A217134][24] * [A333619][25] [A381835][26] [A128513][27]

Adjacent sequences: [A351924][28] [A351925][29] [A351926][30] * [A351928][21] [A351929][31] [A351930][32]

KEYWORD

nonn, base

AUTHOR

[Robert Saye][33], Feb 25 2022

STATUS

approved

[Lookup][3] [Welcome][34] [Wiki][35] [Register][36] [Music][37] [Plot 2][38] [Demos][39] [Index][40] [WebCam][41] [Contribute][42] [Format][43] [Style Sheet][44] [Transforms][45] [Superseeker][46] [Recents][47]

[The OEIS Community][48]

Maintained by [The OEIS Foundation Inc.][49]

Last modified August 13 02:49 EDT 2026. Contains 398269 sequences.

[License Agreements, Terms of Use, Privacy Policy][50]


## Links

[1]: /login?redirect=%2fA351927
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A351927/list
[5]: /A351927/graph
[6]: /search?q=A351927+-id:A351927
[7]: /A351927/listen
[8]: /history?seq=A351927
[9]: /search?q=id:A351927&fmt=text
[10]: /A351927/internal
[11]: /A102483
[12]: /A346497
[13]: /A351927/b351927.txt
[14]: https://arxiv.org/abs/2202.13256
[15]: /wiki/User:Michel_Marcus
[16]: /wiki/User:Michael_S._Branicky
[17]: /A351927
[18]: /wiki/User:Chai_Wah_Wu
[19]: /A004642
[20]: /A117970
[21]: /A351928
[22]: /A056392
[23]: /A080149
[24]: /A217134
[25]: /A333619
[26]: /A381835
[27]: /A128513
[28]: /A351924
[29]: /A351925
[30]: /A351926
[31]: /A351929
[32]: /A351930
[33]: /wiki/User:Robert_Saye
[34]: /wiki/Welcome
[35]: /wiki/Main_Page
[36]: /wiki/Special:RequestAccount
[37]: /play.html
[38]: /plot2.html
[39]: /demo1.html
[40]: /wiki/Index_to_OEIS
[41]: /webcam
[42]: /Submit.html
[43]: /eishelp2.html
[44]: /wiki/Style_Sheet
[45]: /transforms.html
[46]: /ol.html
[47]: /recent
[48]: /community.html
[49]: http://oeisf.org
[50]: /wiki/Legal_Documents
