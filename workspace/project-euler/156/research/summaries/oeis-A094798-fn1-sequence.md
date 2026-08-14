> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-A094798-fn1-sequence.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/search?q=A094798&fmt=text | converted from plain text -->

## What is in it

- Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/
- Content is available under The OEIS End-User License Agreement: http://oeis.org/LICENSE


## What it claims

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
%p A094798 nones:=proc(n) local nn,c,j: nn:=convert(n,base,10): c:=0: for j to nops(nn) do if nn[j]=1 then…

%I…

*[digest of a 15870 character source; every section, statement, and proof in full at `research/sources/oeis-A094798-fn1-sequence.full.md`]*
