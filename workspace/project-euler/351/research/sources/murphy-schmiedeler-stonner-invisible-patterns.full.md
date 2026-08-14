<!-- source: https://www.siam.org/media/i1thfsyh/s136404pdf.pdf | converted from PDF -->

First Occurrence and Frequency of Invisible Lattice Point Patterns1
 Nolan Murphy∗ , Lauren Schmiedeler† , and Ellen Stonner‡
2
 Project Advisor: Benjamin Hutz
§
3

4
 Abstract. Consider a “forest” of inﬁnitely thin trees arranged on the lattice Z × Z. If you are standing at the5 origin, (0, 0), not all trees are visible despite the fact that they are inﬁnitely thin. In particular,6 of the trees all lying on a line through (0, 0), only one such point is visible. In this article we7 conclusively classify all closest occurring invisible rectangular n×m blocks of points for 1 ≤ n, m ≤ 4.8 This (partially) resolves a question posed by Goins-Harris-Kubik-Mbirika. Furthermore, we compile9 statistics for all occurring arrangements up to size 4 × 4 and discuss interesting patterns that appear10 in that data.11
 1. Introduction. For inﬁnitely thin trees located on integer lattice points of a coordinate12 grid, with trees labeled by their lattice coordinates, (x, y), the trees visible from the origin13 are exactly the coordinates with gcd(x, y) = 1 (Theorem 2.1). The main focus in this area of14 research is determining the density and patterns which occur in the invisible trees. As this15 problem is entirely symmetric we will only consider what happens in the ﬁrst quadrant.16 This problem was ﬁrst addressed in the 19th century by a number of people with Ces`aro17 credited as the ﬁrst to pose this version of the problem in 1881 [2]. In particular, Ces`aro18 proved that any given point (x, y) has probability approaching 1
ζ(2) = 6
π2 ≈ 0.608 of being19 visible, where ζ(s) is the Riemann zeta function. In 1971, Herzog and Stewart characterized20 patterns of visible and invisible points, which remains the main motivation for current work in21 this area [5]. In 1976, Apostol [1, Theorem 5.29, p. 119] showed that there can be arbitrarily22 large square arrays of invisible points. In 1990, Schumer [7] used the Chinese Remainder23 Theorem to ﬁnd 3 × 3 blocks of invisible points (quite far from the origin) and questioned24 whether utilizing similar methods would be possible for 4 × 4 blocks due to the complexity25 of his calculations. Goodrich-Mbirika-Nielsen [4] took up the challenge using similar methods26 to ﬁnd a 4 × 4 and even a 5 × 5 invisible block, albeit both quite far from the origin. Goins-27 Harris-Kubik-Mbirika [3] pose the question of ﬁnding the nearest invisible forest of dimension28 n × m; this last question is resolved in this article for 1 ≤ m, n ≤ 4.29 A quick computer search can ﬁnd the closest occurrence of all n × m invisible blocks for30 1 ≤ n, m ≤ 3 since we need only search up to the ﬁrst 3 × 3 invisible block occurring at31 (x, y) = (1274, 1308). This search is suﬃcient as all smaller invisible blocks will occur before32 or within a 3 × 3 invisible block. However, ﬁnding the nearest invisible blocks of large size33 becomes computationally interesting. Our goal is to conclusively classify all closest occurring34 invisible rectangular blocks of points for 1 ≤ n, m ≤ 4.35 The paper is organized as follows. In Section 2, the fundamental mathematical results as36
 ∗Department of Mathematics and Statistics, Saint Louis University, St. Louis, MO 63103 (nolan.murphy@slu.edu)
†Department of Mathematics and Statistics, Saint Louis University, St. Louis, MO 63103 (lau-
ren.schmiedeler@slu.edu)
‡Department of Mathematics and Statistics, Saint Louis University, St. Louis, MO 63103 (ellen.stonner@slu.edu)
§Department of Mathematics and Statistics, Saint Louis University, St. Louis, MO 63103 (benjmain.hutz@slu.edu)

 Copyright © SIAM
  Unauthorized reproduction of this article is prohibited

