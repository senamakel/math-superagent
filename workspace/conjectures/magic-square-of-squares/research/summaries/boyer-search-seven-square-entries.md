> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/boyer-search-seven-square-entries.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://www.multimagie.com/Search.pdf | converted from PDF -->

A search for 3x3 magic squares having more than six
square integers among their nine distinct integers.
Draft v2, By Christian Boyer, France, September 16th 2004
cboyer@club-internet.fr
www.multimagie.com/indexengl.htm
  “Martin  LaBar,  in  The  College  Mathematics  Journal
[January 1984, p.69], asked if a 3x3 magic square exists with
nine distinct square numbers. (…) Neither such a square nor
a proof of impossibility has been found. (…) I here offer $100
to  the  first  person  to  construct  such  a  square.  If  it  exists,  its
numbers are sure to be monstrously large.”
Martin Gardner, 1996

Today,  eight  years  after  this  quotation,  nobody  has  succeeded  in  winning  the  $100  of  this
Gardner’s challenge.
However, it is possible to construct a 3x3 square with nine square integers and only one bad
magic sum. The smallest example is the following square, first found independently by Lee
Sallows  and  Michael  Schweitzer.  All  the  rows  and  columns,  but  only  one  of  the  two
diagonals, have the same magic sum.

127²  46²  58²
2²  113²  94²
74²  82²  97²
(fig. 1)

Our problem, here, is to get the maximum number of square integers in a fully magic square:
the eight lines of the squares of our study will always have the same magic sum.

Six square integers
Andrew  Bremner,  Department  of  Mathematics,  Arizona  State  University,  demonstrated  in
2001  that  all  the  sixteen  possible  configurations  of  magic  squares  including  six  square
integers are possible.

x  x  x       x  x    x  x  x       x                     x             x       x  x
x  x       x     x               x  x  x    x  x  x    x  x  x    x  x  x       x  x
x          x  x       x  x  x    x     x    x  x  x    x  x       x     x    x     x
6.I    6.II    6.III    6.IV    6.V    6.VI    6.VII    6.VIII

      x          x          x       x          x  x    x     x       x  x    x     x
x     x    x  x  x    x  x  x    x     x    x  x          x  x    x                x
x  x  x       x  x    x  x       x  x  x    x     x    x     x    x  x  x    x  x  x
6.IX    6.X    6.XI    6.XII    6.XIII    6.XIV    6.XV    6.XVI
 (fig. 2)

 - A search for 3x3 magic squares having more than six square integers, by Christian Boyer, © 2004, page 2/5 -

Numerous  examples  with  six  square  integers  are  easy  to  find,  for  each  configuration.  For
example,  here  is  the  “smallest”  possible  magic  square  with  six  square  integers,  “smallest”
meaning  that  it  is  using  the  smallest  magic  sum.  This  example  belongs  to  the  Bremner’s
configuration 6.XV. The central cell is equal to 145 = 5·29
  265  1²  13²
7²  145  241
11²  17²  5²
(fig. 3)

Here are the two smallest examples using a square integer in the central cell. These examples
belong  to  the  configurations  6.VII  and  6.XIV.  There  is  an  easy  correspondence  between
squares of these two configurations, as mentioned by Bremner: that’s why these two different
squares are in fact very similar, using the same square integers, having one identical diagonal.
  889  697  17²    5²  1561  17²
5²  25²  35²    889  25²  19²
31²  553  19²    31²  -311  35²
(fig. 4)

And when two magic squares 3x3 have the same central cell, then they have the same magic
sum. The magic sum of a magic square 3x3 always equals three times the central cell.

Seven square integers
Up to symmetry (rotation and reflection), there are eight ways of selecting seven entries from
a 3x3 square. These are as follows:

x  x  x    x  x  x    x  x  x    x  x  x    x  x  x    x  x       x  x  x    x  x  x
   x       x  x       x  x  x       x  x    x  x  x    x  x  x    x     x    x     x
x  x  x    x     x    x          x  x          x          x  x    x     x    x  x
7.I    7.II    7.III    7.IV    7.V    7.VI    7.VII    7.VIII
(fig. 5)

Two results are already known about these configurations:

*[excerpt ends; 8889 characters not shown — see `research/sources/boyer-search-seven-square-entries.full.md`]*
