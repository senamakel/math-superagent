<!-- source: https://oeis.org/search?q=%22equal+to+the+number+of%22+%22in+the+decimal+digits+of+all+numbers%22&fmt=text | converted from plain text -->

# Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/

Search: "equal to the number of" "in the decimal digits of all numbers"
Showing 1-10 of 11

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

%I A130428 #18 Jun 10 2026 19:53:05
%S A130428 0,9500000000,9628399986,9628399987,9628399988,9628399989,9628399990,
%T A130428 9628399991,9628399992,9628399993,9628399994,9628399995,10000000000,
%U A130428 19500000000,19628399986,19628399987,19628399988,19628399989
%N A130428 List of numbers n such that n is equal to the number of 6's in the decimal digits of all numbers <= n.
%C A130428 A finite sequence with 72 terms.
%H A130428 Graeme McRae, May 26 2007, <a href="/A130428/b130428.txt">Table of n, a(n) for n = 1..72</a> (full sequence)
%H A130428 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%e A130428 a(5)=9628399988 because the number of 6's in the decimal digits of the numbers from 0 to 9628399988 is 9628399988 and this is the 5th such number.
%Y A130428 Cf. A014778 for proof these sequences are finite; Also A101639, A101640, A101641, A130427, A130429, A130430, A130431; Cf. A130432 for the number of numbers in these sequences.
%K A130428 base,fini,full,nonn
%O A130428 1,2
%A A130428 _Graeme McRae_, May 26 2007

%I A130429 #18 Jun 10 2026 19:53:01
%S A130429 0,9465000000,9471736170,9500000000,9757536170,9965000000,9971736170,
%T A130429 10000000000,19465000000,19471736170,19500000000,19757536170,
%U A130429 19965000000,19971736170,20000000000,29465000000,29471736170
%N A130429 List of all numbers n such that n is equal to the number of 7's in the decimal digits of all numbers <= n.
%C A130429 A finite sequence with 49 terms.
%H A130429 Graeme McRae, May 26 2007, <a href="/A130429/b130429.txt">Table of n, a(n) for n = 1..49</a> (full sequence)
%H A130429 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%e A130429 a(5)=9757536170 because the number of 7's in the decimal digits of the numbers from 0 to 9757536170 is 9757536170 and this is the 5th such number.
%Y A130429 Cf. A014778 for proof these sequences are finite; Also A101639, A101640, A101641, A130427, A130428, A130430, A130431; Cf. A130432 for the number of numbers in these sequences.
%K A130429 base,fini,full,nonn
%O A130429 1,2
%A A130429 _Graeme McRae_, May 26 2007

%I A130430 #18 Jun 10 2026 19:52:58
%S A130430 0,9465000000,9486799989,9486799990,9486799991,9486799992,9486799993,
%T A130430 9486799994,9486799995,9486799996,9486799997,9497400000,9498399989,
%U A130430 9498399990,9498399991,9498399992,9498399993,9498399994,9498399995
%N A130430 List of numbers n such that n is equal to the number of 8's in the decimal digits of all numbers <= n.
%C A130430 A finite sequence with 344 terms.
%H A130430 Graeme McRae, May 26 2007, <a href="/A130430/b130430.txt">Table of n, a(n) for n = 1..344</a> (full sequence)
%H A130430 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%e A130430 a(5)=9486799991 because the number of 8's in the decimal digits of the numbers from 0 to 9486799991 is 9486799991 and this is the 5th such number.
%Y A130430 Cf. A014778 for proof these sequences are finite; Also A101639, A101640, A101641, A130427, A130428, A130429, A130431; Cf. A130432 for the number of numbers in these sequences.
%K A130430 base,fini,full,nonn
%O A130430 1,2
%A A130430 _Graeme McRae_, May 26 2007

%I A130427 #17 Jun 10 2026 19:52:55
%S A130427 0,10000000000,20000000000,30000000000,40000000000
%N A130427 Complete list of all 5 numbers n such that n is equal to the number of 5's in the decimal digits of all numbers <= n.
%H A130427 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%e A130427 a(5) = 40000000000 because the number of 5's in the decimal digits of the numbers from 0 to 40000000000 is 40000000000 and this is the 5th such number.
%Y A130427 Cf. A014778 for proof these sequences are finite; Also A101639, A101640, A101641, A130428, A130429, A130430, A130431; Cf. A130432 for the number of numbers in these sequences.
%K A130427 nonn,base,fini,full
%O A130427 1,2
%A A130427 _Graeme McRae_, May 26 2007

%I A130431 #11 Jun 10 2026 19:52:51
%S A130431 0,10000000000,20000000000,30000000000,40000000000,50000000000,
%T A130431 60000000000,70000000000,80000000000
%N A130431 Complete list of all 9 numbers n such that n is equal to the number of 9's in the decimal digits of all numbers <= n.
%H A130431 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%e A130431 a(5)=40000000000 because the number of 9's in the decimal digits of the numbers from 0 to 40000000000 is 40000000000 and this is the 5th such number.
%Y A130431 Cf. A014778 for proof these sequences are finite; Also A101639, A101640, A101641, A130427, A130428, A130429, A130430; Cf. A130432 for the number of numbers in these sequences.
%K A130431 base,fini,nonn,full
%O A130431 1,2
%A A130431 _Graeme McRae_, May 26 2007

