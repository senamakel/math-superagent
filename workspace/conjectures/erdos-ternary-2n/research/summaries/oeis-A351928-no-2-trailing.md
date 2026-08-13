<!-- source: https://oeis.org/A351928 | converted from HTML -->

A351928 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A351928 - OEIS] [3]

A351928

Smallest positive integer k such that 2^k has no '2' in the last n digits of its ternary expansion.

2

2, 2, 6, 8, 8, 8, 20, 24, 24, 24, 72, 186, 186, 332, 332, 1134, 1134, 1134, 1134, 1134, 1134, 25458, 25458, 25458, 25458, 25458, 25458, 159140, 249968, 249968, 249968, 249968, 249968, 249968, 249968, 249968, 9076914, 9076914, 9076914, 9076914, 9076914, 9076914, 90062678

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

The powers of two are required to have at least n ternary digits, i.e., 2^k >= 3^(n-1).

Erdős (~1978) conjectured that 1, 4, and 256 are the only powers of two whose ternary expansion consists solely of 0's and 1's.

LINKS

[Table of n, a(n) for n=1..43.][11]

Paul Erdős, [Some unconventional problems in number theory][12], Mathematics Magazine, Vol. 52, No. 2 (1979), pp. 67-70.

Robert I. Saye, [On two conjectures concerning the ternary digits of powers of two][13], arXiv:2202.13256 [math.NT], 2022.

MATHEMATICA

smallest[n_] := Module[{k}, k = Max[1, Ceiling[(n - 1) Log[2, 3]]]; While[MemberQ[Take[IntegerDigits[2^k, 3], -n], 2], ++k]; k]; Table[smallest[n], {n, 1, 20}]

PROG

(PARI) a(n) = my(k=max(1, logint(3^(n-1), 2))); while(#select(x->(x==2), Vec(Vecrev(digits(2^k, 3)), n)), k++); k; \\ [Michel Marcus][14], Feb 26 2022

(Python)

from sympy.ntheory.digits import digits

def a(n, startk=1):

k = max(startk, len(bin(3**(n-1))[2:]))

pow2 = 2**k

while 2 in digits(pow2, 3)[-n:]:

k += 1

pow2 *= 2

return k

an = 0

for n in range(1, 22):

an = a(n, an)

print(an, end=", ") # [Michael S. Branicky][15], Feb 27 2022

(Python)

from itertools import count

def [A351928][16] (n):

kmax, m = 3**n, (3**(n-1)).bit_length()

k2 = pow(2, m, kmax)

for k in count(m):

a = k2

while a > 0:

a, b = divmod(a, 3)

if b == 2:

break

else:

return k

k2 = 2*k2 % kmax # [Chai Wah Wu][17], Mar 19 2022

CROSSREFS

Cf. [A004642][18], [A117971][19], [A351927][20].

Sequence in context: [A334518][21] [A099490][22] [A167878][23] * [A331786][24] [A320139][25] [A033724][26]

Adjacent sequences: [A351925][27] [A351926][28] [A351927][20] * [A351929][29] [A351930][30] [A351931][31]

KEYWORD

nonn, base

AUTHOR

[Robert Saye][32], Feb 25 2022

STATUS

approved

[Lookup][3] [Welcome][33] [Wiki][34] [Register][35] [Music][36] [Plot 2][37] [Demos][38] [Index][39] [WebCam][40] [Contribute][41] [Format][42] [Style Sheet][43] [Transforms][44] [Superseeker][45] [Recents][46]

[The OEIS Community][47]

Maintained by [The OEIS Foundation Inc.][48]

Last modified August 13 02:49 EDT 2026. Contains 398269 sequences.

[License Agreements, Terms of Use, Privacy Policy][49]


## Links

[1]: /login?redirect=%2fA351928
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A351928/list
[5]: /A351928/graph
[6]: /search?q=A351928+-id:A351928
[7]: /A351928/listen
[8]: /history?seq=A351928
[9]: /search?q=id:A351928&fmt=text
[10]: /A351928/internal
[11]: /A351928/b351928.txt
[12]: https://www.jstor.org/stable/2689842
[13]: https://arxiv.org/abs/2202.13256
[14]: /wiki/User:Michel_Marcus
[15]: /wiki/User:Michael_S._Branicky
[16]: /A351928
[17]: /wiki/User:Chai_Wah_Wu
[18]: /A004642
[19]: /A117971
[20]: /A351927
[21]: /A334518
[22]: /A099490
[23]: /A167878
[24]: /A331786
[25]: /A320139
[26]: /A033724
[27]: /A351925
[28]: /A351926
[29]: /A351929
[30]: /A351930
[31]: /A351931
[32]: /wiki/User:Robert_Saye
[33]: /wiki/Welcome
[34]: /wiki/Main_Page
[35]: /wiki/Special:RequestAccount
[36]: /play.html
[37]: /plot2.html
[38]: /demo1.html
[39]: /wiki/Index_to_OEIS
[40]: /webcam
[41]: /Submit.html
[42]: /eishelp2.html
[43]: /wiki/Style_Sheet
[44]: /transforms.html
[45]: /ol.html
[46]: /recent
[47]: /community.html
[48]: http://oeisf.org
[49]: /wiki/Legal_Documents