274
 well as the computational framework is described. This section includes the data table on37 the closest (radial) occurrence of n  m invisible rectangles. In Section 3, the mathematical38 explanations for why certain patterns do not occur are examined. In Section 4, the dierence39 between closest invisible forests measured radially versus measured lexicographically is ad-40 dressed. This section also includes the table containing all the lexicographically closestn  m41 invisible rectangular blocks for 1 n; m  4. Finally in Section 5, the frequency of occurrence42 of all the possible invisible patterns up to size 4 4 is examined empirically. The full data for43 all 4  4 invisible patterns is available as an auxilary csv le.44 Note that all decimal values are rounded to 6 signicant gures.45
 2. Computing/Data Gathering. This section describes the computational method used46 to examine all occurring invisible patterns up to size 4 4 for 0  x; y  24;000;000. The47 main program, available upon request, was written in C and run on the Saint Louis University48 High Performance Computing Cluster. The program recorded the rst occurrence of each of49 the possible 4 4 patterns, of which there are 216 = 65536, both according to radial distance50 from (0; 0) and lexicographically. Additionally, the frequency of each pattern in the domain51 was also recorded. The statistics of the data is discussed in Section 5. Note that any size52 pattern is referenced by the coordinates of its lower left hand corner.53 The two main obstacles to overcome are the number of computations to perform and54 the memory problem due to the amount of data being produced. Heavy use is made of the55 symmetry of this problem. As Theorem 2.1 proves, whether any given (x; y ) is invisible is56 a greatest common divisor computation. Thus, determining the 4 4 pattern at any given57 (x; y ) requires 16 gcd calculations. Determining the 4 4 pattern of a point within that58 square should make use of the calculations already performed. However, storing the result of59 the gcd calculation of every single point in the search space is not feasible. Our solution to60 this memory issue is described in Section 2.2. The number of computations is dominated by61 calculating the gcd of each pair (x; y ). We used a basic Euclidean Algorithm method whose62 number of operations grows logarithmically with max(x; y ) and did not make an attempt to63 analyze or optimize these calculations.64 It should be noted that having the data for 4 4 patterns is sucient to have the data for65 all m  n patterns for 1 m; n  4. Statistics for smaller squares are included in Section 5.66
 2.1. Determining if a point is invisible. The following theorem is well known in this area67 and is included for completeness.68
 Theorem 2.1 ([3, Proposition 3]). A point in the lattice is visible if and only if the greatest69 common divisor (gcd) of itsx and y coordinates is 1.70
 Corollary 2.2. The only invisible rectangles with(x; y ) on the diagonal are size1  1.71
 Proof. If x = y, then gcd( x; y + 1) = gcd( x + 1; y ) = 1.72
 2.2. Working with patterns/mask values. The general principle for keeping track of73 invisible patterns is to assign a 16-bit integer to each lower left hand (x; y ) coordinate. Each74 bit represents whether one of the 16 points in the square is invisible or visible. The bit values75 are assigned as follows:76

275
 (2.1)
 8 4 2 1
128 64 32 16
2048 1024 512 256
32768 16384 8192 4096

We call the 16-bit integer themask value associated to the pattern. A corresponding mask77 value and pattern is given in the following example.78
 Example 2.3.The pattern79
 (2.2)
  
 
 
 

is given by the mask value80
 1 + 8 + 32 + 64 + 512 + 1024 + 4096 + 32768 = 38505 :

