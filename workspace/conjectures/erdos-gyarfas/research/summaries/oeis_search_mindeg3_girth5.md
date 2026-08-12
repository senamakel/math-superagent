> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis_search_mindeg3_girth5.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/search?q=minimum+degree+3+girth+at+least+5&fmt=text | converted from plain text -->

## What is in it

- Greetings from The On-Line Encyclopedia of Integer Sequences! http://oeis.org/
- Content is available under The OEIS End-User License Agreement: http://oeis.org/LICENSE


## What it claims

%I A008483 #170 Aug 10 2026 12:11:59
%S A008483 1,0,0,1,1,1,2,2,3,4,5,6,9,10,13,17,21,25,33,39,49,60,73,88,110,130,
%T A008483 158,191,230,273,331,391,468,556,660,779,927,1087,1284,1510,1775,2075,
%U A008483 2438,2842,3323,3872,4510
%N A008483 Number of partitions of n into parts >= 3.
%C A008483 a(0) = 1 because the empty partition vacuously has each part >= 3. - _Jason Kimberley_, Jan 11 2011
%C A008483 Number of partitions where the largest part occurs at least three times. - _Joerg Arndt_, Apr 17 2011
%C A008483 By removing a single part of size 3, an A026796 partition of n becomes an A008483 partition of n - 3.
%C A008483 For n >= 3 the sequence counts the isomorphism classes of authentication codes AC(2,n,n) with perfect secrecy and with largest probability 0.5 that an interceptor could deceive with a substituted message. - E. Keith Lloyd (ekl(AT)soton.ac.uk).
%C A008483 For n >= 1, also the number of regular graphs of degree 2. - _Mitch Harris_, Jun 22 2005
%C A008483 (1 + 0*x + 0*x^2 + x^3 + x^4 + x^5 + 2*x^6 + ...) = (1 + x + 2*x^2 + 3*x^3 + 5*x^4 + ...) * 1 / (1 + x +…

*[digest of a 8714 character source; every section, statement, and proof in full at `research/sources/oeis_search_mindeg3_girth5.full.md`]*
