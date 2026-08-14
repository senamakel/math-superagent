<!-- source: https://oeis.org/search?q=A094798&fmt=text | converted from plain text -->

# Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/

Search: a094798
Showing 1-9 of 9

%I A094798 #42 Oct 18 2023 02:13:45
%S A094798 1,1,1,1,1,1,1,1,1,2,4,5,6,7,8,9,10,11,12,12,13,13,13,13,13,13,13,13,
%T A094798 13,13,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,16,
%U A094798 16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18
%N A094798 Number of times 1 is used in writing out all the numbers 1 through n.
%C A094798 The number of 1's required to write all integers of n or fewer digits (i.e., the sequence a(9), a(99), a(999), ...) is 1, 20, 300, 4000, ..., which is A053541. - Jason D. W. Taff (jtaff(AT)jburroughs.org), Dec 05 2004
%C A094798 A014778 gives the fixed points. - _David Wasserman_, Feb 22 2005
%C A094798 Partial sums of A268643. - _Robert Israel_, Oct 28 2016
%H A094798 Harvey P. Dale, <a href="/A094798/b094798.txt">Table of n, a(n) for n = 1..1000</a>
%F A094798 G.f. g(x) satisfies g(x) = x/((1-x)*(1-x^10)) + ((1-x^10)/(1-x))^2*g(x^10). - _Robert Israel_, Oct 28 2016 [corrected by _Fabio Visonà_, Aug 10 2022]
%p A094798 nones:=proc(n) local nn,c,j: nn:=convert(n,base,10): c:=0: for j to nops(nn) do if nn[j]=1 then c:=c+1 else end if end do: c end proc: a:=proc(n) options operator, arrow: add(nones(k),k=1..n) end proc: seq(a(n),n=1..75); # _Emeric Deutsch_, Mar 01 2008
%p A094798 ListTools:-PartialSums([seq(numboccur(1,convert(n,base,10)),n=1..100)]); # _Robert Israel_, Oct 28 2016
%t A094798 Accumulate[Table[DigitCount[n,10,1],{n,80}]] (* _Harvey P. Dale_, Sep 27 2013 *)
%o A094798 (Python)
%o A094798 from itertools import accumulate, count, islice
%o A094798 def f(_, n): return _ + str(n).count("1")
%o A094798 def agen(): yield from accumulate(count(1), f)
%o A094798 print(list(islice(agen(), 75))) # _Michael S. Branicky_, Aug 09 2022
%o A094798 (PARI) a(n) = sum(k=1, n, #select(x->(x==1), digits(k))); \\ _Michel Marcus_, Oct 03 2023
%Y A094798 Cf. A014778, A053541, A268643.
%K A094798 easy,base,nonn
%O A094798 1,10
%A A094798 _Lekraj Beedassy_, Jun 11 2004

%I A014778 #55 Jun 11 2026 00:58:31
%S A014778 0,1,199981,199982,199983,199984,199985,199986,199987,199988,199989,
%T A014778 199990,200000,200001,1599981,1599982,1599983,1599984,1599985,1599986,
%U A014778 1599987,1599988,1599989,1599990,2600000,2600001,13199998,35000000
%N A014778 Numbers k equal to the number of 1's in the decimal digits of all numbers <= k.
%C A014778 The full list of 84 terms is given in the b-file.
%C A014778 It can be proved that this sequence is finite. (The main idea of the proof is that the number of 1's used in positive integers <= k is greater than or equal to A(k) = (1/10)*(number of digits in positive integers from 1 to k) = (1/10) Sum_{i=1..k} (1+floor(log_10 i)). By considering the area below a logarithmic function and the corresponding integral, it can be shown that A(k)/k goes to infinity.) - _Joseph L. Pe_, Nov 05 2002
%C A014778 Fixed points of A094798. Sequence consists of six runs of ten consecutive numbers, ten pairs of consecutive numbers and four isolated numbers. - _David Wasserman_, Jun 29 2007
%D A014778 Maurice Protat, "Des Olympiades à l'Agrégation", Editions Ellipses, Paris 1997, p. 183.
%H A014778 Graeme McRae, May 26 2007, <a href="/A014778/b014778.txt">Table of n, a(n) for n = 1..84</a> (complete sequence)
%H A014778 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023.
%H A014778 Ed Pegg Jr. and Eric W. Weisstein, <a href="https://mathworld.wolfram.com/news/2004-10-13/google/">Mathematica's Google Aptitude</a>, MathWorld Headline news, Oct 13 2004.
%e A014778 a(5)=199983 because the number of 1's in the decimal digits of the numbers from 0 to 199983 is 199983 and this is the 5th such number.
%t A014778 Join[{0},With[{nn=35*10^6},Position[Thread[{Accumulate[ DigitCount[ Range[nn],10,1]], Range[nn]}],{x_,x_}]]]//Flatten (* _Harvey P. Dale_, Oct 14 2017 *)
%o A014778 (Python)
%o A014778 from itertools import count, islice
%o A014778 def agen(s=0): # generator of terms
%o A014778     yield from (k for k in count(0) if (s:=s+str(k).count('1'))==k)
%o A014778 print(list(islice(agen(),26))) # _Michael S. Branicky_, Oct 02 2023
%Y A014778 Cf. A101639, A101640, A101641, A130427, A130428, A130429, A130430, A130431; cf. A130432 for the number of numbers in these sequences.
%Y A014778 Cf. A094798.
%Y A014778 Cf. A165617 for the sequence generalized to an arbitrary base. - Martin J. Erickson (erickson(AT)truman.edu), Oct 08 2010
%K A014778 base,fini,nonn,full
%O A014778 1,3
%A A014778 Yves Babe, Maurice Protat, _Olivier Gérard_
%E A014778 Corrected and extended by Deepan Majmudar (deepan.majmudar(AT)hp.com), Nov 19 2004
%E A014778 41 further terms from _Ryan Propper_, Dec 07 2004, who observed that there are no more terms <= 10^9
%E A014778 The final (84th) term 1111111110 was sent by Lambrecht Kok (L.P.Kok(AT)rug.nl), Jan 13 2005. He says: "H. van Haeringen and I showed that this list of 84 terms is complete on Dec 15 2004".
%E A014778 Independently shown to be complete by _Ryan Propper_ and Vaughan Pratt, Jan 08 2005
%E A014778 Edited by _M. F. Hasler_, Feb 12 2013

%I A053541 #67 Jul 04 2026 07:44:07
%S A053541 1,20,300,4000,50000,600000,7000000,80000000,900000000,10000000000,
%T A053541 110000000000,1200000000000,13000000000000,140000000000000,
%U A053541 1500000000000000,16000000000000000,170000000000000000,1800000000000000000,19000000000000000000,200000000000000000000
%N A053541 a(n) = n*10^(n-1).
%C A053541 This sequence gives the number of 1's (or any other nonzero digit) required to write all integers from 0 up to 10^n-1. - Jason D. W. Taff (jtaff(AT)jburroughs.org), Dec 05 2004 (improved by _Bernard Schott_, Nov 17 2022)
%C A053541 The corresponding number of 0's required to write all these integers from 0 up to 10^n-1 is A033714(n). - _Bernard Schott_, Nov 17 2022
%D A053541 Albert H. Beiler, Recreations in the Theory of Numbers, Dover, N.Y., 1964, pp. 194-196.
%H A053541 Vincenzo Librandi, <a href="/A053541/b053541.txt">Table of n, a(n) for n = 1..100</a>
%H A053541 Frank Ellermann, <a href="/A001792/a001792.txt">Illustration of binomial transforms</a>.
%H A053541 <a href="/index/Rec#order_02">Index entries for linear recurrences with constant coefficients</a>, signature (20,-100).
%F A053541 a(n) = 20*a(n-1) - 100*a(n-2), with a(0)=0, a(1)=1, a(2)=20.
%F A053541 From Jason D. W. Taff (jtaff(AT)jburroughs.org), Dec 05 2004: (Start)
%F A053541 a(n) = 10*a(n-1) + 10^(n-1).
%F A053541 a(n) = Sum_{k=1..n} k*binomial(n,k)*9^(n-k).
%F A053541 a(n) = A094798(10^n - 1). (End)
%F A053541 From _G. C. Greubel_, May 16 2019: (Start)
%F A053541 G.f.: x/(1-10*x)^2.
%F A053541 E.g.f.: x*exp(10*x). (End)
%F A053541 From _Amiram Eldar_, Oct 28 2020: (Start)
%F A053541 Sum_{n>=1} 1/a(n) = 10*log(10/9).
%F A053541 Sum_{n>=1} (-1)^(n+1)/a(n) = 10*log(11/10). (End)
%F A053541 a(n) = Sum_{k=1..n} A081045(k-1). - _Bernard Schott_, Nov 17 2022
%F A053541 a(n) = A002283(n-1) + A064748(n-1). - _Elmo R. Oliveira_, Oct 19 2025
%p A053541 seq(n*10^(n-1), n = 1 .. 40); # _Bernard Schott_, Nov 17 2022
%t A053541 f[n_]:=n*10^(n-1);f[Range[40]] (* _Vladimir Joseph Stephan Orlovsky_, Feb 09 2011*)
%t A053541 LinearRecurrence[{20,-100},{1,20},20] (* _Harvey P. Dale_, Aug 08 2023 *)
%o A053541 (Magma) [n*10^(n-1): n in [1..30]]; // _Vincenzo Librandi_, Jun 06 2011
%o A053541 (PARI) a(n)=n*10^(n-1) \\ _Charles R Greathouse IV_, Dec 05 2011
%o A053541 (SageMath) [n*10^(n-1) for n in (1..20)] # _G. C. Greubel_, May 16 2019
%o A053541 (GAP) List([1..20], n-> n*10^(n-1)); # _G. C. Greubel_, May 16 2019
%Y A053541 Cf. A001787, A033714, A038303, A053464, A053469, A081045, A094798.
%Y A053541 Cf. A002283, A064748.
%K A053541 easy,nonn
%O A053541 1,2
%A A053541 _Barry E. Williams_, Jan 15 2000
%E A053541 Offset changed from 0 to 1 by _Vincenzo Librandi_, Jun 06 2011

%I A094799 #5 Mar 31 2012 13:20:57
%S A094799 199981,1599981,35199981,500199981,501599981,535199981
%N A094799 First term of a run of 10 consecutive numbers such that for each m in the 10-tuple exactly m 1's are used in writing out all numbers 1 through m.
%C A094799 The sequence is complete. - _David Wasserman_, Jun 29 2007
%D A094799 M. Protat, Des Olympiades a l'Agregation, Nombre de "1", Problem 89, pp. 182-183, Ellipses, Paris 1997.
%Y A094799 Cf. A014778.
%Y A094799 Cf. A094798.
%K A094799 base,easy,fini,full,nonn
%O A094799 1,1
%A A094799 _Lekraj Beedassy_, Jun 11 2004

%I A331375 #32 May 26 2026 15:52:41
%S A331375 -1,0,0,0,0,0,0,0,0,0,0,2,3,4,5,6,7,8,9,10,9,9,7,6,5,4,3,2,1,0,0,1,0,
%T A331375 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
%U A331375 0,0,0,0,1,0,0,0,0,0,0,0,0,0,1
%N A331375 a(n) is the number of times the digit 1 appears in the concatenation of integers from 0 to n, minus the number of times the next most frequent digit appears.
%C A331375 Other than a(0) = 0 the digit 1 is the most frequently seen digit in the concatenation of the integers from 0 to n. See A094798 for the exact number of times. This sequence is the difference between that number and the number of times the next most frequent digit appears. For almost all numbers the next most frequent digit is 2. That only changes to the digit 0 once per order of magnitude, after reaching the number consisting of two or more 1's followed by 0. The digit 0 keeps this record for the next number, a repunit, after which the number of appearances of 2 again either equals or surpasses the number of appearances of 0.
%C A331375 When concatenating the integers from 0 to 10^k, with k >= 2, this sequence reaches its maximum value of 10^(k-1) at n = 10^k/5-1.
%H A331375 Scott R. Shannon, <a href="/A331375/b331375.txt">Table of n, a(n) for n = 0..10000</a>
%e A331375 a(0) = -1 as after '0' the digit 0 has appeared once while 1 has not appeared, so a(0) = 0 - 1 = -1.
%e A331375 a(10) = 0 as after '012345678910' the digits 0 and 1 have both appeared two times, so a(10) = 2 - 2 = 0.
%e A331375 a(11) = 2 as after '01234567891011' the digit 1 has appeared four times and the digit 0 two times, so a(11) = 4 - 2 = 2.
%Y A331375 Cf. A094798, A007376.
%K A331375 sign,base
%O A331375 0,12
%A A331375 _Scott R. Shannon_, Jan 14 2020
%E A331375 Deleted a conjectured but incorrect g.f. and recurrence. - _N. J. A. Sloane_, Jan 17 2020

%I A094800 #5 Mar 31 2012 13:20:57
%S A094800 0,200000,2600000,35000000,35200000,500000000,500200000,502600000,
%T A094800 535000000,535200000
%N A094800 First term of a run of exactly two consecutive numbers such that for each m in the run, exactly m 1's are used in writing out all numbers 1 through m.
%C A094800 Numbers n such that n and n+1 are members of A014778, but n-1 and n+2 are not. - David Wasserman
%D A094800 M. Protat, Des Olympiades a l'Agregation, Nombre de "1", Problem 89, pp. 182-183, Ellipses, Paris 1997.
%Y A094800 Cf. A014778.
%Y A094800 Cf. A094798, A094799, A094801.
%K A094800 base,easy,fini,full,nonn
%O A094800 1,2
%A A094800 _Lekraj Beedassy_, Jun 11 2004
%E A094800 Corrected by _David Wasserman_, Jun 29 2007. There are no further terms.

%I A094801 #8 Feb 14 2021 04:44:56
%S A094801 13199998,117463825,513199998,1111111110
%N A094801 Numbers k such that k is a term of A014778, but k-1 and k+1 are not.
%D A094801 M. Protat, Des Olympiades a l'Agregation, Nombre de "1", Problem 89, pp. 182-183, Ellipses, Paris 1997.
%Y A094801 Cf. A014778.
%Y A094801 Cf. A094798, A094799, A094800.
%K A094801 base,easy,fini,full,nonn
%O A094801 1,1
%A A094801 _Lekraj Beedassy_, Jun 11 2004
%E A094801 Corrected by _David Wasserman_, Jun 29 2007

%I A365097 #61 Oct 01 2023 07:58:23
%S A365097 2,4,25,181,421,3930,8177,102772,199981,3179142,5971945,143610511,
%T A365097 210826981,4754446846,8589934561,222195898593,396718580701,
%U A365097 13494919482970,20479999999961,764527028941797,1168636602822613,41826814261329722,73040694872113105,2855533828630999398
%N A365097 Smallest k > 1 such that the total number of digits "1" required to write the numbers 1..k in base n is equal to k.
%C A365097 a(10) = A014778(3), being the smallest term > 1 there.
%C A365097 An upper bound is a(n) <= A226238(n) = u, since the digits of u show there are u 1's in numbers 1..u (in base n). - _Kevin Ryde_, Sep 28 2023
%H A365097 Jon E. Schoenfield, <a href="/A365097/b365097.txt">Table of n, a(n) for n = 2..200</a>
%F A365097 For even n > 2, a(n) = 2*n^(n/2) - 2*n + 1. - _Jon E. Schoenfield_, Sep 30 2023
%e A365097 For n=2, the first k=2 positive integers are 1 = 1_2 and 2 = 10_2, which have a total of two 1's, so a(2) = 2.
%e A365097 For n=3, the first k=4 positive integers, which are 1_3, 2_3, 10_3, and 11_3, have a total of four 1's, which is equal to k, so a(3) = 4.
%e A365097 For n=4, a total of 25 1's occur in the first k=25 positive integers (they occur in 1_4, 10_4, 11_4, 12_4, 13_4, 21_4, 31_4, 100_4, 101_4, 102_4, 103_4, 110_4, 111_4, 112_4, 113_4, 120_4, and 121_4 = 25), so a(4) = 25.
%t A365097 a[n_] := Module[{k = 1, sum = 1}, While[sum == 1 || sum != k, k++; sum += Count[IntegerDigits[k, n], 1]]; k]; Array[a, 6, 2] (* _Amiram Eldar_, Aug 29 2023 *)
%o A365097 (Python)
%o A365097 from itertools import count
%o A365097 from sympy.ntheory.factor_ import digits
%o A365097 def A365097(n):
%o A365097     c, a, q, m = 1, 1, 0, 1
%o A365097     for k in count(2):
%o A365097         m += 1
%o A365097         if m == n:
%o A365097             m = 0
%o A365097             q += 1
%o A365097             a = digits(q,n).count(1)
%o A365097         elif m==1:
%o A365097             a += 1
%o A365097         elif m==2:
%o A365097             a -= 1
%o A365097         c += a
%o A365097         if c == k:
%o A365097             return k # _Chai Wah Wu_, Sep 28 2023
%Y A365097 Cf. A014778, A094798, A226238.
%K A365097 nonn,base
%O A365097 2,1
%A A365097 _Andrew Pope_, Aug 21 2023
%E A365097 a(11)-a(15) from _Amiram Eldar_, Aug 29 2023
%E A365097 a(16)-a(19) from _Chai Wah Wu_, Sep 29 2023
%E A365097 a(20)-a(25) from _Jon E. Schoenfield_, Sep 30 2023

%I A094797 #25 Nov 21 2025 13:01:21
%S A094797 1,2,21,301,4001,50001,600001,7000001,80000001,900000001,10000000001,
%T A094797 110000000001,1200000000001,13000000000001,140000000000001,
%U A094797 1500000000000001,16000000000000001,170000000000000001,1800000000000000001,19000000000000000001
%N A094797 Number of times 1 is used in writing out all numbers 1 through 10^n.
%H A094797 <a href="/index/Rec#order_03">Index entries for linear recurrences with constant coefficients</a>, signature (21,-120,100).
%F A094797 a(n) = n*10^(n-1) + 1.
%F A094797 From _Colin Barker_, May 23 2014: (Start)
%F A094797 a(n) = 21*a(n-1) - 120*a(n-2) + 100*a(n-3).
%F A094797 G.f.: -(99*x^2-19*x+1)/((x-1)*(10*x-1)^2). (End)
%F A094797 a(n) = A094798(A011557(n)). - _Michel Marcus_, Oct 03 2023
%F A094797 From _Elmo R. Oliveira_, Nov 21 2025: (Start)
%F A094797 E.g.f.: exp(x)*(1 + x*exp(9*x)).
%F A094797 a(n) = A053541(n) + 1 for n > 0. (End)
%t A094797 Table[ n*10^(n - 1) + 1, {n, 0, 17}] (* _Robert G. Wilson v_, Jun 15 2004 *)
%t A094797 LinearRecurrence[{21,-120,100},{1,2,21},20] (* _Harvey P. Dale_, Sep 07 2022 *)
%o A094797 (PARI) Vec(-(99*x^2-19*x+1)/((x-1)*(10*x-1)^2) + O(x^100)) \\ _Colin Barker_, May 23 2014
%Y A094797 Cf. A011557, A053541, A072290, A078427, A094798.
%K A094797 base,nonn,easy
%O A094797 0,2
%A A094797 _Lekraj Beedassy_, Jun 11 2004
%E A094797 More terms from _Robert G. Wilson v_, Jun 15 2004
%E A094797 Further terms from _Colin Barker_, May 23 2014

# Content is available under The OEIS End-User License Agreement: http://oeis.org/LICENSE
