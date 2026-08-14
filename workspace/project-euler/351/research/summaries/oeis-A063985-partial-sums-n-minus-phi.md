> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A063985-partial-sums-n-minus-phi.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A063985 | converted from HTML -->

A063985 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A063985 - OEIS] [3]

A063985

Partial sums of cototient sequence [A051953][4].

10

0, 1, 2, 4, 5, 9, 10, 14, 17, 23, 24, 32, 33, 41, 48, 56, 57, 69, 70, 82, 91, 103, 104, 120, 125, 139, 148, 164, 165, 187, 188, 204, 217, 235, 246, 270, 271, 291, 306, 330, 331, 361, 362, 386, 407, 431, 432, 464, 471, 501, 520, 548, 549, 585, 600, 632, 653, 683

( [list][5]; [graph][6]; [refs][7]; [listen][8]; [history][9]; [text][10]; [internal format][11])

OFFSET

1,3

COMMENTS

Number of elements in the set {(x,y): 1 <= x <= y <= n, 1 = gcd(x,y)}; a(n) = [A000217][12] (n) - [A002088][13] (n) = [A100613][14] (n) - [A185670][15] (n). - [Reinhard Zumkeller][16], Jan 21 2013

8*a(n) is the number of dots not in direct reach via a straight line from the center of a 2*n+1 X 2*n+1 array of dots. - [Kiran Ananthpur Bacche][17], May 25 2022

LINKS

Harry J. Smith, [Table of n, a(n) for n = 1..1000][18]

N. J. A. Sloane, [Families of Essentially Identical Sequences][19], Mar 24 2021 (Includes this sequence)

FORMULA

a(n) = Sum_{x=1..n} (x - phi(x)) = Sum(x) - Sum(phi(x)) = [A000217][12] (n) - [A002088][13] (n), phi(n) = [A000010][20] (n), cototient(n) = [A051953][4] (n).

a(n) = n^2 - [A091369][21] (n). - [Enrique Pérez Herrero][22], Feb 25 2012

G.f.: x/(1 - x)^3 - (1/(1 - x))*Sum_{k>=1} mu(k)*x^k/(1 - x^k)^2. - [Ilya Gutkovskiy][23], Mar 18 2017

a(n) = (1/2 - 3/Pi^2)*n^2 + O(n*log(n)). - [Amiram Eldar][24], Jul 26 2022

MATHEMATICA

f[n_] := n(n + 1)/2 - Sum[ EulerPhi@i, {i, n}]; Array[f, 58] (* [Robert G. Wilson v][25] *)

Accumulate[Table[n-EulerPhi[n], {n, 1, 60}]] (* [Harvey P. Dale][26], Aug 19 2015 *)

PROG

(PARI) { a=0; for (n=1, 1000, write("b063985.txt", n, " ", a+=n - eulerphi(n)) ) } \\ [Harry J. Smith][27], Sep 04 2009

(Haskell)

a063985 n = length [()| x <- [1..n], y <- [x..n], gcd x y > 1]

-- [Reinhard Zumkeller][16], Jan 21 2013

(Python)

from sympy.ntheory import totient

def a(n): return sum(x - totient(x) for x in range(1, n + 1))

[a(n) for n in range(1, 51)] # [Indranil Ghosh][28], Mar 18 2017

(Python)

from functools import lru_cache

@lru_cache(maxsize=None)

def [A063985][29] (n): # based on second formula in [A018805][30]

if n == 0:

return 0

c, j = 0, 2

k1 = n//j

while k1 > 1:

j2 = n//k1 + 1

c += (j2-j)*(k1*(k1+1)-2*[A063985][29] (k1)-1)

j, k1 = j2, n//j2

return (2*n+c-j)//2 # [Chai Wah Wu][31], Mar 24 2021

(Java)

// Save the file as [A063985][29].java to compile and run

import java.util.stream.IntStream;

import java.util.*;

public class [A063985][29] {

public static int getInvisiblePoints(int n) {

Set<Float> slopes = new HashSet<Float>();

IntStream.rangeClosed(1, n).forEach(i ->

{IntStream.rangeClosed(1, n).forEach(j ->

slopes.add(Float.valueOf((float)i/(float)j))); });

return (n * n - slopes.size() + n - 1) / 2;

}

public static void main(String args[]) throws Exception {

IntStream.rangeClosed(1, 30).forEach(i ->

System.out.println(getInvisiblePoints(i)));

}

} // [Kiran Ananthpur Bacche][17], May 25 2022

CROSSREFS

Cf. [A000010][20], [A000217][12], [A002088][13], [A048290][32], [A051953][4].

Sequence in context: [A347877][33] [A167180][34] [A091271][35] * [A050052][36] [A071349][37] [A282737][38]

Adjacent sequences: [A063982][39] [A063983][40] [A063984][41] * [A063986][42] [A063987][43] [A063988][44]

KEYWORD

nonn

AUTHOR

[Labos Elemer][45], Sep 06 2001

EXTENSIONS

Corrected by [Robert G. Wilson v][25], Dec 13 2006

STATUS

approved

[Lookup][3] [Welcome][46] [Wiki][47] [Register][48] [Music][49] [Plot 2][50] [Demos][51] [Index][52] [WebCam][53] [Contribute][54] [Format][55] [Style Sheet][56] [Transforms][57] [Superseeker][58] [Recents][59]

[The OEIS Community][60]

Maintained by [The OEIS Foundation Inc.][61]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.


*[excerpt ends; 1429 characters not shown — see `research/sources/oeis-A063985-partial-sums-n-minus-phi.full.md`]*
