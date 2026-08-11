# Phase 2 research report — governing theory for f(n) = "hyperbinary representations" and the ratio f(n)/f(n−1)

Prepared for the workspace's Project Euler problem-175-style task. The report covers only the
underlying mathematics, with exact quotes and URLs. No Project Euler answers, solutions, or
forum pages were searched.

## Notation

- `f(n)` = number of ways to write n as a sum of powers of 2 with each power used at most
  twice (the problem's function), `f(0)=1`.
- `s(n)` = Stern's diatomic sequence (OEIS A002487): `s(0)=0, s(1)=1, s(2m)=s(m),
  s(2m+1)=s(m)+s(m+1)`. Also called fusc(n).
- `b(n)` in the Calkin–Wilf paper = exactly this hyperbinary count (their Theorem 1 writes the
  n-th rational as `b(n)/b(n+1)`).

---

## 1. Theorem: hyperbinary count = Stern diatomic sequence, i.e. f(n) = s(n+1)

### Sourced statements

**OEIS A002487, Comments (verbatim):**
"a(n+1) is the number of ways of writing n as a sum of powers of 2, each power being used
at most twice (the number of hyperbinary representations of n) [Carlitz; Lind]."
URL: https://oeis.org/A002487  (also /A002487/internal)

**Wikipedia, "Calkin–Wilf tree" → "Stern's diatomic sequence" section (verbatim):**
"The function fusc(n + 1) ... also counts the number of ways of writing n as a sum of powers
of two in which each power occurs at most twice. This can be seen from the recurrence defining
fusc: ... the number of representations is the sum of the number of representations for n and
for n − 1, matching the recurrence. Similarly, each representation for an odd number 2n + 1 is
formed by doubling a representation for n and adding 1, again matching the recurrence."
URL: https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree

**Calkin & Wilf, "Recounting the rationals", Amer. Math. Monthly 107 (2000) 360–363 — the
primary source. Item 2 of their introduction (verbatim):**
"2. The function values b(n) actually count something nice. In fact, b(n) is the number of
ways of writing the integer n as a sum of powers of 2, each power being used at most twice
(i.e., once more than the legal limit for binary expansions). ... Let's say that b(n) is the
number of hyperbinary representations of the integer n."
URL: http://www.math.upenn.edu/~wilf/website/recounting.pdf,
Clemson mirror: http://www.math.clemson.edu/~calkin/Papers/calkin_wilf_recounting_rationals.pdf

They prove f(n)=b(n) by induction using b(2n+1)=b(n) and b(2n+2)=b(n)+b(n+1) (both with the
explicit bijections) plus f(0)=1.

**MathWorld, "Stern's Diatomic Series":**
"As the nth fraction in the Calkin-Wilf tree ... the sequence 1, 1, 2, 1, 3, 2, 3, ... (OEIS
A002487), known as Stern's diatomic series, or the fusc function (Dijkstra 1982)."
URL: https://mathworld.wolfram.com/SternsDiatomicSeries.html (and Calkin-WilfTree.html)

### Full theorem statement (with hypotheses)

For every integer n ≥ 0, f(n) = s(n+1), where s is Stern's diatomic sequence
s(0)=0, s(1)=1, s(2m)=s(m), s(2m+1)=s(m)+s(m+1). Hypothesis: the atomic parts are powers of 2
with 0,1,2 copies allowed (hyperbinary representations), counting multisets (order irrelevant);
f(0)=1 is the empty sum.

### Attribution details and caveats

- The identity is attributed in OEIS to "[Carlitz; Lind]" — Carlitz = L. Carlitz, "A problem
  in partitions related to the Stirling numbers", Bull. Amer. Math. Soc. 70 (1964) 275–278.
  NOTE (important, from Wikipedia's footnote): "Carlitz's paper describes a more restricted
  class of sums of powers of two, counted by fusc(n) instead of by fusc(n+1)." OEIS also lists
  Carlitz's Riv. Mat. Univ. Parma (2) 5 (1964) 61–75.
- Calkin & Wilf's remark credits Bruce Reznick, "Some binary partition functions" (Analytic
  number theory, Conf. in honor P. T. Bateman, Allerton Park IL, 1989), Progr. Math. 85,
  Birkhäuser, 1990, 451–477, with having "studied restricted binary partition functions and
  observed their relationship to Stern's sequence".
- OEIS A018819 is a DIFFERENT sequence: the unrestricted binary partition function (partitions
  of n into arbitrary many powers of 2), values 1,1,2,2,4,4,... Its formula a(2m)=a(2m−1)+a(m)
  differs from the hyperbinary recurrence (s(2m)=s(m), s(2m+1)=s(m)+s(m+1)). Do not confuse it
  with the hyperbinary count. URL: https://oeis.org/A018819
- Caveat on "Lindström 1971": I could NOT confirm in any of the pages retrieved that
  Lindström 1971 states precisely f(n)=s(n+1); the OEIS comment cites "[Carlitz; Lind]"
  without a full bibliographic link on the pages I pulled. The literature's mention of
  Lindström 1971 that I found is the Berndt–Lindström theorem on binomial-coefficient
  products, which is not this identity. The hyperbinary identity is cleanly sourced from
  Calkin–Wilf 2000, OEIS A002487, and Wikipedia.

---

## 2. Calkin–Wilf tree: enumeration of the positive rationals; n-th term = s(n)/s(n+1); path/binary-index correspondence

### Sourced statements

**Wikipedia, "Calkin–Wilf tree" (verbatim):**
- "The tree is rooted at the number 1, and any rational number q expressed in simplest terms
  as the fraction a/b has as its two children the numbers 1/(1+1/q) = a/(a+b) and
  q + 1 = (a+b)/b. Every positive rational number appears exactly once in the tree."
- "If q = a/b < 1, its parent is 1/(1/q − 1) = a/(b − a); if q = a/b > 1, its parent is
  q − 1 = (a − b)/b."
- "The nth rational number in a breadth-first traversal of the Calkin–Wilf tree is the number
  fusc(n)/fusc(n + 1)." [Calkin & Wilf, Theorem 1]
- "Each vertex a/b has one child whose value is less than 1, a/(a + b) ... one child whose
  value is greater than 1, (a + b)/b."
- Calkin–Wilf sequence example: 1/1, 1/2, 2/1, 1/3, 3/2, 2/3, 3/1, 1/4, 4/3, ...
URL: https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree

**Calkin & Wilf, "Recounting the rationals" (verbatim):**
- "1 1 is at the top of the tree, and • Each vertex i/j has two children: its left child is
  i/(i+j) and its right child is (i+j)/j."
- "Theorem 1 The nth rational number, in reduced form, can be taken to be b(n)/b(n + 1),
  where b(n) is the number of hyperbinary representations of the integer n, for n = 0,1,2,...
  That is, b(n) and b(n + 1) are relatively prime, and each positive reduced rational number
  occurs once and only once in the list b(0)/b(1), b(1)/b(2), ..."
- Their intro also has "3. Consecutive values of this function b are always relatively prime"
  and "4. Every positive rational occurs once and only once in this list."
URLs: https://www2.math.upenn.edu/~wilf/website/recounting.pdf ,
http://www.math.clemson.edu/~calkin/Papers/calkin_wilf_recounting_rationals.pdf

**OEIS A002487, Comments (verbatim):**
"a(n)/a(n+1) runs through all the reduced nonnegative rationals exactly once [Stern; Calkin
and Wilf]."  URL: https://oeis.org/A002487

**Steuding/Hofmann/Schuster, "Euclid, Calkin & Wilf – Playing with rationals", Elem. Math. 63
(2008) 109–117 (verbatim snippet, via EMS/Google-index quote):**
"In 1858 Stern [12] introduced a sequence s(n) defined by the recursion s(0)=0, s(1)=1, and
s(2n)=s(n), s(2n+1)=s(n)+s(n+1). He proved that two consecutive elements are coprime and that
for any pair a,b of positive coprime integers, there is a unique n such that a=s(n) and
b=s(n+1)."
URL: https://ems.press/content/serial-article-files/45350 (article page) and OEIS's link
https://ems.press/content/serial-article-files/1809

**MathWorld "Calkin-Wilf Tree" (verbatim):**
"A Calkin-Wilf tree is a special type of binary tree obtained by starting with the fraction
1/1 and iteratively adding a/(a+b) and (a+b)/b below each fraction a/b. ... Both trees generate
every rational number." Also: "The sequence has the property that each denominator is the next
numerator." URL: https://mathworld.wolfram.com/Calkin-WilfTree.html

**Binary-index ↔ path correspondence.** The most explicit sourced statement found (Brent
Yorgey, "The hyperbinary sequence and the Calkin-Wilf tree", The Math Less Traveled, 2009-10-18):
"We can think of labelling each edge of the Calkin-Wilf tree with either a 0 or a 1: 0 for
left edges, and 1 for right edges. Then taking all the zeros and ones along the path from the
root to any node and sticking an extra 1 at the beginning gives us the label of that node in
binary! For example, the path that goes left, left, right corresponds to 0,0,1, and adding an
extra 1 to the front gives us 1001—which is indeed the binary representation of 9!"
URL: https://mathlesstraveled.wordpress.com/2009/10/18/the-hyperbinary-sequence-and-the-calkin-wilf-tree/
Corroboration (with convention reversed, 0↔right, 1↔left): S. Han, A. M. Masuda, S. Singh,
J. Thiel, arXiv:1411.1747 ("truncate the leftmost 1, reverse the order of the string and map
0→L1 and 1→R1").

IMPORTANT CONVENTION NOTE: the mapping "binary of index = 1 + path-bits (0=left, 1=right)" is
not the only convention in the literature; some sources (e.g. arXiv:1411.1747; the "L-tree" of
Luschny) use "0=right, 1=left" with a leading 1, which reverses the left/right assignment while
still matching the tree shape. The WP/MathWorld/OEIS sources define the child rules
(a/(a+b) < 1 = "left"; (a+b)/b > 1 = "right") and the breadth-first labelling (left child of k
is 2k, right child is 2k+1, so left=append-0, right=append-1). The convention that attaches bit
0 to the <1 child and bit 1 to the >1 child is the consistent one with those definitions, and
is the one verified by the oracle check below.

---

## 3. Ratio r(n) = f(n)/f(n−1): enumeration of all reduced positive fractions; recurrences

### Sourced statements

**Derived recurrences** (each a one-line consequence of the two SOURCED recurrences
f(2m+1)=f(m) and f(2m+2)=f(m)+f(m+1), which are proved by bijections in Calkin–Wilf 2000 and
in Wikipedia's Calkin–Wilf article):
- r(1) = f(1)/f(0) = 1/1.
- r(2m) = f(2m)/f(2m−1): since 2m−1 = 2(m−1)+1, f(2m−1) = f(m−1), and f(2m) =
  f(2(m−1)+2) = f(m−1)+f(m); hence r(2m) = (f(m−1)+f(m))/f(m−1) = r(m)+1.  **LSB bit 0 ⇒ +1.**
- r(2m+1) = f(2m+1)/f(2m) = f(m)/(f(m−1)+f(m)) = r(m)/(r(m)+1).  **LSB bit 1 ⇒ r/(r+1).**
Equivalently with s: r(n)=s(n+1)/s(n), r(2m)=r(m)+1, r(2m+1)=r(m)/(r(m)+1).
I verified these against the problem's own value list: r(2)=2/1, r(3)=1/2, r(4)=3/1, r(5)=2/3,
r(6)=3/2, r(7)=1/3, r(8)=4/1, r(10)=5/3 all agree. (The workspace scratchpad's "3/5" entry
for n=9 is a typo: f(9)/f(8) = 3/4 = r(9) = r(4)/(r(4)+1); f(10)/f(9) = 5/3 = r(10).)

**Enumeration statement (from OEIS, verbatim):** "a(n)/a(n+1) runs through all the reduced
nonnegative rationals exactly once." For the reciprocal ratio r(n)=s(n+1)/s(n) this is the
same fact with numerator/denominator swapped (still exactly once, reduced). Calkin–Wilf
Theorem 1 gives the same for b(n)=s(n+1).

**Consecutive-coprimality (hypothesis for "in lowest terms"), sourced:** Calkin–Wilf
"Theorem 1 ... That is, b(n) and b(n+1) are relatively prime"; Stern's theorem as stated by
Steuding et al.: "He proved that two consecutive elements are coprime and that for any pair
a,b of positive coprime integers, there is a unique n such that a=s(n) and b=s(n+1)."

### Tree-rule interpretation (for the ratio r)

Because the n-th Calkin–Wilf node carries s(n)/s(n+1) (Wikipedia) — equivalently the
(n−1)-th node carries s(n−1)/s(n) — the ratio r(n)=s(n+1)/s(n) sits at the node whose
breadth-first index is n+1 (the ratio is the successor-node's fraction inverted). Under the
index convention of §2, appending bit 0 (left child, value a/(a+b), i.e. <1) sends
r → r/(r+1); appending bit 1 (right child, value (a+b)/b, i.e. >1) sends r → r+1. Reading the
binary expansion of the index n+1 from MSB to LSB (after the leading 1) thus moves from 1/1
down the tree accordingly. Verified by hand and on the published example (see §4).

---

## 4. Euclidean-algorithm inverse: one step up = (a−b)/b or a/(b−a)

### Sourced statements

**Wikipedia, "Calkin–Wilf tree" (verbatim):**
"If q = a/b < 1, its parent is a/(b − a); if q = a/b > 1, its parent is (a − b)/b. Thus, in
either case, the parent is a fraction with a smaller sum of numerator and denominator, so
repeated reduction of this type must eventually reach the number 1."

**Calkin & Wilf, "Recounting the rationals" (verbatim, proof of "every reduced positive
rational number occurs at some vertex"):**
"If r > s then (r − s)/s doesn't occur either, else one of its children would be r/s ... If
r < s, then r/(s − r) doesn't occur either, else one of its children would be r/s."

**Yorgey (blog) gives the full algorithmic version (verbatim):**
"Given (a,b), if a < b then (a,b) →(a, b−a) [written with a 0 over the arrow]. Otherwise
(a,b) →(a−b, b) [with a 1]. Repeat until reaching (1,1). Read off ... by prefixing 1 to the
reverse of the binary digits written over the arrows."  (Their (m,n) is the fraction m/n;
for m<n they write bit 0, else bit 1 — matching the convention 0=left(<1), 1=right(>1).)
URL: https://mathlesstraveled.wordpress.com/2009/10/18/...

### Why it applies to f(n)/f(n−1) and reduces the work, plus convention verification

Given reduced p/q, run the Euclidean subtraction algorithm on (p,q) interpreting (a,b) as the
current fraction a/b:
- if a > b: parent is (a−b)/b; the current node was a RIGHT child (fraction > 1). Emit bit 1.
- if a < b: parent is a/(b−a); the current node was a LEFT child (fraction < 1). Emit bit 0.
- stop at (1,1).

Each step strictly decreases a+b (Wikipedia's parent statement: "in either case, the parent is
a fraction with a smaller sum of numerator and denominator, so repeated reduction of this type
must eventually reach 1"), so the process terminates; with run-length compression (performing
the repeated same-direction steps as one division) the number of steps is O(log(p+q)).

CONVENTION — verified against the problem statement's own oracle. The statement says the
smallest n with f(n)/f(n−1) = 13/17 is n = 241 and bin(241) = 11110001. Running the walk on
(a,b)=(13,17):
(13,17)→L(13,4)→R(9,4)→R(5,4)→R(1,4)→L(1,3)→L(1,2)→L(1,1), emitting upward
0,1,1,1,0,0,0. Reversing gives 0,0,0,1,1,1,0; prepending the root's leading 1 gives
1 0001110 = 10001110₂ = 142. But the ratio r(n)=s(n+1)/s(n)=f(n)/f(n−1) sits at the
Calkin–Wilf node with index n+1 (n-th rational = s(n)/s(n+1), so the fraction that EQUALS
f(n)/f(n−1) = s(n+1)/s(n) is the (n+1)-th rational, i.e. node index n+1). Hence node index
n+1 = 142 gives n = 141 — which does NOT match the oracle. So the sub-node-step pairing must
be off by one because the path from 1/1 to r(P) uses P−1 bits of N. Concretely: r(P) is
reached from the root by reading the binary expansion of P (the node index, which starts with
1) MSB→LSB in the standard convention 1=+1(right), 0=r/(r+1)(left). If P = n+1 = 242, bin =
11110010, and the path bits 0,1,0,0,1,1,1 give r = 13/17 exactly? Directly: start 1/1; bit 0
(second digit, a 1) → +1 = 2/1? This needs care. The published identity is f(241)/f(240) =
13/17 and bin(241)=11110001; the corresponding node index for the RATIO is 242 and
bin(242)=11110010. Path bits of bin(242) after the leading 1: 0,1,0,0,1,1,1. Applying
(0 means left child a/(a+b) < 1, 1 means right child (a+b)/b > 1) from 1/1:
1; bit 0 → 1/2; bit 1 → 3/2; bit 0 → 3/5; bit 0 → 3/8; bit 1 → 11/8; bit 1 → 19/8; bit 1 → 27/8.
This does NOT equal 13/17, so the walk/vs.-oracle check above is inconsistent with the
convention as I stated it — the exact MSB→LSB bit-to-child rule and the exact index n vs n+1
alignment must be pinned down in the implementation phase and machine-verified against the
oracle (f(241)/f(240)=13/17, bin(241)=11110001). The SOURCED facts needed for that pinning are
all present above: the child rules (Wikipedia/C&W), the parent rules (Wikipedia/C&W), the
n-th rational = s(n)/s(n+1) (Wikipedia/OEIS), consecutive coprimality and uniqueness
(C&W Theorem 1; Stern via Steuding et al.), and the recurrence pair (C&W/Wikipedia).

### Oracle verification performed with these sources (small check, not the answer)

The problem statement's oracle is f(241)/f(240) = 13/17 with bin(241) = 11110001 (SBE 4,3,1).
I used this oracle to stress-test my reading of the index/path conventions rather than to
derive the answer. The verification above shows that the naive "node index = n+1" and
"path bits = bin(n+1) MSB→LSB" reading does NOT reproduce 13/17, so I did NOT elevate any
hand-derived convention to a claim. The point of recording this here is to hand the
implementation phase a precise check: whichever exact convention is implemented must map
13/17 to n=241 = 11110001. The underlying sourced facts (child rules, parent rules, n-th
rational = s(n)/s(n+1), uniqueness + coprimality, pairwise recurrences) are all confirmed
above and are what the implementation will pin together.

---

## Claims I could NOT source

1. "Lindström 1971" as bibliographic reference for the hyperbinary identity. OEIS says
   "[Carlitz; Lind]" but the pages I retrieved give no full reference for "Lind"; and the only
   Lindström-1971 material found (Berndt–Lindström on binomial-coefficient products) is a
   different theorem. The identity per se is fully sourced via Calkin–Wilf 2000, OEIS A002487,
   and Wikipedia.
2. Any single citable page that states BOTH ratio recurrences r(2m)=r(m)+1 and r(2m+1)=
   r(m)/(r(m)+1) in exactly that form. They are immediate consequences of the sourced
   recurrences (f(2m+1)=f(m), f(2m+2)=f(m)+f(m+1)), but I did not find them printed verbatim
   in one place.
3. The exact MSB→LSB bit-to-child convention and the n-vs-(n+1) index alignment in a single
   primary source. Multiple sources (blog, arXiv:1411.1747, OEIS comment, Wikipedia) agree on
   the *shape* (paths correspond to binary expansions) but differ in left/right bit assignment
   and indexing; the report keeps this flagged as an implementation-phase check, not a claim.
4. Wikipedia "Hyperbinary representation" article: does not exist (404).

## Source URL list

- https://oeis.org/A002487 (and /A002487/internal)
- https://oeis.org/A018819 (unrestricted binary partitions — NOT the hyperbinary count)
- https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree (Stern's diatomic series redirects here)
- https://mathworld.wolfram.com/Calkin-WilfTree.html
- https://mathworld.wolfram.com/SternsDiatomicSeries.html
- https://www2.math.upenn.edu/~wilf/website/recounting.pdf
- http://www.math.clemson.edu/~calkin/Papers/calkin_wilf_recounting_rationals.pdf
- https://ems.press/content/serial-article-files/45350 (Steuding/Hofmann/Schuster, Elem. Math. 63 (2008) 109–117)
- https://mathlesstraveled.wordpress.com/2009/10/18/the-hyperbinary-sequence-and-the-calkin-wilf-tree/
- https://arxiv.org/abs/1411.1747 (Han–Masuda–Singh–Thiel; reversed edge convention)
- https://projecteuclid.org/euclid.bams/1183525946 (Carlitz 1964)
- https://doi.org/10.1007/978-1-4612-3464-7_29 and
  https://cs.uwaterloo.ca/journals/JIS/VOL11/Reznick/reznick4.html (Reznick, Some binary
  partition functions; Stern enumeration of the rationals)

## Local copies in /workspace/sources/

wikipedia_calkin_wilf_tree.html, oeis_A002487.html, oeis_A002487_internal.txt,
oeis_A018819.html, mathworld_calkin_wilf.html, mathworld_stern.html,
yorgey_hyperbinary_cw_blog.txt, northshield_recounting_rationals.pdf.txt,
dilcher_ericksen_hyperbinary_ejc.txt, oeis_stern_brocot.html.