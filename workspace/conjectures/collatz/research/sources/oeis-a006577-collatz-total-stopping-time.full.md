<!-- source: https://oeis.org/A006577 | converted from HTML -->

A006577 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A006577 - OEIS] [3]

A006577

Number of halving and tripling steps to reach 1 in '3x+1' problem, or -1 if 1 is never reached.
(Formerly M4323)

263

0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12, 20, 20, 7, 7, 15, 15, 10, 23, 10, 111, 18, 18, 18, 106, 5, 26, 13, 13, 21, 21, 21, 34, 8, 109, 8, 29, 16, 16, 16, 104, 11, 24, 24, 24, 11, 11, 112, 112, 19, 32, 19, 32, 19, 19, 107, 107, 6, 27, 27, 27, 14, 14, 14, 102, 22

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,3

COMMENTS

The 3x+1 or Collatz problem is as follows: start with any number n. If n is even, divide it by 2, otherwise multiply it by 3 and add 1. Do we always reach 1? This is a famous unsolved problem. It is conjectured that the answer is yes.

It seems that about half of the terms satisfy a(i) = a(i+1). For example, up to 10000000, 4964705 terms satisfy this condition.

n is an element of row a(n) in triangle [A127824][11]. - [Reinhard Zumkeller][12], Oct 03 2012

The number of terms that satisfy a(i) = a(i+1) for i less than a power of ten from 10^1 through 10^10 are: 0, 31, 365, 4161, 45022, 477245, 4964705, 51242281, 526051204, 5378743993. - [John Mason][13], Mar 02 2018

5 seems to be the only number whose value matches its total number of steps (checked to n <= 10^9). - [Peter Woodward][14], Feb 15 2021

REFERENCES

R. K. Guy, Unsolved Problems in Number Theory, E16.

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

LINKS

N. J. A. Sloane, [Table of n, a(n) for n = 1..10000][15]

David Eisenbud and Brady Haran, [UNCRACKABLE? The Collatz Conjecture][16], Numberphile video, 2016.

Geometry.net, [Links on Collatz Problem][17]

Christian Hercher, [There are no Collatz m-Cycles with m <= 91][18], J. Int. Seq. (2023) Vol. 26, Article 23.3.5.

Jason Holt, [Log-log plot of first billion terms][19]

Jason Holt, [Plot of 1 billion values of the number of steps to drop below n][20] ( [A060445][21]), log scale on x axis

Jason Holt, [Plot of 10 billion values of the number of steps to drop below n][22] ( [A060445][21]), log scale on x axis

A. Krowne, [Collatz problem][23], PlanetMath.org.

J. C. Lagarias, [The 3x+1 problem and its generalizations][24], Amer. Math. Monthly, 92 (1985), 3-23.

J. C. Lagarias, [How random are 3x+1 function iterates?][25], in The Mathemagician and the Pied Puzzler - A Collection in Tribute to Martin Gardner, Ed. E. R. Berlekamp and T. Rogers, A. K. Peters, 1999, pp. 253-266.

J. C. Lagarias, [The 3x+1 Problem: an annotated bibliography, II (2000-2009)][26], arXiv:0608208 [math.NT], 2006-2012.

J. C. Lagarias, ed., [The Ultimate Challenge: The 3x+1 Problem][27], Amer. Math. Soc., 2010.

Jeffrey C. Lagarias, [The 3x+1 Problem: An Overview][28], arXiv:2111.02635 [math.NT], 2021.

M. Le Brun, [Email to N. J. A. Sloane, Jul 1991][29]

Mathematical BBS, [Biblography on Collatz Sequence][30]

P. Picart, [Algorithme de Collatz et conjecture de Syracuse][31]

E. Roosendaal, [On the 3x+1 problem][32]

J. L. Simons, [On the nonexistence of 2-cycles for the 3x+1 problem][33], Math. Comp. 75 (2005), 1565-1572.

N. J. A. Sloane, ["A Handbook of Integer Sequences" Fifty Years Later][34], arXiv:2301.03149 [math.NT], 2023, p. 8.

G. Villemin's Almanach of Numbers, [Cycle of Syracuse][35]

Eric Weisstein's World of Mathematics, [Collatz Problem][36]

Wikipedia, [Collatz Conjecture][37]

[Index entries for sequences related to 3x+1 (or Collatz) problem][38]

FORMULA

a(n) = [A006666][39] (n) + [A006667][40] (n).