In designing a program to solve this problem, the rst challenge is tracking the location of81 each point in a 4 4 array. Using for loops for both thex and y axes means each new position82 necessitates knowing values for all surrounding relevant points to keep accurate counts. This83 requires unreasonably large amounts of memory and high computer performance specications84 to calculate and store all of the values for every 4 4 array at once.85 For example, storing 1 `bit' value for each point in a 1 million by 1 million lattice requires86 250 GB of memory, and storing each value as an int uses 8 TB. By storing the value as bits,87 one gcd calculation can contribute to 16 dierent lower left hand corners without additional88 calculation.89 Additionally, we introduce a wrapping system which only keeps the values of 4 columns at90 a time. That is, after the completion of the column for loop, the data for column 5 writes to91 the memory that contains column 1. This ensures the values do not override their neighbors92 until the full 4  4 array has been calculated and recorded accordingly and keeping total93 memory requirements reasonable.94 The entire program only saves the rst location (both radial distance and lexicographic95 order) and count of each 4 4 pattern, in order to eciently utilize storage space. Furthermore,96 we utilize the symmetry of the problem (gcd(x; y ) = gcd( y; x)) and only work with the ( x; y )97 points on or above the diagonaly = x .98 The nal statistics expand this data under symmetry to the whole rst quadrant. To99 avoid extensive live runtime of our program, we split the search space into separate blocks to100 run concurrently on the Saint Louis University High Performance Cluster, and compile the101 separate runs into one overall data le.102 Our data encompasses an integer lattice of 24 million by 24 million. The computation of103 our results took 491 days of CPU time on SLUs High Performance Cluster utilizing 112 cores104

276
 (further specs on the compute nodes is unavailable). The table below lists the location of the105 rst occurrence of each m  n forest, as well as its total number of occurrences in our search106 space. Notice as the size of the forest increases, the occurrence total decreases signicantly.107 Our research also conrms the work of Eric Weisstein in the \Visible Point" entry of the108 MathWorld website, who posited the rst location (with 0 < x < y ) of a 4  4 forest to be109 at (7247643; 10199370). We found the rst ve occurrences by distance from (0; 0) of 4  4110 invisible forests (and the rst 10 after diagonal symmetry is considered):111 (7247643, 10199370), (6349914, 13125369), (13449225, 13458288),112 (3268473, 21374352), (16799913, 22339875).113
 Table 2.1
Invisible Rectangles

Invisible Rectangle Pattern (§,y) of Closest Total Count Prop of Total
(Width  Height) Value Occurrence Rectangles
11 32768 (2, 2) 225833983043489 0.392073
12 34816 (2, 6) 61505212491040 0.106780
13 34944 (2, 6) 31371300360510 0.0544641
14 34952 (2, 30) 7157758947052 0.0124267
21 49152 (6, 2) 61505212491040 0.106780
22 52224 (14, 20) 1237398519088 0.00214826
23 52416 (54, 230) 42011981298 7:29375  10  5

24 52428 (174, 825) 873069048 1:51574  10  6

31 57344 (6, 2) 31371300360510 0.0544641
32 60928 (230, 54) 42011981298 7:29375  10  5

33 61152 (1274, 1308) 989290450 1:71752  10  6

34 61166 (47859, 12824) 394255 6:84470  10  10

41 61440 (30, 2) 7157758947052 0.0124267
42 65280 (825, 174) 873069048 1:51574  10  6

43 65520 (47859, 12824) 394255 6:84470  10  10

44 65535 (7247643, 10199370) 10 1:73611  10  14

As the data for the 1 1 invisible rectangles in Table 2.1 indicates, the proportion of total114 invisible points is 0:392073; thus approximately 40 percent of the points in the lattice are115 invisible. Conversely, the proportion of total visible points is 0:607927; thus approximately 60116 percent of the points in the lattice are visible.117 Sequences for the radial minimalx and y coordinates for 2 2, 3  3, and 4  4 invisible118 forests were added to the On-line Encyclopedia of Integer Sequences as sequences A325602,119 A325603, A325604, A325605, A325606, and A325607.120
 3. Non-Occurring Patterns. It is known that any given n  m invisible rectangle oc-121 curs through a simple application of the Chinese Remainder Theorem (see, for example, [6,122 Theorem 2.4]): choose which distinct primes divide which pairs of coordinates and solve the123 congruence equations forx and y. In this section we look at the possible patterns that do not124 arise in our data and prove that they do not ever occur. The following table summarizes the125 proportion of patterns that did not occur.126 All of these non-occurring patterns can be explained by examining the possible patterns127 modulo 2. In particular, the one not occurring 2 2 pattern is the pattern with all four points128

277
 Table 3.1
Non-Occurring Patterns

Size Total Number Number of Patterns Proportion of Total
of Patterns That Do Not Occur
2  2 24 = 16 1 0.0625
3  3 29 = 512 135 0.263672
4  4 216 = 65536 50626 0.772491

visible. If this 2  2 pattern is contained within any larger pattern, then it cannot occur.129
 Lemma 3.1. No patterns with 2  2 square(s) of visible points occur.130
 Proof. Let (x, y ) be a point in the ﬁrst quadrant with x, y 2 Z. If the greatest common131 divisor of at least 1 pair of coordinates in the 2  2 square132
 (3.1) (x, y + 1) (x + 1, y + 1)
(x, y ) (x + 1, y )

is greater than 1, then the 2  2 square is not visible.133 There are 4 possible cases:134  Case 1: x is even and y is even. Therefore, gcd(x, y )  2.135  Case 2: x is even and y is odd. Therefore, y + 1 is even and gcd(x, y + 1)  2.136  Case 3: x is odd and y is even. Therefore, x + 1 is even and gcd(x + 1, y )  2.137  Case 4: x is odd and y is odd. Therefore, x + 1 and y + 1 are even so that gcd( x +138 1, y + 1)  2.139 In all possible cases, at least 1 pair of coordinates has a greatest common divisor of at140 least 2. Therefore, you cannot get a 2  2 square of visible points.141
 However, this is not the entire story. For example, any 4  4 pattern containing the142 following 4 visible points also cannot occur143
 (3.2)
  

 

This is because these four locations are the same as a 2  2 visible rectangle when taking144 modulo 2 and, as in the proof of the lemma, at least 1 of these 4 must have a gcd of at least145 2 and so must be invisible. We formalize this notion with the following notation. Given a146 2  2 block such that x, y 2 Z, x and y can be even or odd and form an ordered pair in 1 of 4147 combinations:148
 (even,  even),  (even,  odd),  (odd,  even),  (odd,  odd)

278
 Let the four types be calledA, B , C , and D which can be assigned arbitrarily. Then a149 4 4 pattern contains the following types of coordinate pairs (after the possible re-assignment150 of type names).151
 (3.3)
 C D C D
A B A B
C D C D
A B A B

Corollary 3.2. Any pattern that contains at least one visible point of every type A, B , C ,152 and D cannot occur.153
 There are 44 = 256 possible ways to choose one coordinate pair of each type and these154 possibilities cannot all exist. Checking all possible patterns that do not occur in our data,155 every such pattern is explained in this way. This is a special case of the more general theorem156 that says the only non-occurring patterns are those which form complete residue classes of157 pairs modulo some prime [5, Theorem 1].158
 Corollary 3.3. Any occurring n  m rectangle must have at least  n2    m 2  invisible points.159
 Proof. This is a pigeonhole principle argument. An occurring pattern cannot have every160 type A; B; C; D occur. We must have all invisiblex coordinates as even or odd and all invisible161 y coordinates as even or odd. Even and odd are the two categories which integer values are162 sorted into. Given three or more integers, i.e., one more than the number of categories present,163 there must exist at least two even integers or at least two odd integers by the pigeonhole164 principle.165 All (even, even) points are invisible. The fewest possible invisible points then occur when166 the fewest (even, even) points are present within the chosen rectangle, assuming a worst case167 where no other pair types are invisible. For consecutive points, the fewest occurrences of even168 integers in either direction is one half the dimension, rounded down for odd dimensions. Thus,169 there are  n2  and  m 2  minimum possible occurrences, respectively.170
 Proposition 3.4. Every possible occurring pattern occurs within radial distance171
 8
><

>:
 25:24 2  2
6688:16 3  3
12512213:14 4 4

from the origin (0; 0).172
 Proof. Since the data includes the occurrence of all patterns that possibly occur, we take173 the maximum of the minimal distance of each occurring pattern in our data.174
 Theorem 3.5. In a 4  4 square, patterns with less than 4 invisible points cannot exist.175
 Proof. In a 4  4 square, each of A , B , C , and D occur exactly 4 times. For any set of176 invisible points of cardinality less than 4, there remain at least 1 visible point of each typeA ,177

279
 B, C, and D, which is impossible. Therefore, in a 4  4 square there must exist at least 4178 invisible points.179
 4. Radial Distance versus Lexicographic Distance. So far we have discussed nding the180 rst occurring pattern as measured by minimal distance to (0; 0). We could also consider181 \minimal" under the lexicographic ordering. In other words, for a given (occurring) pattern,182 what is the smallest possible x value for which the pattern occurs? This problem is less183 amenable to computation as there is no simple way to enumerate all points up to some184 distance under the lexicographic ordering since there are innitely many coordinates ( x; y)185 for any xed x value. However, for invisible rectangles, it is possible to prove the smallest186 occurring pattern location by examining prime divisibility properties. The following theorem187 summarizes the results.188
 Theorem 4.1. The following table provides the rst occurrence of each m  n rectangle189 under le§icographic ordering x > y .190
 Table 4.1
First Occurrences of Invisible Rectangles

Invisible Rectangle (x,y) of Closest Invisible Rectangle (x,y) of Closest
1×1 (2, 2) 3x1 (6, 2)
1×2 (2, 6) 3x2 (104, 740)
1×3 (2, 6) 3x3 (104, 6200)
1×4 (2, 30) 3x4 (662, 128930788)
2×1 (6, 2) 4x1 (30, 2)
2×2 (14, 20) 4x2 (230, 7104)
2×3 (20, 384) 4x3 (644, 22984014)
2×4 (33, 15554) 4x4 (8853, 5583967323)

Proof. For each m n rectangle we perform the following steps to nd the rst occurrence.191 1. Determine conditions on the number of distinct prime divisors of x; x + 1; : : : ; x + n.192 2. Find the smallest x satisfying those minimal conditions using Sage.193 3. Find the smallest y that realizes an m  n invisible rectangle using Sage.194 As the second and third steps are searches, it is only the rst step that requires proof. Recall195 that a point is invisible if and only if gcd( x; y) 6= 1. In particular x needs at least one prime196 divisor. For 1  n  4, x = 2 satises the necessary condition.197 For 2  n rectangles, x; x + 1 ; : : : ; x + n must share a common divisor with y and y + 1.198 Since gcd( y; y + 1) = 1, each of x; x + 1; : : : ; x + n has at least two prime divisors. This results199 in the smallest x values200
 (n; x ) = (1 ; 6); (2 ; 14); (3; 20); (4; 33):

For 3  n rectangles, x; x + 1; : : : ; x + n must share a common divisor with y, y + 1, and201 y + 2. So either x; x + 1 ; : : : ; x + n have at least three distinct prime divisors, or the values of202 x; x + 1 ; : : : ; x + n which are even have at least two prime divisors, one of which is 2, and the203 values x; x + 1; : : : ; x + n which are odd have at least three distinct odd prime divisors. This204 results is the smallest x values205

280
 (n; x ) = (1; 6); (2; 104); (3; 104); (4; 662):

For 4  n rectangles, x; x + 1; : : : ; x + n must share a common divisor withy , y + 1, y + 2,
and y + 3. So either x; x + 1; : : : ; x + n have at least four distinct prime divisors, or less
when one of those divisors is 2 or 3. There are six possible residue classes modulo 2 and 3
for x which give conditions on the number of prime divisors. However, the least number of
prime divisors needed for eachx; x + 1; : : : ; x + n is three, and when n = 4, at least one of
x; x + 1; : : : ; x + n must have four distinct prime divisors larger than 3. This results in the
smallest x values
 (n; x ) = (1 ; 30); (2; 230); (3; 644); (4; 8853):

Proposition 4.2.For any given x coordinate which satises the necessary prime divisor206 conditions for which an m  n rectangle may appear, there are innitely many y coordinates207 for which (x; y ) is the lower left hand corner of an m  n invisible rectangle.208
 Proof. Given the factorizations of x; x + 1; x + 2 ; x + 3, we may set-up a system of linear209 congruences to solve fory . This system may be solved via the Chinese Remainder Theorem,210 which provides an innite set of solutions.211
 Example 4.3.Consider x = 20 for a 2  3 rectangle. Then we have 20 = 22  5, 21 = 3 7,212 and 22 = 2 11, so we have the system of congruences213
 y = 0 (mod 2  3)

y =  1 (mod 5  7  11) :

This results in the solution214
 y  384 (mod 2310):

Notice that we could also have had the system215
 y = 0 (mod 2  7)

y =   1 (mod 3  5  11):

This results in the solution216
 y  1484 (mod 2310):

Another interesting question is, for the coordinates of anm  n invisible rectangle, what217 is the smallest number of prime divisors that are possible? As a simple upper bound, if218

281
 every integer x; x + 1; : : : ; x + n has at least m prime divisors, then using the the Chinese219 Remainder Theorem, a system of congruences can be constructed and solved (fory ) to nd220 an explicit invisible rectangle. However, this is clearly not optimal as Example 4.3 shows221 and for the simple reason that every second number is divisible by 2, so not every coordi-222 nate needs m prime divisors. An alternate formulation of this problem is to ask, what is223 the fewest number of primes needed to divide every term in a sequence of consecutive inte-224 gers? This problem has received some study under the form of the question: what is the225 longest sequence of consecutive integers divisible by the rstk primes (OEIS A058989)? The226 rst answers are ( f2g; 1); (f2; 3g; 3); ( f2; 3; 5g; 5) ; (f2; 3; 5; 7g; 9); ( f2; 3; 5; 7; 11g; 13). This does227 not quite resolve our problem since the primes that divide our consecutive integers do not228 need to be from among the rst k primes. There is an interesting discussion of this more229 general problem in Quanta Magazine (https://www.quantamagazine.org/solution-the-prime-230 rib-problem-20170908/). For example the 13 numbers 24; : : : ; 36 are all divisible by the primes231 f2; 3; 5; 29; 31g. We can prove that this is optimal. We can arrange 2; 3; 5 to divide 11 of 13232 consecutive integers starting atx by setting it up as233
 x  0 (mod 2);

x  0 (mod 3);

x + 1  0 (mod 5):

Since there are only two numbers leftx + 5; x + 7, they are odd and must have distinct prime234 divisors, so we need at least ve primes. By working through the possible combinatorics,235 it can be determined that this arrangement results in the fewest possible number of primes.236 Note that the ve primes f2; 3; 5; 7; 11g can also solve this problem starting atx = 114, but237 this does not give the smallest solution. When the number of primes becomes seven, not238 only does the rst occurrence dier for smallest primes versus arbitrary primes, but so does239 the maximal number of consecutive integers divisible by the set. So the problems are truly240 dierent. This appears to a rich area of research and warrants study in a future project.241
 5. Frequency of Pattern Occurrence. In this section we make some empirical observa-242 tions about the frequency with which invisible patterns occur. An interesting open problem243 would be to prove these observations conclusively.244
 5.1. 2 2 patterns. There are 16 possible 2 2 patterns and all occur except the pattern245 with no invisible points. In particular, 93:75% of patterns occur. Interestingly, as seen in246 Table 5.1, the frequency with which a pattern occurs appears to depend only on the number247 of invisible points.248

282
 Table 5.1
2x2 Patterns

Number of Points Pattern Frequency
1 1024 0.125487
1 16384 0.125487
1 2048 0.125487
1 32768 0.125487
2 34816 0.0716601
2 49152 0.0716601
2 17408 0.0716601
2 3072 0.0716601
2 18432 0.0716601
2 33792 0.0716601
3 19456 0.0164857
3 35840 0.0164857
3 50176 0.0164857
3 51200 0.01648575
4 52224 0.00214826

5.2. 3 3 patterns. As seen in Table 5.2, the behavior of 3 3 patterns appears to be249 more complicated. There are 512 possible 3 3 patters and 73:63% of them occur. For 3 3250 patterns with six or more points, all possible patterns occur. The non-occurring patterns are251 completel† explained in Corollar† 3.2.252 In the 3 3 case, there was an overall pattern that the number of points determined253 the frequenc† with which a pattern occurred, but onl† up to a point. In other words, the254 frequenc† of pattern occurrence had a larger variation between number of points in the pattern255 compared to the variation in frequenc† within patterns with a xed number of points. In the256 following table we compile the frequenc† of occurrence of patterns groups b† t†pe of pattern.257 The pattern t†pe will be determined b† the lettersA, B ,C ,D representing (§; y) coordinates258 arranged in the following wa†:259
 (5.1) A B A
C D C
A B A

The following ndings use the operations \+" and \or" in addition to the lettersA ,B ,260 C ,D . \+" separates two necessar† conditions while \or" separates two or more possible261 conditions (one of which must be chosen). A single letter indicates that one point of that t†pe262 must be selected while a letter with a coecient in front of it indicates that two, three, or263 four points of that t†pe must be selected.264

283
 Table 5.2
3x3 Patterns

Number of Number of Pattern Types Proportion
Points Patterns
1 1 D 0.01230689
2 8 D + (A or B or C) 0.0152519
2 2 2B or 2C 0.0275588
3 26 D + (2A or (A+B) or (A+C) or (B+C)) 0.00329798
3 12 (2B + (A or C)) or (2C + (A or B)) 0.0185499
3 2 D + (2B or 2C) 0.0218479
4 44 A + B + C + D 0.000379761
4 28 (2A + (2B or 2C)) or 0.00367773
(A + ((2B + C) or (B + 2C)))
4 12 ((2B + D) + (A or C)) or 0.00405751
((2C + D) + (A or B))
4 1 2B + 2C 0.00735549
4 1 4A 0.0683364
5 40 (2A + B + C + D) or 2:82946 10 5

(3A + (B or C) + D)
5 32 (2A + B + C) or (3A + (2B or 2C)) 0.000408056
5 28 (2B + D + (2A or (A + C)) or 0.000436352
(2C + D + (2A or (A + B)))
5 4 A + 2B + 2C 0.000816114
5 1 2B + 2C + D 0.000844407
5 5 4A + (B or C or D) 0.0263134
6 16 3A + (B or C) + D 1:519132 10 6

6 16 3A + (2B + C) or (B + 2C)) 2:98136 10 5

6 32 (2A + ((2B + C) or (B + 2C) + D) or 3:13332 10 5

(3A + (2B or 2C) + D)
6 6 2A + 2B + 2C 5:96282 10 5

6 4 A + 2B + 2C + D 6:11476 10 5

6 10 4A + (2B or 2C or (B + C) 0.00452367
or (B + D) or (C + D))
7 16 3A + ((2B + C) or (B + 2C)) + D 1:64427 10 6

7 4 3A + 2B + 2C 3:16359 10 6

7 6 2A + 2B + 2C + D 3:22603 10 6

7 10 4A + ((B + C + D) or 0.000469330
(2B + (C or D)) or (2C + (B or D))
8 4 3A + 2B + 2C + D 1:31291 10 7

8 5 4A + ((2B + C + D) or 3:31089 10 5

(B + 2C + D) or (2B + 2C))
9 1 4A + 2B + 2C + D 1:71752 10 6

We were unable to ﬁnd any clear patterns in the 3 3 data, so we did not expand these265 computations to categorize all of the 4 4 visible patterns. Computing these in a similar266 fashion as the 3  3 patterns would be time-consuming to perform by hand because the267 number of diﬀerent proportions for 4 4 visible patterns with 9 to 14 points becomes large268 (see the data tables below).269 The following tables provide information on invisible 2 2, 3  3, and 4  4 patterns.270 They indicate that the number of points in a pattern relate to the proportion at which this271

284
 pattern occurs. For a proportion (proportion1) to be deemed \the same" as another proportion272 (proportion2), the absolute value of the dierence between proportion1 and proportion2 needs273 to be less than 1 percent of proportion1.274
 Table 5.3
2x2 Invisible Patterns

Number of Number of Number of Total Proportion of Number of
Points in Patterns that Patterns that Number of Total Patterns Dierent
Pattern Do Occur Do Not Occur Patterns that Do Occur Proportions
0 0 1 1 0 0
1 4 0 4 0.266667 1
2 6 0 6 0.4 1
3 4 0 4 0.266667 1
4 1 0 1 0.0666667 1
Total 15 1 16 1 4

Table 5.4
3x3 Invisibe Patterns

Number of Number of Number of Total Proportion of Number of
Points in Patterns that Patterns that Number of Total Patterns Dierent
Pattern Do Occur Do Not Occur Patterns that Do Occur Proportions
0 0 1 1 0 0
1 1 8 9 0.00265252 1
2 10 26 36 0.0265252 2
3 40 44 84 0.106101 3
4 86 40 126 0.228117 5
5 110 16 126 0.291777 6
6 84 0 84 0.222812 6
7 36 0 36 0.0954907 4
8 9 0 9 0.0238727 2
9 1 0 1 0.00265252 1
Total 377 135 512 1 30

285
 Table 5.5
4x4 Invisible Patterns

Number of Number of Number of Total Proportion of Number of
Points in Patterns that Patterns that Number of Total Patterns Dierent
Pattern Do Occur Do Not Occur Patterns that Do Occur Proportions
0 0 1 1 0 0
1 0 16 16 0 0
2 0 120 120 0 0
3 0 560 560 0 0
4 4 1816 1820 0.000268258 1
5 48 4320 4368 0.0032191 2
6 264 7744 8008 0.017705 4
7 880 10560 11440 0.0590168 7
8 1974 10896 12870 0.132385 12
9 3120 8320 11440 0.209242 16
10 3528 4480 8008 0.236604 20
11 2832 1536 4368 0.189927 26
12 1564 256 1820 0.104889 42
13 560 0 560 0.0375562 53
14 120 0 120 0.00804775 30
15 16 0 16 0.00107303 7
16 1 0 1 6:70646 10 5 1
Total 14911 50625 65536 1 221

6. Conclusion. In this paper, we ﬁnd the ﬁrst occurrence of invisible rectangles of size275 m  n for 1  m; n  4. In addition, we record the invisible patterns and their corresponding276 frequencies of occurrence up to (x; y ) = (24000000; 24000000), and we observe and explain the277 patterns that do not occur. We gather statistics that demonstrate nice patterns relating the278 number of points in a pattern to the proportion at which this pattern occurs, and the next279 step would be attempting to prove whether or not these patterns hold generally. We ﬁnd the280 ﬁrst occurring 4 4 invisible rectangle computationally, but based on the expected growth281 rate between previous invisible squares, ﬁnding the ﬁrst occurring 5 5 invisible rectangle282 does not seem like a feasible computational problem with the current method. Therefore, we283 would need to utilize a diﬀerent approach than brute force to ﬁnd the ﬁrst occurrence of this284 next invisible block. One consideration might be to look where small, distinct prime divisors285 occur most commonly in invisible rectangles to narrow the search criteria. For example, the286 x and y coordinates of the lower left point of most invisible rectangles are divisible by 2.287
 REFERENCES288
 [1] T. Apostol , Introduction to Analytic Number Theory , Springer-Verlag, 1976.289 [2] E. Ces `aro , Mathesis, PhD thesis, 1881.290 [3] E. H. Goins, P. E. Harris, B. Kubik, and A. Mbirika, Lattice point visibility on generalized lines of291 sight , Amer. Math. Monthly, 125 (2018), pp. 593{601, https://doi.org/10.1080/00029890.2018.1465760,292 https://doi.org/10.1080/00029890.2018.1465760.293 [4] A. Goodrich, a. Mbirika, and J. Nielsen, New methods to nd patches of invisible integer lattice294 points, Involve, 14 (2021), pp. 283{310, https://doi.org/10.2140/involve.2021.14.283, https://doi.org/295 10.2140/involve.2021.14.283.296

286
 [5] F. Herzog and B. M. Stewart, Patterns of visible and nonvisible lattice points, Amer. Math. Monthly,297 78 (1971), pp. 487{496, https://doi.org/10.2307/2317753, https://doi.org/10.2307/2317753.298 [6] B. Hutz , An experimental introduction to number theory , vol. 31 of Pure and Applied Undergrdauate299 Texts, American Mathematical Socity, 2018.300 [7] P. Schumer, Strings of strongly composite integers and invisible lattice points, College Math. J., 21 (1990),301 pp. 37{40, https://doi.org/10.2307/2686720, https://doi.org/10.2307/2686720.302

287