%I A130432 #13 Jun 11 2026 00:58:52
%S A130432 84,14,36,48,5,72,49,344,9
%N A130432 For digit n from 1 to 9, a(n) = the number of numbers m such that m is equal to the number of n's in the decimal digits of all numbers <= m.
%C A130432 Note: sequences A101639, A101640 and A101641 are defined so that they exclude 0, so they have 13, 35 and 47 elements, respectively. This sequence counts all the zeros, so elements 2,3,4 of this sequence are 14,36,48.
%H A130432 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 784. See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%e A130432 a(3)=36 because there are 36 numbers m such that m is equal to the number of 3's in the decimal digits of all numbers <= m.
%Y A130432 See A014778 for proof that these sequences are finite and also A101639, A101640, A101641, A130427, A130428, A130429, A130430, A130431 for the numbers themselves.
%K A130432 base,fini,nonn,full
%O A130432 1,1
%A A130432 _Graeme McRae_, May 26 2007

%I A216398 #6 Sep 07 2012 05:05:28
%S A216398 22786974071,73737982962,372647999625,741999999540,100000000000,
%T A216398 2434703999430,1876917059570,15312327487352,360000000000
%N A216398 For digit n from 1 to 9, a(n) = the sum of all numbers m such that m is equal to the number of n's in the decimal digits of all numbers <= m.
%C A216398 Closely related to A130432. - _N. J. A. Sloane_, Sep 07 2012
%Y A216398 Cf. A014778, A101639, A101640, A101641, A130427, A130428, A130429, A130430, A130431, A130432.
%K A216398 nonn,base,fini,full
%O A216398 1,1
%A A216398 _V. Raman_, Sep 06 2012

%I A101640 #24 Jun 11 2026 00:58:47
%S A101640 371599983,371599984,371599985,371599986,371599987,371599988,
%T A101640 371599989,371599990,371599991,371599992,500000000,10000000000,
%U A101640 10371599983,10371599984,10371599985,10371599986,10371599987,10371599988
%N A101640 Positive integers n for which n = f(n), where f(n) is the total number of 3's required when writing out all numbers between 0 and n.
%C A101640 Related to a problem posed by Google and discussed on the MathWorld link.
%C A101640 Together with the b-file, this gives the complete list of all 35 positive numbers n such that n is equal to the number of 3's in the decimal digits of all numbers <= n. - Daniel Hirschberg (dan(AT)ics.uci.edu), May 05 2007
%H A101640 Daniel Hirschberg (dan(AT)ics.uci.edu), May 05 2007, <a href="/A101640/b101640.txt">Table of n, a(n) for n = 1..35</a>
%H A101640 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%H A101640 Mathworld, <a href="https://mathworld.wolfram.com/news/2004-10-13/google/">Problem 17 of Google Labs Aptitude Test Partially Answered</a>, MathWorld Headline News, October 13 2004.
%e A101640 a(1) = 371599983, since writing out all numbers from 0 to 371599983 requires that 371599983 3's be used and since 371599983 is the first such positive integer.
%e A101640 a(4) = 371599986 because the number of 3's in the decimal digits of the numbers from 1 to 371599986 is 371599986 and this is the 4th such number.
%Y A101640 Cf. A014778 for proof these sequences are finite; Also A101639, A101641, A130427, A130428, A130429, A130430, A130431; cf. A130432 for the number of numbers in these sequences.
%K A101640 nonn,base,fini,full
%O A101640 1,1
%A A101640 _Ryan Propper_, Dec 10 2004
%E A101640 More terms from Daniel Hirschberg (dan(AT)ics.uci.edu), May 05 2007

%I A101641 #29 Jun 11 2026 00:58:50
%S A101641 499999984,499999985,499999986,499999987,499999988,499999989,
%T A101641 499999990,499999991,499999992,499999993,500000000,10000000000,
%U A101641 10499999984,10499999985,10499999986,10499999987,10499999988,10499999989
%N A101641 Positive integers n for which n = f(n), where f(n) is the total number of 4's required when writing out all numbers between 0 and n.
%C A101641 Related to a problem posed by Google and discussed on the MathWorld link.
%C A101641 Together with the b-file, this gives the complete list of all 47 positive numbers n such that n is equal to the number of 4's in the decimal digits of all numbers <= n. - Daniel Hirschberg (dan(AT)ics.uci.edu), May 05 2007
%H A101641 Daniel Hirschberg (dan(AT)ics.uci.edu), May 05 2007, <a href="/A101641/b101641.txt">Table of n, a(n) for n = 1..47</a>
%H A101641 Tanya Khovanova and Gregory Marton, <a href="https://doi.org/10.1080/00029890.2025.2525050">Archive Labeling Sequences</a>, Amer. Math. Monthly 132(8) (2025) 780-787. See p. 783 (Table 2). See also <a href="https://arxiv.org/abs/2305.10357">arXiv:2305.10357</a> [math.HO], 2023. See p. 4.
%H A101641 Mathworld, <a href="https://mathworld.wolfram.com/news/2004-10-13/google/">Problem 17 of Google Labs Aptitude Test Partially Answered</a>, MathWorld Headline News, October 13 2004.
%F A101641 a(n) = 499999983 + n, n <= 10; a(n) = 500000000, n = 11
%e A101641 a(1) = 499999984, since writing out all numbers from 0 to 499999984 requires that 499999984 4's be used and since 499999984 is the first such positive integer.
%e A101641 a(4) = 499999987 because the number of 4's in the decimal digits of the numbers from 1 to 499999987 is 499999987 and this is the 4th such number.
%Y A101641 Cf. A014778 for proof these sequences are finite; Also A101639, A101640, A130427, A130428, A130429, A130430, A130431; cf. A130432 for the number of numbers in these sequences.
%K A101641 nonn,base,fini,full
%O A101641 1,1
%A A101641 _Ryan Propper_, Dec 11 2004
%E A101641 More terms from Daniel Hirschberg (dan(AT)ics.uci.edu), May 05 2007
%E A101641 Keyword added by _Charles R Greathouse IV_, Jul 22 2010

# Content is available under The OEIS End-User License Agreement: http://oeis.org/LICENSE