a(n) = [A112695][41] (n) + 2 for n > 2. - [Reinhard Zumkeller][12], Apr 18 2008

a(n) = [A008908][42] (n) - 1. - [L. Edson Jeffery][43], Jul 21 2014

a(n) = [A135282][44] (n) + [A208981][45] (n) (after [Alonso del Arte][46] 's comment in [A208981][45]), if 1 is reached, otherwise a(n) = -1. - [Omar E. Pol][47], Apr 10 2022

a(n) = 2*[A007814][48] (n + 1) + a( [A085062][49] (n)) + 1 for n > 1. - [Wing-Yin Tang][50], Jan 06 2025

EXAMPLE

a(5)=5 because the trajectory of 5 is (5,16,8,4,2,1).

MAPLE

[A006577][51]:= proc(n)

local a, traj ;

a := 0 ;

traj := n ;

while traj > 1 do

if type(traj, 'even') then

traj := traj/2 ;

else

traj := 3*traj+1 ;

end if;

a := a+1 ;

end do:

return a;

end proc: # [R. J. Mathar][52], Jul 08 2012

MATHEMATICA

f[n_] := Module[{a=n, k=0}, While[a!=1, k++; If[EvenQ[a], a=a/2, a=a*3+1]]; k]; Table[f[n], {n, 4!}] (* [Vladimir Joseph Stephan Orlovsky][53], Jan 08 2011 *)

Table[Length[NestWhileList[If[EvenQ[#], #/2, 3#+1]&, n, #!=1&]]-1, {n, 80}] (* [Harvey P. Dale][54], May 21 2012 *)

PROG

(PARI) a(n)=if(n<0, 0, s=n; c=0; while(s>1, s=if(s%2, 3*s+1, s/2); c++); c)

(PARI) step(n)=if(n%2, 3*n+1, n/2);

[A006577][51] (n)=if(n==1, 0, [A006577][51] (step(n))+1); \\ [Michael B. Porter][55], Jun 05 2010

(Haskell)

import Data.List (findIndex)

import Data.Maybe (fromJust)

a006577 n = fromJust $ findIndex (n `elem`) a127824_tabf

-- [Reinhard Zumkeller][12], Oct 04 2012, Aug 30 2012

(Python)

def a(n):

if n==1: return 0

x=0

while True:

if n%2==0: n//=2

else: n = 3*n + 1

x+=1

if n<2: break

return x

print([a(n) for n in range(1, 101)]) # [Indranil Ghosh][56], Jun 05 2017

(Python)

def [A006577][51] (n):

ct = 0

while n != 1: n = [A006370][57] (n); ct += 1

return ct # [Ya-Ping Lu][58], Feb 22 2024

(R) collatz<-function(n) ifelse(n==1, 0, 1+ifelse(n%%2==0, collatz(n/2), collatz(3*n+1))); sapply(1:72, collatz) # [Christian N. K. Anderson][59], Oct 09 2024

CROSSREFS

See [A070165][60] for triangle giving trajectories of n = 1, 2, 3, ....

Cf. [A006370][57], [A125731][61], [A127885][62], [A127886][63], [A008908][42], [A112695][41], [A135282][44], [A208981][45], [A025586][64].

Cf. [A008884][65], [A161021][66], [A161022][67], [A161023][68].

Cf. [A006878][69] (records), [A006877][70] (starting values for records).

Sequence in context: [A337357][71] [A340420][72] [A127885][62] * [A337150][73] [A280234][74] [A368383][75]

Adjacent sequences: [A006574][76] [A006575][77] [A006576][78] * [A006578][79] [A006579][80] [A006580][81]

KEYWORD

nonn, nice, easy, [hear][7], [look][5]

AUTHOR

[N. J. A. Sloane][82], [Bill Gosper][83]

EXTENSIONS

More terms from Larry Reeves (larryr(AT)acm.org), Apr 27 2001

"Escape clause" added to definition by [N. J. A. Sloane][82], Jun 06 2017

STATUS

approved

[Lookup][3] [Welcome][84] [Wiki][85] [Register][86] [Music][87] [Plot 2][88] [Demos][89] [Index][90] [WebCam][91] [Contribute][92] [Format][93] [Style Sheet][94] [Transforms][95] [Superseeker][96] [Recents][97]

[The OEIS Community][98]

Maintained by [The OEIS Foundation Inc.][99]

Last modified August 18 05:02 EDT 2026. Contains 398405 sequences.

[License Agreements, Terms of Use, Privacy Policy][100]


## Links

[1]: /login?redirect=%2fA006577
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A006577/list
[5]: /A006577/graph
[6]: /search?q=A006577+-id:A006577
[7]: /A006577/listen
[8]: /history?seq=A006577
[9]: /search?q=id:A006577&fmt=text
[10]: /A006577/internal
[11]: /A127824
[12]: /wiki/User:Reinhard_Zumkeller
[13]: /wiki/User:John_Mason
[14]: /wiki/User:Peter_Woodward
[15]: /A006577/b006577.txt
[16]: https://www.youtube.com/watch?v=5mFpVDpKX70
[17]: http://www.geometry.net/theorems_and_conjectures/collatz_problem.html
[18]: https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html
[19]: /A006577/a006577_1Blog.png
[20]: /A006577/a006577_1B.png
[21]: /A060445
[22]: /A006577/a006577_10B.png
[23]: https://planetmath.org/collatzproblem
[24]: http://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/paper.html
[25]: http://www.cfrd.cl/~moises/DVD/05Bibliografia%20-%20Geometria%20Sagrada/Matematica%20Recreativa/Martin%20Gardner/Martin%20Gardner%20-%20The%20Mathemagician%20and%20Pied%20Puzzler%20-%20A%20Collection%20in%20Tribute%20to%20Martin%20Gardner.pdf
[26]: https://arxiv.org/pdf/math/0608208
[27]: http://www.ams.org/bookstore-getitem/item=mbk-78
[28]: https://arxiv.org/pdf/2111.02635
[29]: /A006577/a006577.pdf
[30]: http://felix.unife.it/Root/d-Mathematics/d-Number-theory/b-3x+1
[31]: http://trucsmaths.free.fr/js_syracuse.htm
[32]: http://www.ericr.nl/wondrous/index.html
[33]: https://doi.org/10.1090/S0025-5718-04-01728-4
[34]: https://arxiv.org/pdf/2301.03149
[35]: https://translate.google.com/translate?hl=en&amp;sl=fr&amp;u=http://villemin.gerard.free.fr/Wwwgvmm/Iteration/Syracuse.htm#top
[36]: https://mathworld.wolfram.com/CollatzProblem.html
[37]: https://en.wikipedia.org/wiki/Collatz_conjecture
[38]: /index/3#3x1
[39]: /A006666
[40]: /A006667
[41]: /A112695
[42]: /A008908
[43]: /wiki/User:L._Edson_Jeffery
[44]: /A135282
[45]: /A208981
[46]: /wiki/User:Alonso_del_Arte
[47]: /wiki/User:Omar_E._Pol
[48]: /A007814
[49]: /A085062
[50]: /wiki/User:Wing-Yin_Tang
[51]: /A006577
[52]: /wiki/User:R._J._Mathar
[53]: /wiki/User:Vladimir_Joseph_Stephan_Orlovsky
[54]: /wiki/User:Harvey_P._Dale
[55]: /wiki/User:Michael_B._Porter
[56]: /wiki/User:Indranil_Ghosh
[57]: /A006370
[58]: /wiki/User:Ya-Ping_Lu
[59]: /wiki/User:Christian_N._K._Anderson
[60]: /A070165
[61]: /A125731
[62]: /A127885
[63]: /A127886
[64]: /A025586
[65]: /A008884
[66]: /A161021
[67]: /A161022
[68]: /A161023
[69]: /A006878
[70]: /A006877
[71]: /A337357
[72]: /A340420
[73]: /A337150
[74]: /A280234
[75]: /A368383
[76]: /A006574
[77]: /A006575
[78]: /A006576
[79]: /A006578
[80]: /A006579
[81]: /A006580
[82]: /wiki/User:N._J._A._Sloane
[83]: /wiki/User:Bill_Gosper
[84]: /wiki/Welcome
[85]: /wiki/Main_Page
[86]: /wiki/Special:RequestAccount
[87]: /play.html
[88]: /plot2.html
[89]: /demo1.html
[90]: /wiki/Index_to_OEIS
[91]: /webcam
[92]: /Submit.html
[93]: /eishelp2.html
[94]: /wiki/Style_Sheet
[95]: /transforms.html
[96]: /ol.html
[97]: /recent
[98]: /community.html
[99]: http://oeisf.org
[100]: /wiki/Legal_Documents
